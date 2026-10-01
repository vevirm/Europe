# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **931** (Main **513** + Historical **418**)
- Automatic queue still needing V2 verification: **793** (Main **172** + Historical **621**)
- Currently assigned to workers: **78** (Main **20** + Historical **58**)
- Bounded access-recovery retries still eligible: **220**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **715**

## Worker lanes

### Worker A
- Current package: `worker-a-72864c47788f`
- Assigned unresolved records: **36**
  1. `link:https://www.atlanticcouncil.org/wp-content/uploads/2026/09/Europe-Gulf-Forum-Policy-Brief-Trade.pdf` — Trade and connectivity in the Europe-Gulf strategic partnership
  2. `link:https://doi.org/10.1080/09654313.2026.2684528` — Technological diversification through global value chains in European regions
  3. `link:https://www.atlanticcouncil.org/wp-content/uploads/2026/09/Europe-Gulf-Forum-Policy-Brief-Investment.pdf` — The strategic rationale for closer investment ties between Europe and the Gulf
  4. `link:https://doi.org/10.1080/00343404.2026.2681659` — The geography of artificial intelligence in European regions: innovation, exposure and use
  5. `link:https://www.atlanticcouncil.org/wp-content/uploads/2026/09/Europe-Gulf-Forum-Policy-Brief-Energy.pdf` — How Europe and the Gulf can unite behind an energy-transition agenda
  6. `link:https://www.atlanticcouncil.org/wp-content/uploads/2026/09/Europe-Gulf-Forum-Policy-Brief-Defense-1.pdf` — Three principles to guide European-Gulf defense cooperation
  7. `link:https://doi.org/10.1007/s00168-026-01555-x` — The role of twin skills in attracting FDI: evidence from European regions
  8. `link:https://doi.org/10.1016/j.glt.2026.06.001` — Agricultural sustainable development goals in the EU: The role of global value chains
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-866c3aaf0914`
- Assigned unresolved records: **36**
  1. `historical:id:d47b3c10f2ea639f` — Geopolitics of the green transition and improving EU’s economic security
  2. `historical:id:1beafac8cb12a4af` — France 2024 Digital Decade Country Report | Shaping Europe’s digital future
  3. `historical:id:ce044422ec4b9617` — Foreign Subsidies Instrument - BusinessEurope comments on the draft implementing regulation
  4. `historical:id:15ab47a803eb4167` — Finland 2025 Digital Decade Country Report | Shaping Europe’s digital future
  5. `historical:id:f2b04839b1a9ca0a` — Finland 2024 Digital Decade Country Report | Shaping Europe’s digital future
  6. `historical:id:414317a08015bf8c` — Evaluation and possible revision of the current EU framework for the screening of investments into the Union - Letter from Markus J. Beyrer to Valdis Dombrovskis
  7. `historical:id:2a5bccb5c473c329` — European Critical Raw Materials Act
  8. `historical:id:6952f3749b24463e` — Estonia 2025 Digital Decade Country Report | Shaping Europe’s digital future
  - … plus 28 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **6**
  1. `link:https://doi.org/10.1177/2336825x261466891` — Ukraine and the transformation of French strategic imaginaries: The discursive reconfiguration of European strategic autonomy under the presidency of Emmanuel Macron (2017-2026) — recovery attempt 2/3
  2. `link:https://doi.org/10.1093/hrlr/ngag015` — Finding a bridge between Erga Omnes obligations and WTO agreements: the case of human rights-based export controls on cyber-surveillance items — recovery attempt 2/3
  3. `link:https://doi.org/10.4324/9781003756637-13` — The EU-Japan Strategic Partnership Agreement (SPA) — recovery attempt 2/3
  4. `link:https://doi.org/10.1080/09662839.2026.2700180` — Institutionalising defence production: reconceptualising the role of institutions and states in European defence industrial policy — recovery attempt 2/3
  5. `link:https://doi.org/10.1177/17816858261489016` — European autonomy, competitiveness and security in the new space era — recovery attempt 2/3
  6. `link:https://doi.org/10.1080/09662839.2026.2700178` — European arms production: A re-conceptualisation of the defence technological and industrial base, industrial policy and hybrid governance — recovery attempt 2/3

## Terminally dropped after failed scans

These records no longer consume automatic Deep Scan slots and are excluded from active reasoning after three failed attempts. Re-open one only by explicitly resetting its work-state entry after materially new evidence becomes available.

- `link:https://doi.org/10.1093/ser/mwag003` — **Green monetary transitions? Central banking and climate finance in Europe and China** — attempts: 3/3 — Socio-Economic Review — 2026-07-09 — Identity was verified, but substantive evidence remained inaccessible or too thin after the required recovery search. — https://doi.org/10.1093/ser/mwag003
