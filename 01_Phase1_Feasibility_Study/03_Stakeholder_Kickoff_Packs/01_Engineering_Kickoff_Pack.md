# Kick-Off Pack 1: Engineering & Automation Alignment (`P1-KO-001`)

**Target Attendees**: Engineering Lead / Director, Automation Engineer, Electrical Maintenance Lead | **Duration**: 45 Minutes | **Languages**: `EN / DE`

---

## Bilingual Meeting Objective (`EN / DE`)
- **EN**: Align on the technical BOM (`CPU 1512C-1 PN` + `MTP700 Unified Comfort` + renewed `UE142` safety relay), approve immediate **Day-1 Containment (`C-1..C-3`)** to back up the live `TP170B Color` Flash recipes, review CAPEX/outage trade-offs between **Option 1** (€28k–€42k, 2–3 day outage) and **Option 2** (€58k–€85k, Servo X/Y), and select the execution model for Phase 2–3.
- **DE**: Abstimmung der Ziel-Stückliste (`CPU 1512C-1 PN` + `MTP700 Unified Comfort` + Ersatz `UE142`), Freigabe der **Sofortmaßnahmen (`C-1..C-3`)** zur Sicherung der `TP170B`-Flash-Rezeptdaten sowie Entscheidungsvorbereitung zwischen **Option 1** (Steuerungs-Retrofit, 2–3 Tage Stillstand) und **Option 2** (inkl. elektrischer Servoachsen X/Y).

---

## 1. 45-Minute Agenda

| Time | Topic | Key Technical Evidence |
| :--- | :--- | :--- |
| **00–10 min** | **Obsolescence & Unbacked Flash Exposure (`RPN = 125`)** | `TP170B` (`PM490` discontinued 2017), `S7-300` (`PM410` discontinued 2025-10-01), `UE142` (20-yr $T_M$ reached 2026), and `DB20/DB21/DB106 = 0` offline proof. |
| **10–25 min** | **Target Architecture & Mechanical Cutout Fit** | `CPU 1512C-1 PN` covers HSC (`BQ281`) + Analog (`YV263`/`YV266`) + DI/DQ; `MTP700 Unified Comfort` matches exact **`197 × 141 mm`** cutout (avoids classic `TP700 Comfort` `PM400` phase-out). |
| **25–35 min** | **Field Hardware Scope (`UE71`/`UE76` VFDs, `YV263`/`YV266`)** | Decide whether to proactively replace ~20-yr VFDs (`UE71`, `UE76`) during Phase 3 or hold pre-parameterized spares; review Option 1 vs. Option 2 CAPEX. |
| **35–45 min** | **Day-1 Walkdown Scheduling & Gate 1 Sign-Off** | Schedule 30-minute planned stop to execute [`04_Shopfloor_Walkdown_and_Backup_Checklist.md`](../04_Shopfloor_Walkdown_and_Backup_Checklist.md); confirm target VI maintenance shutdown window. |

---

## 2. Engineering Decision Matrix (To Complete at Kick-Off)

| Decision ID | Decision Question | Recommended Baseline | Selected Option & Notes |
| :--- | :--- | :--- | :--- |
| **`ENG-D1`** | **Modernization Option (`Option 1` vs. `Option 2`)** | **Option 1** (`S7-1512C-1 PN` + `MTP700 Unified` + safety relay; retain pneumatic X/Y unless VI Process Eng reports chronic drift/damage) | `[ ] Option 1` / `[ ] Option 2` |
| **`ENG-D2`** | **20-Year Conveyor VFDs (`UE71` & `UE76`)** | Proactively replace or purchase 2x pre-parameterized drop-in VFDs during Phase 2 procurement | `[ ] Replace in Phase 3` / `[ ] Stock Spare` |
| **`ENG-D3`** | **Safety Architecture (`UE142` Replacement)** | Standalone dual-channel safety relay (`SIRIUS 3SK1` / `PNOZsigma`) matching existing hardwired safety topology (`SB150`, `SQ160`, `SQ351/352`, `YV311`) | `[ ] Standalone Safety Relay` / `[ ] CPU 1512SP F-1 PN` |
| **`ENG-D4`** | **Phase 2–3 Execution Model** | Internal Automation Engineering (`0` protected blocks in `C6060007S_12.zip`, all `362` tags already translated `EN/DE`) + panel technician | `[ ] Internal` / `[ ] External Integrator` |
| **`ENG-D5`** | **Target Cutover Outage Window** | Align 2–3 day Phase 3 installation + 2–3 day Phase 4 `IQ/OQ/PQ` with next planned VI line maintenance shutdown | Target Date: `_______________` |

---

## 3. Gate 1 Engineering Action Items
- [ ] Assign Automation/Maintenance resource to execute [`04_Shopfloor_Walkdown_and_Backup_Checklist.md`](../04_Shopfloor_Walkdown_and_Backup_Checklist.md) within 5 business days.
- [ ] Locate printed/PDF electrical schematic binder (`C6060007.FER_SER_C6105006`) and upload/attach via [`upload_denester_fault.ps1`](../../tools/upload_denester_fault.ps1) into `00_Legacy_Baseline/Denester_Fault/`.
- [ ] Confirm analog output signal range (`0–10 V`, `±10 V`, or `4–20 mA`) for `YV263` (`PQW 752`) and `YV266` (`PQW 754`).
