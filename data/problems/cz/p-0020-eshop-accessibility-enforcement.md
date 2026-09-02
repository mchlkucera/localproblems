---
id: p-0020
region: cz
title: Czech e-shops and digital services must meet the European Accessibility Act (zákon
  č. 424/2023 Sb.), in force since June 2025
category: retail-services
geo: CZ-national
score: 4
scores:
  proof: 0
  money: 0
  urgency: 3
  demand: 1
  gap: 0
status: rejected
build:
  capital: garage
  first_revenue: weeks
  builder: small-team
  note: 'The law is in force and ČOI is the designated supervisor, so audits and remediation
    can sell to obligated e-shops now; a dev plus accessibility auditor shipping zákon č. 424/2023
    mapping and a Shoptet-channel app needs integration effort, not capital.'
comps:
- name: AudioEye
  url: https://www.audioeye.com/
  geo: US
  since: 2005
  traction: 'NASDAQ: AEYE; $38.7M ARR, ~123k customers (Q3 2025 results); EU push timed to
    EAA enforcement (PRNewswire, Jul 2025)'
- name: accessiBe
  url: https://accessibe.com/
  geo: IL
  since: 2018
  traction: '$58M raised (Crunchbase); ~110k customers, widget on 200k+ sites (2024); overlay
    model auditors contest'
sources:
- type: regulation
  name: "European Accessibility Act (zákon č. 424/2023 Sb.)"
  gist: "the law, in force since 2025"
  why: "Czech law since 28 June 2025 — e-shops, banks, transport ticketing and e-book sellers must be usable by disabled customers, with ČOI among the designated supervisors."
  url: https://coi.gov.cz/pro-podnikatele/pristupnost-vyrobku-a-sluzeb-pro-podnikatele/
  note: 'reg-accessibility-act-cz: European Accessibility Act as zákon č. 424/2023 Sb., in
    force since 28 Jun 2025; 2026 is the first full enforcement year — ČOI runs mystery-shopping
    test purchases across whole checkout flows and can order corrective measures and fines.
    Forcing function live: deadline 2.'
  date: '2026-06-28'
  signal: reg-accessibility-act-cz
- type: complaint
  name: "shop5.cz — accessibility explainer for merchants"
  gist: "merchant confusion about scope"
  why: "A Czech e-commerce vendor's help page answering which shops the law actually covers — the trade's own sign that merchants are still working out whether it applies to them."
  url: https://www.shop5.cz/clanek/faq-pristupnost-e-shopu-a-zakon-c-424-2023-sb-na-koho-se-skutecne-vztahuje/
  note: E-commerce industry FAQ traffic (shop5.cz and peers) documents merchant confusion
    about scope and obligations — scattered but real industry pressure; demand scored 1.
  date: '2026-08-13'
created: '2026-08-13'
updated: '2026-09-02'
---

The European Accessibility Act — consumer digital services must be usable by disabled customers — has been Czech law since 28 June 2025 as zákon č. 424/2023 Sb. [S1]. It binds e-shops, banks, transport ticketing, e-book sellers and consumer-device makers; only the smallest service firms (micro-enterprises) are exempt [S1]. ČOI — the Czech trade inspection — is among the designated supervisors [S1].

Why now: the obligation is in force, not scheduled [S1]. Czech e-commerce help pages are still answering which shops it covers, so merchants are discovering it late [S2].

Who pays: e-shops, banks and other digital-service providers, buying audits, fixes and ongoing monitoring [S1]. E-commerce platforms are the channel — one integration with Shoptet or a peer reaches every obligated shop on it.

Existing non-solutions: no Czech vendor selling audits or fixes against zákon č. 424/2023 is known, and no market search has been run to find one.

Next moves: search the Czech market for accessibility tooling. Pull ČOI enforcement figures; the first fines would be a hard receipt. Test the platform channel inside the Shoptet ecosystem.

## Revisions

2026-08-20 · evidence audit — Four unbacked claims removed. From the lead: "The Czech e-commerce sector, one of Europe's densest per capita, is largely non-compliant with WCAG-level accessibility" — the corpus's only per-capita density claim is about road haulage, and no signal measures Czech accessibility compliance at all. From "Who pays": the merchant count attached to Shoptet, which appears in no signal; the platform stays named, the number does not. The whole competitive sentence in "Existing non-solutions" is gone — UserWay returns no hits anywhere, "no Czech legal mapping" and "a handful of Czech agencies do manual audits at consulting prices" have no receipt, and accessiBe's contested effectiveness is a comps traction line, which cannot back a body claim. What remains is the statement the record could already make: no CZ gap check was run this cycle, so gap scores 0.

2026-08-24 · fact check and rejected — The enforcement claim failed verification on every surface: the cited ČOI page carries no mystery shopping, no test purchases and no corrective-measure powers; ČOI's own published market-surveillance program for 2026 contains no accessibility project and no mention of zákon č. 424/2023; and no press receipt of accessibility inspections was found. The claim is deleted from the title, the lead, the window and the build note. The title also still asserted "most sites remain non-compliant" — the claim this record's own 2026-08-20 audit retracted from the body — and is gone with it. What remains receipted, an in-force law [S1] and one merchant FAQ [S2], is a compliance date, not a documented local problem. Rejected, not deleted — the trail stays. A mechanical sweep of the 606-add-on marketplace corpus on this date found no Czech accessibility add-on either, recorded here as coverage, not as proof of absence.

2026-09-02 · plain-language pass — Glossed three terms at first use: the European Accessibility Act, ČOI (the Czech trade inspection) and micro-enterprises, and replaced the FAQ acronym with plain words. The argument moved from 154 to 178 words — glosses cost words; every receipt is kept and the 28 June 2025 date is now stated. Both sources gained a public name, gist and why. Next moves is rewritten verbs-first, its self-reference struck. No score, status, note or marker touched.
