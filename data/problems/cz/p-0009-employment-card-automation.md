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
score: 7
scores:
  proof: 3
  money: 0
  urgency: 1
  demand: 1
  gap: 2
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
locals:
- name: Spring Walk (zamestnaneckekarty.cz)
  url: https://www.zamestnaneckekarty.cz/zamestnanecke-karty
  ico: '11740108'
  since: 2021
  competes: adjacent
  maturity: early
  evidence: 'a law firm, not a software vendor. zamestnaneckekarty.cz — the top Czech-language
    result for the process itself — is run by Spring Walk vízová kancelář s.r.o., ARES-dated
    August 2021, part of a Brno and Prague practice of over fifty people. What it sells is
    hands-on case handling billed per application. There is no portal, dashboard, status
    tracking or reminder anywhere on the page, and that missing layer is exactly what a
    software product would add. No limb of the established test is on file.'
- name: Foreigners.cz
  url: https://www.zamestnavamecizince.cz/
  competes: adjacent
  maturity: early
  evidence: 'a five-office relocation agency and knowledge portal, running the employer-facing
    site zamestnavamecizince.cz. What it sells is people doing the agenda, plus articles
    explaining it — there is nothing an employer logs into to see where an application stands.
    The group resolves in ARES as several separate Brno companies and none of them could be
    attributed to this site, so no IČO is claimed here and no launch year is on file.'
- name: ReloCzech
  url: https://www.reloczech.cz/
  competes: adjacent
  maturity: early
  evidence: 'sells a serviced immigration agenda: the provider files and chases the
    zaměstnanecká karta for the employer, case by case, for a fee. No self-service tracking is
    offered anywhere on the site. No company resolves in ARES under the trade name, so no IČO
    is claimed and no founding year is on file.'
- name: Expat Support
  url: https://expatsupport.cz/
  ico: '45148830'
  since: 1992
  competes: adjacent
  maturity: early
  evidence: 'sells a serviced immigration and expat agenda by the case rather than software.
    Expat Support s.r.o. is ARES-dated May 1992 and is by far the oldest provider here, but age
    is only the first limb of the test: nothing is named or counted on the buyer side, there is
    no public contract for the IČO in the Czech contracts register, no round and no state
    listing,
    so the second limb is unmet.'
- name: Principio
  ico: '07600330'
  competes: adjacent
  maturity: early
  evidence: 'sells a serviced immigration agenda and monitors document expiries as a service —
    a person watching the dates, which is the single function such a product would
    automate first. It is carried on its IČO rather than a link: ARES resolves one
    Brno company under this trade name, Principio s.r.o., registered in October 2018, and no
    product site was reachable to confirm the match, so the identification is stated here for
    a reader to check. No limb of the established test is on file.'
- name: DMPF Expat Assistant
  ico: '19765851'
  since: 2023
  competes: adjacent
  maturity: early
  evidence: 'sells a serviced immigration agenda under the Expat Assistant name. ARES resolves
    it as DMPF Consulting s.r.o., incorporated in October 2023, which makes it the youngest
    provider here; no product site was reachable, so it is carried on the IČO rather than a
    guessed domain. No limb of the established test is on file.'
- name: Workking
  url: https://workking.cz/sluzby/vyrizeni-zamestnanecke-karty/
  ico: '09553231'
  since: 2020
  competes: adjacent
  maturity: early
  evidence: 'sells the employee-card agenda by hand from offices in Prague and Brno, including
    for staffing agencies, which it says most of its competitors will not touch. It is people
    doing the filing: the site offers no portal, no case status a client can open and no expiry
    watch. ARES dates Workking s.r.o. to September 2020, and nothing on the site names or counts
    who it has filed for, so no limb of the established test is on file.'
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
- type: gap-check
  name: "Market scan — the same question, an in-domain control"
  why: "A Czech query written the way an employer would ask surfaced the agencies — including one this record had missed — and no software: the method finds providers in this market when they are there, and there is no product among them."
  url: https://workking.cz/sluzby/vyrizeni-zamestnanecke-karty/
  note: 'Gap check 2026-08-25, run because the rung-2 claim needed a control INSIDE this market:
    the 2026-08-20 control was Softlink CEM Smart and Ringil, real Czech incumbents but in metering
    and logistics, which proves the method works and proves nothing about immigration vendors.
    POSITIVE CONTROL, in domain, passed first: the descriptive Czech query "vyřízení zaměstnanecké
    karty pro zaměstnavatele služba agentura Brno Praha cizinci nábor", carrying no vendor name,
    returned zamestnaneckekarty.cz (Spring Walk) at the top — the provider this record already
    names — together with Workking s.r.o., a Prague and Brno agency the 2026-08-20 sweep missed,
    now added to the ledger. ARES resolved Workking s.r.o. under IČO 09553231, incorporated
    2020-09-29. So the method surfaces Czech providers in THIS market when they exist. SECOND
    SHAPE, the employer''s own words for the software this record proposes ("HR software evidence
    cizinců hlídání platnosti povolení k pobytu zaměstnanecké karty upozornění zaměstnavatel
    systém"): ministry and labour-office pages, an HR magazine, and ASB Group — a corporate
    services firm that files the employer''s foreigner reports by hand. No Czech product. NOT
    FOUND, on a controlled method: no Czech software that prepares an employee-card application,
    tracks its status for the employer or watches permit expiries. Everything found sells the
    outcome by hand and is on the ledger as adjacent. That is rung 2 as SCORING.md now words it —
    a check that found nobody SELLING THIS, with a passing positive control — and gap moves 1 → 2,
    score 6 → 7. Context noted, not scored: the same sweep surfaced a new obligation, a register of
    verified employers under the new foreigner act, without a dated receipt this pass could stand
    behind; it belongs to a urgency re-check, not to this one.'
  date: '2026-08-25'
  queries:
    - "vyřízení zaměstnanecké karty pro zaměstnavatele služba agentura Brno Praha cizinci nábor"
    - "HR software evidence cizinců hlídání platnosti povolení k pobytu zaměstnanecké karty upozornění zaměstnavatel systém"
  checked: [ares, google-cz]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-08-25'
---

Czech employers structurally depend on foreign workers — Ukraine, Philippines, India — channeled through government kvóty programs [S1,S2]. The zaměstnanecká karta pipeline is notoriously slow and paper-based [S1]; employers outsource it to relocation agencies and law firms that work manually at high fees, with no software layer for application preparation, status tracking or ongoing compliance (permit renewals, reporting duties) [S2].

Why now: the US shows the model being replicated rapidly — Gale (YC W25) automates the corporate visa pipeline, with Mayflower (YC F25) and LegalOS (YC W26) extending the cluster within a year [S1]. The playbook of software coordinating independent attorneys transfers to the Czech advokát market structure.

Who pays: employers with recurring foreign-hiring volume (manufacturing, logistics, healthcare, IT) who currently pay per-case agency fees; agencies themselves are a secondary buyer for tooling that raises their case throughput. The volume is large and documented: about 82,000 employee-card proceedings ran in 2024 — 14,287 new applications, 44,869 extensions and 22,793 employer changes [S5] — against an annual quota ceiling of roughly 45,300 that most countries never reach [S6]. What cannot be sized from public sources is the price: nine Czech relocation agencies and law firms were checked and not one publishes a per-case fee, so any revenue assumption here has no public receipt behind it and must come from a vendor conversation. The state fee alone is 1,000 CZK at an embassy [S5].

Existing non-solutions: ministry information pages, permit.cz (static form-filling guides), classic law firms (e.g. ARROWS) and manual relocation agencies [S2]. A 2026-08-13 search found no automation platform [S2], and a 2026-08-20 follow-up held that finding against a market that is dense but entirely manual: zamestnaneckekarty.cz turns out to be the law firm Spring Walk with no portal or tracking of any kind, Foreigners, ReloCzech, Expat Support, Principio and DMPF sell serviced immigration agendas, and ARES lists nine "Relocation" and fifteen "Expat" companies without a software vendor among them [S4]. A fresh Czech-language search on 2026-08-25 added one more agency, Workking, and again returned no product: what an employer can buy here is somebody else's staff doing the filing [S7].

Solved elsewhere: the US cluster above is the newest layer [S1,S3], but the proof sits closer to home. Localyze in Germany and Jobbatical in Estonia have sold employer-side immigration case handling across Europe for years — the ledger below carries both. What does not transfer is the procedure itself, which is national; the Czech process's paper-heaviness is exactly what makes an automation layer valuable.

## Revisions

2026-08-24 · evidence audit — Cut "labor shortage keeps hiring volumes up" from Why now: a trajectory claim with no second data point anywhere in the corpus — yc-gale documents employer dependence on foreign workers at a single point in time [S1], the same defect the 2026-08-20 audit removed from p-0007. The structural-dependence claim in the lead stands [S1,S2]. A fresh spot-check on this date (Czech query for foreigner-employment tracking software) returned only generic HR/asset registries (Aptien, plusPortal), consistent with the 2026-08-20 NOT FOUND verdict [S4]. Scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `scores.proof` 1 → 3: Localyze (Germany) and Jobbatical (Estonia) both pass the established test in two CEE-adjacent markets, while Gale and LegalOS are two years old. The 'Solved elsewhere' paragraph asserted that validation was US-only, which contradicted this record's own comps ledger, and it now names the two European players instead. `scores.gap` stays 1: the 2026-08-20 scan found a dense but entirely manual market — Spring Walk, Foreigners, ReloCzech, Expat Support, Principio, DMPF [S4] — and six commercial providers selling the outcome by hand are the weak incumbents of rung 1, not the empty field of rung 2. No `locals[]` key, because those are service firms rather than product vendors and the ledger the gap ladder reads is a ledger of products. `score` 4 → 6. Fifth pass this date, merged here: **this record gains a `locals[]` ledger for the first time**, reversing the decision recorded above to omit one. That decision was that the six providers found on 2026-08-20 are service firms rather than product vendors and the gap ladder reads a ledger of products. Under the split, "a service firm rather than a product vendor" is one of the things `competes: adjacent` exists to say, and naming them is the point. Six entries, all adjacent and all early: **Spring Walk** (zamestnaneckekarty.cz is run by Spring Walk vízová kancelář s.r.o., IČO 11740108, ARES-dated August 2021), **Foreigners.cz**, **ReloCzech**, **Expat Support** (IČO 45148830, ARES-dated May 1992), **Principio** (ARES resolves one Brno company under the trade name, Principio s.r.o., IČO 07600330) and **DMPF Expat Assistant** (DMPF Consulting s.r.o., IČO 19765851, October 2023) [S4]. Every evidence line says what the firm actually sells — a serviced agenda billed per case, with no portal, dashboard or status tracking — because that missing layer is exactly what this record proposes to build. Foreigners.cz and ReloCzech carry a URL and no IČO on purpose: the Foreigners.cz group resolves in ARES as several separate Brno companies and none could be attributed to the site, and no company resolves under the ReloCzech trade name, so neither IČO was guessed. ARROWS stays in the body as a general law firm rather than an immigration provider. `scores.gap` stays 1 and `score` stays 6: adjacent players never move the score. FLAGGED FOR MATCH, NOT CHANGED HERE: with every named local now labelled adjacent and no direct player on the ledger, the new ladder reads this record at rung 2 rather than rung 1, and the 2026-08-20 check does carry queries[], checked[] and a passing positive control — the only thing that can raise a gap score. Making that move is a scoring judgment under SPEC §4 and was not made in a schema-conversion pass. Sixth pass this date, merged here: that flag is now answered, and `scores.gap` moves 1 → 2, `score` 6 → 7. Rung 1 means locals sell this and are all early; nobody on this ledger sells this at all — six service firms and no product — so rung 1 was describing a record other than this one. Rung 2 costs a check with a passing positive control, and the 2026-08-20 control was Softlink CEM Smart and Ringil: real Czech incumbents, but in metering and logistics, which proves the method works and proves nothing about this market. So the check was run again with the control INSIDE this market [S7]. A descriptive Czech query written the way an employer would ask — no vendor name in it — put zamestnaneckekarty.cz at the top, and surfaced **Workking** (Workking s.r.o., IČO 09553231, ARES-dated September 2020), a Prague and Brno agency the earlier sweep missed, which does the cards by hand and advertises that it will do them for staffing agencies too. It is now the seventh entry on the ledger, adjacent and early. The method therefore finds Czech providers in this domain when they are there; a second query shape, in the words an employer would use for the software itself, returned ministry pages, an HR magazine and another firm filing reports by hand. No Czech product prepares the application, tracks its status or watches permit expiries. The non-solutions paragraph now says so and carries the new receipt [S7]. What the ladder still cannot say: rung 2 renders as an open field, and the field is not empty — it is full of people selling the outcome by hand at a price this record's buyer already pays. The ledger's adjacent half is where that fact lives, and it is the reason the entries are worth reading before the score. Noted and not scored: the same sweep surfaced a register of verified employers under the new foreigner act, without a dated receipt this pass could stand behind. No source note was edited and no [Sn] marker moved. Same pass, prose hygiene: ledger lines that talked about this file rather than about the market were reworded — they render under each entry on the public page, where a reader has no idea a register exists.
