# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2835** (Main **1180** + Historical **1655**)
- Automatic queue still needing V2 verification: **20** (Main **19** + Historical **1**)
- Currently assigned to workers: **14** (Main **13** + Historical **1**)
- Bounded access-recovery retries still eligible: **6**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **6**

## Worker lanes

### Worker A
- Current package: `worker-a-20261103T083240Z-99bf5fe41ff7`
- Assigned unresolved records: **13**
  1. `link:https://rhg.com/wp-content/uploads/2026/11/Chinas-Chemicals-Capacity-Buildout.pdf` — Global Impacts of China’s Chemicals Buildout
  2. `link:https://doi.org/10.1057/s41278-026-00374-3` — Economic impact of Smart Ports on the national economy: an input–output analysis applied to Portugal
  3. `link:https://doi.org/10.1016/j.nbsj.2026.100386` — Value Chain analysis of Nature-based Solutions in Europe: Understanding Demand, Supply, and Mainstreaming Potential
  4. `link:https://doi.org/10.48550/arxiv.2610.39573` — Cybersecurity Practices in Industrial Automation and Control Systems: a Study of Croatian System Integrators
  5. `link:https://doi.org/10.1016/j.sftr.2026.101912` — Locating dry ports in the function of maritime logistics
  6. `link:https://www.cer.eu/sites/default/files/EV_eu_gas_2.11.26.pdf` — The EU must make the Hormuz crisis a turning point
  7. `link:https://doi.org/10.48550/arxiv.2610.40494` — AI in the EGI e-infrastructure -- Past experiences and future strategies
  8. `link:https://doi.org/10.1007/s13563-026-00720-0` — From global rare earth resources to the EU supply security: An overview on primary and alternative resources and strategic pathways
  - … plus 5 more in the package manifest

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
