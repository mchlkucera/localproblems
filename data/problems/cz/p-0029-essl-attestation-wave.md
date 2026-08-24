---
id: p-0029
region: cz
title: Czech public bodies must run state-attested electronic records systems by 31 Dec 2026
  — non-attested products are already banned from sale to public bodies, and ~19 buyers re-procured
  eSSL in a single ten-week window
category: govtech
geo: CZ-national
score: 5
scores:
  proof: 0
  money: 2
  urgency: 3
  demand: 0
  gap: 0
status: candidate
build:
  capital: funded
  first_revenue: year-plus
  builder: funded-team
  note: 'The state atest is a per-product, per-version certification gate and every buyer procures publicly — payroll runs through attestation and tender cycles before first revenue.'
comps:
- name: Documaster
  url: https://www.documaster.com/
  geo: NO
  since: 2014
  traction: 'First records kernel certified by Norway''s National Archives (Noark); NOK 100M from Summa Equity; revenue >15x since 2017 (Summa)'
sources:
- type: regulation
  url: https://www.epravo.cz/top/clanky/dodani-elektronickeho-systemu-spisove-sluzby-po-172025-119824.html
  note: 'Attestation regime under §69b-e zákona č. 499/2004 Sb. (introduced by the DEPO amendment,
    z. č. 261/2021 Sb.): electronic records-management systems (eSSL) must hold a state atest
    — from 1 Jul 2025 suppliers may no longer offer non-attested products, and the transitional
    period for public-law originators (state organizational units, contributory organisations,
    state enterprises) to run attested systems ends 31 Dec 2026. Verified via legal commentary
    2026-08-13. Compliance date <18 months with the supply-side ban already in force: deadline
    sub-score 2.'
  date: '2026-12-31'
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/415250-2026
  note: 'ted-415250-2026: SÚKL ran an OPEN ~€1.4M competition for a records management system
    (Jun 2026) — open tender ≥5M CZK: money 2. It sits in a wave of ~28 records-management
    procurement records from ~19 distinct public buyers (~€17M) in the Jun–Aug TED window:
    SÚRAO published its certified-eSSL tender four times, Nemocnice Pardubického kraje three
    times, OZP twice — repeat publications signalling procedures that struggle to close.'
  date: '2026-06-17'
  signal: ted-415250-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/559572-2026
  note: 'ted-559572-2026: City of Prague awarded ~€3.3M for e-spis development incl. modules
    and training (Aug 2026), its third records-management award in the window — the large-buyer
    end of the same wave, purchasing development on the incumbent ICZ e-spis stack.'
  date: '2026-08-12'
  signal: ted-559572-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/535679-2026
  note: 'ted-535679-2026: Ministry of the Interior awarded ~€642k for records-management systems
    support 2025–2028 (Aug 2026) — a ministry-level buyer inside the same Jun–Aug window,
    and support (not just licence) spend, which is the recurring half of the bill.'
  date: '2026-08-03'
  signal: ted-535679-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/442243-2026
  note: 'ted-442243-2026: Ostravská univerzita awarded ~€408k for a records management system
    incl. service support (Jun 2026) — the university buyer type in the same wave.'
  date: '2026-06-29'
  signal: ted-442243-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/529246-2026
  note: 'ted-529246-2026: Czech State Forests (Lesy ČR) awarded ~€1.1M for an electronic records
    management system (Jul 2026) — the state-enterprise buyer type, and one of the larger
    single awards in the wave.'
  date: '2026-07-30'
  signal: ted-529246-2026
- type: tender
  url: https://ted.europa.eu/en/notice/-/detail/533101-2026
  note: 'ted-533101-2026: City of Prague awarded ~€275k for GINIS ENTERPRISE+ development incl.
    records management (framework, Jul 2026) — direct receipt that GORDIC''s GINIS stack is
    one of the incumbents the wave is being bought from, alongside ICZ e-spis.'
  date: '2026-07-31'
  signal: ted-533101-2026
created: '2026-08-13'
updated: '2026-08-24'
---

Every Czech public body runs a spisová služba — the legally mandated records-management layer beneath all official correspondence — and the state has now put a hard gate on the software that runs it: eSSL systems must pass state attestation, suppliers have been banned from offering or supplying non-attested products to public-law originators since 1 July 2025, and the transitional period for state organizational units, contributory organisations and state enterprises to operate attested systems ends 31 December 2026 [S1].

Why now: the procurement wave the deadline predicts is visible in the data. In a single June–August 2026 window, ~19 distinct public buyers generated ~28 TED records for records-management systems (~€17M) — SÚKL, ministries, hospitals, universities, insurance funds, state enterprises [S2,S4,S5,S6]. The friction is visible too: SÚRAO published its certified-eSSL tender four times and the Pardubice hospital group three times, the classic signature of procedures that fail to attract compliant bids and must be re-run against a fixed statutory clock [S2].

Who pays: twice over. Public bodies pay for migration, integration and support of attested systems — recurring public IT spend documented above threshold [S2,S3,S4], with the long tail of smaller organisations buying below TED's line of sight. Vendors pay for attestation itself [S1]: the atest is a per-product, per-version regulatory asset, which raises the cost of staying in the market and concentrates supply in the incumbents who can afford the cycle.

Existing non-solutions — and why no open local field is claimed: this is not an empty field. GORDIC (GINIS), ICZ (e-spis) and the other attested-product vendors dominate, and the wave is being bought from them [S3,S7]; the register does not pretend a greenfield product gap where strong incumbents are winning. The honest problem is narrower: a statutory deadline colliding with concentrated attested supply and repeat-failing tenders — a migration-capacity and procurement problem, with the attestation barrier itself defining who can compete.

No foreign analog is on file — attestation of records software this strict is a Czech construction — and no buyer-side complaint is yet on file. What would move this record: a documented count of bodies still running non-attested systems as the deadline approaches, or vendor-queue evidence that attestation and migration capacity cannot clear the 31 Dec 2026 wall.

## Revisions

2026-08-24 · fact check — The supply-side ban was stated one notch too widely: §69e bans offering or supplying non-attested eSSL to public-law originators ("zákaz nabízet nebo dodávat veřejnoprávním původcům"), not from sale generally — verified live on the S1 commentary, and title and lead now say so [S1]. The procurement-wave arithmetic was re-counted mechanically against the signal corpus on this date: ~30 matching records, 19 distinct buyers, SÚRAO with four publications and Nemocnice Pardubického kraje with three, as stated [S2].
