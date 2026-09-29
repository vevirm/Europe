# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **464** (Main **464** + Historical **0**)
- Automatic queue still needing V2 verification: **1110** (Main **152** + Historical **958**)
- Currently assigned to workers: **78** (Main **20** + Historical **58**)
- Bounded access-recovery retries still eligible: **138**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1032**

## Worker lanes

### Worker A
- Current package: `worker-a-c5abcfce1620`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMirwFBVV95cUxOX1pLOFFWZURhd3NXNS1LMXM5aFludFpVRjY2bGpIN0hIVkRNR25jWVF0TG1qazZZUXk1NHVlUnhQQmJHVHlJckYwblI0SWVEZENvTGZfYTBZYlZBNFpiVXVXZXk4Z3AtSTBkeE13MUxPY2lCeUFVbWlicENRUEp6TGsxOTlBRGZ4RzlCT1N3SHJHVTI5aVk1QS01VWlpSkVrVmRGcTBQeDhIb0VMTldz?oc=5` — Trump’s diesel export threat meets a shrug in fuel-strapped Europe
  2. `link:https://news.google.com/rss/articles/CBMirgFBVV95cUxPM1BDVkFhTlFidkFYaXA2Wk54T1NWT19JQ0FtTF81bE5yUC1KbnAxYlVMRU80cEp2WlpTTjN5ZzZiV3R4MVBxNGFmTEptdGRMcHM4VXpwUEc4ck1OcHhrbjJFM0Y4WWhYbG0xRHhkZlZHaTNuLTRYMlVnOU9ocWdwb3I3NTZCSWVZTFlTVWt5VV9ma3VLU2FLQjFHcmFNYmE4RWFEbXpSNERSOWZLMlE?oc=5` — EU to Exempt Two Russian Tycoons in Sanctions Renewal Deal
  3. `link:https://news.google.com/rss/articles/CBMiygFBVV95cUxPNEU3cG0xb2xfWXdEaVhqMEQ3cEVhZTJFX2tMVEo5YkFXVXF3YmJQSUU5eGxJbHcteEQ3ZWlidmhabTRFazM5MzRIbjQ1aWRhUHQ4LURidWtLdEM4ekdRb1A0RlFGWWloT0lBbWxkQUZhR2tVVy1vSndNeXZGSUR0cDBtRHFMRTNOY3RMUmo4MWtpN2lGYnRuSlJXYm9sZUhwa3JCMHZ3RjVXVnBCMDhIeU9CSkRyZFJsbUtpODZsckNSZjBYWWZwNWJB?oc=5` — Volkswagen benefited from €1.5bn in German EV subsidies as it lobbies EU to hit Chinese cars harder
  4. `link:https://news.google.com/rss/articles/CBMiiwFBVV95cUxPaGlTdkJldUN6aWwyNFFnUVBEWEtnZWVPQUp4VGpPNGZMRTI4bE9fZlVOTEhZZ2VqcVpfS3N3S0d2UlhPcUp3Vk1WT1pES1ctVlFZZ1UydWNTbWxHVGwzbGNlbGE0TUJBMUJldVpZUFN0ZXBla3ZhM3pTMjF6UFdVY3ZtZnBtMldWVERZ?oc=5` — EU’s Russia sanctions are running out of easy targets
  5. `link:https://news.google.com/rss/articles/CBMi_gFBVV95cUxNbko3RENKVG5HMTNYczRtOVpwTHJQNmJFN20xT0ZKSzBuTEM2VzMxZkZGMmZFUWZxYUx2OFByS0U5aTVteDNIeG5rRXhENldSZmFsRWlPRl9aUVkyVFRycFZkUTBlQWtBNmJxTG4wTmpvazNBRWtiZ2JrZHd2UXZLZzZ2Qk56U25KRnVnNXhyeTFINElNZ2s3QXhmWU1NNHhwTkNvRHhoZjhkenA0dWt2ejcydkNWOTM1elY4Q0lwZ0VxeUJ1SUZYcjNnVExyZlVtNk16ZFQ3SFNHbjFSakJSOE40dGU4RF9peWJHQi16dGJmN2ZlREpYRzJpLThYdw?oc=5` — EU sanctions 10 individuals and 17 entities over unlawful deportation of Ukrainian children to Russia
  6. `link:https://news.google.com/rss/articles/CBMi6wFBVV95cUxNeEVJUmhhejd3Y0xuTFFPWnlGOXdrSmR4MDFmYm1jZDFTR2RNUlFhVmxwOC1rNzlzdy1BYW9kNi1LaEFUTEFzR0Eyck5nVGZoN2lSUFE5anBIVVhGbzg1LVNtV09GaUVHYmFnR2U4cFlBV3hWZEpZR3lKS3llQUFPUlBCQUFEMmpWdG13NDNINkxJeTZHNHRVMWtib19IcDVOWFlxcXMtcEpiWDhCMWtnc2pMazRWU2dSOWg3c1dsbTZrUHFYWTVMQVhhNnR0MG9HTWVPemltdDJRSXRSWjRsNzhxTzk5UkxjMXEw?oc=5` — European defence industry: Council identifies the first five projects of common interest
  7. `link:https://news.google.com/rss/articles/CBMisgFBVV95cUxQdkJsS2FSMnQzd1dNc0ZfS0hJRlRONktheHk4R0dicVhoOGpmNEV0aXFFZ3pHLUNZVUZ0Qml3Z2FzUkZZc3Z3ZjRFbFZKM3E3U2pTcUxfOHdRaklMR2tIYjVtNnNtYTlKU18yZkFDNVZvMHpRV3VwSDJFX2s1c1lNTE5FMFNhOVJsSFZWbU5yQV9yUUZyRTNGU09QcDJTVXF1RDRCTVQ1MTNvTHRtQmlKZTNn?oc=5` — Europe Draws More LNG as Hormuz Crisis Tightens Global Market
  8. `link:https://news.google.com/rss/articles/CBMivgFBVV95cUxOVDRjSXY3THA4d0lJaGlLM05DM3FVeDc3TFVFa3p2d1Z5OWRiNnBxbVhqMkVoZmw0M0xNeDVaNXhrTVN6bnhTRy1Pc0E4VXEwSjhsS3VkcE9BSjZMQ0hUM0FfM010Zk8zNGlZTUN0MmRZbS1ZTEhxQUFGWUVDUFBESzRKWkYxUUZMVjJIZzd0ZjZVbDViRFRDTkFpUjlCalJfODhOQUk5OC1Nc3d1X2NOdE5aUk1tWS1PdDdJZkNR?oc=5` — German gas supply is secure despite low storage levels, VNG chief says
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-4eb7623e3b6c`
- Assigned unresolved records: **36**
  1. `historical:id:64f7d996c94f7cd1` — “Economic Security” Done Badly Will Make Us Less Economically Secure
  2. `historical:id:6d00e26535bd49ca` — Let’s Get Critical: Critical Minerals Mini Deals as Evolving Models of Trade Cooperation
  3. `historical:id:910592fe83ac1500` — The digital euro - strengthening Europe's payments ecosystem | Bank for International Settlements
  4. `historical:id:2433c92388ae268b` — Mining for Europe's future: Critical raw materials, public attitudes and risks in enlargement partners
  5. `historical:id:250a74bab8cf52ee` — How EU industrial policy got its groove back: securitisation and governance shifts in the geoeconomic era
  6. `historical:id:0e3b1813e6c28103` — Centimanes v. Titans: right-wing populist governments’ treatment of foreign multinationals in East Central Europe
  7. `historical:id:56f43b36e4bd7bd7` — A pivot or a saga? How Turkish foreign policy is torn between domestic pressures and economic needs – CEPS
  8. `historical:id:2b9abbfbed136d9d` — China and the EU-US rift + Economic security + Car imports from China
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
