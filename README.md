# Current kickoff scope — 24 November 2026 (proposed, not yet approved)

The **current approval request is to replace only the Denester PLC, associated PLC I/O and HMI**. OT Automation leads all PLC/HMI technical work. The **Head of Production is the System Owner and operational risk owner**. QA is a required stakeholder for TrackWise change control and GMP/qualification decisions. VI Process Engineering defines process requirements; Mechanical Engineering supports **mechanical interfaces only**.

**Phase 2**: initiate TrackWise Change Control; prepare GAMP 5 validation planning and a process-approved URS; perform the functional/GMP risk assessment; and compare **in-house OT execution versus external vendor quotations**. No project cost, outage cost or delivery-duration estimate has been approved for the kickoff presentation. Procurement, implementation and GMP release require the applicable later approvals.

- [Approval presentation (editable PowerPoint)](presentations/Denester_PLC_HMI_Replacement_Kickoff_2026-11-24.pptx)
- [Meeting plan, risk framing, decision record and RACI](01_Phase1_Feasibility_Study/03_Stakeholder_Kickoff_Packs/04_Production_OT_QA_Approval_Kickoff_2026-11-24.md)
- [Phase 2 GAMP 5 / TrackWise / URS / make-or-buy plan](02_Phase2_Program_and_Planning/01_GAMP5_TrackWise_URS_Make_or_Buy_2026-11-24.md)

> Earlier repository modernization materials below represent preliminary historical concepts (including servo/safety/drive additions, budget estimates and assumptions on the downstream VI qualification boundary); those items are **not part of the current PLC/HMI-only approval request**. Verify exact Siemens lifecycle status and QA impact before making final claims.

---

# `MP1P-Ferring` Syringe Nest Denester Modernization (`S7-300` & `ProTool` → `S7-1500` & `WinCC Unified`)

**ISPE GAMP 5 (2nd Ed.) 4-Phase Modernization Repository** — Upgrading the legacy **CORIMA / IMA Life `MP1P-Ferring`** syringe nest denester (`SIMATIC S7-300 CPU 313C` + `SIMATIC TP170B Color` `ProTool V6.0`) to **`SIMATIC S7-1500 CPU 1512C-1 PN`** and **`SIMATIC HMI MTP700 Unified Comfort`** (`TIA Portal V19/V20`), while preserving the **Hardwired 24VDC Visual Inspection (VI) Validation Firewall** (`Zero Downstream VI Re-Qualification`).

---

## Reorganized GAMP 5 Repository Structure

| Directory / File | Phase & Purpose | Status |
| :--- | :--- | :--- |
| [`00_Legacy_Baseline/`](./00_Legacy_Baseline/) | Master untouched [`C6060007S_12.zip`](./00_Legacy_Baseline/PLC_HMI_Archive/C6060007S_12.zip), extracted JSON/CSV inventory (`63` I/O, `31` blocks, `362` `IT/EN/DE` symbols, `37` ProTool screens), and [`Denester_Fault/`](./00_Legacy_Baseline/Denester_Fault/README.md) audit | **Complete** *(Ready for extra `E:\Denester_Fault` files)* |
| [`00_GAMP5_Master_Roadmap/`](./00_GAMP5_Master_Roadmap/00_GAMP5_Master_Project_Plan.md) | **4-Phase ISPE GAMP 5 Master Project Plan (`EN / DE`)**: V-Model, System Classification (Cat. 4), Annex 11 / 21 CFR Part 11 Governance, RACI & Gates `1–4` | **Complete** |
| [`01_Phase1_Feasibility_Study/`](./01_Phase1_Feasibility_Study/) | **Phase 1 Package (`Active`)**: Feasibility Study (`Options 0–3`), Quantitative FMEA Risk Register (`12` items, `RPN = 125` Flash recipe finding), Kick-Off Packs (**Engineering**, **VI Process Engineer**, **System Owner**), Day-1 Backup Checklist & Interactive HTML Deck | **Complete — Ready for Gate 1 Review** |
| [`02_Phase2_Program_and_Planning/`](./02_Phase2_Program_and_Planning/README.md) | **Phase 2 Gate Manifest**: `VP`, `URS`, `FRS/HDS/SDS`, `FRA`, `RTM`, TIA Portal `S7-1500` / `MTP700 Unified` engineering & `PLCSIM Advanced` testing | **Staged (Starts upon Gate 1 Approval)** |
| [`03_Phase3_Implementation/`](./03_Phase3_Implementation/README.md) | **Phase 3 Gate Manifest**: Sub-plate pre-build, `FAT`, `197 × 141 mm` zero-cutting HMI drop-in swap, `63`-point I/O loop check & `SAT` | **Staged** |
| [`04_Phase4_Requalification/`](./04_Phase4_Requalification/README.md) | **Phase 4 Gate Manifest**: `IQ`, `OQ` (incl. Hardwired VI Firewall proof), `PQ` (`64 / 100 / 160` syringe nests), `RTM` closure & `VSR` | **Staged** |
| [`tools/`](./tools/) & [`tests/`](./tests/) | Reproducible STEP 7 / ProTool binary parser ([`extract_s7_baseline.py`](./tools/extract_s7_baseline.py)), Windows uploader ([`upload_denester_fault.ps1`](./tools/upload_denester_fault.ps1)), and automated `pytest` verification suite | **Passing** |

---

## Uploading Remaining Local Files from `E:\Denester_Fault`

The September 2026 `Denester_Fault` STEP 7 symbol/comment translations (`362` tags in `EN / DE`) and `0`-byte MC7 logic checksum proof have already been extracted from [`C6060007S_12.zip`](./00_Legacy_Baseline/PLC_HMI_Archive/C6060007S_12.zip) into [`00_Legacy_Baseline/Denester_Fault/`](./00_Legacy_Baseline/Denester_Fault/README.md).

To add any remaining local Windows files from `E:\Denester_Fault` (PDF electrical schematics, fault notes, photos, `ProSave` `.psb` files):
1. **Drag-and-Drop**: Zip `E:\Denester_Fault` (or run `.\tools\upload_denester_fault.ps1 -Mode Zip` in Windows PowerShell) and drop `Denester_Fault_Upload.zip` into the Antigravity chat, **OR**
2. **Direct GitHub Push**: Run `powershell -ExecutionPolicy Bypass -File .\tools\upload_denester_fault.ps1 -SourcePath "E:\Denester_Fault" -Mode GitPush` on your Windows PC to automatically categorize and push all files into `00_Legacy_Baseline/Denester_Fault/`.

---

## Reproducing the Baseline & Running Verification Tests

```bash
python3 tools/extract_s7_baseline.py
uv run --with pytest pytest tests/test_phase1_gamp5_package.py -v
```
