# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1114** (Main **539** + Historical **575**)
- Automatic queue still needing V2 verification: **632** (Main **168** + Historical **464**)
- Currently assigned to workers: **86** (Main **13** + Historical **73**)
- Bounded access-recovery retries still eligible: **225**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **546**

## Worker lanes

### Worker A
- Current package: `worker-a-8867967ab9ec`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.4324/9781003669654-4` — Europe's Hydrogen Targets and Their Impact on the Market
  2. `link:https://doi.org/10.36253/wep-19990` — Trade Policy Uncertainty: the Ultimate Wine Label Remover
  3. `link:https://doi.org/10.30965/23761202-bja10067` — Competing Connectivity Strategies in the South Caucasus: Discourse-Based Insights into Armenia’s Strategic Dilemma
  4. `link:https://www.gmfus.org/global-power-shifts/indo-pacific-program` — Indo-Pacific Program
  5. `link:https://news.google.com/rss/articles/CBMikAFBVV95cUxQbkwxQnk0RzlFWmVtTEpTWlFBcFlyQTNQVzlibWZpNUM0WnphbU15VlZuR2Fab2Q3XzRDYzFFeHpQSDJsN1hQR2o5N2pnV2E5cHpOal9WU3dQWnJOQWc1eU16c2hyd2k4TXNlNkpBNUN1VmFQVUZYQmk3UzdqM1B0bkw4WnJYRVdoTVROaDVLYUw?oc=5` — ‘Tough’ talks with China have yet to deliver, EU trade chief says
  6. `link:https://news.google.com/rss/articles/CBMiogFBVV95cUxQWmlaa2hLZEw1UjBQMG9tTzMxWC1BMzBJRnkwTmhuajBMSHNrSUdYTWh4bXd5N0lVWlhhMTNHLUNRaS1id1JYZU1PUVljMnU5X2ZBc0VtN2g1TUtFeUU4dEhzTGYtdG5OeGFFeTZIb3lhVGREN3BjWElOZ0s0SnBVOFJqVkl5anVYV0tYdzVjS1pYSm9BX3hUUVN4WWdRX05WMXc?oc=5` — EU-China political relations | 05-10-2026 | News
  7. `historical:id:74b354ba22e49767` — China connecting Europe?
  8. `historical:id:baeb1d96e7783679` — Politicisation of the European Foreign, security, and defence cooperation: the case of the EU’s Russian sanctions
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-4f3865965194`
- Assigned unresolved records: **44**
  1. `historical:id:7b65c4b7515137ac` — Europe’s energy security and EU-US cooperation
  2. `historical:id:c9edfa6b3626faa7` — EU: Three Russian banks and one technology company added to the frozen funds list as part of sanctions package - Global Trade Alert
  3. `historical:id:e2a628c87a06054e` — EU: Additional financial sanctions on Russia, including the exclusion of 7 banks from the SWIFT paying system - Global Trade Alert
  4. `historical:id:e2eec73b1db2c549` — EU discusses energy security with Japan
  5. `historical:id:209cab6667c84237` — EU Space Strategy for Security and Defence
  6. `historical:id:15db2f653fa8bcb3` — Declaration by the High Representative on behalf of the European Union on leaks in the Nord Stream gas pipelines
  7. `historical:id:23f72ce10b2dc494` — Balancing inflation, output and fiscal sustainability: policy responses to energy shocks
  8. `historical:id:ddb09e818241b367` — Agrifood trade and EU sanctions adopted further to the invasion of Ukraine by the Russian Federation and the support of Belarus to it
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
