# Phase 1: Obsolescence & ICH Q9 / GAMP 5 FMEA Risk Assessment

**Document ID**: `P1-RA-001` | **Framework**: ISPE GAMP 5 (2nd Ed.) / ICH Q9 / EN ISO 13849-1 | **Data Source**: [`obsolescence_risk_register.csv`](./data/obsolescence_risk_register.csv)

---

## Bilingual Risk Summary (`EN / DE`)

- **EN**: Quantitative FMEA evaluation across `12` hardware, safety, process, and GMP compliance failure modes identifies **`4` CRITICAL risks ($\text{RPN} \ge 80$)**, **`3` HIGH risks ($\text{RPN}\ 48\text{–}79$)**, **`4` MEDIUM risks ($\text{RPN}\ 25\text{–}47$)**, and **`1` LOW risk ($\text{RPN} < 25$)**. The single highest operational exposure (`R-01`, **$\text{RPN} = 125$**) is that X/Y axis proportional valve speeds, ramps, and holding pressures (`DB20`/`DB21`) plus active gripper timers (`DB106`) are **all zero (`0`) in the offline STEP 7 project** and reside exclusively inside the discontinued `TP170B Color` Flash memory. Executing **Day-1 Containment Actions `C-1` through `C-4`** immediately protects Visual Inspection (VI) line continuity while Phase 2–4 engineering proceeds.
- **DE**: Die quantitative FMEA-Risikobewertung über `12` Subsysteme identifiziert **`4` KRITISCHE Risiken ($\text{RPN} \ge 80$)** und **`3` HOHE Risiken ($\text{RPN}\ 48\text{–}79$)**. Das höchste Einzelrisiko (`R-01`, **$\text{RPN} = 125$**) resultiert daraus, dass sämtliche X/Y-Proportionalventil-Geschwindigkeiten, Rampen und Haltedrücke (`DB20`/`DB21`) im Offline-STEP-7-Projekt den Wert **`0`** aufweisen und ausschließlich im Flash-Speicher des seit 2017 abgekündigten `TP170B Color` liegen. Die **Sofortmaßnahmen `C-1` bis `C-4`** sichern den laufenden VI-Linienbetrieb vor Umbaubeginn ab.

---

## 1. FMEA Scoring Methodology ($\text{RPN} = S \times L \times D$)

| Score (`1–5`) | **Severity ($S$)** *(VI Line / Safety / Product Quality)* | **Likelihood ($L$)** *(Lifecycle & Component Age)* | **Detectability / Recovery ($D$)** *(Backup & Spare Lead Time)* |
| :---: | :--- | :--- | :--- |
| **5** | Unrecoverable VI line stop (>1 week), operator injury risk, or uncontained glass breakage / major GMP citation | Component >15 yrs old & `PM490` totally discontinued / past 20-yr $T_M$ | Zero offline parameter backup or zero cross-model spare compatibility |
| **4** | Extended VI line stop (2–5 days), cosmetic syringe defect spike, or Annex 11 audit deficiency | `PM410` discontinued or ~20-yr wear item (VFDs, proportional valves) | Requires gray-market sourcing, legacy WinXP/MPI PG, or manual re-tuning |
| **3** | Shift-level downtime (<24 h) or repeated operator intervention | Active phase-out (`PM400`) or moderate mechanical wear | Spare available within 2–5 days; manual recalibration required |
| **2** | Minor nuisance stop (<2 h), zero syringe damage | Mature component with standard catalog replacement | Direct drop-in spare in site maintenance crib |
| **1** | Negligible operational or quality impact | Current active industrial product (<5 yrs) | Automated diagnostics & restorable backup verified |

**Risk Tiers**:
- **`CRITICAL` ($\text{RPN}\ 80\text{–}125$)**: Immediate Day-1 containment mandatory + primary driver for Phase 1–4 modernization.
- **`HIGH` ($\text{RPN}\ 48\text{–}79$)**: Address in Phase 2/3 BOM or preventive maintenance refurbishment.
- **`MEDIUM` ($\text{RPN}\ 25\text{–}47$)**: Mitigate through design controls (e.g., Hardwired VI Firewall, `MTP700 Unified` selection).
- **`LOW` ($\text{RPN}\ 1\text{–}24$)**: Manage via standard diagnostic enhancements and routine PM.

---

## 2. Quantitative FMEA Risk Summary Table

*(Full CSV dataset maintained in [`obsolescence_risk_register.csv`](./data/obsolescence_risk_register.csv))*

| ID | Asset / Tag | Finding Summary | $S$ | $L$ | $D$ | **RPN** | Tier | Target Resolution |
| :--- | :--- | :--- | :-: | :-: | :-: | :-: | :--- | :--- |
| **`R-01`** | `TP170B Color` + `DB20/21/106` | `PM490` Total Discontinuation (2017-04-01); X/Y motion & timer DBs are `0` offline (Flash-only) | 5 | 5 | 5 | **125** | **CRITICAL** | Day-1 capture (`C-1`) + `MTP700 Unified` + retentive `S7-1500` DBs |
| **`R-02`** | `CPU 313C` (`V1.0`) | `PM410` S7-300 Discontinuation (2025-10-01); MPI-only; V1.0 blocked from direct TIA migration | 5 | 4 | 5 | **100** | **CRITICAL** | Online RAM upload (`C-2`) + `CPU 1512C-1 PN` |
| **`R-03`** | Safety Relay `UE142` | ~2006 relay reached **20-year EN ISO 13849-1 mission time ($T_M$)** in 2026 | 5 | 4 | 4 | **80** | **CRITICAL** | Walkdown date check (`C-3`) + new `3SK1` / `PNOZ` safety relay |
| **`R-04`** | ProTool Passwords & `FORZA_USCITE` | Shared numeric passwords, zero Annex 11 audit trail, raw output forcing screens | 4 | 4 | 5 | **80** | **CRITICAL** | Password custody (`C-4`) + WinCC Unified RBAC, Audit & forcing lockout |
| **`R-05`** | `YV263` / `YV266` Proportional Axes | 20-yr spool/seal wear & analog zero drift (`TARATURA ASSE X/Y`); glass impact risk | 4 | 4 | 4 | **64** | **HIGH** | Option 1 valve overhaul/spare vs. Option 2 `SINAMICS S210` servos |
| **`R-06`** | Belt VFDs `UE71` & `UE76` | ~20-yr DC-bus capacitor aging; `UE76` trip halts syringe feed into VI | 4 | 4 | 4 | **64** | **HIGH** | Walkdown nameplate capture + proactive VFD spare/replacement |
| **`R-07`** | `SM 321` & `SM 323` I/O | `PM410` Type Discontinuation (2025-10-01); spare-parts cost/lead-time escalation | 4 | 3 | 4 | **48** | **HIGH** | Replace with `S7-1500` DI16 + DQ16 modules (+20% spare) |
| **`R-08`** | VI Interface (`J291`/`B293`/`UE76`) | Modifying interface protocol could trigger costly re-qualification of downstream VI | 5 | 2 | 4 | **40** | **MEDIUM** | Enforce **Hardwired 24VDC Validation Firewall** in `URS` & `OQ` |
| **`R-09`** | Target HMI Lifecycle Trap | Classic `TP700 Comfort` entered `PM400` Phase-Out on **2026-01-31** | 3 | 3 | 4 | **36** | **MEDIUM** | Specify **`MTP700 Unified Comfort`** (`6AV2128-3GB06-0AX1`) |
| **`R-10`** | Quadrature Encoder `BQ281` | Shaft/bearing wear shifts `64 / 100 / 160` row pick position (`PID 768`) | 4 | 3 | 3 | **36** | **MEDIUM** | Map to `CPU 1512C-1 PN` `High_Speed_Counter` TO + stock 1x spare |
| **`R-11`** | `ProTool V6.0` WinXP Dependency | Requires legacy 32-bit OS + MPI adapter incompatible with modern IT policies | 3 | 4 | 3 | **36** | **MEDIUM** | Consolidate into TIA Portal V19/V20 over standard Ethernet |
| **`R-12`** | Sequence Sensors & Valves (`SEQ1..3`) | Reed switch drift causes generic step hangs in `FC10 SEQUENCER` | 3 | 3 | 2 | **18** | **LOW** | Add explicit step-timeout sensor diagnostics on `MTP700 Unified` |

---

## 3. Mandatory Day-1 Interim Containment Plan (`C-1` to `C-4`)

> [!CAUTION]
> **Execute Before Powering Down the Denester or Approaching Cutover**
> Do **not** pull the `CPU 313C` MMC card or cycle power to a degraded `TP170B Color` before completing `C-1` and `C-2` using [`04_Shopfloor_Walkdown_and_Backup_Checklist.md`](./04_Shopfloor_Walkdown_and_Backup_Checklist.md).

1. **`C-1` — Live `TP170B Color` Recipe & ProSave Capture *(Owner: Maintenance / Automation, Target: Week 1)***:
   - Navigate through `PARAMETRI1`, `PARAMETRI2`, `PARAMETRI3`, `TARATURA1`, and `FORMATO_VISUALIZZA_1` (`64`, `100`, `160` sets) on the live `TP170B Color` and photograph/record every value.
   - Connect via MPI and take a complete binary **`ProSave` (`.psb`) backup image** (including Recipes and Password List).
2. **`C-2` — Online `CPU 313C` RAM Upload *(Owner: Automation Engineering, Target: Week 1)***:
   - Connect STEP 7 v5.7 via MPI (`187.5 kbps`, Address `2`) and upload online actual values of `DB20`, `DB21`, `DB100`, `DB105`, and `DB106` from PLC RAM into a timestamped snapshot so Phase 2 `S7-1500` retentive DBs start with exact production-proven setpoints.
3. **`C-3` — Safety Relay `UE142` & Field Nameplate Audit *(Owner: Engineering, Target: Week 1)***:
   - Record OEM part numbers, serials, and manufacture dates for `UE142`, `YV263`, `YV266`, `UE71`, `UE76`, and `BQ281`; confirm `YV263`/`YV266` analog control signal (`0–10 V` vs. `±10 V` vs. `4–20 mA`).
4. **`C-4` — Interim Administrative Password Control *(Owner: System Owner, Target: Immediate)***:
   - Restrict the highest-level ProTool numeric password (granting access to `FORZA_USCITE` and `CONTROLLO_COMANDO_VARIABILI`) strictly to Automation Engineering until Phase 3 cutover.
