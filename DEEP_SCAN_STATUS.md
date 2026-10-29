# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2731** (Main **1129** + Historical **1602**)
- Automatic queue still needing V2 verification: **50** (Main **30** + Historical **20**)
- Currently assigned to workers: **45** (Main **25** + Historical **20**)
- Bounded access-recovery retries still eligible: **1**
- Dropped after three failed recovery passes (archived): **177**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **5**

## Worker lanes

### Worker A
- Current package: `worker-a-20261029T092154Z-3766c6c7dc64`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1016/j.euroecorev.2026.105501` — Reassessing the benefits of European integration and the European Union’s ability to achieve strategic autonomy
  2. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=41efa9e7-d253-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Member States' consolidated comments on Presidency third compromise text on the recitals and Title III (Certification) - Publications Office of the EU
  3. `link:https://ecipe.org/wp-content/uploads/2026/10/ECI_26_PolicyBrief_15-2026_LY02.pdf` — Changing South Caucasus: Time for EU Leadership
  4. `link:https://www.businesseurope.eu/wp-content/uploads/2026/10/2026-10-BusinessEurope_Benchmarking-of-competitiveness-checks.pdf` — Benchmarking competitiveness checks used in selected EU impact assessments from 2025-2026 - a BusinessEurope position paper
  5. `link:https://defence-industry-space.ec.europa.eu/commission-disburses-eur286-billion-ukraine-drones-missiles-and-urgent-battlefield-needs-2026-10-27_en` — Commission disburses €2.86 billion to Ukraine for drones, missiles and urgent battlefield needs
  6. `link:https://www.businesseurope.eu/wp-content/uploads/2026/10/2026-10-28-Joint-Statement_Tax-Simplification-Package.pdf` — Europe cannot prosper under the weight of unnecessary complexity - Joint statement by 23 business, financial and professional associations
  7. `link:https://doi.org/10.47287/cen.479100.newsarticle` — European nations push for tougher trade measures on China
  8. `link:https://doi.org/10.1787/10379f9f-en` — SME Policy Index for Western Balkans and Türkiye 2026 – Economy Profile for Türkiye
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261029T092204Z-3f888158976a`
- Assigned unresolved records: **9**
  1. `historical:id:203e40e2773fc500` — Working with the EU: How Discourses Shape the Application of EU State Aid Rules
  2. `historical:id:e25492ca0cdc7c23` — The Impact of Natural Gas Prices on Electricity Tariffs in the UK
  3. `historical:id:06211c3d0f1fa8a4` — Next level partnership - Bolstering EU-NATO cooperation to counter hybrid threats in the Western Balkans
  4. `historical:id:70497d61af6609b7` — Sanction-proof or sanction-hit: How can the EU make Putin’s evil war even more costly
  5. `historical:id:1c5ae0e8eb7014a6` — Russia-Ukraine: Short-Term Energy Security Doctrines, Long-Term Climate Damage?
  6. `historical:id:0cc1df006c1dd60e` — Russia, Gas And The European Union: An Explosive Mix
  7. `historical:id:fe965befe0714a77` — Gas and the Energy Transition: Japan’s Turnaround
  8. `historical:id:4909a12b32ed339d` — Gas and the Energy Transition: China’s Pragmatism
  - … plus 1 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
