---
id: p-0030
region: cz
title: The MiCA transition ended 1 Jul 2026 with only 11 licensed crypto providers in Czechia
  — hundreds of formerly trade-licensed firms must wind down, migrate customer assets, or
  operate illegally
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
sources:
- type: regulation
  url: https://www.cnb.cz/cs/cnb-news/aktuality/Upozorneni-Ceske-narodni-banky-Konec-prechodneho-obdobi-podle-narizeni-MiCA-k1.7.2026/
  note: 'reg-mica-casp-cz: ČNB warning — the MiCA grandfathering period in Czechia ended 1
    Jul 2026; only CASP-licensed firms may serve clients, others must cease activity and transfer
    customer crypto and funds to licensed providers or self-custody. ČNB fines can exceed
    CZK 100M; licensing projects cost CZK 1-5M per firm. In force with active supervisory
    enforcement: deadline sub-score 2, urgency 3 with freshness.'
  date: '2026-07-01'
  signal: reg-mica-casp-cz
- type: news
  url: https://www.cnb.cz/cs/cnb-news/tiskove-zpravy/MiCA-CNB-udelila-kryptolicenci-11-subjektum/
  note: 'ČNB press release: 11 CASP licences granted — against a former population of hundreds
    of trade-licence (živnost) crypto providers under the pre-MiCA regime (per the reg signal).
    The licensed set is two orders of magnitude smaller than the affected set: the market
    structure receipt for the wind-down/migration problem.'
  date: '2026-08-13'
- type: gap-check
  url: https://zpravy.kurzy.cz/864080-finreg-partners-jako-prvni-v-cesku-stoji-za-tremi-licencemi-mica/
  note: 'Gap check 2026-08-13: the supply side is licensing advisory — Finreg Partners (behind
    3 of the 11 licences), ARROWS, Kopečný & Partners, AMS Europe sell licence applications
    and compliance consulting as services; no CZ product for customer-asset migration, wind-down
    execution, or ongoing CASP compliance operations (safeguarding, DORA, AML reporting) was
    found. Gap 1 (quick search, services-only incumbents named).'
  date: '2026-08-13'
- type: gap-check
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
created: '2026-08-13'
updated: '2026-08-24'
---

Czechia entered the MiCA era with crypto services provided under a plain trade licence (živnost), and hundreds of firms did exactly that [S1,S2]. That regime ended on 1 July 2026: ČNB's warning is explicit that only CASP-licensed firms may serve clients [S1], and it has licensed eleven [S2]. Everyone else must cease activity and transfer customer crypto-assets and funds to licensed providers or the customers' own custody [S1] — an orderly-wind-down obligation most small providers have no playbook for.

Why now: the cliff is not approaching, it has happened, and the exposed population is large. Operating unlicensed now risks fines that can exceed CZK 100M [S1], and the licence gate is demonstrably narrow: ČNB assessed 251 applications and granted 11 [S2,S4]. Every week of 2026 H2 is therefore a live sorting of hundreds of firms into three bins: migrate the business into a licensed structure, wind down correctly, or drift into illegality.

Who pays: three distinct buyers. Exiting providers need wind-down execution — customer notification, asset-transfer mechanics, records, tax closure — done defensibly. The eleven licensees (and applicants behind them) need ongoing compliance operations they never ran before: safeguarding of client assets, DORA resilience, MiCA-grade AML and reporting [S1,S3] — recurring obligations, not a one-off project. And licensed incumbents (including EU-passported entrants) have a concrete acquisition channel: the orphaned customer books that must legally land somewhere licensed.

Existing non-solutions: licensing advisory as a service — Finreg Partners, ARROWS, Kopečný & Partners and peers write applications and policies at law-firm economics [S3]. The 2026-08-13 gap check found no productized wind-down or CASP-compliance-operations offering in Czechia [S3].

No funded foreign analog is receipted for the wind-down/migration wedge specifically (proof 0 — MiCA compliance tooling is emerging EU-wide but nothing is on file), and no documented complaint from affected firms is yet in evidence (demand 0). The score is carried by the enforcement-live deadline; the affected population is a few hundred firms [S1,S2], so this is a sharp, time-boxed problem rather than an economy-wide one — the register should expect it to decay unless the licensee-side compliance-ops wedge proves recurring.

## Revisions

2026-08-20 · evidence audit — Three unbacked claims removed from the framing. "one of Europe's loosest crypto regimes": a cross-EU comparison the register never ran, and neither ČNB source makes any comparative claim about other member states. "from exchanges and brokers to ATM operators": the enumeration follows the marker and has no receipt — the signal says only that hundreds of former živnost-based providers are affected. "with bank-licence-grade scrutiny": nothing in the corpus compares CASP licensing to bank licensing. The money figures in the same paragraph are not affected — the fine ceiling and the licensing project cost are both carried verbatim in the ČNB regulation signal and stay cited [S1].

2026-08-24 · fact check — The licensing-cost claim, "a licence application is a CZK 1-5M project", is gone. The 2026-08-20 audit kept it as carried by the regulation signal, but the signal's only URL is the ČNB warning, which was fetched on this date and does not state it; nor does the licensing-advisory article on this ledger [S3], and it verifies nowhere else on file. The fine ceiling stays — it is on the ČNB page verbatim ("pokut, jejichž horní hranice přesahuje 100 milionů Kč") [S1]. The narrow gate is now stated from receipted numbers instead: 251 applications assessed, 11 granted, both confirmed live on the ČNB press release [S2,S4].
