---
id: p-0009
region: cz
title: Czech employers hiring foreign workers push zaměstnanecká karta applications through
  a notoriously slow paper process via manual relocation agencies and law firms
fix: 'Software that files a Czech employee card — the work-and-residence permit for a
  foreign hire — end to end for the employer: documents, submission and status tracking,
  instead of a per-case agency fee.'
category: legal-compliance
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
  note: 'Software plus attorney coordination on the Gale model needs a dev and an
    immigration-domain partner rather than any certification, and employers already
    paying per-case agency fees can convert within an SMB pilot cycle.'
comps:
- name: Gale
  url: https://galevisa.com/
  geo: US
  since: 2024
  traction: '$2.7M seed, Apr 2025 (Business Insider, 2025); automates H-1B pipeline,
    coordinates independent attorneys'
  signal: yc-gale
- name: LegalOS
  url: https://www.ycombinator.com/companies/legalos
  geo: US
  since: 2024
  traction: 'YC W26; claims 100% approval across dozens of filings, 48h turnaround
    (YC profile, 2026)'
  signal: yc-legalos
- name: Localyze
  url: https://www.localyze.com/
  geo: DE
  since: 2018
  traction: '$35M Series B led by General Catalyst (TechCrunch, 2022); revenue up
    6x YoY; 10 European markets'
- name: Jobbatical
  url: https://www.jobbatical.com/
  geo: EE
  since: 2014
  traction: '€11.6M Series A (TechCrunch, 2022); clients incl. N26, TravelPerk, Personio;
    live in 8 countries'
  markets: [DE, ES, GB, PT, FR, NL]
sources:
- type: arbitrage
  name: "Gale"
  why: "A $2.7M-seed US company automating the corporate work-visa pipeline — application prep, compliance, HR integration — by coordinating independent attorneys rather than replacing them."
  url: https://www.ycombinator.com/companies/gale
  note: 'yc-gale: Gale (YC W25) automates the corporate work-visa pipeline — application prep,
    compliance, HR-system integration, coordinating independent attorneys; Mayflower (YC F25)
    and LegalOS (W26) show the cluster is hot. All US, scored as one analog.'
  date: '2026-08-13'
  signal: yc-gale
- type: gap-check
  name: "First Czech market scan"
  why: "An early sweep that surfaced ministry pages, law firms and static form-filling guides, and documented the employee-card process as slow, paper-based and handled manually at high fees."
  url: https://www.ycombinator.com/companies/gale
  note: 'Absence check 2026-08-13: searches surface ministry pages, law firms (ARROWS) and
    permit.cz (static form-filling guides); no automation platform. Demand point: signal documents
    the zaměstnanecká karta process as notoriously slow and paper-based, with relocation agencies
    working manually at high fees; CZ employers depend on government kvóty programs for workers
    from Ukraine, Philippines, India.'
  date: '2026-08-13'
- type: arbitrage
  name: "LegalOS"
  why: "'The AI-Native Immigration Law Firm' (YC W26) — a service firm rather than a software vendor, which is the form factor that fits a paper-based process best."
  url: https://www.ycombinator.com/companies/legalos
  note: 'yc-legalos: LegalOS (YC W26) — ''The AI-Native Immigration Law Firm'', an AI-first
    service firm rather than software vendor; the service-firm form factor is the most transferable
    to the CZ paper-based karta process.'
  date: '2026-08-13'
  signal: yc-legalos
- type: gap-check
  name: "Market scan — Czech immigration providers"
  why: "Six searches and an ARES sweep found a dense manual market — Spring Walk, Foreigners, ReloCzech, Expat Support, Principio, DMPF — with no portal, dashboard or tracking, and no software vendor among them."
  url: https://www.zamestnaneckekarty.cz/zamestnanecke-karty
  note: 'Gap re-check 2026-08-20: looked for the specific thing this record claims missing — a
    Czech software layer doing zaměstnanecká karta application preparation, status tracking or
    ongoing compliance (renewals, reporting duties) for employers. Six searches plus an ARES sweep
    found a dense market of MANUAL providers and no platform. zamestnaneckekarty.cz, the top
    Czech-language result for the process itself, is operated by Spring Walk, an advokátní kancelář
    in Brno and Prague (50+ staff, 11 years) and describes hands-on case handling with no portal,
    dashboard, tracking or reminder system anywhere on the page. Foreigners / zamestnavamecizince.cz
    is a five-office relocation agency and knowledge portal, not a dashboard; ReloCzech, Expat
    Support, Principio and DMPF Expat Assistant all sell serviced immigration agendas (Principio
    monitors document expiries as a service). ARES lists nine "Relocation" companies and fifteen
    "Expat" entities, all service, tax or consulting firms — no software vendor among them. The only
    self-service tracking found for the Czech process is inside Deel, a foreign EOR platform, which
    is not a local entrant and does not de-rank. A StartupJobs-targeted query returned nothing
    on-topic and that surface is therefore not claimed here. POSITIVE CONTROL passed first: the same
    method surfaced Softlink CEM Smart and Ringil at the top of their queries, and ARES resolved
    IRESOFT s.r.o., SOFTLINK s.r.o. and Ringil s.r.o. by name. Verdict: NOT FOUND — no de-rank, and
    a negative never raises a score, so gap stays 1 and the total is unchanged.'
  date: '2026-08-20'
  queries:
    - "zaměstnanecká karta software pro zaměstnavatele automatizace vyřízení"
    - "platforma pro zaměstnávání cizinců relokace software sledování víz Česko"
    - "systém pro správu pobytových oprávnění cizinců zaměstnanců HR software hlídání platnosti víz"
    - "DMPF Expat Assistant software zaměstnávání cizinců systém sledování žádostí"
    - "startupjobs.cz relokace cizinců imigrace startup platforma zaměstnanecké karty"
    - "immigration software platform Czech Republic employee card employer visa tracking SaaS"
  checked: [ares, google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: news
  url: https://mv.gov.cz/migrace/clanek/vyrocni-zpravy-o-situaci-v-oblasti-migrace-a-integrace.aspx
  name: 'Interior Ministry migration report 2024'
  why: The transaction volume this product would automate — new applications, extensions and employer changes, counted by the ministry that decides them.
  note: 'MV CR OAMP annual report for 2024 (published 30 Jul 2025): 14,287 new employee-card applications filed at embassies, 12,843 granted; 44,869 employment-purpose extension applications; 22,793 employer/position-change notifications. Total employer-facing proceedings approximately 82,000 for the year. The same report records 3,518 formal complaints of administrative inaction, upheld in 40.6% of cases.'
  date: '2025-07-30'
- type: regulation
  url: https://www.zakonyprolidi.cz/cs/2019-220
  name: 'Government Decree 220/2019: employee-card quotas'
  why: The hard ceiling on annual volume — and evidence the constraint is processing capacity rather than quota.
  note: 'Narizeni vlady 220/2019 Sb., in force version effective 1 Jul 2026, sets a maximum of approximately 45,300 employee-card applications a year across listed embassies (Priloha 2: 44,820; Priloha 3: 480). Utilisation is far below the ceiling for most countries - Ukraine drew about 10% of its 11,000 capacity in 2024 - so quota is not the binding constraint except for India and Kazakhstan.'
  date: '2026-07-01'
created: '2026-08-13'
updated: '2026-08-25'
---

Czech employers structurally depend on foreign workers — Ukraine, Philippines, India — channeled through government kvóty programs [S1,S2]. The zaměstnanecká karta pipeline is notoriously slow and paper-based [S1]; employers outsource it to relocation agencies and law firms that work manually at high fees, with no software layer for application preparation, status tracking or ongoing compliance (permit renewals, reporting duties) [S2].

Why now: the US shows the model being replicated rapidly — Gale (YC W25) automates the corporate visa pipeline, with Mayflower (YC F25) and LegalOS (YC W26) extending the cluster within a year [S1]. The playbook of software coordinating independent attorneys transfers to the Czech advokát market structure.

Who pays: employers with recurring foreign-hiring volume (manufacturing, logistics, healthcare, IT) who currently pay per-case agency fees; agencies themselves are a secondary buyer for tooling that raises their case throughput. The volume is large and documented: about 82,000 employee-card proceedings ran in 2024 — 14,287 new applications, 44,869 extensions and 22,793 employer changes [S5] — against an annual quota ceiling of roughly 45,300 that most countries never reach [S6]. What cannot be sized from public sources is the price: nine Czech relocation agencies and law firms were checked and not one publishes a per-case fee, so any revenue assumption here has no public receipt behind it and must come from a vendor conversation. The state fee alone is 1,000 CZK at an embassy [S5].

Existing non-solutions: ministry information pages, permit.cz (static form-filling guides), classic law firms (e.g. ARROWS) and manual relocation agencies [S2]. A 2026-08-13 search found no automation platform [S2], and a 2026-08-20 follow-up held that finding against a market that is dense but entirely manual: zamestnaneckekarty.cz turns out to be the law firm Spring Walk with no portal or tracking of any kind, Foreigners, ReloCzech, Expat Support, Principio and DMPF sell serviced immigration agendas, and ARES lists nine "Relocation" and fifteen "Expat" companies without a software vendor among them [S4].

Solved elsewhere: the US YC cluster above [S1,S3]. Validation is US-only and immigration processes are jurisdiction-specific; the counterweight is that the Czech process's paper-heaviness is exactly what makes an automation layer valuable.

## Revisions

2026-08-24 · evidence audit — Cut "labor shortage keeps hiring volumes up" from Why now: a trajectory claim with no second data point anywhere in the corpus — yc-gale documents employer dependence on foreign workers at a single point in time [S1], the same defect the 2026-08-20 audit removed from p-0007. The structural-dependence claim in the lead stands [S1,S2]. A fresh spot-check on this date (Czech query for foreigner-employment tracking software) returned only generic HR/asset registries (Aptien, plusPortal), consistent with the 2026-08-20 NOT FOUND verdict [S4]. Scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched.
