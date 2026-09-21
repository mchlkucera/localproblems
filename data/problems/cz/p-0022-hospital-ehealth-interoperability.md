---
id: p-0022
region: cz
title: 'Czech hospitals each pay millions for their own software to share patient data'
solution: 'Build integration software that plugs into a hospital''s systems and links them to other providers, as 2 companies already do in 2 other countries.'
brief: 'Hospital after hospital is buying its own software to share patient data, for up to 190M CZK [S1,S2,S3,S14,S15]. State auditors found the national version years behind [S6].'
good_for: 'Engineers who know hospital software and can wait out long public tenders.'
category: health
geo: CZ-national
score: 8
scores:
  proof: 3
  money: 2
  urgency: 1
  demand: 2
  gap: 0
status: watching
entry:
  level: very-hard
  buyer: public
  permission: registration
  incumbents: direct
  integration: national-system
  money: outside-money
  why: 'Easier: hospitals already buy integration in open tenders, they publish the message formats they want, and EU law requires exchangeable patient summaries from 2029. Harder: every sale is a public tender of €0.2M to €7.7M, seven established Czech vendors already sell it, and bidding costs money before any payment.'
comps:
- name: Redox
  url: https://www.redoxengine.com/
  geo: US
  since: 2014
  traction: '$95M raised (Tracxn); 450+ provider organizations plus hundreds of apps exchange
    data via its API platform (PRNewswire, 2022)'
- name: Better
  url: https://www.better.care/
  geo: SI
  since: 1989
  traction: '30M+ patients, 500+ hospitals in 15 countries on its openEHR platform (openEHR.org);
    NHS trusts, Karolinska, Basel'
  markets: [GB, SE, CH]
locals:
- name: STAPRO
  url: https://www.stapro.cz/
  ico: '13583531'
  since: 1990
  competes: direct
  maturity: established
  evidence: It sells FONS and TransMISE — hospital information systems plus an integration layer
    wired into the national eHealth contact point (NCPeH) [S8]. Trading since 1990, and KNTB Zlín,
    FN u sv. Anny, FN Olomouc and Kroměříž hospital all sign STAPRO amendments on the state contracts
    register [S5]. MMN, which runs the Semily hospital, signed its interoperability contract with
    STAPRO in April 2026 [S23], and Karlovarská krajská nemocnice signed its Karlovy Vary
    interoperability contract with STAPRO on 27 June 2026 [S27].
- name: ICZ (eMEDOCS)
  url: https://www.i.cz/
  ico: '25145444'
  since: 1997
  competes: direct
  maturity: established
  evidence: It sells eMEDOCS, a hospital data-exchange platform connected to the national eHealth
    contact point (NCPeH) [S8]. Trading since 1997, with customers including Český statistický
    úřad for ICZ a.s. and Nemocnice Břeclav for ICZ.HEA a.s. (IČO 07240091) on the state contracts
    register [S5].
- name: Medicalc (mEx)
  url: https://www.medicalc.cz/
  ico: '26350513'
  since: 2002
  competes: direct
  maturity: established
  evidence: It sells mEx, a hospital integration product carried on the state framework listing
    of systems connected to the national eHealth contact point (NCPeH) [S8]. Trading since 2002.
    Nemocnice Sokolov signed implementation, licence and service contracts with it on 31 August
    2026 for its eHealth-programme IT modernisation [S26].
- name: PHYSTER TECHNOLOGY
  url: https://www.physter.com/
  ico: '27091937'
  since: 2003
  competes: direct
  maturity: established
  evidence: It sells hospital integration on the same state framework listing of systems connected
    to the national eHealth contact point (NCPeH) [S8]. Trading since 2003.
- name: AutoCont (AC Pramen, ESB ACIB)
  url: https://www.autocont.cz/
  since: 1991
  competes: direct
  maturity: established
  evidence: It sells AC Pramen and the ESB ACIB service bus, both on the state framework listing
    of systems connected to the national eHealth contact point (NCPeH) [S8]. Trading since 1991.
- name: M.I.T. Consulting
  url: https://www.mitconsulting.cz/
  ico: '25689240'
  since: 1998
  competes: direct
  maturity: established
  evidence: It sells a hospital enterprise service bus, and holds the Czech records-management
    attest 4/2026 for MIT ERMS from the Czech Agency for Standardization [S8]. Trading since 1998.
- name: OR-CZ
  url: https://www.orcz.cz/
  ico: '48168921'
  since: 1993
  competes: direct
  maturity: established
  evidence: It sells hospital information-system integration, with customers including Psychiatrická
    léčebna Šternberk on the state contracts register [S11]. OR-CZ spol. s r.o. has traded since
    17 March 1993.
sources:
- type: tender
  name: "TED — Uherské Hradiště eHealth platform (~€7.7M)"
  gist: "the €7.7M Uherské Hradiště award"
  why: "A regional hospital bought a platform for provider-to-provider communication and data sharing in August 2026 — the largest single award in this wave."
  url: https://ted.europa.eu/en/notice/-/detail/549134-2026
  note: 'ted-549134-2026: Uherskohradišťská nemocnice awarded ~€7.7M to create an eHealth
    platform for provider-to-provider communication and data sharing (Aug 2026).'
  date: '2026-08-07'
  signal: ted-549134-2026
- type: tender
  name: "TED — Plzeň hospital group, NIS with ESB (~€5.8M)"
  gist: "the open €5.8M Plzeň tender"
  why: "The Plzeň region's hospital group ran an open competition for a hospital information system with an enterprise service bus and integrations."
  url: https://ted.europa.eu/en/notice/-/detail/476712-2026
  note: 'ted-476712-2026: Nemocnice Plzeňského kraje group tendering NIS + ESB + integrations,
    OPEN competition ~€5.8M (Jul–Aug 2026). Open tender ≥5M CZK: money scored 2. Superseded
    2026-09-19: an open tender is public money nearby and earns no point on the new ladder; it
    names no award, and it bundles a whole hospital information system. Money now rests on the
    awarded lines restated as [S21] and [S22].'
  date: '2026-07-10'
  signal: ted-476712-2026
- type: tender
  name: "TED — Zlín KNTB hospital system (~€2.8M)"
  gist: "the €2.8M Zlín award"
  why: "Zlín's regional hospital bought a hospital information system with integration scope; FN Olomouc bought eHealth interoperability (~€0.7M) in the same weeks."
  url: https://ted.europa.eu/en/notice/-/detail/443904-2026
  note: 'ted-443904-2026: Krajská nemocnice T. Bati (Zlín) awarded ~€2.8M for a hospital information
    system incl. integrations (Jun 2026); FN Olomouc bought eHealth interoperability (~€0.7M)
    in the same window — ≥4 distinct regional buyers in ten weeks.'
  date: '2026-06-29'
  signal: ted-443904-2026
- type: contract
  name: "Registr smluv — Karlovy Vary hospital (~70.9M CZK)"
  gist: "the 70.9M CZK Karlovy Vary contract"
  why: "The regional hospital signed for hospital-system delivery and support, alongside a wave of psychiatric-hospital system contracts in the same weeks."
  url: https://smlouvy.gov.cz/smlouva/38551596
  note: 'hlidac-38551596: Karlovarská krajská nemocnice signed ~70.9M CZK for NIS delivery
    + service support (registr smluv, 27 Jun 2026); same weeks show a psychiatric-hospital
    NIS wave — PN Horní Beřkovice (~9.7M + 8.1M support), DPN Opařany (~9.3M), PN Marianny
    Oranžské (~6.0M). With TED that''s 8+ distinct public buyers re-solving the same integration
    problem in one summer.'
  date: '2026-06-27'
  signal: hlidac-38551596
- type: contract
  name: "Registr smluv — STAPRO amendment churn"
  gist: "the incumbent's amendment churn"
  why: "Price-increase amendments signed the same day, extended works deadlines and an integration platform on its eighth amendment — what buying integration from the incumbent costs after signature."
  url: https://smlouvy.gov.cz/smlouva/38419070
  note: 'hlidac-38419070: KNTB Zlín signed STAPRO NIS-service amendments No. 1 and No. 2 the
    same day — both price increases (~2.8M CZK, Jun 2026). The same weeks: FN u sv. Anny extended
    a STAPRO works deadline (hlidac-38592936), FN Olomouc signed amendment No. 3 on its NIS
    works (hlidac-38869946), and Kroměříž hospital signed amendments No. 7 and No. 8 on its
    STAPRO integration platform within a month (hlidac-38657096, hlidac-38954950). Incumbent
    lock-in repricing and permanent change-request mode, documented in the open — buyer-side
    cost pain supporting the demand point.'
  date: '2026-06-17'
  signal: hlidac-38419070
  dims:
  - demand
- type: complaint
  name: "NKÚ — digitalisation of Czech healthcare"
  gist: "the state audit's six-year delay"
  why: "The state audit office finds health-data sharing and eŽádanka six years late and legally required registries still missing — the national layer hospitals are waiting for does not exist."
  url: https://www.zdravotnickydenik.cz/2026/01/digitalizace-ceskeho-zdravotnictvi-nku/
  note: 'nku-ehealth-delay: NKÚ''s II. summary digitalization report (Jan 2026) documents
    health-data sharing and eZádanka six years late (2020 plan → 2026 at the earliest), core
    health registries required by law still missing as of early 2023, and 158M CZK spent on
    e-health strategic goals 2020-2024 with infrastructure absent. State-audit receipt that
    the national interop layer hospitals are waiting for does not exist — demand scored 1
    (authoritative single-body documentation, not yet recurring buyer complaints).'
  date: '2026-01-31'
  signal: nku-ehealth-delay
- type: regulation
  name: "European Health Data Space — Regulation (EU) 2025/327"
  gist: "the law and its 2029 deadline"
  why: "Sets the legal end state: cross-border patient summaries and ePrescription from 2029, imaging and discharge data from 2031, with conformity duties landing on the Czech hospital-system vendors."
  url: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
  note: 'reg-ehds: EHDS Regulation (EU) 2025/327 in force since Mar 2025; implementing acts
    due Mar 2027; cross-border primary use (patient summaries, ePrescription) and most secondary-use
    rules apply from Mar 2029, imaging/labs/discharge categories 2031. Dated obligations >18
    months out: deadline sub-score 1. Rescored 2026-09-19: on the new ladder a dated duty more
    than 18 months out is Why now 1, and with the freshness point retired that is the whole
    score. EHR-system conformity requirements will hit the CZ vendor
    ecosystem (Stapro, ICZ, CGM) directly.'
  date: '2029-03-26'
  signal: reg-ehds
- type: gap-check
  name: "Czech hospital integration products"
  gist: "the six named Czech vendors"
  why: "A sweep of the Czech field naming what already exists — Medicalc mEx, PHYSTER, Stapro FONS/TransMISE, ICZ eMEDOCS, AutoCont's ESB ACIB and M.I.T. Consulting's hospital bus."
  url: https://www.zdravotnickydenik.cz/2026/01/medicalc-meni-fungovani-nemocnic-jan-kupka/
  note: 'Gap check 2026-08-13: CZ integration-platform products DO exist — Medicalc mEx, PHYSTER
    TECHNOLOGY, Stapro FONS/TransMISE, ICZ eMEDOCS/ISAC, AutoCont AC Pramen/ESB ACIB are NCPeH-connected
    integration offerings, and M.I.T. Consulting sells a hospital ESB. The field is not empty:
    local players named, gap stays 0 and status moves to watching per the de-rank rule. The
    residual question is why 8+ buyers still procure bespoke multi-million integration builds
    despite these products — vendor-neutrality and coverage, not absence.'
  date: '2026-08-13'
- type: contract
  name: "Registr smluv — Motol/Homolka health-IT licences and support (~€11.7M)"
  gist: "the €11.7M Prague mega-buyer"
  why: "Prague's merged mega-buyer signed a health-IT licence expansion and a support services deal on the same day — €11.7M of incumbent-stack spend from a single buyer in one August week."
  url: https://smlouvy.gov.cz/smlouva/39006306
  note: 'hlidac-36661862 + hlidac-36661866: FN Motol a Homolka signed a framework health-IT
    software licence expansion (~€5.77M) and a health-IT support services contract (~€5.93M)
    on 4 Aug 2026 (registr smluv 39006306, 39006310) — the largest hospital buyer in the
    2026-08-25 retrospective harvest (46 contracts, incl. a ~€7.3M cybersecurity detection
    framework already receipted on p-0008 via ted-373331-2026). Corroborates the per-hospital
    incumbent-stack spend this record describes; backs no new score point — money already
    rests on the open Plzeň tender [S2]. Superseded 2026-09-19: money now rests on the awarded
    lines [S21] and [S22]; this contract buys health-IT licences and support, not the
    data-sharing layer, so it stays untagged.'
  date: '2026-08-04'
  signal: hlidac-36661862
  dims: []
- type: regulation
  name: "VeKLEP — e-health act amendment in draft"
  gist: "the e-health act in redraft"
  why: "The Health Ministry is amending Act 325/2021 Coll., the national e-health law — the legal frame behind the missing national layer is itself in motion."
  url: https://odok.cz/portal/veklep/material/ALBSDVLDLD32/
  note: 'veklep-ALBSDVLDLD32: ministry bill amending zákon č. 325/2021 Sb. o elektronizaci
    zdravotnictví, filed to VeKLEP 3 Jul 2026 (first VeKLEP harvest, 2026-08-25). Draft with
    no dated obligation yet: context receipt for the why-now, backs no score dimension.'
  date: '2026-07-03'
  signal: veklep-ALBSDVLDLD32
  dims: []
- type: gap-check
  name: "Czech hospital integration supply — coverage recorded"
  gist: "the Czech-language supply sweep"
  why: "The 2026-08-13 sweep named the Czech integration vendors but never wrote down what was searched. This one does, and it surfaces one more: OR-CZ, which sells IS integration to hospitals alongside Stapro, ICZ, Medicalc, PHYSTER and AutoCont."
  note: 'Coverage receipt 2026-08-25. The [S8] scan named real incumbents but recorded no
    queries, so gap 0 rested on a check whose reach nobody could judge; this entry supplies
    the coverage rather than a new verdict. Czech-language search for hospital integration
    platforms and enterprise service buses returned, on the first page: OR-CZ (orcz.cz/integrace),
    a Czech vendor selling information-system integration to hospitals that [S8] did not name;
    STAPRO''s own contract documents in registr smluv; Krajská nemocnice T. Bati''s own
    "Integrační platforma eHealth" procurement, which describes exactly the bespoke build this
    file is about; FN Olomouc''s eHealth-and-interoperability programme page; and technical
    specifications requiring an ESB inside the integration layer, exchanging HL7 and DASTA.
    POSITIVE CONTROL PASSED: STAPRO, the incumbent [S5] and [S8] already name, surfaced
    unprompted at the top of a plain descriptive Czech query — the method produces positives
    before any conclusion is drawn from it. NOTHING RESCORED. gap was already 0 and stays 0 on
    the established players in locals[]; OR-CZ is added to the picture, not to the score, and
    is left out of locals[] because no limb of the established test is receipted for it here.'
  url: https://www.orcz.cz/integrace
  date: '2026-08-25'
  queries:
    - "integrační platforma pro nemocnice český dodavatel propojení nemocničních systémů eHealth sběrnice"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-23'
- type: tender
  name: "TED — Petrohrad psychiatric hospital eHealth system (~€206K)"
  gist: "the Petrohrad eHealth award"
  why: "A psychiatric hospital tendered its own eHealth medical information system — another
    named buyer procuring bespoke software rather than a shared layer."
  url: https://ted.europa.eu/en/notice/-/detail/589279-2026
  note: 'ted-589279-2026: Psychiatrická léčebna Petrohrad tendered an eHealth medical
    information system, ~€206K (5,158,000 CZK), Aug 2026 — no supplier named. Republished
    2026-08-31 at the same value as ted-597290-2026, not separately cited. Re-announced again
    on 2026-09-14 as ted-631085-2026, same procedure identifier (6307d460-...), no value
    stated, bids due 15 Oct 2026; read from the TED search API on 2026-09-19, the description
    names interoperability and a secure link to the outside environment. Not separately cited.'
  date: '2026-08-26'
  signal: ted-589279-2026
- type: tender
  name: "TED — Mladá Boleslav hospital NIS modernization, STAPRO (~€2.9M)"
  gist: "the €2.9M Mladá Boleslav award"
  why: "The incumbent STAPRO won another hospital's NIS modernization outright — one more
    named buyer paying for a bespoke build rather than a shared product."
  url: https://ted.europa.eu/en/notice/-/detail/592268-2026
  note: 'ted-592268-2026: Oblastní nemocnice Mladá Boleslav awarded STAPRO [S5] ~€2.9M
    (72.4M CZK) to modernize and develop its hospital information system (NIS), Aug 2026.
    Republished the next day at a marginally revised value as ted-596098-2026, not
    separately cited.'
  date: '2026-08-27'
  signal: ted-592268-2026
- type: tender
  name: "TED — Revmatologický ústav eHealth and interoperability re-tender, STAPRO (~€1.11M)"
  gist: "the repeat €1.11M Prague award"
  why: "A repeat award for 'eHealth and interoperability' work, won again by the incumbent
    STAPRO — a tender in the very words of this problem."
  url: https://ted.europa.eu/en/notice/-/detail/598479-2026
  note: 'ted-598479-2026: Revmatologický ústav v Praze re-tendered "eHealth a
    interoperabilita" — repeat award — to STAPRO [S5], ~€1.11M (27.76M CZK), Aug 2026.
    Matches the amendment-churn pattern [S5] already documents: the same hospital paying
    the same incumbent again for the same kind of work.'
  date: '2026-08-31'
  signal: ted-598479-2026
- type: tender
  name: "TED — Náchod hospital PACS and eHealth platform, OR-CZ (~€293K)"
  gist: "OR-CZ's second named buyer"
  why: "OR-CZ, the seventh established Czech vendor named here, won a system explicitly built for
    exchanging data between providers, patients and information systems — a second named
    public buyer for it beyond Šternberk."
  url: https://ted.europa.eu/en/notice/-/detail/599893-2026
  note: 'ted-599893-2026: Oblastní nemocnice Náchod awarded OR-CZ [S11] a PACS imaging
    system as part of an eHealth platform "for communication, exchange and sharing of
    information between healthcare providers, patients and information systems," ~€293K,
    second re-announcement of the same notice, Sep 2026.'
  date: '2026-09-01'
  signal: ted-599893-2026
- type: regulation
  name: "EU Commission — HealthData@EU technical framework (draft)"
  gist: "the HealthData@EU implementing step"
  why: "A more granular EU regulatory step inside the same EHDS obligation already on file,
    setting the technical rules for cross-border secondary use of health data."
  url: https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16155
  note: 'echys-16155: European Commission initiative (have-your-say/consultation stage,
    not yet adopted), 1 Sep 2026, setting the technical and functional framework for
    HealthData@EU — cross-border secondary-use infrastructure under EHDS [S7] — plus an
    IT tool for enforcement transparency among national health data bodies. Draft, no new
    dated deadline: backs no score dimension.'
  date: '2026-09-01'
  signal: echys-16155
  dims: []
- type: tender
  name: "TED — Masaryk Memorial Cancer Institute eHealth package (~€3M)"
  gist: "the €3M Masaryk Institute award"
  why: "A major Czech cancer hospital tendered its own eHealth software package — another
    named buyer solving this alone, at meaningful scale."
  url: https://ted.europa.eu/en/notice/-/detail/604583-2026
  note: 'ted-604583-2026: Masarykův onkologický ústav tendered an eHealth medical software
    package, ~€3M (75M CZK), Sep 2026 — no supplier named.'
  date: '2026-09-02'
  signal: ted-604583-2026
- type: price
  url: https://smlouvy.gov.cz/smlouva/38419070
  name: "KNTB Zlín — two price rises in one day"
  gist: "about 2.8M CZK of amendments"
  why: "A regional hospital signed two same-day price increases worth about 2.8M CZK on its hospital-system service contract, which is what buying integration from the vendor already inside costs."
  note: 'Price receipt drawn from the contract already on this ledger (hlidac-38419070, KNTB
    Zlín, STAPRO NIS-service amendments No. 1 and No. 2 signed the same day, both price
    increases, ~2.8M CZK, Jun 2026). No annual term stated, so one-off. dims omitted: the
    existing source keeps its demand tag and this receipt backs no score.'
  date: '2026-06-17'
  payer: 'Krajská nemocnice T. Bati, Zlín'
  amount_czk: 2800000
  unit: one-off
  basis: signed-contract
- type: subsidy
  name: "IROP calls 78 and 79 — eHealth, about 2.1bn CZK, open to 2 December 2026"
  gist: "the 2.1bn CZK eHealth calls"
  why: "Two open state eHealth grant calls pay a named list of Czech hospitals, psychiatric hospitals and regional ambulance services for electronic health services, alongside the recovery plan's interoperability programme. Up to 28M CZK per provider; applications close on 2 December 2026."
  url: https://irop.gov.cz/cs/vyzvy-2021-2027/vyzvy/79vyzvairop
  note: 'dotace-irop-78-79-ehealth (dotace-scan, 2026-09-18), linked in MATCH 2026-09-18.
    Call 78 (06_23_078): ERDF 401,076,529 CZK + state budget 70,778,211 CZK = 471,854,740 CZK;
    call 79 (06_23_079, transition regions): ERDF 1,144,629,052 CZK + state budget 490,555,308
    CZK = 1,635,184,360 CZK; together 2,107,039,100 CZK (call texts "Text 78/79 výzvy eHealth k
    26. 5. 2026", irop.gov.cz; totals match the MS2021+ XML). Cap per healthcare provider 9.5M
    CZK (78) and 28M CZK (79), 5M CZK per ambulance service. Eligible: an enumerated list of
    named providers and regional ambulance services plus their founders. Continuous calls,
    applications 28 Nov 2023 14:00 to 2 Dec 2026 14:00. The call text names NPO component 1.1
    reform 2, eHealth interoperability II, as complementary. Applicant-level support rate not
    read (it sits in the consolidated specific rules). WHY MONEY: an open grant far above 5M CZK
    for eHealth work at named hospitals; money was already 2 on S2 and does not move. Superseded
    2026-09-19: on the new ladder this is public money nearby, which only lifts an asking price;
    money 2 now rests on the paid awards [S21] and [S22], so the lift is not needed. WHAT IT IS
    NOT: it pays the hospital, not a vendor, and the signal names no integration line item.'
  date: '2026-12-02'
  signal: dotace-irop-78-79-ehealth
  dims: [money]
- type: complaint
  name: "NKÚ audit 25/14 — IKEM bought IT through 345 small orders"
  gist: "IKEM's untendered IT orders"
  why: "The state audit office found that IKEM — Prague's institute of clinical and experimental medicine — paid three IT suppliers 59.5M CZK through at least 345 orders without a tender, and broke procurement law in half of the 30 contracts it checked."
  url: https://www.nku.cz/assets/kon-zavery/k25014.pdf
  note: 'nku-ikem-hospodareni (demand-scan, 2026-09-18), linked in MATCH 2026-09-18. NKÚ
    audit conclusion 25/14, approved 17 Aug 2026, published 14 Sep 2026: 30 contracts worth
    578.7M CZK checked, law broken in 15 worth 380.1M CZK; 59.5M CZK paid for IT services to
    three suppliers on at least 345 orders without a tender. From the conclusion PDF, read in
    MATCH 2026-09-18 (sections 4.4.1 to 4.4.3): after a closed marketplace procedure with one
    supplier, IKEM placed every follow-up order for developing and maintaining 13 applications
    with it, 189 orders each under 150,000 CZK excluding VAT, more than 31M CZK in 2022 to 2024;
    a second application supplier got 109 such orders, more than 20M CZK; cyber-security
    services ran on at least 47 orders, almost 8M CZK. CONTEXT ONLY, dims empty: the audit
    names no integration or data-sharing software, so it documents how one hospital buys
    software from the supplier already inside, not the interoperability pain itself.'
  date: '2026-09-14'
  signal: nku-ikem-hospodareni
  dims: []
- type: price
  url: https://ted.europa.eu/en/notice/-/detail/549134-2026
  name: "Uherské Hradiště — the eHealth platform award"
  gist: "about 189M CZK for one hospital"
  why: "A regional hospital awarded about 189M CZK in August 2026 for a platform to exchange and share patient information with other providers."
  note: 'Price receipt drawn from the tender already on this ledger [S1] (ted-549134-2026),
    added in the 2026-09-19 tagging pass. Awarded notice, buyer Uherskohradišťská nemocnice
    a.s.; value 189,163,478 CZK, read from the TED search API (result-value-notice, currency
    CZK) on 2026-09-19, which is the 189.2M CZK the 2026-08-24 fact check recorded and the
    ~€7.72M in the signal. It buys an eHealth platform for communication, exchange and sharing
    of information between providers: this job, awarded within 24 months. No term stated, so
    one-off.'
  date: '2026-08-07'
  payer: 'Uherskohradišťská nemocnice a.s., a regional hospital'
  amount_czk: 189163478
  unit: one-off
  basis: tender-line
  dims: [money]
- type: price
  url: https://ted.europa.eu/en/notice/-/detail/598479-2026
  name: "Revmatologický ústav — eHealth and interoperability, awarded again"
  gist: "about 27.8M CZK, a repeat award"
  why: "Prague's rheumatology institute awarded about 27.8M CZK in August 2026 for eHealth and interoperability work, in a repeat award to the vendor it already paid."
  note: 'Price receipt drawn from the tender already on this ledger [S14] (ted-598479-2026),
    added in the 2026-09-19 tagging pass. Repeat award of "eHealth a interoperabilita
    Revmatologického ústavu v Praze – opakované zadání" to STAPRO s. r. o. (IČO 13583531);
    buyer Revmatologický ústav (IČO 00023728); 27,756,514 CZK as the signal records it
    (converted there to ~€1.11M at a fixed 25.0 CZK/EUR). The tender names this job in its
    title, awarded within 24 months. No term stated, so one-off.'
  date: '2026-08-31'
  payer: 'Revmatologický ústav, Prague''s rheumatology institute'
  amount_czk: 27756514
  unit: one-off
  basis: tender-line
  dims: [money]
- type: tender
  name: "TED — Semily hospital interoperability, deadline extended over the state's e-health centre"
  gist: "the Semily contract delay"
  why: "MMN, a hospital company based in Jilemnice, extended its Semily hospital's April 2026 interoperability contract because the Health Ministry's national e-health centre had not cooperated on testing the hospital's connection to the national system."
  url: https://ted.europa.eu/en/notice/-/detail/633755-2026
  note: 'ted-633755-2026, read 2026-09-19 from the TED search API and the notice XML. A
    contract-modification notice (can-modif, published 15 Sep 2026) on "Interoperabilita v
    Nemocnici Semily", buyer MMN, a.s. (IČO 05421888), supplier STAPRO s. r. o. (IČO
    13583531), awarded 10 Apr 2026, contract signed 13 Apr 2026, original notice
    272969-2026. Scope: modernising the hospital information system with provider-to-provider
    information exchange, interoperability, connection to the national health information
    system (NZIS) and central registries, and integration links to external systems.
    Modification: amendment No. 1 extends the completion date. Stated reason, verbatim in
    part: "nesoučinnost Ministerstva zdravotnictví, respektive Národního centra elektronického
    zdravotnictví, které zajišťuje testování napojení systému Nemocnice Semily do ekosystému
    interoperability". Co-financed by the National Recovery Plan (RRF), project
    CZ.31.1.0/0.0/0.0/23_088/0011020. Subcontracted share, per the notice''s subcontracting value and description fields, 4,576,440 CZK for a patient portal,
    telemetry, a master patient index, a document repository, code lists, an ESB with the
    national central-services connection and an audit log. WHY demand: a buyer''s own filing
    that the state layer held up its integration; it supports demand 1 and does not lift it.
    The price is restated as [S24].'
  date: '2026-09-15'
  signal: ted-633755-2026
  dims: [demand]
- type: price
  url: https://ted.europa.eu/en/notice/-/detail/633755-2026
  name: "MMN Semily — the interoperability award"
  gist: "about 10.9M CZK for one hospital"
  why: "The company running the Semily hospital awarded about 10.9M CZK in April 2026 for interoperability work, including links to other providers and the national health information system."
  note: 'Price receipt drawn from [S23] (ted-633755-2026). Result value 10,877,401.33 CZK
    excluding VAT, read from the notice XML on 2026-09-19. The notice''s price note splits it:
    7,411,169.33 CZK to deliver and implement the upgraded hospital system, plus 3,466,232 CZK
    of service for four years (the contract runs indefinitely); the tender price, with 120
    months of service, was 13,576,749.33 CZK. Awarded 10 Apr 2026 to STAPRO, within 24 months.
    The title names this job and the scope includes provider-to-provider exchange and
    integration links; it also bundles the hospital-system upgrade, which is stated here, not
    hidden. Money was already 2 on [S21] and [S22] and does not move.'
  date: '2026-04-10'
  payer: 'MMN, a.s., for Nemocnice Semily'
  amount_czk: 10877401
  unit: per-project
  basis: tender-line
  dims: [money]
- type: tender
  name: "TED — Olomouc military hospital interoperability, re-announced (~7.3M CZK)"
  gist: "the Olomouc military re-tender"
  why: "The military hospital in Olomouc re-announced its interoperability tender in September 2026, with no supplier named."
  url: https://ted.europa.eu/en/notice/-/detail/624897-2026
  note: 'ted-624897-2026, read 2026-09-19 from the TED search API. Contract notice
    (cn-standard), Vojenská nemocnice Olomouc (IČO 60800691), "Interoperabilita ve Vojenské
    nemocnici Olomouc – opakované vyhlášení", estimated 7,334,800 CZK. Scope: modernising the
    hospital information system by extending its functions, one lot, service excluded. The
    title says re-announced; why the first call ended is not on file. An estimate, not a paid
    price, so it is not a price receipt.'
  date: '2026-09-10'
  signal: ted-624897-2026
- type: tender
  name: "TED — Sokolov hospital eHealth II modernisation, Medicalc (~12.9M CZK)"
  gist: "the Sokolov eHealth award"
  why: "Sokolov's hospital awarded an eHealth-programme modernisation of its internal IT to an established Czech hospital-software vendor in August 2026."
  url: https://ted.europa.eu/en/notice/-/detail/634231-2026
  note: 'ted-634231-2026, read 2026-09-19 from the TED search API and the notice XML.
    Award notice, Nemocnice Sokolov s.r.o. (IČO 24747246), "Modernizace vnitřního IT
    prostředí - eHealth II.", open procedure, lowest price, winner Medicalc software s.r.o.
    (IČO 26350513), 12,856,500 CZK, awarded 23 Jul 2026, implementation, licence and service
    contracts signed 31 Aug 2026. The notice describes only "modernizace nemocnice v rámci
    programu eHealth" and states no data-sharing or integration scope, so it is not restated
    as a price for this job. Context only: a named hospital customer for a local on file.'
  date: '2026-09-15'
  signal: ted-634231-2026
  dims: []
- type: tender
  name: "TED — Karlovy Vary hospital interoperability, waiting on the state's e-health centre"
  gist: "the Karlovy Vary interoperability award"
  why: "Karlovy Vary's regional hospital finished and took over its interoperability work in August 2026, but the health ministry's e-health centre had still not confirmed the hospital was connected, so the date for that confirmation was moved to the end of 2026."
  url: https://ted.europa.eu/en/notice/-/detail/647371-2026
  note: 'ted-647371-2026, read 2026-09-21 from the TED search API. Contract-modification
    award notice (can-modif), published 21 Sep 2026, "Interoperabilita v nemocnici Karlovy
    Vary, KKN a.s.", buyer Karlovarská krajská nemocnice a.s. (IČO 26365804), supplier
    STAPRO s. r. o. (IČO 13583531), contract concluded 27 Jun 2026, result value
    58,559,999.6 CZK, previous notice 459607-2026. SCOPE, verbatim in part: the systems are
    changed "tak, aby došlo ke zlepšení způsobu vedení zdravotnické dokumentace umožňující
    její interoperabilní výměnu, sdílení, bezpečné uložení a interpretaci", with data
    interfaces for standardised exchange of medical records between providers over national
    or regional infrastructure linked to the national eHealth contact point (NCPeH),
    interfaces to e-health services, registries and central eGovernment services, online
    access for authorised people, and the identifiers the e-health act requires. It is not
    a new hospital information system but an extension and integration of the one in place.
    MODIFICATION, verbatim in part: the work was "dne 25. 8. 2026 řádně dokončeno, předáno
    a převzato bez vad a nedodělků", production running and service support started the
    same day, but the "Potvrzení MZ ČR / NCEZ o úspěšném napojení do ekosystému
    interoperability" had not been issued "z důvodů na straně třetí osoby"; the parties set
    31 Dec 2026 as the new date for producing it. Justification code mod-cir. WHY demand: a
    SECOND named hospital buyer filing that the health ministry''s national e-health centre
    step held up its interoperability project, after Semily''s [S23] earlier the same year;
    with the state audit [S6] and the amendment churn [S5] the complaints are recurring
    rather than single, which is demand 2. IT ALSO RESOLVES WHAT [S4] COULD NOT SHOW: the
    contracts register entry 38551596, read 2026-09-21, is the same contract — "Smlouva o
    dílo a poskytování servisní podpory SM-AS008841", concluded 27 Jun 2026, counterparty
    STAPRO s. r. o., 58,559,999.60 CZK excluding VAT and 70,857,599.52 CZK including it,
    procurement reference Z2026-021431 — so the ~70.9M CZK [S4] records is this
    interoperability contract, not a hospital system with no data-sharing scope. The price
    is restated as [S28].'
  date: '2026-09-21'
  signal: ted-647371-2026
  dims: [demand]
- type: price
  url: https://ted.europa.eu/en/notice/-/detail/647371-2026
  name: "Karlovy Vary — the interoperability contract"
  gist: "about 58.6M CZK for one hospital"
  why: "The Karlovy Vary regional hospital signed about 58.6M CZK in June 2026 for work that lets its medical records be exchanged and shared with other providers."
  note: 'Price receipt drawn from [S27] (ted-647371-2026). Result value on the notice
    58,559,999.6 CZK, truncated here to whole crowns, read from the TED search API on
    2026-09-21; the contracts register gives the same contract as 58,559,999.60 CZK
    excluding VAT and 70,857,599.52 CZK including it (smlouvy.gov.cz/smlouva/38551596, read
    the same day), which is the ~70.9M CZK already on file as [S4]. Concluded 27 Jun 2026
    with STAPRO, within 24 months. The title and scope name this job — interoperable
    exchange and sharing of medical documentation between providers over the national
    eHealth contact point — and the contract also carries service support, which is stated
    here, not hidden. Money was already 2 on [S21] and [S22] and does not move.'
  date: '2026-06-27'
  payer: 'Karlovarská krajská nemocnice a.s., the Karlovy Vary regional hospital'
  amount_czk: 58559999
  unit: per-project
  basis: tender-line
  dims: [money]
- type: regulation
  name: "EHDS dataset descriptions — Implementing Regulation (EU) 2026/2098"
  gist: "the 2029 metadata duty"
  why: "From 26 March 2029 every holder of health data, hospitals included, must describe the data it holds in one machine-readable European format."
  url: https://eur-lex.europa.eu/eli/reg_impl/2026/2098/oj
  note: 'reg-ehds-metadata-drzitele-dat-2029 (reg-scan, 2026-09-21). Commission
    Implementing Regulation (EU) 2026/2098 of 18 September 2026, published in the OJ of 21
    September 2026, in force on the twentieth day after publication (11 Oct 2026) and
    applying from 26 March 2029. Article 3 requires health data holders to provide the
    Part B minimum metadata elements for their dataset descriptions using the definitions,
    structure, cardinalities and controlled vocabularies of HealthDCAT-AP; Article 1(2)
    extends it to authorised participants in HealthData@EU. It implements Article 77(4) of
    the EHDS Regulation (EU) 2025/327 already on file as [S7], and the duty falls on Czech
    hospitals as data holders and on the vendors whose systems must emit the catalogues.
    WHY NOTHING MOVES: the application date is more than 18 months after `updated`, so it
    fails CLOSE exactly as [S7] does, and Why now stays 1. The sibling act published the
    same day, Reg. (EU) 2026/2083 on MyHealth@EU, places its duties on national contact
    points rather than on hospitals and is not recorded.'
  date: '2029-03-26'
  signal: reg-ehds-metadata-drzitele-dat-2029
created: '2026-08-13'
updated: '2026-09-21'
---

Czech hospitals each buy their own software to link their systems and share patient data, one tender at a time [S1,S3].

- Uherské Hradiště's hospital awarded about €7.7M for a data-sharing platform in August 2026 [S1].
- Plzeň's hospital group tendered about €5.8M for a hospital system with integrations [S2].
- Zlín and Olomouc bought systems and interoperability work for about €2.8M and €0.7M [S3].

The layer they buy lets a hospital's own systems talk to each other and to outside providers [S1,S2]. Between June and August 2026, four regional hospital groups went to market for it separately [S1,S3].

- Uherské Hradiště's platform is for communication and data sharing between healthcare providers [S1].
- Plzeň's tender asks for an enterprise service bus, the switchboard that routes messages between clinical systems, plus the integrations around it [S2].
- Zlín's regional hospital bought a hospital information system with integrations included, and Olomouc's university hospital bought eHealth interoperability work in the same weeks [S3].
- Published hospital specifications ask for the same thing: a service bus inside the integration layer, exchanging messages in HL7 and DASTA (the two health-data formats Czech hospitals run on) [S11]. Zlín's own tender for an eHealth integration platform describes exactly such a one-off build [S11].

More hospitals followed in August and September 2026:

- Psychiatrická léčebna Petrohrad, a psychiatric hospital, tendered its own eHealth medical information system for about €206K, with no supplier named [S12].
- Mladá Boleslav's regional hospital awarded about €2.9M to modernise and develop its hospital information system [S13].
- Revmatologický ústav, Prague's rheumatology institute, awarded "eHealth and interoperability" work for about €1.11M, in a repeat award to the vendor it already paid for this work [S14].
- Náchod's regional hospital awarded about €293K for an imaging system, part of an eHealth platform for exchanging information between providers, patients and information systems [S15].
- Masarykův onkologický ústav, Brno's cancer institute, tendered an eHealth software package for about €3M, with no supplier named [S16].
- Olomouc's military hospital re-announced its interoperability tender in September 2026, estimated at about 7.3M CZK, with no supplier named [S25].
- Semily's hospital signed for interoperability work in April 2026, including links to other providers and to the national health information system [S23].
- Karlovy Vary's regional hospital bought the same kind of work in June 2026, and finished it in August [S27].

Two of those buyers have since filed that the state held them up. Semily's owner extended its contract because the health ministry's national e-health centre had not helped test the hospital's connection [S23]. Karlovy Vary's hospital had its work finished and handed over on 25 August 2026, but no confirmation from that same centre that it was connected [S27].

Existing non-solutions: Seven established Czech vendors already sell hospital integration, and the oldest keeps amending its hospital contracts after signing [S5,S8].

Each one's name, products and customers are in its row. What they sell:

- Five sell integration connected to the national eHealth contact point, the state gateway for exchanging patient data between providers [S8]. One of them won Sokolov hospital's eHealth modernisation in August 2026 [S26].
- A sixth sells a hospital enterprise service bus [S8].
- A seventh sells information-system integration to hospitals [S11]. It won Náchod's data-sharing platform in September 2026 [S15].
- The oldest has sold hospital systems in Czechia since 1990, and its contracts with four named hospitals are public [S5].

Those public contracts show what buying from the vendor already inside looks like after signing [S5]:

- Zlín's regional hospital signed two amendments to its hospital-system service contract on the same day, and both raised the price [S5]. What they came to is in the table of what one buyer pays, under [Willing to pay](#willing-to-pay).
- St Anne's university hospital in Brno extended a works deadline with the same vendor in the same weeks [S5].
- Olomouc's university hospital signed a third amendment on its hospital-system works [S5].
- Kroměříž hospital signed the seventh and eighth amendments to its integration platform within a month [S5].
- The same vendor won the repeat interoperability award in Prague and the Mladá Boleslav modernisation in August 2026 [S13,S14]. It also holds Semily's interoperability contract, signed in April 2026, and Karlovy Vary's, signed in June 2026 [S23,S27].

The state audit office found one hospital buying its software the same way, from suppliers already inside and without competition [S20]. IKEM — Prague's institute of clinical and experimental medicine — paid three IT suppliers 59.5M CZK through at least 345 orders without a tender [S20]. One supplier alone got more than 31M CZK in 2022–2024 for building and maintaining 13 of its applications, in orders each under 150,000 CZK [S20].

Why now: Hospitals are paying millions each for data-sharing software now, while the state's shared version runs six years late [S1,S6].

- Each hospital pays millions for its own links to other providers [S1,S3].
- After signing, the oldest vendor has raised prices and extended deadlines by amendment [S5].
- National data sharing, planned for 2020, will come in 2026 at the earliest [S6].

Behind those three items are a state audit, a grant deadline and the dates of a new EU law:

- In January 2026 the state audit office, which checks how public money is spent, reported that health-data sharing and electronic referrals are six years late [S6].
- The same report found registries the law requires still missing in early 2023, and 158M CZK spent on e-health goals in 2020–2024 with the infrastructure still absent [S6].
- In September 2026 the Semily hospital's owner extended its interoperability contract, because the health ministry's national e-health centre had not helped test the hospital's connection [S23].
- Also in September 2026 Karlovy Vary's hospital and its vendor moved to 31 December 2026 the date for producing the state's confirmation that the hospital is connected, because it had not been issued [S27].
- The European Health Data Space, the EU regulation on sharing health records, has been in force since March 2025 [S7].
- Its implementing acts, the detailed technical rules, are due in March 2027, and its rules for hospital record systems fall on the Czech vendors that sell them [S7].
- From 26 March 2029 patient summaries and electronic prescriptions must be exchangeable across borders, and most rules on re-using health data apply [S7].
- From 2031 imaging, laboratory results and discharge reports follow [S7].
- From 26 March 2029 hospitals must also describe the data they hold in one machine-readable European format, set by the European Commission in September 2026 [S29].
- On 3 July 2026 the health ministry filed a draft amendment of Act No. 325/2021, the Czech e-health law, with no dated duty yet [S10].
- On 1 September 2026 the European Commission put out for comment a draft of the technical rules for HealthData@EU, the EU network for re-using health data across borders; it sets no new deadline [S17].
- On 2 December 2026 at 14:00 the state's two eHealth grant calls close, after being open since November 2023 [S19].
- Hospitals are not waiting for any of this: they buy their own systems and integration now, one at a time [S4].

Who pays: Yes: hospitals, and the regions that own many of them, pay for integration now through public tenders [S1,S2].

- Three hospitals paid for exactly this work in 2026, through awarded tenders [S1,S14,S23].
- Four hospital purchases came to about €17M in ten weeks of 2026 [S1,S3].
- Motol and Homolka signed €11.7M of health-IT licences and support on one day [S9].
- Karlovy Vary's hospital signed 70.9M CZK for its hospital system and support [S4].

The first four projects ran from about €0.7M to €7.7M [S1,S3]. Three of the four were awards; Plzeň's was an open competition in July and August 2026 [S2].

- Motol and Homolka, two merged Prague hospitals that buy as one, signed a health-IT licence expansion of about €5.77M and a support contract of about €5.93M on 4 August 2026 [S9].
- Karlovy Vary's regional hospital signed its 70.9M CZK contract for hospital-system delivery and service support on 27 June 2026 [S4]. The European notice for that same contract names it interoperability work, and its value without VAT is in the table of what one buyer pays [S27].
- Psychiatric hospitals signed hospital-system contracts in the same weeks: Horní Beřkovice about 9.7M CZK plus 8.1M CZK of support, Opařany about 9.3M CZK, and Marianny Oranžské about 6.0M CZK [S4].
- Together with the tenders above, at least 8 public buyers bought or tendered hospital systems or integration in one summer [S4].
- One hospital's same-day price rises on its system contract are in the table of what one buyer pays.

Public money can pay part of it. Two state eHealth grant calls hold about 2.1bn CZK for a named list of hospitals, psychiatric hospitals and regional ambulance services, up to 28M CZK per provider [S19]. They pay the hospital, not a vendor, and their closing date is under [Why now](#why-now) [S19].

A rough estimate, not a finding: if a third of the €17M were sold as licences instead, that would be about €5.7M, and these buyers keep paying for more work rather than finishing [S5,S14].

Solved elsewhere: Two established foreign companies sell the shared layer as one product, built once and sold to many hospitals.

A US company trading since 2014 moves data between hundreds of provider organisations and hundreds of apps through one API, an interface other software plugs into.

A company in Ljubljana, Slovenia, selling since 1989, runs its openEHR platform, built on an open standard for health records, in hundreds of hospitals. Trusts in Britain's National Health Service, Karolinska in Sweden and Basel in Switzerland are among them.

The Slovenian company is the closer template: a Central European firm long in hospital software, as the Czech vendors are [S8]. Neither was cheap to build.

## First moves

1. Build a connector that links a hospital's existing systems to other providers, in the message formats Czech hospital tenders already ask for. The specifications hospitals publish ask for a service bus inside the integration layer that exchanges the two health-data formats Czech hospitals run on; see [The opportunity](#opportunity). Build that as one product that sits beside whatever hospital system is already installed, not as another hospital system. Established vendors already sell connections to the state's eHealth gateway, so yours has to work beside theirs; see [Market gap](#competition).
2. Call the IT heads of the Zlín, Kroměříž and Olomouc hospitals, which keep signing amendments with their system vendor, and ask what integration costs them. Their contracts are public, and the amendments are listed under [Market gap](#competition), with what one of them cost under [Willing to pay](#willing-to-pay). Ask which connections they pay for again and again, and which they would rather buy once as a product. Then show them the date from which the EU makes exchangeable records compulsory, under [Why now](#why-now).
3. Bid for the open hospital tenders, the only purchases here an outsider can enter without displacing a signed contract. The Plzeň hospital group's system with integrations, a psychiatric hospital's eHealth system and Brno's cancer institute's eHealth package all went out without a supplier named; see [The opportunity](#opportunity). Their results are not on file, so find out who won each. Where an established vendor won, the next open tender is the door.
4. Plan for a long fight against seven established Czech vendors, and watch for the two events that could open the field. Each already sells hospital integration, and the oldest has sold hospital systems for decades; see [Market gap](#competition). The first event is who wins open tenders like Plzeň's. The second is the EU's detailed rules for hospital record systems, which fall on every one of those vendors; their date is under [Why now](#why-now). Bidding costs money long before a first payment, as [Execution difficulty](#execution-difficulty) explains.

## Revisions

P26-08-25 · citation corrected — The OR-CZ ledger entry cited [S9], the Motol/Homolka licence contracts, which do not name OR-CZ. The receipt is [S11], the coverage gap-check that found it: "OR-CZ (orcz.cz/integrace), a Czech vendor selling information-system integration to hospitals that [S8] did not name". A wrong marker is worse than none — it sends a reader to a source that does not carry the claim, which is the failure the [Sn] system exists to prevent. Corrected in place; no marker renumbered.

2026-08-25 · locals completeness — OR-CZ added to `locals[]`. The record's own argument already named it selling hospital IS integration alongside the five vendors on the ledger, and then observed that it was not on the ledger — the register stating its own omission rather than fixing it [S9]. Under the owner's rule that no player is ever excluded, it is now recorded: verified in ARES as OR-CZ spol. s r.o., IČO 48168921, incorporated 17 March 1993, and present in the contracts register supplying Psychiatrická léčebna Šternberk. `scores.gap` is unmoved — it was already 0 on six established direct sellers, and a seventh cannot make a taken space more taken. What changes is that a builder now sees the true size of the field.

2026-08-13 · de-rank — A gap check found real CZ integration products (Medicalc mEx, PHYSTER, Stapro FONS/TransMISE, ICZ eMEDOCS, AutoCont ESB ACIB), so the original "no product layer" framing was too strong [S8]; gap stays 0 with incumbents named and status moves to watching. What survives the check: EHDS conformity deadlines (2029/2031) now put a dated end-state behind the spend [S7], and the NKÚ receipt plus the amendment churn document that the current model is failing its buyers [S5,S6]. Watch the Plzeň open tender outcome and the EHDS implementing acts (Mar 2027) for the moment this re-ranks [S2,S7].

2026-08-20 · evidence audit — Four unbacked claims removed. NCEZ: the institution and the claim that it "sets standards but ships no tooling" both return no hits anywhere in the signal corpus or in any source note here. "StaproMedea" (a mangled compound) and "AMIS" appear nowhere in the register at all; the product names that are on file sit in this record's own gap-check note, so the clause now reads Stapro FONS/TransMISE and ICZ eMEDOCS and is cited to [S8] rather than to three TED tenders that name none of them. "Each is a bespoke SI project; none produces a reusable product" — the tender receipts show what was bought, not what the delivery produced. And "the products are mostly incumbent-ecosystem stacks rather than neutral layers" — the gap check names the products but does not characterise their architecture.

2026-08-24 · fact check — The "€3-8M projects" range misdescribed its own receipts: the awards on this ledger are ~€7.7M, ~€5.8M, ~€2.8M and ~€0.7M [S1,S2,S3], so two of the four fall outside it. Body and build note now state the receipted span, €0.7-7.7M. The three TED values were re-verified live against the TED API on this date — 189.2M, 143.0M and 68.8M CZK — and the registr-smluv lookup corpus independently pairs STAPRO and ICZ.HEA with named hospital buyers, corroborating the incumbent picture [S5,S8].

2026-08-25 · plain-language pass and evidence added — Two passes this date, merged here. First: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek; that pass touched no score, source note or [Sn] marker. Second, from the 2026-08-25 retrospective harvest: Motol/Homolka signed ~€11.7M of health-IT licences and support in one August week [S9], corroborating the incumbent-stack spend already argued from the amendment churn [S5], and the Health Ministry filed an amendment of the national e-health act 325/2021 Sb. to VeKLEP [S10]. Both are context receipts; no score moved by that pass. Third pass this date, merged here: re-scored under the rewritten SCORING.md, which replaces the v1 "does a company exist?" test with the ESTABLISHED test and flips its sign between abroad and locally. `scores.proof` 0 → 3. Both comparables pass the test outright: Redox has sold since 2014 with 450+ named provider organisations, and Better has sold since 1989 into 500+ hospitals across fifteen countries with NHS trusts, Karolinska and Basel named [S8] — established in two-plus markets with Slovenia and Sweden both CEE-adjacent, which is rung 3 exactly. The old 0 was the contradiction the owner flagged for MATCH on 2026-08-24 and it is now resolved in the direction the evidence always pointed. `scores.gap` stays 0 and is now a positive finding rather than an unchecked one: six local incumbents were lifted out of the [S8] scan prose into a structured `locals[]` ledger, all six established — STAPRO (IČO 13583531, ARES 1990) on two limbs at once, two distinct public buyers in `data/lookup/cz-contract-parties.jsonl` plus four named hospital customers in registr smluv [S5]; ICZ and ICZ.HEA on named public customers [S5]; Medicalc, PHYSTER and AutoCont on the state NCPeH connection [S8]; M.I.T. Consulting on the eSSL attest it holds. Founding years were verified in ARES on this date. `score` 5 → 8. The non-solutions and Proven-abroad paragraphs were rewritten to state maturity rather than mere existence, because under the new ladder that is the fact carrying both scores; no claim was added beyond its sources and none removed. Money, urgency and demand untouched, and every existing [Sn] marker and source note is unchanged.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. All six entries convert to `competes: direct` + `maturity: established`: STAPRO, ICZ (eMEDOCS), Medicalc, PHYSTER, AutoCont and M.I.T. Consulting each sell an NCPeH-connected integration offering to hospitals, which is the product and the buyer this file is about [S8]. STAPRO's evidence line now names FONS/TransMISE outright, because "sells hospital systems since 1990" on its own read like a neighbouring vendor rather than a competitor. `scores.gap` stays 0 and now rests on the field it was always meant to: direct sellers that pass the established test, not merely mature firms in the vicinity. Noted and NOT acted on, because it is an addition rather than a conversion: [S9] also names OR-CZ selling hospital IS integration alongside these five, and it is not on the ledger. Adding it would move no score, but until it is added the ledger under-names the field by one. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 7 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass. NOTED AND NOT ACTED ON: the OR-CZ line carries an [S9] marker that resolves to the Motol/Homolka contract rather than to the coverage check that found OR-CZ, which is [S11]. It is left exactly as found — markers resolve by position and moving one is a renumbering, not a wording fix.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 8; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the open Plzeň competition as the one procedure an entrant can enter without displacing a signed contract [S2], connectors built against the HL7 and DASTA specifications the buyers keep writing [S11], the STAPRO amendment churn as the opening fact [S5], and the six incumbents named as what makes this hard [S8]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Restored the missing Revisions heading; without it every entry below rendered publicly under First moves. Glossed or replaced nine trade terms: FN, TED, ESB, ACIB, NHS, DASTA, KNTB, STAPRO, OR-CZ. Argument 444 → 423 words, every marker, figure and named vendor kept. First moves rewritten verbs-first, the incumbents restated as seven named sellers [S8,S11]. A gist added to all 11 sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The Zlín amendments already on file are now also recorded as a price: about 2.8M CZK of same-day price increases on one hospital's system-service contract [S18]. No score, status, note or marker touched.

2026-09-16 · headline copy — The headline was rewritten for a general builder as three lines under the title: a `brief:` on what is happening and why it matters now, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "Czech hospitals are buying software to share patient data one by one. EU sharing rules start in 2029."; brief: "Hospital after hospital is buying its own software to share patient data, for up to 190M CZK [S1,S2,S3,S14,S15]. State auditors found the national version years behind [S6]."; solution: "Build integration software that plugs into a hospital's systems and links them to other providers, as companies already do abroad."; good_for: "Health-software engineers ready for long public hospital tenders.". Previous title, verbatim: "Czech hospitals each buy the same data plumbing from scratch". Previous solution, verbatim: "One hospital integration layer built as a product and sold to every hospital group, instead of each one commissioning the same connections between its clinical systems from scratch.". There was no previous brief or good_for. Rewritten from the agent draft, which predated the owner's framing rules, and cut to the owner's length limits. Kept from its claim check: no "from scratch", which the 2026-08-20 audit cut from the body; no claim that the Plzeň competition is still open. "Hospital after hospital" stands on six buyers of software for linking systems and sharing data between June and 1 September 2026: Uherské Hradiště [S1], Plzeň, tendered rather than awarded [S2], Zlín and Olomouc [S3], Revmatologický ústav [S14] and Náchod [S15]; the psychiatric and Karlovy Vary contracts [S4] are hospital information systems with no stated data-sharing scope and are not counted. 190M CZK is the Uherské Hradiště award, 189.2M CZK on TED, the largest and not a typical one, hence "up to" [S1]. "Years behind" is the audit office's six years, 2020 plan to 2026 at the earliest [S6]. 2029 is when the EU's cross-border patient summaries and ePrescription apply [S7]. "Redox in the US" became "as companies already do abroad" (Redox, Better) [S8]. Seven established Czech vendors already sell this [S8,S11], and the copy claims no opening. No score, status, source, note, marker or body sentence changed. Same date, pain-point pass: title "Czech hospitals are buying software to share patient data one by one. EU sharing rules start in 2029." → "Czech hospitals each pay millions for their own software to share patient data". Why: the old headline described a buying pattern and a 2029 rule, not a cost to anyone. The new pain is the money each hospital spends alone: separate tenders and awards from about 5M CZK to about 190M CZK [S1,S2,S3,S12,S14,S15], which the unchanged brief already tells. "Millions" holds for every award on file, the smallest being 5.158M CZK [S12]. The 2029 date stays in the body [S7]. No score, status, source, note or body sentence changed. Same date, good-for opener (owner: "Good for should always start with a person"): "Health-software engineers ready for long public hospital tenders." became "Engineers who know hospital software and can wait out long public tenders." — same meaning, person first. Same date, abroad count (owner: fill "do abroad" with "X companies do in Y countries"): solution "…links them to other providers, as companies already do abroad." became "…links them to other providers, as 2 companies already do in 2 other countries." Counted from comps[] only: Redox (comps[0], geo US), whose API platform moves data between 450+ provider organisations and hundreds of apps; Better (comps[1], geo SI), whose openEHR platform runs in 500+ hospitals and which the body names as the closer template for the shared layer. None excluded. Countries are where the two are based, not Better's 15 markets.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on hospitals buying alone, with the Uherské Hradiště, Plzeň, Zlín and Olomouc purchases as its three items [S1,S2,S3], the service-bus gloss and the HL7/DASTA specification (from old move 2) as detail [S11], and the later buyers as a new list [S12,S13,S14,S15,S16]. Competition opens on the seven established vendors, describes them by what they sell and leaves every name, product and customer to its `locals[]` row, and gained the amendment churn from old moves 3 and 4 [S5] and the incumbent's two August awards [S13,S14]. Why now opens on the money each hospital spends and the six-year national delay, with the audit and the EU law's dates below the first three items [S1,S5,S6,S7]. Willing to pay answers yes, with the €17M, Motol and Homolka and Karlovy Vary as its items and the psychiatric-hospital contracts as detail [S1,S3,S4,S9]. Validated abroad describes both `comps[]` companies without their names or figures, which stay in their rows. The moves lost every [Sn] marker, figure and company name for links; move 1 now builds the connector (old move 2) and move 2 calls the hospitals with the amendments (old move 3). `entry.why` was rewritten as "Easier: … Harder: …" from the same gates [S1,S7,S8,S11]; the STAPRO and ICZ names left it for their rows. S14.why and S15.why no longer say "this record". Detail added from sources already on file, none of it new evidence: the Motol and Homolka amounts and date [S9], the e-health act amendment [S10], the five later buyers [S12–S16], the HealthData@EU draft [S17], the missing registries and the 158M CZK [S6], the EU law's 2025 entry into force and 2027 implementing acts [S7], the St Anne's and Olomouc amendments [S5], and the psychiatric-hospital amounts [S4]. Corrected against the sources rather than the old sentences: "four awards" became three awards and one open tender, since Plzeň's was an open competition [S2]; M.I.T. Consulting was listed among the vendors wired into the national eHealth contact point, but [S8] names five such offerings and M.I.T. only as selling a hospital service bus; move 2's "each locked inside its own stack" [S8] went, because the 2026-08-20 audit already found [S8] does not describe their architecture, and its "six" became five; move 3's "eighth amendment inside a month" became the seventh and eighth amendments signed within a month [S5]; move 1's "every other contract here is already signed" no longer holds, since the Petrohrad and cancer-institute tenders named no supplier [S12,S16] and Plzeň's summer competition has no result on file [S2], so move 3 now names all three and says so; "eight or more public buyers re-solving one problem" became buyers who "bought or tendered hospital systems or integration" [S4], since those contracts state no data-sharing scope; "spending toward it now" (the EU law) became "not waiting … buy their own systems now" [S4], which does not tie the spend to the law; the 1990 start now reads as the oldest vendor's row date, not as [S5]; Better "grew out of a decades-old systems-integration business" is on no source here, and its own about page (better.care/about-us, read 2026-09-18) gives only a Ljubljana head office and "30+ years in healthcare IT", so it now reads "a Central European firm long in hospital software"; Redox's "Madison" is not in its row and was dropped. Flagged as inference: the licence estimate, kept as "a rough estimate, not a finding", with "annual" dropped because the €17M covers ten weeks, not a year, and "renew rather than finish" now resting on the amendments and the repeat award [S5,S14]; and "bidding costs money long before any payment" in `entry.why`, carried from the old line, which cited nothing. No process block was added: the sources document purchases and amendments, not who sends patient data where, and the one step that would describe the vendors' side is the architecture claim [S8] does not support. No score, status, source, `note:`, `sources[]` order, title, brief, solution or good_for changed. Same date, later pass, merged here: evidence added from the monthly scans. IROP calls 78 and 79, about 2.1bn CZK of open eHealth grants for named hospitals and ambulance services, closing 2 December 2026, now sit under Willing to pay and in the Why now dates [S19]; money was already 2 and does not move. The audit office's IKEM finding, 59.5M CZK of IT bought through at least 345 untendered orders, was added to Competition as context only [S20]: the audit does not say those applications share patient data, so it backs no score. No score or status changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 2 → 1 and `score` 8 → 7, so the band moves STRONG → FAIR; Willing to pay stays 2. Why now was 2 as deadline 1 plus the freshness point, which is retired. The only dated duty on file is the European Health Data Space: from 26 March 2029 patient summaries must be exchangeable, which is more than 18 months after this date, and its rules for record systems fall on the vendors [S7]. That is rung 1. The e-health act amendment and the HealthData@EU rules are drafts, already tagged `dims: []` [S10,S17]. The eHealth grants' 2 December 2026 close is a grant date, not a deadline [S19]. Willing to pay was 2 on the open Plzeň tender above 5M CZK [S2]. That is now public money nearby, and money is 2 on paid receipts instead. Tagging pass, every source on file that shows someone paying for this job, the integration and data-sharing layer: two awarded tender lines are restated as price receipts. [S21] is Uherskohradišťská nemocnice's eHealth platform for sharing information between providers, 189,163,478 CZK, awarded 7 August 2026 [S1]. The CZK value was read from the TED search API on this date, and matches the 189.2M CZK of the 2026-08-24 fact check. [S22] is Revmatologický ústav's "eHealth a interoperabilita" repeat award, 27,756,514 CZK, 31 August 2026 [S14]. Both are dated within 24 months. They are appended as new sources rather than retyped in place, because the body cites [S1] and [S14] for the buying wave and a cited price receipt fails `PRICE_RESTATED`; the p-0008 receipts set that pattern. Not restated, and why. Plzeň is an open competition with no award on file, and it bundles a whole hospital information system [S2]. Zlín's award buys a hospital information system [S3]; Olomouc's €0.7M interoperability work in the same note is this job, but its own notice and CZK value are not on file. Karlovy Vary and the psychiatric hospitals bought hospital systems with no data-sharing scope [S4]. The Zlín price rises [S18] are on a hospital-system service contract, so [S18] stays untagged; the Kroměříž integration-platform amendments in [S5] are this job but carry no amount on file. Motol and Homolka bought health-IT licences and support [S9]. Mladá Boleslav's award modernises its hospital system [S13]. Náchod's award line buys an imaging archive inside a data-sharing project, with only a euro value on file [S15]. Petrohrad and the cancer institute tendered with no award [S12,S16]. The eHealth grants stay on file as public money nearby, and their lift is not needed [S19]. Stale notes fixed on [S2], [S7], [S9] and [S19], which named the old money and deadline rungs. Why now prose re-read: it leads on what hospitals pay now and the state's delay, and claims no firm deadline, so it stands. Willing to pay's first list now opens with the two awards the score rests on, without their amounts, which live in the receipts [S1,S14]. Its "Yes" answer stands. `[Competition](#competition)` became `[Market gap](#competition)` in moves 1, 2 and 4. No other score, status, entry or body sentence changed. Same date, later pass, merged here: evidence audit — Linked four TED notices. Semily's interoperability contract with the oldest vendor [S23], restated as a paid award [S24]; its deadline was extended because the ministry's e-health centre did not help test the connection, tagged demand, which stays 1 (one buyer's filing, not recurring complaints). Olomouc military hospital's re-tender [S25]; Sokolov's eHealth award, no data-sharing scope [S26]. Money stays 2. Gap rechecked: both winners already on file, stays 0. entry.why's tender floor now €0.2M [S12], and its "long" cut to fit 320 characters. Petrohrad's third notice folded into [S12].

2026-09-21 · evidence added and demand rescored — Three sources linked from the weekly scan. [S27] is Karlovy Vary's interoperability award, a contract-modification notice read from the TED search API this date: "Interoperabilita v nemocnici Karlovy Vary", buyer Karlovarská krajská nemocnice, supplier STAPRO, concluded 27 June 2026, result value 58,559,999.6 CZK, scope the interoperable exchange and sharing of medical documentation between providers over the national eHealth contact point. [S28] restates it as a price receipt; money was already 2 on [S21] and [S22] and does not move. [S29] is Commission Implementing Regulation (EU) 2026/2098, which makes the HealthDCAT-AP dataset description compulsory for every health data holder from 26 March 2029 — the same date as the EHDS rules already on file [S7], more than 18 months out, so Why now stays 1. DEMAND 1 → 2, `score` 7 → 8, band FAIR → STRONG. The rung is "recurring documented complaints". [S23], a notice published on 15 September 2026 and added here on 2026-09-19, is one buyer's filing that the health ministry's national e-health centre had not helped test its connection, and was recorded then as supporting demand 1 because one filing is not recurring. [S27] is a second named hospital buyer filing the same kind of thing six days later: the work was finished, handed over without defects and in production on 25 August 2026, but the ministry's confirmation that the hospital is connected to the interoperability ecosystem had not been issued, so the date for producing it moved to 31 December 2026. With the state audit [S6] and the amendment churn already tagged demand [S5], the complaints are recurring. Prose re-read under the moved score and made to match: The opportunity gained the Karlovy Vary purchase as a later buyer and a short paragraph naming both hold-ups [S23,S27]; Why now gained the Karlovy Vary date beside Semily's, and the 2029 metadata duty [S27,S29]; Market gap's sentence on the incumbent's wins gained Karlovy Vary [S23,S27]; STAPRO's ledger line names it as a further hospital customer [S27]. CORRECTION, ANNOUNCED. The 2026-09-19 entry above states that Karlovy Vary and the psychiatric hospitals "bought hospital systems with no data-sharing scope [S4]", which is why that contract was not restated as a price. That was true of the evidence then on file and is not true of the contract: the contracts register entry behind [S4] (38551596, read this date) gives "Smlouva o dílo a poskytování servisní podpory SM-AS008841", concluded 27 June 2026 with STAPRO, 58,559,999.60 CZK without VAT and 70,857,599.52 CZK with it, and the TED notice for the same procurement names interoperability in its title and its scope. So the ~70.9M CZK [S4] records is this interoperability contract, and Willing to pay now says so. Nothing is claimed about the psychiatric-hospital contracts in the same note, which still state no data-sharing scope. Gap re-checked: the winner is STAPRO, already on the ledger as direct and established, so gap stays 0 and `status` stays watching. Proof untouched. No source note was edited, no marker renumbered, and the three sources were appended at the end.
