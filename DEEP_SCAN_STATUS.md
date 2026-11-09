# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2993** (Main **1258** + Historical **1735**)
- Automatic queue still needing V2 verification: **18** (Main **18** + Historical **0**)
- Currently assigned to workers: **6** (Main **6** + Historical **0**)
- Bounded access-recovery retries still eligible: **12**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **12**

## Worker lanes

### Worker A
- Current package: `worker-a-20261109T064737Z-b21eb823da7c`
- Assigned unresolved records: **6**
  1. `link:https://doi.org/10.1080/10220461.2026.2742401` — Securing Africa’s digital backbone: Subsea cable vulnerability and the case for an African critical infrastructure protection regime
  2. `link:https://doi.org/10.1016/j.apenergy.2026.129186` — Critical raw material intensity of electricity generation technologies: A probabilistic and multicriteria approach applied to the European Union
  3. `link:https://doi.org/10.1016/j.inteco.2026.100764` — Energy shocks, war, and supply chain reconfiguration: The case of Italy and Spain in ceramic tiles
  4. `link:https://doi.org/10.1111/issj.70076` — Public Priorities Between Worker Protection and Renewable Power in the AI Transition: Evidence From a Novel Randomized Survey Experiment
  5. `link:https://doi.org/10.1371/journal.pone.0342837` — Limited capital? Explaining transatlantic divergences in artificial intelligence startup financing
  6. `link:https://doi.org/10.1787/b3a6ab2c-en` — Unlocking the potential of intermediary cities for regional development in Brindisi, Italy

### Worker B
- Current package: `worker-b-20261107T111515Z-8d31efbfd461`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
