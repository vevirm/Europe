# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2971** (Main **1245** + Historical **1726**)
- Automatic queue still needing V2 verification: **37** (Main **28** + Historical **9**)
- Currently assigned to workers: **32** (Main **23** + Historical **9**)
- Bounded access-recovery retries still eligible: **18**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **5**

## Worker lanes

### Worker A
- Current package: `worker-a-20261108T094504Z-f060e1f433f8`
- Assigned unresolved records: **32**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=93107309-d4af-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — WORKING PARTY ON COMPETITIVENESS AND GROWTH (Industry) (Chips Act 2.0) - Publications Office of the EU
  2. `link:https://doi.org/10.1016/j.esr.2026.102389` — Reassessing the EU’s LNG expansion strategy: Geopolitical dependencies, energy security, and climate goals after the Russian invasion of Ukraine
  3. `link:https://doi.org/10.1080/10168737.2026.2692699` — European Manufacturing Exports and Exposure to Chinese ICT Services
  4. `link:https://doi.org/10.1080/1540496x.2026.2755507` — How the EU Regulates the Outflow of Emerging Technologies: A Perspective from China
  5. `link:https://doi.org/10.1016/j.resourpol.2026.106086` — Blurred lines between governments and firms: A competitiveness framework for critical raw material dependent industries
  6. `link:https://doi.org/10.1002/eet.70160` — Discursive Alignment in EU Palm Oil Policy: How Securitisation Legitimises Ecological‐Neocolonial Governance
  7. `link:https://doi.org/10.1080/09662839.2026.2749007` — When arms embargoes become procurement problems: Spain, Israel and normative decoupling in defence acquisition
  8. `link:https://doi.org/10.1080/14767724.2026.2758677` — Will Europe be able to align and accelerate global cooperation in S&T to foster a new knowledge-based global order ?
  - … plus 24 more in the package manifest

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
