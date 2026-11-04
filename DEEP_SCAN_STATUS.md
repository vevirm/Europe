# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2848** (Main **1193** + Historical **1655**)
- Automatic queue still needing V2 verification: **31** (Main **17** + Historical **14**)
- Currently assigned to workers: **25** (Main **11** + Historical **14**)
- Bounded access-recovery retries still eligible: **6**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **6**

## Worker lanes

### Worker A
- Current package: `worker-a-20261104T074951Z-597db88ec598`
- Assigned unresolved records: **24**
  1. `link:https://doi.org/10.1017/eis.2026.10099` — Europe, strategic constraint, and the politics of dependence: Rethinking strength, treaties, and the transatlantic bargain
  2. `link:https://doi.org/10.1365/s43439-026-00177-5` — Enforcing the AI Act at the national level: Germany’s KI-MIG as a blueprint for AI market surveillance in Europe?
  3. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=9d397d4a-d728-11f1-b0c5-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Regulation (EU) 2026/2382 of the European Parliament and of the Council of 21 October 2026 amending Regulations (EC) No 1907/2006, (EC) No 1272/2008, (EU) No 528/2012, (EU) 2019/1021 and (EU) 2021/697 as regards defence readiness and facilitating defence investments and conditions for defence industry - Publications Office of the EU
  4. `link:https://doi.org/10.1016/j.sftr.2026.102267` — Energy dependence, industrial structure, and growth in the EU
  5. `link:https://doi.org/10.1163/15718166-12340224` — Balancing National Security and Non-Refoulement: the Securitization of EU Migration Policies and the Crisis of Fundamental Rights
  6. `link:https://ecfr.eu/wp-content/uploads/2026/11/Pulling-together-A-European-partnership-model-for-decarbonisation.pdf` — Pulling together: A European partnership model for decarbonisation – European Council on Foreign Relations
  7. `link:https://doi.org/10.1111/jcms.70130` — Asymmetric Regulatory Embeddedness and Post‐Brexit Governance: Explaining Adaptive Convergence in the United Kingdom
  8. `link:https://doi.org/10.1016/j.tfp.2026.101514` — Wood availability and export pressure associated with major forest disturbances: A comparative analysis of industrial roundwood flows in Slovenia and Czechia
  - … plus 16 more in the package manifest

### Worker B
- Current package: `worker-b-20261101T092736Z-c510784a458c`
- Assigned unresolved records: **1**
  1. `historical:id:8b6f795f74a8f736` — Trump's trade attack on China – who laughs last?

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
