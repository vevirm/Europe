# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2773** (Main **1151** + Historical **1622**)
- Automatic queue still needing V2 verification: **7** (Main **7** + Historical **0**)
- Currently assigned to workers: **7** (Main **7** + Historical **0**)
- Bounded access-recovery retries still eligible: **7**
- Dropped after three failed recovery passes (archived): **178**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261029T141549Z-050c3dac22cd`
- Assigned unresolved records: **5**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=41efa9e7-d253-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Member States' consolidated comments on Presidency third compromise text on the recitals and Title III (Certification) - Publications Office of the EU — recovery attempt 2/3
  2. `link:https://doi.org/10.1080/07036337.2026.2753502` — Constrained autonomy in EU external action: allied institutional hedging and the private compliance veto under US extraterritorial sanctions — recovery attempt 2/3
  3. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=f163e49d-d253-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Regulation on accelerating industrial capacity and decarbonisation (Industrial Accelerator Act) - Second Presidency Options Paper on Union Origin requirements - Publications Office of the EU — recovery attempt 2/3
  4. `link:https://doi.org/10.1111/exsy.70465` — A Network‐Enhanced Supervised Learning Framework for Early Prediction of Corruption Risk Indicators in Public Procurement Data — recovery attempt 2/3
  5. `link:https://doi.org/10.1080/13563467.2026.2751108` — Reconfiguring labour regimes in the Eastern industrial peripheries of the EU: a labour perspective on European industrial reorganisation within geoeconomic rivalry — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261029T141553Z-a6f415f8e42e`
- Assigned unresolved records: **2**
  1. `link:https://doi.org/10.1016/j.foodpol.2026.103185` — Advancing sustainable food systems cooperation in trade agreements: Lessons from Chile — recovery attempt 2/3
  2. `link:https://doi.org/10.2478/bjes-2026-0029` — Regulating LLM training under EU copyright law and its linguistic implications for smaller languages such as Estonian — recovery attempt 2/3

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
