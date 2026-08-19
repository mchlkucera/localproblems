---
id: p-0022
region: cz
title: Czech regional hospitals are each buying bespoke multi-million-euro eHealth interoperability
  platforms — the same integration problem solved separately, over and over
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
  note: 'Hospital-grade interoperability sold through €3-8M public tenders against entrenched
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
  url: https://ted.europa.eu/en/notice/-/detail/549134-2026
  note: 'ted-549134-2026: Uherskohradišťská nemocnice awarded ~€7.7M to create an eHealth
    platform for provider-to-provider communication and data sharing (Aug 2026).'
  date: '2026-08-07'
  signal: ted-549134-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/476712-2026
  note: 'ted-476712-2026: Nemocnice Plzeňského kraje group tendering NIS + ESB + integrations,
    OPEN competition ~€5.8M (Jul–Aug 2026). Open tender ≥5M CZK: money scored 2.'
  date: '2026-07-10'
  signal: ted-476712-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/443904-2026
  note: 'ted-443904-2026: Krajská nemocnice T. Bati (Zlín) awarded ~€2.8M for a hospital information
    system incl. integrations (Jun 2026); FN Olomouc bought eHealth interoperability (~€0.7M)
    in the same window — ≥4 distinct regional buyers in ten weeks.'
  date: '2026-06-29'
  signal: ted-443904-2026
- type: contract
  url: https://smlouvy.gov.cz/smlouva/38551596
  note: 'hlidac-38551596: Karlovarská krajská nemocnice signed ~70.9M CZK for NIS delivery
    + service support (registr smluv, 27 Jun 2026); same weeks show a psychiatric-hospital
    NIS wave — PN Horní Beřkovice (~9.7M + 8.1M support), DPN Opařany (~9.3M), PN Marianny
    Oranžské (~6.0M). With TED that''s 8+ distinct public buyers re-solving the same integration
    problem in one summer.'
  date: '2026-06-27'
  signal: hlidac-38551596
- type: contract
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
  url: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
  note: 'reg-ehds: EHDS Regulation (EU) 2025/327 in force since Mar 2025; implementing acts
    due Mar 2027; cross-border primary use (patient summaries, ePrescription) and most secondary-use
    rules apply from Mar 2029, imaging/labs/discharge categories 2031. Dated obligations >18
    months out: deadline sub-score 1. EHR-system conformity requirements will hit the CZ vendor
    ecosystem (Stapro, ICZ, CGM) directly.'
  date: '2029-03-26'
  signal: reg-ehds
- type: gap-check
  url: https://www.zdravotnickydenik.cz/2026/01/medicalc-meni-fungovani-nemocnic-jan-kupka/
  note: 'Gap check 2026-08-13: CZ integration-platform products DO exist — Medicalc mEx, PHYSTER
    TECHNOLOGY, Stapro FONS/TransMISE, ICZ eMEDOCS/ISAC, AutoCont AC Pramen/ESB ACIB are NCPeH-connected
    integration offerings, and M.I.T. Consulting sells a hospital ESB. The field is not empty:
    local players named, gap stays 0 and status moves to watching per the de-rank rule. The
    residual question is why 8+ buyers still procure bespoke multi-million integration builds
    despite these products — vendor-neutrality and coverage, not absence.'
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-08-19'
---

Between June and August 2026, at least four Czech regional hospital groups went to market separately for what is structurally the same thing: an interoperability layer that lets hospital systems talk to each other and to outside providers. Uherské Hradiště awarded ~€7.7M for an eHealth communication platform; the Plzeňský kraj hospital group has an open ~€5.8M tender for NIS delivery with ESB and integrations; Zlín's KNTB awarded ~€2.8M for a NIS with integration scope; FN Olomouc bought interoperability work. Each is a bespoke SI project; none produces a reusable product.

Why now: the European Health Data Space regulation (in force since March 2025, with obligations phasing toward 2029+) makes structured, exchangeable health records a legal end-state, and Czech hospitals are spending toward it now, hospital by hospital, without a shared platform. The procurement cluster is the receipt: this is recurring, multi-buyer public spend on an unsolved integration problem.

Who pays: hospital groups and kraje (the owners) — today via SI tenders, which is exactly the opportunity for consultancies and dev shops; longer-term, a productized interop/ESB layer with Czech NIS integrations (StaproMedea, FONS, ICZ AMIS ecosystems) could compress these €3-8M projects into licensing deals.

Existing non-solutions: the incumbent Czech NIS vendors (Stapro, ICZ, CompuGroup) sell systems and their own integration stacks; NCEZ (the national eHealth center) sets standards but ships no tooling — and per NKÚ's January 2026 digitalization report, the national layer hospitals are waiting for is six years late, with health-data sharing and eZádanka slipping from 2020 to 2026-at-the-earliest and legally required registries still missing. Each hospital tender therefore re-solves interoperability locally, and what the registr smluv shows about how that goes is not flattering: STAPRO service amendments repricing upward, works deadlines extended, and one integration-platform contract on its eighth amendment.

Updated 2026-08-13 — de-rank applied: a gap check found real CZ integration products (Medicalc mEx, PHYSTER, Stapro FONS/TransMISE, ICZ eMEDOCS, AutoCont ESB ACIB), so the original "no product layer" framing was too strong; gap stays 0 with incumbents named and status moves to watching. What survives the check: the products are mostly incumbent-ecosystem stacks rather than neutral layers, EHDS conformity deadlines (2029/2031) now put a dated end-state behind the spend, and the NKÚ receipt plus the amendment churn document that the current model is failing its buyers. Watch the Plzeň open tender outcome and the EHDS implementing acts (Mar 2027) for the moment this re-ranks.
