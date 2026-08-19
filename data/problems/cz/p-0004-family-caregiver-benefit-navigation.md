---
id: p-0004
region: cz
title: Families caring for ~380,000 dependent Czechs must obtain and defend příspěvek na péči
  through an opaque, bureaucratic process with no help beyond static info portals
category: health
geo: CZ-national
score: 6
scores:
  proof: 1
  money: 1
  urgency: 1
  demand: 1
  gap: 2
status: candidate
build:
  capital: kiosk
  first_revenue: weeks
  builder: small-team
  note: 'A guided claim-and-appeal tool over public MPSV rules is solo-dev cheap and families
    pay flat or success fees immediately, but credible hodnocení stupně závislosti guidance
    needs a social-benefits practitioner alongside the dev.'
comps:
- name: Oma Care
  url: https://www.omacare.com/
  geo: US
  since: 2024
  traction: 'YC W24, 2-person team (YC, 2026); automates enrolment in US Medicaid programs paying family caregivers up to $28/hr'
  signal: yc-oma-care
- name: Givers
  url: https://www.givers.com/
  geo: US
  since: 2021
  traction: '$3.5M seed led by CRV (Forbes, 2023); app used by 15,000 caregivers/month (Forbes, 2026)'
- name: KareHero
  url: https://www.karehero.com/
  geo: GB
  since: 2022
  traction: 'company raise undisclosed (Tracxn, 2025); £9M+ care funding unlocked for families, avg £27k each (company, 2026); employer channel'
sources:
- type: arbitrage
  url: https://www.ycombinator.com/companies/oma-care
  note: 'yc-oma-care: Oma Care (YC W24) builds infrastructure to train and get family caregivers
    paid (53M caregivers in the US); CareOasis (YC S23) is the same model — a validated US
    cluster. US-only, scored as one analog.'
  date: '2026-08-13'
  signal: yc-oma-care
- type: subsidy
  url: https://www.ycombinator.com/companies/oma-care
  note: Signal note references příspěvek na péči — four levels, raised again in 2024-25, flowing
    to ~380k dependent persons — the state benefit program the product would help families
    access.
  date: '2026-08-13'
- type: gap-check
  url: https://www.ycombinator.com/companies/oma-care
  note: 'Absence check 2026-08-13: searches return only advice articles and government pages
    (pece.cz, mpsv.gov.cz); no player that files, tracks or optimizes claims for families.
    Demand point: signal documents that application, hodnocení stupně závislosti and appeals
    are bureaucratic and opaque.'
  date: '2026-08-13'
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/402149-2026
  note: 'ted-402149-2026 (context): MPSV ''IT delivery III'' framework ~€74.7M plus a dozen
    related awards (EKIS III ~€19.8M open, OKaplikace ~€65M) in Jun–Aug 2026 — the state demonstrably
    budgets tens of millions EUR/yr for benefits back-office IT while the citizen-facing navigation
    layer stays unbuilt. Adjacent spend: kept at money=1, not 2.'
  date: '2026-06-11'
created: '2026-08-13'
updated: '2026-08-19'
---

Roughly 380,000 dependent persons in Czechia receive příspěvek na péči, and the care it funds is largely delivered informally by family members. To get the benefit — and the correct level of it — families must navigate the application, the hodnocení stupně závislosti assessment, and frequently appeals, in a process the yc-oma-care signal characterizes as bureaucratic and opaque. Families that misnavigate it leave state money on the table while providing the care anyway.

Why now: benefit levels were raised again in 2024-25, increasing the money at stake per claim, while the navigation layer remains nonexistent. Demographic aging steadily grows the claimant pool.

Who pays: families themselves (success-fee or flat-fee claim assistance, subscription support and caregiver training), analogous to how Oma Care monetizes caregiver enablement in the US. Downstream, home-care providers and insurers are plausible channel partners since properly funded clients can afford services.

Existing non-solutions: static information portals (pece.cz, mpsv.gov.cz guides) and word-of-mouth from social workers. The 2026-08-13 absence check found no Czech company that files, tracks or optimizes claims for families.

Solved elsewhere: Oma Care (YC W24) and CareOasis (YC S23) form a validated US cluster around getting family caregivers trained and paid from state programs. Arbitrage scored 1 because validation is US-only; the money point reflects the příspěvek na péči program explicitly referenced in the signal note.

---
**CORRECTION (2026-08-13, post-run fact check):** The recipient figure should read **374,000 (Dec 2024, ČSÚ/MPSV)** — 41.3 bn CZK paid in 2024. The ~380k figure in this record is slightly above the latest confirmed official number. Sources: https://csu.gov.cz/produkty/prispevek-na-peci-loni-vyuzivalo-vice-nez-370-tisic-lidi
