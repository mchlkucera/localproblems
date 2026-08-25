---
id: p-0032
region: cz
title: Czech families place elderly relatives into care homes blind — every home runs its
  own queue, and nobody sells placement
category: health
geo: CZ-national
score: 8
scores:
  proof: 2
  money: 1
  urgency: 1
  demand: 2
  gap: 2
status: candidate
build:
  capital: kiosk
  first_revenue: weeks
  builder: small-team
  note: 'A directory is cheap to build; the moat is live vacancy and queue data kept fresh
    by phone-and-relationship work across hundreds of homes, plus a social-care practitioner
    for credible guidance — operations discipline more than engineering.'
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
sources:
- type: arbitrage
  name: "A Place for Mom"
  why: "The US template: a senior-care referral marketplace paid by providers per move-in, funded at $175M growth equity and valued above $1 billion."
  url: https://www.businesswire.com/news/home/20220123005094/en/A-Place-for-Mom-Raises-%24175M-in-Growth-Equity-Funding
  note: 'A Place for Mom raised $175M growth equity led by Insight Partners with General Atlantic
    and Silver Lake participating, Jan 2022, valuation stated above $1B. Business model: advisory
    service for families, paid by the provider network per placement. Announcement verified
    2026-08-25 (Businesswire release also carried by insightpartners.com and aplaceformom.com).'
  date: '2022-01-23'
- type: arbitrage
  name: "Lottie"
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
  why: "Brno is procuring construction of a retirement home as a concession worth about 5.2 billion CZK — capacity money at a scale the register rarely sees."
  url: https://ted.europa.eu/en/notice/-/detail/754888-2025
  note: 'ted-754888-2025: Statutární město Brno, concession Kociánka, retirement home construction,
    5,171,175,000 CZK ≈ €206.8M (fixed 25 CZK/EUR conversion at ingest). Adjacent capacity spend,
    not budget for a placement product: money held at 1, not 2.'
  date: '2025-11-14'
  signal: ted-754888-2025
- type: tender
  name: "TED — Praha 14 senior-home concession (~4.37 bn CZK)"
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
created: '2026-08-25'
updated: '2026-08-25'
---

Placing a parent into a Czech care home means applying blind. Each domov pro seniory or domov se zvláštním režimem runs its own application and its own queue; no shared view of vacancies exists. Homes held 70,209 and 37,849 pending applications at the end of 2024 — a pressure index inflated by families applying to many homes at once, not a count of waiting people [S4]. Desperate families end up in unregistered homes the ombudsman warns against [S6].

Why now: the 80+ population grows from 466,000 to 690,000 between 2023 and 2030 [S7], and the ministry's own models call for roughly 34,700 new long-term-care beds by 2035 [S5]. The state is building — Brno and Praha 14 tendered care-home concessions worth 5.2 and 4.4 billion CZK [S8,S9], a 1 bn CZK modernization call just closed [S10] — and a new social-services act with per-client funding is planned for 2031 [S11].

Who pays: private care homes and assisted-living operators pay per qualified move-in — the provider-paid referral model A Place for Mom runs at national scale in the US [S1]. Families pay flat fees for guided placement — shortlisting, filing, queue tracking. Both sides buy the same missing thing: knowing where a bed is.

Existing non-solutions: directories exist, placement does not. SrovnejPéči.cz, launched 2024, compares more than 1,500 registered facilities and forwards inquiries, but carries no vacancy data and places nobody [S12]. Můjdůchod.cz is a database; regional lists like Středočeský kraj's SENIOR portal cover one region each; free social counselling helps with forms [S12]. No Czech service files applications, tracks queues or finds an available bed for a family [S12].

Solved elsewhere: A Place for Mom (US) raised $175M in growth equity at a valuation above $1 billion on provider-paid senior-care referral [S1]. Lottie (GB) raised a $21M Series A led by Accel for a family-facing marketplace plus occupancy software that tracks real-time bed availability for providers [S2]. pflege.de (DE) built the German later-life platform and was bought outright by care-products group Paul Hartmann [S3].

## First moves

1. Build the vacancy dataset nobody has: start from the MPSV register of providers, then phone-survey every DS and DZR in one pilot kraj for live queue length and expected openings — the data asymmetry is the product.
2. Sell families first: flat-fee guided placement (shortlist, applications filed, queues tracked) in the pilot region, with the yearbook's 70,209 pending applications [S4] as the opening fact of every conversation.
3. Sign private homes with sellable capacity onto per-move-in referral fees — the A Place for Mom model [S1] — and offer them the occupancy tooling Lottie proved providers buy [S2].
4. Watch the successor to the closed 1 bn CZK modernization call [S10] on the [tenders ledger](/signals/tenders#dotace-npo-31-24-138-pobytove-sluzby): every funded bed is new inventory.
5. Named competition: SrovnejPéči.cz [S12] — it owns the directory position and could add vacancy data; move before it does.

## Revisions

2026-08-25 · record created — Minted from the elder-care deep sweep (run 2026-08-24): demand from the MPSV yearbook queue statistics [S4] and capacity models [S5], money from the Brno and Praha 14 concessions [S8,S9] and the closed NPO call [S10], comparables verified against their funding announcements [S1,S2,S3]. The 80+ figures were recomputed from the primary ČSÚ workbook (Tab. 1, middle variant): 465,991 on 1 Jan 2023 → 690,376 on 1 Jan 2030, +48.2% [S7]. Unmet-application counts are stated as a multi-application pressure index throughout, never as persons waiting [S4].
