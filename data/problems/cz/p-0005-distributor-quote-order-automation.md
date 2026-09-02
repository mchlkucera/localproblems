---
id: p-0005
region: cz
title: Czech SMB distributors and manufacturing suppliers re-type inbound RFQs and orders
  from e-mail, PDF and Excel into their ERPs by hand
category: b2b
geo: CZ-national
score: 3
scores:
  proof: 2
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
locals:
- name: Apertia Tech
  url: https://apertia.ai/b2b-objednavky-agent
  ico: '27117758'
  since: 2004
  competes: direct
  maturity: established
  evidence: 'Its "B2B objednávky pomocí AI" reads products and specifications out of an inbound
    e-mail, matches them against the buyer''s catalogue and internal item codes, writes the
    order into the ERP and replies with a confirmation and a delivery date. Apertia Tech s.r.o.
    has traded since 2004 and says it is used in dozens of completed customer integrations
    across Pohoda, ABRA, ABRA Flexi, Money S3/S5, Helios and K2.'
- name: Dativery
  url: https://www.dativery.com/cs/
  ico: '05574617'
  since: 2016
  competes: direct
  maturity: established
  evidence: 'Used by Digitoo as its integration layer, Dativery sells order and invoice
    extraction into ABRA Flexi and POHODA. Dativery s.r.o. has traded since 2016.'
- name: Alice (Redque)
  url: https://redque.cz/
  ico: '14430266'
  since: 2022
  competes: direct
  maturity: early
  evidence: 'Extracts receipts, invoices and purchase orders into Helios, Pohoda and Abra. Redque
    s.r.o. was incorporated in April 2022 and names nobody using it.'
sources:
- type: arbitrage
  name: "Mercura"
  gist: "the Bavarian template"
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
  gist: "the superseded first sweep"
  why: "An early sweep that returned US and global tools plus generic Czech AI agencies — superseded by the three Czech vendors found later."
  url: https://www.ycombinator.com/companies/mercura
  note: 'Absence check 2026-08-13: searches return US/global tools (WizCommerce, turian) and
    CZ generic AI agencies (Appmine); no CZ vertical product. Classification: no CZ player
    found.'
  date: '2026-08-13'
- type: arbitrage
  name: "Ventura"
  gist: "the third funded team"
  why: "A two-person YC W26 team selling ERP-integrated quote and order entry as an 'AI workforce for distributors and manufacturers' — a third funded company on this wedge inside two years."
  url: https://www.ycombinator.com/companies/ventura
  note: 'yc-ventura: Ventura (YC W26) — ''AI workforce for distributors and manufacturers'';
    a third company on the wedge within two years, confirming the category keeps getting funded.'
  date: '2026-08-13'
  signal: yc-ventura
- type: gap-check
  name: "Apertia Tech, Alice and Dativery"
  gist: "the three Czech incumbents"
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
updated: '2026-09-02'
---

Quote requests (RFQs) and orders reach Czech wholesalers and manufacturing suppliers as e-mail, PDF and Excel; staff re-type them into Pohoda, Helios and ABRA — the ERP packages (accounting and stock software) they run on [S1]. Re-typing is slow, error-prone, and caps how many quotes a desk turns around [S1].

Why now: AI document extraction is commodity and the model proven one border away — Mercura (YC W25, Bavaria) sells this to construction-supply distributors, with Comena (S25) and Seals AI (S24) on the same job in the US [S1].

Who pays: distributors and suppliers buy this themselves, because a quote returned first wins the order. Integration with Pohoda, Helios and ABRA was the planned defence [S1]; three Czech vendors already hold it [S4].

Existing non-solutions: manual entry, agencies (Appmine) writing one-off scripts, and foreign tools (WizCommerce, turian) with no Czech integrations or language handling [S2]. A Czech product already sells this [S2]. **Apertia Tech s.r.o.** (Prague) ships "B2B Objednávky pomocí AI": it reads an e-mail's products and specifications, matches them to the customer's catalogue and item codes, writes the order into the ERP and replies with a delivery date [S4]. Apertia names dozens of completed integrations with Pohoda, ABRA, ABRA Flexi, Money S3/S5, Helios and K2 [S4]. Its worked example is a velkoobchod se stavebními materiály — the construction-supply distributor Mercura sells to in Bavaria [S1,S4]. **Alice by Redque** and **Dativery** sell the same extraction into the same systems [S4].

Solved elsewhere: the product is funded in Germany and the US [S1,S3], but the companies are young — only Workist, on a €9M Series A led by Earlybird, is three years in and past seed. Funding buys no empty field here — Czech vendors already sell this [S4]. No complaint is documented: the demand case is structural, not evidenced.

## Revisions

2026-08-25 · re-scored on the new ladder — Re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries Apertia Tech, Dativery and Alice by Redque [S4]. Apertia (trading since 2004, dozens of completed customer integrations across the Czech SMB ERPs) and Dativery (since 2016, the integration layer behind Digitoo) both pass the established test, so `scores.gap` stays 0 and the 2026-08-20 de-rank now rests on a receipt a machine can re-check; Redque s.r.o., incorporated in April 2022, is early. `scores.proof` 3 → 2, a genuine downgrade: only Workist passes the established test — Mercura and Ventura are under three years old, and turian, though older, cites no customer count, no public buyer, no Series A and no state listing. One established player in one market is rung 2, not rung 3, and the 'Solved elsewhere' paragraph no longer claims two. `score` 4 → 3. Second pass this date, merged here: `locals[]` converted from `status:` to the orthogonal `competes:` + `maturity:` pair. All three entries are `competes: direct`: Apertia's B2B Objednávky, Dativery's order and invoice extraction into ABRA Flexi and POHODA, and Redque's Alice each take an inbound order document and write it into a Czech ERP, which is this record's product for this record's buyer. Maturities are unchanged. `scores.gap` stays 0 on Apertia Tech and Dativery, both direct and established. No player was ever excluded from this ledger, so there is nothing to restore. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed.

2026-08-20 · gap re-check — De-ranked. The 2026-08-13 absence check behind gap 2 was recorded against a YC company page and returned only US/global tools plus "CZ generic AI agencies" [S2]; it never looked at what Czech vendors call this in Czech. Re-run against Czech-language search, the first query surfaced Apertia Tech s.r.o. selling a named B2B order-processing AI product with the exact Pohoda/ABRA/Helios/Money/K2 integration set that would have been the moat, plus Alice by Redque and Dativery doing the same extraction into the same ERPs [S4]. Gap 2 → 0 and score 6 → 4 under the SPEC §4 de-rank rule, status → watching; the who-pays and existing-non-solutions paragraphs were rewritten so the prose no longer contradicts the score. The record's remaining honest content is its proof: the wedge is funded in DE and the US, and it is also already being sold here.

2026-08-24 · evidence audit — Cut from Why now: "German-owned distributors operating in CZ already know the category, easing sales." The clause is the harvest note's own sales speculation [S1] — no signal, receipt or source documents any CZ distributor's awareness of anything, and buyer awareness is not a checkable fact. The Apertia incumbent receipt was re-verified live on this date (apertia.ai/b2b-objednavky-agent, HTTP 200) [S4]. Scores untouched.

2026-09-02 · plain-language pass — Glossed ERP, ABRA, RFQ and velkoobchod at first use; replaced SMB and ROI with plain words. Apertia's product line and its integration list are now separate sentences [S4]. Argument tightened 341 → 299 words, every [Sn] marker, figure and named company kept; Workist's €9M Series A added as the receipt behind "past seed". A gist now sits beside each of the four sources' why lines. No score, status, note or marker touched.
