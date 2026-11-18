#!/usr/bin/env python3
"""
Unpacks and reorganizes C6060007S_12.zip ("Denester_Fault" STEP 7 + ProTool project)
into clean, human-browsable folders under 00_Legacy_Baseline/Denester_Fault/:

  01_VAT1_Fault_Diagnostic_Table/  -> Extracted Sept 2026 VAT_1 watch table (CSV + TIA TSV)
  02_PLC_DataBlocks_Source/        -> Readable .db STRUCT source files for DB10..DB106
  03_PLC_Logic_Blocks_Docs/        -> Readable interfaces, CO.RI.M.A. headers & network titles (OB/FB/FC)
  04_ProTool_HMI_TP170B/           -> ProTool TP170B Color project (PRO.PDB) + screens & HMI tags CSVs
  05_STEP7_Clean_Project/          -> Active STEP 7 v5.7 project (C6060007.s7p) without backup clutter
  06_Original_2016_Backup/         -> Separated 2016 ORIGINAL_BACKUP folders + symbol diff CSV
"""

from __future__ import annotations

import csv
import re
import shutil
import zipfile
from pathlib import Path

from tools.extract_s7_baseline import (
    ARCHIVE_PATH,
    FAULT_DIR,
    PROTOOL_SCREENS,
    normalize_iec_address,
    parse_dbf,
    read_dbt_memo,
    split_en_de_comment,
)

VAT_AREA_MAP = {
    ("2", "1"): ("I", "BOOL"),
    ("3", "1"): ("Q", "BOOL"),
    ("4", "1"): ("M", "BOOL"),
    ("4", "2"): ("MB", "BYTE"),
    ("4", "3"): ("MW", "WORD"),
    ("4", "4"): ("MD", "DWORD"),
    ("5", "2"): ("DBB", "BYTE"),
    ("8", "0"): ("T", "TIMER"),
}


def parse_vat1_entries(vat_addinfo: str, sym_by_name: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    """Parse STEP 7 VAT_1 (SUBBLKTYP 00027) ADDINFO string into structured watch rows."""
    pattern = re.compile(
        r"(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+(?:[A-Z0-9#]+\s+)?V52_Beginn\s+([^\"]+?)\s*\""
    )
    rows: list[dict[str, str]] = []
    for idx, match in enumerate(pattern.finditer(vat_addinfo), start=1):
        area, width, byte_no, bit_no, db_no, sym_name = match.groups()
        sym_clean = sym_name.strip()
        prefix, dtype = VAT_AREA_MAP.get((area, width), ("M", "BOOL"))
        if prefix == "DBB":
            iec_addr = f"DB{db_no}.DBB {byte_no}"
        elif prefix == "T":
            iec_addr = f"T {byte_no}"
        elif dtype == "BOOL":
            iec_addr = f"{prefix} {byte_no}.{bit_no}"
        else:
            iec_addr = f"{prefix} {byte_no}"

        lookup_key = sym_clean.lstrip("^")
        meta = sym_by_name.get(lookup_key, {})
        en_desc, de_desc = split_en_de_comment(meta.get("_COMMENT", ""))
        rows.append(
            {
                "row": str(idx),
                "symbol": sym_clean,
                "iec_address": iec_addr,
                "data_type": dtype,
                "description_en": en_desc or "Sequence / Diagnostic variable",
                "description_de": de_desc or "Schrittketten- / Diagnosevariable",
            }
        )
    return rows


def clean_comment_blob(raw: bytes) -> list[str]:
    """Extract readable header lines and network titles from SUBBLKTYP 00017/00018/00019."""
    chunks = [
        p.decode("latin1", errors="replace").strip()
        for p in re.split(rb"[\x00-\x08\x0b-\x1f]+", raw)
        if len(p.strip()) >= 3
    ]
    cleaned: list[str] = []
    for c in chunks:
        if c == "commento revisioni":
            continue
        if c.endswith("*c") and c.startswith("*"):
            c = c[:-1]
        elif c.endswith("c") and c.startswith("***"):
            c = c[:-1]
        cleaned.append(c)
    return cleaned


def unpack_and_organize() -> dict[str, int]:
    """Unpack C6060007S_12.zip into clean, logical subfolders under 00_Legacy_Baseline/Denester_Fault/."""
    vat_dir = FAULT_DIR / "01_VAT1_Fault_Diagnostic_Table"
    db_dir = FAULT_DIR / "02_PLC_DataBlocks_Source"
    blk_dir = FAULT_DIR / "03_PLC_Logic_Blocks_Docs"
    hmi_dir = FAULT_DIR / "04_ProTool_HMI_TP170B"
    s7_dir = FAULT_DIR / "05_STEP7_Clean_Project"
    bak_dir = FAULT_DIR / "06_Original_2016_Backup"

    for d in (vat_dir, db_dir, blk_dir, hmi_dir, s7_dir, bak_dir):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(ARCHIVE_PATH, "r") as zf:
        sym_new = parse_dbf(zf.read("C6060007S_12/YDBs/25319/SYMLIST.DBF"))
        sub_new = parse_dbf(zf.read("C6060007S_12/ombstx/offline/00000001/SUBBLK.DBF"))
        dbt_new = zf.read("C6060007S_12/ombstx/offline/00000001/SUBBLK.DBT")
        pdb_raw = zf.read("C6060007S_12/TDOP/PRO.PDB")

        # Unpack files cleanly into 04_ProTool_HMI_TP170B, 05_STEP7_Clean_Project, and 06_Original_2016_Backup
        for member in zf.infolist():
            if member.is_dir():
                continue
            rel_name = member.filename  # starts with C6060007S_12/...
            payload = zf.read(member.filename)

            if "/offline_ORIGINAL_BACKUP/" in rel_name or "/YDBs_ORIGINAL_BACKUP/" in rel_name:
                sub_rel = rel_name.split("C6060007S_12/", 1)[1]
                dest = bak_dir / sub_rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(payload)
            else:
                dest = s7_dir / rel_name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(payload)

                if rel_name.startswith("C6060007S_12/TDOP/"):
                    tdop_rel = rel_name.split("C6060007S_12/TDOP/", 1)[1]
                    hmi_dest = hmi_dir / "TDOP_Project" / tdop_rel
                    hmi_dest.parent.mkdir(parents=True, exist_ok=True)
                    hmi_dest.write_bytes(payload)

    # Move sept2026_denester_fault_diff.csv copy into 06_Original_2016_Backup as well for convenience
    diff_csv = FAULT_DIR / "sept2026_denester_fault_diff.csv"
    if diff_csv.exists():
        shutil.copy2(diff_csv, bak_dir / "sept2026_denester_fault_diff.csv")

    sym_by_name = {r["_SKZ"]: r for r in sym_new}
    block_sym_map: dict[str, dict[str, str]] = {}
    for r in sym_new:
        parts = r["_OPHIST"].split()
        if len(parts) == 2 and parts[0] in {"OB", "FB", "FC", "DB", "SFB", "SFC"} and parts[1].isdigit():
            block_sym_map[f"{parts[0]}{int(parts[1])}"] = r

    # 1. Export VAT_1 Fault Diagnostic Watch Table (created in Sept 2026 Denester_Fault)
    vat_rows: list[dict[str, str]] = []
    for r in sub_new:
        if r["SUBBLKTYP"] == "00027":
            add_txt = read_dbt_memo(dbt_new, r["ADDINFO"]).decode("latin1", errors="replace")
            vat_rows = parse_vat1_entries(add_txt, sym_by_name)

    with (vat_dir / "VAT1_Denester_Fault_WatchTable.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["row", "symbol", "iec_address", "data_type", "description_en", "description_de"])
        writer.writeheader()
        writer.writerows(vat_rows)

    with (vat_dir / "VAT1_TIA_Portal_WatchTable.tsv").open("w", newline="", encoding="utf-8") as fh:
        fh.write("Name\tAddress\tDisplay format\tComment\n")
        for vr in vat_rows:
            fmt = "Bool" if vr["data_type"] == "BOOL" else "Hex"
            fh.write(f"{vr['symbol']}\t%{vr['iec_address'].replace(' ', '')}\t{fmt}\tEN: {vr['description_en']} / DE: {vr['description_de']}\n")

    # 2. Export Readable DB Source Declarations (.db)
    db_structs = {int(r["BLKNUMBER"]): read_dbt_memo(dbt_new, r["MC5CODE"]).decode("latin1", errors="replace") for r in sub_new if r["SUBBLKTYP"] == "00006"}
    db_count = 0
    for db_num, struct_txt in sorted(db_structs.items()):
        bkey = f"DB{db_num}"
        sym_info = block_sym_map.get(bkey, {})
        sym_name = sym_info.get("_SKZ", bkey)
        comment = sym_info.get("_COMMENT", "")
        safe_sym = re.sub(r"[^A-Za-z0-9_]+", "_", sym_name)
        out_file = db_dir / f"{bkey}_{safe_sym}.db"
        out_file.write_text(
            f'DATA_BLOCK "{sym_name}" // {bkey} — {comment}\n'
            f"VERSION : 0.1\n"
            f"{struct_txt.strip()}\n"
            f"BEGIN\n"
            f"END_DATA_BLOCK\n",
            encoding="utf-8",
        )
        db_count += 1

    # 3. Export Readable OB / FB / FC Interfaces & Network Comments (.md)
    iface_map: dict[str, str] = {}
    cmt_map: dict[str, list[str]] = {}
    iface_type = {"00003": "OB", "00004": "FB", "00005": "FC", "00007": "SFC", "00009": "SFB"}
    cmt_type = {"00017": "OB", "00018": "FB", "00019": "FC"}

    for r in sub_new:
        styp = r["SUBBLKTYP"]
        bnum = int(r["BLKNUMBER"])
        if styp in iface_type:
            bkey = f"{iface_type[styp]}{bnum}"
            iface_map[bkey] = read_dbt_memo(dbt_new, r["MC5CODE"]).decode("latin1", errors="replace").strip()
        elif styp in cmt_type:
            bkey = f"{cmt_type[styp]}{bnum}"
            cmt_map[bkey] = clean_comment_blob(read_dbt_memo(dbt_new, r["MC5CODE"]))

    logic_keys = sorted(set(iface_map) | set(cmt_map))
    for bkey in logic_keys:
        sym_info = block_sym_map.get(bkey, {})
        sym_name = sym_info.get("_SKZ", bkey)
        en_c, de_c = split_en_de_comment(sym_info.get("_COMMENT", ""))
        safe_sym = re.sub(r"[^A-Za-z0-9_]+", "_", sym_name)
        lines = cmt_map.get(bkey, [])
        header_lines = [ln for ln in lines if ln.startswith("*")]
        net_titles = [ln for ln in lines if not ln.startswith("*")]

        doc_parts = [
            f"# `{bkey}` — `{sym_name}`",
            "",
            f"- **EN**: {en_c}",
            f"- **DE**: {de_c}",
            "",
        ]
        if header_lines:
            doc_parts.extend(["## OEM Revision Header (`CO.RI.M.A. SRL`)", "", "```text", *header_lines, "```", ""])
        if iface_map.get(bkey):
            doc_parts.extend(["## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)", "", "```iecst", iface_map[bkey], "```", ""])
        if net_titles:
            doc_parts.append("## Sequence / Network Titles (Original Italian)")
            doc_parts.append("")
            for idx, nt in enumerate(net_titles, start=1):
                doc_parts.append(f"{idx}. `{nt}`")
            doc_parts.append("")

        (blk_dir / f"{bkey}_{safe_sym}.md").write_text("\n".join(doc_parts), encoding="utf-8")

    # 4. Export ProTool HMI Screens & HMI Tags CSV
    with (hmi_dir / "protool_screens.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["screen_index", "protool_screen_name", "wincc_unified_migration_action"])
        for idx, scr in enumerate(PROTOOL_SCREENS, start=1):
            action = (
                "REMOVE/LOCK in Production (EU GMP Annex 11 compliance)"
                if "FORZA_USCITE" in scr or "CONTROLLO_" in scr
                else "Rebuild natively in WinCC Unified (800x480 WVGA, EN/DE)"
            )
            writer.writerow([idx, scr, action])

    raw_tag_blobs = [
        s.decode("latin1")
        for s in re.findall(rb"(?:HMI|LAVORO|MERKER|SYS)\.[A-Za-z0-9_\.]+", pdb_raw)
    ]
    split_tags: set[str] = set()
    for blob in raw_tag_blobs:
        for m in re.finditer(
            r"(?:HMI|LAVORO|MERKER|SYS)\.[A-Za-z0-9_\.]+?(?=HMI\.|LAVORO\.|MERKER\.|SYS\.|PT/CS|Segnalazioni|Acquisizioni|$)",
            blob,
        ):
            split_tags.add(m.group(0).rstrip("."))
    hmi_tags = sorted(split_tags)
    with (hmi_dir / "protool_hmi_tags.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["tag_index", "protool_symbolic_tag"])
        for idx, t in enumerate(hmi_tags, start=1):
            writer.writerow([idx, t])

    return {
        "vat1_rows": len(vat_rows),
        "db_files": db_count,
        "logic_block_docs": len(logic_keys),
        "protool_tags": len(hmi_tags),
    }


if __name__ == "__main__":
    stats = unpack_and_organize()
    print(
        f"Unpacked & organized Denester_Fault project: "
        f"{stats['vat1_rows']} VAT_1 diagnostic tags, "
        f"{stats['db_files']} readable .db files, "
        f"{stats['logic_block_docs']} OB/FB/FC block docs, "
        f"{stats['protool_tags']} ProTool HMI tags."
    )
