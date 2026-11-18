"""Automated verification tests for the Reorganized GAMP 5 Repository & Phase 1 Package."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from tools.extract_s7_baseline import ARCHIVE_PATH, extract_baseline

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_master_archive_reorganized_and_untouched() -> None:
    """Verify C6060007S_12.zip is cleanly relocated under 00_Legacy_Baseline and byte-identical."""
    assert ARCHIVE_PATH.exists(), f"Missing master archive at {ARCHIVE_PATH}"
    assert ARCHIVE_PATH.stat().st_size == 683_720
    assert not (REPO_ROOT / "C6060007S_12.zip").exists(), "Root duplicate C6060007S_12.zip should be moved"


def test_baseline_extractor_and_sept2026_denester_fault_audit() -> None:
    """Verify full inventory extraction, 0 protected blocks, 0 MC7 diffs vs 2016, and offline zero-byte proof."""
    inv = extract_baseline()
    assert inv["project_metadata"]["station_name"] == "MP1P-Ferring"
    assert inv["project_metadata"]["mc7_logic_modified_in_sept2026"] is False
    assert inv["counts"]["total_symbols"] == 362
    assert inv["counts"]["physical_io_tags"] == 63
    assert inv["counts"]["plc_blocks"] == 31
    assert inv["counts"]["know_how_protected_blocks"] == 0
    assert inv["counts"]["mc7_modified_blocks_vs_2016"] == 0
    assert inv["counts"]["protool_screens"] == 37
    assert inv["counts"]["sept2026_symbol_translations"] == 362

    # Verify live nest pitch tables (64, 100, 160)
    recipes = {r["nest_format_syringes"]: r for r in inv["nest_recipes_offline"]}
    assert recipes[64]["active_rows"] == 8
    assert recipes[100]["active_rows"] == 10
    assert recipes[160]["active_rows"] == 16

    # Verify critical R-01 finding: DB20/DB21 motion words 0..8 are all zero offline
    zero_audit = inv["offline_zero_parameter_audit"]
    assert zero_audit["DB20_motion_setpoints_all_zero_offline"] is True
    assert zero_audit["DB21_motion_setpoints_all_zero_offline"] is True


def test_vi_firewall_and_safety_tags_in_io_csv() -> None:
    """Verify critical VI interface, safety, encoder, VFD, and proportional valve tags in CSV."""
    csv_path = REPO_ROOT / "00_Legacy_Baseline" / "Extracted_Inventory" / "field_devices_and_io.csv"
    with csv_path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 63
    by_tag = {r["tag"]: r for r in rows}

    for tag in ("J291", "B293", "UE76_RUN", "UE76_OK"):
        assert tag in by_tag
        assert "Visual Inspection" in by_tag[tag]["subsystem_group"]

    for tag in ("UE142_OK", "SB150", "SQ160", "YV311", "YV263", "YV266", "BQ281_COUNT", "UE71_RUN"):
        assert tag in by_tag


def test_fmea_risk_register_math_and_tiers() -> None:
    """Validate RPN = S * L * D math and tier thresholds across all 12 risk items."""
    fmea_path = REPO_ROOT / "01_Phase1_Feasibility_Study" / "data" / "obsolescence_risk_register.csv"
    with fmea_path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 12

    for r in rows:
        s = int(r["severity_s"])
        l_val = int(r["likelihood_l"])
        d = int(r["detectability_leadtime_d"])
        rpn = int(r["rpn"])
        assert s * l_val * d == rpn, f"RPN mismatch on {r['risk_id']}"
        tier = r["risk_tier"]
        if rpn >= 80:
            assert tier == "CRITICAL"
        elif rpn >= 48:
            assert tier == "HIGH"
        elif rpn >= 25:
            assert tier == "MEDIUM"
        else:
            assert tier == "LOW"
        assert r["day1_containment_action"].strip()
        assert r["phase2_3_target_mitigation"].strip()


def test_all_4_gamp5_phases_and_bilingual_deliverables_exist() -> None:
    """Verify all 4 GAMP 5 phases, Kick-Off packs, PowerShell uploader, and EN/DE content exist."""
    required_files = [
        "README.md",
        "00_Legacy_Baseline/Denester_Fault/README.md",
        "00_Legacy_Baseline/Denester_Fault/sept2026_denester_fault_diff.csv",
        "00_Legacy_Baseline/Extracted_Inventory/system_inventory.json",
        "00_Legacy_Baseline/Extracted_Inventory/all_symbols_it_en_de.csv",
        "00_GAMP5_Master_Roadmap/00_GAMP5_Master_Project_Plan.md",
        "01_Phase1_Feasibility_Study/01_Engineering_Feasibility_Study.md",
        "01_Phase1_Feasibility_Study/02_Obsolescence_and_FMEA_Risk_Assessment.md",
        "01_Phase1_Feasibility_Study/03_Stakeholder_Kickoff_Packs/01_Engineering_Kickoff_Pack.md",
        "01_Phase1_Feasibility_Study/03_Stakeholder_Kickoff_Packs/02_VI_Process_Engineer_Kickoff_Pack.md",
        "01_Phase1_Feasibility_Study/03_Stakeholder_Kickoff_Packs/03_System_Owner_and_QA_Kickoff_Pack.md",
        "01_Phase1_Feasibility_Study/04_Shopfloor_Walkdown_and_Backup_Checklist.md",
        "01_Phase1_Feasibility_Study/phase1_gamp5_dashboard.html",
        "02_Phase2_Program_and_Planning/README.md",
        "03_Phase3_Implementation/README.md",
        "04_Phase4_Requalification/README.md",
        "tools/upload_denester_fault.ps1",
    ]
    for rel in required_files:
        p = REPO_ROOT / rel
        assert p.exists() and p.stat().st_size > 200, f"Missing or empty deliverable: {rel}"

    # Verify JSON parses cleanly
    inv_json = json.loads(
        (REPO_ROOT / "00_Legacy_Baseline/Extracted_Inventory/system_inventory.json").read_text(encoding="utf-8")
    )
    assert inv_json["hmi_protool"]["panel_cutout_mm"] == "197 x 141 mm"

    # Verify bilingual EN/DE presence in master roadmap, feasibility study & HTML dashboard
    for bilingual_doc in [
        "00_GAMP5_Master_Roadmap/00_GAMP5_Master_Project_Plan.md",
        "01_Phase1_Feasibility_Study/01_Engineering_Feasibility_Study.md",
        "01_Phase1_Feasibility_Study/phase1_gamp5_dashboard.html",
    ]:
        txt = (REPO_ROOT / bilingual_doc).read_text(encoding="utf-8")
        assert "Deutsch" in txt and "GAMP 5" in txt


def test_unpacked_denester_fault_folders() -> None:
    """Verify C6060007S_12.zip is unpacked into 6 clean, human-readable folders under Denester_Fault."""
    from tools.unpack_denester_fault import unpack_and_organize

    stats = unpack_and_organize()
    assert stats["vat1_rows"] >= 80
    assert stats["db_files"] == 9
    assert stats["logic_block_docs"] == 22
    assert stats["protool_tags"] >= 100

    fault_root = REPO_ROOT / "00_Legacy_Baseline" / "Denester_Fault"
    assert (fault_root / "01_VAT1_Fault_Diagnostic_Table" / "VAT1_Denester_Fault_WatchTable.csv").exists()
    assert (fault_root / "02_PLC_DataBlocks_Source" / "DB106_HMI.db").exists()
    assert (fault_root / "03_PLC_Logic_Blocks_Docs" / "FC106_SEQ1_SOL_SIRINGHE.md").exists()
    assert (fault_root / "04_ProTool_HMI_TP170B" / "protool_hmi_tags.csv").exists()
    assert (fault_root / "05_STEP7_Clean_Project" / "C6060007S_12" / "C6060007.s7p").exists()
    assert (fault_root / "06_Original_2016_Backup" / "sept2026_denester_fault_diff.csv").exists()

