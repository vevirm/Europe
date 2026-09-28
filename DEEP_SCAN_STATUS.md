# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **389** (Main **389** + Historical **0**)
- Automatic queue still needing V2 verification: **1133** (Main **209** + Historical **924**)
- Currently assigned to workers: **78** (Main **78** + Historical **0**)
- Bounded access-recovery retries still eligible: **78**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1055**

## Worker lanes

### Worker A
- Current package: `worker-a-f683543333a5`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.2478/jlst-2026-0010` — Corridor X: Strategic significance for logistics and transport in the Republic of Serbia
  2. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=95d507ec-b88a-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Enhancing competitiveness, sovereignty and security of the European Union in frontier AI - Publications Office of the EU
  3. `link:https://doi.org/10.1111/rego.70156` — Chain Reactions: How Businesses Plan to Respond to the EU Deforestation Regulation in Brazil, the Congo Basin, and Europe
  4. `link:https://doi.org/10.1017/elo.2025.10056` — Europe and the race to structural transformation: a narrow path ahead
  5. `link:https://doi.org/10.1371/journal.pstr.0000265` — Conflicts and energy transitions: The case of the 2026 Iran War
  6. `link:https://doi.org/10.48550/arxiv.2607.09951` — Macroeconomic Risks from Maritime Trade Disruptions
  7. `link:https://www.atlanticcouncil.org/issue/geopolitics-energy-security/` — Geopolitics & Energy Security
  8. `link:https://www.atlanticcouncil.org/issue/security-defense/` — Security & Defense
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-78d35a36b3db`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMisgFBVV95cUxPb1duUkszRE5ZVnF4dTNyaVpQbUdVOEhrNmJxQTYxN2ZlVC1TdER1eko4M2Y4SUNpZllIMGdQamJfdDdOTURfNGtyYUQ3SkRFS1Z0OUswSlBVQ0xnZ3BOaE5BcUdzdmQxRWdmQTVyUjUtemNqVkxIalBXbGs1VmpDN1FGaHdydC1ZcXhLUW8telVIYXBmM29mTVZLRktMd2lJSGRaSmNSaUJzdGJ5MHRDM1NB?oc=5` — Germany to Lobby EU on China Policy, May Seek More Tariffs
  2. `link:https://news.google.com/rss/articles/CBMivgFBVV95cUxQUURnbnNMX3ZZUFNzdFEzSlQ2SV9aelhVaHhBYUdhTHRHMjhVdHVkS1RCUm1FSE1NdDVkYTdFS1NEbTlMeHRxdGxHTlhTZ2hDMFhXYlh0M0RQNWhyTFZ2bWFpZ0x5dWpqRHZvWEo2eXlJNXZRTUs2TDdjcHFLNTFnOVdoNVF0SzIwT19BZXdOUHFld0F0eG5xdHUtUm9ybmpkWE9DQnpLM09mTUxDcWFXMEZTTWRwMkJ2S0lZUXlR?oc=5` — German state politician calls for EU tariffs on Chinese hybrid cars, letter shows
  3. `link:https://news.google.com/rss/articles/CBMijgFBVV95cUxQeUIwaTZaTUNUTWJpV09qa1hfYzlPamQ5T3FNX0M0bWozMGFoYXl1WE4wY3VUS3c1dVpvYU54QVRVWlpNbGpBR1lOTVhIa2ZfUnJBa0cyWF8zQnFDT3NYeDdCTWZXalRja213bE82YjZZVUVUeVpuVVpDMTIzUzEtWVd2Vk9PNERRNm9SNFln?oc=5` — INTERVIEW: Ireland floats rethink of EU’s sanctions against Russia
  4. `link:https://news.google.com/rss/articles/CBMirwFBVV95cUxPNElNb1FhTDBHYXh6a3pqUFBrZjRFVC1pbDEzNC1nRFY3TEViejRBTjdPa05peXp0OXpGbEFzMndOX0UxdFY2c3d3cFdVYlZBWlhod3MzZEd2OGI0VndxUUZIdUF5WUxLOV9sRkNaaWRCbS1NRWMyT2dXQ0h2X05VMTFRMTc1ZU1jN052UHFBTUVRbFlROXVSUEJhelNEak94OVFlOC04SlJhNjJHOWdB?oc=5` — Trend.Monitor: What lies behind China’s gloomy verdict on the German economy - Table.Briefings
  5. `link:https://news.google.com/rss/articles/CBMi5AFBVV95cUxQRjltek52d1dad2pHeGx4OHNLbVlzVGZWelU3OHlVbzNrRFk4N2l2WWlQWUVRSjJYS1pGQ05rUzIxczBPU3hFR0F3QkllWVJTZGVWSUtEMmgxX1BseUJZakVRTzZsMWE3UlU1QnM3OEIwYzJBRGUyTXdBam9sSGZ2R3pUVnBYTmxtS2pNNjR3UHpwQU1fdHpjcmlPbkVJVmpkMEcyRlNFdmROWFpXTm9oZHY4dGVDTmRubGgycEM4WFZUUWlNb2JWSE9pbzFzbUxBR0RraEtuQnNxbVhhZHVVWlV4NTg?oc=5` — Pomp in Washington, hard bargaining behind the scenes + Why China is writing off Germany’s economy - Table.Briefings
  6. `link:https://borderlex.net/2026/09/24/eu-to-defend-carbon-border-levy-in-russian-wto-challenge/` — EU to defend carbon border levy in Russian WTO challenge - Borderlex - European trade policy
  7. `link:https://news.google.com/rss/articles/CBMivwFBVV95cUxPNldBQXliTFpySThuQlRkUlBMVVBLaUYzMS00N2NwM0JnZVBUUTdxaE1ZdmQ2U2NCNFU0dmVQV1hiU1hxWXJoRnJzTGktVjVKeUE0cm82elZ6U3pMc0FES2NJMU8wcWFmc2s0SXRDZDFiX3FHeWtVQnR1a3k2N2RHUkZzdXR4d0dUMjFPZ1dOSW4xZ004TWRMYmNnV2xrT3Z0WDJsTmx1YXI3b2hYa1lKdkFhbXFaZ0stWHROTVd1cw?oc=5` — Azerbaijan pardons French national after EU drops sanctions on Usmanov
  8. `link:https://news.google.com/rss/articles/CBMiqAFBVV95cUxOLTZkdHFod21LTGUtdGFpZWJVVm1vb2MyLXV2VzZHLWVrZGdtS3BFNmR1bk9OSEJBX3QwVkRmMHRrNThMSEJOZXJGdGFLQW44eFFGTGRNZF82Vi05dmkyX0RTM3hwaGRDU09KU1dLUjFBTWJUS01lWURGak9yN1JtYXNSR0g3ZmtKblAwcGZkSFl5eUtoSWtfRHBJYUR4YmVGMnhWR01zUWo?oc=5` — Estonia says France must explain push to lift EU sanctions on Usmanov
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
