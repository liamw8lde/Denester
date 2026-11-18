# Phase 4 — Requalification (GAMP 5 IQ, OQ, PQ & GMP Release)

> [!NOTE]
> **Gate Status**: **Scheduled immediately following Phase 3 Gate 3 SAT Completion**.

## 1. GAMP 5 Qualification Scope

### 1.1 Installation Qualification (`IQ`)
- Verify installed part numbers, serial numbers, and firmware versions (`CPU 1512C-1 PN`, `MTP700 Unified Comfort`, renewed safety relay `UE142`, power supplies) against approved `HDS`.
- Verify as-built EPLAN electrical drawings, wire ferrules, earthing/bonding, and cleanroom IP65 front-bezel sealing on the `197 × 141 mm` HMI cutout.
- Verify TIA Portal project archive backup, checksum documentation, and `MTP700 Unified` cybersecurity hardening (disabled unused ports, NTP/clock sync, admin password custody).

### 1.2 Operational Qualification (`OQ`)
- **Safety & Interlock Challenge**: E-Stop `SB150`, guard doors/covers `SQ160` / `SQ351` / `SQ352`, vertical axis brake `YV311`, and low-air switch `SP292`.
- **Hardwired VI Validation Firewall Verification**: Prove discrete signal polarity, fail-safe drop-out, and timing on `J291` (`I 125.0` Downstream VI Ready), `B293` (`I 125.2` Outfeed Max Level), and `UE76` (`Q 125.1` / `I 125.3` Connecting Belt VFD) without touching downstream VI software/config.
- **Annex 11 / 21 CFR Part 11 Controls**: Challenge individual user logins (`Operator`, `Maintenance`, `VI Process Engineer`, `Admin`), auto-logoff, unauthorized access rejection, raw forcing lockout (`FORZA_USCITE`), and electronic Audit Trail generation/export upon recipe modification.
- **Motion & Sequence Challenge**: Verify `SEQ1` lifter, `SEQ2` X/Y transfer head, `SEQ3` extraction guide, and `BQ281` encoder row indexing across `64`, `100`, and `160` formats, plus power-loss retentivity of `DB10`–`DB12` and `DB20`–`DB21`.

### 1.3 Performance Qualification (`PQ`)
- Executed jointly with the **VI Process Engineer** using representative `64`, `100`, and `160` glass syringe nests:
  - Sustained line throughput (UPH) matching downstream Visual Inspection machine demand without starvation or `B293` sensor chatter.
  - Zero increase in glass syringe breakage, flange chipping, barrel scuffing, or fallen syringes on connecting belt `UE76`.
  - Clean format changeover verification (`64 ↔ 100 ↔ 160`) using standard operator SOPs.

### 1.4 Validation Closure (Gate 4)
- Finalized **Requirements Traceability Matrix (`RTM`)** (`100%` requirements verified, `0` open critical/major deviations).
- Updated Operator, Maintenance, and Backup/Restore SOPs + training records.
- Signed **Validation Summary Report (`VSR`)** and formal QA Change Control release to GMP production.
