---
id: p-0009
region: cz
title: 'Czech work permits for foreign staff get stuck, and agencies still do every file by hand'
brief: 'Every renewal or job change means a new file, prepared case by case [S5,S7]. The ministry got 3,518 complaints in 2024 that foreigners'' cases sat untouched [S5].'
solution: 'Build software for employers and their agencies that prepares work-permit files, tracks each case and warns before permits expire.'
good_for: 'Someone who''d like to work with employers who hire foreign workers.'
price_search: 'Registr smluv full-text for "zaměstnanecká karta" or "relokační služby" — a
  public employer that hires abroad, a fakultní nemocnice (teaching hospital) or a university,
  publishes its relocation-agency contract there with the per-case fee; otherwise ask the HR
  director of a fakultní nemocnice or the head of a university''s welcome office what an agency
  charges per card; the MS2021+ index under "cizinců" returns only state integration centres,
  not the employer''s filing.'
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
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: open
  integration: software
  money: bootstrap
  why: 'Easier: employers already pay a fee for every case, no licence or regulator stands in the way, and the seven Czech providers all do the work by hand. Harder: the filing itself is still on paper, and no provider publishes its fee, so the price has to be learned one conversation at a time.'
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
  evidence: 'A law firm, not a software vendor: zamestnaneckekarty.cz — the top Czech-language
    result for the process itself — is run by Spring Walk vízová kancelář s.r.o., registered in
    August 2021 and part of a Brno and Prague practice of over fifty people. What it sells is
    hands-on case handling billed per application; there is no portal, dashboard, status
    tracking or reminder anywhere on the page, and that missing layer is exactly what a
    software product would add.'
- name: Foreigners.cz
  url: https://www.zamestnavamecizince.cz/
  competes: adjacent
  maturity: early
  evidence: 'A five-office relocation agency and knowledge portal running the employer-facing
    site zamestnavamecizince.cz. What it sells is people doing the paperwork, plus articles
    explaining it — there is nothing an employer logs into to see where an application stands —
    and the group appears on the state business register as several separate Brno companies,
    none of which could be tied to this site, so no company number or launch year is claimed
    here.'
- name: ReloCzech
  url: https://www.reloczech.cz/
  competes: adjacent
  maturity: early
  evidence: 'Sells a serviced immigration agenda: the provider files and chases the employee card
    for the employer, case by case, for a fee, with no self-service tracking offered anywhere
    on the site. No company of that trade name appears on the state business register, so no
    company number or founding year is claimed here.'
- name: Expat Support
  url: https://expatsupport.cz/
  ico: '45148830'
  since: 1992
  competes: adjacent
  maturity: early
  evidence: 'Sells a serviced immigration and expat agenda by the case rather than software.
    Expat Support s.r.o. has been registered since May 1992 and is by far the oldest provider
    here, but it names and counts nobody on the buyer side, holds no public contract in the
    state contracts register and discloses no funding.'
- name: Principio
  ico: '07600330'
  competes: adjacent
  maturity: early
  evidence: 'Sells a serviced immigration agenda and watches document expiry dates as a service —
    a person watching the dates, which is the single function such a product would automate
    first. One Brno company of that trade name sits on the state business register, Principio
    s.r.o., registered in October 2018; no product site was reachable to confirm the match, so
    the identification is stated here for a reader to check, and it names no client.'
- name: DMPF Expat Assistant
  ico: '19765851'
  since: 2023
  competes: adjacent
  maturity: early
  evidence: 'Sells a serviced immigration agenda under the Expat Assistant name. The state
    business register resolves it as DMPF Consulting s.r.o., incorporated in October 2023,
    which makes it the youngest provider here; no product site was reachable, and it names no
    client.'
- name: Workking
  url: https://workking.cz/sluzby/vyrizeni-zamestnanecke-karty/
  ico: '09553231'
  since: 2020
  competes: adjacent
  maturity: early
  evidence: 'Sells the employee-card agenda by hand from offices in Prague and Brno, including
    for staffing agencies, which it says most of its competitors will not touch. It is people
    doing the filing — no portal, no case status a client can open, no expiry watch — and the
    company, registered in September 2020, names nobody it has filed for.'
process:
  summary:
    today: 'An agency or law firm prepares each employee-card file by hand, the interior ministry decides it, and no Czech provider offers software that tracks the case or its expiry date [S4,S5].'
  steps:
  - who: An agency or law firm
    today: 'Prepares each permit file by hand'
    known: documented
    cites: [4, 7]
    change: changes
    after: 'Prepares the file in shared software'
  - who: Interior ministry
    today: 'Decides each case; some sit untouched'
    known: documented
    cites: [5]
    change: stays
    after: 'Unchanged: the ministry still decides'
  - who: '?'
    today: 'How an employer follows its case today is not known'
    known: unknown
    cites: []
    change: changes
    after: 'The employer sees where each case stands'
  - who: An agency, for clients who pay for it
    today: 'Watches permit expiry dates by hand'
    known: documented
    cites: [4]
    change: changes
    after: 'Software warns before each permit expires'
sources:
- type: arbitrage
  name: "Gale"
  gist: "the $2.7M US template"
  why: "A $2.7M-seed US company automating the corporate work-visa pipeline — application prep, compliance, HR integration — by coordinating independent attorneys rather than replacing them."
  url: https://www.ycombinator.com/companies/gale
  note: 'yc-gale: Gale (YC W25) automates the corporate work-visa pipeline — application prep,
    compliance, HR-system integration, coordinating independent attorneys; Mayflower (YC F25)
    and LegalOS (W26) show the cluster is hot. All US, scored as one analog.'
  date: '2026-08-13'
  signal: yc-gale
- type: gap-check
  name: "First Czech market scan"
  gist: "the first Czech sweep"
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
  gist: "the AI-native law firm"
  why: "'The AI-Native Immigration Law Firm' (YC W26) — a service firm rather than a software vendor, which is the form factor that fits a paper-based process best."
  url: https://www.ycombinator.com/companies/legalos
  note: 'yc-legalos: LegalOS (YC W26) — ''The AI-Native Immigration Law Firm'', an AI-first
    service firm rather than software vendor; the service-firm form factor is the most transferable
    to the CZ paper-based karta process.'
  date: '2026-08-13'
  signal: yc-legalos
- type: gap-check
  name: "Market scan — Czech immigration providers"
  gist: "the six-agency sweep"
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
  gist: "the 82,000-proceeding count"
  why: The transaction volume this product would automate — new applications, extensions and employer changes, counted by the ministry that decides them.
  note: 'MV CR OAMP annual report for 2024 (published 30 Jul 2025): 14,287 new employee-card applications filed at embassies, 12,843 granted; 44,869 employment-purpose extension applications; 22,793 employer/position-change notifications. Total employer-facing proceedings approximately 82,000 for the year. The same report records 3,518 formal complaints of administrative inaction, upheld in 40.6% of cases.'
  date: '2025-07-30'
- type: regulation
  url: https://www.zakonyprolidi.cz/cs/2019-220
  name: 'Government Decree 220/2019: employee-card quotas'
  gist: "the 45,300 quota ceiling"
  why: The hard ceiling on annual volume — and evidence the constraint is processing capacity rather than quota.
  note: 'Narizeni vlady 220/2019 Sb., in force version effective 1 Jul 2026, sets a maximum of approximately 45,300 employee-card applications a year across listed embassies (Priloha 2: 44,820; Priloha 3: 480). Utilisation is far below the ceiling for most countries - Ukraine drew about 10% of its 11,000 capacity in 2024 - so quota is not the binding constraint except for India and Kazakhstan. dims set empty on 2026-09-19: the decree caps what the state accepts and puts no dated duty on employers, so it backs no Why now point.'
  date: '2026-07-01'
  dims: []
- type: gap-check
  name: "Market scan — the same question, an in-domain control"
  gist: "the in-domain control check"
  why: "A Czech query written the way an employer would ask surfaced the agencies — including one an earlier search had missed — and no software: the method finds providers in this market when they are there, and there is no product among them."
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
- type: regulation
  name: "Zákon 18/2004 novela — assessing non-EU qualifications"
  gist: "a second file per hire, 2028"
  why: "From 1 January 2028 Czechia is to get its first route for assessing a professional qualification earned outside the EU — today a diploma is recognised but that is often not enough to enter a regulated profession, so every third-country hire into one carries a second dossier alongside the employee card."
  url: https://odok.gov.cz/portal/services/download/attachment/KORNDXANW6BC/
  note: 'reg-uznavani-kvalifikace-treti-zeme-2028: education ministry draft amending act 18/2004,
    důvodová zpráva attachment cited (no Závěrečná zpráva RIA is attached); the draft is the one
    the scripted feed holds as veklep-KORNDXAMWBJD. Authorised 2026-08-25, in comment procedure;
    effective date read verbatim from the article-by-article part ("Účinnost je navrhována na
    1. ledna 2028") and matching the legislative plan (to government by 12.2026, effect 01.28).
    It is the first full revision of the act since 2004 and cures the breach the Court of Justice
    found in C-75/22 Commission v Czech Republic (articles 3(1)(g),(h), 7(3) and 51(1) of directive
    2005/36). Other limbs: activities involving the exercise of public authority put expressly out
    of scope, paper applications for the European Professional Card abolished, and assessment by a
    public-law employer removed as unused. Why it is on THIS record: the duty-holder is the same
    employer, the same hire and the same document-handling agenda the employee card creates — the
    second file a third-country hire into a regulated profession needs. The Commission separately
    counts 365 regulated professions in Czechia, second in the EU (ecsem-cz2026-admin-burden,
    linked at p-0003), which sizes how often that second file is required. Filed as context: 2028
    is beyond the 18-month deadline window, so it moves no score. Corrected 2026-09-19: 1 January
    2028 is inside 18 months of 2026-09-19. The draft backs Why now 1 because it is a bill in
    comment procedure, not enacted law, so it fails REAL (SCORING.md URGENCY); dims set to
    [urgency].'
  date: '2028-01-01'
  signal: reg-uznavani-kvalifikace-treti-zeme-2028
  dims: [urgency]
- type: regulation
  name: "Act 634/2004 on administrative fees — the embassy fee for an employee card"
  gist: "the 5,000 CZK state fee"
  why: "The state's fee schedule: an embassy charges 5,000 CZK to accept an application for an employee card."
  url: https://www.zakonyprolidi.cz/cs/2004-634
  note: 'Zákon č. 634/2004 Sb., o správních poplatcích, version in force 1 Sep 2026 to 31 Dec 2027
    (verze 166), read 2026-09-19. Sazebník, Část XII Konzulární poplatky, položka 162: "c) Přijetí
    žádosti o vydání zaměstnanecké karty, modré karty, karty vnitropodnikově převedeného
    zaměstnance, karty vnitropodnikově převedeného zaměstnance jiného členského státu Evropské unie
    nebo povolení k dlouhodobému pobytu za účelem investování Kč 5000"; "d) Zpracování objednávky k
    sjednání termínu osobního podání žádosti o vydání povolení k dlouhodobému nebo trvalému pobytu
    Kč 1000" — probably where the earlier 1,000 CZK came from, but it is the booking of the
    appointment, not the application, and this item does not name the employee card. Domestic fees
    (položka 116) are 2,500 CZK for a residence-permit application or an extension. Added to replace
    the uncited 1,000 CZK embassy fee. dims empty: backs no score.'
  date: '2026-09-19'
  dims: []
created: '2026-08-13'
updated: '2026-09-19'
---

A worker hired from outside the EU needs an employee card to work and live here, and agencies prepare each file by hand [S4,S7].

- About 82,000 employee-card cases went through the interior ministry in 2024 [S5].
- Each renewal or job change means a new file, prepared by hand [S5,S7].
- No Czech software prepares the file, tracks it or watches its deadlines [S4,S7].

Czech employers hire from Ukraine, the Philippines and India through government quota programmes [S1,S2]. Getting an employee card is slow and runs on paper [S1,S2]. After it is issued come renewals and the employer's reporting duties, and no Czech product watches those dates for the employer [S4].

- The 82,000 were 14,287 new applications filed at embassies, 44,869 extensions and 22,793 changes of employer or position [S5]. 12,843 new cards were granted that year [S5].
- A government decree caps new applications at about 45,300 a year across the listed embassies, and most countries never come close [S6].
- Ukraine used about 10% of its 11,000 places in 2024, and only for India and Kazakhstan is the quota the real limit [S6].

Existing non-solutions: Seven Czech agencies and law firms sell this work by hand, and none sells software that tracks a case [S4,S7].

Each sells a person doing the paperwork, case by case, with no portal, dashboard or status a client can open [S4,S7].

- The top Czech search result for the process belongs to a law practice in Brno and Prague that handles each case by hand [S4].
- One agency watches clients' permit expiry dates as a service: a person watching the dates, not software [S4].
- One agency in Prague and Brno also files cards for staffing-agency workers, which it says comparable firms rarely do [S7].
- A corporate services firm files employers' reports on their foreign staff by hand [S7].
- The state business register lists nine "Relocation" and fifteen "Expat" companies, all service, tax or consulting firms [S4].
- Ministry pages, form-filling guides such as permit.cz and general law firms such as ARROWS (a Czech law firm) make up the rest, and none of them is software that does the work [S2].
- The only self-service tracking of the Czech process sits inside Deel, a foreign platform that employs staff on a company's behalf [S4].

Why now: Foreign staff wait on stalled permit cases, and every renewal or job change means a new file prepared by hand [S5,S7].

- 3,518 complaints in 2024 said foreigners' cases sat untouched, and 40.6% were upheld [S5].
- 44,869 extensions and 22,793 job changes in 2024 each needed a new file [S5].
- Employers pay agencies high fees for each file done by hand [S2].

A draft law would add a second file for some of these hires from 2028 [S8]:

- From 1 January 2028 Czechia is to get its first route for assessing a professional qualification earned outside the EU [S8].
- Today such a diploma can be recognised, but that is often not enough to enter a regulated profession [S8]. So a hire into one needs a second file beside the employee card [S8].
- The European Commission counts 365 regulated professions in Czechia, the second most in the EU [S8].
- The draft comes from the education ministry and went out for comment in August 2026 [S8]. It is the first full revision since 2004 of the act on recognising qualifications, and it answers a ruling of the EU Court of Justice against Czechia [S8].

Who pays: Employers already pay agencies and law firms to prepare each file by hand, but no Czech provider publishes its fee [S2,S4].

- Agencies charge high fees for files they prepare by hand [S2].
- A Brno and Prague law practice of over fifty people does this work [S4].
- One agency sells watching clients' permit expiry dates as a service [S4].

What the work costs is not public:

- None of nine Czech agencies and law firms publishes a per-case fee, so the price has to be asked for [S4,S7].
- The state's own fee is public: an embassy charges 5,000 CZK to accept each application [S9].
- Agencies are a likely second buyer, for software that lets the same staff handle more cases.

Solved elsewhere: Funded companies in Germany, Estonia and the US already handle employers' work-permit cases with software [S1,S3].

A German company and an Estonian one have sold employer-side immigration case handling for years, both funded at Series A or later, and the Estonian one names well-known European tech firms among its clients.

In the US, a company with a $2.7M seed round automates the corporate work-visa pipeline: application prep, compliance and links to the company's personnel systems [S1]. It coordinates independent attorneys rather than replacing them [S1]. Two more US companies followed within about a year: Mayflower, which screens hires for immigration issues for personnel teams, and an AI-native immigration law firm [S1,S3]. Y Combinator, the US startup accelerator, backed all three, in its batches from winter 2025 to winter 2026 [S1]. The work-visa company and the law firm both started in 2024 [S1,S3].

That model fits Czechia, where this work sits with agencies and law firms [S1,S3]. A service firm run on software, rather than software sold to a firm, is the form that fits a paper-based process best [S3]. The Czech procedure is national and runs on paper, which is a local builder's edge [S1,S2].

## First moves

1. Build a simple deadline watch that warns an employer before each foreign worker's employee card or permit runs out. It files nothing and carries no legal risk, so it can ship before any filing feature. Today one agency sells this as a person watching the dates, and no Czech product does it; the only self-service tracking sits inside a foreign platform, as [Market gap](#competition) shows. Give an employer one screen with every worker's dates and a warning well before each one, and let the agency it already uses see the same screen.
2. Point the first version at renewals and job changes rather than new hires, because they are most of the cases and they keep coming back. The ministry's own counts, under [The opportunity](#opportunity), show extensions and changes of employer far outnumber new applications filed at embassies. Renewals run to fixed dates and are filed inside Czechia, so someone at the employer has to watch every one of them. That person is the user to design for.
3. Call the heads of personnel at employers who hire from outside the EU, and open with the ministry's count of complaints about stalled cases. The count and the share upheld are under [Why now](#why-now). Ask how many of last year's hires started late, and who found out first. The cost that matters to them is less the agency fee than the worker who cannot start on time, and their answers show which warning to build next.
4. Offer the same software to the agencies and law firms that prepare these files, so the same staff can handle more cases. One of them is a large law practice in Brno and Prague, and another also takes staffing-agency workers, which it says comparable firms rarely do; see [Market gap](#competition). More cases per person is their margin, so show them the time saved per file. Go in knowing that none of them publishes a per-case fee, so ask what they charge before you set your own price; see [Willing to pay](#willing-to-pay).

## Revisions

2026-08-24 · evidence audit — Cut "labor shortage keeps hiring volumes up" from Why now: a trajectory claim with no second data point anywhere in the corpus — yc-gale documents employer dependence on foreign workers at a single point in time [S1], the same defect the 2026-08-20 audit removed from p-0007. The structural-dependence claim in the lead stands [S1,S2]. A fresh spot-check on this date (Czech query for foreigner-employment tracking software) returned only generic HR/asset registries (Aptien, plusPortal), consistent with the 2026-08-20 NOT FOUND verdict [S4]. Scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `scores.proof` 1 → 3: Localyze (Germany) and Jobbatical (Estonia) both pass the established test in two CEE-adjacent markets, while Gale and LegalOS are two years old. The 'Solved elsewhere' paragraph asserted that validation was US-only, which contradicted this record's own comps ledger, and it now names the two European players instead. `scores.gap` stays 1: the 2026-08-20 scan found a dense but entirely manual market — Spring Walk, Foreigners, ReloCzech, Expat Support, Principio, DMPF [S4] — and six commercial providers selling the outcome by hand are the weak incumbents of rung 1, not the empty field of rung 2. No `locals[]` key, because those are service firms rather than product vendors and the ledger the gap ladder reads is a ledger of products. `score` 4 → 6. Fifth pass this date, merged here: **this record gains a `locals[]` ledger for the first time**, reversing the decision recorded above to omit one. That decision was that the six providers found on 2026-08-20 are service firms rather than product vendors and the gap ladder reads a ledger of products. Under the split, "a service firm rather than a product vendor" is one of the things `competes: adjacent` exists to say, and naming them is the point. Six entries, all adjacent and all early: **Spring Walk** (zamestnaneckekarty.cz is run by Spring Walk vízová kancelář s.r.o., IČO 11740108, ARES-dated August 2021), **Foreigners.cz**, **ReloCzech**, **Expat Support** (IČO 45148830, ARES-dated May 1992), **Principio** (ARES resolves one Brno company under the trade name, Principio s.r.o., IČO 07600330) and **DMPF Expat Assistant** (DMPF Consulting s.r.o., IČO 19765851, October 2023) [S4]. Every evidence line says what the firm actually sells — a serviced agenda billed per case, with no portal, dashboard or status tracking — because that missing layer is exactly what this record proposes to build. Foreigners.cz and ReloCzech carry a URL and no IČO on purpose: the Foreigners.cz group resolves in ARES as several separate Brno companies and none could be attributed to the site, and no company resolves under the ReloCzech trade name, so neither IČO was guessed. ARROWS stays in the body as a general law firm rather than an immigration provider. `scores.gap` stays 1 and `score` stays 6: adjacent players never move the score. FLAGGED FOR MATCH, NOT CHANGED HERE: with every named local now labelled adjacent and no direct player on the ledger, the new ladder reads this record at rung 2 rather than rung 1, and the 2026-08-20 check does carry queries[], checked[] and a passing positive control — the only thing that can raise a gap score. Making that move is a scoring judgment under SPEC §4 and was not made in a schema-conversion pass. Sixth pass this date, merged here: that flag is now answered, and `scores.gap` moves 1 → 2, `score` 6 → 7. Rung 1 means locals sell this and are all early; nobody on this ledger sells this at all — six service firms and no product — so rung 1 was describing a record other than this one. Rung 2 costs a check with a passing positive control, and the 2026-08-20 control was Softlink CEM Smart and Ringil: real Czech incumbents, but in metering and logistics, which proves the method works and proves nothing about this market. So the check was run again with the control INSIDE this market [S7]. A descriptive Czech query written the way an employer would ask — no vendor name in it — put zamestnaneckekarty.cz at the top, and surfaced **Workking** (Workking s.r.o., IČO 09553231, ARES-dated September 2020), a Prague and Brno agency the earlier sweep missed, which does the cards by hand and advertises that it will do them for staffing agencies too. It is now the seventh entry on the ledger, adjacent and early. The method therefore finds Czech providers in this domain when they are there; a second query shape, in the words an employer would use for the software itself, returned ministry pages, an HR magazine and another firm filing reports by hand. No Czech product prepares the application, tracks its status or watches permit expiries. The non-solutions paragraph now says so and carries the new receipt [S7]. What the ladder still cannot say: rung 2 renders as an open field, and the field is not empty — it is full of people selling the outcome by hand at a price this record's buyer already pays. The ledger's adjacent half is where that fact lives, and it is the reason the entries are worth reading before the score. Noted and not scored: the same sweep surfaced a register of verified employers under the new foreigner act, without a dated receipt this pass could stand behind. No source note was edited and no [Sn] marker moved. Same pass, prose hygiene: ledger lines that talked about this file rather than about the market were reworded — they render under each entry on the public page, where a reader has no idea a register exists. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Kept deliberately in the Principio and DMPF entries: the statement that no product site was reachable, so the identification rests on the company name alone. That is a caveat about the world a reader can act on, not bookkeeping. Same pass: `## First moves` written for the first time, which the template requires of a record scoring 7 and which the sixth pass above did not add when it moved the score there. Four moves off receipts already on the record — the ministry's 2024 proceeding counts and its inaction complaints [S5], Principio's expiry monitoring and Deel as the only self-service tracking found [S4], Spring Walk and Workking on the agency side [S4,S7], and the state fee [S5]. The unpublished per-case price is stated as a move rather than hidden: it is already the honest limit in "Who pays". No new claim was introduced and no score moved.

2026-09-02 · plain-language pass — Seven terms glossed or replaced: employee card, kvóty, advokát, ARROWS [S2], DMPF and ARES, now the state business register [S4], HR as somebody in the company, and SMB in the build note. Argument tightened 413 → 323 words, every [Sn] marker, figure and named company kept. First moves rewritten in the plain house voice; a gist added to all seven sources. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` on who is stuck and what is happening, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Czech employers hiring foreign workers push zaměstnanecká karta applications through a notoriously slow paper process via manual relocation agencies and law firms". Previous solution, verbatim: "Software that files a Czech employee card — the work-and-residence permit for a foreign hire — end to end for the employer: documents, submission and status tracking, instead of a per-case agency fee." The record carried no brief and no good_for before this pass. Every claim was checked against this record's sources first. 82,000 is the sum of the interior ministry's 2024 counts, 14,287 new applications, 44,869 extensions and 22,793 employer or position changes, and about 68,000 of them are extensions and changes [S5]. The 3,518 inaction complaints, upheld in 40.6% of cases, are the ministry's figure for foreigners' proceedings, not shown to be employee cards alone, so the brief says "foreigners' cases" [S5]. "No Czech software tracks them" is the 2026-08-25 check with an in-domain positive control [S7]; the only self-service tracking found sits inside a foreign platform [S4]. The old title's "notoriously slow paper process" rests only on the harvest note behind [S1] and was not repeated. There is no dated trigger on this record, so the headline states the problem without one. No score, status, source, note, marker or body sentence changed. Simplified for the front page: title "Czechia handled 82,000 work-permit cases for foreign staff in 2024, and no Czech software tracks them" → "Czechia handled 82,000 work-permit cases in 2024, and no Czech software tracks them"; brief "About 68,000 were renewals and job changes, and the interior ministry got 3,518 complaints that foreigners' cases sat untouched, upholding 4 in 10 [S5]. Agencies and law firms do the paperwork by hand, case by case [S4,S7]." → "Agencies and law firms do each foreign worker's paperwork by hand, case by case [S4,S7]. The interior ministry got 3,518 complaints that foreigners' cases sat untouched [S5]."; solution "Build software for employers and their agencies that prepares work-permit files, tracks each case and warns before permits expire, as companies already do in Germany." → "Build software for employers and their agencies that prepares work-permit files, tracks each case and warns before permits expire.". The 68,000 renewals-and-changes figure and the 4-in-10 upheld rate were cut from the brief; "for foreign staff" left the headline; "as companies already do in Germany" was cut from the solution. Same date, pain-point pass: title "Czechia handled 82,000 work-permit cases in 2024, and no Czech software tracks them" → "Czech work permits for foreign staff get stuck, and agencies still do every file by hand"; brief "Agencies and law firms do each foreign worker's paperwork by hand, case by case [S4,S7]. The interior ministry got 3,518 complaints that foreigners' cases sat untouched [S5]." → "Every renewal or job change means a new file, prepared case by case [S5,S7]. The ministry got 3,518 complaints in 2024 that foreigners' cases sat untouched [S5].". Why: the owner asked of the old headline "Why is that a problem? I don't see the pain point there." — a volume and a missing product, no one hurting. The owner-approved card is applied. Markers checked: renewals (44,869 extension applications) and job changes (22,793 employer or position changes) are counted in the ministry's 2024 report [S5], and the case-by-case manual handling is the two Czech market scans [S4,S7], so the first sentence carries [S5,S7]. "Get stuck" rests on the same report's 3,518 complaints of inaction, upheld in 40.6% of cases [S5]; "every file by hand" on the scans that found only manual providers [S4,S7]. The approved draft said "last year", but those complaints are in the 2024 report and today is 2026-09-16, so the brief says "in 2024". The 82,000 figure stays in the body [S5]. No score, status, source, note or body sentence changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the employee card prepared by hand and holds the ministry's 2024 counts, now with the 12,843 cards granted from the same note, and the quota ceiling with Ukraine's 10% use and the India and Kazakhstan exception from its note [S5,S6]. Why now was the US startups' timing, which is not pain; it now opens on staff waiting and every renewal or job change needing a new file, with the 3,518 complaints, the renewal counts and the agency fees as its first items and the 2028 qualification law as dated detail, gaining the 365 regulated professions, the comment procedure and the Court of Justice ruling from its note [S2,S5,S7,S8]. The US timing, with the Y Combinator batches, moved to Validated abroad [S1,S3]. The unpublished fee, the state fee and the agencies as a second buyer moved under Willing to pay. Every comps[] and locals[] name left the body and the moves: each company is described by what it sells, and its name, year, funding, market count and named clients (N26, TravelPerk, Personio) stay in its ledger row. The move-only facts now have a home: the expiry watch sold as a service and Deel's tracking under Competition [S4], the practice of over fifty people under Willing to pay [S4], and the renewal counts under The opportunity [S5]. The moves lost every [Sn] marker and figure for links, move 1 now builds the deadline watch (the old move 2), and the old move 1 on renewals is move 2. `entry.why` was rewritten as "Easier: … Harder: …" with the same gates. S7's `why` said "this record"; it now says "an earlier search". A `process:` block was added, four steps, each from sources already cited: the agency or law firm preparing each file by hand [S4,S7], the interior ministry deciding, with complaints of cases left untouched [S5], how an employer follows its case marked unknown, and an agency watching expiry dates as a paid service [S4]; the record should join `PROCESS_PHRASE_ENFORCED` with the body gate. Corrected against the sources: the Who pays sectors "manufacturing, logistics, healthcare, IT" appear in neither [S2]'s note nor the signal behind [S1], so they were cut; the claim that one agency "takes the cases most rivals refuse" now says what its page says, that it also files cards for staffing-agency workers, which it calls uncommon among comparable firms (page read 2026-09-18) [S7]; and "somebody in the company is already tracking them on a spreadsheet" in the old move 1 had no source, so move 2 now says only that someone has to watch each renewal. Flagged, kept: "The state fee alone is 1,000 CZK at an embassy [S5]" is not in [S5]'s note, and "none of nine Czech agencies and law firms publishes a per-case fee [S4,S7]" rests on the 2026-08-25 research in commit 5bff299, not on either note; the one provider page re-read on 2026-09-18 publishes no price [S7], and both claims need a receipt. Flagged as inference: that employers are the ones paying the agencies' high fees [S2]; that agencies are a likely second buyer; that renewals are filed inside Czechia and that a deadline watch carries no legal risk (moves 1 and 2); that the real cost is the worker who cannot start on time (move 3); and that a national, paper-based procedure is a local builder's edge [S1,S2]. No score, status, source, `note:`, `sources[]` order, title, brief, solution or good_for changed.

2026-09-19 · state fee corrected, source added (owner-approved) — "The state fee alone is 1,000 CZK at an embassy [S5]" was flagged on 2026-09-18: [S5]'s note, the interior ministry's migration report, carries no fee. The official fee schedule was fetched on this date and added as [S9]: Act 634/2004 on administrative fees, in the version in force from 1 September 2026, consular item 162 c), charges 5,000 CZK to accept an application for an employee card at an embassy [S9]. So the figure was wrong as well as uncited, and the bullet now reads "The state's own fee is public: an embassy charges 5,000 CZK to accept each application [S9]." Item 162 d) charges 1,000 CZK to book the appointment to hand in a long-term or permanent residence application, which is probably where the old figure came from; it does not name the employee card, so it is recorded in [S9]'s note and not claimed in the body. [S9] is appended after [S8], so no marker moved; it backs no score. The bullet sits under "What the work costs is not public" and says the state fee is the exception. No score, status, note, other marker, headline field or other body sentence changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now stays 1 and Willing to pay stays 0, so `score` stays 7 and the band stays FAIR; what changed is the evidence under Why now. It was 1 as deadline 0 plus the freshness point, which is retired. It is now 1 on the education ministry's draft amendment to Act 18/2004, which from 1 January 2028 would add a second qualification file for hires into regulated professions: a dated duty reaching these employers, inside 18 months of this date, but a bill in comment procedure rather than enacted law, so it fails REAL and stops at rung 1 [S8]. [S8] was tagged `dims: []` with a note saying 2028 is beyond the 18-month window; it is not, so the note now says so and the source is tagged `dims: [urgency]`. The employee-card quota decree [S6] had backed Why now by its type alone; it caps what the state accepts and puts no dated duty on employers, so it is now `dims: []`. Tagging pass for Willing to pay: no source on file shows anyone paying for this job with an amount. The agencies and law firms sell the work by hand but publish no fee [S2,S4,S7], and the 5,000 CZK embassy fee is a state charge for the application, not the preparation work [S9]. No receipt added; money stays 0, as the worksheet had it. `[Competition](#competition)` became `[Market gap](#competition)` in moves 1 and 4. Why now and Willing to pay prose re-read against the numbers and left as written: Why now already calls the 2028 law a draft, and Willing to pay already says no provider publishes its fee. No other score, status, entry or body sentence changed.
