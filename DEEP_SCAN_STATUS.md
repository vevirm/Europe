# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3217** (Main **1385** + Historical **1832**)
- Automatic queue still needing V2 verification: **67** (Main **51** + Historical **16**)
- Currently assigned to workers: **65** (Main **50** + Historical **15**)
- Bounded access-recovery retries still eligible: **23**
- Dropped after three failed recovery passes (archived): **189**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **2**

## Worker lanes

### Worker A
- Current package: `worker-a-20261121T065030Z-fc8aa073eb5d`
- Assigned unresolved records: **36**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=ef4e43e5-e4c5-11f1-b745-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Working Party on Competitiveness and Growth (Public Procurement) - Publications Office of the EU
  2. `link:https://celis.institute/scaling-up-screening-out-economic-security-in-the-eus-draft-merger-guidelines/#download-pdf` — Scaling Up, Screening Out: Economic Security in the EU’s Draft Merger Guidelines - CELIS Institute
  3. `link:https://doi.org/10.1080/11926422.2026.2757589` — Geopolitical icebergs of the High North: the Arctic frontier of Nordic diplomacy
  4. `link:https://www.ispionline.it/wp-content/uploads/2026/11/REPORT-DELOITTE-MedDialogue_WEB.pdf` — The Digital Divide in the Mediterranean: Different Speeds and a Fragmented Agenda | ISPI
  5. `link:https://cdn.ceps.eu/2026/11/2026-08-Industrial-Policy-Explainer.pdf` — Getting European industrial policy right: some key lessons from around the world – CEPS
  6. `link:https://www.europarl.europa.eu/RegData/etudes/BRIE/2024/757615/EPRS_BRI(2024)757615_EN.pdf` — Digital trade policy: The EU's approach to shaping digital trade rules
  7. `link:https://doi.org/10.1016/j.fub.2026.100196` — Three regulations, no common language: Standardising process costing for EU critical raw materials governance
  8. `link:https://www.bruegel.org/external-publication/chinas-anti-dumping-investigation-pork-imports-europe-calibrated-retaliation` — China’s anti-dumping investigation on pork imports from Europe: a calibrated retaliation
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261121T065040Z-ec94ffae757a`
- Assigned unresolved records: **29**
  1. `historical:id:d7c4465bd4ccf392` — (Not) Coming of age? Unpacking the European Union’s quest for strategic autonomy in security and defence
  2. `historical:id:ac2f3945b30838ca` — Exempting Least Developed Countries from Border Carbon Adjustments: Simple Economically but Complex Legally
  3. `historical:id:42e7201c0b2af893` — EU and Russian Hegemony in the 'Shared Neighbourhood': Between Coercion, Prescription, and Co-optation
  4. `historical:id:8f4a482461ab316a` — States, firms, and security: How private actors implement sanctions, lessons learned from the Netherlands
  5. `historical:id:568c10f15cb9cfc2` — The EU-Japan free trade agreement in evolving global trade politics
  6. `historical:id:d973a6232f08ea25` — Lithuania, Latvia and Estonia: Euro-Atlantic consolidation
  7. `historical:id:729a734abf1d8ced` — EU-Japan EPA a “Stumbling Block or a Stepping Stone” toward Multilateralism for Food and Beverages
  8. `historical:id:6662f2a2c5ad46e2` — EU Sanctions against Russia: A Punishment, a Signal of Displeasure or a Wild-Goose Chase
  - … plus 21 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
