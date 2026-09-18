---
id: p-0005
region: cz
title: 'Czech wholesalers type incoming orders into their systems by hand'
brief: 'Orders reach Czech wholesalers as e-mails, PDFs and spreadsheets, and staff type each line into their accounting software [S1,S4].'
solution: 'Build software that reads orders arriving by e-mail, PDF or Excel and enters them into the wholesaler''s accounting system.'
good_for: 'Someone who''d like to work with wholesalers and their accounting software.'
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
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: direct
  integration: software
  money: bootstrap
  why: 'Easier: wholesalers and suppliers sign for themselves, no licence is needed, and writing an order into the buyer''s own accounting system is ordinary software work. Harder: three Czech firms already sell this into the same accounting systems, so the field is crowded, and two of them have traded for ten years or more.'
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
process:
  summary:
    today: 'An order arrives as an e-mail, a PDF or a spreadsheet, and someone in sales reads it, looks up each item''s code and types the order into the accounting system [S1,S4].'
    after: 'The software matches each line to the wholesaler''s own item codes and writes the order into its system, and staff check the order instead of typing it.'
  steps:
  - who: Customer
    today: 'Sends an order by e-mail, PDF or Excel'
    known: documented
    cites: [1, 4]
    change: stays
    after: 'Unchanged: customers order the way they do now'
  - who: Sales staff
    today: 'Read each order and look up every item'
    known: documented
    cites: [1, 4]
    change: changes
    after: 'Check the items the software matched'
  - who: Sales staff
    today: 'Type the order into the accounting system'
    known: documented
    cites: [4]
    reenters: true
    change: goes
    after: null
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
- type: arbitrage
  name: "Asakana"
  gist: "the food-distributor order entry"
  why: "A US company listed by Y Combinator in August 2026 that turns e-mailed and texted orders into entries in food distributors' business systems: the same product, sold to a different trade."
  url: https://www.ycombinator.com/companies/asakana
  note: 'yc-asakana: YC-funded (31 Aug 2026) US company doing AI order entry from e-mail and
    text into ERP for food distributors — this record''s exact product shape, freshly funded
    abroad. Documents that the cluster is live; does NOT reopen the local field (Apertia Tech
    already sells this in CZ). Listing carries no founding year or traction, so arbitrage
    source only, no comps entry.'
  date: '2026-08-31'
  signal: yc-asakana
created: '2026-08-13'
updated: '2026-09-03'
---

Quote requests and orders reach Czech wholesalers as e-mails, PDFs and spreadsheets, and staff type them into their accounting software by hand [S1,S4].

- Staff read each order and look up every item's code themselves [S1,S4].
- Wholesalers and manufacturing suppliers both work this way [S1].
- Their systems include Pohoda, Helios and ABRA — Czech accounting and stock software [S1,S4].

A Czech seller of software for this lists the hand steps it replaces: reading each e-mailed request, searching the product database by name or code, matching each line to the firm's own item code, and filling in the order form [S4].

- In that seller's worked example, a building-materials wholesaler gets an e-mail listing bricks, mortar and lintels, and each line has to be matched to one of its own item codes [S4]. It is the same kind of buyer the Bavarian company under [Validated abroad](#validated-abroad) sells to [S1].
- The Bavarian company describes the same job at distributors: staff read each request, compare it with the product catalogue and pick the products by hand [S1].
- No source counts how many Czech wholesalers still type orders by hand, and no complaint from one has been found.

Existing non-solutions: Three Czech firms already sell software that reads orders into these accounting systems, and two have traded for ten years or more [S4].

- The oldest reads an order e-mail and writes it into the accounting system [S4].
- Its integrations cover Money and K2 as well as Pohoda, Helios and ABRA [S4].
- The other two read orders and invoices into the same systems [S4].
- On the way, the oldest matches each item to the buyer's catalogue and item codes, then replies with a confirmation and a delivery date [S4].
- So connecting to the Czech accounting systems gives a newcomer no head start: these firms already do it [S4].
- Generic Czech AI agencies such as Appmine also turn up in a web search for this, and so do foreign tools such as WizCommerce and one of the German companies under [Validated abroad](#validated-abroad) [S2].

Why now: A wholesaler's sales staff lose time on every order they type, and a slow reply can cost the sale [S1,S4].

- One Czech seller says each e-mailed request took 10–15 minutes by hand [S4].
- Typing each line again brings mistakes into the order [S1,S4].
- More orders mean more staff, because each one is typed by hand [S4].

The same seller counts a slow reply to the customer among the costs [S4]. The Bavarian company says the hand work keeps sales staff from selling and puts revenue at risk [S1].

Software for this keeps being funded abroad. Y Combinator, the US startup programme, backed teams for it in 2024 and 2025 [S1]. It backed two more in 2026, the latest listed in August [S3,S5].

Who pays: Yes: Czech firms already buy this from local vendors, and one vendor names dozens of completed customer integrations [S4].

- Wholesalers and suppliers decide and buy for themselves.
- Until they buy, they pay in staff time for every typed order [S1,S4].
- Abroad, distributors already pay for the same software; see [Validated abroad](#validated-abroad).

Solved elsewhere: Young, funded companies in Germany and the US already sell this software to distributors [S1,S3].

- A Bavarian company of about 20 people sells this to construction-supply distributors [S1].
- Comena and Seals AI, from Y Combinator too, do this in the US [S1].
- A two-person US team sells order entry that plugs into the distributor's system [S3].
- The Bavarian company came from Y Combinator's early-2025 batch, and handles quote requests as well as orders [S1].
- The US team came from the early-2026 batch, and handles quotes too [S3].
- Asakana, listed by Y Combinator in August 2026, turns e-mailed and texted orders into entries in US food distributors' business systems [S5].
- Of the four companies listed above, only the oldest has a funding round beyond seed money on record.
- Funding abroad opens no empty field here: three Czech firms already sell this [S4]; see [Competition](#competition).

## Revisions

2026-08-25 · re-scored on the new ladder — Re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries Apertia Tech, Dativery and Alice by Redque [S4]. Apertia (trading since 2004, dozens of completed customer integrations across the Czech SMB ERPs) and Dativery (since 2016, the integration layer behind Digitoo) both pass the established test, so `scores.gap` stays 0 and the 2026-08-20 de-rank now rests on a receipt a machine can re-check; Redque s.r.o., incorporated in April 2022, is early. `scores.proof` 3 → 2, a genuine downgrade: only Workist passes the established test — Mercura and Ventura are under three years old, and turian, though older, cites no customer count, no public buyer, no Series A and no state listing. One established player in one market is rung 2, not rung 3, and the 'Solved elsewhere' paragraph no longer claims two. `score` 4 → 3. Second pass this date, merged here: `locals[]` converted from `status:` to the orthogonal `competes:` + `maturity:` pair. All three entries are `competes: direct`: Apertia's B2B Objednávky, Dativery's order and invoice extraction into ABRA Flexi and POHODA, and Redque's Alice each take an inbound order document and write it into a Czech ERP, which is this record's product for this record's buyer. Maturities are unchanged. `scores.gap` stays 0 on Apertia Tech and Dativery, both direct and established. No player was ever excluded from this ledger, so there is nothing to restore. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed.

2026-08-20 · gap re-check — De-ranked. The 2026-08-13 absence check behind gap 2 was recorded against a YC company page and returned only US/global tools plus "CZ generic AI agencies" [S2]; it never looked at what Czech vendors call this in Czech. Re-run against Czech-language search, the first query surfaced Apertia Tech s.r.o. selling a named B2B order-processing AI product with the exact Pohoda/ABRA/Helios/Money/K2 integration set that would have been the moat, plus Alice by Redque and Dativery doing the same extraction into the same ERPs [S4]. Gap 2 → 0 and score 6 → 4 under the SPEC §4 de-rank rule, status → watching; the who-pays and existing-non-solutions paragraphs were rewritten so the prose no longer contradicts the score. The record's remaining honest content is its proof: the wedge is funded in DE and the US, and it is also already being sold here.

2026-08-24 · evidence audit — Cut from Why now: "German-owned distributors operating in CZ already know the category, easing sales." The clause is the harvest note's own sales speculation [S1] — no signal, receipt or source documents any CZ distributor's awareness of anything, and buyer awareness is not a checkable fact. The Apertia incumbent receipt was re-verified live on this date (apertia.ai/b2b-objednavky-agent, HTTP 200) [S4]. Scores untouched.

2026-09-02 · plain-language pass — Glossed ERP, ABRA, RFQ and velkoobchod at first use; replaced SMB and ROI with plain words. Apertia's product line and its integration list are now separate sentences [S4]. Argument tightened 341 → 299 words, every [Sn] marker, figure and named company kept; Workist's €9M Series A added as the receipt behind "past seed". A gist now sits beside each of the four sources' why lines. No score, status, note or marker touched.

2026-09-10 · likely solution — Added the one-sentence `solution:`, now required on every record and always shown as the likely solution, compressed from the existing non-solutions paragraph, locals[], build.note and the solved-elsewhere paragraph. No claim, score or source changed.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` on who is stuck and what is happening, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Czech SMB distributors and manufacturing suppliers re-type inbound RFQs and orders from e-mail, PDF and Excel into their ERPs by hand". Previous solution, verbatim: "Software for wholesalers and suppliers that reads quote requests and orders arriving by e-mail, PDF or Excel, matches each line to the firm's own item codes, and enters the order into its Pohoda, Helios or ABRA accounting and stock system." The record carried no brief and no good_for before this pass. Every claim was checked against this record's sources first. No source on file measures how much re-typing happens: the workflow rests on the harvest note behind [S1], and the Czech products sold to automate it [S4] show the work exists without counting it; this record scores demand 0. The copy therefore carries no "most", "many", count, cost or date, and names no deadline because the record has none. The old title's "SMB", "RFQs" and "ERPs" are replaced with plain words. Three Czech vendors already sell this, two of them established [S4]; the solution describes the product neutrally. No score, status, source, note, marker or body sentence changed. Simplified for the front page: title "Czech wholesalers type orders from e-mails, PDFs and spreadsheets into their systems by hand" → "Czech wholesalers type incoming orders into their systems by hand"; brief "Orders and quote requests reach Czech wholesalers and suppliers as e-mails, PDFs and spreadsheets, and staff type each line into accounting and stock software such as Pohoda, Helios or ABRA [S1,S4]." → "Orders reach Czech wholesalers as e-mails, PDFs and spreadsheets, and staff type each line into their accounting software [S1,S4]."; solution "Build software that reads orders arriving by e-mail, PDF or Excel and enters them into the wholesaler's accounting system, as companies already do in Germany." → "Build software that reads orders arriving by e-mail, PDF or Excel and enters them into the wholesaler's accounting system."; good_for "Someone who'd like to work with wholesalers and the accounting software they run on." → "Someone who'd like to work with wholesalers and their accounting software.". The named accounting products and "quote requests" were cut; no claim was added.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the hand typing and keeps the three accounting systems with their gloss [S1,S4]; the "no complaint is documented" line moved there from Solved elsewhere, reworded without "the demand case is structural". Competition opens on the three Czech sellers and describes them by what they sell, with their names, years and the Digitoo link left to their `locals[]` rows; the product steps, the integration list and the building-materials worked example stay [S4]; "integration ... was the planned defence" became "connecting to the Czech accounting systems gives a newcomer no head start" [S4]. Why now opens on who loses time and the sale, with the funding abroad below as detail [S1,S3,S5]. Validated abroad describes each foreign company without its name; Mercura, turian, Workist and Ventura left the body for their `comps[]` rows, Workist's €9M Series A with them, and Apertia Tech, Alice by Redque and Dativery left it for `locals[]`. `entry.why` is now "Easier: … Harder: …" and names no company. S5 gained a public `name`, `gist` and `why` beside its unchanged note, and is now cited [S5]. Added from the pages behind sources already on file, both read on this date and neither in its note: the hand steps the Czech seller lists ("Manuální čtení každého e-mailu s poptávkou", "Ruční vyhledávání produktů v databázi podle názvu nebo kódu", "Ruční vyplňování objednávkových formulářů", "Lidské chyby při přepisování dat", "Zdlouhavá reakce na zákazníky", "Nemožnost zpracovat větší objem poptávek bez navyšování týmu"), its worked example's bricks, mortar and lintels, and its "Každá poptávka vyžadovala 10-15 minut manuální práce", written as the seller's own claim [S4]; and the Y Combinator page's description of inside sales teams reading each request against the catalogue by hand, delaying replies and risking revenue [S1]. Process figure added, three steps, all `documented`: the customer sends the order [S1,S4]; sales staff read it and look up each item [S1,S4]; sales staff type it into the accounting system, marked `reenters` and `goes` [S4]. The "sales staff" role is S1's page's word; S4's page names no role. Corrected against the sources: "A Czech product already sells this" cited [S2], the first sweep, which found none, so it now cites [S4]; "caps how many quotes a desk turns around" was cited to [S1], whose page says the hand work keeps staff from selling, and the capacity point is S4's page, now cited there [S1,S4]; "a quote returned first wins the order" has no source and became S1's "delaying responses … risk of lost revenue" and S4's slow reply; "AI document extraction is commodity" has no source and was cut, the funding dates standing in its place [S1,S3,S5]; S2's note says only that searches returned Appmine, WizCommerce and turian, so "writing one-off scripts" and "no Czech integrations or language handling" were cut; and "only Workist … is three years in and past seed" carried no marker and Ventura's funding beyond Y Combinator is undisclosed, so the body now says only the oldest has a round beyond seed "on record". Flagged as inference: that Czech firms already buy this rests on S4's "dozens of completed customer integrations", with no price or contract on file [S4]; that distributors abroad pay for it rests on the `comps[]` traction lines, not on a source; and that wholesalers decide and buy for themselves rests on `entry.buyer`. No score, status, entry gate, source order, `note:`, title, brief, solution or good_for changed.
