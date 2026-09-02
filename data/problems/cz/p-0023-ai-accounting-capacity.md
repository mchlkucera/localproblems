---
id: p-0023
region: cz
title: Czech accountants are scarce, and the rules change in 2028
fix: 'An accounting firm run as an AI document pipeline with licensed accountants on top,
  starting with the single monthly payroll report every Czech employer has had to file
  since April 2026.'
category: b2b
geo: CZ-national
score: 4
scores:
  proof: 1
  money: 0
  urgency: 3
  demand: 0
  gap: 0
status: watching
build:
  capital: funded
  first_revenue: months
  builder: funded-team
  note: 'Every analog raised before scaling (Skalar €12M, Finto $3.4M, Bluebook $3M)
    because the model puts licensed accountants on payroll next to an agent stack
    — here one tuned to Pohoda/ABRA data and JMHZ filings — before fees compound.'
comps:
- name: Skalar
  url: https://skalar.de/
  geo: DE
  since: 2025
  traction: '€12M pre-seed+seed led by Headline (Munich Startup, Jul 2026); one professional
    serves 100+ clients vs ~20; targets €0.5–20M-revenue firms'
  signal: de-skalar
- name: Finto
  url: https://www.gofinto.com/
  geo: DE
  since: 2025
  traction: '$3.4M seed from Lightspeed, YC, Gradient (Tech.eu, Jul 2026); customers
    incl. Arminia Bielefeld, Eat Happy Group; SAP/DATEV integrations'
  signal: round-finto
- name: Bluebook
  url: https://getbluebook.com/
  geo: SE
  since: 2024
  traction: '$3M incl. $2.5M pre-seed led by EQT Ventures (Tech.eu, Feb 2025); 30
    leading Nordic accounting firms on the platform (getbluebook.com)'
  signal: yc-bluebook
  markets: [DK, NO, FI]
- name: Combinely
  url: https://www.combinely.ai/
  geo: GB
  since: 2024
  traction: 'YC Spring 2025; profitable (london.edu); trusted by 15+ UK accounting
    firms incl. Blick Rothenberg (Startup Intros)'
  signal: yc-combinely
locals:
- name: Účtárna.ai
  url: https://www.uctarna.ai/
  ico: '88865835'
  since: 2012
  competes: direct
  maturity: established
  evidence: 'It sells the bookkeeping itself, not the software: 300+ client companies, licensed
    accountants reviewing what the AI has posted, and published prices — bookkeeping and VAT from
    5,000 CZK a month, payroll 300 CZK per employee [S9]. The proprietor behind it has traded
    since 20 June 2012 [S9].'
- name: Trivi
  url: https://www.trivi.com/
  ico: '28378440'
  since: 2008
  competes: direct
  maturity: established
  evidence: It sells tech-enabled bookkeeping with its own accountants, tax advisors and bank
    feeds, and states that more than 1,000 entrepreneurs are its customers [S9]. Trivi a.s. has
    traded since 21 April 2008.
- name: STORMWARE (POHODA)
  url: https://www.stormware.cz/pohoda/
  ico: '25313142'
  since: 1996
  competes: adjacent
  maturity: established
  evidence: It sells accounting SOFTWARE licences to companies and to the accounting firms that
    serve them — the shelf an AI-first bookkeeping firm runs on, not the bookkeeping service,
    which STORMWARE does not sell [S3,S9]. Selling since 1996, POHODA is used in Czech companies
    under more than 180,000 licences sold, per stormware.cz verified live 2026-08-25, and it is
    the ecosystem the new Accounting Act forces a rewrite of [S3].
- name: Seyfor (Money)
  url: https://www.seyfor.cz/
  ico: '01572377'
  since: 2013
  competes: adjacent
  maturity: established
  evidence: It sells the Money accounting and ERP line to companies and their accountants — again
    the tool, not the bookkeeping service, and on the other side of the counter from an AI-first
    firm [S9]. Trading since 2013, with Město Krnov and Psychiatrická nemocnice v Kroměříži among
    its public buyers on the state contracts register.
- name: E-Consulting (AI Accounting)
  url: https://www.e-consulting.cz/
  since: 2013
  competes: direct
  maturity: early
  evidence: It sells the full-stack service itself — its technology posts up to 85% of transactions
    automatically while the firm carries the responsibility, out of Prague, Bratislava and Wrocław
    offices [S9]. It names nobody who has bought it, publishes no count and shows up against no
    public buyer on the state contracts register, so how much it sells is unknown.
- name: MyÚčto.cz
  url: https://www.myucto.cz/
  competes: direct
  maturity: early
  evidence: 'It sells the tech-enabled version of the same service: most movements posted automatically
    by rule, with a client portal and an AI assistant on top [S9]. It publishes no start year,
    no count and no client names, so how much it sells is unknown.'
- name: Digitoo
  url: https://www.digitoo.ai/
  ico: '08494584'
  since: 2019
  competes: adjacent
  maturity: early
  evidence: It sells invoice-capture automation to companies and to their accountants — one layer
    of the pipeline, not the firm that runs the whole ledger and signs off the return [S2,S9].
    Trading since 9 September 2019; it names nobody who has bought it and publishes no count,
    so how widely it is used is unknown.
sources:
- type: arbitrage
  name: "Skalar"
  gist: "the Munich €12M round"
  why: "Munich, €12M seed led by Headline — an AI-native tax and accounting firm where agents do the bookkeeping, payroll and tax grunt work so one professional serves 100+ clients."
  url: https://techfundingnews.com/skalar-raises-12m-headline-ai-accounting-firm/
  note: 'de-skalar: Skalar (Munich, Stocard founder) raised €12M seed (Headline, 14 Jul 2026)
    for an AI-native tax/accounting firm — AI agents do bookkeeping/payroll/tax grunt work
    so one professional serves 100+ clients, attacking the tax-advisor shortage. Funded DE
    analog, CEE-adjacent: arbitrage 2.'
  date: '2026-07-14'
  signal: de-skalar
- type: gap-check
  name: "Czech accounting-automation scan (first pass)"
  gist: "the superseded quick scan"
  why: "The early look at the Czech field, later superseded: it named Digitoo (invoice capture) and ÚOL (online accounting service) as the partial incumbents."
  url: https://techfundingnews.com/skalar-raises-12m-headline-ai-accounting-firm/
  note: 'Quick check 2026-08-13: CZ has Digitoo (invoice capture automation) and ÚOL (online
    accounting service) as partial incumbents; no full-stack AI-first accounting/tax firm
    found. Gap 1 (quick search only).'
  date: '2026-08-13'
- type: regulation
  name: "New Czech Accounting Act (draft)"
  gist: "the law and its 2028 date"
  why: "Submitted to parliament in December 2025 with planned effect from 1 January 2028 — IFRS-aligned concepts that force rewrites across the Pohoda/Money/ABRA/Helios ecosystem. Not yet enacted, so the date can slip."
  url: https://www.ey.com/cs_cz/technical/tax/tax-alerts/2025/12/novy-zakon-o-ucetnictvi-a-zmenovy-zakon-miri-do-poslanecke-snemovny
  note: 'reg-accounting-act-cz: nový zákon o účetnictví submitted to the Chamber 12 Dec 2025,
    planned effectiveness 1 Jan 2028 (12-month vacatio legis; NOT yet enacted — date can slip).
    IFRS-aligned concepts force rewrites across the Pohoda/Money/ABRA/Helios ecosystem and
    retraining for every accountant. Deadline 1 (>18mo, pending).'
  date: '2028-01-01'
  signal: reg-accounting-act-cz
- type: arbitrage
  name: "Finto"
  gist: "the second Munich round"
  why: "Munich, ~€2.9M seed from Lightspeed, Y Combinator and Gradient for AI agents automating enterprise accounting — the second funded Munich AI-accounting company inside a month."
  url: https://www.vestbee.com/insights/articles/top-european-funding-rounds-closed-in-july-2026
  note: 'round-finto: Finto (Munich) raised ~€2.9M seed (Jul 2026, Lightspeed + Y Combinator
    + Gradient) for AI agents automating enterprise accounting — the SECOND funded Munich
    AI-accounting company inside a month of Skalar''s €12M. Germany''s e-invoicing issuance
    mandate (2027) is making accounting automation a compliance purchase; ViDA points the
    same direction for CZ.'
  date: '2026-07-31'
  signal: round-finto
- type: arbitrage
  name: "Billow AI Labs"
  gist: "the category's newest entrant"
  why: "A YC Summer 2026 'AI-native accounting firm to replace the Big-4' — with Bluebook (Stockholm) and Combinely (London), the wedge is funded across the US, the Nordics and the UK."
  url: https://www.ycombinator.com/companies/billow-ai-labs
  note: 'yc-billow-ai-labs: Billow AI Labs (YC Summer 2026) — ''AI-native Accounting Firm
    to Replace the Big-4''; with Bluebook (YC W25, Stockholm — Nordics), Combinely (GB), Afternoon.co
    and Cifrato, the AI-accounting wedge is funded across the US, Nordics and UK. Analogs
    in 2+ markets AND CEE-adjacent validation twice over in Munich: proof upgraded 2→3.'
  date: '2026-08-13'
  signal: yc-billow-ai-labs
- type: regulation
  name: "Jednotné měsíční hlášení zaměstnavatele (Act 323/2025)"
  gist: "the monthly employer report"
  why: "Since 1 April 2026 every Czech employer files one monthly electronic report to ČSSZ in place of up to 25 forms — a live, recurring load on exactly the payroll capacity that is already short."
  url: https://www.cssz.gov.cz/kdo-podava-jmh-
  note: 'reg-cz-jmhz: Jednotné měsíční hlášení zaměstnavatele (zákon č. 323/2025 Sb.) — every
    CZ employer files a single monthly electronic report to ČSSZ from 1 Apr 2026, replacing
    up to 25 forms; Jan–Mar 2026 filed retroactively. In force with a recurring monthly clock:
    a live forcing function on exactly the payroll/accounting capacity this record is about
    — deadline sub-score 2, urgency 2→3.'
  date: '2026-04-01'
  signal: reg-cz-jmhz
- type: subsidy
  name: "OP TAK — Inovační vouchery IV"
  gist: "the rolling innovation voucher"
  why: "A rolling voucher scheme paying SMEs for knowledge services bought from research organisations, open until 30 April 2027 — co-funding for the agent stack."
  url: https://apiagentura.gov.cz/cs/radce/vsechny-vyzvy/
  note: 'dotace-optak-inovacni-vouchery-4: OP TAK Inovační vouchery IV — rolling voucher
    scheme paying SMEs for knowledge services bought from research organizations, open until
    30 Apr 2027; allocation not shown on the API agentura call listing (a parallel IP-protection
    voucher call III runs to 31 Dec 2026). Co-funding channel for the agent stack named in
    First moves.'
  date: '2027-04-30'
  signal: dotace-optak-inovacni-vouchery-4
- type: subsidy
  name: "OP TAK — Partnerství znalostního transferu IV"
  gist: "the knowledge-transfer grant"
  why: "Funds joint knowledge-transfer projects that place research expertise inside an SME; applications close 21 September 2026."
  url: https://apiagentura.gov.cz/cs/radce/vsechny-vyzvy/
  note: 'dotace-optak-pzt-4: OP TAK Partnerství znalostního transferu IV — funds joint knowledge-transfer
    projects placing research expertise into SMEs; deadline 21 Sep 2026, allocation not shown
    on the listing. The deeper co-funding route named in First moves.'
  date: '2026-09-21'
  signal: dotace-optak-pzt-4
- type: gap-check
  name: "Účtárna.ai and the Czech AI-accounting field"
  gist: "the Czech field, occupied"
  why: "A Czech-language sweep finding the model already trading here: Účtárna.ai, E-Consulting's AI Accounting, Trivi and MyÚčto.cz all sell AI-assisted bookkeeping with licensed accountants behind it."
  url: https://www.uctarna.ai/
  note: 'Gap re-check 2026-08-20: OCCUPIED. The record claimed no Czech equivalent of the full-stack
    AI-first accounting firm; the 2026-08-13 check was self-described as a quick search, and a proper
    Czech-language one finds the model already trading. Účtárna.ai sells "digitální účetnictví s
    využitím umělé inteligence" as a service, not software: bookkeeping and VAT from 5,000 CZK a
    month, payroll at 300 CZK per employee per month, tax optimization, a client document portal,
    AI-processed documents reviewed by licensed accountants on staff, and professional liability
    cover the firm states at 5 million CZK; it claims 300+ client firms on its own site, and its
    named CEO Ing. Rebecca Kotrmanová resolves in ARES (IČO 88865835, Brno, registered 2012-06-20).
    E-Consulting''s AI Accounting (Prague-Karlín, with Bratislava and Wrocław offices) runs the same
    hybrid — it states technology now posts up to 85% of transactions automatically while the firm
    carries responsibility for accuracy. Trivi a.s. (ARES IČO 28378440, Praha, 2008) has been running
    the tech-enabled version for years with its own accountants and tax advisors, smart apps and bank
    integration, and says over a thousand entrepreneurs use it; MyÚčto.cz posts most movements
    automatically by rule and ships a client portal with an AI assistant. That is alongside Digitoo
    (ARES IČO 08494584) at the invoice-capture layer, which this record already named. POSITIVE
    CONTROL passed twice before the verdict: a generic Czech query for accounting automation returned
    the obvious domestic incumbents (Pohoda/Stormware, Seyfor, ABRA FlexiBee, iDoklad, iÚčto, BMD)
    on the first page, and the register''s own known incumbents resolved by name in ARES —
    IRESOFT s.r.o., SOFTLINK s.r.o., Ringil s.r.o. De-rank rule applied: gap 1 to 0 with incumbents
    named, score 7 to 6, status watching. No count of the Czech accounting profession is asserted
    here; none was found.'
  date: '2026-08-20'
  queries:
    - "AI účetní kancelář umělá inteligence účetnictví česká firma"
    - "online účetní firma s AI vede účetnictví pro firmy Česko chytré účetnictví"
    - "účetní software pro firmy automatizace účetnictví Česko"
  checked: [ares, google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-09-02'
---

Czech accountants are scarce, and their rulebook is being rewritten. The new Accounting Act reached parliament in December 2025 and is planned for 1 January 2028 [S3]. It brings in IFRS (international financial reporting standards) and functional-currency accounting, forcing rewrites across Pohoda, Money, ABRA and Helios — the software Czech firms keep their books on — and retraining for every accountant [S3].

Why now: Munich funded this twice in one month. Skalar raised €12M from Headline for agents doing the bookkeeping, payroll and tax grunt work, so one professional serves 100+ clients [S1]. Finto followed weeks later, same city [S4]. The same scarcity is here, and the 2028 switch loosens client and accountant loyalty at once. One clock already runs: since 1 April 2026 every Czech employer files one monthly report to the social-security administration in place of up to 25 forms [S6].

Who pays: small firms that cannot find an accountant pay first, then larger ones pushed by the new Accounting Act [S3]. The AI-first firm charges service fees; a second wedge sells transition tooling to the accounting firms already here.

Existing non-solutions: Digitoo automates invoice capture and ÚOL — an online bookkeeping service — sells the bookkeeping [S2]; the software vendors will ship compliance updates [S3]. The full-stack AI firm already trades here. Účtárna.ai keeps books, VAT, payroll and tax as a service, with licensed accountants checking what the AI posted, at published prices; E-Consulting says its technology posts up to 85% of transactions automatically; Trivi and MyÚčto.cz sell the same [S9]. None is new: Trivi since 2008, Účtárna.ai's principal since 2012 [S9].

Two limits. The 2028 date is planned, not enacted [S3], so the only clock actually running is the monthly employer report [S6]. And no Czech figure for the shortage exists: the demand case rests on the German parallel.

Solved elsewhere: the AI-first accounting firm is funded across Europe, and very young. Skalar (Munich, €12M) and Finto (Germany, $3.4M) raised in 2026, both selling only since 2025 [S1]; Bluebook (Sweden) and Combinely (Britain, profitable) opened in 2024, and Billow AI Labs came out of Y Combinator this summer [S4,S5]. None has traded three years. Abroad that is a market being proven now, a fair moment to join; here the seat is already held by firms selling for a decade and more.

## First moves

1. Call five payroll bureaus and accounting firms about the monthly employer report — every employer has filed it since 1 April 2026 [S6]. Write down what one filing costs them. That is the demand number nobody has.
2. Automate that one report end-to-end for a single bureau before touching bookkeeping. It is the only recurring clock here, and it replaced up to 25 separate forms [S6].
3. Hire one licensed Czech accountant as the founding professional. Skalar runs one professional per 100+ clients [S1], so the first hire buys leverage, not headcount.
4. Pre-sell to ten small firms that cannot find an accountant, and pull the shortage statement from the Komora daňových poradců, the chamber of tax advisers. No Czech figure exists yet.
5. Let public money carry part of the build. [OP TAK Inovační vouchery IV](/sources/tenders#dotace-optak-inovacni-vouchery-4) — the state's business-support programme — pays small firms for research-institute work, rolling until 30 April 2027, with no allocation published [S7]. The deeper route, [OP TAK Partnerství znalostního transferu IV](/sources/tenders#dotace-optak-pzt-4), closes 21 September 2026 [S8].
6. Plan to displace, not to fill a void. **Účtárna.ai** already runs the whole thing — books, VAT, payroll, tax, licensed accountants over an AI document pipeline, published prices; **E-Consulting AI Accounting** says it posts up to 85% of transactions automatically; **Trivi** and **MyÚčto.cz** sell the tech-enabled service; **Digitoo** holds invoice capture and **ÚOL** the online bookkeeping [S2,S9]. Price, a niche, or the 2028 changeover is the wedge — and 2028 is still only planned, and can slip [S3].

## Revisions


2026-08-25 · rewrite — Added the missing “Solved elsewhere” paragraph so the Proven-abroad section renders its argument rather than a bare comps ledger; no score, source note or citation target changed. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. The who-pays opening sentence, which IS the dek, was reworded out of insider shorthand a reader outside Czechia could not decode: "facing the act’s transition" now names the act — "facing the new Czech Accounting Act". Scores, status, source notes and every [Sn] marker are untouched by those passes. Third pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test. `scores.proof` 3 → 1, and this record is the worked example of why the v1 ladder had to go. The old 3 was awarded on 2026-08-13 for "analogs in 2+ markets AND CEE-adjacent validation twice over in Munich" — a count of companies that exist. Under the maturity test not one of the four comparables qualifies: Skalar and Finto started selling in 2025, Bluebook and Combinely in 2024, so all four fail the three-year limb and the ladder reads EARLY foreign players only, rung 1. That is not a demotion of the opportunity — rung 1 explicitly means the market is being proven right now and it is a good moment to join — but it is an honest statement that there is no durable business abroad to copy yet. `scores.gap` stays 0, and now means TAKEN rather than the v1 rung's "check not done": seven local players were lifted out of the [S9] scan prose into a structured `locals[]` ledger, four established — Účtárna.ai (IČO 88865835, ARES 2012, 300+ client firms), Trivi (IČO 28378440, ARES 2008, 1,000+ entrepreneurs), STORMWARE/POHODA (180,000+ licences, verified live on stormware.cz this date) and Seyfor (two distinct public buyers in `data/lookup/cz-contract-parties.jsonl`) — and three early on receipts alone: E-Consulting, MyÚčto.cz and Digitoo publish no customer count, pair with no public buyer and carry no round or state listing. `score` 6 → 4. ABRA and Helios/Asseco were deliberately NOT lifted: they appear in [S9] as first-page hits of the positive control, not as sellers of the model this record proposes, and no maturity limb is receipted for them here. The why-now and Proven-abroad paragraphs were rewritten so the words stop asserting a proven category — the foreign detail moved out of "Why now", which duplicated it, into "Solved elsewhere" where the maturity finding belongs, and the argument was trimmed back under the length target in the same pass. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. Two entries are relabelled and one more corrected. STORMWARE (POHODA) and Seyfor (Money) move to `competes: adjacent` at `maturity: established` — both sell accounting SOFTWARE licences to companies and to the firms that keep their books, which is the shelf an AI-first accounting firm would run on rather than the bookkeeping service this file describes. They stay established, on the POHODA licence tally and on Seyfor's two distinct public buyers, and neither now touches the score. Digitoo moves to `adjacent` on the reason its own evidence line already carried: invoice capture is one layer of the pipeline, not the firm that runs the ledger and signs off the return. `scores.gap` stays 0 and is now carried only by the two direct sellers that pass the test, Účtárna.ai and Trivi — which is what the 0 always meant here, and what the one-field schema could not say. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.

2026-08-20 · gap re-check and evidence audit — Two blocks recorded on this date, merged here. De-ranked: the AI-native accounting firm has a Czech operator. The prior gap check labelled itself "quick search only" and concluded no full-stack AI-first accounting or tax firm existed here. It does. Účtárna.ai sells exactly that model as a service — bookkeeping, VAT, payroll, tax optimization, a client portal, AI-processed documents reviewed by licensed accountants, published pricing, and a stated 300+ client firms; its named CEO resolves in ARES (IČO 88865835). E-Consulting AI Accounting states technology posts up to 85% of transactions automatically while the firm remains responsible for accuracy, and Trivi a.s. (IČO 28378440) and MyÚčto.cz run tech-enabled versions of the same service [S9]. Per the SPEC §4 de-rank rule: gap 1 → 0, score 7 → 6, status candidate → watching. The title's claim that the model "has no Czech equivalent" was removed for the same reason, and the non-solutions paragraph and first move 6 were rewritten so the body stops asserting an absence its own score denies. The scarcity and the 2028 re-platforming window are untouched — they are backed by [S3] and [S6] and remain the record's live content. Cut in the same pass: the count of Czech accounting firms in "Who pays", because no count of the profession exists anywhere in the signal corpus or in any source note here and the wedge stands without it; and the client-load baseline in the third first move, which lives only in the Skalar comps traction line, and a comparable's traction cannot back a body claim. The client figure the Skalar source note does carry is unchanged and still cited [S1]. No headcount for the Czech accounting profession has been reintroduced: the re-check looked and found none.

THE LEDGER NOTES, IN PLAIN LANGUAGE. All 7 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Glossed IFRS, ABRA and ÚOL at first use; replaced three acronyms with plain words — JMHZ became the monthly employer report [S6], ČSSZ the social-security administration, UK Britain. Argument tightened 447 to 385 words, every [Sn] marker, figure, date and named company kept. First moves rewritten verbs-first, the register-bookkeeping opener on move six gone. A gist added to all nine sources. No score, status, note or marker touched.
