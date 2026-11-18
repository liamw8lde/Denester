# Kick-Off Pack 3: System Owner & QA / CSV Alignment (`P1-KO-003`)

**Target Attendees**: VI Line System Owner, CSV / Qualification Lead, Quality Assurance (QA), Automation Engineer | **Duration**: 60 Minutes | **Languages**: `EN / DE`

---

## Bilingual Meeting Objective (`EN / DE`)
- **EN**: Confirm the **ISPE GAMP 5 Category 4** validation strategy, lock down the **Hardwired 24VDC VI Validation Firewall** (`J291`, `B293`, `UE76`) so the downstream Visual Inspection system requires **zero re-qualification**, remediate legacy GMP compliance gaps (`FORZA_USCITE` raw forcing, shared passwords, missing audit trail) under **EU GMP Annex 11 / 21 CFR Part 11**, and align on bilingual (`EN / DE`) operator screens.
- **DE**: Bestätigung der **GAMP-5-Kategorie-4**-Validierungsstrategie, Festschreibung der **festverdrahteten 24-VDC-Validierungsgrenze** (`J291`, `B293`, `UE76`) zur **Vermeidung einer Revalidierung der nachgeschalteten VI-Anlage**, Schließung bestehender Annex-11-Abweichungen (`FORZA_USCITE` Ausgangs-Forcen, Gruppenpasswörter, fehlender Audit-Trail) und Freigabe des zweisprachigen (`EN / DE`) Bedienkonzepts.

---

## 1. Protecting the Downstream Visual Inspection (VI) System ("Zero VI Re-Validation")

Code inspection of [`C6060007S_12.zip`](../../00_Legacy_Baseline/PLC_HMI_Archive/C6060007S_12.zip) proves there is **no MPI, PROFIBUS, PROFINET, or OPC UA connection** between the `MP1P-Ferring` Denester and the downstream Visual Inspection machine. The entire machine-to-machine interface consists of **four hardwired 24VDC signals**:

| Electrical Tag | PLC Address | Direction | Signal Function (`EN / DE`) | Phase 2–4 Validation Firewall Rule |
| :--- | :---: | :---: | :--- | :--- |
| **`J291`** | `I 125.0` | Input from VI | Downstream VI machine ready / `Nachfolgemaschine bereit` | Retain exact 24VDC dry-contact input circuit, terminal strip number, and debounce logic. |
| **`B293`** | `I 125.2` | Input from Outfeed | Outfeed accumulation max level / `Auslaufstau maximal` | Retain exact 24VDC photoelectric sensor input and automatic pause/resume behavior. |
| **`UE76_RUN`** | `Q 125.1` | Output to VFD | Infeed/connecting belt RUN / `Inverter Verb.band EIN` | Retain exact 24VDC run command interlocking with `J291` and `B293`. |
| **`UE76_OK`** | `I 125.3` | Input from VFD | Infeed/connecting belt healthy / `Inverter Verb.band OK` | Retain exact fault supervision & immediate belt-fault alarm generation. |

> [!IMPORTANT]
> **CSV Impact Conclusion**: By preserving this exact electrical 24VDC interface as our Phase 2–4 baseline—and proving electrical/timing equivalence during Phase 4 `OQ`—**zero hardware, PLC code, vision recipes, or electronic batch record logic inside the validated Visual Inspection system are touched**, eliminating expensive VI re-qualification.

---

## 2. Remediating Legacy `ProTool` GMP & Data Integrity Gaps

Inspection of `TDOP/PRO.PDB` (`C6060007H_10`) identified **three critical compliance gaps** on the legacy `TP170B Color` that will be closed natively on **`SIMATIC HMI MTP700 Unified Comfort`**:

| Legacy `TP170B Color` Gap (Found in `PRO.PDB`) | Regulatory Reference | Target `MTP700 Unified Comfort` Remediation |
| :--- | :--- | :--- |
| **Shared numeric password list** (`HMI.PASSWORD.Level_ON`), no individual user attribution | EU GMP Annex 11 Cl. 12 / 21 CFR 11.10(d),(g) | Individual named user accounts across 4 roles (`Operator`, `Maintenance`, `VI Process Engineer`, `System Admin`), minimum password complexity, failed-login lockout, and automatic inactivity logoff. |
| **Zero electronic audit trail** when X/Y speeds (`DB20/21`), timers (`DB106`), or nest pitches (`DB10–12`) are edited | EU GMP Annex 11 Cl. 9 / 21 CFR 11.10(e) | **WinCC Unified Audit** logs `Timestamp`, `User ID`, `Tag/Recipe Parameter`, `Old Value`, `New Value`, and optional electronic comment to tamper-evident storage with CSV/PDF QA review export. |
| **Unrestricted raw forcing screens** (`FORZA_USCITE`, `CONTROLLO_COMANDO_VARIABILI`, `ByteDiComando`) | EU GMP Annex 11 Cl. 7 & Machinery Safety | Remove raw memory/byte forcing (`CONTROLLO_COMANDO_VARIABILI`) completely; replace `FORZA_USCITE` with safe, safety-interlocked manual actuator jog buttons (`Maintenance` role only, machine stopped, `UE142_OK = TRUE`). |
| **Legacy `IT / DE` 320×240 screens** (`C6060007H_10` lacks English runtime text) | Site SOP / Multi-lingual Operations | Clean **`800 × 480` WinCC Unified** screens with instant 1-tap **`English (EN)` / `Deutsch (DE)`** language toggle (leveraging the `362` `EN/DE` tags already prepared in [`all_symbols_it_en_de.csv`](../../00_Legacy_Baseline/Extracted_Inventory/all_symbols_it_en_de.csv)). |

---

## 3. System Owner & QA Decision Checklist (Gate 1 Sign-Off)

| Decision ID | Governance Question | Recommended Baseline | Decision |
| :--- | :--- | :--- | :--- |
| **`SO-D1`** | **Downstream VI Interface Scope** | **Preserve Hardwired 24VDC Firewall** (`J291`, `B293`, `UE76` only — Zero VI Re-Validation); defer optional OPC UA/PROFINET format cross-check unless requested by QA | `[ ] Hardwired Only` / `[ ] Add OPC UA Check` |
| **`SO-D2`** | **Annex 11 / 21 CFR Part 11 Tier** | **Local WinCC Unified RBAC + Electronic Parameter Audit Trail** (no batch record master storage on Denester; periodic QA/Admin backup SOP) | `[ ] Local RBAC + Audit` / `[ ] AD/Central Server` |
| **`SO-D3`** | **Operator Runtime Languages** | **Bilingual `English (EN)` + `Deutsch (DE)`** *(optional retention of `IT` for OEM service reference if desired)* | `[ ] EN + DE` / `[ ] EN + DE + IT` |
| **`SO-D4`** | **GAMP 5 Deliverable Set (Phases 2–4)** | Change Control + `VP` + `URS` + combined `FRS/HDS/SDS` + `FRA` + `RTM` + `FAT/SAT` + `IQ/OQ/PQ` + `VSR` | `[ ] Approved` / `[ ] Modify per Site SOP` |
