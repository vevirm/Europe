# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3263** (Main **1419** + Historical **1844**)
- Automatic queue still needing V2 verification: **68** (Main **32** + Historical **36**)
- Currently assigned to workers: **65** (Main **29** + Historical **36**)
- Bounded access-recovery retries still eligible: **21**
- Dropped after three failed recovery passes (archived): **189**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **3**

## Worker lanes

### Worker A
- Current package: `worker-a-20261123T060941Z-804b42fa0413`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1080/09692290.2026.2762334` — Strategic regulatory engagement in multipolar value chains: contesting the EU Deforestation regulation in the Global South
  2. `link:https://doi.org/10.1017/eds.2026.10070` — The relative importance of drought-related and structural economic factors in explaining regional economic performance across Europe: an explainable machine-learning approach
  3. `link:https://doi.org/10.1002/pad.70099` — AI‐Ready Bureaucracies? Assessing Capacity‐Building Approaches in European National AI Strategies
  4. `link:https://doi.org/10.1017/eso.2026.10173` — The Problem of Speed and Scale in Green Transitions: The Failure of Northvolt and the European Battery Industry
  5. `link:https://doi.org/10.1596/45879` — Closing the Energy Efficiency Gap: Unlocking Private-Sector Investment in Poland and Romania
  6. `link:https://doi.org/10.1007/s43681-026-01546-w` — Governing Agentic AI: An Onto-Relational-Sophic (ORS) Framework for Deployment-Sensitive Governance
  7. `link:https://doi.org/10.1016/j.resourpol.2026.106033` — Extraterritorial ESG regulation and mining governance in Peru: Risks of a legislative disconnect
  8. `link:https://doi.org/10.1021/acs.est.6c07336` — Meta Life Cycle Assessment, Techno-Economic Analysis, and Risk Assessment of Carbon Mineralization Pathways to Inform Policy Frameworks
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261123T060949Z-6a4deb5cb704`
- Assigned unresolved records: **29**
  1. `historical:id:2ec10a872ec0f56b` — Gas diversification as a way of strengthening the national security of the Republic of Serbia
  2. `historical:id:23dfa06482ad51ac` — Foreign Direct Investment Regimes Laws and Regulations Report 2024 Austria – ICLG.com - CELIS Institute
  3. `historical:id:2962cffa7cd6c8fb` — Transforming Europe? The EU's industrial policy and geopolitical turn
  4. `historical:id:5c55c26d9349072e` — (Re)conceptualization of the term cybersecurity in the European Union’s security policy
  5. `historical:id:48dc51e33256eed0` — The securitized energy relationship: The EU and Russia political and security discourses
  6. `historical:id:16422698d5ae0f33` — How the EU and the US should overcome their trade and supply chain disputes
  7. `historical:id:5f46c9393ab7729b` — In brief: foreign investment review procedure in Austria – Lexology - CELIS Institute
  8. `historical:id:d4cfe81ac08169ff` — The looming third European gas crisis
  - … plus 21 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
