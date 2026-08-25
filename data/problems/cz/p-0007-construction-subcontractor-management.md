---
id: p-0007
region: cz
title: Czech contractors source subcontractor crews through Facebook groups and brokers and
  run their payroll on generic legacy software, with no vetting or compliance layer for the
  crews they hire
category: housing
geo: CZ-national
score: 5
scores:
  proof: 2
  money: 0
  urgency: 1
  demand: 1
  gap: 1
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'A vetted-crew matching wedge with compliance-document handling is a CoCrafter-shaped
    small-team build, though two-sided liquidity and any payroll expansion press the top
    of the garage band.'
comps:
- name: CoCrafter
  url: https://www.cocrafter.com/
  geo: DE
  since: 2023
  traction: '€1.7M pre-seed — YC, 10x Founders (Crunchbase); 3,000+ German SMB construction companies on the marketplace'
  signal: yc-cocrafter
- name: Hammr
  url: https://www.hammr.com/
  geo: US
  since: 2023
  traction: 'YC W23, 10-person team (YC, 2026); company reports ~$5M raised from YC and Soma Capital (Work at a Startup)'
  signal: yc-hammr
- name: conmeet
  url: https://conmeet.io/
  geo: DE
  since: 2023
  traction: '€6M seed — Reimann Investors, Smedvig (Tech.eu, Aug 2026) after €1.3M pre-seed (EU-Startups, Feb 2026)'
  signal: de-conmeet
- name: Lumber
  url: https://www.lumberfi.com/
  geo: US
  since: 2023
  traction: '$21M total — $15.5M Series A led by Foundation Capital (PRNewswire, 2025); construction payroll, time and insurance'
sources:
- type: arbitrage
  name: "CoCrafter"
  why: "Munich B2B marketplace matching general contractors with vetted subcontractors, foreign-crew sourcing and compliance documents included — 3,000+ German SMB construction firms on it."
  url: https://www.ycombinator.com/companies/cocrafter
  note: 'yc-cocrafter: CoCrafter (YC W24, Munich) — B2B marketplace matching GCs with vetted
    subcontractors incl. foreign-crew sourcing and compliance docs; 3,000+ German SMB companies
    onboard. Funded DE analog, no CZ B2B equivalent found.'
  date: '2026-08-13'
  signal: yc-cocrafter
- type: arbitrage
  name: "Hammr"
  why: "'Rippling for construction' (YC W23) — construction-specific payroll, HR and compliance, which is the second half of this problem, funded in the US."
  url: https://www.ycombinator.com/companies/hammr
  note: 'yc-hammr: Hammr (YC W23, US) — construction-specific payroll, HR and compliance (''Rippling
    for construction''). No CZ construction-vertical payroll/compliance product found; only
    generic payroll (Vema, Pamica) and site tools (Stavario).'
  date: '2026-08-13'
  signal: yc-hammr
- type: gap-check
  name: "First Czech market scan"
  why: "Czech construction-tech lists showing only consumer marketplaces and generic payroll, plus the documented informal sourcing of Ukrainian and Balkan crews through Facebook groups and brokers."
  url: https://www.ycombinator.com/companies/cocrafter
  note: 'Absence checks 2026-08-13: Tracxn CZ construction-tech lists and searches show no
    B2B subcontractor marketplace (only consumer marketplaces Wilio, Nejřemeslníci) and no
    vertical payroll. Demand point: signals document chronic labor shortage and informal Ukrainian/Balkan
    crew sourcing via Facebook groups and brokers with zero vetting.'
  date: '2026-08-13'
- type: arbitrage
  name: "conmeet"
  why: "Munich, €6M seed in August 2026 for an AI operations system covering procurement to invoicing at 10–500-employee trades and construction firms — German money on construction back-office software."
  url: https://tech.eu/2026/08/05/conmeet-raises-eur6m-to-power-construction-businesses-with-ai/
  note: 'de-conmeet: conmeet (Munich) raised €6M seed (5 Aug 2026) for an AI-native ops OS
    for 10–500-employee trades/construction firms — procurement to invoicing. Reinforces DE
    validation of construction-firm back-office software; CZ partial incumbent remains Stavario
    (site diary/attendance only).'
  date: '2026-08-05'
  signal: de-conmeet
- type: gap-check
  name: "Bildix and the Czech near-misses"
  why: "Bildix runs a contractor's whole internal operation but does no crew sourcing, vetting or payroll; NejStav and ePoptávka are lead generation, and PlanRadar tenders only to subcontractors already on a live project."
  url: https://bildix.app/
  note: 'Gap re-check 2026-08-20: looked for (a) a Czech B2B marketplace matching general
    contractors with vetted subcontractor crews and (b) a construction-vertical payroll or
    posted-worker-compliance product. NEITHER FOUND, and the near-misses are all off-target.
    The B2B construction platforms Czech search returns are lead-generation for investor or
    homeowner demand — NejStav.cz, ePoptávka, Poptávka-EU, B2Bpoptavka — the same class as the
    Wilio/Nejřemeslníci consumer marketplaces this record already names, not GC-to-crew
    matching with document vetting. Subcontractor tendering does exist inside project software,
    but as a feature of PlanRadar, an Austrian vendor that entered the CZ market in spring 2025,
    and only toward subcontractors already on a live project. The closest Czech player is
    Bildix (CVF Group, s.r.o., Prague) — "Jedna platforma pro celou realizační firmu": leads,
    quotes, projects, service, purchasing, grant admin and cashflow with iDoklad and Pohoda
    integration. That makes Bildix a stronger CZ analog of conmeet than Stavario is, and it is
    named here for that reason, but it is an internal ops platform: no crew sourcing, no
    vetting, no payroll, no A1/posted-worker handling. On payroll, Czech search returns only
    horizontal vendors (Vema, Alfa-soft, M3P3) plus construction software that is budgeting or
    scheduling (RTS Stavitel+) or site diary and attendance (Stavario, STAVEE, Stavar.io,
    Buildary) — none of them pay a crew. NOTHING MOVED: `scores.gap` stays 1 and `score` stays
    5. Searching and not finding is not the same as absence, and this pass has no authority to
    raise a gap score on a negative.'
  date: '2026-08-20'
  queries:
    - "marketplace subdodavatelé stavební firmy ověřené party poptávka B2B platforma Česko"
    - "platforma pro shánění part na stavbu generální dodavatel subdodavatelé ověření dokladů startup"
    - "software mzdy docházka pro stavební firmy party na stavbě vysílání pracovníků A1"
    - "mzdový software specializovaný pro stavebnictví výplaty dělníků stavební firmy vertikální"
    - "český startup stavebnictví nedostatek dělníků zprostředkování ukrajinských part software 2026"
  checked: [google-cz, own-funded-ledger]
  expires: '2026-11-18'
created: '2026-08-13'
updated: '2026-08-20'
---

Czech construction (~400k employed) is subcontractor-driven and chronically short of labor [S1,S2]. General contractors source Ukrainian and Balkan crews informally — Facebook groups and brokers — with no vetting, document checking or compliance tooling [S3]; the same firms then run payroll for multi-site crews, agenturní zaměstnávání and A1/posted-worker compliance on generic legacy software (Vema, Pamica) or through external accountants [S2]. Two ends of one problem: finding compliant crews and paying them correctly.

Why now: in Germany — a structurally similar subcontractor market — CoCrafter (YC W24) has 3,000+ SMB companies on its vetted GC-subcontractor marketplace, showing the informal sourcing layer can be productized [S1].

Who pays: general contractors and mid-sized stavební firmy — the marketplace side monetizes matching and compliance document management; the payroll side is per-employee SaaS replacing accountant hours and compliance risk. Entry through either wedge lands in the same buyer.

Existing non-solutions: consumer home-services marketplaces (Wilio, Nejřemeslníci) that do not serve B2B crews [S3], site-diary and attendance tools (Stavario, PlanRadar) that stop short of pay and compliance, and generic payroll software [S2,S4]. Searches on 2026-08-13 found no Czech B2B subcontractor marketplace and no construction-vertical payroll product [S3].

Solved elsewhere: CoCrafter (DE) for sourcing [S1] and Hammr (US, YC W23) for construction payroll/HR [S2]. Each facet of the merged problem is validated in only one market so far.

## Revisions

2026-08-20 · evidence audit and title sweep — Two blocks recorded on this date, merged here. The "Why now" trend sentence was removed: the claims that the labour shortage keeps worsening, that foreign-crew usage keeps rising, and that posted-worker compliance exposure grows with them. No signal in the corpus carries a trajectory for any of the three — yc-cocrafter and yc-hammr document a chronic shortage and informal Ukrainian/Balkan sourcing at a single point in time, with no second data point behind any of the three verbs. The lead-in now carries the German productization receipt, which is sourced. The title claimed "no vetting, compliance or construction-specific tooling". The first two stand — the 2026-08-20 gap check searched five surfaces and found no crew-vetting or construction payroll product [S5]. The third did not: Bildix is Czech construction-specific tooling, named on this record, and it simply does not do crew sourcing. Narrowed to what the check actually supports.
