---
id: p-0027
region: cz
title: Complaints about Czech consumer loans have quadrupled, all handled by hand
fix: 'Case software for lenders answering complaints at the Financial Arbitrator: pull the
  loan file, draft the response, hold every deadline, and flag which cases to settle.'
category: fintech
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 0
  urgency: 1
  demand: 2
  gap: 2
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Respondent-side dispute-workflow software needs no licence — a dev plus a consumer-credit lawyer can pilot with one non-bank lender facing the ~20,000-filing wave and 167-day proceedings.'
comps:
- name: ClaimSorted
  url: https://www.claimsorted.com/
  geo: GB
  since: 2024
  traction: '$13.3M seed led by Atomico (Forbes, 2025); 20+ insurer clients across US/UK/EU; tech-enabled claims TPA'
  signal: yc-claimsorted
  markets: [US]
- name: Casap
  url: https://www.casaphq.com/
  geo: US
  since: 2023
  traction: '$25M Series A led by Emergence at $105M valuation (BusinessWire, 2025); automates bank and credit-union payment-dispute lifecycle'
- name: Audun
  url: https://www.getaudun.com/
  geo: NO
  since: 2026
  traction: 'YC S26, 4-person Oslo team (YC directory, 2026); AI-native debt collection; no public funding or customer figures yet'
  signal: yc-audun
locals:
- name: aCompliance
  url: https://www.acompliance.cz/klienti/nebankovni-poskytovatele-uveru/
  ico: '02571901'
  since: 2014
  competes: adjacent
  maturity: early
  evidence: 'It sells a service, not a product: outsourced handling of client complaints and out-of-court
    disputes at the financial arbiter, marketed to non-bank lenders and staffed by people [S5].
    Its own page offers "pomoci s vyřizováním stížností a reklamací klientů, včetně případných
    mimosoudních sporů (zejména u Finančního arbitra)" [S7] — the same job for the same buyer,
    and still the opposite shape: a firm doing the work, not software a lender runs itself. Acompliance
    poradenství s.r.o. has traded since 28 January 2014, but names nobody who has bought it and
    publishes no count, so how many lenders it handles is unknown [S7].'
- name: ePohledávky.cz (SoftGate Systems)
  url: https://www.epohledavky.cz/
  ico: '28859685'
  since: 2013
  competes: adjacent
  maturity: early
  evidence: It sells a receivables and collections platform — software for the creditor pursuing
    the debtor, the other side of the same relationship from the creditor defending a consumer
    claim at the arbiter [S5]. Trading since 2013; it names nobody who has bought it, publishes
    no count and pairs with no public body on the state contracts register.
- name: Barrister (ASW)
  url: https://www.asw.cz/
  competes: adjacent
  maturity: early
  evidence: It sells collections and receivables software, again on the pursuit side of the relationship
    rather than the defence side [S5]. No start year, no named buyer and no published count, so
    how widely it is used is unknown.
- name: Evolio (AVE Soft)
  url: https://evolio.cz/
  ico: '25378392'
  since: 1997
  competes: adjacent
  maturity: early
  evidence: It sells law-office software whose headline feature is filing electronic payment orders
    in bulk on one click — automation aimed squarely at the creditor suing the debtor, which is
    the pursuit side again and not the defence of a consumer claim [S7]. AVE Soft s.r.o. has traded
    since 14 July 1997, but publishes no count of the firms running it, so its reach is unknown.
- name: SingleCase
  url: https://www.singlecase.cz/
  competes: adjacent
  maturity: early
  evidence: It sells law-practice case management to law firms — generic matter tooling, with
    no financial-arbiter docket in it [S5]. No start year and no published user count are on file.
- name: Praetor (Wolters Kluwer ČR)
  url: https://www.wolterskluwer.com/cs-cz/solutions/praetor/funkce
  ico: '63077639'
  since: 1995
  competes: adjacent
  maturity: early
  evidence: 'It sells the widest-selling Czech case-management system for law firms and in-house
    legal departments — intake, documents, court-register watching, deadlines, escrow and billing
    — and there is no arbiter docket anywhere in it [S7]. This is the vendor best placed to turn
    and build one: Wolters Kluwer ČR has traded since 3 April 1995, though it publishes no count
    of Praetor users, its distribution deal with ČSOB is a bank offer rather than a reference,
    and only one public body pairs with it on the state contracts register [S7].'
- name: Advokátní spis (ATLAS consulting)
  url: https://advokatnispis.cz/
  ico: '46578706'
  since: 1992
  competes: adjacent
  maturity: early
  evidence: It sells electronic case files for individual advocates — full-text search across
    files, time recorded per case, deadlines pushed into Outlook [S7] — general practice tooling
    with no arbiter docket in it. ATLAS consulting spol. s r.o. has traded since 14 May 1992;
    it publishes no user count, and only one public body pairs with it on the state contracts
    register.
- name: E-OFFICE Advokát (AISoft)
  url: http://www.aisoft.cz/akoffice.html
  ico: '18826024'
  since: 1991
  competes: adjacent
  maturity: early
  evidence: It sells an office system for medium and large law firms — accounting, a diary of
    tasks and deadlines, an electronic registry, management oversight [S7]. Again the firm's own
    administration rather than the arbiter's docket. AISoft spol. s r.o. has traded since 16 May
    1991, but names nobody who has bought it and publishes no count.
- name: ISAK
  url: https://www.isak.cz/
  competes: adjacent
  maturity: early
  evidence: It sells practice software for running a law office securely and in order [S7] — the
    same general matter tooling as the rest of this group, with nothing in it aimed at a consumer-credit
    dispute. No start year and no published user count are on file.
- name: Aptien
  url: https://www.aptien.com/
  ico: '26397668'
  since: 2005
  competes: adjacent
  maturity: early
  evidence: It sells generic case and record management to companies, with no financial-arbiter
    docket in it [S5]. Trading since 30 August 2005; it names nobody who has bought it and publishes
    no count.
sources:
- type: complaint
  name: "Financial arbiter — 2025 annual report"
  gist: "the 12,050-filing year"
  why: "The caseload receipt: 2,660 new proceedings in 2023, 5,683 in 2024, 12,050 in 2025 and 8,200 more filed by May 2026, with consumer credit at ~92% of the running docket and proceedings averaging 167 days."
  url: https://finarbitr.gov.cz/cs/informace-pro-verejnost/aktuality/vyrocni-zprava-financniho-arbitra-za-rok-2025-425.html
  note: 'fa-spotrebitelske-uvery: the financial arbiter''s 2025 annual report documents 12,050
    new proceedings in 2025 (vs 5,683 in 2024 and 2,660 in 2023, +113% YoY), consumer-credit
    disputes at ~92% of the 15,446 running proceedings, 8,200 new filings by the May 2026
    report date (~20,000 projected for 2026), average proceeding 167 days, 83% of concluded
    cases settled. Creditworthiness-assessment (úvěruschopnost) claims dominate — a mass-scale
    claims industry is industrializing filings.'
  date: '2026-05-29'
  signal: fa-spotrebitelske-uvery
- type: complaint
  name: "MPO — consumer policy progress report"
  gist: "the ministry's five-year tally"
  why: "A second official count: ~18,700 financial-arbiter filings between 2020 and mid-2025, inside 45,000+ out-of-court dispute filings across sectors. The caseload is structural, not a one-year spike."
  url: https://mpo.gov.cz/assets/cz/ochrana-spotrebitele/aktualni-informace/2026/3/Zprava-o-prubeznem-plneni-Strategie-spotrebitelske-politiky-2025.pdf
  note: 'mpo-adr-vyuziti: MPO''s consumer-policy progress report tabulates ~18,700 financial-arbiter
    filings 2020-H1/2025 (consumer credit, strongly rising) within 45k+ out-of-court dispute
    filings across sectors — a second official receipt that the caseload is recurring and
    structural, not a one-year spike. Demand scored 2: recurring documented dispute volume
    in two independent official sources.'
  date: '2026-03-31'
  signal: mpo-adr-vyuziti
- type: arbitrage
  name: "ClaimSorted"
  gist: "the nearest funded model"
  why: "A YC-backed London company productising claims processing for insurers — with Audun's AI debt collection in Norway, the nearest funded model to lender-side dispute operations, and still one vertical away."
  url: https://www.ycombinator.com/companies/claimsorted
  note: 'yc-claimsorted: ClaimSorted (YC S24, London) productizes claims processing for insurers;
    the funded claims-operations cluster (Avallon AI, Basepilot, Amera in US insurance; Audun,
    YC-backed AI-native debt collection in Norway) proves AI dispute/claims ops in adjacent
    verticals. No funded analog found for consumer-credit dispute operations specifically
    — proof scored 1 (weak adjacent analogs only).'
  date: '2026-08-13'
- type: gap-check
  name: "Czech dispute-tooling scan (first pass)"
  gist: "the first Czech search"
  why: "Searches returned the arbiter's own information pages, consumer advisories and law firms handling cases by hand — no Czech product for lender-side dispute response was found."
  url: https://finarbitr.gov.cz/cs/informace-pro-verejnost/caste-otazky.html
  note: 'Gap check 2026-08-13: searches return only the arbiter''s own information pages,
    consumer advisories (obcanskeporadny.cz, dostupnyadvokat.cz) and law firms handling cases
    manually; no CZ product for lender-side dispute response, FA-docket management or settlement
    workflow was found. Gap 1 (quick search, no CZ player found).'
  date: '2026-08-13'
- type: gap-check
  name: "aCompliance and the Czech respondent-side field"
  gist: "the aCompliance finding"
  why: "A deeper Czech sweep: receivables platforms point the other way, law-practice case management carries no arbiter docket, and aCompliance handles arbiter disputes as a service rather than a product."
  url: https://www.acompliance.cz/klienti/nebankovni-poskytovatele-uveru/
  note: 'Gap re-check 2026-08-20: NOT FOUND, score unchanged. Looked for a Czech product on
    the respondent side — dispute-response workflow for lenders, docket management against
    the financial arbiter, settlement decisioning. Nearest CZ supply is adjacent and points
    the other way: receivables and collections platforms (eDebit, ePohledávky.cz by SoftGate
    Systems, Evolio, Barrister by ASW) automate the creditor pursuing the debtor, not the
    creditor defending a consumer claim; law-practice case management (SingleCase, LegiSpace,
    Aptien) is generic firm tooling with no arbiter docket in it. The one offering aimed
    squarely at this need is a service, not a product — aCompliance markets handling of client
    complaints and out-of-court disputes at the financial arbiter to non-bank lenders. Our
    own funded ledger holds no CZ entrant either: the dispute cluster in it is the demand
    evidence plus foreign analogs. IMPORTANT: this is a not-found, not a proven absence, and
    per the register rule a negative never raises a gap score. Gap stays 1 with its coverage
    now recorded. Method control passed first at Wultra (p-0017) and Softlink (p-0026).'
  date: '2026-08-20'
  queries:
    - "software pro správu sporů finanční arbitr nebankovní poskytovatel úvěru reklamace klientů systém"
    - "český software správa právních sporů case management pro právní oddělení bank a věřitelů"
    - "software pro vymáhání a správu pohledávek spotřebitelské úvěry Česko platforma věřitelé"
    - "software evidence stížností a reklamací klientů banka pojišťovna poskytovatel úvěru Česko systém"
    - "Czech software lender-side complaint and dispute management financial arbiter consumer credit case workflow"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
- type: regulation
  name: "VeKLEP — consumer credit act revision in draft"
  gist: "the credit act being rewritten"
  why: "The Finance Ministry is revising the Consumer Credit Act 257/2016 — the statute whose creditworthiness-assessment duties generate most of the arbiter's docket is itself being rewritten."
  url: https://odok.cz/portal/veklep/material/KORNDDVFVG8B/
  note: 'veklep-KORNDDVFVG8B: Finance Ministry draft amending zákon č. 257/2016 Sb. o
    spotřebitelském úvěru, in VeKLEP since 14 Feb 2025 (first VeKLEP harvest, 2026-08-25).
    Draft with no dated obligation on file: context receipt — the legal frame behind the
    dispute flood is in motion — backing no score dimension.'
  date: '2025-02-14'
  signal: veklep-KORNDDVFVG8B
  dims: []
- type: gap-check
  name: "Czech dispute tooling, searched again in a lender's words"
  gist: "the ten-vendor sweep"
  why: "A wider Czech sweep of the supply side. It surfaced a dense field of Czech law-office
    software — Praetor, Evolio, Advokátní spis, E-OFFICE Advokát, ISAK — and none of it, and
    nothing else Czech, handles a case at the Financial Arbitrator."
  url: https://evolio.cz/
  note: 'Czech-language sweep 2026-08-25, run because the check on this file dated 2026-08-13
    recorded no queries at all and closed with the words "quick search", which is not coverage
    anyone can judge. POSITIVE CONTROL PASSED, run before any conclusion was drawn. Two
    controls, both aimed at Czech supply already known to exist. (a) Query 4, in a lender''s
    descriptive language, returned aCompliance''s non-bank-lender page at the top of the first
    page — the one Czech offering aimed squarely at this need, already on this ledger. (b)
    Query 2, aimed at Czech legal case software, returned SIX bootstrapped Czech vendors on
    one page — E-OFFICE Advokát (AISoft spol. s r.o., IČO 18826024, ARES 1991), Advokátní spis
    (ATLAS consulting spol. s r.o., IČO 46578706, ARES 1992), Evolio (AVE Soft s.r.o., IČO
    25378392, ARES 1997), Praetor (Wolters Kluwer ČR, IČO 63077639), ISAK, and Acta Safe — of
    which only SingleCase was previously on file anywhere in the register. That is exactly the
    class of vendor a capital-and-tender ledger is structurally blind to, so the method
    demonstrably produces positives here and its negative carries weight. NOT FOUND: no Czech
    product sells the responding side of a consumer-credit dispute — no arbiter docket, no
    deadline clock against a Financial Arbitrator proceeding, no settlement decisioning, no
    pack assembly from a loan file. Everything found sells something else and is recorded in
    locals[]: aCompliance sells the work as a service; ePohledávky.cz, Barrister and Evolio
    automate the creditor pursuing the debtor; SingleCase, Praetor, Advokátní spis, E-OFFICE
    Advokát, ISAK and Aptien are general matter and record management. Query 3, aimed straight
    at mass creditworthiness claims and creditor defence, returned only legal commentary
    (epravo.cz, kn.cz) and the arbiter''s own pages — no vendor of any kind. NOT LEDGERED, and
    why: abcreklamace.cz surfaced on query 1 as a Czech complaints-registry system, but the
    domain now redirects to an unrelated betting-affiliate site, so the product is gone and
    recording a dead link would be worse than not recording it; Acta Safe surfaced on query 2
    as a legal-office tool on a Webnode subdomain and nothing about it could be verified, so
    it is named here rather than claimed in the ledger. gap moves 1 to 2 on this controlled
    check: the field is dense, everyone in it is recorded, and nobody in it sells this.'
  date: '2026-08-25'
  queries:
    - 'software pro vyřizování reklamací a stížností klientů nebankovní poskytovatel úvěru evidence lhůt odpověď finančnímu arbitrovi'
    - 'český software pro právní oddělení evidence sporů lhůt a spisů advokátní kancelář správa případů'
    - 'hromadné žaloby na neposouzení úvěruschopnosti obrana věřitele nástroj automatizace odpovědí finanční arbitr poskytovatelé úvěrů 2026'
    - 'outsourcing vyřizování stížností a mimosoudních sporů klientů pro finanční instituce Česko služba compliance nebankovní věřitel'
  checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
  expires: '2026-11-23'
created: '2026-08-13'
updated: '2026-09-02'
---

The Kancelář finančního arbitra — the out-of-court forum for consumer disputes with banks and lenders — took 2,660 new cases in 2023, 5,683 in 2024, 12,050 in 2025 and 8,200 more by May 2026, on track for about 20,000 [S1]. Consumer credit is 92% of the running caseload, mostly claims the lender never checked the borrower could repay (úvěruschopnost) [S1].

Why now: the arbiter reports claims filed at mass scale — a claims industry, not one-off grievances — while lenders answer one at a time [S1]. Cases average 167 days; 83% of those concluded settle [S1].

Who pays: non-bank lenders and banks, who must produce documents, take a legal position and decide whether to settle on every case the arbiter opens [S1]. At 2026 volumes that is tens of thousands of cases a year, answered by hand by in-house legal teams and outside law firms [S1,S4]. The arbiter, at 167 days a case, is a third buyer [S1].

Existing non-solutions: people, billed by the hour [S4]. aCompliance takes the job off the lender, handling complaints and arbiter disputes for non-bank lenders as a service rather than software [S5]. Czech software points elsewhere: ePohledávky.cz, Barrister and Evolio chase debtors for creditors, while SingleCase, Praetor, Advokátní spis, E-OFFICE Advokát, ISAK and Aptien sell general law-office tooling — files, deadlines, billing — with nothing for an arbiter case [S7]. Nobody sells the defending side a product [S7].

Solved elsewhere: Casap has automated the bank payment-dispute cycle since 2023 on a $25M Series A at a $105M valuation — the one seller old enough to prove the model [S3]. ClaimSorted, London 2024, handles claims for twenty-plus insurers on $13.3M; Audun is four people in Oslo building AI debt collection [S3]. All three sit one vertical away; nobody is recorded building consumer-credit dispute response [S3].

## First moves

1. Sell to non-bank lenders first — they carry about 92% of the arbiter's caseload [S1]. Every case is answered by hand today, in-house or by outside law firms [S4]. Shadow one lender for a week, count the lawyer hours a case burns, and price against that.
2. Build the settlement call first. 83% of concluded cases settle, so that is the decision a lender actually makes [S1]. Then add the deadline clock on each proceeding and the response pack assembled from the loan file: nothing sold in Czech does any of the three [S7].
3. Open with the trend line. Filings ran 2,660 in 2023, 5,683 in 2024 and 12,050 in 2025, with 8,200 more by May 2026 and the average case at 167 days [S1].
4. Watch the two who could move in. aCompliance sells this exact job today, but as a firm doing the work, and it has traded since 2014 [S5]. Praetor, from Wolters Kluwer's Czech arm, is the widest-selling case-management system in Czech law firms and one product decision away [S7]. Ten Czech vendors turned up in that sweep and not one handles a case at the arbiter [S7].

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "each incoming FA proceeding" now reads "each new case at the Financial Arbitrator", and "external advokáti" now reads "outside law firms". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the first VeKLEP harvest put the Finance Ministry's pending revision of the Consumer Credit Act 257/2016 on the ledger as a context receipt [S6] — the statute generating the docket is being rewritten. No score moved by that pass. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 1 → 2. Casap passes the test outright — selling since 2023, so the three-year limb is met, on a $25M Series A at a $105M valuation — which is one established foreign player, rung 2. ClaimSorted and Audun do not: ClaimSorted opened in 2024 and Audun in 2026, both inside the three-year limb, so neither counts however well funded. Rung 3 was considered and declined: it needs establishment in two-plus markets with one CEE-adjacent, and Casap's United States is the only market with an established seller in it. `scores.gap` stays 1. The five Czech offerings the [S5] sweep found were lifted into a structured `locals[]` ledger and every one reads early on receipts — aCompliance sells the arbiter-dispute work as a service with no product behind it, ePohledávky.cz and Barrister automate the creditor pursuing the debtor rather than defending a claim, and SingleCase and Aptien are generic case management with no arbiter docket; none publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or state listing. Early local players do not close a space, so gap does not fall to 0; and it does not rise to 2 either, because [S5] found local players rather than none. `score` 5 → 6. The two Proven-abroad paragraphs were merged into one. The first, "Solved elsewhere, weakly", asserted the old score in words — "no funded analog exists" — and, because it is not the literal lead-in, it was rendering inside the local-competition section rather than the foreign one. The merged paragraph keeps its honest limit intact: the only proven seller is one vertical away, and nobody anywhere has been documented productising consumer-credit dispute response. Avallon, Basepilot and Amera dropped out of the body with it; they remain in the [S3] source note, unedited. Money, urgency and demand untouched; no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. All five entries are `competes: adjacent`, and every evidence line now leads with what the player actually sells. aCompliance is the sharpest case and the reason the field exists: it handles complaints and out-of-court disputes at the financial arbiter for non-bank lenders, the same job for the same buyer, but as a firm doing the work rather than software a lender runs itself — the service-instead-of-product limb of adjacency. ePohledávky.cz and Barrister sit on the pursuit side of the same relationship, automating the creditor chasing the debtor; SingleCase and Aptien sell generic matter and record management with no arbiter docket in them. `scores.gap` stays 1 and is FLAGGED rather than moved. Under the new ladder rung 1 means locals sell this and are all early, and nothing on this ledger sells it: [S4] searched and found no Czech product for dispute-response operations. Rung 2 is the arguable score, but moving it is a MATCH judgment and not a content pass, so it is written down here and left to the owner. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

FIFTH PASS THIS DATE, MERGED HERE: the local field was searched properly and `scores.gap` 1 → 2, `score` 6 → 7. The score it replaces rested on a check whose own note ends "Gap 1 (quick search, no CZ player found)" — a self-declared quick search with no queries recorded, and old-ladder language besides. Under the current ladder rung 1 means locals sell this and are all early; nothing on this ledger sold it, so the record was understating itself on a receipt nobody could audit. [S7] is that check run for real: four Czech query shapes in a lender's descriptive language, and TWO positive controls run and passed BEFORE any conclusion was drawn. The first returned aCompliance — the one Czech offering aimed at this exact need — at the top of its own query. The second, aimed at Czech legal case software, returned six bootstrapped Czech vendors on a single page, of which only SingleCase was anywhere in the register beforehand; that is the class of vendor a capital-and-tender ledger cannot see, so the method demonstrably produces positives here and its negative is worth something. It found no Czech product that runs the responding side of a consumer-credit dispute: no arbiter docket, no deadline clock against a proceeding, no settlement decisioning. FIVE PLAYERS ADDED under the no-exclude rule, all new to the register and all `competes: adjacent`: Evolio (AVE Soft s.r.o., IČO 25378392), whose bulk electronic payment-order filing puts it on the pursuit side beside ePohledávky.cz and Barrister; and Praetor (Wolters Kluwer ČR, IČO 63077639), Advokátní spis (ATLAS consulting, IČO 46578706), E-OFFICE Advokát (AISoft, IČO 18826024) and ISAK, which are general matter tooling beside SingleCase and Aptien. Praetor is the one a builder should look at twice — the widest-selling case-management system in Czech law firms, one product decision away from this — and its entry says so. aCompliance gained the IČO and registration year the ledger lacked (Acompliance poradenství s.r.o., ARES 2014-01-28) and stays early: twelve years of trading meets the first limb, and its page names no client and publishes no tally, so no second limb is met. TWO PLAYERS DELIBERATELY NOT LEDGERED, and the reason is written into [S7]: abcreklamace.cz is a dead domain that now redirects to a betting-affiliate site, and Acta Safe could not be verified at all. Every evidence line also dropped the repository filename it used to print to the reader. The non-solutions paragraph was rewritten to match the ledger and to name the choice a lender actually faces — hand the disputes to aCompliance, or run them on software that does not exist here. Proof, money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S7] is appended, not inserted.

2026-08-20 · evidence audit — Three legal-status claims removed, none of which the register ever checked. The arbiter's forum was described as mandatory: neither S1's note nor the underlying signal says so. The interest-voiding doctrine ("a failed assessment can void the credit contract's interest") is gone — the corpus records only that creditworthiness-assessment claims dominate the docket, nothing about the remedy. And "Free proceedings with no lawyer requirement remove any natural brake on volume": both procedural facts had no receipt. The caseload figures, the settlement rate and the proceeding length are unaffected; they are receipted [S1].

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 10 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the non-bank lenders carrying 92% of the docket as the first buyer [S1], a settlement recommendation as the first thing to build because 83% of cases settle [S1,S7], the filing trend as the opening fact [S1], and aCompliance and Praetor named as the two that could turn [S5,S7]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Three trade terms glossed at first use: E-OFFICE Advokát and ISAK now sit inside a plain description of what law-office software does, and Wolters Kluwer ČR reads as Wolters Kluwer's Czech arm. Argument cut from 450 words to 300, every figure, named firm and [Sn] marker kept. A gist added to all seven sources. First moves rewritten verbs-first. No score, status, note or marker touched.
