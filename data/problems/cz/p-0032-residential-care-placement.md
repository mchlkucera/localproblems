---
id: p-0032
region: cz
title: 'Czech families looking for a care-home bed apply to home after home, then wait'
solution: 'Build a placement service that finds free care-home beds and applies for families, as 2 companies already do in 2 other countries.'
brief: 'Every home keeps its own waiting list, so families put their parent on list after list [S4,S12]. By 2030 Czechia will have 690,000 people over 80, nearly half more than in 2023, so even more families will be searching [S7].'
good_for: 'Someone who''d like to work with care homes and families.'
price_search: 'Ask the admissions director of a private care-home chain what a filled bed is
  worth per move-in and what it pays per lead today, and ask SrovnejPéči.cz for its
  provider-listing price list; registr smluv full-text for "evidence žadatelů" or "volná místa"
  with "sociální služby" shows what Středočeský kraj paid for its regional vacancy database,
  the public manual equivalent of the live list; the MS2021+ index under "domov pro seniory"
  returns only construction and energy grants.'
category: health
geo: CZ-national
score: 8
scores:
  proof: 3
  money: 1
  urgency: 1
  demand: 2
  gap: 1
status: candidate
entry:
  level: easy
  buyer: small-firms
  permission: none
  incumbents: open
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed to place families, the work starts as phone calls to homes, not a system to plug into, and private homes and families buy without a tender. Harder: no Czech buyer is known to pay for placement yet, and a young Czech directory already lists more than 1,500 homes and could add free-bed data.'
comps:
- name: A Place for Mom
  url: https://www.aplaceformom.com/
  geo: US
  since: 2000
  traction: '$175M growth equity led by Insight Partners at a valuation above $1B (Businesswire,
    Jan 2022); largest US senior-care referral marketplace, provider-paid'
- name: Lottie
  url: https://lottie.org/
  geo: GB
  since: 2021
  traction: '$21M Series A led by Accel (PR Newswire, Oct 2023); 500,000+ monthly users;
    sells providers "Found by Lottie" occupancy software with real-time bed availability'
- name: pflege.de
  url: https://www.pflege.de/
  geo: DE
  since: 2011
  traction: 'VC-backed (Holtzbrinck Digital, Hanse Ventures, KfW et al.); ~10M visitors/yr
    (Carlsquare); acquired 100% by care-products group Paul Hartmann AG (announced Jan 2021)'
locals:
- name: SrovnejPéči.cz
  url: https://srovnejpeci.cz/
  since: 2024
  competes: direct
  maturity: early
  evidence: It sells provider-side listings on a family-facing comparison of more than 1,500 registered
    facilities, with reviews and prices, and forwards inquiries to the home [S12] — the same buyer
    and the same job, without the vacancy data or the application handling. It launched in 2024
    and publishes no count of families it has placed, so how much it moves is unknown.
- name: Můjdůchod.cz
  url: https://www.mujduchod.cz/
  competes: direct
  maturity: early
  evidence: It runs a static database of facilities for families to search themselves [S12] —
    the same job again, thinner, with no vacancy or queue data behind it. It publishes no start
    year and nothing names who pays for it, so whether it is a business at all is unclear.
- name: pece.cz
  url: https://www.pece.cz/
  competes: adjacent
  maturity: early
  evidence: 'It sells advice rather than placement: it counsels families and does not place them,
    alongside the free odborné sociální poradenství [S12]. No start year and no figures for how
    many families it advises are published.'
process:
  summary:
    today: 'A family searches directories that show no free beds, applies to home after home, and waits while each home keeps its own list [S4,S12].'
    after: 'One service keeps a live list of free beds, files the family''s applications and tracks each queue for them.'
  steps:
  - who: The family
    today: 'Searches directories with no free-bed data'
    known: documented
    cites: [12]
    change: changes
    after: 'Gets a shortlist of homes with free beds'
  - who: The family
    today: 'Applies to home after home'
    known: documented
    cites: [4]
    change: changes
    after: 'Signs once; the service files each application'
  - who: Each care home
    today: 'Keeps its own waiting list'
    known: documented
    cites: [4, 12]
    change: stays
    after: 'Unchanged: the service works with each home''s own list'
  - who: The family
    today: 'Waits with no sight of free beds'
    known: documented
    cites: [4, 12]
    change: changes
    after: 'The service tracks every queue for them'
  - who: '?'
    today: 'How a home picks from its list when a bed frees up is not known'
    known: unknown
    cites: []
    change: stays
    after: 'Unchanged: the service does not choose who moves in'
sources:
- type: arbitrage
  name: "A Place for Mom"
  gist: "the $175M US template"
  why: "The US template: a senior-care referral marketplace paid by providers per move-in, funded at $175M growth equity and valued above $1 billion."
  url: https://www.businesswire.com/news/home/20220123005094/en/A-Place-for-Mom-Raises-%24175M-in-Growth-Equity-Funding
  note: 'A Place for Mom raised $175M growth equity led by Insight Partners with General Atlantic
    and Silver Lake participating, Jan 2022, valuation stated above $1B. Business model: advisory
    service for families, paid by the provider network per placement. Announcement verified
    2026-08-25 (Businesswire release also carried by insightpartners.com and aplaceformom.com).'
  date: '2022-01-23'
- type: arbitrage
  name: "Lottie"
  gist: "the British occupancy-data marketplace"
  why: "The UK version, five years in: a care-home marketplace for families plus occupancy software that gives providers real-time bed availability — the data layer Czechia lacks."
  url: https://www.prnewswire.com/news-releases/lottie-raises-21m-series-a-led-by-accel-to-confront-the-social-care-crisis-and-elevate-the-standard-of-later-living-301949817.html
  note: 'Lottie raised $21M (£16.35M) Series A led by Accel with General Catalyst and Kindred
    Ventures, 2023-10-09. Marketplace comparing 4,000+ care homes and home-care services with
    transparent pricing; "Found by Lottie" SaaS manages enquiries, occupancy, billing and
    real-time bed availability for providers; 500,000+ monthly users, 300% YoY growth claimed
    in the release. Verified 2026-08-25.'
  date: '2023-10-09'
- type: arbitrage
  name: "pflege.de"
  gist: "the German platform, bought outright"
  why: "The German later-life care platform — VC-funded, ~10 million visitors a year, and bought outright by care-products group Paul Hartmann."
  url: https://www.pflegemarkt.com/2021/01/07/pflege-de-wird-uebernommen-von-paul-hartmann/
  note: 'pflege.de (web care LBJ GmbH, Hamburg, founded 2011) was acquired 100% by Paul Hartmann
    AG; Bundeskartellamt filing 2020-12-23, trade press 2021-01-07. Prior investors per the
    Carlsquare deal page: Holtzbrinck Digital, Hanse Ventures, Alstin, Schlutersche, Aschendorff,
    PDV Inter-Media Venture, KfW; ~10M visitors/yr. Funding totals are secondary-reported
    (Tracxn ~$14M) and are deliberately not asserted in the body. DE analog grounds proof 2;
    proof held below 3 because pflege.de is content-and-leads, not full placement navigation.'
  date: '2021-01-07'
- type: statistic
  name: "MPSV yearbook — unmet care-home applications"
  gist: "the 2024 unmet-application counts"
  why: "70,209 applications for domovy pro seniory and 37,849 for domovy se zvláštním režimem sat unsatisfied at the end of 2024 — a queue-pressure index inflated by families applying to many homes at once, never a headcount."
  url: https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv
  note: 'civic-mpsv-rocenka-neuspokojene-2024: Statistická ročenka 2024, workbook 5_Socialni
    sluzby.xlsx, tab. 5.9, Celkem ČR row, data k 31.12.2024: 70,209 DS + 37,849 DZR + 4,043
    DOZP neuspokojené žádosti. Families multi-apply BY DESIGN of the system, so this is a
    demand-pressure index only. The multi-applying itself is this record''s subject: it exists
    because no shared vacancy view does.'
  date: '2024-12-31'
  signal: civic-mpsv-rocenka-neuspokojene-2024
  dims: [demand]
- type: statistic
  name: "MPSV/ÚZIS long-term-care prediction"
  gist: "the 34,700 new beds by 2035"
  why: "The ministry's own models call for roughly 34,700 new long-term-care beds by 2035 — the queue problem gets structurally worse before it gets better."
  url: https://mpsv.gov.cz/predikce-potreb-dlouhodobe-pece-cesko-ceka-jeden-z-nejvetsich-ukolu-pristich-desetileti
  note: 'civic-mpsv-ltc-predikce-2035: MPSV/ÚZIS predictive models published 2025-11-14 project
    residential clients 93,536 (2024) → 135,624 (2035), beds 76,761 → 111,503 (~34,700 new);
    170,323 clients modelled by 2050. The ministry calls it one of the largest tasks of the
    coming decades.'
  date: '2025-11-14'
  signal: civic-mpsv-ltc-predikce-2035
  dims: [demand]
- type: complaint
  name: "Ombudsman — unregistered senior homes"
  gist: "the illegal-homes warning"
  why: "The deputy ombudsman warns families against live illegal care homes in three towns — the overflow from full registered capacity, documented by the state's own inspector."
  url: https://www.ochrance.cz/aktualne/dalsi_nelegalni_domovy_mohou_ohrozovat_dustojnost_i_bezpeci_senioru-_nesverujte_jim_sve_blizke_varuje_zastupce_ombudsmana/
  note: 'ombud-nelegalni-domovy: 2026-06-23, unregistered facilities operating in Mutěnice,
    Svitavy and České Budějovice; recurring inspections show structural shortage of registered
    long-term-care capacity pushing families to illegal providers. Demand point: families
    navigating a full system with no guidance end up in the worst corner of it.'
  date: '2026-06-23'
  signal: ombud-nelegalni-domovy
  dims: [demand]
- type: statistic
  name: "ČSÚ projection — the 80+ cohort"
  gist: "the 80+ cohort to 2030"
  why: "466,000 people aged 80+ on 1 January 2023 become 690,000 by 1 January 2030 — a 48% rise in seven years, in the middle variant of the state's own projection."
  url: https://csu.gov.cz/produkty/projekce-obyvatelstva-ceske-republiky-2023-2100
  note: 'Recomputed 2026-08-25 from the primary workbook rather than quoted: Tab. 1 Střední
    varianta (1301392301.xlsx, ages 80..100+ summed) gives 465,991 on 1.1.2023 and 690,376
    on 1.1.2030, +48.2%. Projection published 2023-11-30. Context receipt for the why-now;
    backs no score dimension on its own.'
  date: '2023-11-30'
  dims: []
- type: tender
  name: "TED — Brno Kociánka care-home concession (~5.17 bn CZK)"
  gist: "the 5.2bn CZK Brno concession"
  why: "Brno is procuring construction of a retirement home as a concession worth about 5.2 billion CZK — capacity money at a scale the register rarely sees."
  url: https://ted.europa.eu/en/notice/-/detail/754888-2025
  note: 'ted-754888-2025: Statutární město Brno, concession Kociánka, retirement home construction,
    5,171,175,000 CZK ≈ €206.8M (fixed 25 CZK/EUR conversion at ingest). Adjacent capacity spend,
    not budget for a placement product: money held at 1, not 2.'
  date: '2025-11-14'
  signal: ted-754888-2025
- type: tender
  name: "TED — Praha 14 senior-home concession (~4.37 bn CZK)"
  gist: "the 4.4bn CZK Praha 14 concession"
  why: "Praha 14 tendered a senior-home construction concession worth about 4.4 billion CZK in April 2026 — the second ten-figure capacity concession in six months."
  url: https://ted.europa.eu/en/notice/-/detail/244129-2026
  note: 'ted-244129-2026: Městská část Praha 14, concession for construction of a home for
    seniors, 4,373,000,000 CZK ≈ €174.9M (fixed conversion). With ted-754888-2025 and the
    Liblín build-and-operate tender ted-337152-2026 (€77.8M), the state side is demonstrably
    building beds while the family side stays unnavigated. Adjacent spend: money 1.'
  date: '2026-04-10'
  signal: ted-244129-2026
- type: subsidy
  name: "NPO call 31_24_138 — residential care modernization (1 bn CZK)"
  gist: "the closed 1bn CZK call"
  why: "The National Recovery Plan put a billion crowns into modernizing residential care for seniors — the second call of a series, now closed."
  url: https://mpsv.gov.cz/vyzva-c.-31_24_138-modernizace-a-rozvoj-pobytovych-sluzeb-socialni-pece-ii
  note: 'dotace-npo-31-24-138-pobytove-sluzby: call announced 2024-11-15, applications closed
    2025-06-30, allocation 1 bn CZK (May 2026 revision), grants 5–80M CZK. Closed: evidence of
    state investment into beds, not open money for a builder — money stays 1. Component
    allocation 9.5 bn CZK per the MPSV infrastructure page.'
  date: '2024-11-15'
  signal: dotace-npo-31-24-138-pobytove-sluzby
- type: regulation
  name: "New social services act planned for 2031"
  gist: "the 2031 rewrite of the rules"
  why: "MPSV is to draft a wholly new social services act by Q3 2028, with per-client funding from January 2031 — the market's rules are set to be rewritten."
  url: https://nrzp.cz/2026/03/02/informace-c-13-2026-uvahy-o-novem-zakone-o-socialnich-sluzbach/
  note: 'reg-soc-sluzby-novy-zakon-2031: legislative plan reported by NRZP ČR (informace
    č. 13-2026) from the government''s 2026 legislative intents — not enacted, dates can slip.
    Per-client funding, allowance valorization, multi-year provider financing. Dated trigger
    >18 months out; backs the window as context, not a compliance deadline.'
  date: '2026-03-02'
  signal: reg-soc-sluzby-novy-zakon-2031
- type: gap-check
  name: "Market scan — who places a Czech family"
  gist: "the Czech placement-market sweep"
  why: "Czech searches found comparison directories only — SrovnejPéči.cz (1,500+ facilities, inquiries forwarded, no vacancy data), můjdůchod.cz, one regional database — and no service that files applications, tracks queues or finds a bed."
  url: https://srovnejpeci.cz/
  note: 'Checked 2026-08-25: three Czech-language searches for placement services returned
    facility sites, job boards and directories. SrovnejPéči.cz (launched 2024) verified on its
    own site: comparison of 1,500+ registered facilities with reviews, prices and direct
    inquiries to providers — no application filing, no bed-finding, no real-time vacancy data;
    monetizes provider-side listings. Můjdůchod.cz is a static database; Středočeský kraj
    publishes a regional SENIOR vacancy database behind its portal; pece.cz and free odborné
    sociální poradenství advise but do not place. POSITIVE CONTROL passed first: the same
    method put Ringil — a register-confirmed CZ incumbent — at the top of its own Czech query.
    Own funded ledger grepped for CZ senior-care entrants: none (only cz-onsinch, event
    staffing, unrelated). Weak incumbents named, position empty: gap 2.'
  date: '2026-08-25'
  queries:
    - '"domov pro seniory" najít volné místo služba pomoc s umístěním rodina platforma'
    - 'srovnejpeci.cz srovnání domovů pro seniory'
    - 'služba "umístíme" seniora do domova poradce za poplatek vyřídíme žádosti domov pro seniory'
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-23'
- type: contract
  name: "Registr smluv — municipal senior-home construction wave"
  gist: "the municipal building wave"
  why: "Thirteen-plus municipal and regional senior-care construction contracts, amendments and grants landed between November 2025 and August 2026 — Prague's Bohnice pavilions alone at ~€10.8M — new beds being built one town at a time."
  url: https://smlouvy.gov.cz/smlouva/38020781
  note: 'hlidac-35713825: Praha signed ~€10.8M works for pavilions 3+4 of the Bohnice senior
    home (May 2026). The 2026-08-25 retrospective harvest carries a wave behind it: Trutnov''s
    R. Frimla expansion on its 3rd–6th amendment (~€4.8M; hlidac-34618133, -35453613, -35834233,
    -35868497), Litomyšl ~€8.8M (hlidac-36361600), Domov Luna Havířov ~€13.8M (hlidac-35024473),
    Domov ve Věži ~€4.1M (hlidac-35081745), Kralupy design documentation ~€1.8M (hlidac-36742246),
    and South Bohemia covering Domov Třeboňsko''s ineligible costs ~€5.6M (hlidac-33836861).
    Capacity-side context: backs no score point — money already rests on the concessions
    [S8,S9] and stays 1 (adjacent capacity spend, not placement budget).'
  date: '2026-05-14'
  signal: hlidac-35713825
  dims: []
- type: regulation
  name: "VeKLEP — social services act amendment in draft"
  gist: "the amendment already in draft"
  why: "MPs filed a bill amending the Social Services Act 108/2006 and the disability-benefits act, and the implementing decree 505/2006 is being updated — the rules of this market are moving before the planned 2031 rewrite."
  url: https://odok.cz/portal/veklep/material/ALBSDS9BKZY8/
  note: 'veklep-ALBSDS9BKZY8: MPs'' bill no. 125 (Juchelka, Pastuchová, filed 17 Mar 2026)
    amending zákon č. 108/2006 Sb. o sociálních službách and zákon č. 329/2011 Sb.; alongside
    it veklep-KORNDSFK3SWC updates implementing decree 505/2006 Sb. (comments incorporated,
    Mar 2026). Both drafts, no dated obligation: context receipts for the why-now, backing
    no score dimension — the 2031 rewrite [S11] remains the dated trigger on file.'
  date: '2026-03-17'
  signal: veklep-ALBSDS9BKZY8
  dims: []
created: '2026-08-25'
updated: '2026-09-02'
---

Czech families looking for a care-home bed apply to each home separately, because no shared list shows free beds [S4,S12].

- Each home runs its own applications and its own waiting list [S4,S12].
- Directories list the homes but show no free beds [S12].
- No Czech service files applications or tracks queues for a family [S12].

The homes in question are the domov pro seniory, the ordinary care home, and the domov se zvláštním režimem, the care home for people with dementia [S4].

- At the end of 2024, 70,209 applications to ordinary care homes and 37,849 to dementia care homes were still unmet [S4]. Another 4,043 applications to homes for people with disabilities were unmet too [S4].
- Those are applications, not people: families apply to many homes at once, as the system is built, so the counts measure pressure rather than a headcount [S4].
- In June 2026 the deputy ombudsman warned families against unregistered care homes operating in Mutěnice, Svitavy and České Budějovice [S6]. The office adds that the country lacks enough legally run services of this kind [S6].

Existing non-solutions: Czech directories list care homes, but none shows free beds or files applications for a family [S12].

Each one's name and details are in its row. What each does:

- One compares more than 1,500 registered facilities, with reviews and prices, and forwards a family's inquiry to the home [S12]. It launched in 2024, carries no free-bed data and places nobody [S12].
- A second is a static database of facilities for families to search themselves [S12].
- SENIOR (the Středočeský region's own vacancy list) covers that one region [S12].
- A private adviser and the free social counselling service advise families, but neither places them [S12].

Why now: Families already wait on list after list, and the number of people over 80 is projected to grow by nearly half by 2030 [S4,S7].

- Families apply to home after home, then wait, seeing no free beds [S4,S12].
- Unregistered care homes are operating, and the ombudsman warns families off them [S6].
- The labour ministry's models call for about 34,700 more long-term-care beds by 2035 [S5].

Behind those three items are the state's projections and the rules now being rewritten:

- The statistical office's middle projection puts 466,000 people aged 80 or over on 1 January 2023 and 690,000 on 1 January 2030, a 48% rise in seven years [S7].
- The labour ministry and the health-statistics institute modelled residential clients rising from 93,536 in 2024 to 135,624 in 2035, and beds from 76,761 to 111,503 [S5]. They model 170,323 clients by 2050, and the ministry calls it one of the largest tasks of the coming decades [S5].
- In March 2026 MPs filed a bill amending the social services act, No. 108/2006, and the disability-benefits act, and the decree that carries out the first was being updated at the same time [S14]. Both are drafts with no dated duty [S14].
- A wholly new social services act is planned, drafted by the third quarter of 2028, with funding that follows each client from January 2031 [S11]. It is not law yet, and its dates can slip [S11].

Who pays: Nobody is known to pay for placement in Czechia yet; abroad, care homes and providers pay for it [S1,S2].

- A Czech directory of more than 1,500 facilities sells listings to the homes [S12].
- In the US, care providers pay a referral service for each placement [S1].
- In Britain, care homes pay for software showing their free beds live [S2].

Whether Czech families would pay a fee for placement, or Czech homes a fee per move-in, is not known.

The public money nearby builds beds rather than finding them:

- Brno is procuring a retirement home as a concession worth about 5.2 billion CZK, published in November 2025 [S8].
- Praha 14, a Prague district, tendered a senior-home concession worth about 4.4 billion CZK in April 2026 [S9].
- Towns and regions signed at least 13 senior-care building contracts, amendments and grants between November 2025 and August 2026 [S13]. Prague's work on two pavilions of the Bohnice senior home alone came to about €10.8M in May 2026 [S13].
- The National Recovery Plan, the EU-funded recovery programme, put 1 billion CZK into modernising residential care in a call that closed on 30 June 2025, with grants of 5–80M CZK [S10]. The call is on the [tenders ledger](/signals/tenders#dotace-npo-31-24-138-pobytove-sluzby), where its successor will appear.

Solved elsewhere: Two established services abroad find families a care home, and a third, in Germany, sells leads and advice content [S1,S3].

In the US a referral service trading since 2000 advises families and is paid by the care providers for each placement [S1]. It raised $175M of growth equity in January 2022, led by Insight Partners with General Atlantic and Silver Lake, at a valuation above $1 billion [S1].

In Britain a marketplace founded in 2021 compares more than 4,000 care homes and home-care services with their prices, and sells homes software that manages inquiries, occupancy, billing and real-time bed availability [S2]. It raised a $21M Series A led by Accel in October 2023 and reports more than 500,000 users a month [S2].

In Germany a later-life care platform founded in Hamburg in 2011 draws about 10 million visitors a year [S3]. It publishes advice and passes on inquiries rather than placing families itself, and the care-products group Paul Hartmann bought all of it, announced in January 2021 [S3]. It is next door and fifteen years in [S3].

## First moves

1. Build the list nobody has: which care homes in one region have a bed coming free, and how long each home's waiting list is. Start from the state's register of social-care providers, then phone every ordinary and dementia care home in the region and write down its queue and when beds come free. Directories list the homes but not the free beds, and only one region publishes its own vacancy list; see [Competition](#competition). That list is the product.
2. Offer families in one region a flat fee to find their parent a place, file the applications and track the queues for them. Families today apply to home after home and wait, as [The opportunity](#opportunity) shows, and nobody does this for them. Open every conversation with the count of unmet care-home applications under [The opportunity](#opportunity), and say plainly that it counts applications, not people.
3. Sign up private care homes with beds to fill, paid by a fee for each family that moves in. That is how the US service is paid, and the British one also sells homes software showing their free beds; see [Validated abroad](#validated-abroad). Whether Czech homes will pay this way is not known yet, as [Willing to pay](#willing-to-pay) says, so ask the first homes directly.
4. Follow the public money that builds new care-home beds, because every bed it funds is a place to fill. Brno, Prague and other towns are building homes, and the last state modernisation call has closed; see [Willing to pay](#willing-to-pay). Watch for the next call and for new homes opening, and reach them before their beds are full.
5. Move before the Czech comparison site that forwards families' inquiries to homes adds free-bed data to its listings. It is young, but it already compares more than a thousand registered homes and sells them listings; see [Competition](#competition). Adding vacancies would give it the list from the first move, so build yours first and sign the homes it lists.

## Revisions

2026-08-25 · record created — Minted from the elder-care deep sweep (run 2026-08-24): demand from the MPSV yearbook queue statistics [S4] and capacity models [S5], money from the Brno and Praha 14 concessions [S8,S9] and the closed NPO call [S10], comparables verified against their funding announcements [S1,S2,S3]. The 80+ figures were recomputed from the primary ČSÚ workbook (Tab. 1, middle variant): 465,991 on 1 Jan 2023 → 690,376 on 1 Jan 2030, +48.2% [S7]. Unmet-application counts are stated as a multi-application pressure index throughout, never as persons waiting [S4]. Same date, separate pass: added the new optional `fix:` frontmatter field — one plain sentence naming what a builder would actually build — which the page renders directly under the dek, so the product answer arrives before the scorecard rather than three sections down. Scores, status, source notes and every [Sn] marker are untouched by that pass. Third pass this date, merged here: the 2026-08-25 retrospective harvest added the municipal construction wave — 13+ senior-care building contracts and grants Nov 2025–Aug 2026, led by Prague's Bohnice pavilions [S13] — and the pending legislative motion on the Social Services Act (MPs' bill 125 plus the decree 505/2006 update) [S14]. Both context; no score moved by that pass. Fourth pass this date, merged here: re-scored under the rewritten SCORING.md and its ESTABLISHED test, and the two dimensions moved in opposite directions to the same total. `scores.proof` 2 → 3. All three comparables pass the maturity test — A Place for Mom selling since 2000 on $175M of growth equity above a $1B valuation, Lottie since 2021 with a $21M Series A and 500,000 monthly users, pflege.de since 2011 at ~10M visitors a year and acquired outright by Paul Hartmann [S1,S2,S3] — established in three markets with Germany CEE-adjacent, which is rung 3. The [S3] note's reason for holding proof at 2, that pflege.de is content-and-leads rather than full placement navigation, was a judgment about product shape; the rewritten ladder measures maturity and market spread instead, and does not read product shape at all. That note is left exactly as written. `scores.gap` 2 → 1, a genuine de-rank on the same evidence. Rung 2 now means a check that found NO local player, and [S12] found three: SrovnejPéči.cz, Můjdůchod.cz and pece.cz, all lifted into a structured `locals[]` ledger and all early — SrovnejPéči.cz fails the three-year limb outright at two years old, and none of the three publishes a customer count, pairs with a public buyer in `data/lookup/cz-contract-parties.jsonl`, or carries a round or state listing. Rung 1, "local players exist but all EARLY, or only weak/legacy incumbents", is that exactly, and [S12]'s own note called them weak incumbents. Nothing about the opportunity changed: early players do not close a space, and the placement position [S12] looked for is still unoccupied. `score` unchanged at 8. The Středočeský kraj SENIOR portal was deliberately not lifted into `locals[]` — it is a regional public database, not a player — and stays named in the body. The non-solutions and Proven-abroad paragraphs now state ages rather than only funding, and first move 5 says how old the named competitor is. Money, urgency and demand untouched; no source note edited and no [Sn] marker moved. Same date, separate pass, merged here: First moves lightly rewritten in plain language (owner: "make the ideas simple") — "the data asymmetry is the product" and "sellable capacity" replaced with plain sentences; every [Sn] marker and link kept; scores untouched.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. SrovnejPéči.cz and Můjdůchod.cz stay `competes: direct` at `early`: both sell families the job of finding a facility, without the vacancy data, application filing or queue tracking that would finish it, and both fail the established test on their own receipts. pece.cz moves to `adjacent` — it counsels families and does not place them, sold beside the free odborné sociální poradenství, which is advice rather than the placement service this file describes. `scores.gap` stays 1, read literally: locals sell this and all of them are early. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 3 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

2026-09-02 · plain-language pass — The p-0010 retrofit run, applied here. GLOSSES: the SENIOR portal is now named as Středočeský kraj's own vacancy list at first use; MPSV is glossed in First moves as the labour and social affairs ministry; the two registered home types moved out of the opener and into First moves, where they are said in full — domov pro seniory and domov se zvláštním režimem, glossed as the ordinary and the dementia care homes — which retires the bare DS and DZR abbreviations the old First moves used. TIGHTENING: the argument went from 396 to 321 words with every [Sn] marker, figure, date, price and named company kept. What was cut was framing, not evidence: "the field is not empty so much as thinly held, and everything in it is young" (the sentences under it already say so, with dates), "both sides buy the same missing thing: knowing where a bed is" (the `fix:` line renders that four lines above), and the doubled geography in Proven abroad. The multi-application caveat on the 70,209 and 37,849 counts [S4] survives verbatim as the pressure-index reading this record has always required, and the Why-now block's three-marker sentence was split in two, so no rendered sentence now carries three citation markers. FIRST MOVES: rewritten verbs-first — Build, Sell, Sign, Watch, Move — move 3 lost its "Then", and move 5 no longer opens on the noun "Named competition:" but on the instruction, with SrovnejPéči.cz's two-year age and directory position behind it. SOURCES: a gist was added to all 14 entries, so each row renders as NAME · gist · date with its `why` sentence behind the more toggle; every entry already carried `name:` and `why:`, so none was written or changed. `score`, `scores`, `status`, `created`, `id`, `region`, `category`, `geo`, `fix:`, the `comps[]` and `locals[]` ledgers and every `sources[].note` are untouched. No [Sn] marker in the rendered body was moved, dropped or renumbered, and the only marker this pass wrote is the [S4] on the sentence above, inside this entry. `updated:` moved to 2026-09-02.

2026-09-16 · headline copy — The headline was rewritten for a general builder as three lines under the title: a `brief:` on what is happening and why it matters now, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "Czech families hunt home by home for a care-home bed"; brief: "Each home keeps its own waiting list, and no national list shows free beds [S12]. Czechs over 80 are projected to reach 690,000 by 2030 [S7]."; solution: "Build a placement service that phones care homes for free beds and applies for families, as companies already do abroad."; good_for: "Someone who'd like to work with care homes and families.". Previous title, verbatim: "Czech families place elderly relatives into care homes blind — every home runs its own queue, and nobody sells placement". Previous solution, verbatim: "A placement service for families: one live list of which care homes actually have a bed, applications filed on the family's behalf, paid for by the homes per move-in.". There was no previous brief or good_for. Rewritten from the agent draft, which predated the owner's framing rules, and cut to the owner's length limits. The 108,000 unmet applications at end-2024 are out of the copy: they count applications, not people, and families sit on several lists at once [S4], so the number would read as people waiting. "National" because Středočeský kraj runs a regional vacancy database and the directories on file carry no live vacancy data [S12]. 690,000 on 1 January 2030 is the statistical office's middle projection, from 466,000 in 2023 [S7]. Dropped: the old title's "nobody sells placement" (SrovnejPéči.cz and Můjdůchod.cz are early direct players [S12]); "paid per move-in", which no Czech receipt shows; the ombudsman line, which overstated [S6]. The closed 1bn CZK call and the 2031 act are not framed as upcoming. "As companies already do abroad" rests on A Place for Mom and Lottie [S1,S2]. No score, status, source, note, marker or body sentence changed. Same date, owner-approved final copy, written verbatim with only the [Sn] markers added. Title "Czech families hunt home by home for a care-home bed" became "Czech families looking for a care-home bed apply to home after home, then wait". Brief "Each home keeps its own waiting list, and no national list shows free beds [S12]. Czechs over 80 are projected to reach 690,000 by 2030 [S7]." became "Every home keeps its own waiting list, so families put their parent on list after list [S4,S12]. By 2030 Czechia will have 690,000 people over 80, nearly half more than in 2023, so even more families will be searching [S7]." Markers checked against the ledger: [S12] is the market scan finding only directories and one regional vacancy database, no shared list; [S4] is the ministry yearbook's 70,209 unmet care-home applications, which its note says are inflated by families applying to many homes at once by design. [S7] is the statistical office's middle projection, 465,991 people over 80 on 1 January 2023 and 690,376 on 1 January 2030, +48.2%, so "nearly half more" holds; it is a projection, which "will have" states more firmly than the source. "So even more families will be searching" is the owner's inference from that projection and is left as written. Solution "Build a placement service that phones care homes for free beds and applies for families, as companies already do abroad." became "Build a placement service that finds free care-home beds and applies for families, as 2 companies already do in 2 other countries." (owner: fill "do abroad" with "X companies do in Y countries"). The abroad count is taken from comps[] only: A Place for Mom (comps[0], geo US), an advisory placement service for families paid per placement [S1]; Lottie (comps[1], geo GB), a family marketplace with real-time care-home bed availability [S2]. Excluded: pflege.de (comps[2], geo DE), which this record's own [S3] note calls content-and-leads, not full placement navigation. Countries are where the two are based. good_for unchanged. No score, status, source, note or body sentence changed.

2026-09-18 · body rewritten to the writing rules, process figure added — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on families applying home by home, with the unmet-application counts, their applications-not-people caveat and the ombudsman's warning as detail [S4,S6]. Competition opens on directories without free beds and describes each `locals[]` player by what it does, leaving names and ages to the rows [S12]. Why now opens on the wait and the growing over-80s, with the bed models, the projection and the two social-services bills below the first three items [S4,S5,S6,S7,S11,S14]. Willing to pay says nobody is known to pay for placement here yet, lists what buyers pay abroad and the Czech directory's listings as its items, and holds the concessions, the building wave and the closed recovery-plan call as the public money nearby [S1,S2,S8,S9,S10,S12,S13]. Validated abroad became one answer sentence and three short paragraphs, one per `comps[]` company, without their names [S1,S2,S3]. The moves lost every [Sn] marker, figure and company name for links, and the tenders-ledger link moved from move 4 to the recovery-plan call under Willing to pay. `entry.why` was rewritten as "Easier: … Harder: …" [S12]. S14.why no longer says "this record". Detail added from sources already on file, none of it new evidence: the 4,043 unmet applications to homes for people with disabilities [S4], the client and bed models to 2035 and 2050 [S5], the ombudsman's three towns and its line that legal services are short [S6], the MPs' bill and decree update [S14], the 2028 drafting date [S11], the building wave [S13], the co-investors, Lottie's 4,000 compared services and its software, and pflege.de's Hamburg base and lead-passing model [S1,S2,S3]. Corrected against the sources rather than the old sentences: "private care homes and assisted-living operators pay per qualified move-in" rested on [S1], a US company, and no Czech receipt shows it, as the 2026-09-16 headline pass already found, so Willing to pay now says nobody is known to pay here yet; "families pay a flat fee for guided placement" had no source and is now the offer in move 2 and an open question in Willing to pay; free social counselling "helps with forms" is not in [S12], which says it advises and does not place; "some families end up in the unregistered homes" went further than [S6], whose release (read 2026-09-18) warns families not to entrust relatives to them and says legal services are short, so the item now says the homes operate and the ombudsman warns families off them; the recovery-plan call "just closed" in fact closed on 30 June 2025 [S10]; the old `entry.why` said homes pay per move-in and families pay a fee, which no Czech source shows, and that both directories are under three years old, though Můjdůchod.cz publishes no start year; and the old "three markets, three sellers" now says the German platform sells leads and advice content, as its [S3] note records. Flagged as inference: "because no shared list shows free beds" in the opening sentence is the [S4] note's reading of why families apply many times; "could add free-bed data" in `entry.why` and move 5 rests on the directory already comparing the homes and forwarding inquiries [S12]; and "fifteen years in" is 2011 counted to 2026 [S3]. The new `process` block draws the family searching directories [S12], applying home by home [S4], each home keeping its own list [S4,S12] and the wait [S4,S12], with every step phrase 4–8 words; how a home picks from its list when a bed frees up is marked unknown. The coordinator may add p-0032 to `PROCESS_PHRASE_ENFORCED`. No score, status, source, `note:`, `sources[]` order, title, brief, solution or good_for changed.
