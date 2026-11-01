# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2816** (Main **1177** + Historical **1639**)
- Automatic queue still needing V2 verification: **8** (Main **7** + Historical **1**)
- Currently assigned to workers: **8** (Main **7** + Historical **1**)
- Bounded access-recovery retries still eligible: **7**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261101T094856Z-d0bc2e070126`
- Assigned unresolved records: **7**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=ab289355-d3aa-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU)2019/881 (The Cybersecurity Act 2) – Title II (ENISA) - Presentation by the Presidency - Publications Office of the EU — recovery attempt 2/3
  2. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=edc102a9-d3b0-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) – Title II (Fees), Articles 47 - Presentation by the Commission - Publications Office of the EU — recovery attempt 2/3
  3. `link:https://doi.org/10.1080/03068374.2026.2740496` — THE MAGHREB AND THE MIDDLE KINGDOM: CHINA’S EV SUPPLY-CHAIN DIPLOMACY IN AN ERA OF GEOPOLITICAL RIVALRY — recovery attempt 2/3
  4. `link:https://doi.org/10.1016/j.respol.2026.105657` — The effects of national security assessments in public procurement on competition, sustainability, innovation, and critical technology procurement — recovery attempt 2/3
  5. `link:https://doi.org/10.1080/13563467.2026.2751110` — The semi-periphery's ‘defence dividend’: redistribution of labour in Europe's defence industry — recovery attempt 2/3
  6. `link:https://doi.org/10.1080/13563467.2026.2751102` — Globalization unravelling? ASML and the geopolitics of Europe-China tech decoupling — recovery attempt 2/3
  7. `link:https://doi.org/10.1016/j.erss.2026.105047` — Monopolising the green transition: China's structural dominance and selective weaponisation of critical raw materials in Europe — recovery attempt 2/3

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
