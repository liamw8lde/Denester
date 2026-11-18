# Day-1 Shop-Floor Walkdown & Live `TP170B` Flash Backup Checklist (`P1-CL-001`)

**Machine**: `MP1P-Ferring` Syringe Nest Denester | **Duration**: ~30 Minutes (Machine Safe / Stopped between Batches)

> [!CAUTION]
> **DO NOT CYCLE MAIN POWER OR REMOVE THE `CPU 313C` MMC CARD BEFORE COMPLETING SECTIONS 1 & 2.**
> Offline STEP 7 inspection proved that `DB20` (X-Axis), `DB21` (Y-Axis), and `DB106` (active gripper/discharge timers) are **all `0` offline**. If the 20-year-old `TP170B Color` fails during a power cycle before these values are recorded, all production-tuned speeds and ramps must be re-commissioned from scratch.

---

## Section 1 — Live `TP170B Color` Screen Parameter Capture (`Containment C-1`)

Navigate on the `TP170B Color` panel (photograph every screen clearly **AND** record values below):

### 1.1 X/Y Proportional Axis Parameters (`PARAMETRI1` / `PARAMETRI2` / `TARATURA1` → `DB20` & `DB21`)
| Parameter (`IT / DE` Label on `TP170B`) | PLC Tag | Format `64` | Format `100` | Format `160` | Photo Taken? |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **X Forward Fast** (`X nest avanti veloce`) | `LAVORO.PARAMETRI.AsseX.AvantiVeloce` | `_____` | `_____` | `_____` | `[ ]` |
| **X Forward Slow** (`X nest avanti lento`) | `AsseX` Slow Fwd | `_____` | `_____` | `_____` | `[ ]` |
| **X Forward Accel / Decel** (`AvantiAcc / AvantiDec`) | `AsseX.AvantiAcc / Dec` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |
| **X Forward Holding Force** (`avanti fermo forza staz.`) | `DB20` Hold Fwd | `_____` | `_____` | `_____` | `[ ]` |
| **X Return Fast / Slow** (`X nest indietro veloce/lento`) | `AsseX.IndietroVeloce` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |
| **X Return Accel / Decel / Hold** (`IndietroAcc / Dec`) | `AsseX.IndietroAcc / Dec` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |
| **Y High Fast / Slow** (`Y nest alto veloce / lento`) | `AsseY.AltoVeloce` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |
| **Y High Accel / Decel / Hold** (`AltoAcc / AltoDec`) | `AsseY.AltoAcc / Dec` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |
| **Y Low Fast / Slow** (`Y nest basso veloce / lento`) | `AsseY.BassoVeloce` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |
| **Y Low Accel / Decel / Hold** (`BassoAcc / BassoDec`) | `AsseY.BassoAcc / Dec` | `___ / ___` | `___ / ___` | `___ / ___` | `[ ]` |

### 1.2 Process Dwell Timers & Active Selectors (`PARAMETRI3` / `SELETTORI1` / `FORMATO_VISUALIZZA_1`)
| Parameter | PLC Tag | Recorded Live Value | Photo Taken? |
| :--- | :--- | :---: | :---: |
| **Gripper Close Delay** | `LAVORO.PARAMETRI.SecPinzaOn` | `_________` | `[ ]` |
| **Gripper Open Delay** | `LAVORO.PARAMETRI.SecPinzaOff` | `_________` | `[ ]` |
| **Outfeed Max Level Delay** | `LAVORO.PARAMETRI.SecScaMaxOn` | `_________` | `[ ]` |
| **Nest Discharge On / Off Timers** | `SecScaNestOn / SecScaNestOff` | `____ / ____` | `[ ]` |
| **Active Nest Pitch Verification (`64 / 100 / 160`)** | `FORMATO_VISUALIZZA_1` (`DB12 / DB10 / DB11`) | Matches offline? `[ ] Yes [ ] Diff` | `[ ]` |
| **Software Version Screen (`VERSIONE_SW`)** | `VSW_PROGRAMMA_PLC` / `VSW_PROGRAMMA_OP` | `_________________` | `[ ]` |

---

## Section 2 — Electronic MPI Backups (`Containment C-1 & C-2`)
- [ ] **ProSave Full Backup (`.psb`)**: Connected PG/Laptop to `TP170B Color` (MPI Address `1`, `187.5 kbps`) and saved full image + **Recipes** + **Password List** (`Filename: _______________________`).
- [ ] **STEP 7 Online RAM Upload**: Connected STEP 7 v5.7 to `CPU 313C` (MPI Address `2`) and uploaded online `DB10`, `DB11`, `DB12`, `DB20`, `DB21`, `DB90`, `DB100`, `DB105`, `DB106` (`Filename: _______________________`).

---

## Section 3 — Control Cabinet & Field OEM Nameplate Audit (`Containment C-3`)

| Schematic Tag | Subsystem | Manufacturer & Exact Model / Part Number | Key Electrical / Mechanical Spec | Checked |
| :--- | :--- | :--- | :--- | :---: |
| **`UE142`** | Safety Relay (`I 125.6`) | `______________________________` | Mfg Year: `______` / Supply: `24VDC` | `[ ]` |
| **`YV263`** | X-Axis Proportional Valve (`PQW 752`) | `______________________________` | Signal: `[ ] 0-10V [ ] +-10V [ ] 4-20mA` | `[ ]` |
| **`YV266`** | Y-Axis Proportional Valve (`PQW 754`) | `______________________________` | Signal: `[ ] 0-10V [ ] +-10V [ ] 4-20mA` | `[ ]` |
| **`UE71`** | Nest Conveyor VFD (`Q 124.6`) | `______________________________` | kW / Amps: `____________` | `[ ]` |
| **`UE76`** | VI Connecting Belt VFD (`Q 125.1`) | `______________________________` | kW / Amps: `____________` | `[ ]` |
| **`BQ281`** | Nest Quadrature Encoder (`PID 768`) | `______________________________` | PPR: `______` / `[ ] 24V HTL [ ] 5V TTL` | `[ ]` |
| **HMI Cutout** | Stainless Operator Door (`TP170B`) | Verify outer bezel clearance & depth behind door | Cutout `197×141 mm` / Depth `>65 mm`? `[ ] Yes` | `[ ]` |
| **VI Strip** | Terminal Strip (`J291`, `B293`, `UE76`) | Record terminal numbers & relay isolation source (`24VDC` internal vs. VI wet contact) | Terminals: `____________________` | `[ ]` |

**Walkdown Executed By**: `______________________` | **Date**: `____________` | **Reviewed By (Automation)**: `______________________`
