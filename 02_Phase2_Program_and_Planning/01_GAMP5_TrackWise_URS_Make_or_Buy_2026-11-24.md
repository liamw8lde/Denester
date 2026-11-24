# Denester — Phase 2 GAMP 5, TrackWise, URS and Make-or-Buy Plan

**Status:** Proposed planning deliverables — not approved design or executable change.  
**Primary technical owner:** OT Automation.  
**Machine / operational risk owner:** Head of Production.  
**Quality oversight:** QA.

## Entry gate

- Head of Production agrees in principle that the legacy Denester PLC and HMI should be replaced.
- OT and QA have reviewed the initial controls-obsolescence risks.
- Live PLC settings and HMI recovery data are captured/verified under an approved safe working procedure.
- Mechanical, pneumatic, belt-drive and downstream VI modifications remain outside the agreed PLC/HMI-only scope unless separately approved.

## Deliverables and accountability

| ID | Deliverable | Responsible / reviewer | Acceptance evidence |
|---|---|---|---|
| P2-01 | TrackWise Change Control, impact classification and implementation prerequisites | OT initiates with System Owner; QA reviews/approves per site SOP | TrackWise change record and required approvals |
| P2-02 | GAMP 5 validation strategy and plan | OT with QA / CSV | Approved strategy; confirmed software categorisation and GMP impact |
| P2-03 | User Requirements Specification (URS) | VI Process Engineering + Production, with OT technical input | Approved URS covering 64/100/160 formats as applicable, sequence behaviour, HMI, alarms, recipes, recovery and VI handshake |
| P2-04 | Preliminary functional and GMP risk assessment | OT + Process Engineering + QA | Reviewed hazards and risk controls; distinction between controls obsolescence and unrelated faults |
| P2-05 | Functional / hardware / software design specification | OT or qualified vendor under OT oversight | Architecture and supported Siemens part numbers, I/O map, validated configuration, maintained field interfaces |
| P2-06 | Requirements traceability matrix and test plan | OT + QA / CSV | URS-to-FAT/SAT/IQ/OQ/PQ (or justified equivalent) coverage |
| P2-07 | Internal OT execution estimate | OT | Estimated engineering hours, specialist capacity, tools, FAT/SAT and documentation effort |
| P2-08 | External-vendor scope and quotation | OT + Procurement | Same URS/acceptance criteria used for comparable bids; supplier competence and documentation assessed |
| P2-09 | Make-or-buy recommendation | OT + Procurement + Head of Production | Comparable lifecycle support, engineering effort, total scope, cost, risk and resource requirements |
| P2-10 | Go/no-go design and execution approval | Head of Production, relevant budget owner(s), QA and OT according to site SOP | Approved scope, funding, change/validation strategy and execution responsibilities |

## URS topics to agree

1. Maintain current validated process functions, including required 64/100/160 syringe-nest recipes and all interlocks.
2. Define HMI roles, diagnostics, alarm handling, parameter adjustment, data retention and backup/restore behaviour proportional to GMP risk.
3. Verify complete PLC/HMI recovery from tested backups including live values currently absent in the offline archive.
4. Preserve the intended `J291`, `B293`, and `UE76 RUN/OK` interface electrical and timing behaviour; QA determines downstream impact.
5. Define observable functional and process acceptance criteria with VI Process Engineering.
6. Preserve safety-related behaviours; assess any impact from altering control logic or safety interfaces in accordance with approved procedures.

## Make-or-buy comparison — no invented costs

| Decision factor | Internal OT delivery | External vendor delivery |
|---|---|---|
| Technical scope | Internal OT designs/programs PLC and HMI | Vendor delivers agreed scope under OT technical review |
| Resources | OT capacity and specialist tools to be quantified | Supplier resources and support to be quoted |
| Validation evidence | OT prepares test evidence with QA/CSV | Vendor provides agreed documentation/test packages; OT/QA review |
| Knowledge and long-term support | In-house retention of code and diagnostics | Verify full source project, licenses, backups, handover and support arrangements |
| Commercial evidence | Site internal effort estimate | Comparable competitive quotations |
| Decision | Phase 2 controlled assessment | Phase 2 controlled assessment |

**No implementation budget, downtime cost, schedule commitment, vendor pricing or future Siemens spare availability is presented as established until evidence has been collected and approved.**

## Phase 2 exit criteria

- [ ] TrackWise change in the status required by the applicable SOP.
- [ ] URS and GMP/functional risk assessment approved.
- [ ] Design and QA qualification strategy agreed.
- [ ] Internal and external execution scenarios compared using actual estimates/quotations.
- [ ] Technical owner, supplier, procurement and qualification roles documented.
- [ ] Necessary implementation and investment authorisations obtained before work starts.