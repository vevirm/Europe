# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2816** (Main **1177** + Historical **1639**)
- Automatic queue still needing V2 verification: **26** (Main **9** + Historical **17**)
- Currently assigned to workers: **19** (Main **2** + Historical **17**)
- Bounded access-recovery retries still eligible: **7**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **7**

## Worker lanes

### Worker A
- Current package: `worker-a-20261102T152113Z-2b1cc2661e2a`
- Assigned unresolved records: **18**
  1. `link:https://doi.org/10.1016/j.ijhydene.2026.158363` — Process analysis of low-temperature steam reforming of DME with integrated carbon capture
  2. `link:https://doi.org/10.1016/j.scs.2026.108044` — Monitoring and forecasting of urban air pollution and exceedance events: implications for environmental risk assessment and early warning communication using machine learning in sustainable cities
  3. `historical:id:c7be77885788319e` — Macroeconomic and institutional impacts of energy security risk in the European Union
  4. `historical:id:52a10b4b2e05351c` — Joris Teer on China's rare earth export controls
  5. `historical:id:01668b1a0bb8a4a8` — "European countries are also likely to be boycotted if China really wants to stop [rare earth] exports to the US"
  6. `historical:id:d19cfd4c9521443f` — Does Europe want to become the supercontinent of raw materials?
  7. `historical:id:6199d285ad497b8a` — European Union Enlargement and Geopolitical Power in the Face of War
  8. `historical:id:1961cb046d0a1dfb` — Behind the façade of the Hague Summit, the disintegration of the transatlantic link - Institut Jacques Delors
  - … plus 10 more in the package manifest

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
