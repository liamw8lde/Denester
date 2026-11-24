# Denester — PLC/HMI Replacement Approval Kickoff

**Status:** Draft for stakeholder meeting, 24 November 2026  
**Project lead:** OT Automation  
**Machine owner / operational risk owner:** Head of Production (System Owner)  
**Meeting:** Head of Production, OT Automation, VI Process Engineer, QA, Mechanical Engineering

## Decision sought

Approve **replacement of the existing Denester PLC, associated PLC I/O and HMI** as the project direction. This is an approval in principle for the OT-led replacement programme, not an approval to place orders or start implementation before the site's required change-control, qualification, procurement and financial approvals.

The project is **not** a machine redesign. Proposed scope excludes servomotor conversion, pneumatic redesign, conveyor drive replacement and modifications to the downstream Visual Inspection machine. The as-built interface and necessary verification remain subject to QA assessment.

## Evidence and initial risk position

| Element | Existing configuration | Risk / next evidence required |
|---|---|---|
| PLC | Siemens S7-300 CPU 313C, `6ES7 313-5BE00-0AB0` | Confirm exact Siemens product/repair/spare status and recoverability |
| I/O | S7-300 modules SM 321 and SM 323 | Confirm installed MLFBs, spares and replacement I/O mapping |
| HMI | SIMATIC TP170B Color, `6AV6 545-0BC15-2AX0`, ProTool V6.0 | Confirm panel support, restore procedure and recoverable recipe/settings backup |
| Offline data | Repository reports `DB20`, `DB21`, `DB106` production setpoints/recipe buffer zeroed in offline archive | Capture and compare live data before any intervention |
| VI interface | Existing hardwired signals `J291`, `B293`, `UE76 RUN/OK` | Preserve intended electrical/functional behaviour; QA to determine qualification impact |

**Caveat:** The repository's original 12-item FMEA and RPN scores are preliminary engineering work and require OT/Production/QA review. Obsolescence by itself does not establish the cause of current mechanical or process downtime. Do not claim PLC/HMI replacement eliminates unrelated faults.

## Responsibilities

| Stakeholder | Responsibility |
|---|---|
| Head of Production — System Owner | Owns production continuity and operational risk; confirms business need and residual operational risk position |
| OT Automation | Leads project; owns PLC/HMI scope, technical feasibility, architecture, programming, backup, migration, FAT/SAT technical evidence |
| QA | GMP and quality-risk assessment, TrackWise change-control oversight, validation/qualification requirements and required approvals |
| VI Process Engineer | URS process owner/contributor, operating requirements, functional-equivalence and acceptance criteria |
| Mechanical Engineering | Mechanical support **only** where mounting or physical interfaces require work |
| Procurement / finance | Sourcing and financial review in Phase 2 under applicable site process |

## Phase gates

1. **Phase 1 — Risk review and approval:** Identify and review PLC/HMI risks, obtain agreement to replace, protect live backups.
2. **Phase 2 — GAMP 5 and planning:** TrackWise change control, URS, GMP impact, risk/validation planning, functional/design requirements, make-or-buy study and costing, sourcing plan and formal execution approvals.
3. **Phase 3 — Engineering and implementation:** Develop/test PLC/HMI, FAT, controlled installation, SAT, configuration and restoration evidence.
4. **Phase 4 — Qualification and GMP release:** Perform approved IQ/OQ/PQ or justified alternative, close traceability/deviations, obtain QA and System Owner release.

## Proposed 45-minute agenda

| Minutes | Topic | Lead |
|---|---|---|
| 0–5 | Project objective and approval requested | OT / Head of Production |
| 5–15 | Existing controls, Siemens lifecycle, recovery concerns | OT |
| 15–25 | Operational and GMP risk implications | Production / QA / Process |
| 25–35 | PLC/HMI-only scope, phase gates and Phase 2 deliverables | OT / QA |
| 35–45 | Decision, responsibilities and action owners | Head of Production |

## Required meeting decision record

- [ ] Replacement of the PLC/HMI approved as direction by the Head of Production.
- [ ] OT technical project lead confirmed.
- [ ] QA agrees TrackWise / GAMP 5 planning approach and names accountable approvers.
- [ ] Process Engineering assigned to the URS and process acceptance requirements.
- [ ] Mechanical Engineering involvement limited to physical interfaces if required.
- [ ] Phase 2 in-house-vendor costing study approved as an activity, without any unverified budget commitments.
- [ ] Immediate verified backup and walkdown actions assigned.

## References

- [`00_Legacy_Baseline/Extracted_Inventory/system_inventory.json`](../../00_Legacy_Baseline/Extracted_Inventory/system_inventory.json)
- [`01_Phase1_Feasibility_Study/02_Obsolescence_and_FMEA_Risk_Assessment.md`](../02_Obsolescence_and_FMEA_Risk_Assessment.md)
- [`01_Phase1_Feasibility_Study/04_Shopfloor_Walkdown_and_Backup_Checklist.md`](../04_Shopfloor_Walkdown_and_Backup_Checklist.md)
- Siemens SiePortal — exact installed article numbers must be verified for lifecycle and supply status.

**No cost figures or outage assumptions are included in this approval deck.**