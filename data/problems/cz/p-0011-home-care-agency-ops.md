---
id: p-0011
region: cz
title: Czech home-care agencies burn scarce nurse time on phone-and-paper intake, scheduling
  and coordination, with only a legacy record-keeping system to help
category: health
geo: CZ-national
score: 4
scores:
  proof: 1
  money: 0
  urgency: 1
  demand: 1
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Czech-language intake and scheduling automation that coexists with Cygnus
    DP is real integration work for a dev plus care-domain pair, and small agencies
    buy on demonstrated capacity gains after a pilot, not self-serve.'
comps:
- name: Sage Care
  url: https://www.sagecare.ai/
  geo: US
  since: 2024
  traction: 'YC S24; AI intake/CRM for home-care agencies; claims 100+ min saved
    per intake (company site, 2026)'
  signal: yc-sagecare
- name: TakeCareOS
  url: https://www.ycombinator.com/companies/takecareos
  geo: US
  since: 2026
  traction: 'YC Spring 2026; 6 agencies with 200+ employees running ops on it (YC
    launch post, 2026)'
  signal: yc-takecareos
- name: Birdie
  url: https://www.birdie.care/
  geo: GB
  since: 2017
  traction: '$30M Series B led by Sofina (Sifted, 2022); $52M total; 700+ care providers'
- name: AlayaCare
  url: https://alayacare.com/
  geo: CA
  since: 2014
  traction: 'CAD $225M Series D (Businesswire, 2021); ~$274M total raised; 500+ care
    organizations'
  markets: [US, AU]
sources:
- type: arbitrage
  url: https://www.ycombinator.com/companies/sagecare
  note: 'yc-sagecare: Sage Care (YC S24) automates home-care agency operations with AI — intake,
    communication, scheduling busywork; Cova (S26, AI-native home care agency) shows the model
    being replicated. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-sagecare
- type: gap-check
  url: https://www.ycombinator.com/companies/sagecare
  note: 'Absence check 2026-08-13: CZ searches return only care providers themselves and IRESOFT
    Cygnus DP (documentation/billing records, no AI ops automation). Demand point: signal
    documents hundreds of agentury domácí péče running on phone + paper + Cygnus DP under
    a chronic nurse shortage.'
  date: '2026-08-13'
- type: arbitrage
  url: https://www.ycombinator.com/companies/takecareos
  note: 'yc-takecareos: TakeCareOS (YC Spring 2026) — AI-native operating system for long-term
    care providers; third US company on care-ops within two years. Still US-only: arbitrage
    stays 1.'
  date: '2026-08-13'
  signal: yc-takecareos
created: '2026-08-13'
updated: '2026-08-20'
---

Hundreds of Czech agentury domácí péče and pečovatelské služby — from Včelka to charity providers — coordinate care visits by phone and paper, with Cygnus DP (IRESOFT) serving as documentation and billing record-keeping rather than operations automation [S1,S2]. Under a chronic nurse shortage, every hour of intake calls, client onboarding and schedule juggling is an hour of clinical capacity lost; admin time savings convert directly into more clients served [S1].

Why now: the nurse shortage makes capacity the binding constraint, aging demographics grow demand, and AI-native operations layers for exactly this agency profile are being funded repeatedly in the US — Sage Care (YC S24) and Cova (YC S26) within two years of each other [S1,S3].

Who pays: the agencies. The pitch is capacity, not cost: an agency that automates intake and coordination can take on more reimbursed care with the same staff. Larger charity networks (Charita ČR) offer multi-branch deals.

Existing non-solutions: phone, paper, and Cygnus DP as the system of record; no Czech AI ops automation was found in the 2026-08-13 absence check — only the providers themselves and IRESOFT [S2].

Solved elsewhere: the US home-care AI-ops cluster above [S1,S3]. Arbitrage scored 1 (US-only) [S3]; Czech-language voice/intake automation and Cygnus DP integration are the localization work a domestic entrant would own.
