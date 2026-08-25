---
id: p-0022
region: cz
title: Czech hospitals each buy the same data plumbing from scratch
category: health
geo: CZ-national
score: 5
scores:
  proof: 0
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
sources:
- type: tender
  name: "TED — Uherské Hradiště eHealth platform (~€7.7M)"
  why: "A regional hospital bought a platform for provider-to-provider communication and data sharing in August 2026 — the largest single award in this wave."
  url: https://ted.europa.eu/en/notice/-/detail/549134-2026
  note: 'ted-549134-2026: Uherskohradišťská nemocnice awarded ~€7.7M to create an eHealth
    platform for provider-to-provider communication and data sharing (Aug 2026).'
  date: '2026-08-07'
  signal: ted-549134-2026
- type: tender
  name: "TED — Plzeň hospital group, NIS with ESB (~€5.8M)"
  why: "The Plzeň region's hospital group ran an open competition for a hospital information system with an enterprise service bus and integrations."
  url: https://ted.europa.eu/en/notice/-/detail/476712-2026
  note: 'ted-476712-2026: Nemocnice Plzeňského kraje group tendering NIS + ESB + integrations,
    OPEN competition ~€5.8M (Jul–Aug 2026). Open tender ≥5M CZK: money scored 2.'
  date: '2026-07-10'
  signal: ted-476712-2026
- type: tender
  name: "TED — Zlín KNTB hospital system (~€2.8M)"
  why: "Zlín's regional hospital bought a hospital information system with integration scope; FN Olomouc bought eHealth interoperability (~€0.7M) in the same weeks."
  url: https://ted.europa.eu/en/notice/-/detail/443904-2026
  note: 'ted-443904-2026: Krajská nemocnice T. Bati (Zlín) awarded ~€2.8M for a hospital information
    system incl. integrations (Jun 2026); FN Olomouc bought eHealth interoperability (~€0.7M)
    in the same window — ≥4 distinct regional buyers in ten weeks.'
  date: '2026-06-29'
  signal: ted-443904-2026
- type: contract
  name: "Registr smluv — Karlovy Vary hospital (~70.9M CZK)"
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
  why: "A sweep of the Czech field naming what already exists — Medicalc mEx, PHYSTER, Stapro FONS/TransMISE, ICZ eMEDOCS, AutoCont's ESB ACIB and M.I.T. Consulting's hospital bus."
  url: https://www.zdravotnickydenik.cz/2026/01/medicalc-meni-fungovani-nemocnic-jan-kupka/
  note: 'Gap check 2026-08-13: CZ integration-platform products DO exist — Medicalc mEx, PHYSTER
    TECHNOLOGY, Stapro FONS/TransMISE, ICZ eMEDOCS/ISAC, AutoCont AC Pramen/ESB ACIB are NCPeH-connected
    integration offerings, and M.I.T. Consulting sells a hospital ESB. The field is not empty:
    local players named, gap stays 0 and status moves to watching per the de-rank rule. The
    residual question is why 8+ buyers still procure bespoke multi-million integration builds
    despite these products — vendor-neutrality and coverage, not absence.'
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-08-24'
---

Between June and August 2026, four Czech regional hospital groups went to market separately for structurally the same thing: a layer that lets hospital systems talk to each other and to outside providers. Uherské Hradiště awarded ~€7.7M for an eHealth communication platform [S1]. The Plzeň hospital group opened a ~€5.8M competition for a hospital system with an enterprise service bus [S2]. Zlín awarded ~€2.8M, and FN Olomouc bought interoperability work at ~€0.7M [S3].

Why now: the European Health Data Space makes structured, exchangeable health records a legal end state — cross-border patient summaries from 2029, imaging and discharge data from 2031 [S7]. Czech hospitals are spending toward it now, one hospital at a time [S4]. The national layer they would otherwise wait for is six years late: health-data sharing and eŽádanka have slipped from 2020 to 2026 at the earliest, and registries required by law are still missing [S6].

Who pays: hospital groups and the regions that own them — today through integration tenders, which is where the money already is. Four TED awards alone carried ~€17M in ten weeks [S1,S2]. The contract registry adds the same summer's Karlovy Vary hospital at ~70.9M CZK and a psychiatric-hospital wave behind it, making eight or more distinct public buyers re-solving one problem in a single season [S4]. Projects run €0.7M to €7.7M each [S1,S3]. A product that converted even a third of that spend into licences would be a multi-million-euro annual line, and these buyers renew rather than finish.

Existing non-solutions: the field is not empty. Stapro (FONS, TransMISE), ICZ (eMEDOCS) and CompuGroup sell hospital systems with their own integration stacks, and Medicalc, PHYSTER and AutoCont's ESB ACIB sell integration products beside them [S8]. What the contract registry shows about buying that from an incumbent is less flattering: two service amendments repriced upward on the same day, works deadlines extended, one integration platform on its eighth amendment [S5].

Solved elsewhere: the shared layer exists as a product in other markets — built once, sold many times. Redox (Madison, $95M raised) moves data between 450+ US provider organisations and hundreds of applications through one API platform. Better (Ljubljana) runs an openEHR platform under 500+ hospitals across 15 countries, including NHS trusts, Karolinska and Basel. Better is the closer template: it grew out of a decades-old systems-integration business, which is the position Czech vendors already occupy [S8]. Neither was cheap to build.

## Revisions

2026-08-13 · de-rank — A gap check found real CZ integration products (Medicalc mEx, PHYSTER, Stapro FONS/TransMISE, ICZ eMEDOCS, AutoCont ESB ACIB), so the original "no product layer" framing was too strong [S8]; gap stays 0 with incumbents named and status moves to watching. What survives the check: EHDS conformity deadlines (2029/2031) now put a dated end-state behind the spend [S7], and the NKÚ receipt plus the amendment churn document that the current model is failing its buyers [S5,S6]. Watch the Plzeň open tender outcome and the EHDS implementing acts (Mar 2027) for the moment this re-ranks [S2,S7].

2026-08-20 · evidence audit — Four unbacked claims removed. NCEZ: the institution and the claim that it "sets standards but ships no tooling" both return no hits anywhere in the signal corpus or in any source note here. "StaproMedea" (a mangled compound) and "AMIS" appear nowhere in the register at all; the product names that are on file sit in this record's own gap-check note, so the clause now reads Stapro FONS/TransMISE and ICZ eMEDOCS and is cited to [S8] rather than to three TED tenders that name none of them. "Each is a bespoke SI project; none produces a reusable product" — the tender receipts show what was bought, not what the delivery produced. And "the products are mostly incumbent-ecosystem stacks rather than neutral layers" — the gap check names the products but does not characterise their architecture.

2026-08-24 · fact check — The "€3-8M projects" range misdescribed its own receipts: the awards on this ledger are ~€7.7M, ~€5.8M, ~€2.8M and ~€0.7M [S1,S2,S3], so two of the four fall outside it. Body and build note now state the receipted span, €0.7-7.7M. The three TED values were re-verified live against the TED API on this date — 189.2M, 143.0M and 68.8M CZK — and the registr-smluv lookup corpus independently pairs STAPRO and ICZ.HEA with named hospital buyers, corroborating the incumbent picture [S5,S8].
