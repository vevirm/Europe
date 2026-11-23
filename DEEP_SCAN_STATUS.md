# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3277** (Main **1420** + Historical **1857**)
- Automatic queue still needing V2 verification: **40** (Main **19** + Historical **21**)
- Currently assigned to workers: **4** (Main **3** + Historical **1**)
- Bounded access-recovery retries still eligible: **5**
- Dropped after three failed recovery passes (archived): **203**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **36**

## Worker lanes

### Worker A
- Current package: `worker-a-20261123T072413Z-018848806ee4`
- Assigned unresolved records: **4**
  1. `link:https://news.google.com/rss/articles/CBMitgFBVV95cUxPQkxzUWdBcFpHVy01Y3hvOURnd0drNUZuWW9rWC1QQk5GQVV0blFhU0ZnZVFpY2JWaVZrUlVhZ0pOV2hkVmNtUUZ0ODIyVGtxUWx6RU9LNWhJcDJNTjhCYVlvODk2eWYwRHRnbnE0NFAwOGdaQ1BsTFdSWUVFSFBzaHJaVWxDc3NSRF9ZRFVqTk1TdzZTWmNCUDhqLUJsN19YUTl1YUNPMEY0MTNnenN2aHNUeklwdw?oc=5` — Europe tightens sanctions on Russia. America loosens them — recovery attempt 2/3
  2. `link:https://doi.org/10.1596/45855` — Bulgaria Country Climate and Development Report — recovery attempt 2/3
  3. `link:https://doi.org/10.1093/jaenfo/jnag017` — The CNMC’s role in public procurement: key actions and technological developments — recovery attempt 2/3
  4. `historical:id:5f46c9393ab7729b` — In brief: foreign investment review procedure in Austria – Lexology - CELIS Institute — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261123T060949Z-6a4deb5cb704`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
