# Phase 2 — Programming & Detailed Planning (GAMP 5 Specification & Build Phase)

> [!NOTE]
> **Gate Status**: **Pending Phase 1 Gate 1 Approval** (Selection of `Option 1: Controls & Safety Retrofit` vs. `Option 2: Controls + Electric Servo X/Y Upgrade`, plus completion of the Day-1 `TP170B` Flash backup checklist in [`04_Shopfloor_Walkdown_and_Backup_Checklist.md`](../01_Phase1_Feasibility_Study/04_Shopfloor_Walkdown_and_Backup_Checklist.md)).

## 1. Phase 2 Entry Criteria (Gate 1 Exit)
- [ ] Signed Gate 1 Charter across **Engineering**, **VI Process Engineer**, and **System Owner**.
- [ ] Confirmed live `TP170B Color` parameter capture (`DB20` X-axis, `DB21` Y-axis, `DB106` active gripper/discharge timers) and `ProSave` `.psb` backup.
- [ ] Confirmed Annex 11 / 21 CFR Part 11 tier and hardwired VI validation firewall (`J291`, `B293`, `UE76`).

## 2. Planned Phase 2 GAMP 5 Deliverables
1. **`01_Validation_Plan_VP.md`**: GAMP 5 Category 4 validation strategy, roles, supplier assessment, and downstream VI non-impact justification.
2. **`02_URS_User_Requirements.md`**: Bilingual (`EN / DE`) process, throughput (`64 / 100 / 160` nests), safety, alarm, and data-integrity requirements.
3. **`03_FRS_HDS_SDS_Design_Specs.md`**:
   - **HDS**: `S7-1512C-1 PN` (`6ES7 512-1CK01-0AB0`), `MTP700 Unified Comfort` (`6AV2128-3GB06-0AX1`), renewed dual-channel safety relay (`UE142`), and `63`-point I/O terminal mapping.
   - **SDS**: TIA Portal V19/V20 block architecture (`OB1`, `OB100`, migrated `FB11`/`FB50`/`FC10`–`FC109`), `High_Speed_Counter` TO replacing S7-300 `SFB 47` (`BQ281`), retentive recipe DBs (`DB10`–`DB12`, `DB20`–`DB21`), and WinCC Unified `37`-screen hierarchy with RBAC & Parameter Audit Trail.
4. **`04_Functional_Risk_Assessment_FRA.md` & `05_Traceability_Matrix_RTM.csv`**: Clause-by-clause mapping from `URS` → `FRS/HDS/SDS` → `FRA` → `FAT/SAT/IQ/OQ/PQ`.
5. **`06_TIA_Portal_Project_and_Offline_Sim/`**: Structured SCL/LAD/Openness exports, tag tables imported from [`all_symbols_it_en_de.csv`](../00_Legacy_Baseline/Extracted_Inventory/all_symbols_it_en_de.csv), and `S7-PLCSIM Advanced` verification report.

## 3. Phase 2 Exit Criteria (Gate 2)
- [ ] Approved `VP`, `URS`, `FRS/HDS/SDS`, `FRA`, and draft `RTM`.
- [ ] Completed offline PLC/HMI simulation and internal code review (`0` legacy `FORZA_USCITE` production exposures).
- [ ] QA pre-approved `FAT`, `SAT`, `IQ`, `OQ`, and `PQ` test protocols prior to Phase 3 execution.
