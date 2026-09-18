---
id: p-0003
region: cz
title: 'Czech building permits take way too long (6–12 months)'
brief: 'Engineers preparing one chase opinions from many offices and utility companies, each on its own deadline [S7]. The state has cut red tape 4 times since 2022, with little effect [S12].'
solution: 'Build software for design offices that sends permit requests and tracks every answer deadline.'
good_for: 'Someone who knows Czech building permits and can sell to design offices.'
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
entry:
  level: moderate
  buyer: small-firms
  permission: none
  incumbents: adjacent
  integration: national-system
  money: bootstrap
  why: 'Easier: engineering offices buy directly without tenders, and no licence is needed to do the work. Harder: every request and its answer deadline runs through the state''s e-mailbox and building portal, which a newcomer must build against; and a Czech online service already sells the same job.'
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
  evidence: 'Sells AI permit preparation to designers and building owners: it checks the
    drawings, routes requests to the consulted authorities and utility operators through the
    state e-mailbox (datová schránka), tracks each 30/60/90-day statutory deadline and produces
    the certificate that consent has lapsed into approval. On 20 August 2026 it charged 12,900
    CZK per project or 29,900 CZK a month for up to five new projects; by 4 September 2026 its
    page listed 14,900 CZK a project and no longer showed the monthly plan. No company of that
    trade name is on the state business register, no launch year is published and it names
    nobody who has used it.'
- name: Efektivia (AI Efektivia s.r.o.)
  url: https://efektivia.eu/
  ico: '19760680'
  since: 2023
  competes: adjacent
  maturity: established
  evidence: 'Deployed at the Brno-střed town hall and the Neratovice municipal office, AI
    Efektivia s.r.o. has sold AI document triage to the building authority — the office that
    receives an application and checks it — since September 2023. It is the other side of the
    same counter: every hour it saves the office is an hour it does not save the person
    assembling the application.'
process:
  summary:
    today: 'A permit engineer checks the drawings, sends a request to every office and utility that must give an opinion, follows each one up, and files the application with the building office [S10,S7].'
    after: 'The design office sends every request from one tool that shows each answer deadline, and follows up the late ones.'
  steps:
  - who: Permit engineer
    today: 'Sends a request to each office and utility'
    known: documented
    cites: [10, 7]
    change: changes
    after: 'Sends every request from one tool'
  - who: Consulted offices and utilities
    today: 'Each answers on its own deadline'
    known: documented
    cites: [7]
    change: stays
    after: 'Unchanged: each keeps its own deadline'
  - who: Permit engineer
    today: 'Follows up each answer and its conditions'
    known: documented
    cites: [10]
    change: changes
    after: 'Sees every deadline and chases the late answers'
  - who: Building office
    today: 'Decides on the filed application'
    known: documented
    cites: [10]
    change: stays
    after: 'Unchanged: the office still decides'
  - who: '?'
    today: 'How much of the six months to a year goes on waiting for opinions is not known'
    known: unknown
    cites: []
    change: stays
    after: 'Unknown: the tool tracks each deadline, it cannot shorten one'
sources:
- type: arbitrage
  name: "PermitPortal"
  gist: "the closest US template"
  why: "AI pre-construction operating system for US developers (YC F24) — entitlements, zoning intelligence and permit navigation, the closest template abroad."
  url: https://www.ycombinator.com/companies/permitportal
  note: 'yc-permitportal: PermitPortal (YC F24) — AI OS for pre-construction: entitlements,
    zoning intelligence, permit navigation; adjacent YC analogs Permitify (W25) and Verdant
    (S26) confirm the cluster. All US-market, so scored as one weak (non-adjacent) analog.'
  date: '2026-08-13'
  signal: yc-permitportal
- type: complaint
  name: "Portál stavebníka — the digitalization fiasco"
  gist: "the July 2024 portal launch"
  why: "The July 2024 launch of the digitalized permitting system, and trade-press reporting a year on that it had stabilized but still faced complications."
  url: https://www.ycombinator.com/companies/permitportal
  note: Signal documents the July 2024 DSŘ digitalization fiasco (portál stavebníka) and archiweb
    reporting that digitalization 'stabilized after a year, but still faces complications';
    CZ among slowest building-permit processes in OECD.
  date: '2026-08-13'
- type: gap-check
  name: "First Czech market scan"
  gist: "the superseded first sweep"
  why: "An early sweep that returned only news about the broken state portal and US tools — superseded by the two Czech players found later."
  url: https://www.ycombinator.com/companies/permitportal
  note: 'Absence check 2026-08-13: searches return only news about the broken state system
    and US tools (CivCheck); no CZ startup automating permit preparation or navigation.'
  date: '2026-08-13'
- type: arbitrage
  name: "Autositu"
  gist: "the fourth US entrant"
  why: "A two-person YC W26 team selling an AI plan-review workspace — the fourth US company on the permitting problem inside two years."
  url: https://www.ycombinator.com/companies/autositu
  note: 'yc-autositu: Autositu (YC W26) — AI-native workspace for development plan reviews;
    a fourth YC company on the permitting/plan-review problem within two years. Still US-only,
    so arbitrage stays 1.'
  date: '2026-08-13'
  signal: yc-autositu
- type: complaint
  name: "ČKAIT survey — how long a permit takes"
  gist: "six months to a year"
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
  gist: "the retired index"
  why: "The World Bank's 2021 statement retiring its Doing Business index after an investigation into data irregularities; the old claim that Czech permits are among the OECD's slowest came from that index."
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
  gist: "the two Czech players"
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
  gist: "61,613 permits in 2025"
  why: The national permit count and its value — the population any permit-preparation product is sold against. 61,613 permits in 2025, down 14.5% on 2024.
  note: 'CSU preliminary full-year 2025: 61,613 stavebnich povoleni nationally (-10,453 / -14.5% vs 2024); orientacni hodnota 503.3bn CZK (-13.3%). CSU has announced orientacni hodnota will be discontinued and replaced by pocet povolenych zameru, so any series built on the value terminates.'
  date: '2026-02-18'
- type: news
  url: https://www.ckait.cz/o-nas
  name: 'CKAIT: authorised engineers and technicians'
  gist: "36,300 professional buyers"
  why: Sizes the professional buyer side — the projektanti who prepare permit documentation and would buy the tooling.
  note: 'CKAIT states "vice jak 32 tisic autorizovanych inzenyru a techniku"; the architects chamber CKA separately records 4,288 authorised architects as of 1 Jan 2026. Combined addressable professional population approximately 36,300.'
  date: '2026-01-01'
- type: news
  url: https://www.cespron.cz/ceny-inzenyrskych-cinnosti/
  name: 'Published price lists for permit engineering'
  gist: "16,000–42,000 CZK by hand"
  why: What the manual alternative costs today — the price ceiling a software product prices against.
  note: 'Published Czech inzenyrska cinnost price lists for a single family house cluster at 16,000-42,000 CZK per project (CESPRON 16,000 total; Pruvodce drevostavbou 42,000 incl. VAT from 1.1.2026). Pruvodka sells at 12,900 CZK per project, below the low end of human-delivered permit engineering.'
  date: '2026-08-25'
- type: contract
  name: "Registr smluv — building-permit portal upgrade (~€0.8M)"
  gist: "the ministry's portal upgrade"
  why: "The ministry signed a contract to upgrade the digital building-procedure portal — the state is paying again for the system whose 2024 launch caused much of the pain described here."
  url: https://smlouvy.gov.cz/smlouva/39180478
  note: 'hlidac-36829114: ministry contract for upgrading the digital building-procedure
    portal (portál stavebníka / DSŘ), ~€0.81M, Aug 2026 (registr smluv 39180478; 2026-08-25
    retrospective harvest). Money 0→1 on the p-0004 precedent: state spend on the system at
    the centre of the problem is a relevant public contract — adjacent spend, held below 2
    (not an open tender a navigation vendor can win, and no recurring spend receipted).'
  date: '2026-08-19'
  signal: hlidac-36829114
  dims: [money]
- type: complaint
  name: "European Commission — 2026 Country Report for Czechia"
  gist: "four packages, no faster permits"
  why: "The Commission's own measure of the Czech compliance load: more than 1,800 obligations from 171 legal acts, 71 percent of firms calling regulation a barrier to investment in 2025 against 57 percent in 2024, four debureaucratisation packages since 2022 with little measured effect on permitting speed, and urban-plan updates in large cities that can take over a decade."
  url: https://economy-finance.ec.europa.eu/document/download/3f5af374-4872-4b57-ac99-8507c5420083_en?filename=CZ_SWD_2026_203_1_EN_autre_document_travail_service_part1_v3.pdf
  note: 'ecsem-cz2026-admin-burden: Commission Staff Working Document SWD(2026) 203 final,
    2026 Country Report — Czechia, 3 June 2026. Cited for the two limbs that are about this
    record and nothing else: four debureaucratisation packages since 2022 with little measured
    effect on permitting speed, and an urban-plan update in a large city taking over a decade.
    The headline burden figures (>1,800 obligations from 171 acts; 71% of firms in 2025 against
    57% in 2024, EIB investment survey) are the surrounding measure and are cited as that.
    Backs demand, which already sits at its ceiling here — filed as the EU-level receipt behind
    a claim the record previously carried only from national trade press. Runner-up considered
    and rejected: p-0006, whose buyer is the investment intermediary, not a permit applicant.'
  date: '2026-06-03'
  signal: ecsem-cz2026-admin-burden
  dims: [demand]
- type: complaint
  name: "Ombudsman — Q2 2026 report to the Chamber of Deputies"
  gist: "192 building complaints"
  why: "The public defender of rights took 2,509 complaints in the second quarter of 2026, 132 more than the same quarter a year earlier, and building matters were the third-largest agenda at 192."
  url: https://www.ochrance.cz/dokument/zpravy_pro_poslaneckou_snemovnu_2026/2026-ii-q.pdf
  note: 'ombud-q2-2026: quarterly report to the Chamber of Deputies, file number
    KVOP-40911/2026/S — 2,509 complaints, up 132 year on year, 79.8% inside the mandate;
    social security 523, health administration 205, building matters 192. Only the
    building-matters count is cited on this record. The report does not break that figure
    down by proceeding type, so no claim is made about which stage of a permit the complaints
    concern. A standing quarterly series (ombud-q1-2026 recorded 2,341), so it is a repeatable
    index rather than a one-off. Backs demand, already at its ceiling.'
  date: '2026-06-30'
  signal: ombud-q2-2026
  dims: [demand]
- type: price
  url: https://www.cespron.cz/ceny-inzenyrskych-cinnosti/
  name: "Permit engineering, done by a person"
  gist: "from 16,000 CZK a project"
  why: "The lower bound of the published Czech range for permit engineering on one family house: 16,000 to 42,000 CZK a project, paid to a person."
  note: 'Price receipt drawn from the published price lists already on this ledger (CESPRON
    16,000 CZK total; Průvodce dřevostavbou 42,000 CZK incl. VAT from 1.1.2026). A range, so
    the lower bound is recorded and why says so. basis manual-equivalent: it is what the same
    job costs done by hand, which is the reason that basis exists. dims omitted.
    Verified 2026-09-04: the CESPRON price list at that url still itemises the standard
    family-house permit and totals Celková cena standardního řízení 16 000,- Kč, so the
    recorded lower bound holds; the 42,000 CZK upper end sits on the separate Průvodce
    dřevostavbou list, which is not this url.'
  date: '2026-08-25'
  payer: 'A Czech family-house builder commissioning permit engineering'
  amount_czk: 16000
  unit: per-project
  basis: manual-equivalent
- type: price
  url: https://pruvodka.cz/
  name: "Průvodka — the Czech product"
  gist: "12,900 CZK a project"
  why: "Průvodka charges a designer or building owner 12,900 CZK a project to prepare and chase a permit, with a 29,900 CZK monthly studio tier above it."
  note: 'Price receipt lifted from the 2026-08-20 gap re-check already on this ledger, which
    read pruvodka.cz: 12,900 CZK per project one-off or 29,900 CZK/month (Studio, up to 5 new
    projects), Stripe checkout, 14-day money-back. The monthly tier has no matching unit in
    the price vocabulary, so the per-project price is the receipt and the tier is stated in
    why. dims omitted: backs no score.
    Verified 2026-09-04: pruvodka.cz now prices at 14 900 Kč za projekt and no longer
    shows the 29,900 CZK Studio tier, so the recorded 12,900 CZK is what the page said on
    2026-08-20 and the list price has since risen — pruvodka.cz has no Wayback snapshot,
    so no archived page carries the older figure.'
  date: '2026-08-20'
  payer: 'A Czech designer or building owner preparing a permit'
  amount_czk: 12900
  unit: per-project
  basis: list-price
created: '2026-08-13'
updated: '2026-09-04'
---

Czech building permits take six months to a year, and whoever prepares one must chase opinions from many offices and utilities [S5,S7].

- About 1,100 authorised engineers gave that range in a 2024 survey [S5].
- Each consulted office has 30, 60 or 90 days by law to answer [S7].
- A permit engineer's published price list splits the job into four stages [S10].

The survey was published in early 2024, and its range counts the engineering work around a permit as part of the time [S5]. The engineer's four stages, for one family house, are these [S10]:

- Checking the design documents and working out which opinions the permit needs [S10].
- Preparing and sending a request to each office that must give one [S10].
- Following up each office, and working its conditions into the drawings [S10].
- Filing the application with the building office and seeing it through to a final permit [S10].

Requests also go to ČEZ, GasNet and CETIN — the electricity, gas and telecom networks — and to the water companies [S7]. They travel through the state's official e-mailbox, and when an office misses its deadline, its consent counts as given and the applicant can get a certificate saying so [S7].

Existing non-solutions: Permit engineers still chase the opinions by hand, and a Czech online service that automates the job names no customer yet [S10,S7].

The state's own answer is its digital permit portal, which a year after its launch the trade press called stabilized "but still facing complications" [S2].

- Engineering offices do the job case by case, for a published price [S10].
- A Czech online service checks the drawings, sends the requests through the state's e-mailbox and tracks each deadline [S7].
- Another Czech firm sells AI document checking to the building offices themselves, the other side of the same counter [S7].

Why now: Builders still wait months for each permit in 2026, and four rounds of red-tape cuts since 2022 have barely sped them up [S5,S12].

- 192 building complaints reached the public defender of rights in April–June 2026 [S13].
- The state's July 2024 portal launch hurt applicants and building offices alike [S2].
- In a large city, updating the urban plan can take over a decade [S12].

The launch came as the new building act changed the procedures [S2]. The dates behind the rest are these:

- Since 2022 the state has passed four packages to cut red tape, and in June 2026 the European Commission found little measured effect on how fast permits are issued [S12].
- In April–June 2026 the public defender of rights took 2,509 complaints, 132 more than a year earlier, and building matters were the third-largest group after social security and health [S13].
- In August 2026, two years after the launch, the state was still paying to upgrade the portal, as [Willing to pay](#willing-to-pay) shows [S11].

The Commission also counts more than 1,800 obligations on Czech firms from 171 legal acts, and 71 percent of firms called regulation a barrier to investment in 2025, against 57 percent in 2024 [S12].

Who pays: Builders already pay engineers by hand to chase each permit, and a Czech online service charges per project [S10,S7].

- Engineers publish a fixed price for the permit on one family house [S10].
- The Czech online service charges less per project than the engineers do [S7,S10].
- The ministry's August 2026 contract to upgrade its portal is worth about €0.8M [S11].

Two kinds of buyer pay today: the builder who commissions the work, and the design office that prepares it [S7].

- Czechia has about 36,300 authorised engineers, technicians and architects: more than 32,000 in the engineers' chamber and 4,288 architects [S9]. They are the pool that draws up permit documents [S9].
- 61,613 building permits were issued in 2025, 10,453 or 14.5% fewer than in 2024 [S8].
- The buildings permitted in 2025 had an indicative value of 503.3bn CZK, 13.3% less than in 2024 [S8].
- A rough estimate: if a tenth of a year's permits went through such a service at its per-project price, it would bring in about €3M a year, and only if it sells per permit [S7,S8].
- The ministry's portal contract pays for the state's own system; it is not a tender that a seller of permit software could win [S11].

Solved elsewhere: In the United States, funded start-ups sell AI software for building permits, zoning and plan review, all of it for the US market [S1,S4].

Y Combinator, a US programme that funds start-ups, has backed four companies on permits and plan review inside two years [S1,S4]. The oldest, from autumn 2024, sells US developers an AI system for zoning and permits before construction starts [S1]. Permitify, from winter 2025, checks plans against the building code, and Verdant, from summer 2026, handles land-use permits for local government [S1]. The fourth, a two-person team from winter 2026, sells AI plan review [S4].

Permitting rules differ from country to country, so none of these products arrives here on its own [S1,S4].

## First moves

1. Build a deadline tracker that shows an engineering office, across all its projects, which office owes an answer on which permit and by when. Every permit turns on the days each consulted office has by law to answer, and a missed deadline counts as consent; see [The opportunity](#opportunity). Show every open request on one screen, flag the ones whose time has run out, and produce the certificate that consent was given. The Czech online service already selling this prices per project, see [Competition](#competition), while an office preparing many permits a year needs one view of all of them.
2. Contact the chamber of authorised engineers and ask to show the deadline tracker to its members. The chamber asked its own members how long a permit takes, and their answer is under [The opportunity](#opportunity). Bring a second fact: two years after the portal launch, the state is still paying to upgrade it, as [Willing to pay](#willing-to-pay) shows. Few in that room expect the state to fix this soon, so a tool that works around the wait is an easy thing to hear about.
3. Sell to engineering offices rather than one-off builders, because an office runs the same permit procedure many times a year. The pool of authorised engineers and architects who draw up permit documents is under [Willing to pay](#willing-to-pay). A family building one house buys once, while an office that repeats the procedure turns every hour saved into margin the same month.
4. Set your price against what builders pay an engineer to chase a permit by hand, not against the Czech software. Builders already pay a permit engineer per project, and the Czech online service already charges less than that; both prices are under [Willing to pay](#willing-to-pay). Fewer permits were issued last year than the year before, so win share from the engineers rather than wait for the market to grow.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-13 · fact check — The "OECD's slowest / 246 days / 157th in the world" framing traces to World Bank Doing Business 2020 — an index discontinued in 2021 after a data-manipulation scandal [S6] — and it measured the full administrative cycle, not permitting alone. Replaced with the ČKAIT survey (Jan 2024, n≈1,100): typical proceedings 6–12 months [S5], https://zpravy.ckait.cz/vydani/2024-01/delka-povolovani-staveb-v-cr-nikoliv-roky-ale-mesice-ukazal-pruzkum-inzenyrske-komory/

2026-08-20 · evidence audit and gap re-check — Two blocks recorded on this date, merged here. Verifying the 2026-08-13 fact check: the ČKAIT survey (Z+i 2024/01, published 20 Feb 2024) does report that for nearly 1,100 authorized persons "délka trvání většiny povolovacích řízení staveb v ČR, a to včetně související inženýrské činnosti, je obvykle šest měsíců až jeden rok" [S5], and the World Bank Group did discontinue Doing Business on 16 Sep 2021 after investigating data irregularities in the 2018 and 2020 editions [S6]. Still open: the specific "246 days / 157th" figures attributed to Doing Business 2020, which the archived country profile publishes only inside downloadable figures — "Doing Business" returns zero hits across all 6,181 signals, so the figure is not yet traced to a primary source on file. De-ranked in the same pass. The absence this record was built on — "no CZ startup automating permit preparation or navigation" [S3] — was never checked against Czech-language surfaces; it was recorded against a YC company page, and it does not hold: Průvodka (pruvodka.cz) is a live, priced Czech AI product that assembles the vyjadřovačky and stanoviska a stavebník needs before applying, and Efektivia (efektivia.eu) sells the mirror-image triage tool to stavební úřady [S7]. Gap 2 → 0 and score 6 → 4 under the SPEC §4 de-rank rule, status → watching; the existing-non-solutions and comparables paragraphs were rewritten so the prose no longer contradicts the score. Neither incumbent appears in data/signals/funded/, and neither would: both are unfunded, so a capital-shaped ledger is structurally blind to them and only a live Czech-language search could surface them. The title carried the same disproved absence, "with no tooling of their own", and has been cut. Still unresolved and left for MATCH: the title also keeps the "one of the OECD's slowest" framing that the 2026-08-13 entry above retracts. S2 appears to carry the OECD claim independently, so resolving it is a judgment about that source, not an audit fix, and it has not been made here.

2026-08-24 · title sweep — The judgment left open above is now made: the "one of the OECD's slowest" framing in the title and lead is cut. Its only carrier, the yc-permitportal harvest note [S2], states no source of its own, and the record's own 2026-08-13 fact check traced the family of superlatives to the discontinued Doing Business index [S6]. Title and lead now state what the ČKAIT survey receipts: proceedings typically run six months to a year [S5]. Scores untouched; the DSŘ-dysfunction demand receipts [S2] stand.

2026-08-25 · plain-language pass — The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "larger stavebníci" now reads "the larger firms that commission building work", and "offices preparing dokumentace" now reads "offices that draw up the design documents". No `fix:` was authored here: the argument closes with the local position held by Průvodka and names no product an entrant would build that Průvodka does not already sell, so the field is left absent rather than filled with something vague — the template renders nothing when it is. Scores, status, source notes and every [Sn] marker are untouched by that pass. Second pass this date, merged here: the 2026-08-25 retrospective harvest added the ministry's ~€0.8M contract upgrading the building-procedure portal [S11]. Money 0 → 1 on the adjacent-spend precedent p-0004 already carries — the state demonstrably pays into the system at the centre of this record — and score 4 → 5; everything else stands. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries Průvodka, marked early: live and priced, but unfunded, with no launch year published and no ARES match for the trade name, so no limb of the established test is on file [S7]. An early local player does not close a space: `scores.gap` 0 → 1. Efektivia is deliberately NOT in `locals[]` — it sells AI triage to the building authority, the other side of the counter, and `locals[]` is the ledger of players selling this record's own product to its own buyer, which is what the gap ladder reads; it stays named in the body. `scores.proof` 1 → 2: PermitFlow and GreenLite both pass the established test, but both are American, so rung 3's 'two markets, one CEE-adjacent' is not met. `score` 5 → 7. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and **Efektivia is restored to the ledger** as `competes: adjacent`, reversing the exclusion recorded in the pass above. The reason given there for leaving it out — that it sells to the building authority rather than to this record's buyer — is now precisely what the ledger is able to say, and it is what a builder needs to know rather than grounds for dropping the name. Průvodka converts to `competes: direct` and stays early, so `scores.gap` stays 1: the only direct player on file is still an unfunded one. Two corrections while restoring. The pass above said no ARES match exists for Efektivia's trade name; that was wrong. ARES resolves **AI Efektivia s.r.o., IČO 19760680, Brno, incorporated 25 September 2023**, which also supplies the `since` year the entry had been missing. With that year and the two offices it names — MČ Brno-střed and MěÚ Neratovice [S7] — Efektivia passes both limbs of the established test, so it is recorded `adjacent` + `established`; the entry states the September 2023 incorporation date plainly, because three years is met on this register's year clock and not yet on the calendar. The same ARES claim was re-checked for **Průvodka** in this pass and it holds — no company resolves under that trade name. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the Efektivia entry: the note that an earlier pass wrongly claimed no ARES match for the trade name. The correction is real and it is recorded in the pass above, which is where it belongs; the ledger line is for the market, not for our own errata. Same pass: `## First moves` written for the first time. The template reserves the section for records scoring 7 or more and this one has scored 7 since the re-score recorded above, but it had none. Four moves, each grounded in a receipt already on this ledger — the professional population and the published price of doing the work by hand [S9,S10], the statutory answer windows and Průvodka's five-project monthly plan [S7], the ČKAIT survey and the ministry's portal-upgrade contract [S5,S11], and the 2025 permit count [S8]. No new claim was introduced and no score moved. The absent `fix:` stands: the moves say who to sell to and what to build first, which is a route into a contested field, not a product Průvodka does not already sell.

2026-09-02 · plain-language pass — Eighteen Czech and trade terms glossed or replaced at first use, among them stavebníci, inženýrská činnost, DSŘ, úřady, stavební zákon, dokumentace, MČ and MěÚ; ČEZ and CETIN now carry appositives. Argument 438 → 346 words, every [Sn] marker, figure, price and named company kept, and the August 2026 portal contract [S11] added to Why now. First moves rewritten verbs-first. A gist added to all eleven sources. No score, status, note or marker touched.

2026-09-04 · price receipt — Two figures already on file are now recorded as prices: permit engineering by hand from 16,000 CZK a project, the lower bound of a 16,000 to 42,000 CZK range [S14], and Průvodka at 12,900 CZK a project [S15]. No score, status, note or marker touched.

2026-09-10 · likely solution — Added the one-sentence `solution:`, now required on every record and always shown as the likely solution, compressed from First moves 1–2, the Průvodka entry in locals[] and build.note. This reverses the deliberately absent `fix:` recorded on 2026-08-25. No claim, score or source changed.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` on who is stuck and what is happening, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Czech developers and builders face building-permit proceedings that typically run six months to a year, through a still-dysfunctional state portal". Previous solution, verbatim: "Software for the engineering and architecture offices that prepare building permits: it checks the drawings, sends requests to the authorities and utility companies that must give an opinion, and tracks the deadline each one must answer by across all the office's projects." The record carried no brief and no good_for before this pass. Every claim was checked against this record's sources first. The headline's "barely sped them up" stands for the European Commission's "little measured effect on permitting speed" after four debureaucratisation packages since 2022 [S12]. The "6 months to a year" survey was published in early 2024, before the July 2024 launch of the state's digital permitting portal, so the brief dates it as a 2024 survey rather than stating it as today's figure [S5]. The 30-, 60- and 90-day answer windows are as read on 2026-08-20 from a Czech product's own page [S7]. The old title's "still-dysfunctional state portal" was not repeated: its only carrier is a mid-2025 trade-press quote [S2], and the August 2026 portal contract [S11] shows the state paying for changes, not that the portal is broken. The suggested software is close to what Průvodka already sells per project [S7,S15]; the line describes the product neutrally, and whether the field is open stays the gap score's question. No score, status, source, note, marker or body sentence changed. Simplified for the front page: title "Czech building permits are slow, and 4 rounds of red-tape cuts since 2022 have barely sped them up" → "Czech building permits are still slow after 4 rounds of red-tape cuts"; brief "Whoever prepares a permit must collect opinions from several authorities and utility companies, each with its own 30-, 60- or 90-day deadline to answer [S7]. In a 2024 survey, engineers said most permits take 6 months to a year [S5]." → "Whoever prepares a permit must collect opinions from several authorities and utility companies, each on its own deadline [S7]. In a 2024 survey, engineers said most permits take 6 months to a year [S5]."; solution "Build software for design offices that sends permit requests to authorities and utilities and tracks every answer deadline, as companies already do in the US." → "Build software for design offices that sends permit requests to authorities and utilities and tracks every answer deadline."; good_for "Someone who'd like to work with building engineers and connect software to state systems." → "Someone who'd like to work with building engineers and state permit systems.". The 30-, 60- and 90-day windows were cut from the brief; the survey keeps its 2024 date so the figure is not read as today's; "as companies already do in the US" was cut for length. Same date, owner-approved simplification: title "Czech building permits are still slow after 4 rounds of red-tape cuts" became "Czech building permits take way too long (6–12 months)"; brief "Whoever prepares a permit must collect opinions from several authorities and utility companies, each on its own deadline [S7]. In a 2024 survey, engineers said most permits take 6 months to a year [S5]." became "Engineers preparing one chase opinions from many offices and utility companies, each on its own deadline [S7]. The state has cut red tape 4 times since 2022, with little effect [S12]."; solution "Build software for design offices that sends permit requests to authorities and utilities and tracks every answer deadline." became "Build software for design offices that sends permit requests and tracks every answer deadline."; good_for "Someone who'd like to work with building engineers and state permit systems." became "Someone who knows Czech building permits and can sell to design offices.".

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the six-months-to-a-year wait and the chasing of opinions, with the survey, the 30/60/90-day answer windows and the permit engineer's four stages as its items and detail [S5,S7,S10]; the network operators, the state e-mailbox and the lapsed-consent certificate moved there from the Průvodka sentence and the moves [S7]. Competition opens on the chasing done by hand, keeps the state portal's "stabilized but still facing complications" quote as the state's own answer [S2], and describes Průvodka and Efektivia by what each sells, leaving their names, prices, offices and dates to their `locals[]` rows. Why now opens on the builder's wait, with the 192 building complaints, the July 2024 portal launch and the decade-long urban-plan update as its three items, and the red-tape packages, the ombudsman's quarter and the portal contract below as dated bullets [S2,S12,S13,S11]. Willing to pay answers that builders pay engineers by hand and a Czech service charges per project, then holds the buyer pool, the 2025 permit count and the rough €3M estimate [S7,S8,S9,S10]. Validated abroad lost the ledger names PermitPortal and Autositu for descriptions [S1,S4]; Permitify and Verdant, not on the ledger, stay named. Say it once: the 16,000–42,000 CZK range and Průvodka's 12,900 CZK left the body for their price receipts [S14,S15], whose `why` lines already state the range and the monthly tier; the ~€0.8M portal contract now lives once, under Willing to pay, with Why now linking to it. The moves lost every [Sn] marker and figure for links; move 1 now builds the deadline tracker (it was move 2), and the old "Sell to the engineering offices" move is move 3; the chamber move now contacts the chamber. `entry.why` was rewritten as "Easier: … Harder: …" naming the same gates the entry fields already carry, plus the direct Czech seller in `locals[]`. S6.why and S11.why no longer say "this record". Detail added from sources already on file, none of it new evidence: the 10,453 fall in permits and their 503.3bn CZK indicative value [S8]; the 32,000 engineers and 4,288 architects inside the 36,300 [S9]; the ombudsman's 2,509 complaints, up 132 [S13]; the Commission's 1,800 obligations and 71-against-57 percent [S12]; and, read at S10's url on 2026-09-18, the four stages the CESPRON price list itemises for the standard family-house permit (preparing and working out the opinions needed, requesting them, following them up and working in their conditions, filing and seeing the permit through) [S10]. Process block added (none before): five steps, the permit engineer sending the requests and following them up (changes), the consulted offices and utilities answering on their own deadlines and the building office deciding (both stay), and an unknown fifth step, how much of the six to twelve months is waiting on opinions; each drawn step is backed by S10's itemised stages or S7's deadline windows, and no step names a ledger company or a price. Corrected against the sources rather than against the old sentences: "Applicants and building offices both lost throughput" is not what S2 or its signal says; the yc-permitportal harvest behind S2 says the July 2024 launch "created acute pain for both stavebníci and úřady" and that the new building act changed procedures, and the body now says that [S2]; "Czech software for permit preparation does exist [S3]" cited the first sweep, which found none, so that claim now cites S7, the re-check that found it; "law firms" working case by case was cut, since no source on file mentions them, and permit-engineering offices stay [S10]; "Neither publishes a launch year, a customer or a funding round" was wrong for Efektivia, whose row names two town halls it serves and dates it to September 2023, so the body no longer says it; "a proceeding still runs six months to a year" read the early-2024 survey as today's figure, so the survey is now dated [S5]; the 36,300 are engineers, technicians and architects, not engineers and architects [S9]; and the Průvodka row in `locals[]` said it sells at 12,900 CZK or 29,900 CZK a month in the present tense, while S15's note records that on 4 September 2026 its page listed 14,900 CZK and no monthly plan, so the row now dates both [S15]. Flagged as inference: that builders still wait months in 2026 rests on the 2024 survey [S5] and on the Commission's June 2026 finding that the red-tape packages had little measured effect [S12]; that none of the US products arrives here on its own, because permitting rules differ by country, is our reading of S1 and S4 recording them as US-only; the €3M figure is our rough estimate from S7's per-project price and S8's permit count, as it was before; and in the moves, that an office runs the procedure many times a year and that few engineers expect the state to fix this soon are our reading, not a source's. No score, status, source, `note:`, `sources[]` order, entry level, title, brief, solution or good_for changed.
