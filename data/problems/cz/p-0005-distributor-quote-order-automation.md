---
id: p-0005
region: cz
title: Czech SMB distributors and manufacturing suppliers re-type inbound RFQs and orders
  from e-mail, PDF and Excel into their ERPs by hand
category: b2b
geo: CZ-national
score: 4
scores:
  proof: 3
  money: 0
  urgency: 1
  demand: 0
  gap: 0
status: watching
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'AI document extraction is commodity, but Pohoda/Helios/ABRA integrations and distributor
    pilots take real build-and-sales effort — Mercura''s ~20-person seed-funded path shows
    the garage shape.'
comps:
- name: Mercura
  url: https://www.mercura.ai/
  geo: DE
  since: 2024
  traction: '$2.1M oversubscribed seed — TQ Ventures, SignalFire (Startbase, 2025); $1M ARR in under a year (Extruct, 2026); ~20 people'
  signal: yc-mercura
- name: turian
  url: https://www.turian.ai/
  geo: DE
  since: 2022
  traction: '$3.8M seed — Cherry Ventures et al. (PitchBook, 2026); 17 employees; 12+ ERP integrations incl. SAP and Dynamics'
- name: Workist
  url: https://www.workist.com/
  geo: DE
  since: 2019
  traction: '€12M total incl. €9M Series A led by Earlybird (Tech.eu, 2022); AI order entry (WorKL) for B2B document flows'
- name: Ventura
  url: https://www.ventura.ai/
  geo: US
  since: 2025
  traction: 'YC W26, 2-person team (YC, 2026); ERP-integrated quote and order entry automation; funding beyond YC undisclosed'
  signal: yc-ventura
sources:
- type: arbitrage
  name: "Mercura"
  why: "Bavarian YC W25 company, around 20 people, automating quote and order processing for construction-supply distributors — the same buyer, one border away."
  url: https://www.ycombinator.com/companies/mercura
  note: 'yc-mercura: Mercura (YC W25, Bavaria, ~20 people) automates quote/order processing
    for construction-supply distributors with AI; Comena (YC S25) and Seals AI (S24) prove
    the same wedge in a second market. DE (CEE-adjacent) + US = analogs in 2+ markets with
    adjacent validation.'
  date: '2026-08-13'
  signal: yc-mercura
- type: gap-check
  name: "First Czech market scan"
  why: "An early sweep that returned US and global tools plus generic Czech AI agencies — superseded by the three Czech vendors found later."
  url: https://www.ycombinator.com/companies/mercura
  note: 'Absence check 2026-08-13: searches return US/global tools (WizCommerce, turian) and
    CZ generic AI agencies (Appmine); no CZ vertical product. Classification: no CZ player
    found.'
  date: '2026-08-13'
- type: arbitrage
  name: "Ventura"
  why: "A two-person YC W26 team selling ERP-integrated quote and order entry as an 'AI workforce for distributors and manufacturers' — a third funded company on this wedge inside two years."
  url: https://www.ycombinator.com/companies/ventura
  note: 'yc-ventura: Ventura (YC W26) — ''AI workforce for distributors and manufacturers'';
    a third company on the wedge within two years, confirming the category keeps getting funded.'
  date: '2026-08-13'
  signal: yc-ventura
- type: gap-check
  name: "Apertia Tech, Alice and Dativery"
  why: "Apertia's 'B2B Objednávky pomocí AI' pulls orders out of e-mail into Pohoda, ABRA, Money, Helios and K2; Alice by Redque and Dativery sell the same extraction into the same ERPs."
  url: https://apertia.ai/b2b-objednavky-agent
  note: 'Gap re-check 2026-08-20: looked for a Czech vertical product that reads inbound RFQs
    and orders out of e-mail, PDF and Excel and writes them into the Czech SMB ERPs — the
    absence claimed on 2026-08-13. FOUND, on the first Czech-language query. Apertia Tech s.r.o.
    (Praha 6 - Břevnov, IČO 27117758) ships a named product, "B2B Objednávky pomocí AI": it
    extracts products and specifications from an inbound e-mail, matches them against the
    customer''s own catalogue and internal item codes, generates the order in the ERP and
    auto-replies with confirmation and a delivery date. Its worked example on the product page
    is a velkoobchod se stavebními materiály — the same construction-supply distributor
    Mercura sells to in Bavaria. Apertia states dozens of completed integrations with Pohoda,
    ABRA, ABRA Flexi, Money S3/S5, Helios and K2, which is precisely the ERP-integration moat
    this record proposed as the defence against foreign entrants. Two further CZ vendors sell
    the same extraction into the same ERPs: Alice by Redque (receipts, invoices AND objednávky
    into Helios/Pohoda/Abra) and Dativery (orders and invoices into ABRA Flexi and POHODA, and
    the integration layer behind Digitoo). De-ranked under SPEC §4: gap 2 -> 0, score 6 -> 4,
    status -> watching. Method note: none of the three appears in our funded ledger — searching
    `data/signals/funded/` for CZ order-entry or ERP players returns nothing relevant, because
    these are service-and-product businesses that never raised.'
  date: '2026-08-20'
  queries:
    - "automatizace zpracování objednávek z e-mailu do ERP umělá inteligence velkoobchod Česko"
    - "AI vytěžování objednávek poptávek z PDF a Excelu do Pohoda Helios ABRA automaticky"
    - "Apertia.ai B2B objednávky agent automatické zpracování objednávek e-mail PDF EDI česká firma"
    - "česká firma AI agent pro obchodní oddělení zpracování poptávek nabídek distributor výrobce ERP integrace"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-24'
---

Czechia is dense with SMB velkoobchody and manufacturing suppliers running Pohoda, Helios and ABRA ERPs [S1]. Inbound demand arrives as unstructured e-mails, PDFs and Excel sheets, and staff re-type it into quotes and orders by hand [S1] — slow, error-prone work that caps how many RFQs a sales desk can turn around.

Why now: AI document extraction has made this wedge reliably automatable, and the model is proven next door — Mercura (YC W25, Bavaria) sells exactly this to construction-supply distributors and manufacturers in a market structurally adjacent to Czechia, with Comena (YC S25) and Seals AI (YC S24) replicating the wedge in the US [S1].

Who pays: the distributors and suppliers themselves; quote-turnaround speed converts directly to win rate, making ROI legible to owners. Integration into the dominant Czech ERPs (Pohoda/Helios/ABRA) was posited as the localization moat [S1] — and that moat is already held, see below.

Existing non-solutions: manual entry, generic automation agencies (Appmine) building one-off scripts, and US/global tools (WizCommerce, turian) without Czech ERP integrations or language handling [S2]. A Czech vertical product exists, contrary to this record's original finding [S2]. **Apertia Tech s.r.o.** (Prague) sells "B2B Objednávky pomocí AI" — extraction of products and specifications from an inbound e-mail, matching against the customer's catalogue and internal item codes, order generation in the ERP, automatic confirmation with a delivery date — and names dozens of completed integrations with Pohoda, ABRA, ABRA Flexi, Money S3/S5, Helios and K2 [S4]. Its own worked example is a velkoobchod se stavebními materiály, the same construction-supply distributor Mercura sells to in Bavaria [S1,S4]. **Alice by Redque** and **Dativery** sell the same extraction into the same ERPs [S4].

Solved elsewhere: funded analogs in two markets (DE and US), with the German one directly next door to CEE [S1,S3]. What that no longer buys is an empty local field: the model is validated abroad and local vendors already sell it [S4]. No complaints are documented either — the demand case is structural, not evidenced.

## Revisions

2026-08-20 · gap re-check — De-ranked. The 2026-08-13 absence check behind gap 2 was recorded against a YC company page and returned only US/global tools plus "CZ generic AI agencies" [S2]; it never looked at what Czech vendors call this in Czech. Re-run against Czech-language search, the first query surfaced Apertia Tech s.r.o. selling a named B2B order-processing AI product with the exact Pohoda/ABRA/Helios/Money/K2 integration set this record proposed as its moat, plus Alice by Redque and Dativery doing the same extraction into the same ERPs [S4]. Gap 2 → 0 and score 6 → 4 under the SPEC §4 de-rank rule, status → watching; the who-pays and existing-non-solutions paragraphs were rewritten so the prose no longer contradicts the score. The record's remaining honest content is its proof: the wedge is funded in DE and the US, and it is also already being sold here.

2026-08-24 · evidence audit — Cut from Why now: "German-owned distributors operating in CZ already know the category, easing sales." The clause is the harvest note's own sales speculation [S1] — no signal, receipt or source documents any CZ distributor's awareness of anything, and buyer awareness is not a checkable fact. The Apertia incumbent receipt was re-verified live on this date (apertia.ai/b2b-objednavky-agent, HTTP 200) [S4]. Scores untouched.
