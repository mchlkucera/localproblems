---
id: p-0003
region: cz
title: Czech developers and builders face building-permit proceedings that typically run
  six months to a year, through a still-dysfunctional state portal
category: housing
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 1
  urgency: 1
  demand: 2
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Software over public permitting rules has no license gate, but CZ-specific stavební
    zákon workflow content plus developer pilots need a dev-and-permitting-expert team and
    a months-long sales cycle.'
comps:
- name: PermitPortal
  url: https://permitportalapp.com/
  geo: US
  since: 2024
  traction: 'YC F24; AI pre-construction OS for US developers; funding beyond YC undisclosed (YC, 2024)'
  signal: yc-permitportal
- name: PermitFlow
  url: https://www.permitflow.com/
  geo: US
  since: 2021
  traction: '$54M Series B led by Accel (company, 2025) after $31M Series A (TechCrunch, 2024); 80-person team (YC, 2026)'
- name: GreenLite
  url: https://greenlite.com/
  geo: US
  since: 2022
  traction: '$49.5M Series B led by Insight Partners (PRNewswire, 2025); ~100 Fortune 500 customers; permits in 21-45 vs 90-120 days'
- name: Autositu
  url: https://autositu.com/
  geo: US
  since: 2025
  traction: 'YC W26, 2-person team (YC, 2026); AI plan-review workspace claiming 50-70% fewer city comments; funding undisclosed'
  signal: yc-autositu
locals:
- name: Průvodka
  url: https://pruvodka.cz/o-nas
  competes: direct
  maturity: early
  evidence: 'sells AI permit preparation to projektanti and stavebníci at 12,900 CZK per
    project or 29,900 CZK a month — it checks the dokumentace, routes requests to dotčené
    orgány and správci sítí through datová schránka, tracks each 30/60/90-day lhůta and
    generates the doklad o fikci souhlasu. Unfunded, no ARES match for the trade name, no
    launch year published and no limb of the established test on file.'
- name: Efektivia (AI Efektivia s.r.o.)
  url: https://efektivia.eu/
  ico: '19760680'
  since: 2023
  competes: adjacent
  maturity: established
  evidence: 'named customers: live at MČ Brno-střed and MěÚ Neratovice. What it sells is AI
    document triage for the stavební úřad — the office that receives the file and checks it —
    and not the assembly of that file by the applicant, which is what this record''s buyer
    needs. It is the mirror image across the same counter, and every hour it saves the
    authority is an hour it does not save the stavebník. AI Efektivia s.r.o. was incorporated
    in September 2023, so it clears three years only on this register''s year clock; an earlier
    note on this record said no ARES match existed for the trade name, and that was wrong.'
sources:
- type: arbitrage
  name: "PermitPortal"
  why: "AI pre-construction operating system for US developers (YC F24) — entitlements, zoning intelligence and permit navigation, the closest template abroad."
  url: https://www.ycombinator.com/companies/permitportal
  note: 'yc-permitportal: PermitPortal (YC F24) — AI OS for pre-construction: entitlements,
    zoning intelligence, permit navigation; adjacent YC analogs Permitify (W25) and Verdant
    (S26) confirm the cluster. All US-market, so scored as one weak (non-adjacent) analog.'
  date: '2026-08-13'
  signal: yc-permitportal
- type: complaint
  name: "Portál stavebníka — the digitalization fiasco"
  why: "The July 2024 launch of the digitalized permitting system, and trade-press reporting a year on that it had stabilized but still faced complications."
  url: https://www.ycombinator.com/companies/permitportal
  note: Signal documents the July 2024 DSŘ digitalization fiasco (portál stavebníka) and archiweb
    reporting that digitalization 'stabilized after a year, but still faces complications';
    CZ among slowest building-permit processes in OECD.
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  why: "An early sweep that returned only news about the broken state portal and US tools — superseded by the two Czech players found later."
  url: https://www.ycombinator.com/companies/permitportal
  note: 'Absence check 2026-08-13: searches return only news about the broken state system
    and US tools (CivCheck); no CZ startup automating permit preparation or navigation.'
  date: '2026-08-13'
- type: arbitrage
  name: "Autositu"
  why: "A two-person YC W26 team selling an AI plan-review workspace — the fourth US company on the permitting problem inside two years."
  url: https://www.ycombinator.com/companies/autositu
  note: 'yc-autositu: Autositu (YC W26) — AI-native workspace for development plan reviews;
    a fourth YC company on the permitting/plan-review problem within two years. Still US-only,
    so arbitrage stays 1.'
  date: '2026-08-13'
  signal: yc-autositu
- type: complaint
  name: "ČKAIT survey — how long a permit takes"
  why: "A survey of roughly 1,100 authorised engineers: most Czech permit proceedings, related engineering work included, run six months to a year."
  url: https://zpravy.ckait.cz/vydani/2024-01/delka-povolovani-staveb-v-cr-nikoliv-roky-ale-mesice-ukazal-pruzkum-inzenyrske-komory/
  note: 'ČKAIT survey published in Z+i 2024-01 (n≈1,100): typical Czech building-permit
    proceedings run 6–12 months, not years. This is the replacement figure the record''s
    CORRECTION block puts in place of the discontinued World Bank Doing Business framing;
    the url was cited in the body from 2026-08-13 but was not on this ledger. No evidence-layer
    signal covers this article (the one ČKAIT signal on file, chamber-ckait-dsr, is
    a different 2026-03 piece about the DSŘ portal).'
  date: '2024-01-31'
- type: news
  name: "World Bank — Doing Business discontinued"
  why: "The 2021 statement retiring the index behind this record's original 'slowest in the OECD' framing, after an investigation into data irregularities."
  url: https://www.worldbank.org/en/news/statement/2021/09/16/world-bank-group-to-discontinue-doing-business-report
  note: 'World Bank Group statement, 16 Sep 2021 — the Doing Business report is DISCONTINUED
    following the investigation into data irregularities in the Doing Business 2018 and 2020
    editions. Traced by the 2026-08-20 evidence audit as the primary source for the discontinuation
    half of this record''s CORRECTION block. The specific "246 days / 157th" figures the correction
    attributes to Doing Business 2020 were NOT traced to a primary source and stay flagged as
    untraced in the block. No evidence-layer signal covers this statement (Doing Business returns
    zero hits corpus-wide); correction receipt only, backs no score dimension.'
  date: '2021-09-16'
  dims: []
- type: gap-check
  name: "Průvodka and Efektivia"
  why: "Průvodka sells AI permit preparation to projektanti and stavebníci at 12,900 CZK a project or 29,900 CZK a month; Efektivia sells the mirror-image triage tool to the building authorities."
  url: https://pruvodka.cz/o-nas
  note: 'Gap re-check 2026-08-20: looked for a Czech product automating permit preparation
    or navigation for stavebníci, developers or projektanti — the absence this record has
    claimed since 2026-08-13. FOUND, and the claim does not survive it. Průvodka (pruvodka.cz,
    live and priced) sells exactly that: the buyer uploads the dokumentace, AI checks it and
    recommends which dotčené orgány and správci sítí (ČEZ, GasNet, vodárny, CETIN) to approach,
    the requests go out through datová schránka, and the service tracks each authority''s
    30/60/90-day lhůta and generates the doklad o fikci souhlasu when one lapses; 12,900 CZK
    per project one-off or 29,900 CZK/month (Studio, up to 5 new projects), Stripe checkout,
    14-day money-back. Its own about page states it serves "projektantům i stavebníkům" and is
    "postaveno pro české stavební řízení". A second CZ player, Efektivia (efektivia.eu), sells
    AI document triage into municipal offices — the authority side of the same counter, live at
    MČ Brno-střed and MěÚ Neratovice. De-ranked under SPEC §4: gap 2 -> 0, score 6 -> 4, status
    -> watching. Method note: our own funded ledger holds no CZ permitting entrant, and would
    not have — both incumbents are unfunded, so a capital-shaped ledger cannot see them.'
  date: '2026-08-20'
  queries:
    - "software automatizace stavebního povolení příprava dokumentace stavební řízení"
    - "startup AI povolování staveb portál stavebníka pomoc developerům software"
    - "\"stavební povolení\" AI asistent aplikace vyřízení online startup česká firma"
    - "Efektivia AI stavební úřad žádosti o stavební povolení kontrola úplnosti podkladů"
    - "Průvodka.cz vyjádření dotčených orgánů online služba stavebníci firma"
    - "Czech startup permitting software construction permits automation Czechia proptech"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: news
  url: https://csu.gov.cz/plk/vydana-stavebni-povoleni-a-orientacni-hodnota-staveb-v-plzenskem-kraji-v-roce-2025
  name: 'CSU: building permits issued, 2025'
  why: The national permit count and its value — the population any permit-preparation product is sold against. 61,613 permits in 2025, down 14.5% on 2024.
  note: 'CSU preliminary full-year 2025: 61,613 stavebnich povoleni nationally (-10,453 / -14.5% vs 2024); orientacni hodnota 503.3bn CZK (-13.3%). CSU has announced orientacni hodnota will be discontinued and replaced by pocet povolenych zameru, so any series built on the value terminates.'
  date: '2026-02-18'
- type: news
  url: https://www.ckait.cz/o-nas
  name: 'CKAIT: authorised engineers and technicians'
  why: Sizes the professional buyer side — the projektanti who prepare permit documentation and would buy the tooling.
  note: 'CKAIT states "vice jak 32 tisic autorizovanych inzenyru a techniku"; the architects chamber CKA separately records 4,288 authorised architects as of 1 Jan 2026. Combined addressable professional population approximately 36,300.'
  date: '2026-01-01'
- type: news
  url: https://www.cespron.cz/ceny-inzenyrskych-cinnosti/
  name: 'Published price lists for permit engineering'
  why: What the manual alternative costs today — the price ceiling a software product prices against.
  note: 'Published Czech inzenyrska cinnost price lists for a single family house cluster at 16,000-42,000 CZK per project (CESPRON 16,000 total; Pruvodce drevostavbou 42,000 incl. VAT from 1.1.2026). Pruvodka sells at 12,900 CZK per project, below the low end of human-delivered permit engineering.'
  date: '2026-08-25'
- type: contract
  name: "Registr smluv — building-permit portal upgrade (~€0.8M)"
  why: "The ministry signed a contract to upgrade the digital building-procedure portal — the state is paying again for the system whose 2024 launch created much of this record's pain."
  url: https://smlouvy.gov.cz/smlouva/39180478
  note: 'hlidac-36829114: ministry contract for upgrading the digital building-procedure
    portal (portál stavebníka / DSŘ), ~€0.81M, Aug 2026 (registr smluv 39180478; 2026-08-25
    retrospective harvest). Money 0→1 on the p-0004 precedent: state spend on the system at
    the centre of the problem is a relevant public contract — adjacent spend, held below 2
    (not an open tender a navigation vendor can win, and no recurring spend receipted).'
  date: '2026-08-19'
  signal: hlidac-36829114
  dims: [money]
created: '2026-08-13'
updated: '2026-08-25'
---

Czech stavebníci — from housing developers to firms building industrial capacity — face permit proceedings that typically run six months to a year, related inženýrská činnost included [S5]. The July 2024 launch of the digitalized permitting system (DSŘ / portál stavebníka) made things acutely worse [S2]: a year on, trade press (archiweb) describes the system as stabilized "but still facing complications." Both applicants and úřady lost throughput during the transition to the new stavební zákon procedures [S2].

Why now: the new building act changed procedures, the state portal remains unreliable [S2], and every month of permitting delay carries direct financing cost for developers. The pain is documented in national press rather than inferred.

Who pays: developers and the larger firms that commission building work, for whom shaving months off permit preparation is worth meaningful fees; the architecture and engineering offices that draw up the design documents; potentially municipalities buying triage tooling, though the private side is the realistic first buyer. The volume is documented: 61,613 building permits were issued in 2025 [S8], and roughly 36,300 authorised engineers and architects prepare the documentation behind them [S9]. Manual permit engineering for a single family house is published at 16,000–42,000 CZK a project [S10]. Průvodka undercuts that at 12,900 CZK [S7], so even a tenth of the annual permit flow at that price is on the order of €3M a year — a floor, and one that assumes the tool sells only per permit rather than by subscription.

Existing non-solutions: the state's own portál stavebníka (the source of much of the pain), law firms and inženýring service providers who navigate permits manually per project. Czech software for permit preparation does exist [S3]: **Průvodka** sells it to projektanti and stavebníci — upload the dokumentace, AI checks it and recommends which dotčené orgány and správci sítí (ČEZ, GasNet, vodárny, CETIN) to approach, the žádosti go out by datová schránka, and the service tracks each 30/60/90-day lhůta and issues the doklad o fikci souhlasu when one lapses, at 12,900 CZK per project or 29,900 CZK a month on the Studio plan [S7]. On the authority side of the same counter, **Efektivia** sells AI document triage into Czech municipal offices, live at MČ Brno-střed and MěÚ Neratovice [S7]. Both are young and unfunded: neither publishes a launch year or a customer list, and neither appears in any funding feed [S7].

Solved elsewhere: PermitPortal (YC F24), Permitify (YC W25) and Verdant (YC S26) show a funded US cluster around AI permit/zoning navigation [S1]. All analogs are US-based [S1,S4] and permitting is jurisdiction-specific; with the local field contested rather than closed [S7], the documented demand is what remains.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-13 · fact check — The "OECD's slowest / 246 days / 157th in the world" framing traces to World Bank Doing Business 2020 — an index discontinued in 2021 after a data-manipulation scandal [S6] — and it measured the full administrative cycle, not permitting alone. Replaced with the ČKAIT survey (Jan 2024, n≈1,100): typical proceedings 6–12 months [S5], https://zpravy.ckait.cz/vydani/2024-01/delka-povolovani-staveb-v-cr-nikoliv-roky-ale-mesice-ukazal-pruzkum-inzenyrske-komory/

2026-08-20 · evidence audit and gap re-check — Two blocks recorded on this date, merged here. Verifying the 2026-08-13 fact check: the ČKAIT survey (Z+i 2024/01, published 20 Feb 2024) does report that for nearly 1,100 authorized persons "délka trvání většiny povolovacích řízení staveb v ČR, a to včetně související inženýrské činnosti, je obvykle šest měsíců až jeden rok" [S5], and the World Bank Group did discontinue Doing Business on 16 Sep 2021 after investigating data irregularities in the 2018 and 2020 editions [S6]. Still open: the specific "246 days / 157th" figures attributed to Doing Business 2020, which the archived country profile publishes only inside downloadable figures — "Doing Business" returns zero hits across all 6,181 signals, so the figure is not yet traced to a primary source on file. De-ranked in the same pass. The absence this record was built on — "no CZ startup automating permit preparation or navigation" [S3] — was never checked against Czech-language surfaces; it was recorded against a YC company page, and it does not hold: Průvodka (pruvodka.cz) is a live, priced Czech AI product that assembles the vyjadřovačky and stanoviska a stavebník needs before applying, and Efektivia (efektivia.eu) sells the mirror-image triage tool to stavební úřady [S7]. Gap 2 → 0 and score 6 → 4 under the SPEC §4 de-rank rule, status → watching; the existing-non-solutions and comparables paragraphs were rewritten so the prose no longer contradicts the score. Neither incumbent appears in data/signals/funded/, and neither would: both are unfunded, so a capital-shaped ledger is structurally blind to them and only a live Czech-language search could surface them. The title carried the same disproved absence, "with no tooling of their own", and has been cut. Still unresolved and left for MATCH: the title also keeps the "one of the OECD's slowest" framing that the 2026-08-13 entry above retracts. S2 appears to carry the OECD claim independently, so resolving it is a judgment about that source, not an audit fix, and it has not been made here.

2026-08-24 · title sweep — The judgment left open above is now made: the "one of the OECD's slowest" framing in the title and lead is cut. Its only carrier, the yc-permitportal harvest note [S2], states no source of its own, and the record's own 2026-08-13 fact check traced the family of superlatives to the discontinued Doing Business index [S6]. Title and lead now state what the ČKAIT survey receipts: proceedings typically run six months to a year [S5]. Scores untouched; the DSŘ-dysfunction demand receipts [S2] stand.

2026-08-25 · plain-language pass — The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "larger stavebníci" now reads "the larger firms that commission building work", and "offices preparing dokumentace" now reads "offices that draw up the design documents". No `fix:` was authored here: the argument closes with the local position held by Průvodka and names no product an entrant would build that Průvodka does not already sell, so the field is left absent rather than filled with something vague — the template renders nothing when it is. Scores, status, source notes and every [Sn] marker are untouched by that pass. Second pass this date, merged here: the 2026-08-25 retrospective harvest added the ministry's ~€0.8M contract upgrading the building-procedure portal [S11]. Money 0 → 1 on the adjacent-spend precedent p-0004 already carries — the state demonstrably pays into the system at the centre of this record — and score 4 → 5; everything else stands. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries Průvodka, marked early: live and priced, but unfunded, with no launch year published and no ARES match for the trade name, so no limb of the established test is on file [S7]. An early local player does not close a space: `scores.gap` 0 → 1. Efektivia is deliberately NOT in `locals[]` — it sells AI triage to the building authority, the other side of the counter, and `locals[]` is the ledger of players selling this record's own product to its own buyer, which is what the gap ladder reads; it stays named in the body. `scores.proof` 1 → 2: PermitFlow and GreenLite both pass the established test, but both are American, so rung 3's 'two markets, one CEE-adjacent' is not met. `score` 5 → 7. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and **Efektivia is restored to the ledger** as `competes: adjacent`, reversing the exclusion recorded in the pass above. The reason given there for leaving it out — that it sells to the building authority rather than to this record's buyer — is now precisely what the ledger is able to say, and it is what a builder needs to know rather than grounds for dropping the name. Průvodka converts to `competes: direct` and stays early, so `scores.gap` stays 1: the only direct player on file is still an unfunded one. Two corrections while restoring. The pass above said no ARES match exists for Efektivia's trade name; that was wrong. ARES resolves **AI Efektivia s.r.o., IČO 19760680, Brno, incorporated 25 September 2023**, which also supplies the `since` year the entry had been missing. With that year and the two offices it names — MČ Brno-střed and MěÚ Neratovice [S7] — Efektivia passes both limbs of the established test, so it is recorded `adjacent` + `established`; the entry states the September 2023 incorporation date plainly, because three years is met on this register's year clock and not yet on the calendar. The same ARES claim was re-checked for **Průvodka** in this pass and it holds — no company resolves under that trade name.
