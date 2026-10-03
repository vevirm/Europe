# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1378** (Main **591** + Historical **787**)
- Automatic queue still needing V2 verification: **503** (Main **199** + Historical **304**)
- Currently assigned to workers: **78** (Main **17** + Historical **61**)
- Bounded access-recovery retries still eligible: **350**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **425**

## Worker lanes

### Worker A
- Current package: `worker-a-602d33ec81dd`
- Assigned unresolved records: **36**
  1. `historical:id:0901c20b9479d119` — Development of the Regional Natural Gas Market in Southeast Europe
  2. `historical:id:910dc68b07fcc3fd` — Risky business? The EU, China and dual-use technology
  3. `historical:id:f7fff84b18edd262` — On target? EU sanctions as security policy tools
  4. `historical:id:5b5b6367e6db7bd7` — Keeping the Eastern Partnership on track
  5. `historical:id:1bd1770370cd280e` — Did Anti-dumping Duties Really Restrict Import?: Empirical Evidence from the US, the EU, China, and India
  6. `historical:id:7cf8e102589e0fea` — The EU’s gas relationship with Russia: solving current disputes and strengthening energy security
  7. `historical:id:47faeaff495ea249` — New Protectionism, Sanctions and EU Disintegration: Challenges for Baltic Trade (original publication German only) - Kiel Institute
  8. `historical:id:40d4f45309e160fc` — European Leadership in 5G – CEPS
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-047459215537`
- Assigned unresolved records: **36**
  1. `historical:id:a4bbc5c1d47203bd` — The Eternal Sunshine of an Engineer’s Mind: Germany Looks to 5G Security as a Purely Technical Question
  2. `historical:id:2ea42bda01770d0a` — Trading with the frenemy: Germany’s China policy – European Council on Foreign Relations
  3. `historical:id:eff18536e28d4994` — Beyond Investment Screening
  4. `historical:id:b35128270fcadf47` — Chinese Direct Investment in Europe – Challenges for EU FDI Policy - Kiel Institute
  5. `historical:id:381239bb1178e2e8` — Europe’s financial security and Chinese economic statecraft: the case of the Belt and Road Initiative
  6. `historical:id:d18d19c4f57ed851` — The Trade Effects of Anti-Dumping Duties: Firm-Level Evidence from China
  7. `historical:id:34be707287418ec2` — The Idiosyncratic Nature of Chinese Foreign Direct Investment in Europe
  8. `historical:id:c7e3fa009c5ccca9` — Myanmar, the Rohingya Crisis, and Further EU Sanctions
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
