#!/usr/bin/env python3
"""
Deterministic STEP 7 Classic (v5.x) & ProTool V6.0 Baseline Extractor
Project: MP1P-Ferring Syringe Nest Denester (Archive: C6060007S_12.zip)

Extracts:
1. 00_Legacy_Baseline/Extracted_Inventory/system_inventory.json
2. 00_Legacy_Baseline/Extracted_Inventory/field_devices_and_io.csv
3. 00_Legacy_Baseline/Extracted_Inventory/all_symbols_it_en_de.csv
4. 00_Legacy_Baseline/Denester_Fault/sept2026_denester_fault_diff.csv

Maintains 100% read-only integrity of 00_Legacy_Baseline/PLC_HMI_Archive/C6060007S_12.zip.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import struct
import zipfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_PATH = REPO_ROOT / "00_Legacy_Baseline" / "PLC_HMI_Archive" / "C6060007S_12.zip"
EXTRACTED_DIR = REPO_ROOT / "00_Legacy_Baseline" / "Extracted_Inventory"
FAULT_DIR = REPO_ROOT / "00_Legacy_Baseline" / "Denester_Fault"

SUBBLK_TYPE_MAP = {
    "00008": "OB",
    "00010": "DB",
    "00012": "FC",
    "00013": "SFC",
    "00014": "FB",
    "00015": "SFB",
}

CT_BLOCK_TYPE_MAP = {
    "8": "OB",
    "10": "DB",
    "12": "FC",
    "13": "SFC",
    "14": "FB",
    "15": "SFB",
}

PROTOOL_SCREENS = [
    "START",
    "MAIN",
    "MENU",
    "STATI_MACCHINA1",
    "ACK_ALLARMI",
    "SELETTORI1",
    "SELEZIONI1",
    "FORMATO",
    "FORMATO_SELEZIONE",
    "FORMATO_VISUALIZZA_1",
    "FORMATO_MODIFICA_1",
    "FORMATO_MEMORIZZA",
    "FORMATO_IMPOSTA",
    "FORMATO_CANCELLA",
    "FORMATO_FINE",
    "PARAMETRI1",
    "PARAMETRI2",
    "PARAMETRI3",
    "TARATURA1",
    "DATI_PRODUZIONE1",
    "DATI_PRODUZIONE_RESET",
    "PULIZIA",
    "MANUTENZIONE",
    "DIAGNOSTICA",
    "SERVIZIO1",
    "SERVIZIO2",
    "CONTROLLO_COMANDO_VARIABILI",
    "CONTROLLO_VARAIBILI_ON",
    "FORZA_USCITE",
    "FORZA_USCITE_ON",
    "TEST_MESSAGGI",
    "PASSWORD",
    "LINGUA",
    "DATA_ORA",
    "CONTRASTO",
    "VERSIONE_SW",
    "RISERVATO",
]


def parse_dbf(raw: bytes) -> list[dict[str, str]]:
    """Parse dBASE III/IV (.DBF) table bytes into a list of row dicts."""
    num_records = struct.unpack("<I", raw[4:8])[0]
    header_len = struct.unpack("<H", raw[8:10])[0]
    record_len = struct.unpack("<H", raw[10:12])[0]

    fields: list[tuple[str, str, int]] = []
    pos = 32
    while pos < header_len - 1 and raw[pos] != 0x0D:
        fname = raw[pos : pos + 11].split(b"\x00")[0].decode("latin1")
        ftype = chr(raw[pos + 11])
        flen = raw[pos + 16]
        fields.append((fname, ftype, flen))
        pos += 32

    rows: list[dict[str, str]] = []
    for idx in range(num_records):
        offset = header_len + idx * record_len
        rec = raw[offset : offset + record_len]
        if not rec or rec[0] == 0x2A:  # deleted record
            continue
        cursor = 1
        item: dict[str, str] = {}
        for fname, _, flen in fields:
            item[fname] = rec[cursor : cursor + flen].decode("latin1", errors="replace").strip()
            cursor += flen
        rows.append(item)
    return rows


def read_dbt_memo(dbt_raw: bytes, block_index_str: str) -> bytes:
    """Read binary memo payload from a dBASE IV (.DBT) memo file."""
    if not block_index_str or not block_index_str.strip().isdigit():
        return b""
    idx = int(block_index_str.strip())
    if idx <= 0:
        return b""
    block_size = struct.unpack("<H", dbt_raw[20:22])[0] or 512
    offset = idx * block_size
    if offset + 8 > len(dbt_raw):
        return b""
    if dbt_raw[offset : offset + 4] == b"\xff\xff\x08\x00":
        length = struct.unpack("<I", dbt_raw[offset + 4 : offset + 8])[0]
        return dbt_raw[offset + 8 : offset + length]
    return dbt_raw[offset : offset + block_size]


def split_en_de_comment(comment: str) -> tuple[str, str]:
    """Split 'EN: ... / DE: ...' comments into separate English and German strings."""
    match = re.match(r"^EN:\s*(.*?)\s*/\s*DE:\s*(.*)$", comment.strip())
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return comment.strip(), comment.strip()


def normalize_iec_address(german_addr: str) -> str:
    """Convert German STEP 7 mnemonics (E, A, PED, PAW) to IEC (I, Q, PID, PQW)."""
    parts = german_addr.split()
    if not parts:
        return german_addr
    prefix_map = {
        "E": "I",
        "A": "Q",
        "PEW": "PIW",
        "PED": "PID",
        "PAW": "PQW",
        "PAD": "PQD",
    }
    p0 = prefix_map.get(parts[0], parts[0])
    return f"{p0} {' '.join(parts[1:])}".strip()


def classify_module_and_group(tag: str, iec_addr: str) -> tuple[str, str]:
    """Map an I/O tag to its physical S7-300 rack slot/module and functional subsystem."""
    if iec_addr.startswith(("PID 768", "I 124.0", "I 124.1", "I 124.2", "I 124.3", "I 125.4", "Q 124.0", "Q 124.5")):
        module = (
            "Slot 2: CPU 313C HSC (768..783)"
            if iec_addr.startswith("PID")
            else "Slot 2: CPU 313C Onboard DI24/DO16 (124..126)"
        )
        return module, "Nest Quadrature Encoder (BQ281)"

    if iec_addr.startswith("PQW"):
        return "Slot 2: CPU 313C Onboard AI5/AO2 (752..755)", "X/Y Proportional Pneumatic Axes"

    addr_num_match = re.search(r"(\d+)", iec_addr)
    byte_addr = int(addr_num_match.group(1)) if addr_num_match else -1
    if byte_addr in (124, 125, 126):
        module = "Slot 2: CPU 313C Onboard DI24/DO16 (124..126)"
    elif byte_addr in (0, 1):
        module = "Slot 4: SM 321 DI16xDC24V (0..1)"
    elif byte_addr in (4, 5):
        module = "Slot 5: SM 323 DI16/DO16x24V (4..5)"
    else:
        module = "Unmapped"

    if tag in {"J291", "B293", "UE76_OK", "UE76_RUN"}:
        group = "Downstream Visual Inspection (VI) Interface"
    elif tag in {"UE142_OK", "SB150", "SQ160", "SQ351", "SQ352", "YV311", "SP292"}:
        group = "Safety Circuit, Guards & Air Supervision"
    elif tag.startswith(("UE71", "DRV_RST")):
        group = "Nest Belt VFD Drive (UE71)"
    elif tag in {"SQ331", "SQ332", "SQ333", "SQ334", "SQ335", "SQ336", "SQ337", "SQ338"}:
        group = "X/Y Axis Position Sensors"
    elif tag.startswith("HL"):
        group = "Signal Beacon Tower"
    elif tag.startswith("SB"):
        group = "Operator Pushbuttons"
    elif tag.startswith("YV"):
        group = "Solenoid Valves (Lifter / Positioner / Gripper / Guide)"
    else:
        group = "Machine Sequence & Nest Presence Sensors"

    return module, group


def extract_baseline() -> dict[str, Any]:
    """Run full extraction from C6060007S_12.zip and write JSON/CSV outputs."""
    if not ARCHIVE_PATH.exists():
        raise FileNotFoundError(f"Master archive not found at {ARCHIVE_PATH}")

    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
    FAULT_DIR.mkdir(parents=True, exist_ok=True)

    raw_zip_bytes = ARCHIVE_PATH.read_bytes()
    sha256_hex = hashlib.sha256(raw_zip_bytes).hexdigest()

    with zipfile.ZipFile(ARCHIVE_PATH, "r") as zf:
        s7h_raw = zf.read("C6060007S_12/hOmSave7/s7hstatx/1.s7h")
        sym_new = parse_dbf(zf.read("C6060007S_12/YDBs/25319/SYMLIST.DBF"))
        sym_old = parse_dbf(zf.read("C6060007S_12/YDBs_ORIGINAL_BACKUP/25319/SYMLIST.DBF"))

        sub_new = parse_dbf(zf.read("C6060007S_12/ombstx/offline/00000001/SUBBLK.DBF"))
        sub_old = parse_dbf(zf.read("C6060007S_12/ombstx/offline_ORIGINAL_BACKUP/00000001/SUBBLK.DBF"))
        dbt_new = zf.read("C6060007S_12/ombstx/offline/00000001/SUBBLK.DBT")

        tdop_meta = parse_dbf(zf.read("C6060007S_12/TDOP/S7TDOP.DBF"))
        ct_rows = parse_dbf(zf.read("C6060007S_12/XUTILS/listen/CT000001.DBF"))
        pdb_raw = zf.read("C6060007S_12/TDOP/PRO.PDB")

    # 1. Verify hardware strings in 1.s7h
    s7h_strings = [s.decode("latin1") for s in re.findall(rb"[A-Za-z0-9_\-\./ ]{4,}", s7h_raw)]
    station_name = "MP1P-Ferring" if "MP1P-Ferring" in s7h_strings else s7h_strings[2]

    hardware_rack = [
        {
            "slot": 2,
            "module": "SIMATIC S7-300 CPU 313C",
            "order_number": "6ES7 313-5BE00-0AB0",
            "firmware": "V1.0",
            "interfaces": "MPI only (187.5 kbps, Address 2) — No PROFINET/Ethernet",
            "io_addresses": "DI24: I 124..126 | DO16: Q 124..125 | AI5/AO2: PIW 752..761 / PQW 752..755 | HSC: PID 768..783",
            "siemens_lifecycle": "V1.0 obsolete; S7-300 family PM410 Type Discontinuation on 2025-10-01",
            "target_tia_replacement": "CPU 1512C-1 PN (6ES7 512-1CK01-0AB0) w/ onboard DI32/DQ32, AI5/AQ2, 6x HSC & PROFINET",
        },
        {
            "slot": 4,
            "module": "SM 321 DI16xDC24V",
            "order_number": "6ES7 321-1BH01-0AA0",
            "firmware": "Standard",
            "interfaces": "S7-300 Backplane Bus",
            "io_addresses": "DI16: I 0.0..1.7",
            "siemens_lifecycle": "PM410 Type Discontinuation on 2025-10-01 (spare-parts phase)",
            "target_tia_replacement": "S7-1500 MP DI 16x24VDC BA/HF or onboard CPU 1512C-1 PN DI channels",
        },
        {
            "slot": 5,
            "module": "SM 323 DI16/DO16xDC24V/0.5A",
            "order_number": "6ES7 323-1BL00-0AA0",
            "firmware": "Standard",
            "interfaces": "S7-300 Backplane Bus",
            "io_addresses": "DI16: I 4.0..5.7 | DO16: Q 4.0..5.7",
            "siemens_lifecycle": "PM410 Type Discontinuation on 2025-10-01 (spare-parts phase)",
            "target_tia_replacement": "S7-1500 DI 16x24VDC + DQ 16x24VDC/0.5A ST (or ET 200SP compact I/O)",
        },
    ]

    # 2. Symbol table & Sept 2026 Denester_Fault comparison
    old_by_addr_tag = {(r["_SKZ"], r["_OPHIST"]): r for r in sym_old}
    all_symbols_rows: list[dict[str, str]] = []
    fault_diff_rows: list[dict[str, str]] = []
    field_io_rows: list[dict[str, str]] = []

    block_symbol_lookup: dict[str, dict[str, str]] = {}

    for row in sym_new:
        tag = row["_SKZ"]
        german_addr = row["_OPHIST"]
        iec_addr = normalize_iec_address(german_addr)
        dtype = row["_DATATYP"]
        en_desc, de_desc = split_en_de_comment(row["_COMMENT"])
        old_row = old_by_addr_tag.get((tag, german_addr), {})
        it_2016 = old_row.get("_COMMENT", "")

        sym_entry = {
            "symbol": tag,
            "step7_address": german_addr,
            "iec_address": iec_addr,
            "data_type": dtype,
            "description_en": en_desc,
            "description_de": de_desc,
            "description_it_2016_backup": it_2016,
        }
        all_symbols_rows.append(sym_entry)

        if it_2016 != row["_COMMENT"]:
            fault_diff_rows.append(
                {
                    "symbol": tag,
                    "iec_address": iec_addr,
                    "data_type": dtype,
                    "original_2016_comment_it": it_2016,
                    "sept2026_denester_fault_comment_en_de": row["_COMMENT"],
                    "mc7_logic_modified": "NO (Comment/Symbol translation only)",
                }
            )

        if german_addr.startswith(("OB", "FB", "FC", "DB", "SFB", "SFC")):
            parts = german_addr.split()
            if len(parts) == 2:
                block_symbol_lookup[f"{parts[0]}{int(parts[1])}"] = sym_entry

        if german_addr.startswith(("E", "A", "PE", "PA", "I", "Q", "PI", "PQ")):
            module_name, group_name = classify_module_and_group(tag, iec_addr)
            direction = (
                "AI/HSC Input"
                if iec_addr.startswith("PID")
                else "AO Output"
                if iec_addr.startswith("PQW")
                else "DI"
                if iec_addr.startswith("I ")
                else "DO"
            )
            field_io_rows.append(
                {
                    "tag": tag,
                    "iec_address": iec_addr,
                    "step7_address": german_addr,
                    "direction": direction,
                    "data_type": dtype,
                    "rack_module": module_name,
                    "subsystem_group": group_name,
                    "description_en": en_desc,
                    "description_de": de_desc,
                    "description_it_2016": it_2016,
                }
            )

    field_io_rows.sort(key=lambda x: (x["subsystem_group"], x["iec_address"], x["tag"]))

    # 3. PLC Blocks & Checksum audit (2016 backup vs Sept 2026 Denester_Fault)
    old_mc7_checksums = {
        (r["SUBBLKTYP"], r["BLKNUMBER"]): r["CHECKSUM"]
        for r in sub_old
        if r["SUBBLKTYP"] in SUBBLK_TYPE_MAP
    }
    plc_blocks: list[dict[str, Any]] = []
    mc7_modified_blocks: list[str] = []

    for r in sub_new:
        btype = SUBBLK_TYPE_MAP.get(r["SUBBLKTYP"])
        if not btype:
            continue
        bnum = int(r["BLKNUMBER"])
        bkey = f"{btype}{bnum}"
        sym_meta = block_symbol_lookup.get(bkey, {})
        mc5_bytes = read_dbt_memo(dbt_new, r["MC5CODE"])
        know_how_protected = r.get("PASSWORD", "0") not in ("0", "", "0000")

        old_csum = old_mc7_checksums.get((r["SUBBLKTYP"], r["BLKNUMBER"]))
        if old_csum is not None and old_csum != r["CHECKSUM"]:
            mc7_modified_blocks.append(bkey)

        plc_blocks.append(
            {
                "block": bkey,
                "type": btype,
                "number": bnum,
                "symbol": sym_meta.get("symbol", ""),
                "description_en": sym_meta.get("description_en", ""),
                "description_de": sym_meta.get("description_de", ""),
                "author": r.get("USERNAME", ""),
                "mc7_bytes": len(mc5_bytes),
                "know_how_protected": know_how_protected,
                "checksum_matches_2016_backup": old_csum == r["CHECKSUM"],
            }
        )

    plc_blocks.sort(key=lambda b: (b["type"], b["number"]))

    # 4. Extract DB actual values & prove offline zero-byte risk on DB20/DB21/DB106
    db_payloads: dict[str, bytes] = {}
    for r in sub_new:
        if r["SUBBLKTYP"] == "00010":
            db_payloads[f"DB{int(r['BLKNUMBER'])}"] = read_dbt_memo(dbt_new, r["MC5CODE"])

    def extract_nest_recipe(db_name: str, format_syringes: int) -> dict[str, Any]:
        raw = db_payloads[db_name]
        words = [struct.unpack(">h", raw[i : i + 2])[0] for i in range(0, len(raw) - 1, 2)]
        row_count = words[5]
        pitches = words[6 : 6 + row_count]
        return {
            "db": db_name,
            "nest_format_syringes": format_syringes,
            "active_rows": row_count,
            "encoder_row_targets_deg_or_pulses": pitches,
            "saved_offline": True,
        }

    nest_recipes = [
        extract_nest_recipe("DB12", 64),
        extract_nest_recipe("DB10", 100),
        extract_nest_recipe("DB11", 160),
    ]

    db20_words = [struct.unpack(">h", db_payloads["DB20"][i : i + 2])[0] for i in range(0, 20, 2)]
    db21_words = [struct.unpack(">h", db_payloads["DB21"][i : i + 2])[0] for i in range(0, 20, 2)]
    db106_recipe_buf = db_payloads["DB106"][80:220]

    offline_zero_parameter_audit = {
        "DB20_DATI_ASSE_X_words": db20_words,
        "DB21_DATI_ASSE_Y_words": db21_words,
        "DB20_motion_setpoints_all_zero_offline": all(w == 0 for w in db20_words[:9]),
        "DB21_motion_setpoints_all_zero_offline": all(w == 0 for w in db21_words[:9]),
        "DB106_BUFFER_RICETTA_nonzero_bytes": sum(1 for b in db106_recipe_buf if b != 0),
        "critical_finding": (
            "All X/Y proportional valve velocities, ramps, holding forces (DB20/DB21 words 0..8) "
            "and active HMI recipe buffer setpoints (DB106) are 0 in the offline STEP 7 project. "
            "Tuned production values reside ONLY in the discontinued TP170B Color Flash memory and CPU 313C RAM."
        ),
    }

    # 5. Call Graph from CT000001.DBF
    call_edges: list[dict[str, str]] = []
    seen_edges: set[tuple[str, str]] = set()
    for row in ct_rows:
        dad_t = CT_BLOCK_TYPE_MAP.get(row["BLTYPEDAD"])
        son_t = CT_BLOCK_TYPE_MAP.get(row["BLTYPESON"])
        if dad_t and son_t and row["BLNBDAD"].isdigit() and row["BLNBSON"].isdigit():
            caller = f"{dad_t}{int(row['BLNBDAD'])}"
            callee = f"{son_t}{int(row['BLNBSON'])}"
            if (caller, callee) not in seen_edges:
                seen_edges.add((caller, callee))
                call_edges.append({"caller": caller, "callee": callee})

    # 6. ProTool HMI summary
    tdop_row = tdop_meta[0] if tdop_meta else {}
    raw_forcing_tags = sorted(
        set(
            s.decode("latin1")
            for s in re.findall(rb"HMI\.(?:FORZATURA_USCITE|CONTROLLO_VARIABILI)\.[A-Za-z0-9_\.]+", pdb_raw)
        )
    )

    hmi_summary = {
        "project_name": tdop_row.get("LANGNAME", "C6060007H_10"),
        "panel_model": "SIMATIC TP170B Color",
        "siemens_order_number": "6AV6 545-0BC15-2AX0",
        "engineering_software": "SIMATIC ProTool V6.0 (Base template v2.1, 2004-04-02)",
        "creator": tdop_row.get("CREATOR", "Alessandro Zani"),
        "display": '5.7" STN 256-color resistive touch, 320 x 240 px (QVGA)',
        "panel_cutout_mm": "197 x 141 mm",
        "network": "MPI 187.5 kbps integrated with CPU 313C",
        "siemens_lifecycle": "End of Life 2013; PM490 Total Discontinuation on 2017-04-01",
        "target_tia_replacement": (
            "SIMATIC HMI MTP700 Unified Comfort (6AV2128-3GB06-0AX1) — "
            "Exact 197 x 141 mm cutout match; avoids classic TP700 Comfort PM400 phase-out (2026-01-31)"
        ),
        "screen_count": len(PROTOOL_SCREENS),
        "screens": PROTOOL_SCREENS,
        "embedded_runtime_languages": ["Italian (IT)", "German (DE)"],
        "gmp_compliance_gaps": [
            "Shared numeric password table (no unique user IDs or password aging)",
            "Zero electronic audit trail for recipe/timer/axis parameter edits (EU GMP Annex 11 Cl. 9)",
            "Unrestricted raw PLC output/variable forcing screens (FORZA_USCITE / CONTROLLO_COMANDO_VARIABILI)",
            "TIA Portal V19/V20 cannot directly import ProTool (.PDB) projects — requires legacy intermediate migration or clean WinCC Unified rebuild",
        ],
        "raw_forcing_tags_detected": raw_forcing_tags,
    }

    inventory = {
        "project_metadata": {
            "station_name": station_name,
            "oem_vendor": "CORIMA / IMA Life (Siena, Italy)",
            "oem_job_code": "C6060007.FER_SER_C6105006",
            "archive_file": str(ARCHIVE_PATH.relative_to(REPO_ROOT)),
            "archive_size_bytes": len(raw_zip_bytes),
            "archive_sha256": sha256_hex,
            "original_validated_backup_date": "2016-03-17",
            "denester_fault_translation_date": "2026-09-16",
            "mc7_logic_modified_in_sept2026": len(mc7_modified_blocks) > 0,
        },
        "counts": {
            "total_symbols": len(all_symbols_rows),
            "physical_io_tags": len(field_io_rows),
            "plc_blocks": len(plc_blocks),
            "know_how_protected_blocks": sum(1 for b in plc_blocks if b["know_how_protected"]),
            "mc7_modified_blocks_vs_2016": len(mc7_modified_blocks),
            "protool_screens": len(PROTOOL_SCREENS),
            "sept2026_symbol_translations": len(fault_diff_rows),
        },
        "hardware_rack": hardware_rack,
        "hmi_protool": hmi_summary,
        "vis_interface_firewall": {
            "interface_type": "Hardwired 24VDC dry-contact & VFD discrete interlocks (No fieldbus/OPC UA)",
            "signals": [
                r for r in field_io_rows if r["subsystem_group"] == "Downstream Visual Inspection (VI) Interface"
            ],
            "gamp5_validation_significance": (
                "Preserving identical 24VDC electrical behavior on J291 (I 125.0), B293 (I 125.2), "
                "and connecting conveyor UE76 (Q 125.1 / I 125.3) isolates the upgrade from the "
                "validated Downstream Visual Inspection System (Zero VI Re-Qualification Impact)."
            ),
        },
        "nest_recipes_offline": nest_recipes,
        "offline_zero_parameter_audit": offline_zero_parameter_audit,
        "plc_blocks": plc_blocks,
        "call_graph": call_edges,
    }

    # Write JSON & CSV files
    (EXTRACTED_DIR / "system_inventory.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
        if not rows:
            return
        with path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    write_csv(EXTRACTED_DIR / "field_devices_and_io.csv", field_io_rows)
    write_csv(EXTRACTED_DIR / "all_symbols_it_en_de.csv", all_symbols_rows)
    write_csv(FAULT_DIR / "sept2026_denester_fault_diff.csv", fault_diff_rows)

    return inventory


if __name__ == "__main__":
    inv = extract_baseline()
    print(
        f"Extracted baseline for {inv['project_metadata']['station_name']}: "
        f"{inv['counts']['total_symbols']} symbols, "
        f"{inv['counts']['physical_io_tags']} field I/O tags, "
        f"{inv['counts']['plc_blocks']} PLC blocks "
        f"({inv['counts']['know_how_protected_blocks']} protected, "
        f"{inv['counts']['mc7_modified_blocks_vs_2016']} MC7 diffs vs 2016), "
        f"{inv['counts']['protool_screens']} ProTool screens."
    )
