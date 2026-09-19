---
id: p-0030
region: cz
title: 'Since July, all but 11 Czech crypto firms must stop serving clients'
brief: 'Unlicensed firms must hand their customers'' coins and cash to a licensed firm or back to the customer [S1]. Those that keep trading risk fines above 100M CZK [S1].'
solution: 'Build a fixed-price service that winds down an unlicensed crypto firm: tells customers, moves their coins and cash, closes the records.'
good_for: 'Someone who knows crypto wallets and exchanges and likes careful paperwork.'
category: fintech
geo: CZ-national
score: 3
scores:
  proof: 0
  money: 0
  urgency: 2
  demand: 0
  gap: 1
status: candidate
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: departing firms buy for themselves; no licence is needed to sell them the help; the established adviser nearby sells licences, not exits; and the work is notices, transfers and records, not a system to plug into. Harder: a Czech law firm already offers to guide the exit, and no price for the job is published.'
comps: []
locals:
- name: SCHEJBAL&PARTNERS
  url: https://akschejbal.cz/kryptoaktiva-mica
  since: 2026
  competes: direct
  maturity: early
  evidence: It is the one Czech firm found selling the exit rather than the entry. On 18 June
    2026 it published a section headed "Připravte si wind-down plán", set out the four duties
    an unlicensed provider must discharge — move customer crypto-assets and money to an authorised
    provider or the customer's own wallet, tell every client in time how the settlement will run,
    keep meeting anti-money-laundering duties until the last day, and be ready to report the settlement
    to ČNB on request — and closed by naming "příprava řízeného odchodu z trhu" among the things
    it will guide a client through [S7]. The offering is weeks old because the duty is, and its
    standing MiCA page still sells only the entry side — FAÚ permission, whitepaper, CASP licence
    application — naming Coinero as a licence client [S7].
- name: Finreg Partners
  url: https://www.finregpartners.cz/
  ico: '07123949'
  since: 2018
  competes: adjacent
  maturity: established
  evidence: It sells licence applications — the work of GETTING a CASP permission, which is the
    opposite job to winding a firm down and moving its customers' assets out [S3]. Its MiCA page
    was read line by line on 2026-08-25 and carries no exit, wind-down or client-settlement service
    at all; what it has added instead is due-diligence advice for firms ACQUIRING a CASP, which
    serves the buyer of an orphaned book rather than the firm leaving [S7]. Trading since 15 May
    2018, with 3 licensed CASP clients — Finreg stands behind three of the eleven permissions
    ČNB has granted [S3].
- name: ARROWS
  url: https://www.arws.cz/
  ico: '06717586'
  since: 2018
  competes: adjacent
  maturity: early
  evidence: It sells licence applications and compliance policies on law-firm economics [S3,S4]
    — getting a firm licensed, not getting one out. It writes about the wind-down duty, but as
    commentary, and what it offers off the back of it is help deciding whether and how MiCA applies
    to a business model [S7]. Trading since 2018; it names no client and publishes no count.
- name: AMS Europe
  url: https://www.amseurope.cz/
  ico: '14394243'
  since: 2022
  competes: adjacent
  maturity: early
  evidence: It sells licence applications, company formation and anti-money-laundering policies
    [S3,S4,S7] — again the entry side, not a wind-down. Trading since 30 March 2022; it names
    no client and publishes no count.
- name: Kopečný & Partners
  url: https://www.kopecnypartners.com/
  competes: adjacent
  maturity: early
  evidence: It sells legal advice on providing crypto-asset services under MiCA, written for firms
    working out which permission they need and how to keep client assets segregated once they
    hold one [S3,S7] — the staying-in-business side. No start year, no named clients and no count
    are published.
- name: Key2Law
  url: https://key2law.com/en/licences/mica/mica
  competes: adjacent
  maturity: early
  evidence: It sells CASP licensing support and crypto company setup in Czechia, and publishes
    a case study of taking a Czech crypto-wallet startup through MiCA readiness and the ČNB application
    [S7] — the entry side, sold to firms that intend to stay. Beyond that one anonymised study
    it names no client, publishes no count and has no start year on file.
- name: PROFI Poradenství & Finance
  url: https://www.profipf.cz/
  competes: adjacent
  maturity: early
  evidence: It sells financial and regulatory advisory and publishes explainers on the ČNB licensing
    round [S4,S7] — reading material plus consulting hours aimed at firms pursuing a permission,
    with nothing sold to a firm on its way out. No start year, no named clients and no count are
    published.
- name: kryptoregulace.cz (Blockchain Legal)
  url: https://www.kryptoregulace.cz/
  ico: '06297013'
  since: 2017
  competes: adjacent
  maturity: early
  evidence: 'What it supplies is reading material: the site states outright that it is informational
    with no platform behind it, run by Blockchain Legal with AML Systems, Binary Confidence and
    CITADELO [S4]. The firm''s own crypto practice page lists six services — exchanges and bureaux,
    mining and node operation, portfolio management, trading, crypto inside a business, and inheritance
    — and no exit, wind-down or client settlement among them [S7]. Trading since 26 July 2017;
    it names no client and publishes no count.'
- name: Stuchlíková & Partners
  url: https://www.stuchlikova.com/en/specialization/cnb-licenses/crypto-asset-service-provider-mica/
  competes: adjacent
  maturity: early
  evidence: It sells CASP licensing work as a law firm and publishes what a licence takes — €50,000–150,000
    initial capital, 1–2 months of documentation, a 3–6 month ČNB process — but prices the engagement
    only on request [S6]. Again the entry side, not the exit; no start year, no named clients
    and no count are published.
sources:
- type: regulation
  name: "ČNB — end of the MiCA transition period"
  gist: "the 1 July 2026 cutoff"
  why: "The central bank's warning: from 1 July 2026 only licensed firms may serve clients, everyone else must cease and transfer customer crypto and funds. Fines can exceed CZK 100M."
  url: https://www.cnb.cz/cs/cnb-news/aktuality/Upozorneni-Ceske-narodni-banky-Konec-prechodneho-obdobi-podle-narizeni-MiCA-k1.7.2026/
  note: 'reg-mica-casp-cz: ČNB warning — the MiCA grandfathering period in Czechia ended 1
    Jul 2026; only CASP-licensed firms may serve clients, others must cease activity and transfer
    customer crypto and funds to licensed providers or self-custody. ČNB fines can exceed
    CZK 100M; licensing projects cost CZK 1-5M per firm. In force with active supervisory
    enforcement: deadline sub-score 2, urgency 3 with freshness.
    Corrected 2026-09-19: the deadline sub-score and the freshness point are retired. On the
    2026-09-19 ladder this is REAL (MiCA binds the unlicensed provider) and CLOSE (the date passed
    2.5 months before), so urgency 2. TEETH needs, for a passed date, fines levied or proceedings
    opened within 12 months; this page is a warning naming the fine ceiling, and no enforcement
    receipt is on file, so not 3.'
  date: '2026-07-01'
  signal: reg-mica-casp-cz
- type: news
  name: "ČNB — eleven crypto licences granted"
  gist: "11 licences from 251 filings"
  why: "The regulator's own tally: 251 applications assessed, 204 filed inside the transitional period, 11 permissions granted. The licensed set is two orders of magnitude smaller than the affected one."
  url: https://www.cnb.cz/cs/cnb-news/tiskove-zpravy/MiCA-CNB-udelila-kryptolicenci-11-subjektum/
  note: 'ČNB press release: 11 CASP licences granted — against a former population of hundreds
    of trade-licence (živnost) crypto providers under the pre-MiCA regime (per the reg signal).
    The licensed set is two orders of magnitude smaller than the affected set: the market
    structure receipt for the wind-down/migration problem.'
  date: '2026-08-13'
- type: gap-check
  name: "Finreg Partners and the Czech licensing-advisory field"
  gist: "the licensing-advisory field"
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
  gist: "the Czech supply-side sweep"
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
  gist: "the 30,000-subject population"
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
  gist: "€50–150k capital, 3–6 months"
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
- type: gap-check
  name: "Who sells the way out — Czech supply, searched again"
  gist: "the one wind-down seller"
  why: "A wider Czech sweep for anyone selling the exit rather than the licence. Every Czech
    service menu it read sells getting licensed, and one law firm has started offering to
    prepare an orderly departure from the market."
  note: 'Czech-language sweep 2026-08-25, run because the check on this file dated 2026-08-13
    recorded no queries and closed with the words "quick search", which is not coverage anyone
    can judge. POSITIVE CONTROL PASSED, run before any conclusion was drawn: query 2, phrased
    as a firm looking for licensing help, returned finreg.cz/mica-licence at the top of the
    first page — Finreg Partners, the established Czech player already on this ledger and the
    firm behind three of the eleven permissions — together with SCHEJBAL&PARTNERS and
    modernipravnik.cz. The method reaches Czech advisory supply in this exact niche. WHAT WAS
    LOOKED FOR: anyone selling a firm its way OUT — customer notification, transfer of client
    crypto-assets and funds to a licensed provider or self-custody, records and tax closed to a
    standard ČNB will accept — or ongoing compliance operations for the eleven that stayed.
    SERVICE MENUS READ LINE BY LINE, not searched at: Finreg''s MiCA page (no exit service of
    any kind; it has added due-diligence advice for firms ACQUIRING a CASP, which serves the
    acquirer of an orphaned book, not the firm leaving), Blockchain Legal''s crypto practice
    page (six services, none an exit), SCHEJBAL&PARTNERS'' MiCA page (FAÚ permission,
    whitepaper, CASP licence application — entry side only, and it names Coinero as a licence
    client). ONE POSITIVE FINDING, and it is what holds the score down: SCHEJBAL&PARTNERS
    published an article on 18 Jun 2026 headed "Připravte si wind-down plán" which sets out
    the four duties of a controlled exit and closes by naming "příprava řízeného odchodu z
    trhu" among the things the firm will guide a client through. That is this job sold to this
    buyer, by the hour, and it is recorded at competes: direct. It is EARLY and cannot be
    anything else: the duty is weeks old, so no seller can meet the three-year limb. ARROWS
    writes about the wind-down duty as commentary and offers scoping help off the back of it,
    which is not the same thing and is recorded as adjacent. NOT FOUND: no packaged, priced or
    repeatable wind-down offering, Czech or foreign, and no Czech compliance-operations
    product for the eleven licensees — the AML and monitoring tooling that exists (Alessa,
    AMLBot and the rest) is foreign and sells to firms staying in business. Kopečný & Partners,
    Key2Law and PROFI Poradenství & Finance were named in earlier notes on this file without
    ever reaching the ledger; all three are added here. gap STAYS 1 and does not move to 2: a
    named Czech firm advertises this job, so the field is contested rather than empty, and the
    honest rung is the lower one.'
  url: https://akschejbal.cz/konec-krypto-sluzeb-bez-licence-od-leta-2026
  date: '2026-08-25'
  queries:
    - 'nezískali jsme licenci ČNB kryptoaktiva ukončení činnosti převod klientů a jejich kryptoměn na licencovaného poskytovatele pomoc'
    - 'poradenství licence poskytovatele služeb kryptoaktiv ČNB MiCA žádost pomoc firmám Česko'
    - 'odkup klientů kryptosměnárny převzetí klientského portfolia licencovaný poskytovatel kryptoaktiv Česko nabídka'
    - 'česká firma software AML monitoring transakcí a reporting pro kryptofirmy a platební instituce nástroj'
    - '"wind-down" plán ukončení činnosti poskytovatele kryptoaktiv ČNB právní pomoc advokátní kancelář nabídka Česko 2026'
  checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-09-19'
---

Only 11 Czech crypto firms won the new EU licence, and every other provider must stop serving clients [S1,S2].

- About 30,000 people and firms held the old, free crypto trade licence [S5].
- 188 of them kept the right to trade until July 2026 [S5].
- Each firm without a licence must move its clients' coins and cash out [S1].

Czechia let crypto services run on a plain trade licence, and about 5,000 of its holders were companies [S5]. The new rules are MiCA, the EU's rulebook for crypto-assets [S1]. Under it a firm needs a licence as a crypto-asset service provider, and in Czechia the central bank grants it [S1,S2].

A firm without that licence must stop the service and move its customers' coins and cash to a licensed provider or to the customer's own wallet [S1]. The central bank's warning asks it to stop the service, not to close the company [S1].

Existing non-solutions: Czech advisers sell getting licensed, not getting out, and one law firm has offered since June 2026 to guide an exit [S3,S7].

- One established adviser stands behind 3 of the 11 licences granted [S3].
- Five more law and advisory firms sell licence applications and compliance policies [S3,S7].
- Their service menus cover getting licensed, not getting out [S7].

They all sell it on law-firm terms, as advice rather than a product [S3,S7]. The established adviser has added due-diligence advice for firms buying a crypto provider, which serves the buyer of a departing firm's customers rather than the firm leaving [S7].

The one exception published an article in June 2026 telling departing providers to prepare a wind-down plan [S7]. It set out the plan's four duties and offered to guide firms through them, by the hour [S7]. The offer is weeks old, because the duty is [S7].

Nothing here is packaged, priced or repeatable [S6,S7].

Why now: The deadline is behind them: since 1 July 2026 an unlicensed crypto firm must stop serving clients and move their coins and cash out [S1].

- A firm that keeps serving clients unlicensed risks a fine above 100M CZK [S1].
- A departing firm must tell every client in time how settlement will run [S7].
- A departing firm's anti-money-laundering duties last to its final day [S7].

It must also move every client's assets out, as [The opportunity](#opportunity) says, and be ready to report the settlement to the central bank on request [S7]. Those are the four duties of a wind-down [S7].

Most applicants never had their licence judged on its merits [S5]. Of the 184 licence proceedings the central bank closed in 2025, it stopped 171, 117 of them because the application was incomplete [S5]. Binance was among the applicants that failed [S4].

The dates behind this:

- In 2025 the central bank received 245 licence applications, 210 of them by 31 July 2025 and 205 in July alone, and granted none that year [S5].
- On 1 July 2026 the transitional period ended, and only licensed firms may now serve clients [S1].
- By August 2026 the central bank had assessed 251 applications, 204 of them filed inside the transitional period, and granted 11 [S2,S4].

Who pays: No Czech price for a wind-down is published yet: the one law firm offering it bills by the hour [S6,S7].

- The buyers are the firms that traded until July without winning a licence [S1,S5].
- Firms already pay law firms and advisers to get licensed, the opposite job [S3].
- Licensed firms that take over departing firms' customers may pay too [S7].

Not every licensed firm need have been among the 188, so the number of firms leaving is not simply the difference [S2,S5]. The departing firms are on a clock [S1]. The job is customer notices, asset transfers, and records and tax closed so that they hold up.

The 11 licensed firms need the opposite, recurring work [S1,S3]. That means keeping client assets safe and separate, meeting DORA (the EU's rules on IT resilience in finance), and anti-money-laundering reporting to the new EU standard [S1,S3].

Four Czech advisers' pages show no price for either job, so no revenue figure is claimed [S6].

Solved elsewhere: Nobody abroad is known to sell a crypto firm's wind-down as a product, so there is no template to copy [S4,S7].

No foreign company has been found selling it, young or established, and nobody is known to sell the move of customer assets as a product either [S7]. The EU crypto-rule tools that exist sell to firms staying in business [S4]:

- MarketGuard, AMLBot, Sigma360 and CertiK cover sign-up checks, anti-money-laundering and transaction monitoring across the EU [S4].
- KYC-Chain (identity checks at sign-up) covers the same ground [S4].
- None of them is Czech, and none sells an exit [S4].

This opportunity rides a live deadline, not a proven template.

## Revisions

2026-08-20 · evidence audit — Three unbacked claims removed from the framing. "one of Europe's loosest crypto regimes": a cross-EU comparison the register never ran, and neither ČNB source makes any comparative claim about other member states. "from exchanges and brokers to ATM operators": the enumeration follows the marker and has no receipt — the signal says only that hundreds of former živnost-based providers are affected. "with bank-licence-grade scrutiny": nothing in the corpus compares CASP licensing to bank licensing. The money figures in the same paragraph are not affected — the fine ceiling and the licensing project cost are both carried verbatim in the ČNB regulation signal and stay cited [S1].

2026-08-24 · fact check — The licensing-cost claim, "a licence application is a CZK 1-5M project", is gone. The 2026-08-20 audit kept it as carried by the regulation signal, but the signal's only URL is the ČNB warning, which was fetched on this date and does not state it; nor does the licensing-advisory article on this ledger [S3], and it verifies nowhere else on file. The fine ceiling stays — it is on the ČNB page verbatim ("pokut, jejichž horní hranice přesahuje 100 milionů Kč") [S1]. The narrow gate is now stated from receipted numbers instead: 251 applications assessed, 11 granted, both confirmed live on the ČNB press release [S2,S4].

2026-08-25 · board-brief rewrite — The missing `Solved elsewhere:` lead-in was written. Without it the Proven abroad section rendered as an empty ledger and the closing paragraph — which is where the foreign evidence actually lived — fell into local competition. The paragraph now says plainly that `comps` is empty, that no funded company has been documented productising crypto wind-down or customer-asset migration anywhere, and that the EU-wide MiCA tooling on file (MarketGuard, AMLBot, KYC-Chain, Sigma360, CertiK) sells to firms that stay in business rather than to firms exiting [S4]. "How big" now states a bounded population instead of "a few hundred": 204 filings inside the transitional period against 11 licences granted [S2,S4], so roughly 200 one-off exits plus eleven recurring licensees — and states outright that no Czech price for either job is published, so no revenue figure is offered. Argument cut from 341 to ~340 words with the marker clots broken up. Every source gained a public name and why line; scores, status and internal notes untouched. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker were untouched by that pass. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and neither dimension moved. `scores.proof` stays 0 on the plainest reading of rung 0 — `comps` is empty and no foreign player of ANY maturity is on file, early or established. Rung 1 was considered and does not apply: it needs early foreign players, and there are none; the EU-wide MiCA tooling in [S4] sells to firms staying in business, not exiting, so it is not a comparable for this wedge at all. `scores.gap` stays 1. Five Czech advisory firms were lifted out of the [S3], [S4] and [S6] scan prose into a structured `locals[]` ledger, and only one is established: Finreg Partners (IČO 07123949, ARES 2018) on the public-customer-count limb, standing behind three of the eleven licences ČNB granted. ARROWS, AMS Europe, kryptoregulace.cz and Stuchlíková & Partners publish no customer count, pair with no public buyer in `data/lookup/cz-contract-parties.jsonl`, and carry no round or state listing, so all four read early on receipts. Finreg being established does not drop gap to 0, because rung 0 requires an established local player that ALREADY SELLS THIS, and every firm on the ledger sells the opposite service — getting licensed, not winding down. Gap does not rise to 2 either: [S4] is a proper check with recorded `queries[]` and `checked[]`, but it found local players rather than none, and its own note says so. `score` unchanged at 4. The non-solutions paragraph now states the licensed-versus-exit distinction that the gap score turns on, and the Proven-abroad paragraph says the comps ledger is empty of early players too, not just established ones. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. Finreg Partners moves `early` → `established` and takes `competes: adjacent`. The `early` contradicted this file's own re-score entry from earlier the same day, which had already named Finreg as established on the public-customer-count limb, standing behind three of the eleven CASP permissions ČNB granted; the ledger then said early because under the one-field schema an established local would have forced gap to 0. Adjacency now carries that question, and the reason is the one the argument already gives in plain words — every firm here sells getting licensed, and nobody sells getting out. ARROWS, AMS Europe, kryptoregulace.cz and Stuchlíková & Partners are adjacent at `early` on receipts; kryptoregulace.cz's line now says what it supplies, which is reading material and not a service at all. `scores.gap` stays 1 and is FLAGGED rather than moved: with no `competes: direct` entry on the ledger, rung 2 is the arguable score, and moving it is a MATCH judgment rather than a content pass. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

FOURTH PASS THIS DATE, MERGED HERE: the local field was searched properly, and the answer went the other way from the one the ledger's shape suggested. `scores.gap` STAYS 1 and `score` stays 4. The score it replaces rested on a check whose own note ends "Gap 1 (quick search, services-only incumbents named)" — a self-declared quick search with no queries recorded — and the previous pass flagged rung 2 as the arguable reading because nothing on the ledger was `competes: direct`. [S7] is that check run for real: five Czech query shapes and a positive control run and passed before any conclusion was drawn, a query phrased as a firm hunting for licensing help returning Finreg Partners at the top of its own page. It also read four Czech service menus line by line instead of searching at them, and that is what changed the answer. SCHEJBAL&PARTNERS SELLS THIS. On 18 June 2026 it published "Připravte si wind-down plán", set out the four duties of a controlled exit — move client crypto-assets and money to an authorised provider or the customer's own wallet, tell every client in time how settlement will run, keep meeting AML duties to the last day, be ready to report the settlement to ČNB — and closed by naming preparation of an orderly departure from the market among the things it will guide a client through. That is this job sold to this buyer. It goes in at `competes: direct` and `maturity: early`, and early is not a technicality here: the duty is weeks old, so no seller on earth meets the three-year limb. One early direct seller is exactly rung 1, CONTESTED and still enterable, and rung 2 — checked, and NOBODY sells this — would have been false the moment that page was read. Gap authority is asymmetric in both directions: a not-found never raises the score, and a found seller settles it. FOUR PLAYERS ADDED under the no-exclude rule. Kopečný & Partners, Key2Law and PROFI Poradenství & Finance were all named in notes already on this file and had never reached the ledger, which is the false-absence failure the ledger exists to end; SCHEJBAL&PARTNERS is new. Finreg's entry now records what its service page does and does not carry, including the CASP-acquisition due diligence it has added, which serves whoever buys an orphaned customer book rather than the firm leaving. Every evidence line also dropped the repository filename it used to print to the reader. The non-solutions paragraph was rewritten: "Every one of them sells getting licensed; nobody sells getting out" was true when it was written and is not true now, and the paragraph says so plainly along with what is still missing — nothing here is packaged, priced or repeatable. Proof, money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S7] is appended, not inserted.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 9 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Six trade terms glossed at first use: CASP and ČNB where the 1 July 2026 duty is stated [S1,S2], then MiCA, DORA, AML and KYC. Caps-styled law-firm names ARROWS, AMS Europe and PROFI Poradenství now sit in a clause saying what they sell [S3,S7]. Argument cut from 436 to 364 words, every marker and figure kept; the restated three-outcomes sentence went. A gist added beside all seven sources. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` telling the situation, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Only eleven Czech crypto firms got licensed; the rest must wind down". Previous solution, verbatim: "A packaged wind-down for the crypto firms that did not get licensed: notify customers, move their coins and cash to a licensed provider, and close the records and the tax to a standard the regulator will accept." No brief or good_for existed before. Checked against the sources while writing. The deadline is behind us, and both lines say so: the transitional period ended on 1 July 2026 [S1], so the title reads "since July" and the brief "until July". "The rest must wind down" became "must stop serving clients", which is what ČNB's warning requires — cease the crypto-asset service and move customer crypto and funds to a licensed provider or the customer's own wallet [S1]; it does not require the firm itself to close. The brief puts 188 providers that kept the right to trade through the transition [S5] beside the 11 licences granted [S2] rather than subtracting them: the dek's "roughly 175 one-off exits" assumes every licensee was among the 188, which no source on file confirms. The dek's "a wind-down most have never run" carries no marker and was not used. The fine is stated for whom it applies to, a provider that keeps trading without a licence, at ČNB's own "above 100M CZK" [S1]. The solution names no comparable abroad because `comps[]` is empty. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Title before: "Only 11 Czech crypto firms got a licence. Since July, the rest must stop serving clients." After: "Since July, all but 11 Czech crypto firms must stop serving clients". Brief before: "Until July, 188 Czech crypto providers could trade on an old licence; only 11 got the new one [S1,S2,S5]. The rest must stop and hand customers' coins and cash to a licensed firm or back, or risk fines above 100M CZK [S1]." After: "Unlicensed firms must hand their customers' coins and cash to a licensed firm or back to the customer [S1]. Those that keep trading risk fines above 100M CZK [S1]." Solution before: "Build a fixed-price service that winds down an unlicensed crypto firm: it tells customers, moves their coins and cash out, and closes the records." After: "Build a fixed-price service that winds down an unlicensed crypto firm: tells customers, moves their coins and cash, closes the records." Good for before: "Someone who knows how crypto wallets and exchanges work and likes careful paperwork." After: "Someone who knows crypto wallets and exchanges and likes careful paperwork." The passed date stays passed ("since July") [S1]; the 188 providers on the old licence [S5] were cut to keep one number in the brief, the fine [S1], and the 11 licences stay in the headline [S2] without subtracting from the 188. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the 11 licences and holds the old trade licence's 30,000 holders, the 188 that kept trading rights and the duty to move clients' coins and cash, with MiCA, the licence and the central bank explained in plain words below [S1,S2,S5]. Why now opens on the passed deadline, with the fine and the wind-down's four duties as its items and the 2025 application funnel and the dates below as plain bullets [S1,S2,S4,S5,S7]. Willing to pay answers that no Czech price for a wind-down is published and names the three kinds of buyer [S1,S3,S5,S6,S7]. Competition and Validated abroad describe each ledger firm by what it sells; every `locals[]` name left the body, and MarketGuard, AMLBot, KYC-Chain, Sigma360, CertiK and Binance, which are not on a ledger, stay named [S3,S4,S7]. `entry.why` became "Easier: … Harder: …", with semicolons in the Easier half because one of its items carries its own comma list, and no longer names a ledger firm. Detail added from sources already on file, none of it new evidence: the 5,000 companies among the old licence holders and the 2025 funnel of 245 applications, 210 by 31 July 2025 and none granted that year [S5]; the four wind-down duties [S7]; the established adviser's due-diligence advice for firms buying a crypto provider [S7]; and Binance among the applicants that failed [S4]. Corrected against the sources rather than against the old sentences: "171 were terminated on procedural defects" became "it stopped 171, 117 of them because the application was incomplete", because the central bank's 2025 supervision report, Box 5, read 2026-09-18, lists 17 withdrawals among the 171, and a withdrawal is not a defect [S5]; "roughly 175 one-off exits" is gone, because it subtracts the 11 licences from the 188 and no source says every licensed firm was among the 188, as the 2026-09-16 headline pass had already found [S2,S5]; "a wind-down most have never run" is gone, because it carried no marker and no source supports it; and "No Czech firm publishes a price" now says what [S6] checked, four Czech advisers' pages. "The rest must stop" now says the warning asks a firm to stop the service, not to close the company, as the 2026-09-16 pass read [S1]. Flagged as inference: that licensed firms taking over departing firms' customers may pay for help rests on one adviser selling due diligence to such buyers [S7]; and that the 11 licensed firms need recurring compliance work rests on the compliance jobs the licensing-advisory check names [S3]. No `process` block was added: the wind-down is a one-off duty that began on 1 July 2026, and the sources say what a departing firm owes, not who does each step today or how [S1,S7]. No score, status, entry gate value, source, `note:`, `sources[]` order, title, brief, solution or good_for changed.

2026-09-19 · rescored to the 2026-09-19 ladders — `scores.urgency` 3 → 2 and `score` 4 → 3, band FAINT unchanged; `scores.money` stays 0. Urgency: the old 3 was the deadline sub-score 2 plus the retired freshness point. The trigger is the end of the MiCA transition on 1 July 2026 [S1]. It is REAL, because the EU regulation binds the unlicensed provider directly, and CLOSE, because it passed 2.5 months before this date. TEETH is not met: for a passed date the ladder needs fines levied or proceedings opened within 12 months, and the only sanction on file is the central bank's warning naming a ceiling above 100M CZK [S1]. An enforcement receipt would restore 3. Tagging pass for money: no source on file shows anyone paying for a wind-down. The one direct seller bills by the hour and publishes no rate [S7]. Four advisers' pages publish no fee [S6]. Firms pay for licence applications [S3], which is the opposite job and does not count. No receipt was added, so money stays 0 on the same evidence as the worksheet. S1's note, which named the deadline sub-score and freshness, gained a dated correction line. Prose re-read against the new numbers: Why now states the passed date and the fine a firm risks, not a fine levied, and Willing to pay says no price is published, so neither changed. The body had no Competition link to rename. No other score, status, source order or body sentence changed.
