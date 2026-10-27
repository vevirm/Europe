# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2693** (Main **1105** + Historical **1588**)
- Automatic queue still needing V2 verification: **28** (Main **13** + Historical **15**)
- Currently assigned to workers: **25** (Main **13** + Historical **12**)
- Bounded access-recovery retries still eligible: **12**
- Dropped after three failed recovery passes (archived): **171**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **3**

## Worker lanes

### Worker A
- Current package: `worker-a-20261027T092456Z-40aa9535af8e`
- Assigned unresolved records: **19**
  1. `link:https://ecipe.org/publications/forward-looking-agenda-for-eu-quantum-policy/#_ftnref5` — From Sovereignty to Managed Interdependence: A Forward-Looking Agenda for EU Quantum Policy
  2. `link:https://doi.org/10.1515/ordo-2026-2012` — Towards a rule-bound EU transformation policy: Can Ordnungspolitik and industrial strategy be reconciled?
  3. `link:https://doi.org/10.1093/eurpub/ckag169.1923` — Reducing Salt Intake through EU Sustainable Public Procurement in Daycare Meals in Copenhagen
  4. `link:https://doi.org/10.1093/eurpub/ckag169.087` — G.2. Round Table: From call to action to delivery: scaling climate–health solutions across Europe
  5. `link:https://doi.org/10.1093/eurpub/ckag169.430` — P.7. Round Table: Building the foundation: Data governance and harmonisation for CVD and diabetes in Europe
  6. `link:https://doi.org/10.1177/16118944261490056` — An Offshore Financial Centre Inside Europe: Luxembourg, Taxation and European Economic Community (1960s–1970s)
  7. `link:https://doi.org/10.1093/eurpub/ckag169.883` — Governance, not technology: low-hanging fruits for AI readiness in Europe, a latent class analysis
  8. `historical:id:a14995febfdbba0c` — Stable decoupling: Three tests for Europe in the face of Chinese economic coercion – European Council on Foreign Relations
  - … plus 11 more in the package manifest

### Worker B
- Current package: `worker-b-20261026T115433Z-adc5978a6022`
- Assigned unresolved records: **6**
  1. `link:https://doi.org/10.1080/13563467.2026.2751107` — Globalised but divided: European corporations and the EU’s geoeconomic turn against China — recovery attempt 2/3
  2. `link:https://doi.org/10.1080/13563467.2026.2751104` — Chinese and Russian nuclear energy companies in Europe’s geoeconomic turn: giving way to the Americans? — recovery attempt 2/3
  3. `link:https://doi.org/10.1002/sd.71344` — Green Energy Transition and Sustainable Development Outcomes in Europe: Evidence of Threshold and Moderating Effects — recovery attempt 2/3
  4. `link:https://doi.org/10.1177/2336825x261466887` — EU policy towards the sahel in the “post-West” era — recovery attempt 2/3
  5. `link:https://doi.org/10.1080/23322969.2026.2751120` — Emerging research security approaches: organisational arrangements at three European universities — recovery attempt 2/3
  6. `historical:id:dfdf69eee6d7a0f4` — Supranational security states for national security problems: governing by rules & capacities in tech-driven security spaces — recovery attempt 2/3

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
