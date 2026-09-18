---
id: p-0018
region: cz
title: 'Czech employers with 150+ staff would have to redesign how they set pay under a new law'
brief: 'Czechia is already late on the EU rules, and its draft goes further: pay ranges in every job ad and a first pay-gap report due April 2028 [S1].'
solution: 'Build software that reads a company''s payroll export and produces the pay-gap report the draft law would require.'
good_for: 'Someone who knows HR and payroll and can sell to larger employers.'
draft_law: 'Czech pay transparency law, still a draft [S1]'
category: legal-compliance
geo: CZ-national
score: 6
scores:
  proof: 3
  money: 0
  urgency: 3
  demand: 0
  gap: 0
status: watching
entry:
  level: moderate
  buyer: large-firms
  permission: none
  incumbents: direct
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed, the product reads an ordinary payroll export, and it can start without outside money. Harder: the law is still a draft; the buyers are employers with 150 or more staff, so each sale goes through a personnel department; and two established Czech sellers already sell pay-gap analysis.'
comps:
- name: Figures
  url: https://figures.hr/
  geo: FR
  since: 2020
  traction: '€6.67M led by Point Nine (EU-Startups, 2022); benchmarks from 1,200+ EU companies;
    compliance tier from €2,500/yr'
- name: PayAnalytics
  url: https://www.payanalytics.com/
  geo: IS
  since: 2016
  traction: 'acquired by beqom (PRNewswire, Dec 2023); used in 75+ countries; pay decisions
    covering 1.5M+ employees'
- name: Syndio
  url: https://synd.io/
  geo: US
  since: 2017
  traction: '$83M raised incl. $50M Series C (PRNewswire, 2021); 200+ enterprise customers
    incl. 10% of the Fortune 200'
locals:
- name: Sloneek
  url: https://sloneek.com/
  ico: '08684332'
  since: 2019
  competes: direct
  maturity: established
  evidence: 'Its HR system markets pay-band creation and management, automated data collection
    for reporting, and analysis of pay differences by gender or role. Sloneek s.r.o. has traded
    since 2019 and raised a $6M Series A in June 2026 from Orbit Capital and the Venture to
    Future Fund.'
- name: TREXIMA (Manažer odměňování)
  url: https://www.manazerodmenovani.cz/
  ico: '44004508'
  since: 1991
  competes: direct
  maturity: established
  evidence: 'Used by the labour ministry, which has it run the state ISPV earnings survey — the
    same benchmark data it sells back to employers as Manažer odměňování: analytical job
    evaluation, twice-yearly wage benchmarking, an explicit Gender Pay Gap report and a
    pay-system analysis module, at 79,000 CZK a year on a three-year fixed price. TREXIMA,
    spol. s r.o. has traded since November 1991; its own client panel is empty and it holds no
    public contract in the state contracts register, and the product stops short of the
    directive''s prescribed filing — quartile bands, mean and median gaps on variable pay, the
    joint assessment.'
- name: Nakladatelství FORUM (Spolehlivé řízení rovného odměňování)
  url: https://forum-media.cz/
  ico: '27180271'
  since: 2026
  competes: direct
  maturity: early
  evidence: 'A web application at 8,499 CZK a year before VAT that groups employees by job value,
    applies a catalogue of justified pay criteria, tracks the male-female pay ratio, generates
    the mandatory employee pay disclosure and produces audit-ready reports. Nakladatelství
    FORUM s.r.o. has traded since 2004, but this product launched in 2026, sold explicitly
    against Czech pay rules taking effect on 1 January 2027.'
sources:
- type: regulation
  name: "Czech transposition of the Pay Transparency Directive"
  gist: "the 2027 law and 2028 reports"
  why: "Law-firm analysis of the MPSV draft: effective 1 Jan 2027, most duties from 1 Jan 2028, and pay-gap reports for employers with 150+ staff first due 30 April 2028. Czechia missed the June 2026 transposition deadline."
  url: https://iuslaboris.com/insights/czechia-charts-its-own-course-on-pay-transparency-directive-transposition/
  note: 'reg-pay-transparency-cz: EU Pay Transparency Directive (2023/970); CZ missed the
    7 Jun 2026 transposition deadline (infringement exposure). MPSV draft law (26 Mar 2026)
    sets effectiveness 1 Jan 2027, most obligations 1 Jan 2028, pay-gap reporting for 150+
    employee employers with first reports due 30 Apr 2028. Deadline <18 months.'
  date: '2027-01-01'
  signal: reg-pay-transparency-cz
- type: arbitrage
  name: "Figures"
  gist: "the €6.67M French template"
  why: "French compensation-benchmarking and EU pay-transparency tooling sold across Europe — with PayAnalytics and Syndio, the template for what this product looks like when it works."
  url: https://figures.hr/
  note: Figures (FR) sells compensation-benchmarking and EU pay-transparency compliance tooling
    across Europe; PayAnalytics (IS) and Syndio (US) prove the pay-equity analytics category.
    Named analogs only — no CZ gap check run this cycle, so arbitrage scored 1 and gap 0.
  date: '2026-08-13'
- type: news
  name: "Vema and Pamica — the installed Czech payroll base"
  gist: "the installed payroll base"
  why: "Names the legacy payroll systems Czech employers actually run on. It records that they exist; it says nothing about whether they analyse pay gaps."
  url: https://www.ycombinator.com/companies/hammr
  note: 'yc-hammr: the CZ absence check inside this signal names the installed Czech payroll
    base — "generic legacy payroll (Vema, Pamica)". Appended by the 2026-08-20 evidence audit
    as the receipt that Vema exists as a Czech payroll system; it says nothing about what Vema
    analyzes. Existence receipt only, backs no score dimension.'
  date: '2026-08-13'
  signal: yc-hammr
  dims: []
- type: news
  name: "TED — OKbase HR system support"
  gist: "the ministry's OKbase award"
  why: "A Foreign Ministry award for support of the Czech OKbase HR system — a receipt that it is in production use here, and nothing more."
  url: https://ted.europa.eu/en/notice/-/detail/474940-2026
  note: 'ted-474940-2026: Ministry of Foreign Affairs award for "OKbase HR system support"
    (Jul 2026). Appended by the 2026-08-20 evidence audit as the receipt that OKbase exists
    as a Czech HR system in production use; it says nothing about pay-equity analysis. Existence
    receipt only, backs no score dimension.'
  date: '2026-07-09'
  signal: ted-474940-2026
  dims: []
- type: gap-check
  name: "Czech pay-equity tooling scan"
  gist: "the Czech pay-equity sweep"
  why: "Czech pay-equity products already exist: TREXIMA's Manažer odměňování at 79,000 CZK a year with a gender pay-gap report, Nakladatelství FORUM's equal-pay app at 8,499 CZK a year, and the labour ministry's free Logib audit."
  url: https://www.manazerodmenovani.cz/
  note: 'Czech-language pay-equity scan 2026-08-25. The Czech position is NOT open. Commercial
    products found: TREXIMA, spol. s r.o. (IČO 44004508, tř. Tomáše Bati 299, Louky, Zlín)
    sells Manažer odměňování on its HR DRIVE platform (manazerodmenovani.cz, hrdrive.eu) —
    analytical job evaluation, job descriptions, employee-quality assessment, twice-yearly wage
    benchmarking, an explicit Gender Pay Gap report and an Analýza systému odměňování (rovnost
    a transparentnost) module; 79,000 CZK a year on a three-year fixed price, or 55,000 CZK for
    benchmarking alone, with the unadjusted Gender Pay Gap in the standard outputs; TREXIMA
    also runs the state ISPV earnings survey for MPSV, so it holds the reference data as well
    as the tool. Nakladatelství FORUM s.r.o. (IČO 27180271, Střelničná 1861/8a, Praha 8) sells
    Spolehlivé řízení rovného odměňování, a web application at 8,499 CZK a year ex-VAT that
    groups employees by job value, applies a catalogue of justified pay criteria, tracks the
    male-female pay ratio, generates the mandatory employee pay disclosure and produces
    audit-ready reports — sold explicitly against the Czech rules taking effect 1 January 2027.
    Sloneek s.r.o. (IČO 08684332, Praha 8) markets pay-band creation and management, automated
    data collection for reporting, and analysis of pay differences by gender or role inside its
    HRIS. State side: MPSV with the labour inspectorate (SÚIP) runs the Rovná odměna programme
    (rovnaodmena.cz), distributing the Swiss Logib self-audit tool free to private and public
    employers (20+ employers tested), plus a wage calculator over ISPV data and a ROVNÁ ODMĚNA
    certification; SÚIP uses Logib in its own inspections, so the free tool is also the
    enforcement instrument — a competitor priced at zero. Consultancy-only alongside: Deloitte,
    PwC, EY, RSM, Aprofes. WHAT IS GENUINELY NOT FOUND: a Czech product that takes a payroll
    export and returns the directive''s prescribed report as a finished filing — quartile pay
    bands, mean and median gaps on variable components, the joint pay assessment. That is a
    narrower opening than an empty market, and not-finding it is not evidence it does not
    exist. POSITIVE CONTROL: the same Czech-search method run at Vema, the payroll vendor
    already on file at S3, surfaced Vema Mzdy alongside KS program, OKbase, plusPortal, Pinya
    HR, RON, KARAT, DUNA and PREMIER in a Czech software catalogue — control PASSED.
    Register-internal disproof worth recording: data/register.db already held round-sloneek
    (2026-06-30), whose own note names EU pay-transparency transposition as the demand driver
    for Czech HRIS vendors — the register carried a Czech entrant while the body said the Czech
    market had not been searched. TREXIMA and Nakladatelství FORUM return ZERO hits across all
    11,330 signals, the corpus blindness CONVENTIONS predicts. Surfaces: Czech web search
    (queries below), ARES for legal identity and IČO, Czech software catalogues
    (ekonomickysoftware.com, sloneek HRIS comparison), and the funded ledger via register.db.
    gap was already 0 and stays 0; status moves to watching under the SPEC §4 de-rank rule on
    the named Czech incumbents.'
  date: '2026-08-25'
  queries:
    - "software analýza rozdílů v odměňování žen a mužů reporting směrnice o transparentnosti odměňování české řešení"
    - "nástroj pro reporting gender pay gap zaměstnavatel 150 zaměstnanců transparentnost odměňování 2027 příprava HR software"
    - '"transparentnost odměňování" software nástroj pro zaměstnavatele analýza mzdové struktury práce stejné hodnoty česká firma'
    - "Sloneek Vema Elanor OKbase modul rovné odměňování pay gap report mzdová analytika směrnice 2023/970"
    - "česká aplikace pro výpočet rozdílu v odměňování žen a mužů report pro zaměstnavatele mzdový audit rovnost startup"
    - "katalog českého software HR systémy odměňování srovnání vybersoftware přehled dodavatelů personalistika"
    - "český mzdový a personální software pro zpracování mezd firmy dodavatel systém"
  checked: [google-cz, ares, cz-saas-directories, own-funded-ledger]
  expires: '2026-11-23'
- type: regulation
  name: "VeKLEP — unified monthly employer reporting rules amended"
  gist: "the second reporting regime"
  why: "A second reporting regime is landing on the same payroll data: the decree implementing unified monthly employer reporting (417/2025 Sb.) is already being amended, with comments closed in July 2026."
  url: https://odok.cz/portal/veklep/material/KORNDWGLMTLV/
  note: 'veklep-KORNDWGLMTLV: draft regulation amending nařízení č. 417/2025 Sb., which
    implements the jednotné měsíční hlášení zaměstnavatele law; public comments closed
    Jul 2026 (first VeKLEP harvest, 2026-08-25). A DIFFERENT obligation from pay transparency
    — linked as context only: both regimes pull structured reporting out of the same Czech
    payroll systems this record''s buyers run. Backs no score dimension.'
  date: '2026-07-30'
  signal: veklep-KORNDWGLMTLV
  dims: []
- type: price
  url: https://www.manazerodmenovani.cz/
  name: "TREXIMA Manažer odměňování"
  gist: "79,000 CZK a year"
  why: "A Czech employer pays 79,000 CZK a year for the pay-analysis tool with a gender pay-gap report, or 55,000 CZK a year for the wage benchmarking alone."
  note: 'Price receipt lifted from the 2026-08-25 Czech pay-equity scan already on this ledger,
    which read manazerodmenovani.cz: 79,000 CZK a year on a three-year fixed price, or 55,000
    CZK for benchmarking alone. Annual is stated, so the unit is per-year. Nakladatelství
    FORUM at 8,499 CZK a year sits in the same note but its own url is not on this record, so
    it is not written as a receipt here. dims omitted: backs no score.
    Verified 2026-09-04: manazerodmenovani.cz still prints 79 000 Kč as the Základní roční
    cena, though the three-year fixed term and the 55,000 CZK benchmarking-only figure are
    no longer stated on the page.'
  date: '2026-08-25'
  payer: 'A Czech employer of 150 or more staff'
  amount_czk: 79000
  unit: per-year
  basis: list-price
created: '2026-08-13'
updated: '2026-09-04'
---

A draft Czech law would make every employer set pay by a written system, and larger ones report their gender pay gap [S1].

- Every employer would need a written pay system grouping jobs by their value [S1].
- Firms with 150 or more staff would report their gender pay gap [S1].
- Job applicants would be told the minimum pay before they are hired [S1].

The law would put the EU's Pay Transparency Directive (2023/970) into Czech law [S1]. That directive makes pay open, so that women and men get equal pay for work of equal value [S1]. The labour ministry's draft dates from 26 March 2026 [S1].

- Jobs would be grouped by how complex, responsible and demanding the work is [S1].
- Every employer would also need a written system for money benefits beyond pay [S1].
- Employers could not rely on a job applicant's current or past pay [S1].
- Telling applicants the minimum pay is narrower than the EU's rule, which asks for the starting pay or its range [S1].
- Firms with 250 or more staff would report every year, and those with 100 to 249 every three years [S1].
- Where a gap of 5% or more cannot be explained, the employer would run a joint pay assessment with staff representatives [S1].
- No Czech employer survey, business-chamber statement or complaint about pay-gap reporting has been found; the evidence is the draft law and its dates [S1].

Existing non-solutions: The Czech field is taken: two established sellers offer pay-gap analysis, a third is new, and the state gives an audit tool away [S5].

- The firm that runs the state earnings survey sells a gender pay-gap report [S5].
- A personnel-software firm markets pay bands and gender pay analysis [S5].
- A publisher sells a web app built for the new Czech equal-pay rules [S5].

The survey firm also sells job evaluation and wage benchmarks, drawn from the same survey data [S5]. The publisher's app groups staff by the value of their work and tracks the pay ratio between women and men [S5].

- The labour ministry and its labour inspectorate give Logib, a Swiss self-audit tool, to employers for free, and inspectors use it in their own checks [S5].
- Employers already run Czech payroll and personnel systems such as Vema, Pamica and OKbase; the sources say nothing about whether these analyse pay gaps [S3,S4].
- No Czech product was found that turns a payroll export into the finished filing the EU rules prescribe: the share of women and men in each quarter of the pay scale, mean and median gaps on variable pay, and the joint assessment [S5]. Not finding one does not prove none exists [S5].

Why now: Employers would have to rebuild how they set pay from January 2027, and firms with 150+ staff file a first report by April 2028 [S1].

- Personnel teams would sort every job into groups by its value [S1].
- Lacking a written pay system could cost an employer up to CZK 1M [S1].
- Firms that wait for the final law get only months before it starts [S1].

The draft goes further than the EU directive, so employers would rebuild how they set pay, not just document it [S1]:

- The written pay system, the benefits system and the grouping of jobs are Czech additions; the directive asks for none of them [S1].
- Lesser breaches, such as limiting what staff may learn about pay, could cost up to CZK 400,000 [S1].

The dates come from the draft, and a second reporting change lands on the same payroll data [S1,S6]:

- On 7 June 2026 Czechia missed the EU's deadline to put the directive into Czech law [S1].
- On 1 January 2027 the law would take effect, with the pay system, the minimum pay for applicants and the ban on relying on past pay [S1].
- On 1 January 2028 most other duties would start, including the pay-gap reports and the joint assessments [S1].
- By 30 April 2028 firms with 150 or more staff would file their first pay-gap report [S1].
- By 30 April 2031 firms with 100 to 149 staff would file theirs [S1].
- In July 2026 public comments closed on changes to decree 417/2025, which sets the rules for the employer's single monthly report to the state [S6]. It is a different duty, drawn from the same payroll systems [S6].

Who pays: Czech tools sell at a list price, but no Czech employer is yet shown paying for pay-gap reporting [S5].

- Two Czech tools sell pay-gap analysis at a published yearly price [S5].
- Investors backed a Czech personnel-software firm that markets pay-gap analysis, in June 2026 [S5].
- Five consultancies offer pay-equity work as paid advice [S5].

The buyers would be employers with 150 or more staff first, then every employer that hires, since all would need the written pay system [S1]. A seller can come in two ways: a standalone audit tool, or a module inside the payroll systems employers already run [S3,S4]. Whether employers buy before 30 April 2028 or scramble after is the open question [S1].

Solved elsewhere: Three foreign firms, in France, Iceland and the US, already sell the pay analysis these rules would force on Czech employers [S2].

- The French firm sells pay benchmarks and EU pay-transparency tools across Europe [S2].
- The Icelandic and US firms sell pay-equity analytics [S2].

## Revisions


2026-08-25 · rewrite, then market check (one entry per date, so the two merge) — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Later the same day, the market check — the Czech market was searched in Czech for the first time and it is not open: TREXIMA sells Manažer odměňování at 79,000 CZK a year with a gender pay-gap report and analytical job evaluation, Nakladatelství FORUM sells an equal-pay web app at 8,499 CZK a year, Sloneek markets pay bands and gender pay analysis in its HR system, and MPSV with the labour inspectorate gives the Logib audit away free while inspecting with it [S5]. `scores.gap` was already 0 and stays 0 — a search cannot raise it — but `status` moves candidate → watching under the SPEC §4 de-rank rule, and the two paragraphs that asserted the Czech market had not been searched have been rewritten to what was found. `score` is unchanged at 4. Two method notes for the next check. First, the register already held its own disproof: `round-sloneek` (2026-06-30) sits in the corpus naming EU pay-transparency transposition as the demand driver for Czech HR vendors, while the body said nobody had looked. Second, TREXIMA and Nakladatelství FORUM return zero hits across all 11,330 signals — neither raised, neither sells through public tender — so only Czech-language search could find them. Positive control: the same method run at Vema surfaced it alongside eight other Czech payroll vendors, so the method works here. Third pass this date, merged here: the first VeKLEP harvest added the amendment of the unified-monthly-employer-reporting decree (417/2025 Sb.) as a context receipt [S6] — a different obligation pulling structured reporting out of the same payroll systems. No score moved. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries Sloneek, TREXIMA and Nakladatelství FORUM [S5]. Sloneek passes the established test on its June 2026 Series A and seven years of trading, so `scores.gap` stays 0 and the de-rank above holds on a machine-checkable receipt. TREXIMA is recorded as early, and the reason is a receipt gap rather than a judgment about the company: TREXIMA, spol. s r.o. has traded since 1991 and plainly is not an early business, but its own 'Naši klienti' panel is empty, there is no public contract for IČO 44004508 in cz-contract-parties.jsonl, no round and no certification — so no limb of the test is citable, and the ledger records what can be proved. Nakladatelství FORUM is early because the product is new even though the publisher is not: it is sold explicitly against rules taking effect on 1 January 2027. The free MPSV/SÚIP Logib tool is not in `locals[]` — it is a state programme rather than a vendor — and stays named in the body. `scores.proof` 1 → 3: PayAnalytics (Iceland, and therefore Nordic and CEE-adjacent under SCORING.md) and Syndio (US) both pass the established test in two markets, while Figures cites no limb the test reads. `score` 4 → 6. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and **TREXIMA is re-examined and moves from early to established**. The pass above recorded it as early and said plainly that this was a receipt gap rather than a judgment about a 35-year-old company; re-run honestly under the split, the test passes on both limbs. First limb: TREXIMA, spol. s r.o. is ARES-dated 19 November 1991, so ">= 3 years selling" is met many times over. Second limb, named customers: TREXIMA runs the state ISPV earnings survey for the labour ministry [S5] — MPSV is a named public customer, and the benchmark data that survey produces is the same data Manažer odměňování sells back to employers. Which limbs it still fails is worth stating, because "established" is a test and not a compliment: its own 'Naši klienti' panel is empty, cz-contract-parties.jsonl carries no contract for IČO 44004508, and there is no round at any stage. One citable limb is what the test asks for and the ISPV mandate is it. `competes: direct`: analytical job evaluation, twice-yearly wage benchmarking and an explicit Gender Pay Gap report are sold to Czech employers, which is this record's product and this record's buyer — and the fact that it stops short of the directive's prescribed filing is a feature gap inside the same product, not a different segment. Sloneek and Nakladatelství FORUM convert to `competes: direct` with maturities unchanged. `scores.gap` stays 0 and `score` stays 6: the field was already taken on Sloneek, and TREXIMA now confirms it on a second, independent receipt rather than moving the number. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also reworded in the Nakladatelství FORUM entry: "cannot have been on sale for three years" is a rubric sentence, and the fact behind it is simply that the product launched in 2026.
2026-08-20 · evidence audit — Three unbacked claims removed from "Existing non-solutions", plus one from the title. The capability claim that Czech payroll systems "record pay but do not analyze equal-value job categories or gaps" has nothing behind it: no signal or note characterises what Vema or OKbase do. Their existence is receipted, so it stays, now cited to two sources appended for the purpose [S3,S4]. "Big-four consultancies will serve enterprise" and "the mid-market has nothing local" are both gone — no big-four claim exists anywhere in the corpus, and the absence claim contradicted this record's own note that no CZ gap check was run. The title carried the same absence, "— with no local tooling", and has been rewritten to the regulatory facts, which are receipted [S1].
2026-09-02 · plain-language pass — Three trade terms cleared at first use: HR and HRIS replaced with plain words, Nakladatelství FORUM glossed as a publisher. Argument cut from 435 to 342 words, every figure, date, price, named company and [Sn] marker kept. A gist added to all six sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The price already read in the 2026-08-25 sweep is now recorded as a price of its own: 79,000 CZK a year, or 55,000 for benchmarking alone [S7]. The 8,499 CZK rival stays in the note, its own page not being on this ledger. No score, status, note or marker touched.

2026-09-10 · likely solution — Added the one-sentence `solution:`, now required on every record and always shown as the likely solution, compressed from build.note, the existing non-solutions paragraph, locals[] and the solved-elsewhere paragraph. No claim, score or source changed.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as three lines under the headline: a `brief:` on who is stuck and what forces it now, the `solution:` as a call to action starting "Build", and a new `good_for:` line. Previous title, verbatim: "Czech employers must report their gender pay gap from 2027". Previous solution, verbatim: "Software that reads an employer's payroll export, groups staff by the value of their work, and returns the pay-gap report the new law would require of employers with 150 or more staff, ready to file." There was no previous brief or good_for. Checked against the sources before writing: the old headline said employers report "from 2027", but the draft puts the first pay-gap reports at 30 April 2028 and only for employers with 150 or more staff; what 1 January 2027 carries is the law's planned start [S1]. Because the law is a draft, the headline and brief say "would", and "planned for January" is the draft's own date, not a passed law [S1]. The job-ad pay ranges are stated without a start date, because the source puts the law's start in 2027 but most duties in 2028 and does not say which of the two the job-ad rule falls under [S1]. "As companies already do abroad" rests on Figures, PayAnalytics and Syndio [S2]. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Title before: "Czech employers with 150+ staff would have to report their gender pay gap. The draft law is planned to start in January." After: "Czech employers with 150+ staff would have to report their gender pay gap. The draft law is planned for January." Brief before: "Czechia missed the EU's June 2026 deadline to adopt these rules [S1]. Under the draft, every employer would show pay ranges in job ads, and those with 150 or more staff would file a first pay-gap report by 30 April 2028 [S1]." After: "Czechia is already late on these EU rules [S1]. Under the draft, every employer would put pay ranges in job ads, and the first pay-gap reports would be due in April 2028 [S1]." Solution before: "Build software that reads a company's payroll export and produces the pay-gap report the draft law would require, ready to file, as companies already do abroad." After: "Build software that reads a company's payroll export and produces the pay-gap report the draft law would require." Good for before: "Someone who'd like to work with payroll and HR teams at larger companies." After: "Someone who'd like to work with HR and payroll teams." "Missed the EU's June 2026 deadline" became "already late" [S1]; the report date keeps its month and year [S1]; "would" and "draft" stay because the law is not passed. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed. Same date, owner-approved card: title "Czech employers with 150+ staff would have to report their gender pay gap. The draft law is planned for January." became "Czech employers with 150+ staff would have to redesign how they set pay under a new law"; brief "Czechia is already late on these EU rules [S1]. Under the draft, every employer would put pay ranges in job ads, and the first pay-gap reports would be due in April 2028 [S1]." became "Czechia is already late on the EU rules, and its draft goes further: pay ranges in every job ad and a first pay-gap report due April 2028 [S1]."; good_for "Someone who'd like to work with HR and payroll teams." became "Someone who knows HR and payroll and can sell to larger employers.". "Redesign how they set pay" rests on the draft mandating pay-system design, beyond the directive [S1]; the law is still a draft, so every duty is "would". Same date, draft law: added `draft_law:` for the "Draft law" badge. The record's pain — pay-system redesign, pay ranges in job ads, the pay-gap report — exists only in the labour ministry's draft transposing the EU pay transparency directive, which Czechia has not yet passed [S1]. Status re-checked on 2026-09-16: the government approved the bill on 31 August 2026 and it still has to pass parliament (mpsv.gov.cz, "Vláda schválila větší transparentnost odměňování"). No other field changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence and its three most important items, with the rest below as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the written pay system and the pay-gap report, with the directive, the draft's date, the job-grouping criteria, the benefits system, the past-pay ban, the reporting frequency, the joint assessment and the missing demand evidence below [S1]. Competition names no ledger company: the survey firm, the personnel-software firm and the publisher are described by what each sells, and their prices, years, funding and product names stay in their `locals[]` rows and the price receipt [S5,S7]; the free state audit tool, the installed payroll systems and the missing finished filing stay in the detail [S3,S4,S5]. Why now opens on the January 2027 and April 2028 cut-offs, then three pain items (sorting every job into groups, the fine, the months left), then what the draft adds beyond the directive and the dates as plain bullets [S1,S6]. Willing to pay says whether anyone pays: tools sell at a list price and no employer is yet shown paying; the buyers, the two ways in and the open question stay below [S1,S3,S4,S5]. Validated abroad names none of the three foreign firms; their funding, customer counts and acquisition stay in their `comps[]` rows. `entry.why` is now "Easier: … Harder: …" with the same gates (a larger-firm buyer, no licence, ordinary software, no outside money) plus the draft status and the two established sellers, whose names left it for their ledger rows. Added from S1's article, read at its URL on 2026-09-18 because its note carries only the dates: fines of up to CZK 1M and CZK 400,000, the Czech additions beyond the directive (a written pay system and a benefits system for every employer, jobs grouped by complexity, responsibility and how demanding the work is), the ban on relying on past pay, yearly and three-yearly reporting, the 2031 threshold for 100–149 staff, and the 5% joint-assessment trigger [S1]. Added from sources already on file: the second reporting change on the same payroll data [S6], Pamica beside Vema [S3], and the five consultancies [S5]. Corrected against the sources rather than the old sentences: "pay ranges in job ads" became the minimum pay, because the Czech draft asks only for the minimum pay, narrower than the directive's range [S1]; "published pay criteria" became a written pay system grouping jobs by value, which is what the draft requires [S1]; "thousands of Czech firms whose personnel departments have never run a pay-equity analysis" lost both claims, because S1 counts no employers and no source says what they have run [S1]; "a year of that work compresses into months" lost "a year", which no source sizes [S1]; "Nobody sells the finished filing" became "No Czech product was found", with the scan's own caveat [S5]; "none sells it here" was cut, because the French firm sells across Europe and no source says it skips Czechia [S2]; "Vema and OKbase are the installed payroll base" now names the three systems the sources list and says what they do not show [S3,S4]. The 2026-09-16 entry said S1 does not say which date the job-ad rule falls under; its article puts the applicant duties, the pay system and the benefits system at 1 January 2027 [S1]. Flagged, not changed: the owner-approved brief says "pay ranges in every job ad", but S1's article says the Czech draft requires only the minimum pay, so the brief needs the owner's call [S1]. Flagged as inference: "Firms that wait for the final law get only months before it starts" rests on the law still being a draft and its 1 January 2027 start [S1]; "rebuild how they set pay, not just document it" is our reading of the Czech additions [S1]; the two ways in (a standalone tool, or a payroll module) are our reading of the installed systems [S3,S4]. No `process` block added: the pay-gap report is a new duty, and no source on file describes how an employer's personnel team handles pay today. No score, status, `entry` gate value, `sources[]` order, `note:`, title, brief, solution, good_for or draft_law changed.
