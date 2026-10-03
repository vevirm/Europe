# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1378** (Main **591** + Historical **787**)
- Automatic queue still needing V2 verification: **503** (Main **199** + Historical **304**)
- Currently assigned to workers: **78** (Main **12** + Historical **66**)
- Bounded access-recovery retries still eligible: **344**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **425**

## Worker lanes

### Worker A
- Current package: `worker-a-e85cffa12c1e`
- Assigned unresolved records: **36**
  1. `historical:id:352c7880ec11c848` — TTIP and legislative‒executive relations in EU trade policy
  2. `historical:id:ff65784915ce6d7e` — Friendly Fire: The Trade Impact of the Russia Sanctions and Counter-Sanctions - Kiel Institute
  3. `historical:id:57c00e90c31fd599` — European Industrial Policy — Tapping the Full Growth Potential of the EU
  4. `historical:id:8e744b94e8f4bbf1` — The transatlantic dialogue on Iran: the European subaltern and hegemonic constraints in the implementation of the 2015 nuclear agreement with Iran
  5. `historical:id:ef24e3c21d9d6e9f` — <i>European Communities – Definitive Anti-Dumping Measures on Certain Iron or Steel Fasteners from China</i> – <i>Recourse to Article 21.5 of the DSU by China</i> (<i>EC–Fasteners (China) (Article 21.5–China)</i>, DS397)
  6. `historical:id:fb71ead5f0e1aa55` — Mercosur Is Not Really a Free Trade Agreement, Let Alone a Customs Union
  7. `historical:id:3ffa2f842d5560ac` — Study on firm-level drivers of export performance and external competitiveness in Italy
  8. `historical:id:a6ce2ce14214d616` — The geopolitical impact of the shale revolution: Exploring consequences on energy prices and rentier states
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-8cfbbeac458a`
- Assigned unresolved records: **36**
  1. `historical:id:bcdf19da059ff649` — European Union and the United States of America: Facilitation of electronic trade through the EU-U.S. Privacy Shield - Global Trade Alert
  2. `historical:id:a498b360a80cf7b9` — Enforcement and sanctions
  3. `historical:id:d08becd62872809e` — EU Energy Security beyond Ukraine: Towards Holistic Diversification
  4. `historical:id:b078d4edbfbff8d7` — All or nothing? European and British strategic autonomy after the Brexit - Egmont Institute
  5. `historical:id:c42491bbdca3f8fa` — <scp>EU</scp> Trade Preferences and Export Diversification
  6. `historical:id:33fdcfd918811fd8` — The European Union and the African Union: A Strategic Partnership?
  7. `historical:id:c316658669597204` — Like-minded partners in the Asia-Pacific region? The EU’s expanding relationship with Australia
  8. `historical:id:9f456c30c2da0866` — The structuration of Russia’s geo-economy under economic sanctions
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
