# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1158** (Main **540** + Historical **618**)
- Automatic queue still needing V2 verification: **606** (Main **167** + Historical **439**)
- Currently assigned to workers: **94** (Main **13** + Historical **81**)
- Bounded access-recovery retries still eligible: **224**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **512**

## Worker lanes

### Worker A
- Current package: `worker-a-6d79099959fe`
- Assigned unresolved records: **44**
  1. `link:https://doi.org/10.4324/9781003669654-4` — Europe's Hydrogen Targets and Their Impact on the Market
  2. `link:https://doi.org/10.36253/wep-19990` — Trade Policy Uncertainty: the Ultimate Wine Label Remover
  3. `link:https://doi.org/10.30965/23761202-bja10067` — Competing Connectivity Strategies in the South Caucasus: Discourse-Based Insights into Armenia’s Strategic Dilemma
  4. `link:https://www.gmfus.org/global-power-shifts/indo-pacific-program` — Indo-Pacific Program
  5. `link:https://news.google.com/rss/articles/CBMikAFBVV95cUxQbkwxQnk0RzlFWmVtTEpTWlFBcFlyQTNQVzlibWZpNUM0WnphbU15VlZuR2Fab2Q3XzRDYzFFeHpQSDJsN1hQR2o5N2pnV2E5cHpOal9WU3dQWnJOQWc1eU16c2hyd2k4TXNlNkpBNUN1VmFQVUZYQmk3UzdqM1B0bkw4WnJYRVdoTVROaDVLYUw?oc=5` — ‘Tough’ talks with China have yet to deliver, EU trade chief says
  6. `link:https://news.google.com/rss/articles/CBMiogFBVV95cUxQWmlaa2hLZEw1UjBQMG9tTzMxWC1BMzBJRnkwTmhuajBMSHNrSUdYTWh4bXd5N0lVWlhhMTNHLUNRaS1id1JYZU1PUVljMnU5X2ZBc0VtN2g1TUtFeUU4dEhzTGYtdG5OeGFFeTZIb3lhVGREN3BjWElOZ0s0SnBVOFJqVkl5anVYV0tYdzVjS1pYSm9BX3hUUVN4WWdRX05WMXc?oc=5` — EU-China political relations | 05-10-2026 | News
  7. `historical:id:74b354ba22e49767` — China connecting Europe?
  8. `historical:id:baeb1d96e7783679` — Politicisation of the European Foreign, security, and defence cooperation: the case of the EU’s Russian sanctions
  - … plus 36 more in the package manifest

### Worker B
- Current package: `worker-b-83f2b59de0bf`
- Assigned unresolved records: **44**
  1. `historical:id:f68f8cbc3fa26d95` — The EU and China: sanctions, signals, and interests - Egmont Institute
  2. `historical:id:9a4d2017dd999a02` — Strengthened EU export control rules kick in
  3. `historical:id:c8ae8635441e9f45` — Strategic Autonomy in Post-Covid Trade Policy - Institut Jacques Delors
  4. `historical:id:2a72a684c174cd12` — Security Relations Between the EU and Australia
  5. `historical:id:f6eb1edca5fe2bc9` — Security Relations Between the EU and ASEAN
  6. `historical:id:3708dadbe84f22b7` — Secondary sanctions and multilateralism – the way ahead - Egmont Institute
  7. `historical:id:7f3dbfa63e0cfbe7` — Nord Stream 2 and the Energy Security Dilemma
  8. `historical:id:2ec5741eef07ddfb` — Joint Statement on December 2 Sanctions in Response to the Situation in Belarus
  - … plus 36 more in the package manifest

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
