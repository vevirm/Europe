# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **814** (Main **497** + Historical **317**)
- Automatic queue still needing V2 verification: **873** (Main **175** + Historical **698**)
- Currently assigned to workers: **126** (Main **23** + Historical **103**)
- Bounded access-recovery retries still eligible: **218**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **747**

## Worker lanes

### Worker A
- Current package: `worker-a-e29593a73a40`
- Assigned unresolved records: **60**
  1. `link:https://dfrlab.org/2026/08/17/sovereignty-without-borders-decoding-the-transatlantic-digital-relationship-at-a-time-of-change/` — Sovereignty without borders: Decoding the transatlantic digital relationship at a time of change
  2. `link:https://ecfr.eu/wp-content/uploads/2026/09/Little-Venice-little-Sparta-The-UAEs-statecraft-meets-the-war-on-Iran-v2.pdf` — Little Venice, little Sparta: The UAE’s statecraft meets the war on Iran – European Council on Foreign Relations
  3. `link:https://doi.org/10.1177/01956574261473489` — Can Domestic Carbon Markets Buffer the Impact of EU Border Taxes? A Stochastic Frontier Analysis of Decarbonization Costs in India’s Energy-Intensive Industries
  4. `link:https://digital-strategy.ec.europa.eu/en/activities/study-identify-digital-technologies-next-eu-research-and-innovation-fund` — Study to identify key strategic digital technologies for EU research and innovation funding beyond 2027
  5. `link:https://doi.org/10.18288/1994-5124-2026-4-94-109` — Assessing the Impact of Sanctions on the Dynamics of the Russian Economy From 2022 to 2024
  6. `link:https://news.google.com/rss/articles/CBMipwFBVV95cUxObk80WDhOeFJjTzFUMDY5dElGaGdHbFhkWElPSlZDU3psZWU2ZVpxNWRYejYzZHJhOHIwMWI0SEw3eHQ1N1BaMnVoOE5hbzBMRWJWbWF6RFpZOUFIN0l6ZUowSFZoaDMteW9aTFhNQkxPaHlqWDdDZlVYUHVGUTdwbnZIYnJKdjBUQXNJejRWRDBxNXVzNm1reVNTOGF6eW42NWViLWhTQQ?oc=5` — EIB and BNP Paribas sign €700 million grid guarantee deal
  7. `historical:id:dc5698f4b73b354a` — The EU Anti-Coercion Instrument: Anti-What, Exactly? - CELIS Institute - Investment Screening | National Security | Competitiveness
  8. `historical:id:c8968a614fe33647` — Economic nationalists, regional investment aid, and the stability of FDI-led growth in East Central Europe
  - … plus 52 more in the package manifest

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
