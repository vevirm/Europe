# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **873** (Main **511** + Historical **362**)
- Automatic queue still needing V2 verification: **827** (Main **174** + Historical **653**)
- Currently assigned to workers: **102** (Main **22** + Historical **80**)
- Bounded access-recovery retries still eligible: **218**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **725**

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
- Current package: `worker-b-99d853700bb3`
- Assigned unresolved records: **60**
  1. `historical:id:88559fe23454a413` — The EU's Autonomous Sanctions Against Russia in 2014 Versus 2022: How Does the Bureaucratic Politics Model Bring in the Institutional ‘Balance of Power’ Within the EU?
  2. `historical:id:80eb832655ab55c6` — Reducing supply risks for critical raw materials – CEPS
  3. `historical:id:8fb9f913c823aa60` — The European Union’s Anti-Coercion Instrument – A Closer Look at Decision-Making under a Politicized Trade Instrument - CELIS Institute - Investment Screening | National Security | Competitiveness
  4. `historical:id:9ecab69560a01cc0` — What's at Stake in the EU Elections: Industrial Policy
  5. `historical:id:695fc8261096919a` — Reassessing the Impact of the Single Market and Its Ability to Help Build Strategic Autonomy
  6. `historical:id:6c5e8252ab75fa85` — Institut Jacques Delors - Strengthening EU green sovereignty through the Critical Raw Materials Act
  7. `historical:id:3c6350161fe3195c` — Green transition, single market and EU’s open strategic autonomy: the impact of state aid
  8. `historical:id:ba386ea6bfad7db0` — Geopolitics and Trade: German Economists Experts' Assessment of Dependencies on China | ifo Institute
  - … plus 52 more in the package manifest

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
