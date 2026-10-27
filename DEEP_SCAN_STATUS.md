# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2731** (Main **1129** + Historical **1602**)
- Automatic queue still needing V2 verification: **5** (Main **5** + Historical **0**)
- Currently assigned to workers: **5** (Main **5** + Historical **0**)
- Bounded access-recovery retries still eligible: **1**
- Dropped after three failed recovery passes (archived): **177**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261027T211005Z-249432341421`
- Assigned unresolved records: **5**
  1. `link:https://doi.org/10.1016/j.foodpol.2026.103185` — Advancing sustainable food systems cooperation in trade agreements: Lessons from Chile
  2. `link:https://doi.org/10.2478/bjes-2026-0029` — Regulating LLM training under EU copyright law and its linguistic implications for smaller languages such as Estonian
  3. `link:https://doi.org/10.1787/9189105b-en` — OECD Economic Surveys: Slovenia 2026
  4. `link:https://doi.org/10.1080/09662839.2026.2700184` — From national arsenals to European defence: changes in media framings of European defence industries, 2004–2024
  5. `link:https://doi.org/10.1177/16118944261490056` — An Offshore Financial Centre Inside Europe: Luxembourg, Taxation and European Economic Community (1960s–1970s) — recovery attempt 3/3

### Worker B
- Current package: `worker-b-20261027T175216Z-d9afc5af0e51`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
