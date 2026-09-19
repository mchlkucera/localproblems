---
id: p-0018
region: cz
title: 'Czech employers with 150+ staff would have to redesign how they set pay under a new law'
brief: 'Czechia is late on the EU rules, and its draft would make every employer set pay by a written system [S1]. Applicants would learn the minimum pay, and firms with 150+ staff would report their pay gap by April 2028 [S1].'
solution: 'Build software that reads a company''s payroll export and produces the pay-gap report the draft law would require.'
good_for: 'Someone who knows HR and payroll and can sell to larger employers.'
draft_law: 'Czech pay transparency law, still a draft [S1]'
category: legal-compliance
geo: CZ-national
score: 6
scores:
  proof: 3
  money: 2
  urgency: 1
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
    same benchmark data it sells back to employers as Manažer odměňování: job descriptions,
    analytical job evaluation and twice-yearly wage benchmarking at 79,000 CZK a year on a
    three-year fixed price, which in August 2026 also listed an explicit Gender Pay Gap report
    and a pay-system analysis module. Its own client panel is empty, but Česká pošta, a city
    heating company and a public university sign for the tool in the state contracts register,
    and a city bus company paid it in December 2025 for a pay-system audit that included the
    adjusted gender pay gap. TREXIMA, spol. s r.o. has traded since November 1991, and the
    product stops short of the directive''s prescribed filing — quartile bands, mean and median
    gaps on variable pay, the joint assessment.'
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
- name: Greenometer
  url: https://www.greenometer.com/cs/gender-pay-gap
  ico: '07638990'
  since: 2026
  competes: direct
  maturity: early
  evidence: 'Sells pay-gap analysis together with its own Gender Pay Gap software module: from an
    employer''s payroll data it computes the mean, median and adjusted gap, splits base pay from
    bonuses and flags groups of work more than 5% apart. Charles University, the Technical
    University of Liberec, Prague''s city library, a hospital company and a water utility signed
    for it in the state contracts register in 2026. Greenometer s.r.o. has sold carbon-footprint
    and sustainability reporting to public buyers since 2024; its first pay-gap contract on
    file dates from January 2026.'
sources:
- type: regulation
  name: "Czech transposition of the Pay Transparency Directive"
  gist: "the 2027 law and 2028 reports"
  why: "Law-firm analysis of the MPSV draft: effective 1 Jan 2027, most duties from 1 Jan 2028, and pay-gap reports for employers with 150+ staff first due 30 April 2028. Czechia missed the June 2026 transposition deadline."
  url: https://iuslaboris.com/insights/czechia-charts-its-own-course-on-pay-transparency-directive-transposition/
  note: 'reg-pay-transparency-cz: EU Pay Transparency Directive (2023/970); CZ missed the
    7 Jun 2026 transposition deadline (infringement exposure). MPSV draft law (26 Mar 2026)
    sets effectiveness 1 Jan 2027, most obligations 1 Jan 2028, pay-gap reporting for 150+
    employee employers with first reports due 30 Apr 2028. Deadline <18 months. Rescored
    2026-09-19: the Czech law is still a bill (government-approved 31 Aug 2026, before
    parliament) and the directive is untransposed, so it fails REAL and backs Why now 1, not
    the deadline point it carried under v1.'
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
  why: "Czech pay-equity products already exist: TREXIMA's job-grading and wage-benchmarking tool at 79,000 CZK a year, which listed a gender pay-gap report, Nakladatelství FORUM's equal-pay app at 8,499 CZK a year, and the labour ministry's free Logib audit."
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
    the named Czech incumbents.
    Corrected 2026-09-19, Willing to pay search: this sweep missed a Czech seller with paying
    customers, Greenometer s.r.o. (IČO 07638990), which since January 2026 computes mean,
    median and adjusted pay gaps and flags groups more than 5 % apart for public employers, with
    its own Gender Pay Gap software module (S11); it is now in locals[] as direct and early.
    TREXIMA holds public contracts after all: Manažer odměňování licences (Česká pošta,
    Teplárny Brno, Univerzita Pardubice and others) and a Logib-based pay audit for Dopravní
    podnik města Jihlavy (S11). The paid 79,000 CZK set covers job descriptions, analytical job
    evaluation and employee-quality assessment, with benchmarking free as a pilot, and the
    price page read 2026-09-19 names no Gender Pay Gap report. Still not found in any contract
    text read: quartile pay bands and the joint pay assessment.'
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
  why: "A Czech employer pays 79,000 CZK a year for a tool that describes and grades jobs and benchmarks wages against the market; the price page names no pay-gap report."
  note: 'Price receipt lifted from the 2026-08-25 Czech pay-equity scan already on this ledger,
    which read manazerodmenovani.cz: 79,000 CZK a year on a three-year fixed price, or 55,000
    CZK for benchmarking alone. Annual is stated, so the unit is per-year. Nakladatelství
    FORUM at 8,499 CZK a year sits in the same note but its own url is not on this record, so
    it is not written as a receipt here. dims omitted: backs no score. Tagged dims: [money] on
    2026-09-19: an asking price for this job, since the ledger lists TREXIMA as a direct
    seller of pay-gap analysis to these employers, even though the tool stops short of the
    directive''s prescribed filing.
    Verified 2026-09-04: manazerodmenovani.cz still prints 79 000 Kč as the Základní roční
    cena, though the three-year fixed term and the 55,000 CZK benchmarking-only figure are
    no longer stated on the page.
    Corrected 2026-09-19, Willing to pay search: untagged, dims: []. The contracts answer the
    rescore worksheet''s call 9. Česká pošta (registr smluv 38281696, 1 June 2026) and
    Univerzita Pardubice (39357657, 1 September 2026) pay 79,000 CZK excl. VAT a licence year,
    and Pardubice''s clause reads "Cena balíčku Manažer odměňování ve výši 79 000 bez DPH za
    každý licenční rok se vztahuje výhradně na moduly Popisy pracovních pozic, Analytické
    hodnocení prací a Hodnocení kvality zaměstnanců"; the Mzdový benchmarking module is given
    free under an OP TAK proof-of-concept pilot (S11). The page read on this date lists job
    descriptions, job evaluation, employee-quality assessment, wage benchmarking twice a year
    and consultations under 79 000 Kč, a three-year contract at a fixed price, and names no
    gender pay-gap report. The price buys job grading and market benchmarking, the written pay
    system the draft also requires, not the pay-gap report in `solution:`. It stays on file as
    what that next-door job costs. Money rests on S8 and S9.'
  date: '2026-08-25'
  payer: 'A Czech employer of 150 or more staff'
  amount_czk: 79000
  unit: per-year
  basis: list-price
  dims: []
- type: price
  url: https://smlouvy.gov.cz/smlouva/38233433
  name: "Univerzita Karlova — a pay-gap analysis of the whole university, June 2026"
  gist: "a university's pay-gap analysis"
  why: "What a large Czech university paid a specialist firm to calculate its gender pay gap from payroll data, including the gap in bonuses and the groups of work more than 5% apart."
  note: 'Registr smluv 38233433 (idSmlouvy 35917849, č.j. UKRUK/380461/2026-1, UKRUKS/0309/2026),
    concluded 2 June 2026, published the same day: Univerzita Karlova, Rektorát (IČO 00216208) and
    Greenometer s.r.o. (IČO 07638990), "Smlouva o dílo, provedení analýzy rozdílů v odměňování
    žen a mužů na UK". Article I, Phase 1: "Analýzu rozdílů v odměňování žen a mužů na UK (Gender
    Pay Gap, dále jen „GPG“) mzdových dat a jejich interpretaci přes celou UK, odhadem 13 tis.
    položek", with outputs "neočištěný GPG za celou UK – průměr i medián", an adjusted GPG by
    regression, "rozklad rozdílu na základní mzdu vs. variabilní složku", "identifikace skupin
    prací nad zákonnou hranicí 5 %" and an interpretation of the risks. Phase 2: advice on
    categories of work of equal value, capped at 10 person-days. Article II.1: "Celková cena za
    Díla činí 283.000 Kč (slovy: dvě stě osmdesát tři tisíc korun českých) bez DPH"; a
    small-scale contract awarded by a call to one supplier. The data come from the rectorate''s
    personnel and payroll department. Amendment 1, 1 September 2026 (registr smluv 39348805):
    adds Phase 3, transparent pay for work agreements outside employment (DPP, DPČ), sets the
    total at "333.000 Kč ... bez DPH" and moves the deadline to 31 December 2026. An earlier
    pilot on selected rectorate departments, 16 January 2026, is in S11. Contract text read
    through the Hlídač státu API, 2026-09-19; the registry page confirms the date and the
    283,000 CZK value. The amount is the original price excluding VAT, for the pay-gap analysis
    plus the equal-value advice, which the contract does not price apart. The payer is the
    employer whose pay is analysed. basis signed-contract, three and a half months before
    updated: a PAID receipt for this job, money 2.'
  date: '2026-06-02'
  payer: 'Univerzita Karlova, a public university as employer'
  amount_czk: 283000
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/37469849
  name: "Nemocnice České Budějovice — a pay-gap calculation for 2025, March 2026"
  gist: "a hospital company's pay-gap calculation"
  why: "What a Czech hospital company paid for a workshop and a calculation of its gender pay gap for 2025."
  note: 'Registr smluv 37469849 (idSmlouvy 35185493), order no. 26241060103 issued 26 March 2026,
    published 8 April 2026: Nemocnice České Budějovice, a.s. (IČO 26068877) to Greenometer s.r.o.
    (IČO 07638990). The order line: "Úvodní analýza, workshop a výpočet Gender Pay Gap za rok
    2025", 1 ks, "Celkem k úhradě bez DPH (základ DPH) CZK 84000,00", 101,640 CZK with VAT,
    delivery by 17 April 2026, raised by the economic department. The order gives no scope beyond
    that line. The same seller''s "Gender Pay Gap – Fáze 1" package in its contracts with Městská
    knihovna v Praze and Vodohospodářská společnost Olomouc (S11) is a workshop, cleaning and
    anonymising the payroll data, a regression GPG and the positions more than 5 % apart. Order
    text read through the Hlídač státu API, 2026-09-19; the registry page confirms the date and
    the 84,000 CZK value. The register publishes the accepted order as a contract. A joint-stock
    company employing its own staff, the closest payer on file to the large-firms buyer. basis
    signed-contract, six months before updated: a PAID receipt for this job, money 2.'
  date: '2026-03-26'
  payer: 'Nemocnice České Budějovice, a hospital company'
  amount_czk: 84000
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: price
  url: https://forum-media.cz/produkty/reseni-rovnych-mezd/
  name: "Nakladatelství FORUM — equal-pay web app"
  gist: "8,499 CZK a year"
  why: "What a Czech employer pays each year for a web app that tracks pay between women and men within job groups and writes pay-difference reports for inspectors."
  note: 'Product page read 2026-09-19: "8 499 Kč bez DPH za roční licenci" for the web
    application Spolehlivé řízení rovného odměňování, which "vytváří automaticky zprávy o
    rozdílech v odměňování pro kontrolní orgány", lets the employer "sledovat relace v rámci
    nastavených skupin, mezi muži a ženami" and "vykazovat údaje o odměňování", sold against
    the Labour Code change it dates to 1 January 2027. The same price sits in the 2026-08-25
    scan (S5), whose note left it unwritten because the page was not on this ledger. The page
    does not say whether the reports carry the directive''s quartile bands or mean and median
    gaps. basis list-price: an ASKING receipt, rung 1; money rests on S8 and S9.'
  date: '2026-09-19'
  payer: 'A Czech employer preparing for the equal-pay rules'
  amount_czk: 8499
  unit: per-year
  basis: list-price
  dims: [money]
- type: contract
  url: https://smlouvy.gov.cz/smlouva/39120650
  name: "Registr smluv — employers paying for pay-gap analysis, 2025 to 2026"
  gist: "the paying employers"
  why: "The public contracts register shows Czech employers paying consultants and a software seller to calculate their pay gap from payroll data, and the labour ministry paying for audits that employers get free."
  note: 'Hlídač státu API full-text search of the contracts register, 2026-09-19, first page of
    25 hits read per query: "rozdílů v odměňování" (29), "rozdílu v odměňování" (9), "gender pay
    gap" (41, both pages), "transparentnosti odměňování" (39, both pages), "transparentnost
    odměňování" (8), "rovného odměňování" (1,159), "rovné odměňování" (360), "2023/970" (59),
    "analýza odměňování" (16), "audit odměňování" (0), "mzdový audit" (17), "genderový audit"
    (55), "genderového auditu" (116), "platové struktury" (1), "systému odměňování" analýza (47),
    "hodnocení pracovních míst" (2), "Manažer odměňování" (7), Logib (25), ico:44004508 TREXIMA
    (208), ico:07638990 Greenometer (33). 23 contract texts read. EMPLOYERS PAYING GREENOMETER
    S.R.O. (IČO 07638990) FOR PAY-GAP WORK, texts read: (1) Univerzita Karlova, 2 June 2026 and
    its amendment of 1 September 2026: S8. (2) Univerzita Karlova, 16 January 2026 (36439353),
    external audit "Ověření rovnosti odměňování na vybraných odborech Rektorátu ... pomocí
    analýzy Gender Pay Gap" for 2025, 50,000 + 50,000 CZK excl. VAT for the GPG parts inside a
    200,000 CZK contract, the rest a sustainability-audit method. (3) Technická univerzita v
    Liberci, 12 August 2026 (39120650, S/0259/2026): "Výstupy Gender Pay Gap", purpose
    "zpracování návrhu řešení implementace požadavků směrnice EU o transparentnosti odměňování
    (2023/970)"; phase 2.1, groups of work of equal value and a recalculated GPG, 124,000; phase
    2.2, pay rules, pay bands and the directive''s articles 5 and 7, 118,000; phase 2.3,
    communication and "Nastavení reportingového procesu dle čl. 9 směrnice (zákonný reporting
    GPG od 2027)" with "Reportingová šablona a procesní manuál pro zákonný reporting", 42,000;
    each phase with "Platforma Greenometer", "Gender Pay Gap modul", unlimited users, to 31 July
    2027. Clause 5.1 reads 284,000 CZK excl. VAT; the registry value is 264,000, so neither is
    restated. (4) Městská knihovna v Praze, 5 June 2026 (38332060): "Gender Pay Gap – Fáze 1",
    a regression GPG and "special cases" over 5 %, with the platform module, 67,000 CZK excl.
    VAT. (5) Nemocnice České Budějovice, a.s., 26 March 2026: S9. (6) Vodohospodářská
    společnost Olomouc, a.s., 11 March 2026 (37165205): "Gender Pay Gap – Fáze 1" baseline
    report plus a carbon footprint, 90,000 CZK excl. VAT, milestones read in the text layer as
    22,500, 52,500 and 15,000. Greenometer''s other public contracts since 2024 are carbon
    footprints and ESG reporting; its first pay-gap contract found is (2). TREXIMA, SPOL. S R.O.
    (IČO 44004508): Dopravní podnik města Jihlavy, a.s., 16 December 2025 (36452533), a fixed
    200,000 CZK excl. VAT for an audit of the pay system "včetně „očištěného" Gender Pay Gap
    (GPG) prostřednictvím nástroje LOGIB" and a final report on the GPG and readiness for
    transparent pay, bundled with benchmarking, interviews and a new pay concept. Manažer
    odměňování licences: Česká pošta, s.p., 1 June 2026 (38281696), 79,000 CZK a year; Univerzita
    Pardubice, 1 September 2026 (39357657), 79,000 a year, registry 237,000; Vodárna Plzeň a.s.,
    24 February 2026 (36940369), 237,000; Plzeňské městské dopravní podniky, a.s., 2 April 2026
    (37424837), 240,000; Teplárny Brno, a.s., order 22 April 2026 (37917329, 80,000, "analytického
    a řídícího nástroje Manažer odměňování") and licence 16 July 2026 (38826962, no text layer).
    The licensed set is job descriptions, analytical job evaluation and employee-quality
    assessment, with Mzdový benchmarking free under OP TAK proof-of-concept project
    CZ.01.01.01/08/25_072/0008601; no Gender Pay Gap module is licensed, so none is a receipt
    (S7''s correction line). OTHER ADVISERS, texts read, not restated because the pay-gap line is
    bundled or absent: BD Advisory s.r.o. for Národní rozvojová banka, a.s., 19 May 2025
    (33328308), "Mzdová politika pro rok 2025 pro jednotlivé mzdové třídy a výpočet Gender Pay
    Gap", 135,000 CZK; for Operátor ICT, a.s., 9 January 2026 (36386473), support implementing
    the directive (job segmentation, recommendations, documents), 120,000; BL Services s.r.o. for
    Dopravní podnik měst Mostu a Litvínova, 15 April 2026 (37746073, registry 200,000, advisory
    and analytical services under 2023/970, hourly rate redacted) and Dopravní podnik města
    Děčína, 24 March 2026 (37359793, no value); LEGALITÉ advokátní kancelář for Vojenská zdravotní
    pojišťovna, February 2025 (32365576), a 200,000 CZK frame for a labour-law audit and legal
    advice on equal pay. THE STATE PAYS, EMPLOYERS DO NOT: MPSV and Ernst & Young, s.r.o., 19
    December 2024 (31616404), 15,792,300 CZK excl. VAT from OPZ+ project "Strategie a nástroje
    pro zvyšování transparentnosti v odměňování": at least 30 equal-pay audits and 3 re-audits
    by 31 December 2026, each audit priced in the itemised budget at 78,000 for data collection,
    126,000 for data analysis, 54,000 for the final report, 54,000 for the Pay Equality Plan,
    66,000 for advice and 30,000 for the de minimis paperwork; the template agreement with each
    employer says the service is "bezúplatné". Amendments 1 to 6 (March 2025 to August 2026)
    not read. A fully funded purchase for the employer: public money for this job, but it cannot
    lift money (SCORING.md), and it is a free competitor alongside Logib. FOUND AND NOT COUNTED:
    gender audits and gender-equality plans at universities, research institutes and towns,
    2017 to 2026 (e.g. Ústav živočišné fyziologie a genetiky AV ČR 27 March 2026, 145,440 CZK;
    Univerzita Palackého re-audit 6 May 2026, 175,000; Ostravská univerzita 2 September 2025,
    180,000), texts not read, pay gap not shown in scope; job architecture and job grading,
    the draft''s other duty: Deloitte Advisory for Mikrobiologický ústav AV ČR, 7 May 2026,
    1,203,400 CZK, and a sole trader for Fyzikální ústav AV ČR, 8 September 2026, a 1,200 CZK
    rate, registry 192,000; MPSV payments to TREXIMA and others inside the same state project,
    texts not read; a trade-union survey of employees on pay transparency (Asociace samostatných
    odborů, 2026). Every paying employer found is public, because only public bodies publish
    their contracts here. POSITIVE CONTROL: the ico:44004508 query surfaced MPSV''s ISPV
    contract with TREXIMA (28768012, "Dodatek č. 1 ke Smlouvě o ISPV 2024 - 2027", 15 May 2024;
    30190748, 17 September 2024), the mandate this ledger already names; control PASSED. WHY
    THIS ROW BACKS GAP, NOT MONEY: the amounts are restated as S8 and S9; this row carries the
    paying customers of the Czech sellers in locals[]. Gap was 0 and stays 0.'
  date: '2026-08-12'
  dims: [gap]
created: '2026-08-13'
updated: '2026-09-19'
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

Existing non-solutions: The Czech field is taken: two established sellers offer pay-gap analysis, two newer ones sell it too, and the state gives audits away [S5,S11].

- The firm that runs the state earnings survey sells a gender pay-gap report [S5,S11].
- A personnel-software firm markets pay bands and gender pay analysis [S5].
- A sustainability-reporting firm calculates pay gaps for universities and a hospital company [S11].
- A publisher sells a web app built for the new Czech equal-pay rules [S5].

The survey firm also sells job evaluation and wage benchmarks, drawn from the same survey data [S5]. Employers sign for its job grading in the public contracts register, and a city bus company paid it for a pay audit that included the gender gap [S11]. The sustainability firm sells its own pay-gap software module with the analysis [S11]. Its contracts compute the mean and median gap and flag groups of work more than 5% apart [S11]. The publisher's app groups staff by the value of their work and tracks the pay ratio between women and men [S5].

- The labour ministry and its labour inspectorate give Logib, a Swiss self-audit tool, to employers for free, and inspectors use it in their own checks [S5].
- Until the end of 2026 the labour ministry also pays a large consultancy for at least 30 equal-pay audits, free to the employers audited [S11].
- Employers already run Czech payroll and personnel systems such as Vema, Pamica and OKbase; the sources say nothing about whether these analyse pay gaps [S3,S4].
- No Czech product was found that turns a payroll export into the whole filing the EU rules prescribe [S5]. The contracts read cover the mean and median gap and the gap in bonuses, but none lists the share of women and men in each quarter of the pay scale, or the joint assessment [S11]. Not finding one does not prove none exists [S5].

Why now: Employers would have to rebuild how they set pay from January 2027, and firms with 150+ staff would report by April 2028 [S1].

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

Who pays: Some Czech employers already pay specialists to calculate their pay gap from payroll data, before the law has passed [S11].

- Two universities, a hospital and a water company bought pay-gap calculations in 2026 [S11].
- The labour ministry pays for 30 equal-pay audits that employers get free [S11].
- Czech pay-grading and pay-gap tools sell at a yearly list price [S5].

Every paying employer on file is a public one, because public bodies must publish their contracts [S11].

- Charles University's contract covers the mean and median gap, the gap in bonuses, and groups of work more than 5% apart [S11].
- The Technical University of Liberec also bought a template and a process for the legal pay-gap report [S11].
- Prague's city library bought the same first-phase calculation [S11].
- Other advisers bill public companies for a pay policy with a pay-gap calculation, or for help with the directive [S11].
- The survey firm billed a city bus company for a pay-system audit that included the gender gap [S11].
- The ministry's own audits cost it 126,000 CZK each for the data analysis alone [S11].
- Investors backed a Czech personnel-software firm that markets pay-gap analysis, in June 2026 [S5].
- Five consultancies offer pay-equity work as paid advice [S5].

The buyers would be employers with 150 or more staff first, then every employer that hires, since all would need the written pay system [S1]. A seller can come in two ways: a standalone audit tool, or a module inside the payroll systems employers already run [S3,S4]. Whether most employers buy before 30 April 2028 or scramble after is still open [S1].

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

2026-09-19 · brief corrected (owner-approved) — Brief before, verbatim: "Czechia is already late on the EU rules, and its draft goes further: pay ranges in every job ad and a first pay-gap report due April 2028 [S1]." After: "Czechia is late on the EU rules, and its draft would make every employer set pay by a written system [S1]. Applicants would learn the minimum pay, and firms with 150+ staff would report their pay gap by April 2028 [S1]." Why: [S1]'s article, re-read at its URL on this date, says the Czech draft obliges employers "to disclose only the minimum wage or salary", narrower than the directive's "initial pay level or its range", and that it is given "before employment contract negotiations begin"; it does not say the pay goes in the job ad. So "pay ranges in every job ad" became "Applicants would learn the minimum pay", the correction the 2026-09-18 entry flagged. "Goes further" was attached to the job-ad rule, which is narrower than the EU's, so the card now names what the draft does add beyond the directive instead: every employer must set pay by "a formal, documented remuneration system", from 1 January 2027 [S1]. "Already" was cut for length, and "a first pay-gap report due April 2028" became "firms with 150+ staff would report their pay gap by April 2028", so the card says who reports; the 30 April 2028 date is [S1]'s. No score, status, source, note, marker, title, solution, good_for, draft_law or body sentence changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 3 → 1, Willing to pay 0 → 1 and `score` 6 → 5; the band stays FAIR. Why now was 3 as deadline 2 plus the freshness point, which is retired. The duties are dated and close, from 1 January 2027, with first reports by 30 April 2028, but they sit in the labour ministry's bill. The government approved it on 31 August 2026 and it has not passed parliament. The EU directive behind it is untransposed [S1]. A bill fails REAL, and `draft_law:` holds the record at rung 1. The bill's fines of up to CZK 1M are not law yet. The decree change on monthly employer reporting is a different duty, tagged `dims: []` [S6]. Tagging pass for Willing to pay, every source on file that shows someone paying: TREXIMA's Manažer odměňování, 79,000 CZK a year to a Czech employer of 150 or more staff, is now tagged `dims: [money]` as an asking price [S7]. The ledger lists it as a direct seller: it sells a gender pay-gap report and pay-system analysis to these employers. It stops short of the directive's exact filing, and that is why it is an asking price for this job rather than for something adjacent. Not restated: Nakladatelství FORUM's 8,499 CZK a year sits in the [S5] note, but its own page is not on file; the Foreign Ministry's OKbase award buys support for an HR system, not pay-gap reporting [S4]; the five consultancies publish no fee [S5]; the state's Logib tool is free and paid for by no employer [S5]. No public money for these employers is on file, so there is no lift and money stops at 1, as the worksheet had it. [S1]'s and [S7]'s notes carried the old reading and now carry the correction. Why now prose re-read: the answer sentence stated the April 2028 report as fact while every other duty says "would"; "file a first report" now reads "would report", which keeps it within 25 words. Willing to pay already says Czech tools sell at a list price and no employer is yet shown paying, which is rung 1 in words. No `[Competition](#competition)` link was on this record. No other score, status, entry or body sentence changed.

2026-09-19 · Willing to pay search, owner-approved — `scores.money` 1 → 2, `score` 5 → 6; the band stays FAIR and `status` stays watching, since gap is still 0. The rescore above scored money 1 on TREXIMA's list price and left open whether that tool does this job (worksheet call 9). The search looked for a paid receipt and for a published price for the report itself. A full-text search of the contracts register through the Hlídač státu API, twenty queries, found Czech employers paying for pay-gap analysis in 2026, and 23 contract texts were read [S11]. Two are restated as price receipts tagged money. Univerzita Karlova signed on 2 June 2026 for an analysis of its whole payroll: the mean and median gap, an adjusted gap, base pay against bonuses, the groups of work more than 5% apart, and advice on equal-value categories, 283,000 CZK excluding VAT [S8]. Nemocnice České Budějovice, a.s. ordered a workshop and a Gender Pay Gap calculation for 2025 on 26 March 2026, 84,000 CZK excluding VAT [S9]. Both are signed within 24 months of `updated`, so money is 2 on a paid receipt and no public-money lift is needed. Nakladatelství FORUM's price page, left unwritten on 2026-09-04 because its URL was not on file, was read and added as an asking price: 8,499 CZK a year for an app that writes pay-difference reports for inspectors [S10].

TREXIMA untagged: [S7] now carries `dims: []`, which answers call 9. Česká pošta and Univerzita Pardubice pay 79,000 CZK a year, and Pardubice's contract says the price covers only job descriptions, job evaluation and employee grading; the wage benchmarking is given free as a pilot [S11]. The price page read on this date lists those modules plus benchmarking and names no pay-gap report. So the 79,000 CZK buys job grading, the written pay system next door, not the report in `solution:`. The score does not rest on it. S7's `why` had said the tool came with a gender pay-gap report and now says what the price buys; S5's `why` now calls it a job-grading and wage-benchmarking tool that listed a pay-gap report; both notes gained a correction line.

Market gap: new in `locals[]`, Greenometer, a sustainability-reporting firm that sells pay-gap analysis with its own software module, paid by five public employers in 2026 [S11]. It is `competes: direct` and `maturity: early`: its first pay-gap contract on file is January 2026, so it has sold this for less than three years. Gap was 0 on Sloneek and TREXIMA and stays 0, and `entry.incumbents` stays direct. TREXIMA's row said it "holds no public contract in the state contracts register"; the register holds several, so the row now names its paying customers, among them a city bus company that paid it 200,000 CZK in December 2025 for a pay-system audit that included the adjusted gender gap [S11]. The August sweep missed both, and S5's note says so.

Body: Willing to pay now opens on employers already paying specialists to calculate their pay gap [S11]. Its first three items are the paying employers, the ministry's free audits and the list prices [S5,S11]; below them, what the contracts cover, the Liberec reporting template, the library, the other advisers, the survey firm's audit and the ministry's cost per analysis [S11], with the funding and consultancy items kept [S5]. The old answer, "no Czech employer is yet shown paying", is false and is gone. Market gap now counts two newer sellers and the free audits in its answer sentence, adds the sustainability firm as item 3 and the ministry's audits as a bullet, and the "no product turns a payroll export into the finished filing" bullet now says what the contracts cover (mean and median gaps, the gap in bonuses) and what none lists (quartile bands, the joint assessment) [S5,S11]. Flagged as our reading: "because public bodies must publish their contracts" is the contracts-register law, not a sentence in any source; every payer found is public [S11]. "Two universities" counts Liberec, whose contract recalculates the gap after regrouping jobs [S11].

Searched and not added, all in S11's note: university and institute gender audits (2017 to 2026), whose texts were not read and whose scope does not show a pay gap; job-architecture and job-grading contracts (Deloitte for the Microbiology Institute, 1,203,400 CZK, May 2026; a sole trader for the Institute of Physics, September 2026), which buy the draft's other duty [S11]; BD Advisory, BL Services and LEGALITÉ, whose pay-gap line is bundled with pay policy or legal advice; the rest of Greenometer's pay-gap contracts (Liberec, the city library, the Olomouc water utility, the January 2026 university pilot), kept in the row, two receipts being enough; and the labour ministry's 15,792,300 CZK contract with Ernst & Young for at least 30 equal-pay audits [S11]. That last one is public money for this job, but the employer pays nothing, so it is fully funded and cannot lift money (SCORING.md); it is recorded as a free competitor. Web: the consultancy pages read (PwC, Deloitte, BDO, EY, Accace) and Greenometer's product page publish no fee. Positive control: the query on TREXIMA's IČO surfaced the labour ministry's ISPV contract with it (May and September 2024), the mandate the ledger already names. Only the first page of each query was read; "rovného odměňování" has 1,159 hits and was not exhausted. Not changed: title, brief, solution, good_for, draft_law, urgency, proof, demand and `entry`; none of the headline fields is made false by what was found.
