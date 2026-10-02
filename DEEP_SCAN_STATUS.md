# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1284** (Main **582** + Historical **702**)
- Automatic queue still needing V2 verification: **549** (Main **194** + Historical **355**)
- Currently assigned to workers: **78** (Main **11** + Historical **67**)
- Bounded access-recovery retries still eligible: **351**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **471**

## Worker lanes

### Worker A
- Current package: `worker-a-65026296f26e`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMiowFBVV95cUxOemlnd1lGT2NJY3Z1dlZwczJlU1Z4eFg3cklraDRENXNIZzV5M05OSkc1bDVYRm1JazB0VUFnUzNlMGUxQ09vUDdmNE9va3ZaWHZURmRxVk9mSy0ySnBjeVY4WWZaQng3RV92cGxGamc5ZmtPczNOYkNZWnRETGRwRl8zYnlLYjI3WnRsZ1RBUG5YcV83ZTdpNXItQXA2bXNXNjJZ?oc=5` — Firms in France Put Sovereignty at Core of Hybrid Cloud Plans – Company Announcement
  2. `link:https://news.google.com/rss/articles/CBMiswFBVV95cUxPSkhVRnBvY29CRmlBLTJ1TlpiYzRZQzduNnN6b2NUWlA1cjdMT00xMDRrUWFYVXp2T1RZUmE5a1RxSy02c2NueWZHLUM5OUw2SWpsTUhVb0hQalB4LXMxcG5rSXoyN3RPbHNtZE1XVVRCRk5KaHdLaHR0cWNVRTJhSFFoUEVDUk5QWWNVMHV5UlNfOExkYW5HSGVfa1BSSExlUnVoSzduTTlaaEFOeksyYmVpVQ?oc=5` — EU’s Curbs Threaten 27% of Chinese Exports to Bloc, Goldman Says
  3. `historical:id:ae6d5be6b50d40f7` — Chinese FDI in Europe: 2018 Trends and Impact of New Screening Policies
  4. `historical:id:82eb0ef5612a9546` — Myanmar Strategic Partnership
  5. `historical:id:498213c27e04e50d` — Institut Jacques Delors - Bolstering EU foreign and security policy in times of contestation
  6. `historical:id:960bc24d204d5e00` — Institut Jacques Delors - Beyond industrial policy: Why Europe needs a new growth strategy
  7. `historical:id:04e774496a31629b` — Georgia Country Partnership Framework 2019-2022
  8. `historical:id:3289f88016bd6e25` — Fighting for Europe. European strategic autonomy and the use of force - Egmont Institute
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-78e4ec89057c`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMixgFBVV95cUxQTnZzanpPU3RDZjJPc1B3akxmZ19aT2p5Q04wYS16NTFCT1RYM0RCQVd3QmNhWGJ1QmJraWh3M3BBNGE0UE9qOWpTLUhSUzJ0b3lZN1M1eWk1TnYwekthRmJ1am5TSFp0UE9lWVBwamRSb1J6ZF9CcGs2NUowVlR1YWF4QktoTk1rMmk4Y09idUJkbTZGbjFuZ1F6OTRRd3p1QjdTUjJzdFhIX2dJUTI0LUd0OFhFV0dyV3NwS3JEYm4tNWhNNVE?oc=5` — Critical raw materials: Sweden declares security of supply a matter of national security - Table.Briefings
  2. `link:https://news.google.com/rss/articles/CBMiqgFBVV95cUxQZFlMLUdIdHpaejlGQ1cwUm5BWjhBdG1PcHdJYlBjSUhXcVNHeTItVDdObFpiVm1zWjgzdlNWN1hoSGgyQ2VFdWlUMlM3amUzNlp0X05VTFQyVFRzN0J2MFFoVnlJSjFjMHZqUVhhWUFzZlJkU2NmSjJaNGlZbHJZMEozRk5NdzA5OTg1U1l2T0M3M2trU1RCUUZVQUlSbGhPQW5KNHhidE9IZw?oc=5` — EBRD and EU join forces to strengthen Kyiv’s energy security
  3. `link:https://news.google.com/rss/articles/CBMitAFBVV95cUxQNHRoNHc3V2p5TW5tMlVDd2pJQ2pPODhDRnZEVnJlSkpwNUY0MWtUcmg1c095blNCLWhrdHUyMjBfSlh3Y3R5MGtGcnNVUkJuTGxQYURqUUhoMXdFbU1tLVpTWDlPOFdDNjd6Smt3V3N4RGhDSk5oMU5nVloxdXBHcUNTdFAtcTN4SzRudU5xNHpSSDNvcWtsY05oX19xeWdrbHVyUFEwY25PeE45Q3U0R1J1Tk8?oc=5` — Germany's Uniper firms up 20-year LNG purchase deal with Canada
  4. `historical:id:a4bbc5c1d47203bd` — The Eternal Sunshine of an Engineer’s Mind: Germany Looks to 5G Security as a Purely Technical Question
  5. `historical:id:2ea42bda01770d0a` — Trading with the frenemy: Germany’s China policy – European Council on Foreign Relations
  6. `historical:id:eff18536e28d4994` — Beyond Investment Screening
  7. `historical:id:b35128270fcadf47` — Chinese Direct Investment in Europe – Challenges for EU FDI Policy - Kiel Institute
  8. `historical:id:2ae93c9e6fcacd54` — The euro in the field of energy
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
