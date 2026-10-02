# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1216** (Main **542** + Historical **674**)
- Automatic queue still needing V2 verification: **617** (Main **234** + Historical **383**)
- Currently assigned to workers: **94** (Main **59** + Historical **35**)
- Bounded access-recovery retries still eligible: **342**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **523**

## Worker lanes

### Worker A
- Current package: `worker-a-e879d2d0fb96`
- Assigned unresolved records: **44**
  1. `link:https://news.google.com/rss/articles/CBMizgFBVV95cUxOTk01YnZuTmlUd0J0Y2oyOW9CMXF6Sm5IT1NZR2FmVVUzQ0h2aU54M1pMbGc2bElaWmpEWkNLQ29ZSVRtMEozM21WbGhidXhaQUpZWVpaLS1FclExNUQ2ckZKemwxSjRGcEFVNlk4VmN6aEpwSmF2aTFYUVlKN3JHYk5adF9SMFBSejdPbVI3WkNfRmlKdUplRVRmTlBFbkdaTmtaTWhlQkhtMjBnaURmemV0NTNfcjlKaUl4SGZudEk5SXEzZVVYUW1NeG0tZw?oc=5` — EU-supported BizConnect strengthens education–industry partnerships in Timor-Leste - European External Action Service (EEAS)
  2. `link:https://news.google.com/rss/articles/CBMioAFBVV95cUxPT19VbVoyelRLLW4wbHRQaVZnRUN2OUxUdlU1SjlzUEVhcTBTNERfQllpMEp4Q3FKMWsyVlBEeVdha3A2ZWV5Ql82Q0ljME9qQVhjUm54V0w1ZVhBd1NqWEFvTEdLSXBvREItSExGdkYtTVdRWHYzbmkwU1cxNEZiYnNxek1yakxXZGZ3WTl6bzdWSXhjVFpiOFA3U3lUOFNP?oc=5` — German industry hoards rare earths as Brussels squares up to China
  3. `link:https://news.google.com/rss/articles/CBMi3gFBVV95cUxOTXJBX0NXcXdvSFdWY01NLVJFM0gxRnVud08yLWlxdWNFd2hhVmFCam5jbnFQRFByLWcxVmxJUTlfb0dQeXlTWWdaRl9kVUdhRXlFNVR0UTFkbEZmSjFXVW1nTWttZ3JCeTB0UXhyWWE1RDNuRTRJc01vdUdvQ0ZyUllOZG90dmFWMExVUDg0elc0enltVkpuMjNkUVc3bEs5TUJjRm42VjVKUTlpbjl0TEpWNERfT0pseE9zWThOWlVqeklSTEM3TkpzZGNrU00zSG5NaExBMkVkQVM4cUE?oc=5` — Supply chains: German Federal Ministry for Economic Affairs and Energy conducts national vulnerability analysis - Table.Briefings
  4. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=352dbb2a-bc9e-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on establishing the European Competitiveness Fund ('ECF’), including the specific programme for defence research and innovation activities, repealing Regulations (EU) 2021/522, (EU) 2021/694, (EU) 2021/697, (EU) 2021/783, and amending Regulations (EU) 2021/696, (EU) 2023/588, (EU) [EDIP] - Presidency text on Article 65(5) and recital (38) - Publications Office of the EU
  5. `link:https://news.google.com/rss/articles/CBMieEFVX3lxTE5MWVQtT2FJZTJLNnhaenhhdHJxOGRRVlNUN2FVbkNIMGFVb2NLRUZ4cVNLbEY2Vjhzb0xTTFhaN2tFSGlGYUstczNZbHBCRzZLczRfZTZKTEZiRHhocUxXcXlZVmIyaXJkUkZRZ0FLUHRpV3dKUXZnYg?oc=5` — Trump wants to be with the ‘winners.’ Europe should remember that.
  6. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=38cd153a-b33c-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL establishing the conditions for the implementation of the Union support to the Common Fisheries Policy, to the European Ocean Pact and of the Union’s maritime and aquaculture policy as part of the National and Regional Partnership Fund set out in Regulation (EU) [...] [NRP Fund] for the period from 2028 to 2034 - Opinion of the European Commitee of the Regions - Publications Office of the EU
  7. `link:https://news.google.com/rss/articles/CBMifkFVX3lxTFByRF9oT1RwUFhUVnA2NzFhVVdyTnE3RHdZZDV0RkxhRmdJUFRYWlpKeWdXa3RsX2tJaDg4S28wZG1jVFdnMHdFUVVYV3JPNkJNc2hsX2JtUVRrMDJZNUp0VnI1SlhFSy1IQWJPZ05WRFUzSlRKLVpXOGJhaTNlUQ?oc=5` — International dimension of the proposed Industrial Accelerator Act
  8. `link:https://news.google.com/rss/articles/CBMihAFBVV95cUxPUzJhTTdEQzA5bWVMaTB3a2pmZFlNRGkzTzJkTVM3eHpfQzJycTN5MmhiUmlkYkpUWTVjei1xMFBKTkRnWnRidlRtT3JyVVUxRGluWDlUVFFQbERyT2RlWVFLWGZBeW80ZVFkbEJQaHFGdEUyNnNNUF9DWklucC1XQTc3QXE?oc=5` — Donald Trump suggests EU-Canada associate member deal would be ‘hostile act’
  - … plus 36 more in the package manifest

### Worker B
- Current package: `worker-b-d1b5ba98d5c8`
- Assigned unresolved records: **44**
  1. `link:https://news.google.com/rss/articles/CBMitAFBVV95cUxPYkN0bndZUUs5aEFIYU5FYUFWZzRZNjJ1aGVCck1aZDlhTS1uZzVabGhLWU1VeVo0MVprTTF6cmJNR0toRmZsVEdhT2ZvZ3dvSXZkSDVOdXd0NDVta3ZNeUYza3ZHQVVYei1PX00tUjlIdnR0UElCOGw2S0JoWXJFX2h3b1lYNm4zVnEyX0o1dmtFaENrNWNtSnJaQzhWZnBERWlUTTVJaGpUVmxIaDVIZ2x6dWw?oc=5` — China Aid for Key Sectors Can Feed Trade Tensions, ECB Blog Says
  2. `link:https://news.google.com/rss/articles/CBMijgFBVV95cUxORXhnV25kdThiUU5EQnBVamYwTElhdnpXVmw1LWhtTHljNnZkUGxnMzBaOTBiU1VobmdDc1RJRFhEV3p2OVB1UUVkWFZFQVpIdmdlbkVQSlhIQ1h1MkNmdXI4MExUOE9aTGVjZ2dyZ25xdlFGZ2pIRXE5QktFc3hWTlM3VTVFd3dtbFJCOHdn?oc=5` — Supply Chain Resilience, Diversification and the Future of Trade Governance - European Central Bank
  3. `link:https://news.google.com/rss/articles/CBMimwFBVV95cUxNaFRfR2pQSXN0VFlacjlkREFVek5mb2FLckVtN0p6OHNFWWhXbmRPVmtRX2hTSUZmcGp1ay1ha3Y0WWhhQVdBRDRCMkJiTG1lQW5QNTlualRUN0ZIVkNZM3JIR0xqb3BtV0NrckxXT2trVlFzeWZCRy1ZT21BOXdDMFM1QnhMX2xpUjNDZXZwM25kaklEZGp2b29pOA?oc=5` — Digital euro: Survey shows little enthusiasm among businesses - Table.Briefings
  4. `link:https://news.google.com/rss/articles/CBMihAFBVV95cUxOeHctMHRHZHJMZlhlZmhwMThpTTE0YTBZRXBXeUJHX29xRVlfdXVnbkN0VHBidHJWS1ZlNjlFeEpSYXN4QnNQVGIwaVV3SHdfT1h4T3lLWF8yMFN3ZXlrcnh2WmVGcmo3MXlHYk1uRWNyU1ltS1RqSmFwdkl6bHNfV3lzUzA?oc=5` — How the EU can face down Trump's tech aggression
  5. `link:https://news.google.com/rss/articles/CBMixgFBVV95cUxNSkJFSC1uYWxnMFE2YnN4U3ZmdnFOUTB6TmJaYVE0X1ktN0tTOFZYUUdfMUZMNW13bzFGbEtHYUF0ZE03aHpEbVZnejRZbjI1SGRVM0hqeHJQV2dnWnhyT3RfbE9aTmlxdk1vVzVwQ1ZxUHM5VjNyVEhFQ3hkZzdxSGdkb0VOS0dwSC1HcGdNM25wR3N6a25fS3NTMEpvQUU4UDFld0x5SVFxUWRLc18tZHh2QlFZSndjcFM2UEhfMmVLRnJxUUE?oc=5` — Critical raw materials + Interior ministers on Ceuta + Scaleup Europe Fund - Table.Briefings
  6. `link:https://news.google.com/rss/articles/CBMioAFBVV95cUxPY0ZQVDVKM1dld1JjOFdOUFNOWjZnTGJhU19qYTZneWNtaFBubWdVa25CUmpVNTd1MmtlTklqb3BWblFNemd6TThMV1VVWnA1dkxKV0ZXRWVza1NoOTY2YUkxYmM3OHJHcXA2Ukp3Z0d1bVJERTRpY1hqQ3IxRUhuSVAzeXpfVkp5LUI5ZVVYakVGbnhWOVRHZTJLVjA5RzVE?oc=5` — Greece's €93mn medicines bet yields €557mn in value, new study reveals
  7. `link:https://news.google.com/rss/articles/CBMixgFBVV95cUxQTnZzanpPU3RDZjJPc1B3akxmZ19aT2p5Q04wYS16NTFCT1RYM0RCQVd3QmNhWGJ1QmJraWh3M3BBNGE0UE9qOWpTLUhSUzJ0b3lZN1M1eWk1TnYwekthRmJ1am5TSFp0UE9lWVBwamRSb1J6ZF9CcGs2NUowVlR1YWF4QktoTk1rMmk4Y09idUJkbTZGbjFuZ1F6OTRRd3p1QjdTUjJzdFhIX2dJUTI0LUd0OFhFV0dyV3NwS3JEYm4tNWhNNVE?oc=5` — Critical raw materials: Sweden declares security of supply a matter of national security - Table.Briefings
  8. `link:https://news.google.com/rss/articles/CBMitwNBVV95cUxObmVjOWh1QTJxb3BBN0xiQ3pzZEFiQjhjZjItWDdfX3QxOXp4QVNqNFBMQi1sOWJISjl1dkw5VEZrLTRNUzNYMEhCclVhczlaR1oyM0NrV0FUSVlNVHdDQ1JtckkwRU0xWDFyaVlvVjZsVkZkV3M0SldJcEJvUXB2MTZEVkoyb0RFRU0wTExsdGNuQ05vdkdqZ2dYbTVHZC1PY2tuQUFoWkNvTkkybldmQ0dLSVA3YjJHWjlBcjhkNDVRSzNKcTFWbWpEOUp0ZENYVFkyOVlYb0FUTUNTV2RkWVFBNFNyMHdSZ1JHNXFzcnpXeHpMUjAzRG9XQVZUNDVkc21mVFI2S3BYRGY3RHVFaWxCbzc2WUI0SW1xMVJCRHVDOEwyX09RdEF3dDd3ZFFxeUFuRWlmY2pkVEQwVF9JYVVqNjlHcmNQdU1MS3FBQ2Q1YnZHd1VNanVMMXlwNXdxSHFqbEFOS21TcGhvXzJtVXJScV9oOVJfR0hrRmFtajl1ck5IVk45WGw3V0QwMzRjWEg2b04xb2hzcDJjUUxsRldlRlZTWC1oMFprcENPMXBCaW1JM1pN?oc=5` — Statement by the High Representative on behalf of the EU on the alignment of certain countries concerning restrictive measures in respect of actions undermining or threatening the territorial integrity, sovereignty and independence of Ukraine
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
