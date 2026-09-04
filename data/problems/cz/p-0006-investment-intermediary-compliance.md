---
id: p-0006
region: cz
title: Thousands of Czech investment intermediaries and advisors face growing ČNB/MiFID paperwork
  today and a directly applicable EU AML rulebook from July 2027
fix: 'Compliance software for investment-advice firms covering the half nobody sells here
  yet: client-suitability paperwork, tied-agent oversight and the reporting the Czech
  central bank requires.'
category: fintech
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 0
  urgency: 3
  demand: 1
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'The vendor itself is unregulated — a dev plus a compliance lawyer can ship AMLR-ready
    policy and KYC workflow SaaS, but intermediary-network sales cycles put first revenue
    months out.'
comps:
- name: Saturn
  url: https://www.saturnos.com/
  geo: GB
  since: 2023
  traction: '€12.9M Series A led by Singular (EU-Startups, 2025); 600+ UK advisory firms and 6,500+ advisers on platform'
  signal: yc-saturn
- name: Muinmos
  url: https://muinmos.com/
  geo: DK
  since: 2012
  traction: 'raise undisclosed; 19 employees (Tracxn, 2026); regulatory onboarding/KYC engine for banks and investment firms globally'
- name: Apiax
  url: https://www.apiax.com/
  geo: CH
  since: 2017
  traction: '$6.6M Series A (Crowdfund Insider, 2019) after $1.5M seed; machine-readable compliance rules for banks and wealth managers'
locals:
- name: AML Proof
  url: https://amlproof.ai/cs/aml-software
  ico: '23791497'
  since: 2025
  competes: direct
  maturity: early
  evidence: 'A Czech cloud anti-money-laundering platform sold to the firms the law obliges,
    which it names as financial advisers and intermediaries: client identification, screening
    against sanctions and politically-exposed-person lists, beneficial-owner verification, risk
    scoring, an internal-policy document, reporting to the financial intelligence unit and
    ten-year archiving, self-serve from 25 CZK a credit. AML Proof, s.r.o. was incorporated on
    1 October 2025, so it has been selling for under a year.'
- name: AML solutions
  ico: '10691766'
  since: 2021
  competes: direct
  maturity: early
  evidence: 'Sells sanctions and politically-exposed-person screening to the same obliged firms
    as AML Proof, against the same law. AML solutions s.r.o. has been on the state business
    register since March 2021, and it names no client, holds no public contract and discloses
    no funding.'
- name: Resistant AI
  ico: '07825439'
  since: 2019
  competes: adjacent
  maturity: established
  evidence: 'Sells document-fraud and financial-crime detection to banks and fintechs — it scores
    whether a document or a transaction is forged — with Payoneer, AXA and Finom on its own
    reference list, a USD 25M Series B in October 2025 led by DTCP, and trading since January
    2019. An investment intermediary needs the opposite job done: its own suitability
    questionnaires, tied-agent oversight and central-bank reporting produced and archived.'
- name: Broker Trust
  ico: '26439719'
  since: 2001
  competes: adjacent
  maturity: early
  evidence: 'Runs the Bety 2.0 and BT Invest platform for its own tied advisers, with a
    compliance methodology behind it — the closest thing on the Czech market to the suitability
    and oversight tooling an independent intermediary would buy. It is not for sale: Broker
    Trust, a.s. has run it since March 2001 as in-house tooling for its own broker network, so
    an intermediary outside that network cannot buy it at any price.'
sources:
- type: arbitrage
  name: "Saturn"
  gist: "the 600-firm London template"
  why: "London's compliance operating system for wealth managers (YC S24) — KYC, suitability and regulatory reporting, on the platform of 600+ UK advisory firms."
  url: https://www.ycombinator.com/companies/saturn
  note: 'yc-saturn: Saturn (YC S24, London, ~18 people) builds compliance and back-office
    workflow software for wealth managers — KYC, suitability, regulatory reporting. UK-based,
    so scored as one analog outside the DE/AT/PL/Nordics band.'
  date: '2026-08-13'
  signal: yc-saturn
- type: regulation
  name: "EU AML Regulation 2024/1624"
  gist: "the 10 July 2027 rulebook"
  why: "Applies directly from 10 July 2027, replacing much of the Czech AML regime with one harmonised rulebook under the new AMLA supervisor — every firm in scope needs a policy rewrite before then."
  url: https://eur-lex.europa.eu/eli/reg/2024/1624/oj
  note: 'reg-amlr-single-rulebook: EU AML Regulation 2024/1624 applies 10 Jul 2027 (verified
    on EUR-Lex, Art 90), directly replacing much of the Czech AML Act regime — harmonised
    CDD, beneficial-ownership and internal-policy requirements, new obliged entities, AMLA
    supervision. Deadline <18 months.'
  date: '2027-07-10'
  signal: reg-amlr-single-rulebook
- type: gap-check
  name: "First Czech market scan"
  gist: "the superseded first sweep"
  why: "An early sweep that found only law firms and compliance consultancies selling services, and documented compliance run on Word templates under growing ČNB and MiFID II paperwork."
  url: https://www.ycombinator.com/companies/saturn
  note: 'Absence check 2026-08-13: only law firms and compliance consultancies (Comply, aCompliance)
    — services, no product. Demand point: signal documents compliance done via consultants
    and Word templates under growing ČNB/MiFID II paperwork plus DORA load from 2025.'
  date: '2026-08-13'
- type: gap-check
  name: "AML Proof"
  gist: "the first Czech entrant"
  why: "A Czech cloud AML platform sold self-serve from 25 CZK a credit to the very buyer this record names — client screening, beneficial owners, internal policies and FAÚ reporting. The MiFID II half of the stack is still empty."
  url: https://amlproof.ai/cs/aml-software
  note: 'Gap re-check 2026-08-20: OCCUPIED on the AML side. Looked for a Czech regtech SaaS
    selling AMLR-ready KYC, beneficial-owner verification, internal policies and reporting
    to investment intermediaries and advisers, plus a MiFID II suitability/reporting product.
    Found AML Proof, s.r.o. (IČO 23791497, Kaprova 42/14, Praha 1, confirmed in ARES) selling
    a cloud AML platform to povinné osoby it names as finanční poradci and zprostředkovatelé:
    client identification, PEP and sanctions screening, UBO verification, risk scoring and
    EDD, systém vnitřních zásad, FAÚ reporting, 10-year archival and audit trails, self-serve
    from 25 CZK per credit with the internal-policy module free. Alongside it, AML solutions
    s.r.o. and AML Basic sell sanctions/PEP screening to obliged entities, and our own funded
    ledger carries Resistant AI (Prague, round-resistant-ai, USD 25M Series B Oct 2025) selling
    document-fraud and financial-crime detection to banks and fintechs. NOT found: any Czech
    product for the MiFID II half — suitability questionnaires, product-governance records,
    vázaný-zástupce oversight, ČNB reporting; the nearest thing is broker-pool software
    (Broker Trust: Bety 2.0, BT Invest, methodology base) built for one network rather than
    sold as compliance SaaS. Verdict: the record claim "no Czech regtech SaaS for this segment,
    services only" does not survive. De-rank rule applied: gap 0 with incumbent named, status
    watching. Positive control passed before this negative was trusted (see the correction).'
  date: '2026-08-20'
  queries:
    - "software pro investiční zprostředkovatele compliance ČNB reporting vázaní zástupci"
    - "AML software Česko KYC compliance finanční instituce regtech"
    - "AML software česká firma identifikace klienta lustrace PEP sankční seznamy"
    - "Broker Trust eBroker software pro poradce investiční zprostředkovatel systém"
    - "český software investiční dotazník vhodnost MiFID II záznam z jednání poradce compliance"
    - "AML Proof software finanční poradci investiční zprostředkovatelé povinné osoby cena"
  checked: [google-cz, ares, own-funded-ledger]
  expires: '2026-11-18'
- type: price
  url: https://amlproof.ai/cs/pricing
  name: "AML Proof — self-serve from 25 CZK"
  gist: "from 25 CZK a check"
  why: "The lower bound of what a Czech investment intermediary pays AML Proof for one client check: from 25 CZK a credit, with the internal-policy module free."
  note: 'Price receipt lifted from the 2026-08-20 gap re-check already on this ledger, which
    read amlproof.ai: self-serve from 25 CZK per credit with the systém vnitřních zásad module
    free. A credit is consumed per client check, so the unit is per-case. "From" is a lower
    bound and why says so. dims omitted: backs no score.
    Verified 2026-09-04: the amlproof.ai Ceník page still states Kredity od 25 Kč za kus
    (balíček 1 000), the 25 CZK being the 1,000-credit tier, while the default 10-credit
    package on the same page shows 90 Kč per credit.'
  date: '2026-08-20'
  payer: 'A Czech investment intermediary or financial adviser'
  amount_czk: 25
  unit: per-case
  basis: list-price
created: '2026-08-13'
updated: '2026-09-04'
---

Thousands of Czech investment intermediaries, their tied agents and the networks they sell through — Broker Consulting, Partners, independents — answer to ČNB (the Czech central bank) [S1,S3]. The paperwork keeps growing: suitability tests, client identity checks, regulatory reporting under MiFID II — the EU rulebook for investment services [S1,S3]. They run it on Word templates and outside consultants, not software [S1].

Why now: the EU's anti-money-laundering regulation 2024/1624 applies directly from 10 July 2027, replacing most of Czech act 253/2008 with one rulebook under AMLA — a new EU supervisor [S2]. Every firm in scope redoes its client due diligence, beneficial-owner verification and internal policies before that date [S2]. Crowdfunding, most crypto services and luxury-goods traders enter scope for the first time [S2].

Who pays: the advisory networks and mid-sized firms first, where one subscription spreads across hundreds of tied agents and a licence rides on the paperwork. Independents follow through the networks. The regulation names the product: beneficial-owner verification APIs and reporting built to the new rulebook [S2].

Existing non-solutions: Comply, aCompliance and the law firms sell one-off reviews; internal policies still get written in Word [S3]. AML Proof (Praha 1, IČO 23791497) sells a Czech cloud platform to the firms the law obliges, named as financial advisers and intermediaries: client identification, sanctions and politically-exposed-person screening, beneficial-owner verification, risk scoring, internal policies, reporting to FAÚ — the financial intelligence unit — and ten-year archiving, self-serve from 25 CZK a credit [S4]. AML solutions s.r.o. and AML Basic sell screening beside it; Resistant AI (Prague, USD 25M Series B) sells document-fraud detection to banks and fintechs [S4]. AML Proof, s.r.o. was incorporated in October 2025 [S4] — a first entrant, not a settled incumbent. Nothing Czech covers the MiFID II half: suitability questionnaires, the record of the advice meeting, product-governance records, tied-agent oversight, ČNB reporting [S4]. The nearest is Broker Trust's advisor stack, built for one network rather than sold [S4].

Solved elsewhere: three funded firms sell this abroad, none in Central Europe. Saturn (YC S24, London) runs a compliance system for wealth managers across 600+ British advisory firms [S1]. Muinmos (Denmark) sells regulatory onboarding to banks and investment firms; Apiax (Switzerland) turns compliance rules into machine-readable checks.

## First moves

1. Sell to the networks, not the independents. Broker Consulting, Partners and their peers each carry hundreds of tied agents, and the network's compliance officer is the one who can spread a subscription across all of them [S1,S3]. Saturn sells that way in Britain: the firm buys, its advisers use it [S1].
2. Build the MiFID II half. Plug into the anti-money-laundering half rather than rebuild it: AML Proof already sells client identification, sanctions and politically-exposed-person screening, beneficial-owner verification, internal policies and reporting to the financial intelligence unit, from 25 CZK a credit [S4]. Nobody sells the suitability questionnaire, the record of the advice meeting, product-governance records, tied-agent oversight or central-bank reporting [S4].
3. Open with the date. The rulebook applies from 10 July 2027, and every firm in scope rewrites its client due diligence and internal policies before then [S2]. Ask what they plan to do. Today the answer is a consultant and a Word template [S1,S3].
4. Watch Broker Trust. It has run the Bety 2.0 and BT Invest platform for its own tied advisers since March 2001 — the closest thing on the market to what is missing, and no intermediary outside that network can buy it at any price [S4]. The day it goes on sale, this opening closes.

## Revisions

2026-08-25 · locals ledger — The AML solutions s.r.o. entry is not carried in `locals[]`: no product URL for it exists on this record or anywhere in the signal corpus, and the field requires one. Inventing a plausible domain would be exactly the failure this register is built against, so the company stays named in the argument prose with its [S4] receipt instead. It is early either way and carries no part of the gap score.

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-20 · de-rank and gap re-check — Two blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The absence claim was never checked against a Czech surface — the 2026-08-13 gap check cites a Y Combinator page for a London company as the receipt for a Czech absence, which proves nothing about Czechia. Re-run in Czech against google-cz, ARES and our own funded ledger, it fails: AML Proof, s.r.o. sells the AMLR-shaped product this record calls missing, to the buyer this record names, self-serve [S4]. Gap 1 → 0, score 6 → 5, status candidate → watching. Method control, run before the negative half was trusted: the same method was applied at Wultra (p-0017) and Softlink (p-0026) — the ledger grep returned round-wultra and cz-ringil, and a purely descriptive Czech query ("software platforma dálkové odečty vodoměrů vodárny Česko dodavatel") surfaced softlink.cz unprompted, so the method demonstrably produces positives. One sensitivity limit is recorded honestly: a narrow product-shaped Czech query for Wultra's wallet gateway did not surface Wultra, so a single query shape is not evidence of absence, and six were run here. The title clause "armed only with Word templates and consultants" was argued both ways inside the same block — left standing as receipted by [S1], which describes how firms operate rather than what they can buy, then cut because AML Proof is sold as software and the clause asserted what the ledger refutes. The title as it now stands does not carry the clause. What the AMLR deadline still does is land on every firm in the segment in July 2027 [S2], and the MiFID II suitability and reporting surface still has no Czech product on it [S4], so residual room exists downstream of AML Proof. What the register can no longer claim is that the segment has no Czech regtech SaaS.

2026-08-24 · fact check — Cut "and, since 2025, DORA obligations" from the lead. DORA does not apply to investiční zprostředkovatelé: they operate under the MiFID II Article 3 national regime, which is excluded from DORA's scope (verified against Czech legal commentary on DORA's reach, 2026-08-24). The claim came from the yc-saturn harvest note ("DORA adds load from 2025") with nothing behind it — asserting an EU regulation onto a segment it exempts is the error class this register exists to avoid. MiFID II paperwork claims stand [S1,S3]; the AML Proof incumbent receipt re-verified live (amlproof.ai, HTTP 200) [S4]. Scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries AML Proof and AML solutions, both early [S4]. AML Proof, s.r.o. was incorporated on 1 October 2025 — under a year of selling — and AML solutions cites no limb the test reads. An early local player does not close a space, so `scores.gap` 0 → 1: the 2026-08-20 de-rank was right that the AML half is no longer unbuilt, but wrong to score the field as taken on an entrant younger than the record. Resistant AI is deliberately not in `locals[]` — it sells document-fraud detection to banks and fintechs, a different product to a different buyer — and stays named in the body. `scores.proof` 1 → 2: Saturn and Apiax both pass the established test, but Britain and Switzerland are not CEE-adjacent, so rung 3 is not met. `score` 5 → 7. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and three players are restored — every one of them reversing an exclusion recorded above. **AML solutions** returns: the `locals ledger` entry above dropped it because the schema then demanded a `url` and none exists anywhere in the corpus, and `url` is now optional where an `ico` is present. It is carried on **IČO 10691766** (ARES-dated March 2021) and the page links ARES rather than a guessed domain. It stays `competes: direct` and early. **Resistant AI** joins as `competes: adjacent`, reversing the decision above to keep it out: what it sells — document-fraud and financial-crime detection to banks and fintechs — is now sayable on the ledger instead of being the reason to omit it. Resistant AI s.r.o. (IČO 07825439, ARES-dated January 2019) passes the established test on its October 2025 Series B, and it too is carried on its IČO because no product URL for it is on file. **Broker Trust** joins as `competes: adjacent` and early, because it is the nearest thing on the market to the MiFID II half this record calls missing and a builder should know why it does not close it: the Bety 2.0 and BT Invest stack is in-house tooling for one broker network, not a product an intermediary outside that network can buy at any price. AML Proof converts to `competes: direct`, unchanged at early. `scores.gap` stays 1: both direct players are early, and the two adjacent entries never touch the number. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the Resistant AI entry: the explanation that it is filed against its IČO because no product URL is on file. That is how the row was built, not what a builder needs from it. Same pass: `## First moves` written for the first time. The template reserves the section for records scoring 7 or more and this record reached 7 in the pass above without gaining one. Four moves, all off receipts already here — the networks named in the lead [S1,S3], the AML half AML Proof already sells and the MiFID II half nobody does [S4], the 10 July 2027 application date [S2], and Broker Trust's in-house-only stack [S4]. No new claim was introduced and no score moved.

2026-09-02 · plain-language pass — Ten acronyms handled at first use: ČNB, MiFID II, AMLA and FAÚ glossed; AML, KYC, CDD, UBO, PEP and AMLR replaced with plain words, plus six Czech terms. Argument 412 → 368 words, every [Sn] marker, figure, date, IČO and named firm kept; Muinmos, Apiax and Saturn's 600+ British firms now named in Solved elsewhere. First moves rewritten verbs-first; a gist added to all four sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The self-serve price already read in the 2026-08-20 sweep is now recorded as a price of its own: from 25 CZK a client check [S5]. No score, status, note or marker touched.
