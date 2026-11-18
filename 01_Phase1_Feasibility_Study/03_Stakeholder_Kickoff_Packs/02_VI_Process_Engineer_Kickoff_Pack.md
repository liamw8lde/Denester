# Kick-Off Pack 2: Visual Inspection (VI) Process Engineer Alignment (`P1-KO-002`)

**Target Attendees**: Visual Inspection (VI) Process Engineer, Packaging / Syringe Process Specialist, Automation Engineer | **Duration**: 60 Minutes | **Languages**: `EN / DE`

---

## Bilingual Meeting Objective (`EN / DE`)
- **EN**: Review syringe handling mechanics (`SEQ1` lifter, `SEQ2` transfer head, `SEQ3` extraction guide), verify active syringe-nest formats (`64`, `100`, `160` + any future formats), assess whether existing proportional pneumatic X/Y motion (`YV263`/`YV266`) meets glass cosmetic quality targets (**Option 1** vs. **Option 2 Servo**), and define **Phase 4 `OQ / PQ` syringe acceptance criteria**.
- **DE**: Überprüfung der Spritzen-Handhabungssequenzen (`SEQ1`–`SEQ3`), Bestätigung der aktiven Nestformate (`64er`, `100er`, `160er` sowie zukünftiger Formate), Bewertung der pneumatischen Proportionalachsen (`YV263`/`YV266`) hinsichtlich Glasbruch-/Kosmetikrisiko (**Option 1** vs. **Option 2 Servo**) und Festlegung der **`OQ / PQ`-Akzeptanzkriterien** für Phase 4.

---

## 1. Verified Syringe-Nest Baseline from `C6060007S_12.zip`

Byte-level extraction from `SUBBLK.DBT` ([`system_inventory.json`](../../00_Legacy_Baseline/Extracted_Inventory/system_inventory.json)) confirms three pre-configured syringe-nest format tables managed by `FB50` (`CALCOLO_PASSO`) and quadrature encoder `BQ281` (`PID 768`):

| Recipe DB | Syringe Nest Format | Active Rows | Saved Encoder Row Targets (`BQ281`) | Transfer Sequence |
| :--- | :--- | :---: | :--- | :--- |
| **`DB12` (`DATI_NEST64_1`)** | **64-Syringe Nest** *(typically 5 mL / 10 mL)* | `8` rows | `[150, 275, 400, 525, 650, 775, 900, 1025]` | `SEQ1` lifts row → `SEQ3` guides flanges → `SEQ2` (`YV317/318` gripper + `YV263/266` X/Y) places row onto discharge / `UE76` VI belt |
| **`DB10` (`DATI_NEST100_1`)** | **100-Syringe Nest** *(typically 1 mL long / 2.25 mL)* | `10` rows | `[29, 128, 229, 320, 419, 518, 617, 716, 815, 914]` | Same 3-sequence cycle |
| **`DB11` (`DATI_NEST160_1`)** | **160-Syringe Nest** *(typically 0.5 mL / 1 mL std)* | `16` rows | `[648, 725, 802, 879, 950, 1033, 1104, 1181, 1258, 1335, 1406, 49, 120, 197, 274, 351]` | Same 3-sequence cycle (wraps encoder zero at row 12) |

> [!IMPORTANT]
> **Critical Process Discovery**: While the nest encoder row pitches above (`DB10`–`DB12`) are stored offline, the **X/Y transfer velocities, acceleration/deceleration ramps, holding forces (`DB20`/`DB21`), and gripper dwell timers (`SecPinzaOn`, `SecPinzaOff`, `SecScaMaxOn` in `DB106`) are `0` in the offline STEP 7 project**. We will capture the live values directly from the `TP170B` screens before any work begins and review their permissible min/max engineering limits with you for Phase 2 `URS` freeze.

---

## 2. 60-Minute Process Engineering Questionnaire & Decision Matrix

| ID | Process Topic | Key Question for VI Process Engineer | Impact on Phase 2 `URS` & Phase 4 `PQ` |
| :--- | :--- | :--- | :--- |
| **`PROC-Q1`** | **Active & Future Nest Formats** | Are all three formats (`64`, `100`, `160`) currently qualified on this VI line, or are any retired / new formats (e.g., `42` or `120` nest, RTU vials/cartridges) planned within 3 years? | Defines recipe slots in WinCC Unified `Parameter Control` and formats required in Phase 4 `PQ`. |
| **`PROC-Q2`** | **Glass Cosmetic Quality & Pneumatic Drift (`YV263`/`YV266`)** | Do operators/mechanics currently perform frequent manual `TARATURA ASSE X / Y` adjustments, or see syringe flange chips, barrel scuffs, or fallen syringes at the `SEQ2` → `UE76` handoff? | **No issues** → Confirm **Option 1** (keep pneumatic X/Y). **Recurring drift/defects** → Justify **Option 2** (`SINAMICS S210` electric servo X/Y). |
| **`PROC-Q3`** | **Throughput & VI Starvation / Backpressure** | What is the target VI machine inspection speed (syringes/min or UPH) per format, and does connecting belt `UE76` / max-level sensor `B293` (`I 125.2`) ever cause micro-stops or syringe crowding? | Sets cycle-time acceptance criteria and `SecScaMaxOn` / `UE76` dwell tuning in Phase 2 `FRS`. |
| **`PROC-Q4`** | **Parameter Locking & Recipe Edit Rights** | Which process parameters should be **locked inside validated recipes** (editable only by `VI Process Engineer`) vs. **operator-adjustable** during a batch? | Configures WinCC Unified role permissions and EU GMP Annex 11 electronic audit trail triggers. |
| **`PROC-Q5`** | **Phase 4 `OQ / PQ` Acceptance Criteria** | How many nests per format (`e.g., 3 nests × 64 / 100 / 160`) and what false-reject / cosmetic-defect threshold at the downstream VI machine are required to sign off Phase 4 `PQ`? | Directly populates Phase 2 `Validation Plan (VP)` and Phase 4 `PQ` protocol acceptance tables. |

---

## 3. Proposed Phase 4 `PQ` Strategy (For VI Process Engineer Review)
1. **Dry-Cycle & Water-Filled / Dummy Nest `OQ` Trial**: Verify row-by-row pick accuracy across `64`, `100`, and `160` nests, emergency stop recovery, and `B293` / `J291` pause-resume behavior without glass damage.
2. **Production-Speed `PQ` Runs**: Run agreed qualification nest quantities per active format feeding directly into the downstream **Visual Inspection (VI)** system; confirm **zero glass breakage**, **cosmetic reject rate $\le$ historical baseline**, and **sustained UPH $\ge$ target VI rate**.
