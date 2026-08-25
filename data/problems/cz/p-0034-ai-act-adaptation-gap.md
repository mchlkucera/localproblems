---
id: p-0034
region: cz
title: Czech firms run live EU AI transparency duties with no national supervisor yet
fix: A fixed-price AI-inventory and Article 50 transparency audit for Czech SME deployers,
  kept current as the adaptation act lands and ČTÚ enforcement starts.
category: legal-compliance
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
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Fixed-price AI-inventory and Art 50 audits sell as a service today, but a product
    must displace PwC''s tooling, cheap scanners like AIshield and Czech-language modules
    like Brain — the differentiator is the CZ enforcement layer once ČTÚ starts acting.'
comps:
- name: Deeploy
  url: https://deeploy.ml/
  geo: NL
  since: 2020
  traction: 'up to €7.5M EIC blended finance for AI-act-aligned MLOps (Silicon Canals, Feb
    2025), after a €2.5M round (Tech.eu, Jun 2023)'
  signal: round-deeploy
sources:
- type: regulation
  name: "VeKLEP — návrh zákona o umělé inteligenci (MPO)"
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
created: '2026-08-25'
updated: '2026-08-25'
---

Since 2 August 2026, the EU AI Act's transparency tier applies to every Czech firm deploying AI toward customers: chatbots must disclose they are machines and synthetic content must be labeled [S3]. The Czech law that would say who enforces this is still a draft — the MPO adaptation bill cleared interministerial comments in June 2026 and awaits the government [S1,S2], and Czechia missed the EU deadline for designating its national AI authorities [S4].

Why now: obligations are in force while supervision is not. The draft hands general AI oversight to ČTÚ, financial-sector AI to ČNB and sensitive high-risk systems to ÚOOÚ, with AI-Act-scaled fines and a sandbox at ČAS [S2]. The Digital Omnibus moved the high-risk deadlines to December 2027 and August 2028 [S3] — so transparency duties are the wave that is already here, and the enforcement machinery arrives mid-wave.

Who pays: deployers first — Czech SMEs running chatbots and generative AI in customer contact hit Article 50 before anything else [S3]. Providers of high-risk systems buy conformity preparation against the 2027–28 clocks [S3]. No Czech tender or grant is attached on file, so money scores 0.

Existing non-solutions: the field is already forming. PwC ČR sells an AI Compliance Tool in Czech, AIshield.cz sells a self-serve exposure scan, Brain sells Czech-language compliance modules, and Adastra and Seyfor sell the advisory tier [S7]. Occupied — gap 0 with incumbents named.

Solved elsewhere: Deeploy (Utrecht) took up to €7.5M in EIC blended finance for an MLOps platform built on the AI Act's explainability duties [S5]. Trustpath (Croatia, Credo Ventures pre-seed) sells EU AI Act vendor-compliance tooling one market over [S6].

## Revisions

2026-08-25 · record created — Minted from the first VeKLEP harvest (198 legislative drafts, run 2026-08-25): the MPO adaptation bill supplies the Czech state's own problem definition [S1], with competences and sanctions receipted from law-firm analysis [S2] and EU application dates from the ledger [S3]. The gap check found the Czech compliance field already occupied (PwC, AIshield, Brain), so the record is born watching at gap 0 [S7]; proof held at 1 despite funded EU analogs [S5,S6] for the same reason.
