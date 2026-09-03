---
id: p-0034
region: cz
title: Czech firms run live EU AI transparency duties with no national supervisor yet
fix: 'A fixed-price check of every AI tool a small Czech company uses — does the chatbot
  say it is a machine, is the AI-made content labelled — repeated each time the rules or the
  regulator move.'
category: legal-compliance
geo: CZ-national
score: 5
scores:
  proof: 1
  money: 0
  urgency: 3
  demand: 0
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'A fixed-price audit of what AI a firm runs, and whether it tells customers, sells as
    a service today; a product has to get past PwC''s tooling, cheap scanners like AIshield
    and Czech-language modules like Brain. What none of them has yet is a Czech regulator
    actually enforcing, and that is the opening.'
comps:
- name: Deeploy
  url: https://deeploy.ml/
  geo: NL
  since: 2020
  traction: 'up to €7.5M EIC blended finance for AI-act-aligned MLOps (Silicon Canals, Feb
    2025), after a €2.5M round (Tech.eu, Jun 2023)'
  signal: round-deeploy
locals:
- name: PwC ČR (AI Compliance Tool)
  url: https://www.pwc.com/cz/cs/sluzby/umela-inteligence-ai/ai-act/ai-compliance-tool.html
  since: 2025
  competes: direct
  maturity: early
  evidence: 'It sells an AI Compliance Tool in Czech — documentation and an audit trail against
    the act — which is this product, sold now [S3,S7]. The firm behind it is old, the offering
    is not: the transparency duty it answers only began applying on 2 August 2026, and no count
    of who has bought it is published.'
- name: AIshield.cz
  url: https://www.aishield.cz/
  since: 2025
  competes: direct
  maturity: early
  evidence: It sells a self-serve scan of a Czech website's exposure under the AI act [S3,S7]
    — the same check, sold off the shelf. It was built against a duty that only started applying
    in August 2026, and publishes no count of who has bought it.
- name: Brain (startbrain.ai)
  url: https://startbrain.ai/
  since: 2025
  competes: direct
  maturity: early
  evidence: It sells Czech-language AI-act compliance modules that reflect local legislation,
    against the same 2026 duty [S3,S7]. Launched into a duty months old, it names no buyer and
    publishes no count.
- name: Seyfor
  url: https://www.seyfor.cz/
  ico: '01572377'
  since: 2013
  competes: adjacent
  maturity: established
  evidence: It sells accounting and ERP software to Czech companies and publishes advisory articles
    about the AI Act [S7]; it does not sell a check of the AI tools a company uses, which is what
    this space is. Trading since 2013, with Město Krnov and Psychiatrická nemocnice v Kroměříži
    among its public buyers on the state contracts register.
- name: Adastra
  url: https://www.adastragrp.com/
  competes: adjacent
  maturity: early
  evidence: It sells data and AI consulting engagements and publishes advisory guidance on the
    AI Act [S7] — project work and reading material, not a fixed-price check a small company buys
    off the shelf. No start year for an AI-act offering is on file and no buyer is named; no IČO
    is recorded either, because the name resolves to more than a dozen Czech entities and none
    could be tied to this offering.
sources:
- type: regulation
  name: "VeKLEP — návrh zákona o umělé inteligenci (MPO)"
  gist: "the Czech bill, still draft"
  why: "The Czech adaptation bill itself: MPO's draft law on artificial intelligence, through interministerial comments and last moved June 2026, with the state-authored RIA problem definition attached."
  url: https://odok.gov.cz/portal/veklep/material/KORNDLSJSEUC/
  note: 'veklep-KORNDLSJSEUC: Návrh zákona o umělé inteligenci a o změně některých souvisejících
    zákonů, MPO čj. 100789/2025, OVA 503/26. Materiál page verified live 2026-08-25: authorized
    2025-09-25, last modified 2026-06-26, vypořádání připomínek attached (1.06 MB) — comments
    settled, awaiting government. RIA and důvodová zpráva on the materiál page; the bill amends
    the market-surveillance act 87/2023 Sb. and establishes the supervision mechanism and a
    notification body.'
  date: '2025-09-25'
  signal: veklep-KORNDLSJSEUC
- type: regulation
  name: "LeitnerLaw — the adaptation act's competences and sanctions"
  gist: "the enforcers and the fines"
  why: "Law-firm analysis of the draft: ČTÚ takes general (residual) AI oversight, ČNB the financial sector, ÚOOÚ sensitive high-risk systems; ČAS runs the regulatory sandbox and fines follow the AI Act's turnover-scaled model."
  url: https://www.leitnerlaw.cz/novinky/ai-act-v-praxi-cesky-adaptacni-zakon-vymezuje-kompetence-postupy-a-sankce/
  note: 'Verified 2026-08-25: draft completed interministerial review, awaiting government;
    designates ČTÚ (general residual competence), ČNB (regulated financial institutions),
    ÚOOÚ (high-risk systems in law enforcement, justice, elections, migration); ÚNMZ approves
    conformity-assessment bodies; regulatory sandbox at the Czech Standardization Agency (ČAS).
    Sanctions mirror the AI Act (turnover-percentage or fixed, lower limit for SMEs), with a
    "genuine repentance" waiver. Expected adoption to align with 2 Aug 2026 application —
    a date already passed at the time of this record.'
  date: '2026-08-25'
- type: regulation
  name: "EU AI Act — application dates after the Digital Omnibus"
  gist: "the dates already in force"
  why: "The obligations already in force: Article 50 transparency (disclose AI interaction, label synthetic content) applies since 2 August 2026, while the Digital Omnibus pushed high-risk deadlines to December 2027 and August 2028."
  url: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  note: 'reg-ai-act-milestones: prohibitions applied 2 Feb 2025, GPAI duties 2 Aug 2025, general
    application incl. Art 50 transparency 2 Aug 2026 (watermarking grace for existing systems
    to 2 Dec 2026); Digital Omnibus (agreed May 2026) postpones high-risk obligations to
    2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I). Deadline sub-score 2: the transparency
    tier is in force now, <18 months trivially.'
  date: '2026-08-02'
  signal: reg-ai-act-milestones
- type: regulation
  name: "MPO — the enforcement gap"
  gist: "the missed designation deadline"
  why: "The ministry's own announcement of the lean adaptation act — and the record that Czechia missed the EU deadline for designating national AI authorities while obligations phase in."
  url: https://mpo.gov.cz/cz/rozcestnik/pro-media/tiskove-zpravy/mpo-pripravilo-navrh-zakona-o-umele-inteligenci--cilem-je-vytvorit-co-nejlepsi-prostredi-pro-rozvoj-ai-v-cesku--289653/
  note: 'reg-ai-act-cz-dozor: MPO''s ~26-paragraph adaptation act plugs AI Act enforcement
    into market-surveillance act 87/2023 Sb.; the planned July 2026 effectiveness already
    slipped, and CZ missed the EU authority-designation deadline while obligations phase in —
    deployers face EU duties with no national supervisor operating.'
  date: '2026-07-01'
  signal: reg-ai-act-cz-dozor
- type: arbitrage
  name: "Deeploy"
  gist: "the funded Dutch analog"
  why: "Utrecht — public EU capital (up to €7.5M EIC blended finance) behind a platform selling exactly the explainability and compliance layer the AI Act's high-risk duties demand."
  url: https://deeploy.ml/europe-invests-in-deeploy/
  note: 'round-deeploy: Deeploy B.V. (Utrecht, founded 2020) selected for EIC blended finance
    (Feb 2025, up to €7.5M per Silicon Canals) for a human-centric MLOps platform positioned
    on EU AI Act high-risk obligations; earlier €2.5M round Jun 2023 (Tech.eu). Funded EU
    analog; proof held at 1 because the Czech field is occupied (see gap check).'
  date: '2025-02-17'
  signal: round-deeploy
- type: arbitrage
  name: "Trustpath"
  gist: "the Croatian pre-seed"
  why: "Croatia — a Credo Ventures pre-seed portfolio company selling EU AI Act vendor-compliance and trust tooling, the same statutory demand one market over."
  url: https://trustpath.ai/
  note: 'hr-trustpath: Croatian AI-compliance platform in Credo Ventures'' Fund V pre-seed
    portfolio (superscout investor page); product verified live 2026-08-25 — enterprise AI
    risk management with built-in EU AI Act compliance, vendor assessment and governance
    dashboards. No public traction numbers, so it is cited as an analog and kept off the
    comps ledger (founding year and figures unverifiable).'
  date: '2024-12-31'
  signal: hr-trustpath
- type: gap-check
  name: "Czech AI-act compliance field scan"
  gist: "the five Czech names found"
  why: "Czech-language search finds the position already forming: PwC ČR sells an AI Compliance Tool, AIshield.cz scans websites for AI-act exposure, Brain (startbrain.ai) sells Czech-language compliance modules, and Adastra and Seyfor publish compliance guidance."
  url: https://www.pwc.com/cz/cs/sluzby/umela-inteligence-ai/ai-act/ai-compliance-tool.html
  note: 'Gap check 2026-08-25: OCCUPIED — the check found incumbents, so no absence is claimed
    and no positive control is required for a positive result. Czech-language search for AI-act
    compliance tooling returns PwC ČR''s AI Compliance Tool (documentation + audit trail for
    AI project compliance, in Czech), AIshield.cz (self-serve AI-act exposure scan for Czech
    websites, productised), Brain at startbrain.ai (Czech-language AI-act compliance modules
    reflecting local legislation), and advisory content from Adastra and Seyfor. Own funded
    ledger grepped for CZ AI-governance entrants: none (the AI-compliance cluster on file is
    US/GB/NL/HR/BE/ES). Big-four tooling plus at least two productised Czech offers: gap 0
    with incumbents named, status watching per the de-rank rule.'
  date: '2026-08-25'
  queries:
    - '"AI Act" compliance software česká firma nástroj soulad audit AI systémů'
    - 'AI Act povinnosti české firmy srpen 2026 nástroj software'
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-23'
- type: regulation
  name: "Plán legislativních prací vlády 2026 — annex 1"
  gist: "the government's own late list"
  why: "The government's own legislative plan flags 21 of its bills for EU infringement exposure — the AI act adaptation among them, planned to take effect in July 2026, a date already past."
  url: https://vlada.gov.cz/assets/media-centrum/dulezite-dokumenty/1234_2026_priloha_c-_1.pdf
  note: 'reg-plan2026-eu-infringement: annex 1 to government resolution 175 of 23 March 2026,
    the legislative plan for the rest of 2026. 21 of 112 tasks carry an infringement footnote;
    16 read "Předložení návrhu v daném termínu je spojeno s hrozbou zahájení řízení", 5 read
    "Implementační lhůta u předpisu EU nebyla dodržena", and one — the capital-market act
    transposing directive 2022/2381, unrelated to this record — already has proceedings open
    with a real prospect of an Article 260(3) TFEU sanction. Cited here for one row: MPO-1, the
    AI act adaptation, planned effective 07.2026 and footnoted for infringement risk. That is
    the government''s own dated admission behind this record''s claim that the bill is late,
    which until now rested on the VeKLEP material page [S1] and a law-firm note [S2]. Context
    receipt: it does not move urgency, which the in-force transparency tier already sets at its
    deadline ceiling [S3]. Runner-ups on the same plan and deliberately not linked: MPO-2 Data
    Act and MPO-7 CRA, which belong to p-0021 and p-0016, both rejected records.'
  date: '2026-03-23'
  signal: reg-plan2026-eu-infringement
  dims: []
created: '2026-08-25'
updated: '2026-09-03'
---

Since 2 August 2026 the EU AI Act's transparency rules bind every Czech firm putting AI in front of customers: a chatbot must say it is a machine, AI-made content must be labelled [S3]. The industry ministry's bill naming its enforcer has awaited the government since June 2026 [S1,S2], and Czechia missed the EU deadline for designating national AI authorities [S4]. The government's own legislative plan had the bill taking effect in July 2026 and flags it, with twenty other files, for EU infringement exposure [S8].

Why now: the draft gives general oversight to ČTÚ (the telecoms regulator), financial firms to ČNB (the central bank) and sensitive high-risk systems to ÚOOÚ (the data-protection office), with turnover-scaled fines and a sandbox at ČAS (the standards agency) [S2]. None of it operates yet. The Digital Omnibus pushed high-risk deadlines to December 2027 and August 2028 [S3], so transparency is the wave already here.

Who pays: Czech companies using AI, not the ones building it. A small firm with a customer-facing chatbot or AI-written content is caught by the transparency rules first [S3]. Firms selling systems the act calls high-risk buy readiness for the 2027 and 2028 deadlines [S3]. No Czech tender or grant is on file, so no budget is claimed.

Existing non-solutions: PwC Czechia sells an AI Compliance Tool in Czech, AIshield.cz a self-serve exposure scan, Brain a set of Czech-language compliance modules; Adastra and Seyfor publish guidance only [S7]. None has been on sale three years — the duty they answer began on 2 August 2026 [S3]. The field is contested, not closed.

Solved elsewhere: thinly. Deeploy has sold from Utrecht since 2020 and took up to €7.5M of EU innovation-council money for a machine-learning platform built on the act's explainability duties, but names no customer and raised nothing labelled Series A [S5]. Trustpath (Croatia) is a Credo Ventures pre-seed with no public traction [S6]. Nothing proven to import, nobody established to displace.

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-25 · record created — Minted from the first VeKLEP harvest (198 legislative drafts, run 2026-08-25): the MPO adaptation bill supplies the Czech state's own problem definition [S1], with competences and sanctions receipted from law-firm analysis [S2] and EU application dates from the ledger [S3]. The gap check found the Czech compliance field already occupied (PwC, AIshield, Brain), so the record is born watching at gap 0 [S7]; proof held at 1 despite funded EU analogs [S5,S6] for the same reason. Second pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, which was written to end exactly the reasoning quoted in the previous sentence. `scores.gap` 0 → 1. The 0 was set because [S7] found players; the new ladder asks how mature they are, and none of the three Czech products is. PwC ČR's AI Compliance Tool, AIshield.cz's exposure scan and Brain's Czech-language modules all answer a duty that only began applying on 2 August 2026 [S3], so on the year the PRODUCT started selling — which is what the test reads — every one fails the three-year limb, and none publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or state listing. An early local player does not close a space. Adastra and Seyfor were lifted into `locals[]` too: Seyfor is established as a company on the public-buyer limb, but what it sells here is published advisory guidance rather than a compliance product, so it does not hold the position either. Gap is not raised past 1: [S7] found local players, not none, so rung 2 is unavailable. `scores.proof` stays 1, and for the first time on a defensible reason. The [S5] note says proof was "held at 1 because the Czech field is occupied" — a LOCAL fact inside a FOREIGN dimension, the precise defect the new SCORING.md struck off the ladder. That note is left exactly as written, but it no longer carries the score. The number survives on its own merits: Deeploy has sold since 2020, so it clears the three-year limb, but it publishes no customer list, pairs with no public buyer, holds no state listing, and its up-to-€7.5M EIC blended finance is public-institution money rather than a round labelled Series A or later, so no limb passes and it reads early. Trustpath is a pre-seed with no public traction at all. Early foreign players only is rung 1 exactly. `score` 4 → 5. The `fix:` line and the who-pays opening were rewritten out of the jargon the owner banned — "Article 50 transparency audit for Czech SME deployers … as the adaptation act lands and ČTÚ enforcement starts" now reads as a plain description of what gets checked and for whom — and the build note lost "Art 50" with it. The non-solutions paragraph stopped printing its own score in words ("Occupied — gap 0 with incumbents named") and now states the fact that carries it: nothing in the field is three years old. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. SEYFOR IS RESTORED, AND ADASTRA WITH IT. Both were named in the argument and in this file's own earlier entry as lifted into `locals[]`, and neither was actually on the ledger. Seyfor had been dropped for a specific reason: its IČO auto-passes the machine buyer limb, so under the one-field schema a firm that only publishes advisory articles about the AI Act would have read as an established local player holding the space, and dropping it was the only way to avoid saying that. That is exactly an adjacent player, and the owner's ruling is that nothing is excluded — an adjacent player is intelligence a builder needs. Seyfor returns at `competes: adjacent` + `maturity: established`, with the buyer limb doing the job it is for, settling maturity rather than eligibility, and the evidence line saying plainly that it sells accounting and ERP software and publishes AI-Act guidance, neither of which is a check of the tools a company actually uses. Adastra returns at adjacent + `early`: consulting engagements and advisory guidance, with no start year for an AI-act offering on file. No IČO is written for Adastra, because the name resolves to more than a dozen Czech entities in ARES and none could be tied to this offering — an invented identifier would be worse than none, and `url` alone satisfies the ledger. PwC ČR, AIshield.cz and Brain stay `direct` + `early`. `scores.gap` stays 1: direct competitors exist and every one of them is early, which is the rung exactly, and the two restored adjacent rows move nothing. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 5 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Seven acronyms glossed or replaced at first use: MPO, ČTÚ, ČNB, ÚOOÚ, ČAS, ČR and EIC now read as the industry ministry, the telecoms regulator, the central bank, the data-protection office, the standards agency, PwC Czechia and EU innovation-council money. Argument cut 377 → 298 words, every [Sn] marker, date and figure kept. A gist added to all seven sources. No score, status, note or marker touched.
