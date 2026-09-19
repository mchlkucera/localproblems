---
id: p-0029
region: cz
title: 'Czech public bodies must keep records in state-certified software from January'
brief: 'Ministries, hospitals and universities that miss the date risk a fine [S9]. This summer 19 public bodies tendered for records software [S2].'
price_search: 'Registr smluv full-text for "elektronická spisová služba" — the Interior
  Ministry''s support framework and Prague''s e-spis development contracts sit there with
  licence and annual-support lines — and the MS2021+ index under "spisové služby" (Město
  Pelhřimov is funded there to deploy one across the town and its organisations); otherwise ask
  the IT head of a district town (obec s rozšířenou působností) what its migration and annual
  support cost.'
solution: 'Build a migration service that moves a public body''s records into certified software, every file and its history intact.'
good_for: 'Someone who can migrate office data and sell through public tenders.'
category: govtech
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 2
  urgency: 3
  demand: 0
  gap: 0
status: watching
entry:
  level: very-hard
  buyer: public
  permission: licence
  incumbents: direct
  integration: national-system
  money: outside-money
  why: 'Easier: a legal date forces every public body to act, and some already tender and pay for records systems. Harder: every buyer buys by public tender; a records system needs the state certificate before it is offered, and four Czech vendors hold one; and tender and certificate cycles run before the first invoice.'
comps:
- name: Documaster
  url: https://www.documaster.com/
  geo: NO
  since: 2014
  traction: 'First records kernel certified by Norway''s National Archives (Noark); NOK 100M from Summa Equity; revenue >15x since 2017 (Summa)'
locals:
- name: GORDIC (GINIS)
  url: https://www.gordic.cz/
  ico: '47903783'
  since: 1993
  competes: direct
  maturity: established
  evidence: It sells GINIS, which holds the state records attest 1/2025, valid to 25 November
    2027 and extended to version 5.26 [S8]. Trading since 1993, and three separate public bodies
    buy from it on the state contracts register — MČ Praha 20 and two Hradec-region secondary
    schools [S8].
- name: ICZ.DMS (e-spis)
  url: https://www.i.cz/
  ico: '06696805'
  since: 2017
  competes: direct
  maturity: established
  evidence: It sells e-spis, which holds the state records attest 2/2026, running 7 May 2026 to
    7 May 2028 [S8]. Prague awarded it about €3.3M for e-spis development in August 2026 [S3];
    ICZ.DMS a.s. has traded since 21 December 2017.
- name: Seyfor (ELDAx)
  url: https://www.seyfor.cz/
  ico: '01572377'
  since: 2013
  competes: direct
  maturity: established
  evidence: It sells ELDAx, which holds the state records attest 3/2026, extended to version 6.0.1
    [S8]. Trading since 2013, with město Krnov and Psychiatrická nemocnice v Kroměříži among its
    public buyers on the state contracts register [S8].
- name: MIT Consulting (MIT ERMS)
  url: https://www.mitconsulting.cz/
  ico: '25689240'
  since: 1998
  competes: direct
  maturity: established
  evidence: It sells MIT ERMS, which holds the state records attest 4/2026, running 22 July 2026
    to 22 July 2028 [S8]. Trading since 31 August 1998.
- name: GEOVAP
  url: https://www.geovap.cz/
  ico: '15049248'
  since: 1991
  competes: direct
  maturity: established
  evidence: It sells a records system into exactly this wave, and two separate public bodies buy
    from it on the state contracts register — statutární město Karviná and Ředitelství silnic
    a dálnic [S8]. Trading since 26 February 1991, but its system is not on the state's list of
    attested products at this check, so it sells into the deadline without the certificate the
    four attested vendors hold.
- name: T-MAPY (TESS Online)
  url: https://www.tmapy.cz/
  ico: '47451084'
  competes: direct
  maturity: early
  evidence: It sells TESS Online, a Czech records system, into exactly this wave — but it is not
    on the state's published list of attested products at this check [S8], so as it stands it
    cannot be offered to a public body from 1 January 2027. No start year and no count of offices
    running it are published, so its size is unknown.
- name: OSS Alliance
  url: https://ossalliance.cz/
  competes: direct
  maturity: early
  evidence: It gives the smallest towns an open-source records system free of charge, with two
    years of hosting, in cooperation with the Ministry of the Interior [S8] — the same product
    to the same buyer at a price of zero, which is why it competes directly. No year for the start
    of supply is published, so how long it has been running is unknown; a zero-price rival at
    the bottom of the market all the same.
- name: GRADUAL SYSTEMS
  ico: '27876608'
  since: 2007
  competes: adjacent
  maturity: established
  evidence: It sells support for the Justice Ministry's ACTA records system, and the ministry pays
    it by the day to move other offices' records into ACTA — the Criminal Register's in 2024 and
    three Government Office units' in 2026 [S12]. ACTA is not on the state's list of certified
    records systems [S8,S12], so these moves land in uncertified software, not in the certified
    kind this problem needs. A named customer, the Justice Ministry, under support contracts of
    2024 and 2025 [S12]; trading since 3 April 2007.
sources:
- type: regulation
  name: "The eSSL attestation regime (§69b–e, Act 499/2004)"
  gist: "the attestation law"
  why: "Legal commentary on the gate: since 1 July 2025 suppliers may not offer non-attested records systems to public-law originators, and the transitional period for those bodies runs out at the end of 2026."
  url: https://www.epravo.cz/top/clanky/dodani-elektronickeho-systemu-spisove-sluzby-po-172025-119824.html
  note: 'Attestation regime under §69b-e zákona č. 499/2004 Sb. (introduced by the DEPO amendment,
    z. č. 261/2021 Sb.): electronic records-management systems (eSSL) must hold a state atest
    — from 1 Jul 2025 suppliers may no longer offer non-attested products, and the transitional
    period for public-law originators (state organizational units, contributory organisations,
    state enterprises) to run attested systems ends 31 Dec 2026. Verified via legal commentary
    2026-08-13. Compliance date <18 months with the supply-side ban already in force: deadline
    sub-score 2.
    Rescored 2026-09-19: the deadline sub-score is retired. On the 2026-09-19 ladder the duty is
    REAL (enacted, binds the public body) and CLOSE; S9 carries the date and the fine, so urgency
    is 3.'
  date: '2026-12-31'
- type: tender
  name: "TED — SÚKL records system (~€1.4M), and the wave around it"
  gist: "the €17M tender wave"
  why: "An open competition by the state drug agency, inside ~28 records-management procurement records from ~19 distinct public buyers (~€17M) in ten weeks — with SÚRAO republishing four times."
  url: https://ted.europa.eu/en/notice/-/detail/415250-2026
  note: 'ted-415250-2026: SÚKL ran an OPEN ~€1.4M competition for a records management system
    (Jun 2026) — open tender ≥5M CZK: money 2. It sits in a wave of ~28 records-management
    procurement records from ~19 distinct public buyers (~€17M) in the Jun–Aug TED window:
    SÚRAO published its certified-eSSL tender four times, Nemocnice Pardubického kraje three
    times, OZP twice — repeat publications signalling procedures that struggle to close.
    Rescored 2026-09-19: "open tender ≥5M CZK: money 2" is the retired rung. An open competition
    for a records system is public money nearby on the
    2026-09-19 ladder and earns no point; it buys the software, not the migration this record
    sells, and no award in the wave is on file restated as a price for the move.'
  date: '2026-06-17'
  signal: ted-415250-2026
- type: tender
  name: "TED — City of Prague, e-spis development (~€3.3M)"
  gist: "the €3.3M Prague award"
  why: "Prague's third records-management award in the window, buying development on the incumbent ICZ e-spis stack — the large-buyer end of the same wave."
  url: https://ted.europa.eu/en/notice/-/detail/559572-2026
  note: 'ted-559572-2026: City of Prague awarded ~€3.3M for e-spis development incl. modules
    and training (Aug 2026), its third records-management award in the window — the large-buyer
    end of the same wave, purchasing development on the incumbent ICZ e-spis stack.'
  date: '2026-08-12'
  signal: ted-559572-2026
- type: tender
  name: "TED — Ministry of the Interior, records support 2025–2028 (~€642k)"
  gist: "the €642k support contract"
  why: "A ministry buying multi-year support rather than a licence — the recurring half of the bill, and the buyer type at the top of the obligated population."
  url: https://ted.europa.eu/en/notice/-/detail/535679-2026
  note: 'ted-535679-2026: Ministry of the Interior awarded ~€642k for records-management systems
    support 2025–2028 (Aug 2026) — a ministry-level buyer inside the same Jun–Aug window,
    and support (not just licence) spend, which is the recurring half of the bill.'
  date: '2026-08-03'
  signal: ted-535679-2026
- type: tender
  name: "TED — Ostrava University records tender, ended without a winner"
  gist: "the university tender, no winner"
  why: "The university buyer type inside the same wave: a tender for a certified records system with support, estimated at about €408k, ended in June 2026 without a winner."
  url: https://ted.europa.eu/en/notice/-/detail/442243-2026
  note: 'ted-442243-2026: Ostravská univerzita awarded ~€408k for a records management system
    incl. service support (Jun 2026) — the university buyer type in the same wave.
    Rescore tagging pass 2026-09-19: the TED notice at this url, read on that date, buys the
    supply and implementation of an attested eSSL plus support, training, development and exit
    services (estimated 10M CZK); it names no migration of existing records, so it is not
    restated as a price receipt for this job and stays public money nearby.
    Corrected 2026-09-19, Willing to pay search: this is a result notice with NO award. Its
    result reads "Vítěz nebyl vybrán a soutěž je ukončena", the reason a buyer''s decision "z
    důvodů technických nebo procedurálních chyb", after 3 tenders (TED XML: winner-selection-status
    clos-nw, non-award-justification tch-pr-error; Czech PDF read on this date). The ~€408k was the
    10,000,000 CZK estimated value, not an award. The procedure (TED 201339-2026, amended by
    310464-2026, then this notice) has no later notice on TED, and the contracts register shows no
    records-system contract signed by Ostravská univerzita (IČO 61988987) since 2025. Name, gist
    and why said "award" and now say what happened.'
  date: '2026-06-29'
  signal: ted-442243-2026
- type: tender
  name: "TED — Lesy ČR records system (~€1.1M)"
  gist: "the €1.1M state-forest award"
  why: "The state-enterprise buyer type, and one of the larger single awards in the wave."
  url: https://ted.europa.eu/en/notice/-/detail/529246-2026
  note: 'ted-529246-2026: Czech State Forests (Lesy ČR) awarded ~€1.1M for an electronic records
    management system (Jul 2026) — the state-enterprise buyer type, and one of the larger
    single awards in the wave.
    Rescore tagging pass 2026-09-19: the TED notice at this url, read on that date, buys the
    supply and implementation of an eSSL integrated with the buyer''s other systems, awarded to
    Seyfor at 27,771,072 CZK; it names no migration of existing records, so it is not restated
    as a price receipt for this job and stays public money nearby.
    Corrected 2026-09-19, Willing to pay search: the signed contract behind this award, read in
    the contracts register on this date, DOES name the move. Its stage 5, "Příprava a převzetí do
    zkušebního provozu, migrace dat", is priced at 483,700 CZK excl. VAT, and Seyfor''s offer
    migrates the open files from the current system; that stage is restated as S10. "It names no
    migration" above holds for the TED notice only.'
  date: '2026-07-30'
  signal: ted-529246-2026
- type: tender
  name: "TED — Prague, GINIS ENTERPRISE+ development (~€275k)"
  gist: "the €275k GINIS award"
  why: "Direct evidence that GORDIC's GINIS stack is one of the incumbents this wave is being bought from, alongside ICZ's e-spis."
  url: https://ted.europa.eu/en/notice/-/detail/533101-2026
  note: 'ted-533101-2026: City of Prague awarded ~€275k for GINIS ENTERPRISE+ development incl.
    records management (framework, Jul 2026) — direct receipt that GORDIC''s GINIS stack is
    one of the incumbents the wave is being bought from, alongside ICZ e-spis.'
  date: '2026-07-31'
  signal: ted-533101-2026
- type: gap-check
  name: "Attested eSSL supplier scan"
  gist: "the four attested vendors"
  why: "The state publishes the roster of attested records systems, and four Czech suppliers are on it — GORDIC's GINIS, ICZ.DMS's e-spis, Seyfor's ELDAx and MIT Consulting's MIT ERMS — with a dozen more Czech systems not yet attested."
  url: https://agenturacas.gov.cz/atestace/vydane-atesty/
  note: 'Czech-language supplier scan 2026-08-25. The decisive instrument is the state''s own
    register: the Czech Agency for Standardization (Česká agentura pro standardizaci) publishes
    every issued eSSL attest at agenturacas.gov.cz/atestace/vydane-atesty. At this check FOUR
    products from FOUR Czech suppliers hold one. Atest 1/2025 — GORDIC spol. s r.o., IČO
    47903783, Erbenova 2108/4, Jihlava — GINIS v525, issued 25.11.2025, valid to 25.11.2027,
    extended by declaration to v5.26 on 15.04.2026. Atest 2/2026 — ICZ.DMS a.s., IČO 06696805,
    Na hřebenech II 1718/10, Praha 4 — e-spis v3, 07.05.2026 to 07.05.2028. Atest 3/2026 —
    Seyfor, a. s., IČO 01572377, Drobného 555/49, Brno — ELDAx eSSL v6.0.0, 07.05.2026 to
    07.05.2028, extended to v6.0.1 on 20.05.2026. Atest 4/2026 — MIT Consulting, s.r.o. — MIT
    ERMS v3.5, 22.07.2026 to 22.07.2028. Every attest runs two years and attaches to a product
    version, so re-attestation is a standing cost that concentrates supply further. The wider
    Czech eSSL field, none of it on the issued-attest list at this check, runs to roughly a
    dozen more products: T-MAPY spol. s r.o. (IČO 47451084) TESS Online, Triada Munis ERMS,
    GEOVAP spol. s r.o. (IČO 15049248) DMS, VERA Radnice, Alis KEO4, MAGION, ELISA, TranSoft,
    WESS, VISION, e-spis LITE, and eZOP from SoftHouse s.r.o. (vendor listing at tesso.cz). At
    the bottom of the market OSS Alliance gives small obce an open-source records system free,
    with two years of hosting, in cooperation with the Ministry of the Interior — a zero-price
    competitor for the smallest originators. CONTRACTS-REGISTER INSTRUMENT —
    data/lookup/cz-contract-parties.jsonl aggregated by IČO over 3,984 distinct suppliers,
    counting the distinct public buyers each serves: within its single recent ingest window
    GORDIC serves 3 distinct public buyers (two Hradec-region secondary schools and MČ Praha 20
    - Horní Počernice), Seyfor 2 (město Krnov, Psychiatrická nemocnice v Kroměříži), GEOVAP 2
    (statutární město Karviná, ŘSD s.p.), ICZ a.s. (IČO 25145444) 1 (Český statistický úřad)
    and ICZ.HEA a.s. (IČO 07240091) 1 (Nemocnice Břeclav). Multi-buyer public suppliers are the
    incumbent signature, not a startup one. The lookup is one ingest window rather than the
    whole registr smluv, so those counts are floors, not totals. POSITIVE CONTROLS, two of
    them. On the contracts instrument: GORDIC, the incumbent this file already named, does
    surface as a multi-buyer public supplier — PASSED. On Czech-language search: the same
    method run at Softlink, the incumbent named on p-0026, surfaced its 169/868 MHz metering
    platform — PASSED. Corpus contrast: T-MAPY, MIT Consulting, ELDAx, Munis, Triada, GEOVAP,
    VERA Radnice and KEO4 return ZERO hits across all 11,330 signals in data/register.db, while
    GORDIC, GINIS and e-spis appear only because they win TED-scale tenders — the pipeline sees
    tender winners and is blind to the rest of the supply side. gap was already 0 and stays 0;
    status moves to watching under the SPEC §4 de-rank rule on the named Czech incumbents.
    NOTED, NOT ACTED ON: several Czech sources in this scan (tyden.cz, munis.cz, eldax.cz)
    report an odklad giving authorities more time to move onto attested systems, and describe
    the hard line as 1 January 2027 rather than 31 December 2026. That touches the S1 deadline
    and needs its own verification against the statute before anything on this file changes.'
  date: '2026-08-25'
  queries:
    - "seznam atestovaných elektronických systémů spisové služby atest eSSL"
    - "elektronická spisová služba atest 2026 dodavatel atestované řešení pro úřady"
    - "spisová služba pro obce a příspěvkové organizace software dodavatelé přehled cena migrace"
    - "kdo dodává atestovanou spisovou službu GINIS e-spis ELDAx MIT ERMS TESS Online porovnání"
    - "český software pro dálkové odečty vodoměrů sběr dat z měřidel vodárny systém"
  checked: [google-cz, ares, cz-saas-directories, own-funded-ledger]
  expires: '2026-11-23'
- type: regulation
  name: "ČAS — when a public body must actually be running an attested eSSL"
  gist: "the 1 January 2027 date"
  why: "The state agency that issues the attests puts the date in one sentence: a public-law originator must be running records management in an attested eSSL no later than 1 January 2027."
  url: https://agenturacas.gov.cz/atestace/otazky-a-odpovedi/
  note: 'Statute check 2026-08-25, closing the item the supplier scan flagged and did not act
    on. The Czech Agency for Standardization Q&A states "Veřejnoprávní původce je povinen
    vykonávat spisovou službu v elektronické podobě v atestovaném eSSL nejpozději od 1. ledna
    2027", pointing at the transitional provision in §27 of vyhláška č. 259/2012 Sb.; the same
    page repeats the supply-side rule, "Dodavatel od 1. července 2025 smí nabízet pouze
    atestovaný eSSL". Legal commentary read live on the same date (epravo, "Nestačí mít systém")
    independently gives 1 January 2027 as the end of the transitional period under §63 odst. 3
    zákona č. 499/2004 Sb., and records a fine of up to 200,000 CZK for an originator that is
    not compliant from that day. So this file had the boundary a day early: the transitional
    period runs THROUGH 31 December 2026 and the obligation bites FROM 1 January 2027, which is
    how the state and the trade press both state it. CAVEAT recorded rather than smoothed over:
    the same ČAS page also carries a stale section giving 1 January 2026 — an internal
    inconsistency on the issuing agency''s own page. The 2027 date is the one tied to the
    transitional provision and the one every Czech source in the 2026-08-25 scan reports.
    Deadline sub-score unchanged at 2, under 18 months either way, so urgency stays 3.
    Rescored 2026-09-19: the deadline sub-score and freshness are retired. On the 2026-09-19
    ladder this is REAL (Act 499/2004 and decree 259/2012, binding the public body), CLOSE (1 Jan
    2027) and has TEETH (the fine up to 200,000 CZK above): rung 3.'
  date: '2027-01-01'
- type: price
  url: https://smlouvy.gov.cz/smlouva/38628540
  name: "Czech State Forests — the records move, priced as its own stage, July 2026"
  gist: "a state firm pays for the move"
  why: "What Czech State Forests pays its certified vendor, as a separate stage of its new records contract, to fill the new system with data and move its open files across."
  note: 'Registr smluv 38628540 (idSmlouvy 36298776, SML-00001-2026-99-20), concluded and
    published 2 July 2026: Lesy České republiky, s.p. (IČO 42196451) and Seyfor, a.s. (IČO
    01572377), "Smlouva o dodávce a implementaci elektronického systému spisové služby a o
    poskytování služeb", the award of open procedure 099/2024/032 (VVZ Z2025-070134; TED
    529246-2026, S6). Art. II.1: the buyer "je veřejnoprávním původcem"; II.2: the delivered
    system "nahradí stávající řešení elektronické spisové služby užívané Objednatelem"; III.2: it
    "musí být atestovaný dle Zákona o archivnictví". Art. III.6 splits delivery into stages; stage
    5 is "Implementační práce – Příprava a převzetí do zkušebního provozu, migrace dat", whose
    output (IV.7) is trial operation "v produkčním prostředí Objednatele včetně jeho naplnění
    daty". Price clause VI.6: "Za řádné provedení etapy č. 5 … náleží Poskytovateli cena ve výši
    483 700 Kč … bez DPH". For scale: implementation 14,389,240 CZK in all, service 1,049,458 CZK
    a year, development 8,200 CZK a man-day, contract value 27,771,072 CZK excl. VAT. Annex 5,
    Seyfor''s technical description of 16 March 2026, §4.2.1: "V rámci implementace bude
    provedena migrace otevřených spisů ze stávajícího systému do nového eSSL v souladu s
    požadavky nové legislativy a NSESSS", with the old filing plan mapped onto the new one and the
    old file marks and reference numbers kept (§4.2.2–4.2.4). Seyfor''s ELDAx holds attest 3/2026
    (S8). The system it replaces is, on the register''s metadata, ACTA, whose maintenance Lesy ČR
    bought from Aricoma Digital in April 2025 (registr smluv 32824880, not opened). LIMITS: the
    stage also covers preparing and handing the system over into trial operation, so 483,700 CZK
    is an upper bound on the move inside this contract, not the move alone; Annex 2, the
    technical specification that defines the stage (ch. 4.1.5), is not in the published text; and
    the offer names the open files, not the whole archive. Contract text read through the Hlídač
    státu API, 2026-09-19. basis signed-contract, 2.5 months before updated: a PAID receipt for
    this job, money 2.'
  date: '2026-07-02'
  payer: 'Lesy České republiky, a state enterprise'
  amount_czk: 483700
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/38920946
  name: "Fakultní nemocnice Plzeň — moving onto the certified version, July 2026"
  gist: "a hospital pays for the move"
  why: "What a faculty hospital pays its vendor to move its records system, and the records in it, onto the certified version before the deadline."
  note: 'Registr smluv 38920946 (idSmlouvy 36579874, contract 0944/26/06/SIS), concluded and
    published 28 July 2026: Fakultní nemocnice Plzeň (IČO 00669806), a contributory organisation
    of the Health Ministry, and ICZ.DMS a.s. (IČO 06696805), "Smlouva o dílo – Upgrade eSSL na
    atestovanou verzi". Art. 2.1: "provedení upgrade elektronického systému spisové služby …
    e-spis na verzi atestovanou v souladu s požadavky zákona č. 499/2004 Sb."; 2.2: it includes
    "migrace binárních souborů na filesystem, analýza dat a oprava na validní data, vytvoření
    testovacího prostředí, migrace dat do testovacího prostředí, vytvoření produkčního prostředí,
    realizace školení uživatelů, migrace dat do produkčního prostředí"; 3.3: finished and running
    "nejpozději do 30.11.2026 tak, aby Objednatel splnil povinnost používat atestovaný
    elektronický systém spisové služby". Art. 4.1: "Celková cena za plnění dle této Smlouvy činí
    892 800 Kč … bez DPH", a ceiling. Annex 3 by line, excl. VAT: binary files to the file system
    172,800; data analysis and repair 76,800; test environment 115,200; data migration to test
    134,400; production environment 124,800; training 57,600; production migration 172,800; extra
    support 38,400. The four data lines come to 556,800 CZK. The cut-over in Annex 2 switches off
    the old platform (G1), backs it up and runs "Provedení převodu dat a konfigurace". No licence
    line is in the price table, so the whole amount buys the move onto the certified version
    (ICZ.DMS e-spis 3, attest 2/2026, S8), with training and extra support. Contract text read
    through the Hlídač státu API, 2026-09-19. basis signed-contract, under two months before
    updated: a PAID receipt for this job.'
  date: '2026-07-28'
  payer: 'Fakultní nemocnice Plzeň, a faculty hospital'
  amount_czk: 892800
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38720408
  name: "Registr smluv — public bodies paying to move their records, 2024 to 2026"
  gist: "who pays for the move"
  why: "The public contracts register shows public bodies paying to have their records moved into certified software inside their vendor contracts, and one ministry buying records moves as separate orders."
  note: 'Hlídač státu API full-text search of the contracts register, 2026-09-19, over contracts
    concluded from 2024-09-19 (24 months before updated): "migrace dat" AND "spisové služby" (222
    hits, all nine pages listed), "atestovanou verzi" (24), "migrace spisové služby" (1); plus the
    two buyers the rescore worksheet named, by IČO: Ostravská univerzita 61988987 with "spisové
    služby" OR eSSL since 2025 (1 hit, a Magion EIS contract, not records) and Lesy ČR 42196451
    with Seyfor 01572377 (34 hits). POSITIVE CONTROL: the Lesy ČR records contract, found first by
    the two IČOs, surfaces on page 3 of the full-text query — PASSED. RESTATED AS PRICE RECEIPTS,
    texts read: Lesy ČR, 2 July 2026, the new certified system replaces the current one and its
    stage 5 prices "migrace dat", the vendor moving the open files with their old file marks and
    reference numbers (S10); Fakultní nemocnice Plzeň, 28 July 2026, the move of its e-spis onto
    the certified version, data migration to test and production included, due by 30 November
    2026 "aby Objednatel splnil povinnost používat atestovaný elektronický systém spisové služby"
    (S11). READ, NOT RESTATED: (1) Český báňský úřad (IČO 00025844) and ICZ.DMS, 33834185,
    concluded 23 June 2025, "Upgrade ESSL na atestovanou verzi", 1,403,376 CZK excl. VAT: impact
    study, test environment, "otestování migrace dat na vzorku dat", production environment,
    training, "migrace produkčního prostředí" and extra support; the same job as S11, but its
    price table is blank in the register''s text layer, so only the total is known, and S11
    already carries the kind. (2) Město Mělník (IČO 00237051) and GORDIC, 37854805, 5 May 2026,
    "Smlouva na dodávku a implementaci atestované elektronické spisové služby", 5,614,000 CZK
    excl. VAT: Annex 3 lists "Migrace dat včetně migrace dat ze současného systému ATHÉNA od roku
    2006" and six months of support for the old system, the move due by 30 November 2026, but
    every line price is blacked out. (3) Fakultní nemocnice Bulovka (IČO 00064211) and Seyfor,
    38002569, 15 May 2026, a new eSSL replacing AthenA, 2,971,777 CZK excl. VAT: the specification
    requires "migrace dat ze stávající eSSL do nové eSSL", the old system kept read-only for at
    least 4 years, but the move has no price line of its own. NEXT DOOR, NOT COUNTED: the Ministry
    of Justice (IČO 00025429) orders GRADUAL SYSTEMS, s.r.o. (IČO 27876608, ARES 3 April 2007),
    under its ACTA support contracts 83/2024-MSP-CES and 171/2025-MSP-CES, to move records INTO
    ACTA: order MSP-101/2024-OI-OBJ/3 of 25 September 2024, registr smluv 30384264, "řešení
    migrace dat Rejstříku trestů do prostředí eSSL Ministerstva spravedlnosti", up to 42
    man-days, 453,600 CZK excl. VAT; order MSP-82/2026-OPPIC-OBJ/2 of 29 June 2026, 38720408,
    "Součinnosti k migraci dat útvarů Úřadu vlády", up to 17 man-days, 190,400 CZK excl. VAT,
    whose offer MSP-ACTA-2025-II/8 moves three Government Office units'' files, documents,
    attached files and transaction log, delivered in the National Standard format, into ACTA,
    keeping file marks, reference numbers and retention codes. That is the migration service
    itself, bought separately at 10,800 and 11,200 CZK a man-day, but ACTA is not on the Czech
    Agency for Standardization''s list of issued attests, re-read on 2026-09-19 with the same four
    products as S8, so the records land in uncertified software: not this job, no receipt.
    Národní rozvojová banka (IČO 44848943) and SoftHouse, 35351441, 13 October 2025, "Migrace dat
    ze systému EZOP etapa 2 - export dokumentů, koordinace, testování", 1,100,736 CZK excl. VAT,
    line "Etapa 2 (Náhrada spisové služby EZOP)": the export out of an uncertified system, but the
    offer is not published and the target is a document-management system bought from ICZ
    (33901561, not opened), not shown to be a certified one. Technical moves inside one system,
    not counted: ICZ.DMS moving e-spis data from database to file system or from Oracle to MS SQL
    for Český Krumlov (37763301, 37763297), Správa NP České Švýcarsko (37023305), Správa NP
    Šumava (36129877) and SOA Třeboň (34631693). METADATA ONLY, NOT OPENED: more moves onto a
    certified version, Město Mariánské Lázně and GORDIC, "Přechod elektronické spisové služby
    GINIS na atestovanou verzi", 27 March 2026 (37403633); Město Louny and GORDIC, "Rozšíření SSL
    na atestovanou verzi", 15 December 2025 (36159889); Město Lipník nad Bečvou and ICZ.DMS,
    upgrade to e-spis G2, 3 July 2025 (34250873); and paid analyses or consultations before a
    move, Město Příbram (36787101), UTB Zlín (36237185), Hlavní město Praha and INADVISORS
    (36662585), Statutární město Olomouc and OVANET (38968354). FOUND, ADJACENT, NOT ON THE
    LEDGER: VITA software, s.r.o. (IČO 61060631, ARES 5 February 1996), paid by Plzeň''s city IT
    body (37673129, 22 April 2026, 254,600 CZK excl. VAT) and by the Dopravní a energetický
    stavební úřad (37636325, 20 April 2026, 189,000 CZK excl. VAT) for "Přechod na atestovanou
    verzi eSSL e-spis G2"; the Plzeň order reads "Dodávka propojení agend VITA na atestovanou
    verzi e-spis G2" with a trial data transfer, so it reconnects its own agenda software to the
    certified system and does not move the records. WHY THIS ROW CARRIES dims: []: the amounts for
    this job are restated as S10 and S11, which carry money; this row names who pays and who does
    the work, and backs no score.'
  date: '2026-07-10'
  dims: []
created: '2026-08-13'
updated: '2026-09-19'
---

Every Czech public body must keep its official records in state-certified software from 1 January 2027 [S9].

- Only four Czech records systems hold the state certificate [S8].
- About a dozen more Czech records systems do not hold it [S8].
- Since July 2025 suppliers may not offer public bodies an uncertified system [S1].

The records service, spisová služba in Czech, is the layer under all of a public body's official correspondence, and it now runs as an electronic records-management system [S1]. The law behind the certificate is the archives act, No. 499/2004 [S1]. It covers what it calls public-law originators: state bodies, organisations the state or a town funds, and state enterprises [S1].

- The certificate is issued by the Czech Agency for Standardization, which publishes every certificate it has issued [S8].
- Each certificate runs for two years and covers one version of one product [S8].

Existing non-solutions: Four Czech vendors already hold the certificate, and a free state-backed system serves the smallest towns [S8].

- The four were certified between November 2025 and July 2026, for two years [S8].
- Three certified vendors also charge public bodies for moving their records in [S12].
- About a dozen more Czech records systems are not on the list [S8].

Prague bought development on two certified systems this summer, and its amounts are under [Willing to pay](#willing-to-pay) [S3,S7]. The uncertified also include Triada's Munis, VERA Radnice and Alis's KEO4 — three more Czech records systems [S8]. Two others sell into this wave and are listed above [S8].

- A public body running one of those systems must move to a certified one by 1 January 2027, unless its supplier is certified first [S8,S9].
- The smallest towns can get an open-source records system free, with two years of hosting, from a group working with the Ministry of the Interior [S8].
- A ministry pays one Czech firm by the day to move other offices' records, but into a system without the certificate [S12].

So the certificate is scarce, not the software [S8]. The demand on record is the tenders themselves: no public body's complaint has been found, and no source counts how many still run an uncertified system [S2].

Why now: Public bodies must be on certified records software by 1 January 2027, and some have already tendered for it more than once [S2,S9].

- A body that misses the date risks a fine up to 200,000 CZK [S9].
- The state nuclear-waste authority published its records-system tender four times [S2].
- The Pardubice region's hospital group published its tender three times [S2].

A health insurer published its tender twice [S2]. A notice published again shows that the tender ran again, not why [S2]. The dates come from the archives act and its decree [S1,S9]:

- Since 1 July 2025 suppliers may not offer or supply an uncertified records system to these public bodies [S1].
- On 31 December 2026 the transition period ends [S1].
- From 1 January 2027 a public body must run its records in a certified system, and one that does not risks the fine [S9].
- The agency that issues the certificates gives the 1 January 2027 date, citing the transition rule in decree No. 259/2012 [S9]. An older section of the same page still gives 1 January 2026; the 2027 date is the one tied to the rule [S9].

Who pays: Public bodies already pay to have their records moved into certified software, inside their contracts with the certified vendors [S12].

- The state forests' records contract prices the data move as its own stage [S12].
- A faculty hospital and the state mining authority each contracted their own move [S12].
- A ministry buys records moves separately, but into a system without the certificate [S12].

The amounts are signed contracts in the public contracts register, and they are listed in this section's table [S12].

- The state forests' new system replaces its current one, and the vendor moves the open files across with their old file marks and reference numbers [S12].
- The faculty hospital's move must be finished by 30 November 2026, so that it meets the duty to use a certified system [S12].
- A town's contract moves its records back to 2006 from its current system, but the price of that line is blacked out [S12].
- A Prague hospital's new contract includes the move, without a price of its own [S12].
- The ministry's two orders buy the move of the criminal register's records in 2024 and of three government-office units' records in 2026, priced by the day [S12].

Public bodies also buy the systems themselves: about €17M tendered this summer, in about 28 procurement notices from about 19 public buyers between June and August 2026, on TED (the EU's public tender journal) [S2].

- Czech State Forests awarded about €1.1M for an electronic records system [S6]. Its award notice does not mention the move; its signed contract does [S6,S12].
- The Interior Ministry awarded about €642k for records-system support to 2028 [S4].
- The state drug agency ran an open competition for a records system worth about €1.4M [S2].
- Prague awarded about €3.3M for development of one certified system, including modules and training, its third records award in the window [S3].
- Prague also awarded about €275k for development of another certified system, under a framework [S7].
- Ostrava University's tender for a certified system, estimated at about €408k, ended in June 2026 without a winner [S5].
- The Interior Ministry's contract runs from 2025 to 2028 and buys support rather than a licence [S4]. So a body pays first for a certified system, then again each year for support [S4].

A rough estimate: if ten weeks' €17M held all year, visible spending would be about €90M a year [S2]. Smaller purchases below the EU tender threshold are not in that count.

Vendors pay too: each certificate covers one product version for two years, so renewing it is a standing cost that leaves fewer suppliers [S8].

Solved elsewhere: One Norwegian company sells records software certified by Norway's national archives, and has grown on that certificate.

Its funding and growth are in its row above. It shows a national certificate can become the thing a seller builds on. No second country with a records certificate this strict has been found.

## First moves

1. Call the IT heads of the public bodies that published their records-system tender more than once, and ask why it had to run again. They are named under [Why now](#why-now). A body that is tendering again still has its budget and its deadline ahead of it. Listen to what went wrong with the last attempt, then offer to take the move to a certified system off their hands.
2. Build a migration service that moves a public body's records, every file and its history, off an uncertified system and onto a certified one. About a dozen Czech records systems still lack the certificate, as [Market gap](#competition) shows, and a body running one has to move before the date under [Why now](#why-now), unless its supplier is certified first. Three of the certified vendors already charge for the move inside their own contracts, as [Willing to pay](#willing-to-pay) shows, so sell the move, not another records system.
3. Open every conversation with the date and the fine, because both come straight from the law. They are under [Why now](#why-now). A body that is not ready does not need to be persuaded that it has a problem, only shown how the move gets done in time.
4. Offer the same migration work to the records-software vendors that do not hold a certificate yet. A certificate runs for two years and covers one version of one product, so even the certified vendors renew on a clock, and the uncertified ones must win a certificate or lose their public customers; see [Market gap](#competition). Either way, their customers' records have to end up in a certified system.
5. Don't compete on the price of the software, because the smallest towns can already get a records system free. That free system has the Interior Ministry behind it; see [Market gap](#competition). Sell the move and the help with the certificate, not the licence.

## Revisions

2026-08-24 · fact check — The supply-side ban was stated one notch too widely: §69e bans offering or supplying non-attested eSSL to public-law originators ("zákaz nabízet nebo dodávat veřejnoprávním původcům"), not from sale generally — verified live on the S1 commentary, and title and lead now say so [S1]. The procurement-wave arithmetic was re-counted mechanically against the signal corpus on this date: ~30 matching records, 19 distinct buyers, SÚRAO with four publications and Nemocnice Pardubického kraje with three, as stated [S2].

2026-08-25 · board-brief rewrite, then market check (one entry per date, so the two merge) — The body was rewritten to the builder-first template and the missing `Solved elsewhere:` lead-in was written: without it the Proven abroad section rendered as a bare comps ledger with no prose, and the body meanwhile claimed "no foreign analog is on file" while Documaster sat on that ledger. The paragraph now states what the one comparable proves — a national records-certification regime (Norway's Noark) turned into a product moat rather than a barrier — and keeps the honest limit that attestation this strict is otherwise a Czech construction. "How big" now carries arithmetic instead of a gesture: ~€17M across ten TED weeks annualises to roughly €90M of visible spend, with the individual awards (~€642k Interior support, ~€1.1M Lesy ČR, ~€408k Ostrava University) showing the spread and the sub-threshold tail named as unmeasured [S2,S4,S5,S6]. The open follow-up moved into the local-competition paragraph so it stops landing inside Proven abroad. Every source gained a public name and why line; scores, status and internal notes untouched. Flagged for MATCH, not changed: `scores.proof` is 0 while a funded foreign comparable (Documaster, NOK 100M from Summa Equity) sits on the comps ledger. Later the same day, the market check — the supply side was checked properly for the first time, in Czech and against the state's own list of issued attests. Four Czech suppliers hold one — GORDIC (GINIS, atest 1/2025), ICZ.DMS (e-spis, 2/2026), Seyfor (ELDAx, 3/2026) and MIT Consulting (MIT ERMS, 4/2026) — each attest running two years and tied to a product version; a dozen further Czech systems are not on the list, and OSS Alliance gives the smallest obce an open-source one free [S8]. "Existing non-solutions" now names all four rather than two. `scores.gap` was already 0 and stays 0; `status` moves candidate → watching under the SPEC §4 de-rank rule, which is what naming incumbents has always implied here. `score` is unchanged at 5. The supplier side of the contracts register was used as a second instrument: aggregating `data/lookup/cz-contract-parties.jsonl` by IČO over 3,984 suppliers shows GORDIC serving three distinct public buyers in one ingest window, Seyfor and GEOVAP two each, ICZ and ICZ.HEA one each — multi-buyer public suppliers, the incumbent signature. Flagged for verification, NOT acted on by that pass: Czech trade coverage in this scan describes an odklad and puts the hard line at 1 January 2027 rather than 31 December 2026, which touches the S1 deadline and needs checking against the statute. Later the same day, that flag was closed and the file re-scored under the rewritten SCORING.md.

THE DEADLINE, SETTLED. The trade coverage is right and this file was a day out. The Czech Agency for Standardization — the body that issues the attests — states in its own Q&A that a public-law originator must be running records management in an attested eSSL "nejpozději od 1. ledna 2027", citing the transitional provision in §27 of vyhláška č. 259/2012 Sb.; legal commentary read live on the same date gives 1 January 2027 as the end of the transitional period under §63 odst. 3 zákona č. 499/2004 Sb., with a fine up to 200,000 CZK from that day [S9]. The lead and "Who pays" now say "from 1 January 2027" instead of "by 31 December 2026", and the [S1] public summary line says the transitional period runs out at the end of 2026 rather than naming the wrong compliance date. Nothing was smoothed over: the same ČAS page carries a stale section giving 1 January 2026, an internal inconsistency on the issuing agency's own page, and [S9] records it. The [S1] internal note is untouched and remains correct as written — a period that ENDS 31 December 2026 and an obligation that BITES from 1 January 2027 are the same boundary. The urgency sub-scores do not move: the date is under eighteen months out either way, so deadline stays 2 and `scores.urgency` stays 3. The title, "by the end of 2026", survives the check unchanged.

THE RE-SCORE. `scores.proof` 0 → 2, resolving the contradiction flagged for MATCH earlier this same day. Documaster passes the ESTABLISHED test on three limbs at once — selling since 2014, a state certification (the first records kernel certified against Norway's Noark standard), growth equity from Summa Equity at NOK 100M, and revenue up more than fifteenfold since 2017. One established foreign player is rung 2 exactly. Rung 3 was considered and declined: it needs two-plus markets, and Norway is the only one on file, CEE-adjacent though the Nordics are. `scores.gap` stays 0, and now means TAKEN rather than the v1 rung's "check not done" — which is precisely the defect the owner caught, a page printing "not yet checked" above a list of four attested competitors. Seven local players were lifted out of the [S8] scan prose into a structured `locals[]` ledger. Six are established, four of them on the state-certification limb outright: GORDIC (atest 1/2025, and three distinct public buyers in `data/lookup/cz-contract-parties.jsonl`), ICZ.DMS (atest 2/2026, plus Prague's ~€3.3M e-spis award [S3]), Seyfor (atest 3/2026, plus two distinct public buyers) and MIT Consulting (atest 4/2026). GEOVAP is established on the public-buyer limb without an attest, and OSS Alliance on its Ministry-of-the-Interior arrangement. Only T-MAPY reads early on receipts alone. Founding years were verified in ARES on this date. `score` 5 → 7. The Proven-abroad paragraph now states Documaster's trading age and says plainly that it is one company in one country, because under the new ladder that is what caps the score. Money, urgency and demand untouched; no source note edited and no existing [Sn] marker moved — [S9] is appended, not inserted.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. THE OSS ALLIANCE QUESTION IS ANSWERED BY THE SPLIT, not compromised. Six entries convert without argument — GORDIC, ICZ.DMS, Seyfor and MIT Consulting are `direct` + `established` on their attests, GEOVAP on its public buyers, T-MAPY `direct` + `early`. OSS Alliance was this file's open interpretive problem: it was marked early with a note saying the test's letter and its spirit had come apart, because a free, state-backed, open-source offering cannot satisfy a "three years SELLING" limb at any age, while in spirit it was the strongest signal on the file that the space is taken at the bottom of the market. Two orthogonal fields dissolve that without splitting the difference. `competes` is now a separate question from maturity and its answer is plainly yes: OSS Alliance supplies the same product — an eSSL records system — to the same buyer, the smallest obce, at a price of zero. A price of zero is a price, not a different product, so it competes directly. `maturity` stays `early`, and stays early honestly: no sourced year for the start of supply is on file, so none is written and the years limb cannot be dated at all. That costs nothing, because `scores.gap` is 0 on the four attested vendors regardless — which is exactly why the two questions had to be separated. The entry now records what OSS Alliance is instead of describing a contradiction. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 7 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` and `data/register.db` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the buyers whose tenders keep republishing as the first customers [S2], migration off the dozen unattested Czech systems as the first build [S8], the 1 January 2027 date and its 200,000 CZK fine as the opening fact [S9], and the unattested vendors themselves as a second, recurring buyer [S1,S8]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Three trade terms glossed at first use: TED as the EU's public tender journal [S2], Lesy ČR as Czech State Forests, OSS Alliance as an open-source group; SÚRAO gained an appositive and NOK became plain Norwegian kroner. The argument went 442 to 367 words, First moves 286 to 183, with every [Sn] marker, figure, date and named vendor kept. A gist was added to all nine sources. No score, status, note or marker touched.

2026-09-10 · likely solution — Added the one-sentence `solution:`, now required on every record and always shown as the likely solution, compressed from First moves 2 and 5, the lead paragraph and the who-pays paragraph. No claim, score or source changed.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` telling the situation, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Czech public bodies must replace their records systems by the end of 2026". Previous solution, verbatim: "A migration service that moves a ministry, hospital or town hall off a records system without the state certificate onto a certified one before 1 January 2027, records and metadata intact." No brief or good_for existed before. Checked against the sources while writing. The title's "by the end of 2026" became "until January", counted from today: the obligation bites from 1 January 2027 [S9], a little over three months out. The old title also said bodies "must replace their records systems", which overstates it: a body already on one of the certified products does not have to replace anything, so the new title says they must move their records onto certified software. The fine of up to 200,000 CZK falls on the public body that is not compliant, which is who the brief names [S9]. The tender wave is stated as two facts side by side, 19 public bodies tendering for records software worth about €17M between June and August 2026 [S2], and not as caused by the deadline; the dek's "they are failing to close" was not carried over, because a re-published notice [S2] shows a re-run and not why. The certified field is held by four established Czech vendors (gap 0, status watching); the brief does not name them and the solution sells the move rather than another system. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Title before: "Czech public bodies have until January to move their records onto state-certified software" After: "Czech public bodies must keep records in state-certified software from January". Brief before: "From 1 January 2027, Czech ministries, hospitals, universities and other public bodies must keep official records in state-certified software or risk fines up to 200,000 CZK [S9]. This summer 19 of them tendered for records software worth about €17M [S2]." After: "Ministries, hospitals and universities that miss the date risk a fine [S9]. This summer 19 public bodies tendered for records software [S2]." Solution before: "Build a migration service that moves a public body's records from uncertified software into a certified system before January, every file and its history intact." After: "Build a migration service that moves a public body's records into certified software, every file and its history intact." Good for before: "Someone who can move data between office systems and sell through public tenders." After: "Someone who can migrate office data and sell through public tenders." The 1 January 2027 date moved to the headline as "from January" [S9]; the 200,000 CZK fine and the €17M were cut to keep one number, the 19 buyers [S2], who are named "public bodies" because not all are ministries, hospitals or universities. The tenders still sit beside the deadline, not as caused by it. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, each first list carries its three most important items, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the 1 January 2027 duty and explains the records service, the archives act, who counts as a public-law originator and what the certificate is [S1,S8,S9]. Competition opens on the four certified vendors and the free system for the smallest towns, and describes them without naming them: their names, certificate numbers, dates and buyers stay in their `locals[]` rows; the three uncertified systems that are not on the ledger (Munis, VERA Radnice, KEO4) are still named [S8]. Why now now opens on the pain, the fine and the re-published tenders, with the law dates below as plain bullets; the 200,000 CZK fine, which lived only in move 3, now has its home there [S9]. Willing to pay opens on what public bodies spend now and lists every award on file, adding the state drug agency's open competition [S2] and Prague's two development awards [S3,S7], which the body used to mention only as "winning the wave". Validated abroad became one answer sentence; the Norwegian company's founding year, funding and growth stay in its `comps[]` row. The moves lost every marker, figure and company name for links to the sections holding the evidence; move 1 now contacts the bodies whose tenders ran again instead of selling to them. `entry.why` was rewritten as "Easier: … Harder: …" and names the same gates (public buyer, the state certificate, money before revenue). Corrected against the sources rather than against the old sentences: "they are failing to close" and "a body on its fourth publication has … no bid" became "published its tender four times": a re-published notice shows the tender ran again, not why, and no source counts bids [S2]; "awards run from ~€408k to ~€1.1M" ignored Prague's ~€3.3M and ~€275k awards on file, so each award is now listed on its own [S3,S5,S6,S7]; the claim that one certificate covers one product version was cited to [S1], whose note does not say it, and is now cited to [S8], which does; "attestation this strict is otherwise a Czech construction" was cited to [S1], which covers only Czech law, so it now reads "no second country with a records certificate this strict has been found"; the Norwegian company's facts carried [S1] although no source on file backs them, so the body drops them for its `comps[]` row, whose traction line keeps its attribution, and "Oslo" is not repeated, since neither that row nor the company's own site (read 2026-09-18) states the city; and "GINIS and e-spis are winning the wave" became what the sources show, Prague buying development on both [S3,S7]. Flagged as inference: that a body on an uncertified system must move unless its supplier is certified first joins the duty [S9] to the list of certified products [S8]; "the certificate is scarce, not the software" is our reading of four certified products against about a dozen uncertified ones [S8]; that a body pays each year for support rests on the ministry's multi-year support contract [S4]; the roughly €90M a year is our arithmetic on ten weeks of tenders [S2]; and that the Norwegian certificate "can become the thing a seller builds on" is our reading of the company's growth on its `comps[]` row. Added from sources already on file: the health insurer's two publications [S2], the stale 1 January 2026 date on the agency's own page [S9], and the certificates being published by the Czech Agency for Standardization [S8]. No process block was added: this is a new duty with no documented step-by-step workflow in the sources. No score, status, source, `note:`, `sources[]` order, title, brief, solution, good_for or `entry` gate value changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Tagging pass first: every source on file was read for someone paying for this job, moving a public body's records, every file and its history, into certified software, and none is. The two awards the worksheet singled out were read at their own TED notices on this date. Ostrava University's buys the supply and implementation of a certified records system with support, training, development and exit services [S5]; the state forests' buys the supply and implementation of a records system tied into its other systems, awarded to a certified vendor at 27,771,072 CZK [S6]. Neither names moving the old records, so by the owner's rule, it counts only if it buys this job, neither is restated as a price. The rest buy the software, not the move: the drug agency's open competition [S2], Prague's two development awards [S3,S7] and the Interior Ministry's support contract [S4]. All six stay public money nearby. `scores.money` 2 → 0: no price receipt for the migration is on file, and public money nearby earns no point on its own. `scores.urgency` stays 3, now on the new ladder: the duty to keep records in a certified system from 1 January 2027 is enacted and binds the public body, it is 3.5 months out, and a fine of up to 200,000 CZK is named [S9]. `score` 7 → 5, FAIR unchanged. The notes on S1, S2 and S9 named retired rungs ("deadline sub-score 2", "open tender ≥5M CZK: money 2") and gained a dated rescore line, and S5 and S6 record the scope read; every original note is left as written. Three `[Competition](#competition)` links now read `[Market gap](#competition)`. Prose re-read against the new numbers. Willing to pay's answer was "Public bodies pay now: this summer they tendered about €17M for records systems, and one ministry bought years of support [S2,S4]." and now reads "Public bodies pay for records systems and support, about €17M tendered this summer, but they buy the software, not a move of old records [S2,S6]."; a detail bullet says what the two award notices buy [S5,S6]; and "So a body pays first to move onto a certified system" became "pays first for a certified system", since no source shows anyone paying for the move [S4]. Why now already leads on the 1 January 2027 date and the fine [S9] and stands. The `price_search:` line stays: a district town's migration cost is still the receipt to look for. No other score, status, source order, marker or headline field changed.

2026-09-19 · Willing to pay search, owner-approved — `scores.money` 0 → 2, `score` 5 → 7, band FAIR unchanged, `status` watching unchanged. The rescore above left one question open (worksheet call 9): do the Ostrava University and state-forests awards include moving the records? Both were read again, this time past the TED notice. The state forests' signed contract with its certified vendor, of 2 July 2026, prices stage 5, "preparation and handover into trial operation, data migration", at 483,700 CZK excluding VAT, and the vendor's offer moves the open files from the current system with their old file marks and reference numbers. It is restated as a price receipt tagged money [S10]. The earlier reading on this date, that it names no migration, held for the TED notice only, and S6's note gained a correction line. The stage also covers the handover into trial operation, so the figure is an upper bound on the move, and S10's note says so. Ostrava University did not award at all: its TED result notice reads that no winner was chosen and the competition ended, for technical or procedural errors, after three tenders [S5]. The ~€408k was the 10M CZK estimate. S5's name, gist and why said "award" and now say what happened; its note gained a correction line; and the body's "Ostrava University awarded about €408k for one, with service support" became the ended tender. A full-text search of the contracts register through the Hlídač státu API, three queries over the 24 months before `updated` plus both named buyers by IČO, found more of the same job, and ten contract texts were read [S12]. Fakultní nemocnice Plzeň signed on 28 July 2026 to move its records system onto the certified version, data migration to test and to production included, for 892,800 CZK excluding VAT, due by 30 November 2026 "so that it meets the duty" in the contract's own words. It is restated as a price receipt tagged money [S11]. Both receipts are signed contracts inside 24 months of `updated`, so money is 2 on its own; the tenders on file stay public money nearby, and no lift is needed. Positive control: the state forests' contract, found first by the buyer's and vendor's IČOs, surfaced on page 3 of the full-text query. Read and not restated: the Czech Mining Office's upgrade to the certified version, 1,403,376 CZK excluding VAT in June 2025, whose price table is blank in the register's text layer; Mělník's certified system, whose migration of records back to 2006 has its price blacked out; and Bulovka hospital's new system, whose migration has no price line of its own [S12]. Searched and NOT added as receipts: the Justice Ministry pays GRADUAL SYSTEMS by the man-day to move other offices' records into its ACTA system, 453,600 CZK in September 2024 and 190,400 CZK in June 2026. That is the migration service itself, bought separately, but ACTA is not on the attest list, re-read on this date with the same four products as [S8], so the records land in uncertified software: next door, not this job [S12]. The National Development Bank's export out of EZOP names no certified target, and ICZ.DMS moving data between databases or onto a file system inside one system is a technical move; both are in S12's note and neither counts. Ledger: GRADUAL SYSTEMS joins `locals[]` as adjacent and established: trading since 3 April 2007 in ARES, with the Justice Ministry a named customer under support contracts of 2024 and 2025. VITA software, paid by two public bodies to reconnect its own agenda software to the certified system, is named in S12's note and not added, because it does not move the records. Gap was already 0 on four certified vendors and stays 0; three of them now show paying customers for the move itself. `entry` is unchanged, incumbents stays direct. S12 carries `dims: []`: the amounts are restated as S10 and S11, and the row names who pays and who does the work. Body: Willing to pay's answer was "Public bodies pay for records systems and support, about €17M tendered this summer, but they buy the software, not a move of old records [S2,S6]." That is no longer true, and it now reads "Public bodies already pay to have their records moved into certified software, inside their contracts with the certified vendors [S12]." Its first three items are the state forests' priced stage, the hospital's and mining authority's own contracts for the move and the ministry's separate orders into uncertified software [S12]; the award list moved below as detail, with the state forests' award keeping its place and a line saying its notice does not mention the move but its contract does [S6,S12]. Market gap's second item is now that three certified vendors charge for the move [S12]; Prague's development awards moved into the paragraph below; and a bullet names the ministry's separate orders into a system without the certificate [S12]. Move 2 said "The certified vendors already sell the software, so sell the move" and now says three of them already charge for the move inside their own contracts, linking Willing to pay. Flagged as inference: that the whole of S11's 892,800 CZK buys the move rests on its price table carrying no licence line. Not changed: title, brief, solution, good_for, `price_search`, urgency, proof, demand, gap, `entry`.
