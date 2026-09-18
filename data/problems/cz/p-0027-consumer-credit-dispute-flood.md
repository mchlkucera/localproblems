---
id: p-0027
region: cz
title: 'Czech lenders pay lawyers by the hour to answer loan complaints that have quadrupled since 2023'
brief: 'Borrowers take lenders to the state''s financial arbiter, mostly saying nobody checked they could repay [S1]. Every case needs documents and a legal answer written by hand, and this year is heading for about 20,000 [S1,S4].'
solution: 'Build case software for lenders that pulls the loan file, drafts the reply to the arbiter and tracks deadlines.'
good_for: 'Someone who can build legal software and sell to banks and lenders.'
price_search: 'No public buyer pays for this, so ask the head of legal or compliance at a
  non-bank lender from the Czech National Bank''s register of consumer-credit providers what
  outside counsel bills per financial-arbiter case, or ask a Czech law firm its fee for
  "zastupování před finančním arbitrem" (representation before the arbiter); registr smluv
  full-text for "Kancelář finančního arbitra" shows only what the arbiter itself pays for
  case-handling software, and the MS2021+ index has nothing on it.'
category: fintech
geo: CZ-national
score: 9
scores:
  proof: 2
  money: 0
  urgency: 3
  demand: 2
  gap: 2
status: candidate
entry:
  level: moderate
  buyer: large-firms
  permission: none
  incumbents: open
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed, none of the ten Czech vendors found handles arbiter cases, and the caseload keeps growing. Harder: the buyers are banks and lenders whose lawyers must trust software with case files, a Czech firm already sells this work to non-bank lenders, and the credit law behind the claims is changing.'
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
process:
  summary:
    today: 'Borrowers, many through claims firms filing in bulk, take complaints to the financial arbiter, and law firms or an outsourced service answer each one for the lender by hand [S1,S4].'
  steps:
  - who: A borrower, or a claims firm filing in bulk
    today: 'Files a complaint with the arbiter'
    known: documented
    cites: [1]
    change: stays
    after: 'Unchanged: the borrower still files'
  - who: A law firm or outsourced service, for the lender
    today: 'Writes each answer to the arbiter by hand'
    known: documented
    cites: [4, 5]
    change: changes
    after: 'Checks a reply drafted from the loan file'
  - who: '?'
    today: 'How a lender tracks each case''s deadlines is not known'
    known: unknown
    cites: []
    change: changes
    after: 'Software tracks every case deadline'
  - who: The lender and the borrower
    today: 'Settle most of the cases that end'
    known: documented
    cites: [1]
    change: stays
    after: 'Unchanged: settling stays their call'
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
- type: regulation
  name: "ADR directive 2025/2647 — the financial arbiter's law to be amended (planned)"
  gist: "the arbiter's rules, rewritten for 2028"
  why: "Two planned Czech bills bring an EU directive on out-of-court consumer disputes into Czech law, one of them amending the Financial Arbiter Act. From 20 September 2028 a trader contacted by a dispute body must say within 20 working days whether it will take part."
  url: https://vlada.gov.cz/assets/media-centrum/dulezite-dokumenty/1234_2026_priloha_c-_2.pdf
  note: 'reg-adr-spotrebitelske-spory-2028 (reg-scan, 2026-09-18), linked in MATCH 2026-09-18.
    Plán legislativních prací vlády 2026, annex 2: MPO-2 amends the Consumer Protection Act
    634/1992 and MF-3 the Financial Arbiter Act 229/2002 to transpose Directive (EU) 2025/2647,
    government deadline 2027 Q2, planned effect 09.2028. EUR-Lex Art 5(1), per the signal:
    adopt by 20 Mar 2028, apply from 20 Sep 2028; the new paragraph 9 makes a trader contacted
    by an ADR entity say within at most 20 working days (30 for complex disputes) whether it
    agrees to take part. DRAFT on the Czech side, date at risk; the EU dates are fixed. Backs
    urgency at deadline 1 on its own (over 18 months out); the deadline point is carried by S9.'
  date: '2028-09-01'
  signal: reg-adr-spotrebitelske-spory-2028
- type: regulation
  name: "CCD2 — the EU consumer-credit directive applies from 20 November 2026"
  gist: "the EU credit rules, from November"
  why: "The EU's new consumer-credit directive applies from 20 November 2026: buy-now-pay-later, interest-free deferred payment and loans under €200 come under consumer-credit law, with a duty to check that the borrower can repay."
  url: https://eur-lex.europa.eu/eli/dir/2023/2225/oj
  note: 'reg-ccd2-consumer-credit (ledger signal, not new this run), linked in MATCH 2026-09-18
    on the coordinator''s instruction to check the CCD2 signals against this record. Directive
    (EU) 2023/2225, verified on EUR-Lex Art 48 per the signal: transposition by 20 Nov 2025,
    measures apply from 20 Nov 2026. Scope extends to BNPL, interest-free deferred payment and
    loans under EUR 200, with mandatory creditworthiness assessment. WHY IT MOVES URGENCY: the
    creditworthiness check is the duty most arbiter claims say was broken (S1), and its new rules
    bind lenders in under 18 months, so the deadline sub-score goes 0 to 2. S6, the Czech bill,
    had been held as undated context because its VeKLEP record carried no date; S10 shows that
    bill takes effect on this same EU date. That more claims will follow the wider scope is an
    inference, not a finding of this source.'
  date: '2026-11-20'
  signal: reg-ccd2-consumer-credit
- type: regulation
  name: "Finance ministry — the Czech CCD2 bill and its effective date"
  gist: "the Czech bill, due by November"
  why: "The finance ministry's amendment of the Consumer Credit Act brings the EU directive into Czech law with effect on the binding EU date, 20 November 2026. It predates the October 2025 election and still has to pass, so the Czech date can slip."
  url: https://mf.gov.cz/cs/financni-trh/spotrebitelske-uvery/aktuality/2025/meziresortni-pripominkove-rizeni-k-navrhu-novely-z-58892
  note: 'reg-ccd2-bnpl-2026 (ledger signal, not new this run), linked in MATCH 2026-09-18. MF
    amendment to Consumer Credit Act 257/2016, inter-ministerial comments Feb 2025, the same
    bill S6 records on VeKLEP (KORNDDVFVG8B, since 14 Feb 2025; the fr-algoan signal of
    2026-09-18 ties the two). Transposes CCD2 with effect on 20 Nov 2026; BNPL, interest-free
    credit and small short-term loans enter scope, with stricter creditworthiness assessment and
    advertising rules. Stage: draft; the bill predates the 10/2025 election and must be
    (re)passed by 11/2026; date at risk.'
  date: '2026-11-20'
  signal: reg-ccd2-bnpl-2026
created: '2026-08-13'
updated: '2026-09-18'
---

Complaints to the state's financial arbiter, mostly about consumer loans, more than quadrupled from 2023 to 2025, and law firms answer them by hand [S1,S4].

- 12,050 new cases reached the arbiter in 2025, against 2,660 in 2023 [S1].
- 8,200 more came by May 2026, on track for about 20,000 this year [S1].
- Consumer credit is about 92% of the cases still running [S1].

The arbiter, the Kancelář finančního arbitra, is the out-of-court forum for consumer disputes with banks and lenders [S1]. Most claims say the lender never checked that the borrower could repay, a duty the law calls creditworthiness assessment [S1].

- In 2024 there were 5,683 new cases, so 2025 more than doubled it [S1].
- 15,446 cases were running when the 2025 report came out [S1].
- The industry and trade ministry counts about 18,700 filings at the arbiter from 2020 to mid-2025, strongly rising [S2]. They sit among more than 45,000 out-of-court consumer disputes across all sectors [S2].
- So the caseload recurs year after year; it is not a one-year spike [S2].

Existing non-solutions: Law firms and one service firm handle these cases by hand, and no Czech software for the lender's side was found [S4,S7].

Ten Czech vendors turned up, and none handles a case at the arbiter [S7]:

- One firm takes the job off non-bank lenders, handling their complaints and arbiter disputes as a service, with people rather than software [S5].
- Three sell software for the other side of the relationship, the creditor chasing a debtor, one of them by filing payment orders in bulk [S5,S7].
- Six sell general law-office or company tooling, such as files, deadlines and billing, with nothing for an arbiter case [S5,S7].
- The widest-selling Czech case-management system for law firms is among those six, and it is the one best placed to add an arbiter docket [S7].
- No Czech product was found keeping an arbiter docket, running a deadline clock on each proceeding, deciding which cases to settle, or assembling the answer from the loan file [S7].
- Searches also returned the arbiter's own pages, consumer advice sites and law firms working cases by hand [S4].

Why now: Lenders already answer bulk claims one at a time, and from 20 November 2026 the repayment check those claims turn on covers more loans [S1,S9].

- Claims firms now file at mass scale, not as one-off grievances [S1].
- Each case takes 167 days on average, tying up the lender's lawyers [S1].
- 83% of concluded cases end in a settlement [S1].

The EU rules behind most claims change on 20 November 2026, and the arbiter's own rules follow in 2028 [S8,S9]:

- The finance ministry is revising the Consumer Credit Act, Act No. 257/2016, and its draft has been on the government's legislative portal since 14 February 2025 [S6].
- That act sets the duty to check that a borrower can repay, the duty most claims say was broken [S1,S6].
- The draft brings the EU's new consumer-credit directive into Czech law, and the directive applies from 20 November 2026 [S9,S10].
- From that date the repayment check also covers buy-now-pay-later, interest-free deferred payment and loans under €200 [S9].
- The Czech bill predates the October 2025 election and still has to pass, so the Czech date can slip [S10].
- From 20 September 2028 a second EU directive rewrites out-of-court consumer disputes, and the finance ministry plans to amend the Financial Arbiter Act for it [S8]. A trader contacted by a dispute body must then say within 20 working days whether it will take part [S8].

Who pays: Lenders must answer every case, and a Czech firm sells them that work, but no buyer or price for it is public [S1,S5].

- Every case needs the lender's documents and a legal answer, written by hand [S1,S4].
- A Czech firm markets arbiter-dispute handling to non-bank lenders as a service [S5].
- Law firms work these cases by hand [S4].

Banks and non-bank lenders must produce documents, take a legal position and decide whether to settle on every case the arbiter opens [S1].

- At this year's pace that is about 20,000 cases, answered by in-house legal teams and outside law firms [S1,S4].
- The arbiter itself, at 167 days a case, could be a third buyer [S1].

Solved elsewhere: A US company automates bank payment disputes, and funded firms abroad automate insurance claims and debt collection, one step from this [S3].

The US company has sold software for the payment-dispute cycle of banks and credit unions since 2023, on a Series A raised in 2025. It is the only one of these sellers with three years of selling behind it.

A London company founded in 2024 and backed by Y Combinator, the US startup accelerator, processes claims for insurers [S3]. In Norway, a small team backed by the same accelerator builds AI debt collection [S3]. In US insurance, Avallon AI, Basepilot and Amera also sell claims operations built on AI [S3].

All of them sit one market away, and no funded company was found doing dispute response for consumer credit [S3].

## First moves

1. Contact the head of legal at one non-bank lender and shadow its arbiter cases for a week, counting the lawyer hours each case burns. Consumer credit is almost all of the arbiter's caseload, and each case is answered by hand; see [The opportunity](#opportunity) and [Competition](#competition). The hours you count are what your software saves, so price against them. Start with non-bank lenders, because a Czech firm already markets this work to them, which shows they are the ones looking for help; see [Willing to pay](#willing-to-pay).
2. Build the settlement call first: a tool that tells a lender, from the loan file, whether a case is worth fighting or settling. Most concluded cases settle, so that is the decision a lender actually makes; see [Why now](#why-now). Then add a deadline clock on each proceeding and the answer pack assembled from the loan file. No Czech product was found doing any of the three; see [Competition](#competition).
3. Open every sales call with the arbiter's own count of new cases, which more than quadrupled in two years. The yearly counts and this year's pace are under [The opportunity](#opportunity), and the months each case takes are under [Why now](#why-now). A lender's head of legal already feels the load; the counts show it is the whole market and not bad luck, and it keeps coming back every year.
4. Watch the two Czech players who could move into this: the firm that sells the work as a service, and the leading law-office software. The service firm does this exact job for non-bank lenders, with people rather than software, and has traded for years. The software vendor sells the widest-selling case-management system in Czech law firms and is one product decision away; see [Competition](#competition). None of the Czech vendors found handles an arbiter case yet, so move before either of them does.

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "each incoming FA proceeding" now reads "each new case at the Financial Arbitrator", and "external advokáti" now reads "outside law firms". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: the first VeKLEP harvest put the Finance Ministry's pending revision of the Consumer Credit Act 257/2016 on the ledger as a context receipt [S6] — the statute generating the docket is being rewritten. No score moved by that pass. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 1 → 2. Casap passes the test outright — selling since 2023, so the three-year limb is met, on a $25M Series A at a $105M valuation — which is one established foreign player, rung 2. ClaimSorted and Audun do not: ClaimSorted opened in 2024 and Audun in 2026, both inside the three-year limb, so neither counts however well funded. Rung 3 was considered and declined: it needs establishment in two-plus markets with one CEE-adjacent, and Casap's United States is the only market with an established seller in it. `scores.gap` stays 1. The five Czech offerings the [S5] sweep found were lifted into a structured `locals[]` ledger and every one reads early on receipts — aCompliance sells the arbiter-dispute work as a service with no product behind it, ePohledávky.cz and Barrister automate the creditor pursuing the debtor rather than defending a claim, and SingleCase and Aptien are generic case management with no arbiter docket; none publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or state listing. Early local players do not close a space, so gap does not fall to 0; and it does not rise to 2 either, because [S5] found local players rather than none. `score` 5 → 6. The two Proven-abroad paragraphs were merged into one. The first, "Solved elsewhere, weakly", asserted the old score in words — "no funded analog exists" — and, because it is not the literal lead-in, it was rendering inside the local-competition section rather than the foreign one. The merged paragraph keeps its honest limit intact: the only proven seller is one vertical away, and nobody anywhere has been documented productising consumer-credit dispute response. Avallon, Basepilot and Amera dropped out of the body with it; they remain in the [S3] source note, unedited. Money, urgency and demand untouched; no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. All five entries are `competes: adjacent`, and every evidence line now leads with what the player actually sells. aCompliance is the sharpest case and the reason the field exists: it handles complaints and out-of-court disputes at the financial arbiter for non-bank lenders, the same job for the same buyer, but as a firm doing the work rather than software a lender runs itself — the service-instead-of-product limb of adjacency. ePohledávky.cz and Barrister sit on the pursuit side of the same relationship, automating the creditor chasing the debtor; SingleCase and Aptien sell generic matter and record management with no arbiter docket in them. `scores.gap` stays 1 and is FLAGGED rather than moved. Under the new ladder rung 1 means locals sell this and are all early, and nothing on this ledger sells it: [S4] searched and found no Czech product for dispute-response operations. Rung 2 is the arguable score, but moving it is a MATCH judgment and not a content pass, so it is written down here and left to the owner. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

FIFTH PASS THIS DATE, MERGED HERE: the local field was searched properly and `scores.gap` 1 → 2, `score` 6 → 7. The score it replaces rested on a check whose own note ends "Gap 1 (quick search, no CZ player found)" — a self-declared quick search with no queries recorded, and old-ladder language besides. Under the current ladder rung 1 means locals sell this and are all early; nothing on this ledger sold it, so the record was understating itself on a receipt nobody could audit. [S7] is that check run for real: four Czech query shapes in a lender's descriptive language, and TWO positive controls run and passed BEFORE any conclusion was drawn. The first returned aCompliance — the one Czech offering aimed at this exact need — at the top of its own query. The second, aimed at Czech legal case software, returned six bootstrapped Czech vendors on a single page, of which only SingleCase was anywhere in the register beforehand; that is the class of vendor a capital-and-tender ledger cannot see, so the method demonstrably produces positives here and its negative is worth something. It found no Czech product that runs the responding side of a consumer-credit dispute: no arbiter docket, no deadline clock against a proceeding, no settlement decisioning. FIVE PLAYERS ADDED under the no-exclude rule, all new to the register and all `competes: adjacent`: Evolio (AVE Soft s.r.o., IČO 25378392), whose bulk electronic payment-order filing puts it on the pursuit side beside ePohledávky.cz and Barrister; and Praetor (Wolters Kluwer ČR, IČO 63077639), Advokátní spis (ATLAS consulting, IČO 46578706), E-OFFICE Advokát (AISoft, IČO 18826024) and ISAK, which are general matter tooling beside SingleCase and Aptien. Praetor is the one a builder should look at twice — the widest-selling case-management system in Czech law firms, one product decision away from this — and its entry says so. aCompliance gained the IČO and registration year the ledger lacked (Acompliance poradenství s.r.o., ARES 2014-01-28) and stays early: twelve years of trading meets the first limb, and its page names no client and publishes no tally, so no second limb is met. TWO PLAYERS DELIBERATELY NOT LEDGERED, and the reason is written into [S7]: abcreklamace.cz is a dead domain that now redirects to a betting-affiliate site, and Acta Safe could not be verified at all. Every evidence line also dropped the repository filename it used to print to the reader. The non-solutions paragraph was rewritten to match the ledger and to name the choice a lender actually faces — hand the disputes to aCompliance, or run them on software that does not exist here. Proof, money, urgency and demand untouched; no existing source note edited and no existing [Sn] marker moved — [S7] is appended, not inserted.

2026-08-20 · evidence audit — Three legal-status claims removed, none of which the register ever checked. The arbiter's forum was described as mandatory: neither S1's note nor the underlying signal says so. The interest-voiding doctrine ("a failed assessment can void the credit contract's interest") is gone — the corpus records only that creditworthiness-assessment claims dominate the docket, nothing about the remedy. And "Free proceedings with no lawyer requirement remove any natural brake on volume": both procedural facts had no receipt. The caseload figures, the settlement rate and the proceeding length are unaffected; they are receipted [S1].

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 10 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the non-bank lenders carrying 92% of the docket as the first buyer [S1], a settlement recommendation as the first thing to build because 83% of cases settle [S1,S7], the filing trend as the opening fact [S1], and aCompliance and Praetor named as the two that could turn [S5,S7]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Three trade terms glossed at first use: E-OFFICE Advokát and ISAK now sit inside a plain description of what law-office software does, and Wolters Kluwer ČR reads as Wolters Kluwer's Czech arm. Argument cut from 450 words to 300, every figure, named firm and [Sn] marker kept. A gist added to all seven sources. First moves rewritten verbs-first. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` telling the situation, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Complaints about Czech consumer loans have quadrupled, all handled by hand". Previous solution, verbatim: "Case software for lenders answering complaints at the Financial Arbitrator: pull the loan file, draft the response, hold every deadline, and flag which cases to settle." No brief or good_for existed before. Checked against the sources while writing. "All handled by hand" is gone from the title: it rests on a search that found no Czech product and on law firms seen working cases manually [S4,S7], which is a not-found and no count of how every case is answered. "Quadrupled" became "more than 4 times since 2023", the arbiter's own growth from 2,660 new cases in 2023 to 12,050 in 2025 and, for consumer credit alone, from 2,097 to 11,386 [S1]. The 12,050 is every new case at the arbiter, not only loan cases, so the brief says "mostly against lenders" — consumer credit is ~92% of the running caseload and creditworthiness claims dominate it [S1] — rather than calling all of them loan complaints. "Nearly 50 a working day" is 12,050 divided by roughly 250 Czech working days. The dek's "lenders must produce documents and take a legal position on every case" was not carried into the brief: it is a reading of the procedure, and [S1]'s note does not state it. The solution's "as companies abroad do" rests on Casap, which automates bank payment disputes in the US [S3]; nobody on file does it for consumer-credit disputes, so the line names payment disputes and not this. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Brief before: "Customers filed 12,050 complaints with the state's financial arbiter in 2025, nearly 50 a working day, mostly against lenders they say didn't check they could repay [S1]. Another 8,200 came by May 2026, and cases stay open 167 days on average [S1]." After: "Borrowers say lenders didn't check they could repay, and take them to the state's financial arbiter [S1]. It got 12,050 complaints last year, mostly against lenders, and cases drag on for months [S1]." Solution before: "Build case software that pulls a lender's loan file, drafts its reply to the arbiter and tracks deadlines, as companies abroad do for payment disputes." After: "Build case software for lenders that pulls the loan file, drafts the reply to the arbiter and tracks deadlines." "Nearly 50 a working day", the 8,200 by May 2026 and "167 days on average" were cut to keep one number, the 12,050; 167 days is put as "months" [S1]. "Mostly against lenders" stays because the 12,050 counts every case at the arbiter [S1]. The payment-disputes comparison abroad was cut for length. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed. Same date, pain-point pass: title "Complaints about Czech consumer loans have grown more than 4 times since 2023" → "Czech lenders now fight more than 4 times as many loan complaints as in 2023". Why: the old headline was a growth figure with no one named. The new one names who carries it: lenders, who must answer every case the arbiter opens, by hand, in cases averaging 167 days [S1,S4]. The figure is unchanged: 2,660 new proceedings in 2023 against 12,050 in 2025 [S1]. Brief unchanged. No score, status, source, note or body sentence changed. Same date, owner-approved card: title "Czech lenders now fight more than 4 times as many loan complaints as in 2023" became "Czech lenders pay lawyers by the hour to answer loan complaints that have quadrupled since 2023"; brief "Borrowers say lenders didn't check they could repay, and take them to the state's financial arbiter [S1]. It got 12,050 complaints last year, mostly against lenders, and cases drag on for months [S1]." became "Borrowers take lenders to the state's financial arbiter, mostly saying nobody checked they could repay [S1]. Every case needs documents and a legal answer written by hand, and this year is heading for about 20,000 [S1,S4]."; good_for "Someone who'd like to build software for banks and lenders." became "Someone who can build legal software and sell to banks and lenders.". Sources: 2,660 cases in 2023 to 12,050 in 2025 is 4.5x, so "quadrupled" [S1]; 8,200 by May 2026 puts the year on track for about 20,000, the arbiter's own pace [S1]; answered by in-house legal teams and law firms billed by the hour [S1,S4].

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the caseload more than quadrupling and holds the yearly counts, and gained from the notes the 15,446 running cases [S1] and the industry and trade ministry's count of about 18,700 arbiter filings from 2020 to mid-2025 among 45,000+ consumer disputes, the first time [S2] is cited in the body. Why now opens on the claims industry filing in bulk, with 167 days and the 83% settlement rate as pain items [S1], and gained the Consumer Credit Act draft, on the legislative portal since 14 February 2025 with no dated obligation, the first time [S6] is cited in the body. Willing to pay answers that lenders must answer every case and a Czech firm sells that work, with no buyer or price public [S1,S5]. Competition describes all ten Czech vendors by what they sell, grouped as the one service firm, the three on the collecting side and the six general law-office tools, and holds the four capabilities no Czech product was found doing [S5,S7]. Validated abroad describes the three foreign companies without names or figures, which stay in their ledger rows, and restores Avallon AI, Basepilot and Amera from [S3]'s note. Every comps[] and locals[] name left the body and the moves. The moves lost every [Sn] marker and figure for links; move 1 now contacts one lender's head of legal instead of selling. `entry.why` was rewritten as "Easier: … Harder: …" with the same gates. A `process:` block was added, four steps from sources already cited: the borrower or a claims firm filing in bulk [S1], a law firm or outsourced service writing each answer by hand [S4,S5], how a lender tracks deadlines marked unknown, and most concluded cases settling [S1]; the record should join `PROCESS_PHRASE_ENFORCED` with the body gate. Corrected against the sources: old move 1 said non-bank lenders "carry about 92% of the arbiter's caseload", but [S1]'s note says consumer credit is ~92% of the running proceedings, banks included, so the move now says consumer credit is almost all of the caseload; the Casap sentence carried [S3], whose note does not mention Casap (its figures come from the comps ledger), so the marker is gone with the figures; "tens of thousands of cases a year" became "about 20,000", the 2026 projection in [S1]'s note; "people, billed by the hour [S4]" became "law firms handle these cases by hand", since [S4]'s note records manual handling and nothing about hourly billing (the title's "pay lawyers by the hour" rests on the same note and is left to the owner); and "Nobody sells the defending side a product [S7]" became "no Czech product was found", in [S7]'s own not-found terms. Flagged as inference: that lenders must produce documents, take a legal position and decide whether to settle on every case, a reading of the procedure that [S1]'s note does not state; that in-house legal teams answer cases, which no note says, and that the law firms in [S4]'s note work for the lender; that cases are answered one at a time and tie up the lender's lawyers [S1]; that the arbiter could be a third buyer; and, in `entry.why`, that lenders' lawyers must trust software with case files. No score, status, source, `note:`, `sources[]` order, title, brief, solution or good_for changed. Same date, later pass, merged here: re-scored on regulation added. The EU consumer-credit directive behind the Czech bill in [S6] applies from 20 November 2026 and extends the repayment check most claims turn on to buy-now-pay-later, interest-free deferred payment and loans under €200 [S9]; the bill takes effect that day but still has to pass [S10]. That is a compliance date under 18 months, so the deadline sub-score goes 0 to 2: `scores.urgency` 1 → 3 and `score` 7 → 9. The planned amendment of the Financial Arbiter Act for a second directive, applying from 20 September 2028, was added too [S8]. Corrected: "The draft carries no dated obligation yet [S6]" is withdrawn, because [S10] dates the same bill. Why now's answer sentence was "Lenders face a claims industry that files in bulk, while each case takes months and is answered one at a time [S1]." and now names the November date. Flagged as inference: that the wider scope will bring new claims. Not linked: the fr-algoan signal, which sells lenders the repayment check itself rather than dispute handling.
