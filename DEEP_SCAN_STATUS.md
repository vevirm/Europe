# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3305** (Main **1432** + Historical **1873**)
- Automatic queue still needing V2 verification: **85** (Main **46** + Historical **39**)
- Currently assigned to workers: **72** (Main **42** + Historical **30**)
- Bounded access-recovery retries still eligible: **11**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **13**

## Worker lanes

### Worker A
- Current package: `worker-a-20261125T101325Z-b0caa28d28ac`
- Assigned unresolved records: **36**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=89ee2aa7-e82f-11f1-b745-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — WORKING PARTY ON COMPETITIVENESS AND GROWTH (Internal Market) - Publications Office of the EU
  2. `link:https://doi.org/10.34135/sjps.260103` — Energy Security After Diversification: Is The European Union Entering A Post-Crisis Vulnerability Trap?
  3. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=823056c0-e6de-11f1-b745-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Notice of initiation of a review of the anti-dumping measures applicable to imports of fatty acid originating in Indonesia, following the recommendations and rulings adopted by the Dispute Settlement Body of the World Trade Organisation in the European Union – Anti-Dumping Measures on Imports of Fatty Acid from Indonesia dispute (DS622) - Publications Office of the EU
  4. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=75c13ec6-e74e-11f1-b745-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Preparation of the Meeting of the Council (Competitiveness (Internal Market, Industry, Research and Space)) on 3-4 December 2026 Regulation on the safety, resilience and sustainability of space activities in the Union (EU Space Act) - Progress Report - Publications Office of the EU
  5. `link:https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/797050/EPRS_BRI(2026)797050_EN.pdf` — Integrating Ukraine's defence industry into the EU defence industrial base
  6. `link:https://www.bruegel.org/first-glance/made-eu-coalition-willing-economic-security-and-decarbonisation` — From ‘Made in EU’ to a coalition of the willing on economic security and decarbonisation
  7. `link:https://doi.org/10.1111/jcms.70197` — From Transatlantic Crisis to European Adaptation? The European Union's Geopolitical Stress Test in 2025
  8. `link:https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/797051/EPRS_BRI(2026)797051_EN.pdf` — EU households' savings and investments
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261125T101332Z-a461ae946e15`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMiswFBVV95cUxQMFVFWVdsaVFNbTNXTEJjemxBZm03WlZIX0NKdkhKVkhYNTZ3WVJPSm5zRHNuQTF6RHFQLTNLMVI1VEctOWF2T2JSYlloc0FaVktVTWVfVUlWZ0t4UEhmeE5XdnlqN0xwUldKdk01MHI2UG8ybm91WVV6NmVyN2F5Zkh3ekZDSHhxQXUteWRHVVdYVEZkdURqa2MtZmhzZnB6a3lwQ0FzeVFJQURMT1hXcDB4VQ?oc=5` — German Industry Proposes Trading House to Secure Critical Raw Materials
  2. `link:https://news.google.com/rss/articles/CBMitAFBVV95cUxQd3FhZU5pZGJLN2ZJUzNrMDJybkl6SV9fbW14Y2hNTHRYajVmUmEzZVY5QzgyZkE2U2t3MjVaOUFTcXVPbjhCQkpWX1lKZTNsbm9jMEwyWTJHQldZcHZFU2FoZmNsLTYzclM5bzVLS3M2XzZQcFpUMWp1NnlNWWJ2enBJeUg3bnhXQVN4WWJVTjNCZ3Q5NWpaOTNUZGEySnhBY2lfbVQySTd4dUdvdG05cVFYWTc?oc=5` — EU-India: Joint Press Release on the 7th Strategic Partnership Review Meeting in New Delhi - European External Action Service (EEAS)
  3. `link:https://news.google.com/rss/articles/CBMiwwFBVV95cUxQU0pwbkJPVTFZbU1zXzlVRlVjc3ljalJncnFvMS03d2REeGJzMG1kZDBRUFYzaVdUSDg5b0ptenlScXhFWGhIdHVmT0dybWtPN2RrWVMybUdKV3VzNENMemtuX1JpRVg1WURkTjJzUTM2d242SHJueGVxR3F5OUctMnJHeUxSOHQ2Z1o3UDVmMUV0U0w4RUlOdllFdTl2SjJvUnFTc3J6NEVzclgwVUZMaXFWSVVtMnZkNFVteElaUUFuSWs?oc=5` — China calls on Switzerland to help resolve EU trade rift, oppose 'Taiwan independence'
  4. `link:https://news.google.com/rss/articles/CBMi7wFBVV95cUxNODc0MU5BeGxvTGw3R3hMSGtYejhtblZKYjRaNFRDdEpPR2lYNmhhampVeXdMNkh5NHV4QkdMeTd0aDVlWDBwVTFQZTEtX3N4NFNQZl8xbjV4em9KN2NfYlhIWWU1MW85RzVrVHg1N1NDdC12STlhUThWMTFtOHdHVU94dHVkRURSeGFvekxuS0JqUkcwdnRZN2dhUEh2aV9NUGNfZHJiVmc3SVVTNkxEZHZfaFdqVm5yWWFLdmZIMjJEVEY1dTl0YWc1MjdZcS1KMV9ta2w4RzJTY3NhWGNfT1hfTTBGRkZmbTUwVHNRbw?oc=5` — Opposition to data centers grows worldwide, from India to Chile, via Ireland and Japan - Le Monde.fr
  5. `historical:id:c83fa3e157abfa5d` — The Geoeconomic Turn on Stage: National Identity and the Interpretation of the EU's Trade Sustainability Diplomacy in Indonesia and Vietnam
  6. `historical:id:30319a6c107274a9` — Hungary’s path to the euro: five tests for a sustainable adoption strategy
  7. `historical:id:6cc3cd48411deef2` — India-EU Strategic Partnership, Still A Long Way To Go - Egmont Institute
  8. `historical:id:f6acd4608a108388` — trade policy | Bruegel | The Brussels-based economic think tank
  - … plus 28 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
