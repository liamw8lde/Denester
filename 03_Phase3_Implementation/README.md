# Phase 3 — Implementation (Hardware Retrofit, FAT, Cutover & SAT)

> [!NOTE]
> **Gate Status**: **Scheduled after Phase 2 Gate 2 Design Freeze & Protocol Pre-Approval**.

## 1. Phase 3 Scope of Work
1. **Off-Line Panel Sub-Plate Pre-Build & Bench `FAT`**:
   - Pre-assemble and wire the `CPU 1512C-1 PN` DIN rail, 24VDC distribution, PROFINET switch, and renewed safety relay (`UE142` replacement) on a bench test rig.
   - Execute Factory Acceptance Test (`FAT`) simulating all `63` I/O channels, quadrature encoder `BQ281`, analog proportional outputs `PQW 752` / `PQW 754`, and all `37` `MTP700 Unified Comfort` screens (`EN / DE`).
2. **Mechanical & Electrical Cutover (Planned VI Line Outage)**:
   - Lockout/Tagout (`LOTO`), final archival backup of legacy `CPU 313C` RAM and `TP170B Color`.
   - Drop-in mechanical installation of **`MTP700 Unified Comfort`** into the existing **`197 × 141 mm`** stainless-steel HMI cutout (zero sheet-metal cutting or cleanroom particulate generation).
   - Install `S7-1500` rack, reconnect field wiring per redlined EPLAN schematics, and verify 24VDC isolation on the downstream VI interface (`J291`, `B293`, `UE76`).
3. **Cold/Hot Commissioning & Site Acceptance Test (`SAT`)**:
   - 100% point-to-point I/O loop check (`63` tags).
   - Safety circuit functional verification (`SB150` E-Stop, `SQ160`/`SQ351`/`SQ352` guards, `YV311` vertical brake).
   - Load captured production parameters into retentive `DB20`, `DB21`, and `DB10`–`DB12`; verify `TARATURA ASSE X/Y` proportional valve tuning (`YV263`/`YV266`) and `BQ281` nest pitch indexing.
   - Execute formal `SAT` and close punch-list items prior to **Gate 3 Handover to Qualification**.
