# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3064** (Main **1295** + Historical **1769**)
- Automatic queue still needing V2 verification: **66** (Main **47** + Historical **19**)
- Currently assigned to workers: **48** (Main **32** + Historical **16**)
- Bounded access-recovery retries still eligible: **18**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **18**

## Worker lanes

### Worker A
- Current package: `worker-a-20261114T084302Z-979cc7bba93c`
- Assigned unresolved records: **36**
  1. `link:https://data.consilium.europa.eu/doc/document/WK-16142-2026-INIT/en/pdf` — Handling and further distribution are under the sole responsibility of community members.
  2. `link:https://doi.org/10.1007/s43621-026-04286-3` — Collateral damage of the EU deforestation regulation on commodity supply chains in cocoa, coffee, palm oil, soy, and cattle value chains
  3. `link:https://doi.org/10.1007/s42461-026-01764-0` — Comparative Life Cycle Assessment of Spodumene Processing Routes for Battery Grade Lithium Hydroxide Production in Australia, China and Finland
  4. `link:https://doi.org/10.1007/s13563-026-00700-4` — Critical metal supply risks for EU electric vehicle batteries: supply-demand misalignments under production and recycling scenarios
  5. `link:https://www.cer.eu/sites/default/files/brejoin_CG_11.11.26.pdf` — Brejoin? Ten reflections on Britain rejoining the EU
  6. `link:https://doi.org/10.1007/s10290-026-00663-2` — Protection of geographical indications in trade agreements: Is it worth it?
  7. `link:https://doi.org/10.1080/10438599.2026.2760887` — Not all digital inputs are equal: regional linkages and global value chain upgrading in Europe
  8. `link:https://ecfr.eu/wp-content/uploads/2026/11/Deutschland-First-What-the-rise-of-the-AfD-means-for-Europe-v4.pdf` — Deutschland First: What the rise of the AfD means for Europe – European Council on Foreign Relations
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261114T084316Z-8992a7a130bf`
- Assigned unresolved records: **12**
  1. `historical:id:634e0a78b0db32db` — Experience and knowledge sharing study tour on SADC-EU Partnership Agreement (EPA) safeguard measures and trade remedies provisions, for trade officials from Angola and Mozambique
  2. `historical:id:3259aa1fe60ec931` — Security of gas supply
  3. `historical:id:2a1784aefa7dd3d6` — Human rights sanctions and the role of black knights: Evidence from the EU’s post-Soviet neighbours
  4. `historical:id:cc68b22be826e61e` — COVID-19 Report for Life Sciences and Health Care Companies (UPDATED) – JD Supra - CELIS Institute
  5. `historical:id:ba3d20fa75f871b1` — COVID-19 Report for Life Sciences and Health Care Companies – Lexology - CELIS Institute
  6. `historical:id:a02a222c7d62cbd5` — Congress Needs to Fight Weaponized Corruption by Russia and Other Actors – Foreign Policy - CELIS Institute
  7. `historical:id:618312e34cf59893` — Commission Report Calls for Investments, ‘Significant Change in Mindset’ to Meet AI Challenges – HSToday - CELIS Institute
  8. `historical:id:e8051ad02a8d9300` — Chinese Acquisitions of Western Tech Firms Are Only Part of the Problem. Secret Venture Capital Is Handing Power to Beijing. – Foreign Policy - CELIS Institute
  - … plus 4 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
