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
  status: early
  evidence: 'a Czech cloud AML platform sold to the povinné osoby it names as finanční poradci
    and zprostředkovatelé — client identification, PEP and sanctions screening, beneficial-owner
    verification, risk scoring, a systém vnitřních zásad, FAÚ reporting and ten-year archival,
    self-serve from 25 CZK a credit. AML Proof, s.r.o. was incorporated on 1 October 2025, so
    it has been selling for under a year.'
sources:
- type: arbitrage
  name: "Saturn"
  why: "London's compliance operating system for wealth managers (YC S24) — KYC, suitability and regulatory reporting, on the platform of 600+ UK advisory firms."
  url: https://www.ycombinator.com/companies/saturn
  note: 'yc-saturn: Saturn (YC S24, London, ~18 people) builds compliance and back-office
    workflow software for wealth managers — KYC, suitability, regulatory reporting. UK-based,
    so scored as one analog outside the DE/AT/PL/Nordics band.'
  date: '2026-08-13'
  signal: yc-saturn
- type: regulation
  name: "EU AML Regulation 2024/1624"
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
  why: "An early sweep that found only law firms and compliance consultancies selling services, and documented compliance run on Word templates under growing ČNB and MiFID II paperwork."
  url: https://www.ycombinator.com/companies/saturn
  note: 'Absence check 2026-08-13: only law firms and compliance consultancies (Comply, aCompliance)
    — services, no product. Demand point: signal documents compliance done via consultants
    and Word templates under growing ČNB/MiFID II paperwork plus DORA load from 2025.'
  date: '2026-08-13'
- type: gap-check
  name: "AML Proof"
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
created: '2026-08-13'
updated: '2026-08-25'
---

Thousands of Czech vázaní zástupci, investiční zprostředkovatelé and advisory networks (Broker Consulting and Partners ecosystems plus independents) operate under ČNB supervision with steadily growing MiFID II paperwork — suitability, KYC, regulatory reporting [S1,S3]. The evidence on file shows this compliance run on Word templates and external consultants, not software [S1].

Why now: the EU AML Regulation (2024/1624) applies directly from 10 July 2027, replacing much of the regime built on zákon 253/2008 with a harmonised single rulebook under the new AMLA supervisor — CDD, beneficial-ownership verification and internal policies all need rework, and new obliged entities (crowdfunding, most crypto services, luxury goods traders) enter scope [S2]. Every firm in the segment faces a gap analysis and policy rewrite before that date [S2].

Who pays: the intermediary networks and mid-sized firms first — they have revenue at stake in license compliance and can amortize a SaaS subscription across hundreds of agents; smaller independents follow via the networks. UBO-verification APIs and AMLR-ready reporting are concrete product surfaces named in the reg signal [S2].

Existing non-solutions and the first entrant: compliance consultancies (Comply, aCompliance) and law firms still sell one-off gap analyses, and internal policies still get written in Word [S3] — but the AML half of the stack is no longer unbuilt. AML Proof, s.r.o. (Praha 1, IČO 23791497) sells a Czech cloud AML platform to the obliged entities it names as finanční poradci and zprostředkovatelé: client identification, PEP and sanctions screening, beneficial-owner verification, risk scoring, a systém vnitřních zásad, FAÚ reporting and ten-year archival, self-serve from 25 CZK per credit [S4]. AML solutions s.r.o. and AML Basic sell sanctions and PEP screening beside it, and Resistant AI (Prague, USD 25M Series B) sells document-fraud and financial-crime detection to banks and fintechs [S4]. AML Proof itself was incorporated in October 2025 [S4] — a first entrant on the AML side rather than a settled incumbent, so the half of the stack it covers is contested rather than closed. What the search did not find is a Czech product for the MiFID II half — suitability questionnaires, product-governance records, vázaný-zástupce oversight and ČNB reporting; the closest is broker-pool software such as Broker Trust's advisor stack, built for one network rather than sold as compliance SaaS [S4].

Solved elsewhere: Saturn (YC S24, London) sells a compliance operating system to wealth managers, showing the productized model works for this buyer [S1]. The analog sits far from the region; the deadline and documented paperwork pressure do the heavy lifting here.

## Revisions

2026-08-25 · locals ledger — The AML solutions s.r.o. entry is not carried in `locals[]`: no product URL for it exists on this record or anywhere in the signal corpus, and the field requires one. Inventing a plausible domain would be exactly the failure this register is built against, so the company stays named in the argument prose with its [S4] receipt instead. It is early either way and carries no part of the gap score.

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-20 · de-rank and gap re-check — Two blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The absence claim was never checked against a Czech surface — the 2026-08-13 gap check cites a Y Combinator page for a London company as the receipt for a Czech absence, which proves nothing about Czechia. Re-run in Czech against google-cz, ARES and our own funded ledger, it fails: AML Proof, s.r.o. sells the AMLR-shaped product this record calls missing, to the buyer this record names, self-serve [S4]. Gap 1 → 0, score 6 → 5, status candidate → watching. Method control, run before the negative half was trusted: the same method was applied at Wultra (p-0017) and Softlink (p-0026) — the ledger grep returned round-wultra and cz-ringil, and a purely descriptive Czech query ("software platforma dálkové odečty vodoměrů vodárny Česko dodavatel") surfaced softlink.cz unprompted, so the method demonstrably produces positives. One sensitivity limit is recorded honestly: a narrow product-shaped Czech query for Wultra's wallet gateway did not surface Wultra, so a single query shape is not evidence of absence, and six were run here. The title clause "armed only with Word templates and consultants" was argued both ways inside the same block — left standing as receipted by [S1], which describes how firms operate rather than what they can buy, then cut because AML Proof is sold as software and the clause asserted what the ledger refutes. The title as it now stands does not carry the clause. What the AMLR deadline still does is land on every firm in the segment in July 2027 [S2], and the MiFID II suitability and reporting surface still has no Czech product on it [S4], so residual room exists downstream of AML Proof. What the register can no longer claim is that the segment has no Czech regtech SaaS.

2026-08-24 · fact check — Cut "and, since 2025, DORA obligations" from the lead. DORA does not apply to investiční zprostředkovatelé: they operate under the MiFID II Article 3 national regime, which is excluded from DORA's scope (verified against Czech legal commentary on DORA's reach, 2026-08-24). The claim came from the yc-saturn harvest note ("DORA adds load from 2025") with nothing behind it — asserting an EU regulation onto a segment it exempts is the error class this register exists to avoid. MiFID II paperwork claims stand [S1,S3]; the AML Proof incumbent receipt re-verified live (amlproof.ai, HTTP 200) [S4]. Scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries AML Proof and AML solutions, both early [S4]. AML Proof, s.r.o. was incorporated on 1 October 2025 — under a year of selling — and AML solutions cites no limb the test reads. An early local player does not close a space, so `scores.gap` 0 → 1: the 2026-08-20 de-rank was right that the AML half is no longer unbuilt, but wrong to score the field as taken on an entrant younger than the record. Resistant AI is deliberately not in `locals[]` — it sells document-fraud detection to banks and fintechs, a different product to a different buyer — and stays named in the body. `scores.proof` 1 → 2: Saturn and Apiax both pass the established test, but Britain and Switzerland are not CEE-adjacent, so rung 3 is not met. `score` 5 → 7.
