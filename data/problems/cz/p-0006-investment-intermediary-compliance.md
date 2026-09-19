---
id: p-0006
region: cz
title: 'A new EU anti-money-laundering law hits Czech investment advisers in under 10 months'
brief: 'From July 2027, an EU rulebook replaces much of Czech anti-money-laundering law, so firms it covers must update client checks and policies [S2,S4]. That comes on top of the central bank''s paperwork [S1,S3].'
solution: 'Build compliance software for advice networks that records why an investment suits each client and files central-bank reports.'
good_for: 'Someone who''d like to work with financial advisers and their compliance officers.'
category: fintech
geo: CZ-national
score: 6
scores:
  proof: 2
  money: 0
  urgency: 2
  demand: 1
  gap: 1
status: candidate
entry:
  level: moderate
  buyer: large-firms
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: the seller needs no central-bank licence, a network buys for all its tied agents at once, and a fixed EU date pushes firms to act. Harder: a Czech anti-money-laundering platform already sells client checks to these firms, so a newcomer must connect to it or beat it; and the buyers are large networks.'
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
  why: "A Czech cloud AML platform sold self-serve from 25 CZK a credit to investment intermediaries and financial advisers — client screening, beneficial owners, internal policies and FAÚ reporting. The MiFID II half of the stack is still empty."
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
    package on the same page shows 90 Kč per credit.
    Rescored 2026-09-19: left untagged on purpose. It prices the anti-money-laundering half,
    which the solution connects to rather than rebuilds, so it is not this job and earns no
    Willing to pay point.'
  date: '2026-08-20'
  payer: 'A Czech investment intermediary or financial adviser'
  amount_czk: 25
  unit: per-case
  basis: list-price
created: '2026-08-13'
updated: '2026-09-19'
---

Czech investment intermediaries and their tied agents answer to the central bank for a growing pile of compliance paperwork [S1,S3].

- The paperwork covers suitability tests, client identity checks and regulatory reporting [S1,S3].
- Big advice networks such as Broker Consulting and Partners work beside independent advisers [S1].
- Thousands of tied agents and intermediaries work in this market [S1].

The supervisor is ČNB (the Czech National Bank), and much of the paperwork comes from MiFID II — the EU rulebook for investment services [S1,S3]. A tied agent sells investments on behalf of one licensed firm. A suitability test records why an investment suits the client it is sold to.

Existing non-solutions: Consultants sell compliance as a service, and Czech software covers only the anti-money-laundering half, not the investment-advice half [S3,S4].

Compliance consultancies and law firms sell services rather than a product, and internal policies still get written in Word [S3].

- A Czech cloud platform, selling since October 2025, offers anti-money-laundering checks to the advisers and intermediaries the law obliges [S4]. It is a first entrant, not a settled incumbent [S4].
- A second Czech firm screens clients against sanctions lists and lists of politically exposed people for the same firms, and AML Basic — another screening service — sells it too [S4].
- A funded Prague company sells document-fraud and financial-crime detection to banks and fintechs, a different job for a different buyer [S4].
- Nothing Czech covers the investment-advice half: suitability questionnaires, notes from the advice meeting, product-governance records, tied-agent oversight and central-bank reporting [S4].
- The nearest is one broker network's platform for its own tied advisers, which no firm outside that network can buy [S4].

Why now: Investment advisers the anti-money-laundering law covers must redo client checks and internal policies before an EU rulebook applies in July 2027 [S2,S4].

- Each covered firm has under 10 months to rewrite its internal policies [S2].
- The rewrite lands on top of central-bank paperwork that keeps growing [S1,S3].
- Firms still pay consultants and fill in Word templates to keep up [S3].

The dates behind this:

- On 10 July 2027 EU Regulation 2024/1624 applies directly and replaces much of the Czech anti-money-laundering act, No. 253/2008 [S2].
- From that date one rulebook sets client checks, beneficial-owner checks and internal policies across the EU, under AMLA — the EU's new anti-money-laundering authority [S2].
- From that date crowdfunding platforms, most crypto services and luxury-goods traders come under the rules for the first time [S2].

Who pays: Firms pay compliance consultants and law firms today, but no price for the investment-advice half is on file [S3,S4].

- Consultancies such as Comply and aCompliance sell compliance work as a service [S3].
- Law firms sell the same kind of compliance work [S3].
- A Czech platform sells anti-money-laundering checks per client, not the advice half [S4].

The likely first buyers are the advice networks and mid-sized firms, where one subscription can cover many tied agents and the firm's licence depends on its paperwork. Independent advisers would follow through the networks.

The new rulebook creates demand for tools that check who really owns a client company, and for reporting built to the rulebook [S2]. No price, public contract or grant for the investment-advice half is on file.

Solved elsewhere: Compliance software for wealth managers already sells abroad, one product on the platform of over 600 British advisory firms [S1].

It comes from a London start-up of about 18 people, from the summer 2024 intake of Y Combinator, a US programme that funds start-ups [S1]. It automates client identity checks, suitability and regulatory reporting for wealth managers, and the advisory firm buys it for its advisers [S1].

The three sellers listed here are based in Britain, Denmark and Switzerland, and none is based in Central Europe.

## First moves

1. Build software for the investment-advice half of compliance: the suitability questionnaire, notes from each advice meeting, tied-agent oversight and central-bank reports. No Czech product sells that half yet, while the anti-money-laundering half already has Czech sellers; see [Market gap](#competition). Connect to their client checks, screening and reporting rather than rebuild them, so a firm keeps what it already uses. Start with the suitability questionnaire, which records why an investment suits each client.
2. Contact the compliance officers of the big advice networks, such as Broker Consulting and Partners, and show them the suitability tool. One network's compliance officer can put all its tied agents on one subscription, where an independent adviser buys only for itself; see [Willing to pay](#willing-to-pay). That is how the London start-up sells in Britain: the firm buys, and its advisers use it; see [Validated abroad](#validated-abroad).
3. Open each conversation with the date the EU anti-money-laundering rulebook applies, and ask the firm what it plans to do before then. Every covered firm has to rewrite its client checks and internal policies by that date; see [Why now](#why-now). Today the answer is a consultant and a Word template, so offer the software that replaces both.
4. Watch the one broker network that runs this paperwork on its own platform, because if it starts selling it, this opening closes. Its platform has run for years inside that one network and is the closest thing on the market to what is missing, but no outside firm can buy it today; see [Market gap](#competition).

## Revisions

2026-08-25 · locals ledger — The AML solutions s.r.o. entry is not carried in `locals[]`: no product URL for it exists on this record or anywhere in the signal corpus, and the field requires one. Inventing a plausible domain would be exactly the failure this register is built against, so the company stays named in the argument prose with its [S4] receipt instead. It is early either way and carries no part of the gap score.

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-20 · de-rank and gap re-check — Two blocks recorded on this date, merged here; the de-rank was written down twice and is stated once. The absence claim was never checked against a Czech surface — the 2026-08-13 gap check cites a Y Combinator page for a London company as the receipt for a Czech absence, which proves nothing about Czechia. Re-run in Czech against google-cz, ARES and our own funded ledger, it fails: AML Proof, s.r.o. sells the AMLR-shaped product this record calls missing, to the buyer this record names, self-serve [S4]. Gap 1 → 0, score 6 → 5, status candidate → watching. Method control, run before the negative half was trusted: the same method was applied at Wultra (p-0017) and Softlink (p-0026) — the ledger grep returned round-wultra and cz-ringil, and a purely descriptive Czech query ("software platforma dálkové odečty vodoměrů vodárny Česko dodavatel") surfaced softlink.cz unprompted, so the method demonstrably produces positives. One sensitivity limit is recorded honestly: a narrow product-shaped Czech query for Wultra's wallet gateway did not surface Wultra, so a single query shape is not evidence of absence, and six were run here. The title clause "armed only with Word templates and consultants" was argued both ways inside the same block — left standing as receipted by [S1], which describes how firms operate rather than what they can buy, then cut because AML Proof is sold as software and the clause asserted what the ledger refutes. The title as it now stands does not carry the clause. What the AMLR deadline still does is land on every firm in the segment in July 2027 [S2], and the MiFID II suitability and reporting surface still has no Czech product on it [S4], so residual room exists downstream of AML Proof. What the register can no longer claim is that the segment has no Czech regtech SaaS.

2026-08-24 · fact check — Cut "and, since 2025, DORA obligations" from the lead. DORA does not apply to investiční zprostředkovatelé: they operate under the MiFID II Article 3 national regime, which is excluded from DORA's scope (verified against Czech legal commentary on DORA's reach, 2026-08-24). The claim came from the yc-saturn harvest note ("DORA adds load from 2025") with nothing behind it — asserting an EU regulation onto a segment it exempts is the error class this register exists to avoid. MiFID II paperwork claims stand [S1,S3]; the AML Proof incumbent receipt re-verified live (amlproof.ai, HTTP 200) [S4]. Scores untouched.

2026-08-25 · plain-language pass — Added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md, where PROOF and GAP both turn on whether a player is established or early rather than on whether one exists. `locals[]` carries AML Proof and AML solutions, both early [S4]. AML Proof, s.r.o. was incorporated on 1 October 2025 — under a year of selling — and AML solutions cites no limb the test reads. An early local player does not close a space, so `scores.gap` 0 → 1: the 2026-08-20 de-rank was right that the AML half is no longer unbuilt, but wrong to score the field as taken on an entrant younger than the record. Resistant AI is deliberately not in `locals[]` — it sells document-fraud detection to banks and fintechs, a different product to a different buyer — and stays named in the body. `scores.proof` 1 → 2: Saturn and Apiax both pass the established test, but Britain and Switzerland are not CEE-adjacent, so rung 3 is not met. `score` 5 → 7. Fifth pass this date, merged here: `locals[]` converted from `status:` to `competes:` + `maturity:`, and three players are restored — every one of them reversing an exclusion recorded above. **AML solutions** returns: the `locals ledger` entry above dropped it because the schema then demanded a `url` and none exists anywhere in the corpus, and `url` is now optional where an `ico` is present. It is carried on **IČO 10691766** (ARES-dated March 2021) and the page links ARES rather than a guessed domain. It stays `competes: direct` and early. **Resistant AI** joins as `competes: adjacent`, reversing the decision above to keep it out: what it sells — document-fraud and financial-crime detection to banks and fintechs — is now sayable on the ledger instead of being the reason to omit it. Resistant AI s.r.o. (IČO 07825439, ARES-dated January 2019) passes the established test on its October 2025 Series B, and it too is carried on its IČO because no product URL for it is on file. **Broker Trust** joins as `competes: adjacent` and early, because it is the nearest thing on the market to the MiFID II half this record calls missing and a builder should know why it does not close it: the Bety 2.0 and BT Invest stack is in-house tooling for one broker network, not a product an intermediary outside that network can buy at any price. AML Proof converts to `competes: direct`, unchanged at early. `scores.gap` stays 1: both direct players are early, and the two adjacent entries never touch the number. Same date, ledger-language pass, merged here: every `locals[]` evidence line was rewritten for the builder it renders to. Those lines print under each entry on the public page, and they were still written in the vocabulary of the scoring rubric — "no limb of the established test is on file", "which is the limb it passes" — which tells a reader deciding what to build precisely nothing. Each line now states what the company sells and what is genuinely unknown about it ("names nobody who has bought it" rather than "no limb is met"), ARES dating is stated as plain trading history, and the contract lookup is named as the state contracts register rather than by its file path. Every date, IČO, price, customer count, funding figure and named buyer is carried across unchanged; no `sources[].note` was touched, no [Sn] marker moved and no score changed. Also cut from the Resistant AI entry: the explanation that it is filed against its IČO because no product URL is on file. That is how the row was built, not what a builder needs from it. Same pass: `## First moves` written for the first time. The template reserves the section for records scoring 7 or more and this record reached 7 in the pass above without gaining one. Four moves, all off receipts already here — the networks named in the lead [S1,S3], the AML half AML Proof already sells and the MiFID II half nobody does [S4], the 10 July 2027 application date [S2], and Broker Trust's in-house-only stack [S4]. No new claim was introduced and no score moved.

2026-09-02 · plain-language pass — Ten acronyms handled at first use: ČNB, MiFID II, AMLA and FAÚ glossed; AML, KYC, CDD, UBO, PEP and AMLR replaced with plain words, plus six Czech terms. Argument 412 → 368 words, every [Sn] marker, figure, date, IČO and named firm kept; Muinmos, Apiax and Saturn's 600+ British firms now named in Solved elsewhere. First moves rewritten verbs-first; a gist added to all four sources. No score, status, note or marker touched.

2026-09-04 · price receipt — The self-serve price already read in the 2026-08-20 sweep is now recorded as a price of its own: from 25 CZK a client check [S5]. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` on who is stuck and what is happening, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Thousands of Czech investment intermediaries and advisors face growing ČNB/MiFID paperwork today and a directly applicable EU AML rulebook from July 2027". Previous solution, verbatim: "Compliance software for investment-advice firms covering the half nobody sells here yet: client-suitability paperwork, tied-agent oversight and the reporting the Czech central bank requires." The record carried no brief and no good_for before this pass. Every claim was checked against this record's sources first. 10 July 2027 is the application date verified on EUR-Lex, under 10 months from this pass [S2]. "Replaces much of" follows the source's own wording rather than the body's "most" [S2]. That the rulebook reaches advisers rests on today's Czech regime, under which a Czech anti-money-laundering platform sells to financial advisers and intermediaries as firms the law obliges [S4]. The old title's "thousands" of intermediaries and the "Word templates" rest only on the harvest note behind [S1], so neither is repeated. The headline's urgency is the anti-money-laundering date, while the suggested product is the suitability and reporting half no Czech product covers [S4], because the anti-money-laundering half already has a Czech entrant [S4]. No score, status, source, note, marker or body sentence changed. Simplified for the front page: title "Czech investment advisers have under 10 months before a new EU anti-money-laundering law applies" → "A new EU anti-money-laundering law hits Czech investment advisers in under 10 months"; brief "From 10 July 2027 one EU rulebook replaces much of Czech anti-money-laundering law, so covered firms must update client checks and internal policies [S2,S4]. That comes on top of the investment-advice paperwork the central bank already requires [S1,S3]." → "From July 2027, an EU rulebook replaces much of Czech anti-money-laundering law, so firms it covers must update client checks and policies [S2,S4]. That comes on top of the central bank's paperwork [S1,S3]."; solution "Build compliance software for advice networks that records why an investment suits each client and files central-bank reports, as companies already do in Britain." → "Build compliance software for advice networks that records why an investment suits each client and files central-bank reports.". "Under 10 months" is unchanged from the old headline [S2]; "covered firms" became "firms it covers"; the exact day 10 July and "as companies already do in Britain" were cut.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the central-bank paperwork, with its contents, the advice networks and the "thousands" of tied agents and intermediaries as its items, and ČNB, MiFID II, tied agent and suitability test explained in the detail [S1,S3]. Competition opens on consultants plus Czech software that covers only the anti-money-laundering half, and describes AML Proof, AML solutions, Resistant AI and Broker Trust by what each sells, leaving their names, IČOs, prices, funding and dates to their `locals[]` rows [S3,S4]; AML Basic, not on the ledger, stays named. Why now opens on the covered advisers who must redo client checks and policies before July 2027, with the under-10-months window, the growing central-bank paperwork and the consultants and Word templates as its items, and the regulation's dates below as plain bullets [S1,S2,S3]. Willing to pay answers that firms pay consultants and law firms today and a Czech platform sells checks per client, with Comply and aCompliance, not on the ledger, named there [S3,S4]; the 25 CZK price stays in its receipt [S5]. Validated abroad lost the ledger names Saturn, Muinmos and Apiax for a description of the London product [S1], with the other two left to their `comps[]` rows. The moves lost every [Sn] marker, figure and ledger name for links; move 1 now builds the investment-advice half (it was move 2), and the old "Sell to the networks" is move 2 and now contacts the networks' compliance officers. The move-only facts already had homes: the AML Proof feature list and price in its row and receipt [S4,S5], Broker Trust's platforms and March 2001 start in its row [S4], and the 10 July 2027 date under Why now [S2]. `entry.why` was rewritten as "Easier: … Harder: …" and no longer names Resistant AI, whose row carries it. S4.why no longer says "the very buyer this record names". Process block: none added. No source on file says who fills in the suitability questionnaire, oversees the tied agents or files the central-bank reports today; S3 records only that consultants and Word templates are used, so there is no documented step to draw. Corrected against the sources rather than against the old sentences: "replacing most of Czech act 253/2008" became "much of", the source's own wording, as the 2026-09-16 entry had already done for the brief [S2]; "The regulation names the product: beneficial-owner verification APIs and reporting" was wrong, since the regulation names no product and the signal behind S2 says only that it creates demand for such tooling, and the body now says that [S2]; "Comply, aCompliance and the law firms sell one-off reviews" became "services rather than a product", which is what S3 records; "They run it on Word templates and outside consultants" is now cited to S3, which records it, rather than S1 alone; "three funded firms sell this abroad, none in Central Europe" dropped "funded", because Muinmos's row says its raise is undisclosed, and now says none is BASED in Central Europe, because the same row says Muinmos sells globally; and "hundreds of tied agents" per network, in Who pays, move 1 and `entry.why`, is in no source, so each now says "many" or "all its" tied agents. Flagged as inference: that the advice networks and mid-sized firms are the likely first buyers, that a firm's licence depends on its paperwork and that independents would follow through the networks (Who pays, unsourced before and still our reading); that the British advisory firms buy the London product for their advisers, which rests on S1 counting the firms on its platform; and that "thousands" of tied agents and intermediaries rests only on the harvest note behind S1, as the 2026-09-16 entry already recorded. No score, status, source, `note:`, `sources[]` order, entry level, title, brief, solution or good_for changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 3 → 2; Willing to pay stays 0; score 7 → 6, still FAIR. Why now: the old 3 was a deadline part of 2 plus the retired freshness point. EU Regulation 2024/1624 [S2] passes REAL, as an EU regulation that applies directly and binds the firms the anti-money-laundering law covers, advisers and intermediaries among them [S4], and CLOSE, applying on 10 July 2027, inside 18 months. It fails TEETH: no source on file names a fine or other sanction on these firms for missing it. Rung 2. Carried over from the worksheet as an open judgement call, not settled here: the rule forces the anti-money-laundering half, while the solution sells the investment-advice half, so whether this deadline forces this product is a reading, not a receipt. Willing to pay, tagging pass first: every source on file was read for someone paying for this exact job, software for suitability records, tied-agent oversight and central-bank reports, or that work bought in. None names an amount. The one price on file, the Czech platform's from 25 CZK per client check [S5], prices the anti-money-laundering half, which the solution connects to rather than rebuilds, so it is not this job and stays untagged; its note gained a line saying so. The consultancies and law firms [S3] publish no price. Money stays 0. Body: the Willing to pay answer now says no price for the investment-advice half is on file [S3,S4], its third item says the platform does not sell that half [S4], and the closing line names prices beside public contracts and grants. The two links to the section now named Market gap carry that name. Same result as the worksheet.
