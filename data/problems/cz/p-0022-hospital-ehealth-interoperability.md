---
id: p-0022
region: cz
title: Czech hospitals each buy the same data plumbing from scratch
fix: 'One hospital integration layer built as a product and sold to every hospital group,
  instead of each one commissioning the same connections between its clinical systems from
  scratch.'
category: health
geo: CZ-national
score: 8
scores:
  proof: 3
  money: 2
  urgency: 2
  demand: 1
  gap: 0
status: watching
build:
  capital: industrial
  first_revenue: year-plus
  builder: funded-team
  note: 'Hospital-grade interoperability sold through €0.7-7.7M public tenders against entrenched
    NIS ecosystems (Stapro, ICZ) — comparables took $95M (Redox) or decades of SI base (Better)
    to reach product scale.'
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
    register [S5].
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
    OPEN competition ~€5.8M (Jul–Aug 2026). Open tender ≥5M CZK: money scored 2.'
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
    months out: deadline sub-score 1. EHR-system conformity requirements will hit the CZ vendor
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
    rests on the open Plzeň tender [S2].'
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
    2026-08-31 at the same value as ted-597290-2026, not separately cited.'
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
    STAPRO — as direct a match to this record's own words as a tender gets."
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
  why: "OR-CZ, this record's seventh named incumbent, won a system explicitly built for
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
created: '2026-08-13'
updated: '2026-09-03'
---

Between June and August 2026, four Czech regional hospital groups went to market separately for the same layer: one that lets hospital systems talk to each other and to outside providers. Uherské Hradiště awarded ~€7.7M for an eHealth platform [S1]. Plzeň's hospital group opened a ~€5.8M competition for a hospital system with an enterprise service bus — the switchboard routing messages between clinical systems [S2]. Zlín awarded ~€2.8M; Olomouc's university hospital bought interoperability work at ~€0.7M [S3].

Why now: the European Health Data Space makes exchangeable health records a legal end state — cross-border patient summaries from 2029, imaging and discharge data from 2031 [S7]. Czech hospitals are spending toward it now, one at a time [S4]. The national layer they would otherwise wait for is six years late: health-data sharing and electronic referrals slipped from 2020 to 2026 at the earliest, and registries required by law are still missing [S6].

Who pays: hospital groups and the regions that own them, through integration tenders. Four awards in the EU tenders journal carried ~€17M in ten weeks [S1,S2]. The state contracts register adds Karlovy Vary hospital at ~70.9M CZK and a psychiatric-hospital wave behind it — eight or more public buyers re-solving one problem in a single summer [S4]. Projects run €0.7M to €7.7M each [S1,S3]. A third of that spend converted to licences is a multi-million-euro annual line, and these buyers renew rather than finish.

Existing non-solutions: the field is not empty, and the vendors in it are old. Stapro has sold hospital systems here since 1990 and signs amendments with four named hospitals in the state contracts register [S5]. ICZ (eMEDOCS), Medicalc, PHYSTER, M.I.T. Consulting and AutoCont's ACIB service bus all sell integration wired into the national eHealth contact point — the state gateway carrying patient data between providers [S8]. What buying that from an incumbent costs: two service amendments repriced upward on the same day, works deadlines extended, one integration platform on its eighth amendment [S5].

Solved elsewhere: the shared layer sells as a product in bigger markets — built once, sold many times. Redox (Madison, since 2014, $95M raised) moves data between 450+ US provider organisations and hundreds of applications through one API platform. Better has sold from Ljubljana since 1989: 500+ hospitals in 15 countries on its openEHR platform, including trusts in Britain's National Health Service, Karolinska in Sweden and Basel in Switzerland. Better is the closer template — it grew out of a decades-old systems-integration business, the position Czech vendors already occupy [S8]. Neither was cheap to build.

## First moves

1. Bid Plzeň. Its hospital group is running an open competition — about €5.8M for a hospital system with a service bus and integrations [S2]. Every other contract here is already signed, so this is the one door that displaces nobody.
2. Build connectors, not another hospital system. Buyers write the same specification every time: a service bus inside the integration layer, exchanging HL7 and DASTA messages — the two health-data formats Czech hospitals run on [S11]. Six Czech vendors already sell a connection to the national eHealth contact point, each locked inside its own stack [S8]. Eight or more public buyers paid for bespoke builds anyway, in one summer [S4].
3. Open with the incumbent's own paperwork. Zlín's regional hospital signed two Stapro service amendments, both price increases, on the same day; St Anne's in Brno extended a works deadline; Kroměříž hospital's integration platform reached its eighth amendment inside a month [S5]. Then hand the buyer the date: cross-border patient summaries and ePrescription in 2029, imaging and discharge data in 2031 [S7].
4. Price the fight honestly. Stapro (selling since 1990), ICZ, Medicalc, PHYSTER, AutoCont, M.I.T. Consulting and OR-CZ each sell hospital integration today — seven named vendors in one field [S8,S11]. Two things could open it: who wins Plzeň [S2], and the European implementing acts due March 2027, which put conformity duties on every one of those vendors [S7].

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
