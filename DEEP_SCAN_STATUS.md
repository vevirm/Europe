# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1507** (Main **705** + Historical **802**)
- Automatic queue still needing V2 verification: **439** (Main **107** + Historical **332**)
- Currently assigned to workers: **78** (Main **35** + Historical **43**)
- Bounded access-recovery retries still eligible: **215**
- Terminally dropped after failed scans: **4**
- Automatic queue pending and not yet assigned: **361**

## Worker lanes

### Worker A
- Current package: `worker-a-81f573736cd8`
- Assigned unresolved records: **36**
  1. `historical:id:302703dc36d212e9` — Trade war to cooperation: scrutinizing China’s strategies to the EU carbon border adjustment mechanism
  2. `historical:id:b4b900e80122ec1f` — R&I needs to reduce dependencies on critical raw materials through advanced materials in electronics
  3. `historical:id:810531b52b581fe5` — Critical minerals and industrial policy: a network-based approach to supply chain risk
  4. `historical:id:b439b69876ade4c7` — CELIS Institute - Non-Paper No 01/2026: Firewalls under EU Sanctions Law: Lessons from the EuroChem Case
  5. `historical:id:2ee98643952017d6` — German hydrogen import pathways: checking reality under uncertainty
  6. `historical:id:f3773aed6f7bf20b` — Resource Productivity: Europe’s Overlooked Route to Economic Security
  7. `historical:id:3e7ad09b31f0cd52` — Mongolian “Third Neighbor Policy” and Strategic Partnership with USA
  8. `historical:id:5fa7ca46e8595914` — EU unemployment and global value chains
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-55f5230e0f0c`
- Assigned unresolved records: **36**
  1. `historical:id:1e10c1f7dfb70d37` — ASEAN and the EU Challenged by “Divide and Rule” Strategies of the US and China Evidence and Possible Reactions
  2. `historical:id:6faf949eee3c5dee` — EU’s strategic partnership with Asian countries: an introductory article for the special issue
  3. `historical:id:f2f809d091b57a9a` — The case for a Euro-Arab summit – CEPS
  4. `historical:id:a9b7cdc893f4b331` — The internal market and national security: Transposition, impact and reform of the EU Directive on Intra-Community Transfers of Defence Products
  5. `historical:id:49b774b3ed41b24a` — Can Trump save the euro? – CEPS
  6. `historical:id:f7fc9e8e2254802b` — Energy Imports, Geoeconomics, and Regional Coordination: The Case of Germany and Poland in the Baltic Energy System - Close Neighbours, Close(r) Cooperation?
  7. `historical:id:d2df15a06da1bc12` — Targeted attacks - protection of critical infrastructure of the country and capacity building | Bank for International Settlements
  8. `historical:id:b736d887659e9e48` — Mobilising ASEAN - building the future through partnership | Bank for International Settlements
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
- `link:https://news.google.com/rss/articles/CBMi0AFBVV95cUxOb21ZTW5pS2NjT2NnS0xra2VZNS04a2hUbUFBSF8ycTBvUUNaT1Y2MDlaYUhrbDJPVUtWeGVocWU1STRsTEhPdVFzNkkwTWh1ek9TVkdGVkY2S0FjMnQ4YWNrSm1VcjctdG1CWWxRV3ZSc3Q4OGJlVi1kNXNYcW1iaUx2dDBNNjF2RlZSN3I5SHdIYWVfRzNSV1Q3MEo4ZzBPYV9VN3psQUFyRW1FYW9GX1RNMjFLOU1jaEx2OTVjTXNQU0dNQ3ZFd2Vka2oyYkUw?oc=5` — **China captures Europe’s hybrid market + Beijing pushes back on overcapacity claims - Table.Briefings** — attempts: 3/3 — Table.Media — 2026-07-28T20:37Z — Deep Scan return rejected: defer must not contain substantive deep_analysis claims — https://news.google.com/rss/articles/CBMi0AFBVV95cUxOb21ZTW5pS2NjT2NnS0xra2VZNS04a2hUbUFBSF8ycTBvUUNaT1Y2MDlaYUhrbDJPVUtWeGVocWU1STRsTEhPdVFzNkkwTWh1ek9TVkdGVkY2S0FjMnQ4YWNrSm1VcjctdG1CWWxRV3ZSc3Q4OGJlVi1kNXNYcW1iaUx2dDBNNjF2RlZSN3I5SHdIYWVfRzNSV1Q3MEo4ZzBPYV9VN3psQUFyRW1FYW9GX1RNMjFLOU1jaEx2OTVjTXNQU0dNQ3ZFd2Vka2oyYkUw?oc=5
- `link:https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3Rzd29FcFlHMldOUlY2ck9NWTdqSUotYWJULVJDUGVfSEYwdy1GeG5XcEU5US1BakNRQUtPZEViV3Nsb0t1dE5ZbVBvaERsZlVGZFpTVXJJME54aFp4Rlk1emlKamhySkRLOXpqX1gwMVBkVFB6anZZRlNMM3ptZW8tald0VGpvUDNmalFEQ1AtZHlSaWdMc1I0OFN4RGRIOTU0QW1hME1SMENpX2t3Zy1td2N5dmdyQXItckJSMHlobHBnbTF3?oc=5` — **China’s chip champion takes off + Why Europe’s supply chain rules hit a wall - Table.Briefings** — attempts: 3/3 — Table.Media — 2026-07-27T20:15Z — Deep Scan return rejected: defer must not contain substantive deep_analysis claims — https://news.google.com/rss/articles/CBMixwFBVV95cUxPM3Rzd29FcFlHMldOUlY2ck9NWTdqSUotYWJULVJDUGVfSEYwdy1GeG5XcEU5US1BakNRQUtPZEViV3Nsb0t1dE5ZbVBvaERsZlVGZFpTVXJJME54aFp4Rlk1emlKamhySkRLOXpqX1gwMVBkVFB6anZZRlNMM3ptZW8tald0VGpvUDNmalFEQ1AtZHlSaWdMc1I0OFN4RGRIOTU0QW1hME1SMENpX2t3Zy1td2N5dmdyQXItckJSMHlobHBnbTF3?oc=5
- `link:https://news.google.com/rss/articles/CBMi3AFBVV95cUxQd2RyTDdsYm03Mmc0S0N1a180WERBZkptYTZVU19qaEpJQ2pJWUs3aV9HS1hBcjdNV291UGF4S0FZNUZzWUVyUzhkemRfX0ZZeEdzVHdiVGNlemYyVk1uMFpwUkNfQ1BOYlFOYUFsM1oxLUpua0RFUDNHVE5QZy1YNFQyckhxVjBqYjg0dldldmdRU3hqR3NHS05mVUJLd0Q3ck1wU1Q4dl9jNURYMnpERFRKTjQyeVQtSmdFX1JGRmw2aUo5ZjZ2UzAzajJvZ21MVUZIOXpEWTRkZzVK?oc=5` — **Taking stock of Turnberry + EU rescue and restructuring guidelines + China’s export controls - Table.Briefings** — attempts: 3/3 — Table.Media — 2026-07-27T04:00Z — Deep Scan return rejected: defer must not contain substantive deep_analysis claims — https://news.google.com/rss/articles/CBMi3AFBVV95cUxQd2RyTDdsYm03Mmc0S0N1a180WERBZkptYTZVU19qaEpJQ2pJWUs3aV9HS1hBcjdNV291UGF4S0FZNUZzWUVyUzhkemRfX0ZZeEdzVHdiVGNlemYyVk1uMFpwUkNfQ1BOYlFOYUFsM1oxLUpua0RFUDNHVE5QZy1YNFQyckhxVjBqYjg0dldldmdRU3hqR3NHS05mVUJLd0Q3ck1wU1Q4dl9jNURYMnpERFRKTjQyeVQtSmdFX1JGRmw2aUo5ZjZ2UzAzajJvZ21MVUZIOXpEWTRkZzVK?oc=5
