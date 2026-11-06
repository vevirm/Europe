# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2870** (Main **1202** + Historical **1668**)
- Automatic queue still needing V2 verification: **65** (Main **37** + Historical **28**)
- Currently assigned to workers: **56** (Main **29** + Historical **27**)
- Bounded access-recovery retries still eligible: **8**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **9**

## Worker lanes

### Worker A
- Current package: `worker-a-20261106T071712Z-c27611082ad8`
- Assigned unresolved records: **36**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=b16139b4-d89d-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — WORKING PARTY ON COMPETITIVENESS AND GROWTH (Internal Market) - Publications Office of the EU
  2. `link:https://cdn.ceps.eu/2026/11/2026-13-FMI-Digital-euro-1.pdf` — Governing the digital euro ecosystem – CEPS
  3. `link:https://data.consilium.europa.eu/doc/document/WK-11040-2026-INIT/en/pdf` — Handling and further distribution are under the sole responsibility of community members.
  4. `link:https://doi.org/10.1016/j.ijggc.2026.104813` — Decision-making and coordination in bio-CCUS value chains: Finnish companies, municipalities, and the role of national and EU-level policy
  5. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=614a4c42-d7fe-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — SET plan progress report 2026 - Publications Office of the EU
  6. `link:https://doi.org/10.1016/j.marpol.2026.107242` — Economic growth and CO₂ emissions in the EU’s primary maritime sector: Evidence of decoupling?
  7. `link:https://doi.org/10.1111/jcms.70186` — State Aid Compatibility Beyond State Aid Law? Public Procurement and the Inextricable Link Doctrine After Paks II
  8. `link:https://doi.org/10.1016/j.apenergy.2026.128902` — Can they compete? Cost competitiveness of non-light-water reactors for heat and power supply in a decarbonized european energy system
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261106T071728Z-5e45ec99a98a`
- Assigned unresolved records: **20**
  1. `historical:id:97e8139fb8c2279e` — Is there a ‘China problem’ and how can the World Trade Organization address it?
  2. `historical:id:feabb1638e72f44a` — Trade Disintegration and Agri‐Food Trade: <scp>United Kingdom</scp> Exit From <scp>EU</scp>
  3. `historical:id:9e457378aa37000a` — European Competitiveness: Lessons from the IRA
  4. `historical:id:c6a3284f33fdfb8e` — Europe urgently needs a common strategy on Russian gas
  5. `historical:id:25b8d52a20196591` — A European circular single market for economic security and competitiveness
  6. `historical:id:a9fdaa8f581dfd8a` — Industrial policy for economic security
  7. `historical:id:6f623c4248d0ecb5` — The end of Russian gas transit via Ukraine and options for the EU
  8. `historical:id:ec11ad9cfde22bbb` — How to de-risk: European economic security in a world of interdependence
  - … plus 12 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
