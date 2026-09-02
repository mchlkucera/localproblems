---
id: p-0029
region: cz
title: Czech public bodies must replace their records systems by the end of 2026
category: govtech
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 2
  urgency: 3
  demand: 0
  gap: 0
status: watching
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
locals:
- name: GORDIC (GINIS)
  url: https://www.gordic.cz/
  ico: '47903783'
  since: 1993
  competes: direct
  maturity: established
  evidence: It sells GINIS, which holds the state records attest 1/2025, valid to 25 November
    2027 and extended to version 5.26 [S8]. Trading since 1993, and three separate public bodies
    buy from it on the state contracts register — MČ Praha 20 and two Hradec-region secondary
    schools [S8].
- name: ICZ.DMS (e-spis)
  url: https://www.i.cz/
  ico: '06696805'
  since: 2017
  competes: direct
  maturity: established
  evidence: It sells e-spis, which holds the state records attest 2/2026, running 7 May 2026 to
    7 May 2028 [S8]. Prague awarded it about €3.3M for e-spis development in August 2026 [S3];
    ICZ.DMS a.s. has traded since 21 December 2017.
- name: Seyfor (ELDAx)
  url: https://www.seyfor.cz/
  ico: '01572377'
  since: 2013
  competes: direct
  maturity: established
  evidence: It sells ELDAx, which holds the state records attest 3/2026, extended to version 6.0.1
    [S8]. Trading since 2013, with město Krnov and Psychiatrická nemocnice v Kroměříži among its
    public buyers on the state contracts register [S8].
- name: MIT Consulting (MIT ERMS)
  url: https://www.mitconsulting.cz/
  ico: '25689240'
  since: 1998
  competes: direct
  maturity: established
  evidence: It sells MIT ERMS, which holds the state records attest 4/2026, running 22 July 2026
    to 22 July 2028 [S8]. Trading since 31 August 1998.
- name: GEOVAP
  url: https://www.geovap.cz/
  ico: '15049248'
  since: 1991
  competes: direct
  maturity: established
  evidence: It sells a records system into exactly this wave, and two separate public bodies buy
    from it on the state contracts register — statutární město Karviná and Ředitelství silnic
    a dálnic [S8]. Trading since 26 February 1991, but its system is not on the state's list of
    attested products at this check, so it sells into the deadline without the certificate the
    four attested vendors hold.
- name: T-MAPY (TESS Online)
  url: https://www.tmapy.cz/
  ico: '47451084'
  competes: direct
  maturity: early
  evidence: It sells TESS Online, a Czech records system, into exactly this wave — but it is not
    on the state's published list of attested products at this check [S8], so as it stands it
    cannot be offered to a public body from 1 January 2027. No start year and no count of offices
    running it are published, so its size is unknown.
- name: OSS Alliance
  url: https://ossalliance.cz/
  competes: direct
  maturity: early
  evidence: It gives the smallest towns an open-source records system free of charge, with two
    years of hosting, in cooperation with the Ministry of the Interior [S8] — the same product
    to the same buyer at a price of zero, which is why it competes directly. No year for the start
    of supply is published, so how long it has been running is unknown; a zero-price rival at
    the bottom of the market all the same.
sources:
- type: regulation
  name: "The eSSL attestation regime (§69b–e, Act 499/2004)"
  gist: "the attestation law"
  why: "Legal commentary on the gate: since 1 July 2025 suppliers may not offer non-attested records systems to public-law originators, and the transitional period for those bodies runs out at the end of 2026."
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
  name: "TED — SÚKL records system (~€1.4M), and the wave around it"
  gist: "the €17M tender wave"
  why: "An open competition by the state drug agency, inside ~28 records-management procurement records from ~19 distinct public buyers (~€17M) in ten weeks — with SÚRAO republishing four times."
  url: https://ted.europa.eu/en/notice/-/detail/415250-2026
  note: 'ted-415250-2026: SÚKL ran an OPEN ~€1.4M competition for a records management system
    (Jun 2026) — open tender ≥5M CZK: money 2. It sits in a wave of ~28 records-management
    procurement records from ~19 distinct public buyers (~€17M) in the Jun–Aug TED window:
    SÚRAO published its certified-eSSL tender four times, Nemocnice Pardubického kraje three
    times, OZP twice — repeat publications signalling procedures that struggle to close.'
  date: '2026-06-17'
  signal: ted-415250-2026
- type: tender
  name: "TED — City of Prague, e-spis development (~€3.3M)"
  gist: "the €3.3M Prague award"
  why: "Prague's third records-management award in the window, buying development on the incumbent ICZ e-spis stack — the large-buyer end of the same wave."
  url: https://ted.europa.eu/en/notice/-/detail/559572-2026
  note: 'ted-559572-2026: City of Prague awarded ~€3.3M for e-spis development incl. modules
    and training (Aug 2026), its third records-management award in the window — the large-buyer
    end of the same wave, purchasing development on the incumbent ICZ e-spis stack.'
  date: '2026-08-12'
  signal: ted-559572-2026
- type: tender
  name: "TED — Ministry of the Interior, records support 2025–2028 (~€642k)"
  gist: "the €642k support contract"
  why: "A ministry buying multi-year support rather than a licence — the recurring half of the bill, and the buyer type at the top of the obligated population."
  url: https://ted.europa.eu/en/notice/-/detail/535679-2026
  note: 'ted-535679-2026: Ministry of the Interior awarded ~€642k for records-management systems
    support 2025–2028 (Aug 2026) — a ministry-level buyer inside the same Jun–Aug window,
    and support (not just licence) spend, which is the recurring half of the bill.'
  date: '2026-08-03'
  signal: ted-535679-2026
- type: tender
  name: "TED — Ostrava University records system (~€408k)"
  gist: "the €408k university award"
  why: "The university buyer type inside the same wave, bought with service support attached."
  url: https://ted.europa.eu/en/notice/-/detail/442243-2026
  note: 'ted-442243-2026: Ostravská univerzita awarded ~€408k for a records management system
    incl. service support (Jun 2026) — the university buyer type in the same wave.'
  date: '2026-06-29'
  signal: ted-442243-2026
- type: tender
  name: "TED — Lesy ČR records system (~€1.1M)"
  gist: "the €1.1M state-forest award"
  why: "The state-enterprise buyer type, and one of the larger single awards in the wave."
  url: https://ted.europa.eu/en/notice/-/detail/529246-2026
  note: 'ted-529246-2026: Czech State Forests (Lesy ČR) awarded ~€1.1M for an electronic records
    management system (Jul 2026) — the state-enterprise buyer type, and one of the larger
    single awards in the wave.'
  date: '2026-07-30'
  signal: ted-529246-2026
- type: tender
  name: "TED — Prague, GINIS ENTERPRISE+ development (~€275k)"
  gist: "the €275k GINIS award"
  why: "Direct evidence that GORDIC's GINIS stack is one of the incumbents this wave is being bought from, alongside ICZ's e-spis."
  url: https://ted.europa.eu/en/notice/-/detail/533101-2026
  note: 'ted-533101-2026: City of Prague awarded ~€275k for GINIS ENTERPRISE+ development incl.
    records management (framework, Jul 2026) — direct receipt that GORDIC''s GINIS stack is
    one of the incumbents the wave is being bought from, alongside ICZ e-spis.'
  date: '2026-07-31'
  signal: ted-533101-2026
- type: gap-check
  name: "Attested eSSL supplier scan"
  gist: "the four attested vendors"
  why: "The state publishes the roster of attested records systems, and four Czech suppliers are on it — GORDIC's GINIS, ICZ.DMS's e-spis, Seyfor's ELDAx and MIT Consulting's MIT ERMS — with a dozen more Czech systems not yet attested."
  url: https://agenturacas.gov.cz/atestace/vydane-atesty/
  note: 'Czech-language supplier scan 2026-08-25. The decisive instrument is the state''s own
    register: the Czech Agency for Standardization (Česká agentura pro standardizaci) publishes
    every issued eSSL attest at agenturacas.gov.cz/atestace/vydane-atesty. At this check FOUR
    products from FOUR Czech suppliers hold one. Atest 1/2025 — GORDIC spol. s r.o., IČO
    47903783, Erbenova 2108/4, Jihlava — GINIS v525, issued 25.11.2025, valid to 25.11.2027,
    extended by declaration to v5.26 on 15.04.2026. Atest 2/2026 — ICZ.DMS a.s., IČO 06696805,
    Na hřebenech II 1718/10, Praha 4 — e-spis v3, 07.05.2026 to 07.05.2028. Atest 3/2026 —
    Seyfor, a. s., IČO 01572377, Drobného 555/49, Brno — ELDAx eSSL v6.0.0, 07.05.2026 to
    07.05.2028, extended to v6.0.1 on 20.05.2026. Atest 4/2026 — MIT Consulting, s.r.o. — MIT
    ERMS v3.5, 22.07.2026 to 22.07.2028. Every attest runs two years and attaches to a product
    version, so re-attestation is a standing cost that concentrates supply further. The wider
    Czech eSSL field, none of it on the issued-attest list at this check, runs to roughly a
    dozen more products: T-MAPY spol. s r.o. (IČO 47451084) TESS Online, Triada Munis ERMS,
    GEOVAP spol. s r.o. (IČO 15049248) DMS, VERA Radnice, Alis KEO4, MAGION, ELISA, TranSoft,
    WESS, VISION, e-spis LITE, and eZOP from SoftHouse s.r.o. (vendor listing at tesso.cz). At
    the bottom of the market OSS Alliance gives small obce an open-source records system free,
    with two years of hosting, in cooperation with the Ministry of the Interior — a zero-price
    competitor for the smallest originators. CONTRACTS-REGISTER INSTRUMENT —
    data/lookup/cz-contract-parties.jsonl aggregated by IČO over 3,984 distinct suppliers,
    counting the distinct public buyers each serves: within its single recent ingest window
    GORDIC serves 3 distinct public buyers (two Hradec-region secondary schools and MČ Praha 20
    - Horní Počernice), Seyfor 2 (město Krnov, Psychiatrická nemocnice v Kroměříži), GEOVAP 2
    (statutární město Karviná, ŘSD s.p.), ICZ a.s. (IČO 25145444) 1 (Český statistický úřad)
    and ICZ.HEA a.s. (IČO 07240091) 1 (Nemocnice Břeclav). Multi-buyer public suppliers are the
    incumbent signature, not a startup one. The lookup is one ingest window rather than the
    whole registr smluv, so those counts are floors, not totals. POSITIVE CONTROLS, two of
    them. On the contracts instrument: GORDIC, the incumbent this file already named, does
    surface as a multi-buyer public supplier — PASSED. On Czech-language search: the same
    method run at Softlink, the incumbent named on p-0026, surfaced its 169/868 MHz metering
    platform — PASSED. Corpus contrast: T-MAPY, MIT Consulting, ELDAx, Munis, Triada, GEOVAP,
    VERA Radnice and KEO4 return ZERO hits across all 11,330 signals in data/register.db, while
    GORDIC, GINIS and e-spis appear only because they win TED-scale tenders — the pipeline sees
    tender winners and is blind to the rest of the supply side. gap was already 0 and stays 0;
    status moves to watching under the SPEC §4 de-rank rule on the named Czech incumbents.
    NOTED, NOT ACTED ON: several Czech sources in this scan (tyden.cz, munis.cz, eldax.cz)
    report an odklad giving authorities more time to move onto attested systems, and describe
    the hard line as 1 January 2027 rather than 31 December 2026. That touches the S1 deadline
    and needs its own verification against the statute before anything on this file changes.'
  date: '2026-08-25'
  queries:
    - "seznam atestovaných elektronických systémů spisové služby atest eSSL"
    - "elektronická spisová služba atest 2026 dodavatel atestované řešení pro úřady"
    - "spisová služba pro obce a příspěvkové organizace software dodavatelé přehled cena migrace"
    - "kdo dodává atestovanou spisovou službu GINIS e-spis ELDAx MIT ERMS TESS Online porovnání"
    - "český software pro dálkové odečty vodoměrů sběr dat z měřidel vodárny systém"
  checked: [google-cz, ares, cz-saas-directories, own-funded-ledger]
  expires: '2026-11-23'
- type: regulation
  name: "ČAS — when a public body must actually be running an attested eSSL"
  gist: "the 1 January 2027 date"
  why: "The state agency that issues the attests puts the date in one sentence: a public-law originator must be running records management in an attested eSSL no later than 1 January 2027."
  url: https://agenturacas.gov.cz/atestace/otazky-a-odpovedi/
  note: 'Statute check 2026-08-25, closing the item the supplier scan flagged and did not act
    on. The Czech Agency for Standardization Q&A states "Veřejnoprávní původce je povinen
    vykonávat spisovou službu v elektronické podobě v atestovaném eSSL nejpozději od 1. ledna
    2027", pointing at the transitional provision in §27 of vyhláška č. 259/2012 Sb.; the same
    page repeats the supply-side rule, "Dodavatel od 1. července 2025 smí nabízet pouze
    atestovaný eSSL". Legal commentary read live on the same date (epravo, "Nestačí mít systém")
    independently gives 1 January 2027 as the end of the transitional period under §63 odst. 3
    zákona č. 499/2004 Sb., and records a fine of up to 200,000 CZK for an originator that is
    not compliant from that day. So this file had the boundary a day early: the transitional
    period runs THROUGH 31 December 2026 and the obligation bites FROM 1 January 2027, which is
    how the state and the trade press both state it. CAVEAT recorded rather than smoothed over:
    the same ČAS page also carries a stale section giving 1 January 2026 — an internal
    inconsistency on the issuing agency''s own page. The 2027 date is the one tied to the
    transitional provision and the one every Czech source in the 2026-08-25 scan reports.
    Deadline sub-score unchanged at 2, under 18 months either way, so urgency stays 3.'
  date: '2027-01-01'
created: '2026-08-13'
updated: '2026-09-02'
---

Every Czech public body runs a spisová služba — the records layer under all official correspondence — on software that now needs a state attestation. Suppliers have been barred from offering non-attested products to public-law originators since 1 July 2025; the bodies must be running an attested system from 1 January 2027 [S1,S9].

Why now: in June–August 2026 ~19 public buyers filed ~28 records-management tenders worth ~€17M on TED — the EU's public tender journal [S2]. They are failing to close: SÚRAO (the nuclear-waste authority) republished four times, the Pardubice hospital group three [S2].

Who pays: every public-law originator facing 1 January 2027 — ministries, hospitals, universities, state enterprises — first to migrate onto an attested system, then annually for support [S9]. Ten TED weeks carried ~€17M, roughly €90M a year of visible spend [S2]. Awards run from ~€408k at Ostrava University to ~€1.1M at Lesy ČR (Czech State Forests) [S5,S6]; the Interior Ministry bought multi-year support, not a licence [S4]. Below TED's threshold the tail is unmeasured. Vendors pay too: an attest covers one product version, so re-certifying is a standing cost that concentrates supply [S1].

Existing non-solutions: four products hold an attest — GORDIC's GINIS, ICZ.DMS's e-spis, Seyfor's ELDAx and MIT Consulting's MIT ERMS — issued November 2025 to July 2026, each for two years [S8]. GINIS and e-spis are winning the wave [S3,S7]. A dozen more Czech systems are not on the list — T-MAPY's TESS Online, Triada's Munis, GEOVAP, VERA Radnice, Alis's KEO4 — and every body running one has to move [S8,S9]. At the bottom, OSS Alliance (an open-source group working with the Interior Ministry) gives the smallest towns a records system free [S8]. The attest is scarce, not the software. No buyer complaint is on file; nobody counts how many bodies still run non-attested systems [S2].

Solved elsewhere: one comparable, and the shape is right. Documaster has sold from Oslo since 2014, built the first records kernel certified against Norway's Noark archival standard, took 100M Norwegian kroner from Summa Equity and has grown revenue more than fifteenfold since 2017 — certification turned into a moat, not a barrier. One company, one country: attestation this strict is otherwise a Czech construction [S1].

## First moves

1. Start with the buyers whose tenders keep failing. SÚRAO republished four times and the Pardubice hospital group three, inside a ~€17M June–August 2026 wave [S2]. A body on its fourth publication has a budget, a date and no bid.
2. Build the migration, not another records system. A dozen Czech systems still in service hold no attest [S8]. Every body running one has to move, records and metadata intact, before 1 January 2027.
3. Open with the date and the fine. Run an attested system from 1 January 2027 or pay up to 200,000 CZK [S9]. Suppliers have been barred from offering non-attested systems to these bodies since 1 July 2025 [S1].
4. Sell to the vendors too. An attest runs two years and covers one product version [S1,S8], so the four attested vendors re-certify on a clock and the unattested dozen must pass the gate or lose their public customers.
5. Do not compete on price. OSS Alliance gives the smallest towns a free system, with the Interior Ministry behind it [S8]. Sell the move and the certificate, not the licence.

## Revisions

2026-08-24 · fact check — The supply-side ban was stated one notch too widely: §69e bans offering or supplying non-attested eSSL to public-law originators ("zákaz nabízet nebo dodávat veřejnoprávním původcům"), not from sale generally — verified live on the S1 commentary, and title and lead now say so [S1]. The procurement-wave arithmetic was re-counted mechanically against the signal corpus on this date: ~30 matching records, 19 distinct buyers, SÚRAO with four publications and Nemocnice Pardubického kraje with three, as stated [S2].

2026-08-25 · board-brief rewrite, then market check (one entry per date, so the two merge) — The body was rewritten to the builder-first template and the missing `Solved elsewhere:` lead-in was written: without it the Proven abroad section rendered as a bare comps ledger with no prose, and the body meanwhile claimed "no foreign analog is on file" while Documaster sat on that ledger. The paragraph now states what the one comparable proves — a national records-certification regime (Norway's Noark) turned into a product moat rather than a barrier — and keeps the honest limit that attestation this strict is otherwise a Czech construction. "How big" now carries arithmetic instead of a gesture: ~€17M across ten TED weeks annualises to roughly €90M of visible spend, with the individual awards (~€642k Interior support, ~€1.1M Lesy ČR, ~€408k Ostrava University) showing the spread and the sub-threshold tail named as unmeasured [S2,S4,S5,S6]. The open follow-up moved into the local-competition paragraph so it stops landing inside Proven abroad. Every source gained a public name and why line; scores, status and internal notes untouched. Flagged for MATCH, not changed: `scores.proof` is 0 while a funded foreign comparable (Documaster, NOK 100M from Summa Equity) sits on the comps ledger. Later the same day, the market check — the supply side was checked properly for the first time, in Czech and against the state's own list of issued attests. Four Czech suppliers hold one — GORDIC (GINIS, atest 1/2025), ICZ.DMS (e-spis, 2/2026), Seyfor (ELDAx, 3/2026) and MIT Consulting (MIT ERMS, 4/2026) — each attest running two years and tied to a product version; a dozen further Czech systems are not on the list, and OSS Alliance gives the smallest obce an open-source one free [S8]. "Existing non-solutions" now names all four rather than two. `scores.gap` was already 0 and stays 0; `status` moves candidate → watching under the SPEC §4 de-rank rule, which is what naming incumbents has always implied here. `score` is unchanged at 5. The supplier side of the contracts register was used as a second instrument: aggregating `data/lookup/cz-contract-parties.jsonl` by IČO over 3,984 suppliers shows GORDIC serving three distinct public buyers in one ingest window, Seyfor and GEOVAP two each, ICZ and ICZ.HEA one each — multi-buyer public suppliers, the incumbent signature. Flagged for verification, NOT acted on by that pass: Czech trade coverage in this scan describes an odklad and puts the hard line at 1 January 2027 rather than 31 December 2026, which touches the S1 deadline and needs checking against the statute. Later the same day, that flag was closed and the file re-scored under the rewritten SCORING.md.

THE DEADLINE, SETTLED. The trade coverage is right and this file was a day out. The Czech Agency for Standardization — the body that issues the attests — states in its own Q&A that a public-law originator must be running records management in an attested eSSL "nejpozději od 1. ledna 2027", citing the transitional provision in §27 of vyhláška č. 259/2012 Sb.; legal commentary read live on the same date gives 1 January 2027 as the end of the transitional period under §63 odst. 3 zákona č. 499/2004 Sb., with a fine up to 200,000 CZK from that day [S9]. The lead and "Who pays" now say "from 1 January 2027" instead of "by 31 December 2026", and the [S1] public summary line says the transitional period runs out at the end of 2026 rather than naming the wrong compliance date. Nothing was smoothed over: the same ČAS page carries a stale section giving 1 January 2026, an internal inconsistency on the issuing agency's own page, and [S9] records it. The [S1] internal note is untouched and remains correct as written — a period that ENDS 31 December 2026 and an obligation that BITES from 1 January 2027 are the same boundary. The urgency sub-scores do not move: the date is under eighteen months out either way, so deadline stays 2 and `scores.urgency` stays 3. The title, "by the end of 2026", survives the check unchanged.

THE RE-SCORE. `scores.proof` 0 → 2, resolving the contradiction flagged for MATCH earlier this same day. Documaster passes the ESTABLISHED test on three limbs at once — selling since 2014, a state certification (the first records kernel certified against Norway's Noark standard), growth equity from Summa Equity at NOK 100M, and revenue up more than fifteenfold since 2017. One established foreign player is rung 2 exactly. Rung 3 was considered and declined: it needs two-plus markets, and Norway is the only one on file, CEE-adjacent though the Nordics are. `scores.gap` stays 0, and now means TAKEN rather than the v1 rung's "check not done" — which is precisely the defect the owner caught, a page printing "not yet checked" above a list of four attested competitors. Seven local players were lifted out of the [S8] scan prose into a structured `locals[]` ledger. Six are established, four of them on the state-certification limb outright: GORDIC (atest 1/2025, and three distinct public buyers in `data/lookup/cz-contract-parties.jsonl`), ICZ.DMS (atest 2/2026, plus Prague's ~€3.3M e-spis award [S3]), Seyfor (atest 3/2026, plus two distinct public buyers) and MIT Consulting (atest 4/2026). GEOVAP is established on the public-buyer limb without an attest, and OSS Alliance on its Ministry-of-the-Interior arrangement. Only T-MAPY reads early on receipts alone. Founding years were verified in ARES on this date. `score` 5 → 7. The Proven-abroad paragraph now states Documaster's trading age and says plainly that it is one company in one country, because under the new ladder that is what caps the score. Money, urgency and demand untouched; no source note edited and no existing [Sn] marker moved — [S9] is appended, not inserted.

THE COMPETES/MATURITY SPLIT. `locals[].status` was replaced by two orthogonal fields under the owner's no-exclude ruling: `competes: direct|adjacent` answers whether a player sells THIS product to THIS buyer, and `maturity: established|early` keeps the SCORING.md established test unchanged and machine-checked. THE OSS ALLIANCE QUESTION IS ANSWERED BY THE SPLIT, not compromised. Six entries convert without argument — GORDIC, ICZ.DMS, Seyfor and MIT Consulting are `direct` + `established` on their attests, GEOVAP on its public buyers, T-MAPY `direct` + `early`. OSS Alliance was this file's open interpretive problem: it was marked early with a note saying the test's letter and its spirit had come apart, because a free, state-backed, open-source offering cannot satisfy a "three years SELLING" limb at any age, while in spirit it was the strongest signal on the file that the space is taken at the bottom of the market. Two orthogonal fields dissolve that without splitting the difference. `competes` is now a separate question from maturity and its answer is plainly yes: OSS Alliance supplies the same product — an eSSL records system — to the same buyer, the smallest obce, at a price of zero. A price of zero is a price, not a different product, so it competes directly. `maturity` stays `early`, and stays early honestly: no sourced year for the start of supply is on file, so none is written and the years limb cannot be dated at all. That costs nothing, because `scores.gap` is 0 on the four attested vendors regardless — which is exactly why the two questions had to be separated. The entry now records what OSS Alliance is instead of describing a contradiction. Scores, `status`, source notes and every existing [Sn] marker are untouched by this pass.


THE LEDGER NOTES, IN PLAIN LANGUAGE. All 7 `locals[].evidence` lines were rewritten. Those lines RENDER — they are the note printed under every entry in the local-competition ledger — but they were written in the scoring vocabulary rather than in words a builder can use: "no limb of the established test is met", "no round at Series stage", bare ARES registration dates, and the repository path `data/lookup/cz-contract-parties.jsonl` and `data/register.db` printed to a reader who has no way to open it. Each line now leads with what the company actually sells and, where the receipts are thin, says what is unknown instead of which limb failed — "publishes no customer count and names no buyer, so how much it sells is unknown" rather than a verdict about our own test. Every date, IČO, customer count, price, funding figure and [Sn] marker was carried across unchanged, and the established test was re-run against the rewritten lines afterwards to confirm that not one maturity verdict moved. `score`, `scores`, `status`, `competes`, `maturity` and every `sources[].note` are untouched by this pass.

FIRST MOVES WRITTEN. `data/RECORD-TEMPLATE.md` reserves the section for records scoring >= 7 and this file scores 7; it was simply missing, which cost the reader the most actionable thing on the page. Four moves, each drawn from evidence already on the record: the buyers whose tenders keep republishing as the first customers [S2], migration off the dozen unattested Czech systems as the first build [S8], the 1 January 2027 date and its 200,000 CZK fine as the opening fact [S9], and the unattested vendors themselves as a second, recurring buyer [S1,S8]. No new fact was introduced, no source note was edited and no [Sn] marker was moved.

2026-09-02 · plain-language pass — Three trade terms glossed at first use: TED as the EU's public tender journal [S2], Lesy ČR as Czech State Forests, OSS Alliance as an open-source group; SÚRAO gained an appositive and NOK became plain Norwegian kroner. The argument went 442 to 367 words, First moves 286 to 183, with every [Sn] marker, figure, date and named vendor kept. A gist was added to all nine sources. No score, status, note or marker touched.
