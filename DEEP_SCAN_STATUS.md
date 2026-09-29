# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **530** (Main **474** + Historical **56**)
- Automatic queue still needing V2 verification: **1095** (Main **160** + Historical **935**)
- Currently assigned to workers: **78** (Main **14** + Historical **64**)
- Bounded access-recovery retries still eligible: **176**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1017**

## Worker lanes

### Worker A
- Current package: `worker-a-d5b4cd36d0a9`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMi_gFBVV95cUxNbko3RENKVG5HMTNYczRtOVpwTHJQNmJFN20xT0ZKSzBuTEM2VzMxZkZGMmZFUWZxYUx2OFByS0U5aTVteDNIeG5rRXhENldSZmFsRWlPRl9aUVkyVFRycFZkUTBlQWtBNmJxTG4wTmpvazNBRWtiZ2JrZHd2UXZLZzZ2Qk56U25KRnVnNXhyeTFINElNZ2s3QXhmWU1NNHhwTkNvRHhoZjhkenA0dWt2ejcydkNWOTM1elY4Q0lwZ0VxeUJ1SUZYcjNnVExyZlVtNk16ZFQ3SFNHbjFSakJSOE40dGU4RF9peWJHQi16dGJmN2ZlREpYRzJpLThYdw?oc=5` — EU sanctions 10 individuals and 17 entities over unlawful deportation of Ukrainian children to Russia
  2. `link:https://news.google.com/rss/articles/CBMi6wFBVV95cUxNeEVJUmhhejd3Y0xuTFFPWnlGOXdrSmR4MDFmYm1jZDFTR2RNUlFhVmxwOC1rNzlzdy1BYW9kNi1LaEFUTEFzR0Eyck5nVGZoN2lSUFE5anBIVVhGbzg1LVNtV09GaUVHYmFnR2U4cFlBV3hWZEpZR3lKS3llQUFPUlBCQUFEMmpWdG13NDNINkxJeTZHNHRVMWtib19IcDVOWFlxcXMtcEpiWDhCMWtnc2pMazRWU2dSOWg3c1dsbTZrUHFYWTVMQVhhNnR0MG9HTWVPemltdDJRSXRSWjRsNzhxTzk5UkxjMXEw?oc=5` — European defence industry: Council identifies the first five projects of common interest
  3. `historical:id:5859fd808f9576e5` — Europe’s research dilemma – balancing security and scientific cooperation with China
  4. `historical:id:3788a70d3bd5491a` — European finance at the fault lines of transatlantic relations | Bank for International Settlements
  5. `link:https://doi.org/10.1057/s41599-026-08607-9` — The obstacles and changes in Sino-European trade routes in the twenty-first century due to climate change and geopolitical risks
  6. `link:https://doi.org/10.48550/arxiv.2606.12201` — Materealistic? How European energy system models exceed raw material reserves
  7. `historical:id:a8a46f983eb65387` — How do EU manufacturing firms navigate tensions, disruptions, and policy changes in foreign markets?
  8. `link:https://doi.org/10.36074/logos-05.06.2026.003` — INSTITUTIONAL DE-RISKING AS A NEW STATE FINANCIAL MODEL FOR STRATEGIC INDUSTRIES: THE CASE OF GREEN HYDROGEN IN UKRAINE
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-e4f5ce344574`
- Assigned unresolved records: **36**
  1. `historical:id:2433c92388ae268b` — Mining for Europe's future: Critical raw materials, public attitudes and risks in enlargement partners
  2. `historical:id:0e3b1813e6c28103` — Centimanes v. Titans: right-wing populist governments’ treatment of foreign multinationals in East Central Europe
  3. `historical:id:9a02512190d6359b` — Out of Many, Many: Variation in East Central Europe Financial Governance Despite the EU's Single Market
  4. `historical:id:e7b6ff5842d21c18` — Transatlantic Approaches to Outbound Investment Screening
  5. `historical:id:2ecd9537efd7b69d` — The digital euro - anchoring Europe's strategic autonomy in a digital future | Bank for International Settlements
  6. `historical:id:83f1f6fff8bda2c1` — The European Union’s Economic Security Strategy Update
  7. `historical:id:f342875f1a3c6fd4` — Supply Chain Secondary Sanctions: How China Weaponised Lithuania's Trade Links - CELIS Institute - Investment Screening | National Security | Competitiveness
  8. `historical:id:b774f5d0aa10d3e3` — Nostalgia is a Broken Compass for Industrial Policy
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
