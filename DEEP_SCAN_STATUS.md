# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3112** (Main **1327** + Historical **1785**)
- Automatic queue still needing V2 verification: **59** (Main **39** + Historical **20**)
- Currently assigned to workers: **41** (Main **24** + Historical **17**)
- Bounded access-recovery retries still eligible: **18**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **18**

## Worker lanes

### Worker A
- Current package: `worker-a-20261116T070203Z-25c8bd2bf358`
- Assigned unresolved records: **36**
  1. `link:https://data.consilium.europa.eu/doc/document/ST-10228-2026-INIT/en/pdf` — Changes compared to the previous Presidency compromise text, set out in document 9694/26, are indicated in bold underline / bold strikethrough.
  2. `link:https://defence-industry-space.ec.europa.eu/advanced-sensors-next-generation-communications-how-european-defence-fund-helps-european-defence-2026-11-13_en` — From advanced sensors to Next-Generation Communications: How the European Defence Fund helps the European defence industry develop critical technologies
  3. `link:https://defence-industry-space.ec.europa.eu/learning-ukraine-resilience-design-2026-11-13_en` — Learning from Ukraine: Resilience by Design
  4. `link:https://doi.org/10.48550/arxiv.2611.13866` — Economic Benefits of Cross-Border Electricity Trade and Domestic Electricity Production in Switzerland
  5. `link:https://doi.org/10.1080/14683849.2026.2752280` — From customs-union asymmetry to bounded co-management? Strategic autonomy and the CETA-plus free trade agreement alternative in EU–Türkiye trade governance
  6. `link:https://data.consilium.europa.eu/doc/document/ST-13545-2026-INIT/en/pdf` — Changes in comparison to the Commission proposal, document ST 10094/26 + ADD1, are marked in bold for additions and in strikethrough for deletions.
  7. `link:https://doi.org/10.1080/14631377.2026.2757264` — New state capitalist varieties in the Global East in a changing global landscape
  8. `link:https://www.bruegel.org/policy-brief/competing-inputs-how-european-union-can-improve-critical-raw-materials-supply-security#footnoteref_8_Yx1CmaIHi7JdFEzVZrRqoJWzecjzuWs2Aux56ODCN9w_1` — Competing for inputs: how the European Union can improve critical raw materials supply security
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261116T070207Z-162cd0dae8a9`
- Assigned unresolved records: **5**
  1. `historical:id:da75becd743726ac` — Anticipating China’s Military Coercion of Taiwan
  2. `historical:id:1cebea2a3b9470ae` — After declaring NATO "brain-dead" has President Macron brought Europe any closer to strategic autonomy ?
  3. `historical:id:9e16d4f3a4dd6a54` — Hybrid Warfare: Escalation in Europe and Implications for European Union and North Atlantic Treaty Organization
  4. `historical:id:e5af6c376410fa26` — Economic, trade and development relations between South Africa and the European Union: The end of a strategic partnership? A South African perspective
  5. `historical:id:17ba50261a1fbe68` — Europe and India: Relaunching a Troubled Trade Relationship

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
