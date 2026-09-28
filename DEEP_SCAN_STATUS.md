# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **401** (Main **401** + Historical **0**)
- Automatic queue still needing V2 verification: **1155** (Main **197** + Historical **958**)
- Currently assigned to workers: **78** (Main **78** + Historical **0**)
- Bounded access-recovery retries still eligible: **118**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1077**

## Worker lanes

### Worker A
- Current package: `worker-a-9116ea06edf4`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMihAFBVV95cUxQWDlTbEtkcmpvbDkxaVFjaFdzMkpjWXJXRUdvcERmb2NQZXIzdjNyRjdmMmlEd2tsYVpsMkNQbFlMU2w1dnhvM09ZbjNMRGZpd3hjMVZWZW1MYmxnQVoxOThpSmRvLXRTU3JiUWEtbktMY1h1S2VFclozOFJ3QXI3dnVYZ0w?oc=5` — European diesel prices climb over prospect of US export ban
  2. `link:https://news.google.com/rss/articles/CBMiswFBVV95cUxQRGNmdDc5NllJOGQyamFRNXBnT2RleXZsMlN0aG90SzA5RlBoMkx2UGdQRElpNTNSREQtdldfcTVkMEZwbFBZU2QxcjhlNTFYQ3hGSGtOak16WW5oWUdCaUNxZGJnQ3k4RzlhNkl3cW9RT01ReGRiN0w2R2piZUhPV01lOFpWd2NLVVlkQ2laQUFDTHBMaWVhVnhsUm5tM3F4YV9HVXdEbXRsV2dWaEhvNWkxcw?oc=5` — Azerbaijan frees French prisoner after EU lifts sanctions on Russian billionaire
  3. `link:https://news.google.com/rss/articles/CBMiwgFBVV95cUxNdm9BcWNoRlkzRVA1RVFkRUNuZ3pmVzVPNXdmMDFzWjg4RGlEcmY5RkxPWmhVWGYyTXotZ3B0d2xMWWZmcDV5QV9NNGp2d1p4enBBZElLbjNlNzdKMHpMajd2ZlJiM0pscDhlTGNlSXc4QXQ5aUtJMEpONHlWTTd5SDV1ZlNvOGx4Z3AwU3ZsWUs3MVYzdGV3SlZjQ3J2X29GS1NWWlR2VzdPT2tRdUJNc0ZVY0tuc1lxN3dfYVhmNGtndw?oc=5` — Portugal says entry into grid operator REN won't affect China's State Grid
  4. `link:https://news.google.com/rss/articles/CBMimAFBVV95cUxOMHp3OHZFbmpMOEFGSXF6VnJxNE5TTTQxREVVaVE3UU9GZ0tkdmQzZ1otXzd1RXMwVmFJVEktV3JQUnZ3eU9fd1E2cGE0enVhZmFDZy04T2JIZ2tJSjU0UnU3UDJmaUdKV2dCQlFuM2paVWFYRlVMVEdlcmlFY0lwQkhUNm90ZThCQmhMdEE0bF9kRnE1TzZ1bg?oc=5` — France and Slovakia remove Russian oligarchs from EU sanctions
  5. `link:https://news.google.com/rss/articles/CBMilAFBVV95cUxONFVVc3ZMMlVNd21TMjAtZ0lSOVQ1Y1FZZXgzaTI2dVMtZk9OeHN2YXdQYTY4NlFCWEFXRldKQ3FEb3RLR2FldUo3c0VseHByOWMwMFljZ3Y5c3Zyc0dZaFdzR2NXcTR5eFhCMnZYVjFET1IxT0pTQ3ZBUEl0Z05JdTdRRnRsSFJrVFBybkpzMU9EN0lw?oc=5` — EU deadlocked over France’s bid to take Russian tycoon off sanctions list
  6. `link:https://news.google.com/rss/articles/CBMivAFBVV95cUxOUjd6SnhEMGdGc0lCWnRQZk1EcEFCcHBoamZJR0ZDQnJRNVVHVHdTbU1RT0Ywc2g3ZEgtX014NTJObldia1NXWjl1N1psZlRVTTVkaThLRXA0Rk83WG1LcnVab1o5MHVSX3h1emVqOHJocmdnMU1YbHV3NzZwX2xzcUtyZEpfTHl0N2VBWVk1cHM2bjFMcmZpTEJSVV9HdGdleWxhSU9FbWd1U2hTVUxUZnUxYzZ1YUtSb1h5UQ?oc=5` — Russia’s hybrid war and Trump’s tantrums are pushing Europe towards real strategic autonomy
  7. `link:https://news.google.com/rss/articles/CBMipwFBVV95cUxNQVo4aDNrTmNzMllrUVotRWpBOHFjYkRrRmNHUVNtczZKQkl2SVlGYUhoTGcxVEdNRFh1QlFJem5EQTFYYlVMNWhfYUVIUVppYVlTNUhwdzBHT3BHV0hudlF4SFQxazhxcnVQczhCM1ZwZlRnMVBtUjdkanEwcE5nMjhWYzNEZFFZT1Q4VS13TEhJdTFUU1p3Y0lfM2toQTZVYmh5X1A2Zw?oc=5` — Rare earths: Chinese study gives Europe reason to diversify - Table.Briefings
  8. `link:https://borderlex.net/2026/09/18/wto-reform-push-takes-aim-at-most-favoured-nation-rule/` — WTO reform push takes aim at most-favoured nation rule - Borderlex - European trade policy
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-a5fac018d2fe`
- Assigned unresolved records: **36**
  1. `link:https://news.google.com/rss/articles/CBMirwFBVV95cUxPNElNb1FhTDBHYXh6a3pqUFBrZjRFVC1pbDEzNC1nRFY3TEViejRBTjdPa05peXp0OXpGbEFzMndOX0UxdFY2c3d3cFdVYlZBWlhod3MzZEd2OGI0VndxUUZIdUF5WUxLOV9sRkNaaWRCbS1NRWMyT2dXQ0h2X05VMTFRMTc1ZU1jN052UHFBTUVRbFlROXVSUEJhelNEak94OVFlOC04SlJhNjJHOWdB?oc=5` — Trend.Monitor: What lies behind China’s gloomy verdict on the German economy - Table.Briefings
  2. `link:https://news.google.com/rss/articles/CBMi5AFBVV95cUxQRjltek52d1dad2pHeGx4OHNLbVlzVGZWelU3OHlVbzNrRFk4N2l2WWlQWUVRSjJYS1pGQ05rUzIxczBPU3hFR0F3QkllWVJTZGVWSUtEMmgxX1BseUJZakVRTzZsMWE3UlU1QnM3OEIwYzJBRGUyTXdBam9sSGZ2R3pUVnBYTmxtS2pNNjR3UHpwQU1fdHpjcmlPbkVJVmpkMEcyRlNFdmROWFpXTm9oZHY4dGVDTmRubGgycEM4WFZUUWlNb2JWSE9pbzFzbUxBR0RraEtuQnNxbVhhZHVVWlV4NTg?oc=5` — Pomp in Washington, hard bargaining behind the scenes + Why China is writing off Germany’s economy - Table.Briefings
  3. `link:https://news.google.com/rss/articles/CBMivwFBVV95cUxPNldBQXliTFpySThuQlRkUlBMVVBLaUYzMS00N2NwM0JnZVBUUTdxaE1ZdmQ2U2NCNFU0dmVQV1hiU1hxWXJoRnJzTGktVjVKeUE0cm82elZ6U3pMc0FES2NJMU8wcWFmc2s0SXRDZDFiX3FHeWtVQnR1a3k2N2RHUkZzdXR4d0dUMjFPZ1dOSW4xZ004TWRMYmNnV2xrT3Z0WDJsTmx1YXI3b2hYa1lKdkFhbXFaZ0stWHROTVd1cw?oc=5` — Azerbaijan pardons French national after EU drops sanctions on Usmanov
  4. `link:https://news.google.com/rss/articles/CBMiqAFBVV95cUxOLTZkdHFod21LTGUtdGFpZWJVVm1vb2MyLXV2VzZHLWVrZGdtS3BFNmR1bk9OSEJBX3QwVkRmMHRrNThMSEJOZXJGdGFLQW44eFFGTGRNZF82Vi05dmkyX0RTM3hwaGRDU09KU1dLUjFBTWJUS01lWURGak9yN1JtYXNSR0g3ZmtKblAwcGZkSFl5eUtoSWtfRHBJYUR4YmVGMnhWR01zUWo?oc=5` — Estonia says France must explain push to lift EU sanctions on Usmanov
  5. `link:https://news.google.com/rss/articles/CBMi0AFBVV95cUxPcHBBN01iSVZHMEMwclNDbGk4VWNOYlpaYUdfUk1IX0Q2OHpMeF9jcHN0Qk1Gakt3cnQ3ak5hQmJPRE1fTWpMY0x3Qk95bWROX2Ntb3lqanh0NnlWOEpvYk9vdEVLMTZGbzZCZVgtN1RFUTZIZTVwMmdaZ2NJRDFXRnNvNDNxbzJoS0tudWZSaU0wUWdFQTZHQXZhdVJXUTk3aUZHZ1AzQl8xOFU1aTIyd041RmhnYTZuRWxSUWIxZ1AwS0ZWS1B0bk5hbU5CNGVB?oc=5` — IAA: China powers into Europe’s truck market + Xi and Modi narrow their differences - Table.Briefings
  6. `link:https://news.google.com/rss/articles/CBMilgFBVV95cUxPYklDSUc1YlRDQTRiWXR1SV9lMzFqenBWQ2tSV3ozeDJlbGYzT0lTU09pWHVSUDZQSWZMRVpnal9KTHhuLUNuandYaDBuMUlvaU9pa0l5dmg3S3JXRmVxc3c3NWR6MXlGVkpmNnJrUE90bU5GcmU0SDM3NUV0RTEwWXZlZ2hVQ2RBUTFETkl1QlgzSHJKcWc?oc=5` — Trump says he is removing US tariffs on Irish whiskey
  7. `link:https://news.google.com/rss/articles/CBMivAFBVV95cUxPcmZuZkpBNWk3aE1rc2l2dkhBSUZfdW9yWi1oQXpJUTJreUJlQVlYX2lEYXdMdDhWb1Nmbl81dzJKR1p1TWlNMVdSbnhrUVZONG1sWVhid1pQMzZHZXZkYkhNcVQ1ckZ1WXdXS2xhX2tJS1ZBWmhYOHdQbjJpZ3NXUjhZZHJRNGYtQTlxcFVoeWFFTkVkU1lRRE5sVE50RTNNazNLcWlBREFOdy1idDI0SDJmNUJmSVUzZ3BBdA?oc=5` — Germany has lost its moral compass, as it shields Israel from sanctions and legal scrutiny
  8. `link:https://news.google.com/rss/articles/CBMirAFBVV95cUxPS2kybnBZdWdDdGV2VTJJYmNXQzEzNmpnNXhYMEJlaXhZRzM5TzVOSXBxcDRqeUR1QTZzSFdDXzRNcXVJd3dsdHhna2hwVzB6eUpiSG9DUVU1MEtaZWJZYV96SU44NEFjSDl2dlpXdTBhWnNqTkNVTGJRYXMyaGxNbmhXbkRVQzVfV052YV94VkluRkNVTmV4ak5RdWN6RWJwTGhZcWF4d2kzYUpT?oc=5` — Funded traineeship for young graduates at the EU Delegation to Japan
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
