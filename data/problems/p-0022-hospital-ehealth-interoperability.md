---
id: p-0022
title: "Czech regional hospitals are each buying bespoke multi-million-euro eHealth interoperability platforms — the same integration problem solved separately, with no product layer"
category: health
geo: CZ-national
score: 3
signals:
  arbitrage: 0
  money: 2
  deadline: 0
  demand: 0
  gap: 0
  freshness: 1
status: candidate
receipts:
  - type: tender
    url: https://ted.europa.eu/en/notice/-/detail/549134-2026
    note: "ted-549134-2026: Uherskohradišťská nemocnice awarded ~€7.7M to create an eHealth platform for provider-to-provider communication and data sharing (Aug 2026)."
    date: 2026-08-07
  - type: tender
    url: https://ted.europa.eu/en/notice/-/detail/476712-2026
    note: "ted-476712-2026: Nemocnice Plzeňského kraje group tendering NIS + ESB + integrations, OPEN competition ~€5.8M (Jul–Aug 2026). Open tender ≥5M CZK: money scored 2."
    date: 2026-07-10
  - type: tender
    url: https://ted.europa.eu/en/notice/-/detail/443904-2026
    note: "ted-443904-2026: Krajská nemocnice T. Bati (Zlín) awarded ~€2.8M for a hospital information system incl. integrations (Jun 2026); FN Olomouc bought eHealth interoperability (~€0.7M) in the same window — ≥4 distinct regional buyers in ten weeks."
    date: 2026-06-29
  - type: contract
    url: https://smlouvy.gov.cz/smlouva/38551596
    note: "hlidac-38551596: Karlovarská krajská nemocnice signed ~70.9M CZK for NIS delivery + service support (registr smluv, 27 Jun 2026); same weeks show a psychiatric-hospital NIS wave — PN Horní Beřkovice (~9.7M + 8.1M support), DPN Opařany (~9.3M), PN Marianny Oranžské (~6.0M). With TED that's 8+ distinct public buyers re-solving the same integration problem in one summer."
    date: 2026-06-27
created: 2026-08-13
updated: 2026-08-13
---

Between June and August 2026, at least four Czech regional hospital groups went to market separately for what is structurally the same thing: an interoperability layer that lets hospital systems talk to each other and to outside providers. Uherské Hradiště awarded ~€7.7M for an eHealth communication platform; the Plzeňský kraj hospital group has an open ~€5.8M tender for NIS delivery with ESB and integrations; Zlín's KNTB awarded ~€2.8M for a NIS with integration scope; FN Olomouc bought interoperability work. Each is a bespoke SI project; none produces a reusable product.

Why now: the European Health Data Space regulation (in force since March 2025, with obligations phasing toward 2029+) makes structured, exchangeable health records a legal end-state, and Czech hospitals are spending toward it now, hospital by hospital, without a shared platform. The procurement cluster is the receipt: this is recurring, multi-buyer public spend on an unsolved integration problem.

Who pays: hospital groups and kraje (the owners) — today via SI tenders, which is exactly the opportunity for consultancies and dev shops; longer-term, a productized interop/ESB layer with Czech NIS integrations (StaproMedea, FONS, ICZ AMIS ecosystems) could compress these €3-8M projects into licensing deals.

Existing non-solutions: the incumbent Czech NIS vendors (Stapro, ICZ, CompuGroup) sell systems, not neutral interop layers; NCEZ (the national eHealth center) sets standards but ships no tooling; each tender re-solves ESB architecture from scratch.

Scored on money and freshness only — deliberately conservative. Next moves: an EHDS deadline receipt (would add deadline points), a gap check on neutral interop products in CEE, and watching whether the Plzeň open tender's outcome names a repeatable platform.
