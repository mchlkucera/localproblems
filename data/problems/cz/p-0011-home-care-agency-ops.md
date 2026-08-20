---
id: p-0011
region: cz
title: Czech home-care agencies burn scarce nurse time on phone-and-paper intake, scheduling
  and coordination
category: health
geo: CZ-national
score: 3
scores:
  proof: 1
  money: 0
  urgency: 1
  demand: 1
  gap: 0
status: watching
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
- type: gap-check
  url: https://veruapp.cz/
  note: 'Gap re-check 2026-08-20: OCCUPIED. The record claimed Cygnus DP was the only thing helping
    and that no Czech player automated agency operations; a Czech-language search of the operations
    layer returns domestic vendors immediately. VeruApp is a Czech multiplatform cloud application
    for terénní pečovatelské služby that builds each caregiver''s chronological daily work plan
    automatically from parameters in the client''s digital record, carries a field mobile app for
    logging delivered tasks, lets managers re-plan around sudden events and coordinate joint home
    visits, and runs client billing and statutory reporting off the same data — intake, scheduling
    and coordination, which is exactly the layer this record said was unbuilt. e-Sestřička sells a
    cloud system for domácí a paliativní péče covering odbornosti 925, 720 and 926, with Sestřička,
    Most k Domovu and AHC on its reference list; ARES resolves SESTŘIČKA.CZ s.r.o. (IČO 05752779,
    Praha, 2017) alongside a chain of regional SESTŘIČKA.CZ — DOMÁCÍ PÉČE s.r.o. entities. The
    information system at pecovatelska.cz, from Petr Zajíc software (trading since 1998), serves
    terénní sociální služby under zák. 108/2006 Sb. and is deployed in more than 200 locations
    across Czechia, sold one-time rather than as SaaS. E-péče adds a publicly funded fourth: an
    Ústecký-kraj project co-financed from OP Spravedlivá transformace, putting a field mobile app
    into 39 care providers including Město Bílina, Město Kadaň and Diecézní charita Litoměřice.
    POSITIVE CONTROL passed first — the same method surfaced Softlink CEM Smart and Ringil at the
    top of their queries, and ARES resolved IRESOFT s.r.o. (this record''s own named incumbent),
    SOFTLINK s.r.o. and Ringil s.r.o. by name. De-rank rule applied: gap 1 to 0 with incumbents
    named, score 4 to 3, status watching.'
  date: '2026-08-20'
  queries:
    - "software pro agentury domácí péče plánování směn pečovatelská služba"
    - "agentura domácí péče software plánování návštěv sester mobilní aplikace"
    - "Chytrá péče aplikace pro pečující rodiny česká sociální dávky"
  checked: [ares, google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-20'
---

Hundreds of Czech agentury domácí péče and pečovatelské služby — from Včelka to charity providers — coordinate care visits by phone and paper, with Cygnus DP (IRESOFT) serving as documentation and billing record-keeping rather than operations automation [S1,S2]. Under a chronic nurse shortage, every hour of intake calls, client onboarding and schedule juggling is an hour of clinical capacity lost; admin time savings convert directly into more clients served [S1]. The tooling gap, however, is narrower than this record originally judged: a 2026-08-20 re-check found Czech vendors already selling planning, field recording and coordination into exactly these agencies [S4].

Why now: the nurse shortage makes capacity the binding constraint, aging demographics grow demand, and AI-native operations layers for exactly this agency profile are being funded repeatedly in the US — Sage Care (YC S24) and Cova (YC S26) within two years of each other [S1,S3].

Who pays: the agencies. The pitch is capacity, not cost: an agency that automates intake and coordination can take on more reimbursed care with the same staff.

Existing non-solutions — superseded. The 2026-08-13 absence check found only the providers themselves and IRESOFT [S2], but it searched the wrong words: a Czech-language search of the operations layer returns domestic vendors on the first page [S4]. VeruApp plans each caregiver's day automatically from the client's digital record and carries a field mobile app; e-Sestřička covers domácí a paliativní péče across odbornosti 925, 720 and 926; the pecovatelska.cz system from Petr Zajíc software runs terénní sociální služby in more than 200 locations; and Ústecký kraj is putting the E-péče field app into 39 providers on EU money [S4]. Phone and paper are still widespread, but they are no longer the only option on the market.

Solved elsewhere: the US home-care AI-ops cluster above [S1,S3]. Arbitrage scored 1 (US-only) [S3]. What a domestic entrant would own is narrower than first written — not the operations layer as such, which is occupied [S4], but the AI-native slice of it: voice intake in Czech, and displacing or integrating with incumbents that already hold the scheduling and records seat.

---
**CORRECTION (2026-08-20, evidence audit):** Removed the sentence "Larger charity networks (Charita ČR) offer multi-branch deals." `Charita` returns no hits anywhere in the signal corpus; `yc-sagecare` supports only the generic phrase "charity providers", which the lead paragraph already carries. The named organisation and the multi-branch channel claim were both unbacked.

---
**CORRECTION (2026-08-20, gap re-check):** **De-ranked — the operations layer is occupied.** The original absence check was run in the wrong language and concluded that Cygnus DP was the only tooling in the market. Searching Czech for the operations layer returns domestic vendors on the first page: **VeruApp** (automatic daily work planning per caregiver from the client's digital record, field mobile app, billing and statutory reporting), **e-Sestřička** (cloud system for domácí a paliativní péče, odbornosti 925/720/926; SESTŘIČKA.CZ s.r.o., IČO 05752779), **pecovatelska.cz** from Petr Zajíc software (terénní sociální služby under zák. 108/2006 Sb., 200+ deployments) and **E-péče** (Ústecký kraj, OP Spravedlivá transformace, 39 providers) [S4]. Per the SPEC §4 de-rank rule: `gap` 1 → 0, `score` 4 → 3, `status` candidate → watching. The title lost the clause "with only a legacy record-keeping system to help", which the re-check disproved, and the non-solutions and comparables paragraphs were rewritten so the body no longer asserts an absence its own score denies. The underlying problem — phone-and-paper coordination under a nurse shortage — is not withdrawn; what is withdrawn is the claim that nobody sells into it.
