---
id: p-0030
region: cz
title: Only eleven Czech crypto firms got licensed; the rest must wind down
fix: 'A packaged wind-down for the crypto firms that did not get licensed: notify
  customers, move their coins and cash to a licensed provider, and close the records and
  the tax to a standard the regulator will accept.'
category: fintech
geo: CZ-national
score: 4
scores:
  proof: 0
  money: 0
  urgency: 3
  demand: 0
  gap: 1
status: candidate
build:
  capital: kiosk
  first_revenue: weeks
  builder: small-team
  note: 'Consulting-led wind-down execution sells immediately to hundreds of exposed firms under live ČNB enforcement — the cost is regulatory expertise and playbooks, not capital; a recurring compliance-ops product is a later, bigger build.'
comps: []
locals:
- name: Finreg Partners
  url: https://www.finregpartners.cz/
  ico: '07123949'
  since: 2018
  status: early
  evidence: 'EARLY for this space — it writes licence applications, standing behind three of the eleven
    CASP permissions ČNB granted [S3], which is the opposite service to winding a firm down;
    ARES registration 2018-05-15. No limb of the established test is met by anything on file
    here: nothing names who has bought it, no published tally exists, there is no pairing in
    data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no state listing.'
- name: ARROWS
  url: https://www.arws.cz/
  ico: '06717586'
  since: 2018
  status: early
  evidence: 'EARLY for this space — licence applications and compliance policies on law-firm economics
    [S3,S4], not a wind-down or asset-migration product; ARES registration 2018-01-01. No
    limb of the established test is met by anything on file here: nothing names who has
    bought it, no published tally exists, there is no pairing in
    data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no state listing.'
- name: AMS Europe
  url: https://www.amseurope.cz/
  ico: '14394243'
  since: 2022
  status: early
  evidence: 'EARLY for this space — licence applications and policies [S3,S4], not a wind-down product;
    ARES registration 2022-03-30. No limb of the established test is met by anything on file
    here: nothing names who has bought it, no published tally exists, there is no pairing in
    data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no state listing.'
- name: kryptoregulace.cz (Blockchain Legal)
  url: https://www.kryptoregulace.cz/
  ico: '06297013'
  since: 2017
  status: early
  evidence: 'EARLY for this space — the site states outright that it is informational with no platform
    behind it, run by Blockchain Legal with AML Systems, Binary Confidence and CITADELO
    [S4]; ARES registration 2017-07-26. No limb of the established test is met by anything
    on file here: nothing names who has bought it, no published tally exists, there is no
    pairing in data/lookup/cz-contract-parties.jsonl, no round at Series stage, and no state
    listing.'
- name: Stuchlíková & Partners
  url: https://www.stuchlikova.com/en/specialization/cnb-licenses/crypto-asset-service-provider-mica/
  status: early
  evidence: 'EARLY on receipts only — publishes what a CASP licence takes (€50,000–150,000
    initial capital, 1–2 months of documentation, a 3–6 month ČNB process) but prices the
    engagement only on request [S6]; no customer count, public-buyer pair, round or state
    listing on file'
sources:
- type: regulation
  name: "ČNB — end of the MiCA transition period"
  why: "The central bank's warning: from 1 July 2026 only licensed firms may serve clients, everyone else must cease and transfer customer crypto and funds. Fines can exceed CZK 100M."
  url: https://www.cnb.cz/cs/cnb-news/aktuality/Upozorneni-Ceske-narodni-banky-Konec-prechodneho-obdobi-podle-narizeni-MiCA-k1.7.2026/
  note: 'reg-mica-casp-cz: ČNB warning — the MiCA grandfathering period in Czechia ended 1
    Jul 2026; only CASP-licensed firms may serve clients, others must cease activity and transfer
    customer crypto and funds to licensed providers or self-custody. ČNB fines can exceed
    CZK 100M; licensing projects cost CZK 1-5M per firm. In force with active supervisory
    enforcement: deadline sub-score 2, urgency 3 with freshness.'
  date: '2026-07-01'
  signal: reg-mica-casp-cz
- type: news
  name: "ČNB — eleven crypto licences granted"
  why: "The regulator's own tally: 251 applications assessed, 204 filed inside the transitional period, 11 permissions granted. The licensed set is two orders of magnitude smaller than the affected one."
  url: https://www.cnb.cz/cs/cnb-news/tiskove-zpravy/MiCA-CNB-udelila-kryptolicenci-11-subjektum/
  note: 'ČNB press release: 11 CASP licences granted — against a former population of hundreds
    of trade-licence (živnost) crypto providers under the pre-MiCA regime (per the reg signal).
    The licensed set is two orders of magnitude smaller than the affected set: the market
    structure receipt for the wind-down/migration problem.'
  date: '2026-08-13'
- type: gap-check
  name: "Finreg Partners and the Czech licensing-advisory field"
  why: "Names who already sells into this: Finreg Partners (behind three of the eleven licences), ARROWS, Kopečný & Partners and AMS Europe — all selling applications and policies as services."
  url: https://zpravy.kurzy.cz/864080-finreg-partners-jako-prvni-v-cesku-stoji-za-tremi-licencemi-mica/
  note: 'Gap check 2026-08-13: the supply side is licensing advisory — Finreg Partners (behind
    3 of the 11 licences), ARROWS, Kopečný & Partners, AMS Europe sell licence applications
    and compliance consulting as services; no CZ product for customer-asset migration, wind-down
    execution, or ongoing CASP compliance operations (safeguarding, DORA, AML reporting) was
    found. Gap 1 (quick search, services-only incumbents named).'
  date: '2026-08-13'
- type: gap-check
  name: "kryptoregulace.cz and the Czech MiCA supply side"
  why: "A deeper Czech sweep for wind-down and compliance-operations products. Everything Czech it found is advisory; the product-shaped answers — MarketGuard, AMLBot, Sigma360 — are all foreign."
  url: https://www.kryptoregulace.cz/
  note: 'Gap re-check 2026-08-20: NOT FOUND, score unchanged. Looked for a Czech product for
    wind-down execution, customer-asset migration, or ongoing CASP compliance operations
    (safeguarding, DORA, MiCA-grade AML and reporting). Every Czech offering found is advisory:
    kryptoregulace.cz is run by Blockchain Legal, advokátní kancelář s.r.o. with AML Systems,
    Binary Confidence and CITADELO and states outright that the site is informational, with
    no platform behind it; Schejbal & Partners, ARROWS, AMS Europe, Key2Law and PROFI
    Poradenství sell licence applications and policies on the same law-firm economics as the
    incumbents already named on this record. Product-shaped answers exist but none is Czech:
    MarketGuard sells CASP onboarding, AML and blockchain transaction monitoring and
    regulatory reporting with no Czech entity, address or ČNB reference disclosed, and
    AMLBot, KYC-Chain, Sigma360, Trusty and CertiK cover the same ground EU-wide. Our own
    funded ledger holds Czech crypto operators (Confirmo, Tatum) and Slovak Blockmate, none
    of them a compliance-operations vendor. The ČNB press release was read directly for the
    licensed population: 251 applications assessed, 204 filed inside the transitional period,
    11 permissions granted, Binance among those that failed. IMPORTANT: this is a not-found,
    not a proven absence, and a negative never raises a gap score. Gap stays 1 with its
    coverage now recorded. Method control passed first at Wultra (p-0017) and Softlink (p-0026).'
  date: '2026-08-20'
  queries:
    - "MiCA compliance software Česko poskytovatel kryptoslužeb ukončení činnosti převod klientských aktiv"
    - "český nástroj compliance kryptoburza CASP reporting AML transakční monitoring krypto software"
    - "česká platforma compliance pro kryptofirmy safeguarding klientských aktiv DORA MiCA produkt"
    - "Česko kryptofirmy bez licence ukončení činnosti pomoc migrace klientů nástroj řešení 2026"
    - "Czech company software CASP wind-down client asset migration MiCA compliance operations product"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: statistic
  name: "ČNB — 2025 supervision report, crypto"
  why: "The regulator's own count of the pre-MiCA population: roughly 30,000 subjects held the free virtual-asset trade licence, about 5,000 of them companies — but only 188 kept the right to trade through the transitional period."
  url: https://www.cnb.cz/export/sites/cnb/cs/dohled-financni-trh/.galleries/souhrnne_informace_fin_trhy/zpravy_o_vykonu_dohledu/download/dnft_2025_cz.pdf
  note: 'Research 2026-08-25: ČNB Zpráva o výkonu dohledu nad finančním trhem 2025 (published
    17 Jun 2026), Box 5 — "tato živnost byla zaregistrována přibližně 30 tisícům subjektů,
    z čehož přibližně pět tisíc subjektů byly právnické osoby" and "Možnost poskytovat služby
    v přechodném období byla v ČR zachována 188 subjektům". The same box records the 2025
    funnel: 245 applications, 210 filed by 31 Jul 2025 (205 in July alone), 184 first-instance
    proceedings closed, 171 terminated (117 incomplete, 28 unpaid fee, 17 withdrawn, 13 filed
    by unsigned e-mail), only 11 reaching substantive review and 0 licences granted in 2025.
    Bounds the affected population this record is about; not a receipt for its money score.'
  date: '2026-06-17'
- type: statistic
  name: "Stuchlíková & Partners — what a CASP licence takes"
  why: "A Czech law firm's own page on the licence: initial capital of €50,000–150,000, one to two months of preparation and a three-to-six-month central-bank process. It publishes no fee, and neither does anyone else in this market."
  url: https://www.stuchlikova.com/en/specialization/cnb-licenses/crypto-asset-service-provider-mica/
  note: 'Research 2026-08-25: the Stuchlíková & Partners CASP page states initial capital of
    EUR 50,000-150,000, documentation preparation of 1-2 months and a ČNB process of 3-6 months,
    and prices the engagement only on request. Four Czech advisory pages were loaded on this
    date — Schejbal & Partners, Stuchlíková & Partners, estrella.ma and Finreg Partners — and
    none publishes a price; a "from EUR 29,000" figure seen in search snippets was not verified
    on any loaded page and is deliberately not carried here. Grounds the plain statement in
    the body that no Czech price is on file; it is not a receipt for any score.'
  date: '2026-08-25'
created: '2026-08-13'
updated: '2026-08-25'
---

Czechia let crypto services run on a plain trade licence, and roughly 30,000 subjects registered for one [S5]. That regime ended on 1 July 2026: only CASP-licensed firms may serve clients, and ČNB has licensed eleven [S1,S2]. Everyone else must stop and move customer crypto-assets and funds to a licensed provider or to the customer's own custody [S1] — an orderly wind-down most small providers have never run.

Why now: the cliff is behind us, not ahead. Trading unlicensed now risks fines above CZK 100M [S1], and the gate is narrow by count: ČNB assessed 251 applications and granted 11 [S2,S4]. Most applications never reached substantive review — 171 of 184 first-instance proceedings closed in 2025 were terminated on procedural defects [S5]. What is left of 2026 sorts the survivors into three bins: migrate into a licensed structure, wind down cleanly, or drift into illegality.

Who pays: firms leaving the market, first and on a clock, for customer notification, asset-transfer mechanics, records and tax closure done defensibly. The population is smaller than the trade register suggests, and it is countable: 188 subjects kept the right to trade through the transitional period, and eleven came out licensed [S5,S2]. That is roughly 175 exits, each a one-off. The eleven licensees need the opposite, something recurring — safeguarding of client assets, DORA resilience, MiCA-grade AML and reporting [S1,S3]. No Czech firm publishes a price for either job [S6], so no revenue figure is claimed here. The third buyer is the licensed incumbent, acquiring orphaned customer books.

Existing non-solutions: licensing advisory, sold as a service. Finreg Partners stands behind three of the eleven licences, and ARROWS, Kopečný & Partners and AMS Europe write applications and policies on law-firm economics [S3]. Every one of them sells getting licensed; nobody sells getting out. A Czech-language search for a productised wind-down, asset-migration or compliance-operations offering returned only more advisory [S4].

Solved elsewhere: nothing. No foreign comparable of any maturity is on file — not an established seller, not a funded prototype, nothing. No company anywhere has been documented productising crypto wind-down or customer-asset migration. The MiCA tooling that does exist sells to firms that stay in business: MarketGuard, AMLBot, KYC-Chain, Sigma360 and CertiK cover onboarding, AML and transaction monitoring EU-wide, none of them Czech and none of them an exit product [S4]. This wedge is carried by a live deadline, not by a proven template.

## Revisions

2026-08-20 · evidence audit — Three unbacked claims removed from the framing. "one of Europe's loosest crypto regimes": a cross-EU comparison the register never ran, and neither ČNB source makes any comparative claim about other member states. "from exchanges and brokers to ATM operators": the enumeration follows the marker and has no receipt — the signal says only that hundreds of former živnost-based providers are affected. "with bank-licence-grade scrutiny": nothing in the corpus compares CASP licensing to bank licensing. The money figures in the same paragraph are not affected — the fine ceiling and the licensing project cost are both carried verbatim in the ČNB regulation signal and stay cited [S1].

2026-08-24 · fact check — The licensing-cost claim, "a licence application is a CZK 1-5M project", is gone. The 2026-08-20 audit kept it as carried by the regulation signal, but the signal's only URL is the ČNB warning, which was fetched on this date and does not state it; nor does the licensing-advisory article on this ledger [S3], and it verifies nowhere else on file. The fine ceiling stays — it is on the ČNB page verbatim ("pokut, jejichž horní hranice přesahuje 100 milionů Kč") [S1]. The narrow gate is now stated from receipted numbers instead: 251 applications assessed, 11 granted, both confirmed live on the ČNB press release [S2,S4].

2026-08-25 · board-brief rewrite — The missing `Solved elsewhere:` lead-in was written. Without it the Proven abroad section rendered as an empty ledger and the closing paragraph — which is where the foreign evidence actually lived — fell into local competition. The paragraph now says plainly that `comps` is empty, that no funded company has been documented productising crypto wind-down or customer-asset migration anywhere, and that the EU-wide MiCA tooling on file (MarketGuard, AMLBot, KYC-Chain, Sigma360, CertiK) sells to firms that stay in business rather than to firms exiting [S4]. "How big" now states a bounded population instead of "a few hundred": 204 filings inside the transitional period against 11 licences granted [S2,S4], so roughly 200 one-off exits plus eleven recurring licensees — and states outright that no Czech price for either job is published, so no revenue figure is offered. Argument cut from 341 to ~340 words with the marker clots broken up. Every source gained a public name and why line; scores, status and internal notes untouched. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by that pass. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and neither dimension moved. `scores.proof` stays 0 on the plainest reading of rung 0 — `comps` is empty and no foreign player of ANY maturity is on file, early or established. Rung 1 was considered and does not apply: it needs early foreign players, and there are none; the EU-wide MiCA tooling in [S4] sells to firms staying in business, not exiting, so it is not a comparable for this wedge at all. `scores.gap` stays 1. Five Czech advisory firms were lifted out of the [S3], [S4] and [S6] scan prose into a structured `locals[]` ledger, and only one is established: Finreg Partners (IČO 07123949, ARES 2018) on the public-customer-count limb, standing behind three of the eleven licences ČNB granted. ARROWS, AMS Europe, kryptoregulace.cz and Stuchlíková & Partners publish no customer count, pair with no public buyer in `data/lookup/cz-contract-parties.jsonl`, and carry no round or state listing, so all four read early on receipts. Finreg being established does not drop gap to 0, because rung 0 requires an established local player that ALREADY SELLS THIS, and every firm on the ledger sells the opposite service — getting licensed, not winding down. Gap does not rise to 2 either: [S4] is a proper check with recorded `queries[]` and `checked[]`, but it found local players rather than none, and its own note says so. `score` unchanged at 4. The non-solutions paragraph now states the licensed-versus-exit distinction that the gap score turns on, and the Proven-abroad paragraph says the comps ledger is empty of early players too, not just established ones. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.
