---
id: p-0034
region: cz
title: 'Czech firms must now say their chatbots are AI, and a draft law sets fines'
brief: 'AI-made content must now be labelled too [S3]. Yet the Czech law naming who checks and fines firms is still a draft, past the EU''s deadline [S1,S2,S4].'
solution: 'Build an online check that scans a small firm''s website for chatbots and AI-made content that must be disclosed.'
good_for: 'Someone who''d like to help small firms follow the new AI rules.'
category: legal-compliance
geo: CZ-national
score: 4
scores:
  proof: 1
  money: 0
  urgency: 2
  demand: 0
  gap: 1
status: candidate
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: small firms buy the check themselves, no licence is needed to sell it, and the one
      established firm nearby publishes guidance rather than a check. Harder: three young Czech
      products already sell the check, and no Czech buyer is known to have paid for one yet.'
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
  why: "The Czech adaptation bill itself: the industry ministry's draft law on artificial intelligence, through the ministries' comments and last changed in June 2026, with the state's own impact assessment attached."
  url: https://odok.gov.cz/portal/veklep/material/KORNDLSJSEUC/
  note: 'veklep-KORNDLSJSEUC: Návrh zákona o umělé inteligenci a o změně některých souvisejících
    zákonů, MPO čj. 100789/2025, OVA 503/26. Materiál page verified live 2026-08-25: authorized
    2025-09-25, last modified 2026-06-26, vypořádání připomínek attached (1.06 MB) — comments
    settled, awaiting government. RIA and důvodová zpráva on the materiál page; the bill amends
    the market-surveillance act 87/2023 Sb. and establishes the supervision mechanism and a
    notification body.
    Corrected 2026-09-19: a bill fails REAL on the 2026-09-19 ladder, and the score rests on the
    enacted AI Act [S3], so this draft now backs no urgency and dims is set empty.'
  date: '2025-09-25'
  signal: veklep-KORNDLSJSEUC
  dims: []
- type: regulation
  name: "LeitnerLaw — the adaptation act's competences and sanctions"
  gist: "the enforcers and the fines"
  why: "Law-firm analysis of the draft: the telecoms regulator takes general AI oversight, the central bank the financial sector and the data-protection office sensitive high-risk systems; the standards agency runs a supervised test space, and fines follow the AI Act's turnover-scaled model."
  url: https://www.leitnerlaw.cz/novinky/ai-act-v-praxi-cesky-adaptacni-zakon-vymezuje-kompetence-postupy-a-sankce/
  note: 'Verified 2026-08-25: draft completed interministerial review, awaiting government;
    designates ČTÚ (general residual competence), ČNB (regulated financial institutions),
    ÚOOÚ (high-risk systems in law enforcement, justice, elections, migration); ÚNMZ approves
    conformity-assessment bodies; regulatory sandbox at the Czech Standardization Agency (ČAS).
    Sanctions mirror the AI Act (turnover-percentage or fixed, lower limit for SMEs), with a
    "genuine repentance" waiver. Expected adoption to align with 2 Aug 2026 application —
    a date already passed at the time of this record.
    Corrected 2026-09-19: these fines are the draft''s, not law, so they do not meet TEETH on the
    2026-09-19 ladder, and this analysis of a bill now backs no urgency; dims is set empty.'
  date: '2026-08-25'
  dims: []
- type: regulation
  name: "EU AI Act — application dates after the Digital Omnibus"
  gist: "the dates already in force"
  why: "The obligations already in force: Article 50 transparency (disclose AI interaction, label synthetic content) applies since 2 August 2026, while the Digital Omnibus pushed high-risk deadlines to December 2027 and August 2028."
  url: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
  note: 'reg-ai-act-milestones: prohibitions applied 2 Feb 2025, GPAI duties 2 Aug 2025, general
    application incl. Art 50 transparency 2 Aug 2026 (watermarking grace for existing systems
    to 2 Dec 2026); Digital Omnibus (agreed May 2026) postpones high-risk obligations to
    2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I). Deadline sub-score 2: the transparency
    tier is in force now, <18 months trivially.
    Corrected 2026-09-19: the deadline sub-score is retired. On the 2026-09-19 ladder Art 50 is
    REAL (an EU regulation, binding as published, with duties on deployers as well as providers)
    and CLOSE (applied 2 Aug 2026, 1.5 months before), so urgency 2. TEETH fails: for a passed
    date it needs enforcement within 12 months, and no Czech supervisor operates yet [S4].'
  date: '2026-08-02'
  signal: reg-ai-act-milestones
- type: regulation
  name: "MPO — the enforcement gap"
  gist: "the missed designation deadline"
  why: "The industry ministry's own announcement of the short adaptation law, and the evidence that Czechia missed the EU deadline for naming national AI authorities while the duties phase in."
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
  why: "Utrecht: up to €7.5M of EU innovation-council money behind a platform that sells the explainability and compliance layer the AI Act's high-risk duties demand."
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
    Act and MPO-7 CRA, which belong to p-0021 and p-0016, both rejected records.
    Corrected 2026-09-19: "its deadline ceiling" was the retired deadline sub-score; the
    transparency tier now sets urgency at 2, as the note on S3 says.'
  date: '2026-03-23'
  signal: reg-plan2026-eu-infringement
  dims: []
created: '2026-08-25'
updated: '2026-09-19'
---

Since 2 August 2026, EU rules say a chatbot must tell people it is a machine, and AI-made content must be labelled [S3].

- Both the makers and the users of AI carry duties, with exceptions [S3].
- The Czech law naming who checks and fines firms is still a draft [S1,S2].
- Czechia missed the EU's deadline for naming its national AI authorities [S4].

The rules come from the EU AI Act, the EU's regulation on artificial intelligence, so they already bind firms here without a Czech law [S3,S4].

- The Czech bill comes from the industry ministry. It is short, and plugs AI oversight into the existing Czech law on market surveillance [S1,S4].
- The ministries have settled their comments on it, and it has awaited the government since June 2026 [S1,S2].
- The government's own legislative plan marks it, and 20 other bills, as at risk of EU proceedings against Czechia for being late [S8].

Existing non-solutions: Three young Czech products already sell this check, and none says how many firms have bought one [S7].

- A big audit firm's Czech arm sells a compliance tool, in Czech [S7].
- A self-serve scan shows what a Czech website must disclose under the act [S7].
- A third seller offers Czech-language compliance modules that reflect Czech law [S7].

The audit firm's tool keeps the documentation and an audit trail against the act [S7]. None of the three has had three years to sell, because the duty it answers is new; see [Why now](#why-now) [S3,S7]. So no established seller holds the field: it is contested, not closed.

Two more firms publish guidance on the act, and neither sells a check [S7]. One is an established accounting and business-software house, the other a data and AI consultancy [S7].

Why now: A firm that does not disclose its chatbot or AI-made content can already break EU rules, and a Czech draft sets fines [S2,S3].

- Fines would be a share of a firm's turnover or a fixed sum [S2].
- Makers of existing AI tools must mark AI-made output by 2 December 2026 [S3].
- No Czech regulator is working yet, though the EU duties already apply [S4].

The draft says who would check and fine firms, and none of it operates yet [S2,S4]:

- ČTÚ (the telecoms regulator) would oversee most firms [S2].
- ČNB (the central bank) would oversee financial firms [S2].
- ÚOOÚ (the data-protection office) would oversee sensitive high-risk systems, such as those used by the police, the courts, elections and migration [S2].
- ČAS (the standards agency) would run a sandbox, a place where firms can test AI under supervision [S2].
- The fines would follow the EU act's model, with a lower ceiling for small firms [S2].

The dates come from the EU act and from the Czech government's plan [S3,S8]:

- On 2 February 2025 the act's bans began to apply, and on 2 August 2025 its duties for general-purpose AI models [S3].
- In July 2026 the Czech law was planned to take effect, but in August the bill still awaited the government [S1,S8].
- On 2 August 2026 the transparency rules began to apply [S3].
- On 2 December 2026 the grace period ends for marking the output of AI tools already on sale [S3].
- On 2 December 2027 and 2 August 2028 the duties for high-risk AI systems begin [S3]. The EU's Digital Omnibus, a package of rule changes agreed in May 2026, moved them back, so the transparency rules are the ones already here [S3].

Who pays: No Czech firm is known to have paid for this check yet, and no Czech tender or grant for it is on file [S7].

- The buyers would be Czech firms that use AI with their customers [S3].
- A small firm with a chatbot or AI-written content is caught first [S3].
- Firms selling high-risk AI systems face later deadlines; see [Why now](#why-now) [S3].

The makers of AI tools have duties of their own, such as marking what their tools produce [S3]. The sellers under [Market gap](#competition) publish no count of who has bought from them, so no budget is claimed [S7].

Solved elsewhere: Only thinly: a Dutch platform backed by EU innovation money and a Croatian pre-seed startup, neither with public customers [S5,S6].

The Dutch company has sold from Utrecht since 2020 [S5]. It took up to €7.5M of EU innovation-council money for a machine-learning platform that explains AI decisions, as the act demands of high-risk AI [S5]. It names no customer and has raised nothing labelled Series A [S5]. What it sells covers high-risk systems, not the transparency check [S5].

Trustpath, from Croatia, is a pre-seed company backed by the investor Credo Ventures [S6]. It sells larger firms AI risk management with EU AI Act compliance built in, and publishes no traction [S6].

So nothing abroad is yet proven enough to import [S5,S6].

## Revisions

2026-08-25 · status follows gap — Corrected from `watching` to `candidate` under the rewritten de-rank rule in SPEC.md. The old rule sent a record to `watching` the moment ANY local player was found; this record's local field is contested rather than taken, meaning the players on file are all EARLY by the SCORING.md established test and none of them closes the space. Scores are untouched — only the status word, which had been asserting the opposite of the score printed beside it.

2026-08-25 · record created — Minted from the first VeKLEP harvest (198 legislative drafts, run 2026-08-25): the MPO adaptation bill supplies the Czech state's own problem definition [S1], with competences and sanctions receipted from law-firm analysis [S2] and EU application dates from the ledger [S3]. The gap check found the Czech compliance field already occupied (PwC, AIshield, Brain), so the record is born watching at gap 0 [S7]; proof held at 1 despite funded EU analogs [S5,S6] for the same reason. Second pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, which was written to end exactly the reasoning quoted in the previous sentence. `scores.gap` 0 → 1. The 0 was set because [S7] found players; the new ladder asks how mature they are, and none of the three Czech products is. PwC ČR's AI Compliance Tool, AIshield.cz's exposure scan and Brain's Czech-language modules all answer a duty that only began applying on 2 August 2026 [S3], so on the year the PRODUCT started selling — which is what the test reads — every one fails the three-year limb, and none publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or state listing. An early local player does not close a space. Adastra and Seyfor were lifted into `locals[]` too: Seyfor is established as a company on the public-buyer limb, but what it sells here is published advisory guidance rather than a compliance product, so it does not hold the position either. Gap is not raised past 1: [S7] found local players, not none, so rung 2 is unavailable. `scores.proof` stays 1, and for the first time on a defensible reason. The [S5] note says proof was "held at 1 because the Czech field is occupied" — a LOCAL fact inside a FOREIGN dimension, the precise defect the new SCORING.md struck off the ladder. That note is left exactly as written, but it no longer carries the score. The number survives on its own merits: Deeploy has sold since 2020, so it clears the three-year limb, but it publishes no customer list, pairs with no public buyer, holds no state listing, and its up-to-€7.5M EIC blended finance is public-institution money rather than a round labelled Series A or later, so no limb passes and it reads early. Trustpath is a pre-seed with no public traction at all. Early foreign players only is rung 1 exactly. `score` 4 → 5. The `fix:` line and the who-pays opening were rewritten out of the jargon the owner banned — "Article 50 transparency audit for Czech SME deployers … as the adaptation act lands and ČTÚ enforcement starts" now reads as a plain description of what gets checked and for whom — and the build note lost "Art 50" with it. The non-solutions paragraph stopped printing its own score in words ("Occupied — gap 0 with incumbents named") and now states the fact that carries it: nothing in the field is three years old. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. SEYFOR IS RESTORED, AND ADASTRA WITH IT. Both were named in the argument and in this file's own earlier entry as lifted into `locals[]`, and neither was actually on the ledger. Seyfor had been dropped for a specific reason: its IČO auto-passes the machine buyer limb, so under the one-field schema a firm that only publishes advisory articles about the AI Act would have read as an established local player holding the space, and dropping it was the only way to avoid saying that. That is exactly an adjacent player, and the owner's ruling is that nothing is excluded — an adjacent player is intelligence a builder needs. Seyfor returns at `competes: adjacent` + `maturity: established`, with the buyer limb doing the job it is for, settling maturity rather than eligibility, and the evidence line saying plainly that it sells accounting and ERP software and publishes AI-Act guidance, neither of which is a check of the tools a company actually uses. Adastra returns at adjacent + `early`: consulting engagements and advisory guidance, with no start year for an AI-act offering on file. No IČO is written for Adastra, because the name resolves to more than a dozen Czech entities in ARES and none could be tied to this offering — an invented identifier would be worse than none, and `url` alone satisfies the ledger. PwC ČR, AIshield.cz and Brain stay `direct` + `early`. `scores.gap` stays 1: direct competitors exist and every one of them is early, which is the rung exactly, and the two restored adjacent rows move nothing. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 5 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — Seven acronyms glossed or replaced at first use: MPO, ČTÚ, ČNB, ÚOOÚ, ČAS, ČR and EIC now read as the industry ministry, the telecoms regulator, the central bank, the data-protection office, the standards agency, PwC Czechia and EU innovation-council money. Argument cut 377 → 298 words, every [Sn] marker, date and figure kept. A gist added to all seven sources. No score, status, note or marker touched.

2026-09-16 · headline copy — The top of the record was rewritten for a general builder as a headline and three lines: a `brief:` telling the situation, the `solution:` as a call to action opening "Build", and a new `good_for:` line. Previous title, verbatim: "Czech firms run live EU AI transparency duties with no national supervisor yet". Previous solution, verbatim: "A fixed-price check of every AI tool a small Czech company uses — does the chatbot say it is a machine, is the AI-made content labelled — repeated each time the rules or the regulator move." No brief or good_for existed before. Checked against the sources while writing. The date has passed and the copy says so: the transparency rules apply since 2 August 2026 [S3]. The dek's "bind every Czech firm putting AI in front of customers" was not carried over: the transparency duties are split between the makers and the users of an AI system, with exceptions, so the brief states what the rules require of a chatbot and of AI-made content rather than claiming every firm is bound [S3]. "No Czech regulator checks it yet" and "still a draft, past the EU's deadline" rest on the bill awaiting the government since June 2026 [S1], the law-firm reading of who it would appoint and what it would fine [S2] and the missed EU deadline for naming national AI authorities [S4]; they are true as of the record's last check of the bill page on 2026-08-25, and must be re-checked if the bill passes. The solution names no comparable abroad: the only one on file, Deeploy, sells a platform for high-risk AI systems, not this check [S5]. No score, status, source, note, marker or body sentence changed. Simplified for the front page: Title before: "Since August, chatbots in Czechia must say they are AI. No Czech regulator checks it yet." After: "Since August, chatbots in Czechia must tell customers they are AI". Brief before: "Since 2 August 2026, EU rules say a chatbot must tell customers it is a machine and AI-made content must be labelled [S3]. The Czech law naming who checks and fines firms is still a draft, past the EU's deadline [S1,S2,S4]." After: "AI-made content must now be labelled too [S3]. Yet the Czech law naming who checks and fines firms is still a draft, past the EU's deadline [S1,S2,S4]." Solution before: "Build an online check that finds the chatbots and AI-made content on a small firm's website and shows what must be disclosed or labelled." After: "Build an online check that scans a small firm's website for chatbots and AI-made content that must be disclosed." Good for before: "Someone who'd like to help small firms use AI within the new rules." After: "Someone who'd like to help small firms follow the new AI rules." "No Czech regulator checks it yet" moved from the headline into the brief, which keeps "still a draft" [S1,S2,S4]. The passed date stays passed ("since August") [S3]. No fact, number or claim was added; no score, status, source, note, marker in the body or body sentence changed. Same date, pain-point pass: title "Since August, chatbots in Czechia must tell customers they are AI" → "Czech firms must now say their chatbots are AI, and a draft law sets fines". Why: the old headline stated a duty with no one hurting and nothing at stake. The new one names the firms and the risk: the Czech adaptation bill carries turnover-scaled fines on the AI Act's model [S2], and the transparency duty applies since 2 August 2026 [S3]. "A draft law" because the bill still awaits the government [S1,S4], which the unchanged brief says. No score, status, source, note or body sentence changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on what the transparency rules require, with the draft Czech law, the missed EU deadline, the bill's origin in the industry ministry, its settled comments and the government plan's infringement flag as detail [S1,S2,S3,S4,S8]. Why now opens on the firm that can already break the rules, with the fine model, the 2 December 2026 marking deadline and the missing regulator as its three items, and the draft's four enforcers and the act's dates below as plain bullets [S2,S3,S4,S8]. Willing to pay answers that no Czech firm is known to have paid, and keeps who would buy and who is caught first [S3,S7]. Competition and Validated abroad describe each company by what it sells; every `locals[]` name and the one `comps[]` name left the body, and Trustpath, which is not on the ledger, stays named [S5,S6,S7]. `entry.why` became "Easier: … Harder: …" and no longer names a ledger company. The page items were cut to 14 words or fewer and the four Czech agency acronyms now carry their gloss after them. Detail added from sources already on file, none of it new evidence: the bill's short length and its hook into the market-surveillance law [S1,S4]; the data-protection office's areas, police, courts, elections and migration, and the lower fine ceiling for small firms [S2]; the act's 2025 dates, the 2 December 2026 grace period for marking existing tools' output, and the Digital Omnibus's May 2026 agreement [S3]; and Trustpath's product [S6]. Corrected against the sources rather than against the old sentences: "bind every Czech firm putting AI in front of customers" became what the rules require of a chatbot and of AI-made content, with the duties split between the makers and the users of AI, with exceptions, as the 2026-09-16 headline pass had already found [S3]; "Czech companies using AI, not the ones building it" now names the users as the buyers and says the makers carry duties of their own [S3]; and "firms selling systems the act calls high-risk buy readiness" became "face later deadlines", since no source on file shows anyone buying that readiness [S3]. Deeploy's platform is now said to cover high-risk systems, not the transparency check, as its source describes it [S5]. Flagged as inference: that no established seller holds the field rests on every direct seller's product being younger than three years, read from the ledger and from the duty's start date [S3,S7]; and "No Czech firm is known to have paid for this check" rests on no seller publishing a buyer count and no tender or grant being on file [S7]. Four source `why` lines were rewritten for plain words: S1 and S5 lost the MPO, RIA and EIC acronyms, S2 names the agencies in words, and S4 no longer says "the record". No `process` block was added: the problem is a new duty, and no source on file describes a workflow anyone runs today. No score, status, entry gate value, source, `note:`, `sources[]` order, title, brief, solution or good_for changed.

2026-09-19 · rescored to the 2026-09-19 ladders — `scores.urgency` 3 → 2, `score` 5 → 4, band FAIR → FAINT; `scores.money` stays 0. Urgency: the old 3 was the deadline sub-score 2 plus the retired freshness point. The trigger is the AI Act's transparency article, which has applied since 2 August 2026 [S3]. It is REAL: an EU regulation binds as published, and on file the duties fall on the users of AI as well as its makers [S3]. It is also CLOSE, applying 1.5 months before this date. TEETH is not met. The fines are in the Czech draft [S1,S2], which is not law. For a passed date the ladder needs enforcement within 12 months, and no Czech supervisor operates yet [S4]. On judgement call 5 in the worksheet, the chatbot half of the duty falls on the tool's maker, but the record's own reading of [S3] is that users of AI carry duties too. So REAL holds for part of this buyer and the score is 2, not 1. An enacted Czech law with its fines, or a first fine, would restore 3. Tags fixed: the draft bill [S1] and the law firm's analysis of it [S2] backed urgency by type, and a bill fails REAL. Both now carry `dims: []`, so the Why now count shows only the instruments behind the score [S3,S4]. Tagging pass for money: no source on file shows anyone paying for this check. The three direct sellers publish no price and no buyer count [S7], and no tender or grant for it is on file. No receipt was added, and money stays 0 on the same evidence as the worksheet. The notes on S1, S2, S3 and S8, which named the deadline sub-score or its ceiling, gained dated correction lines. Prose re-read against the new numbers: Why now says a firm can already break EU rules and a Czech draft sets fines, and names no fine levied. Willing to pay says no firm is known to have paid. Neither changed. One link under Willing to pay now reads Market gap instead of Competition. No other score, status, source order or body sentence changed.
