---
id: p-0042
region: cz
title: 'Czech pupils who need extra help at school wait up to 18 months for an assessment'
brief: 'Counselling centres assess pupils who need extra help at school, and families wait around half a year, up to 18 months in places [S1,S2]. The number of pupils getting that help rose 20% in a year [S2].'
solution: 'Build a service that gives small schools a psychologist and a special educator over video, so pupils get first help while they wait for an assessment, as 2 companies already do in the United States.'
good_for: 'Someone with a psychology or special-education team who can sell to schools.'
category: education
geo: CZ-national
score: 8
scores:
  proof: 2
  money: 2
  urgency: 0
  demand: 2
  gap: 2
status: candidate
entry:
  level: hard
  buyer: public
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed to sell schools a psychologist''s time; some schools already buy it from freelancers; and the state pays schools for these posts every year. Harder: schools are public buyers; only a registered counselling centre can issue the formal recommendation; and psychologists are scarce.'
comps:
- name: Parallel Learning
  url: https://www.parallellearning.com/
  geo: US
  since: 2021
  traction: 'Founded 2021 in New York; supplies school districts with licensed speech-language pathologists, school psychologists and special educators over video for psychoeducational assessments and therapy; USD 20M Series A (May 2022) and USD 20M Series B led by Valspring Capital (Dec 2025), USD 48.9M raised in total; more than 10,000 students in 25 states (Pulse 2.0 and AlleyWatch, 2025)'
  signal: us-parallel-learning
- name: Presence
  url: https://presence.com/
  geo: US
  since: 2009
  traction: 'Founded 2009 to deliver speech-language therapy remotely; now offers remote evaluations, psychoeducational assessments, therapy and counselling for PreK-12 pupils; more than 10,000 schools and more than 2,000 licensed providers (presence.com/about, read 2026-09-18)'
locals:
- name: Didanet (ARET Praha)
  url: https://www.didanet.cz/
  ico: '25113852'
  since: 1997
  competes: adjacent
  maturity: established
  evidence: 'Sells Didanet, the client-record and report system used by 88% of counselling-centre workplaces, at 31,500 CZK a year per centre (price list from January 2026). It keeps files and generates reports; it does not supply specialists or assess pupils. ARET Praha s.r.o. was founded in 1997.'
- name: VIRIDIS (Evidence PPP/SPC)
  url: https://www.viridis.cz/program-evidence-ppp-spc/
  ico: '26449307'
  since: 2001
  competes: adjacent
  maturity: established
  evidence: 'Sells a client-record program for counselling centres, used by about 3% of workplaces; named customers include the Prague 3, 6, 9 and 10, Liberec, Jablonec, Česká Lípa and Kladno centres. Records and reports only. VIRIDIS informační systémy s.r.o. was founded in 2001.'
- name: Amenit (PPP Professional)
  ico: '25816888'
  since: 1998
  competes: adjacent
  maturity: established
  evidence: 'Sells PPP Professional, a record program for counselling centres used by about 5% of workplaces. Records and reports only. Amenit s.r.o. of Nový Jičín was founded in 1998.'
- name: Levebee (Včelka)
  url: https://www.vcelka.cz/dyslexie
  ico: '03362078'
  since: 2014
  competes: adjacent
  maturity: established
  evidence: 'Sells Včelka, a children''s reading app with automatic reading diagnostics. Named customers include the Kolín counselling centre, which bought a licence for 89,500 CZK in 2021; it also won a 6.7M CZK industry-ministry grant in 2025. It trains reading at home and school; it does not supply specialists or issue recommendations. Levebee s.r.o. was founded in 2014.'
- name: Hogrefe-Testcentrum
  ico: '26159392'
  since: 2000
  competes: adjacent
  maturity: established
  evidence: 'Publishes and sells the licensed psychological tests counselling centres assess pupils with; named customers include the Frýdek-Místek counselling centre, which paid 172,000 CZK for a pre-school intelligence test in 2019, and the contracts register holds 394 of its contracts. It sells tests, not assessments or specialist time. Hogrefe-Testcentrum s.r.o. was founded in 2000.'
- name: Terapie řeči
  url: https://terapiereci.cz/
  ico: '22001760'
  since: 2024
  competes: adjacent
  maturity: early
  evidence: 'Runs a speech-therapy centre that treats children and adults in person and online, and offers a service for kindergartens. It does not sell schools psychologists or special educators, or assess pupils for support at school. Terapie řeči s.r.o. was founded in September 2024; no customer count was found.'
- name: Medevio
  url: https://www.medevio.cz/logopedie-online
  ico: '09675400'
  since: 2020
  competes: adjacent
  maturity: early
  evidence: 'Sells online speech-therapy consultations to families as part of a health app; it does not sell to schools or assess pupils for support at school. Medevio s.r.o. was founded in November 2020.'
process:
  summary:
    today: 'A family or school books the counselling centre, waits months for a date, the centre assesses the pupil and writes the report, and the school handles lighter needs alone [S1,S2,S3,S4].'
    after: 'A remote psychologist and special educator help the school with lighter needs at once, so the centre''s dates go to the pupils who need the formal step.'
  steps:
  - who: Family or school
    today: 'Books an assessment at the counselling centre'
    known: documented
    cites: [3]
    change: stays
    after: 'Books only pupils who need the formal step'
  - who: Pupil and family
    today: 'Wait around half a year for a date'
    known: documented
    cites: [2]
    change: changes
    after: 'Get first help from a remote specialist meanwhile'
  - who: Centre psychologist or special educator
    today: 'Assesses the pupil at the centre'
    known: documented
    cites: [1]
    change: stays
    after: 'Unchanged: the formal assessment stays with the centre'
  - who: Centre staff
    today: 'Write up notes, reports and returns'
    known: documented
    cites: [4]
    change: stays
    after: 'Unchanged: the centre keeps its own paperwork'
  - who: Teachers
    today: 'Handle lighter needs without an assessment'
    known: documented
    cites: [2]
    change: changes
    after: 'Handle them with a remote specialist''s guidance'
sources:
- type: complaint
  name: "ČŠI — counselling centres: capacity, work and access"
  gist: "the school inspectorate's report"
  why: "The Czech School Inspectorate's report on counselling centres: the share meeting the legal three-month deadline fell to 80% of workplaces, and only 24% meet it every time, mostly for lack of capacity."
  url: https://www.csicr.cz/CSICR/media/Prilohy/2024_p%c5%99%c3%ADlohy/Dokumenty/TZ_Skolska-poradenska-zarizeni.pdf
  note: 'ČŠI thematic report "Školská poradenská zařízení: kapacity, činnosti a jejich
    dostupnost", 25 Mar 2026, read by the research pass 2026-09-18. p. 32 fn 13: "Tříměsíční
    lhůtu dodržovalo 85 % pracovišť, z toho pouze 30 % ve všech případech. Ve školním roce
    2024/2025 je to již jen 80 % pracovišť, z toho 24 % ve všech případech." p. 32: "značný
    podíl zařízení ... která nedokážou naplnit lhůtu 3 měsíců ... a to především z kapacitních
    důvodů." p. 10: "přepočtený počet psychologů však stagnuje. Dvě třetiny zařízení pak
    vyjádřily potřebu získat další odborné pracovníky". Tab. 4.1: PPP clients 198,404 (2018/19)
    to 212,653 (2023/24); SPC 94,150 (2023/24). "V činnostech psychologů a speciálních pedagogů
    převažuje diagnostika"; "V pěti krajích byla nejčetnější činností speciálních pedagogů
    administrativa." p. 15: Didanet at 88 % of workplaces, PPP Professional about 5 %, Evidence
    PPP/SPC about 3 %. The report''s 168 / 127 clients figure is ambiguous between p. 10 and
    p. 17 and is not used.'
  date: '2026-03-25'
- type: news
  name: "ČT24 — more pupils need support, and neither schools nor centres keep up"
  gist: "waits up to 18 months"
  why: "Nearly 160,000 pupils had support measures last school year, 20% more than the year before, and waits for a counselling centre run around half a year, up to 18 months in places."
  url: https://ct24.ceskatelevize.cz/clanek/domaci/vyrazne-pribyva-deti-ktere-potrebuji-podpurna-opatreni-nestihaji-skoly-ani-poradny-377262
  note: 'ČT24, 4 Sep 2026, fetched 2026-09-18: "Celkem jich v Česku bylo v uplynulém školním roce
    bezmála 160 tisíc, v meziročním srovnání o dvacet procent víc" (MŠMT data); waits "se v
    současnosti pohybují kolem půl roku, na řadě míst ale není výjimkou ani osmnáct měsíců";
    the PPP Brno director: "apelujeme na školy, aby s těmito žáky ... dokázali pedagogové kvalitně
    pracovat bez vyšetření v PPP" (first-degree measures). Growth is largest among lighter,
    first-degree needs.'
  date: '2026-09-04'
- type: complaint
  name: "PPP Liberec — a 10-month booking wait"
  gist: "a named centre's own notice"
  why: "A regional counselling centre's own notice: the wait for an assessment is about 10 months."
  url: https://www.pppliberec.cz/
  note: 'Pedagogicko-psychologická poradna Liberec homepage, notice dated 17 Feb 2026, read by
    the research pass 2026-09-18: "v současné době je objednací lhůta k vyšetření přibližně 10
    měsíců." More than three times the legal three-month limit [S1].'
  date: '2026-02-17'
- type: news
  name: "ČT24 — deferrals overload the centres"
  gist: "half the day on paperwork"
  why: "Families wait months, in places half a year, and about half of centre staff time goes to notes, reports and returns rather than work with children."
  url: https://ct24.ceskatelevize.cz/clanek/domaci/poradny-jsou-kvuli-odkladum-skolni-dochazky-pretizene-356995
  note: 'ČT24, 12 Jan 2025, read by the research pass 2026-09-18: "Ti si musí na termín počkat i
    několik měsíců, někde až půl roku."; "cca padesát procent pracovní doby jde na úkor nepřímé
    práce – zápisy, zprávy, výkazy a podobně". Headline: "Poradny jsou kvůli odkladům školní
    docházky přetížené".'
  date: '2025-01-12'
- type: arbitrage
  name: "Parallel Learning"
  gist: "remote SEN specialists, US"
  why: "A New York company that sells school districts licensed psychologists, speech therapists and special educators over video, for assessments and therapy, after a USD 20M Series B."
  url: https://pulse2.com/parallel-20-million-series-b/
  note: 'us-parallel-learning: Pulse 2.0, 10 Dec 2025: USD 20M Series B led by Valspring
    Capital; operates in 25 states, more than 10,000 students; founded 2021. Earlier USD 20M
    Series A led by Tiger Global, 26 May 2022 (eSchool News: "services begin within days, instead
    of the typical wait of months"). USD 48.9M raised in total (EdWeek Market Brief, 2025-12).
    Established.'
  date: '2025-12-09'
  signal: us-parallel-learning
- type: arbitrage
  name: "Presence"
  gist: "remote school therapy since 2009"
  why: "A US company that has delivered therapy and assessments to schools remotely since 2009, now with more than 10,000 schools and 2,000 licensed providers."
  url: https://presence.com/about/
  note: 'presence.com/about, read 2026-09-18: founded 2009 "to expand access to high-quality
    speech-language therapy through innovative remote delivery"; "more than 10,000 schools and
    more than 2,000 licensed providers"; remote evaluations and teletherapy including
    psychoeducational assessments and mental-health counselling, PreK-12. Established.'
  date: '2026-09-18'
- type: subsidy
  name: "MŠMT — the state takes over school psychologists' pay"
  gist: "about 905M CZK a year"
  why: "The education ministry's own estimate: paying 1,215 school psychologist and special educator posts from the state budget from January 2025 costs about 905M CZK a year."
  url: https://www.zakonyprolidi.cz/media2/file/2403/File65487.pdf
  note: 'MŠMT explanatory report č. j. MSMT-3322/2024-2 (file dated 1 Mar 2024), read by the
    research pass 2026-09-18: "lze k 1. 1. 2025 odhadovat roční finanční náklady na zajištění
    financování 1 215,44 úvazků těchto pedagogických pracovníků ze státního rozpočtu ve výši cca
    905 mil. Kč." edu.gov.cz, 26 Sep 2024: EU (OP JAK) funding of these posts ended in 2024.
    Recurring annual public spend near this problem. It pays posts, not outside services, so
    since 2026-09-19 it is public money nearby: it earns no money point and cannot lift one.'
  date: '2024-03-01'
- type: subsidy
  name: "KVIC — how school psychologists are funded from 2026"
  gist: "posts by school size"
  why: "From January 2026 the state funds school psychologist and special educator posts through a standing per-school allocation, from half a post at 180–299 pupils to 2.5 posts at 1,000 or more."
  url: https://www.kvic.cz/2025/09/11/financovani-skolnich-psychologu-a-specialnich-pedagogu-od-1-ledna-2026-co-se-meni/
  note: 'KVIC, 11 Sep 2025, read by the research pass 2026-09-18: "Od 1. 1. 2026 budou tyto
    pozice financovány ze státního rozpočtu, formou tzv. systémové normativní podpory."
    Allocation "180–299 žáků → 0,5 úvazku" rising to "1000 a více → 2,5 úvazku". Schools under
    180 pupils get no post of their own on this scale, which is our reading of the table, flagged
    in Revisions.'
  date: '2025-09-11'
- type: ask
  name: "TA ČR — the education ministry asks for uniform support decisions"
  gist: "the ministry's own research need"
  why: "The education ministry asked for research on how counselling centres could set support measures for pupils in one uniform way, as a base for tools that unify them."
  url: https://tacr.gov.cz/konzultace-k-moznostem-reseni-vyzkumne-potreby-ttxmsmt502-analyza-a-navrhy-reseni-jednotneho-pristupu-skolskych-poradenskych-zarizeni-pri-nastavovani-podpurnych-opatreni-u-zaku-se-specialnimi-vzdelav/
  note: 'tacr-ttxmsmt502: owner Ministerstvo školství, mládeže a tělovýchovy; research need
    TTXMSMT502, "Analýza a návrhy řešení jednotného přístupu školských poradenských zařízení při
    nastavování podpůrných opatření u žáků se speciálními vzdělávacími potřebami", asking for a
    data, logistical and reference framework for tools that unify how support measures are
    allocated. Page dated 25 Feb 2026. An ask cites demand only (MATCH.md §11).'
  date: '2026-02-25'
  signal: tacr-ttxmsmt502
  dims: [demand]
- type: news
  name: "EDUin — new counselling-centre rules and funding planned for 2027"
  gist: "270 more centre staff planned"
  why: "A new decree on counselling services and a new way of funding the centres are planned from January 2027, with about 270 more staff; the finance ministry disputes the cost."
  url: https://www.eduin.cz/clanky/tz-eduin-poradenske-sluzby-vyhlaska/
  note: 'EDUin, 23 Apr 2026, read by the research pass 2026-09-18: "nový systém financování ŠPZ,
    který má být účinný od 1. ledna 2027"; "předpokládá pro rok 2027 navýšení o 270 pracovníků
    ... asi o 244 milionů korun"; the finance ministry disputes the amount. A plan, not a
    compliance date, so it scores no deadline point.'
  date: '2026-04-23'
- type: gap-check
  name: "Czech check — nobody sells schools remote SEN specialists"
  gist: "the Czech field, searched"
  why: "Fourteen Czech query shapes, the business register and the contracts register: record systems for counselling centres, test publishers, reading apps and family speech therapy exist, and no Czech firm was found selling schools remote psychologists or special educators."
  url: https://www.didanet.cz/
  note: 'Gap check 2026-09-18, two passes (the monthly scan behind us-parallel-learning and a
    research sub-pass), Czech-language web search, ARES, Hlídač/registr smluv full text and
    own-funded-ledger. NOT FOUND: any Czech firm selling schools remote or outsourced
    assessments, or school-psychologist, special-educator or speech-therapist capacity, as a
    product. Schools that buy psychologist time buy it from individual freelancers (ZŠ Mikulov,
    registr smluv, S12). FOUND, ADJACENT: Didanet by ARET Praha (25113852, 1997; 88 % of
    workplaces per ČŠI [S1]; 31,500 CZK/yr per centre, didanet.cz/cenik); Evidence PPP/SPC by
    VIRIDIS (26449307, 2001; about 3 %; named centres); PPP Professional by Amenit (25816888,
    1998; about 5 %); IS Klient PPP, Medikus TURBO asistent and EP SOFTCOM (about 4 % together,
    not opened); Levebee Včelka (03362078, 2014; PPP Kolín licence 89,500 CZK 2021, MPO TWIST
    grant 6,705,275 CZK 2025); Hogrefe-Testcentrum (26159392, 2000; PPP Frýdek-Místek 172,000
    CZK test order 2019; 394 contracts); Terapie řeči (22001760, 2024; speech therapy in person and
    online for children and adults, plus a kindergarten service, terapiereci.cz read 2026-09-18); Medevio (09675400, 2020; online speech-therapy consultations for families);
    Vyslovuj (pronunciation app for parents, no ARES match); Hedepy (09206281) and Terap.io
    (adult online therapy, not in this neighbourhood); DYSLEX and DysTest (Masaryk University
    research tools, no commercial seller found); state centres'' own online consultations (PPP
    Opava), which are public providers, not vendors. POSITIVE CONTROL PASSED, run on both passes:
    "česká firma zabezpečení mobilního bankovnictví software" surfaced Wultra (Wultra App
    Shielding), the p-0017 incumbent; ARES returned Wultra s.r.o. (03643174). Gap 2 rests on
    this check; the seven adjacent entries move nothing.'
  date: '2026-09-18'
  queries:
    - "pedagogicko-psychologická poradna čekací doba měsíce nedostatek psychologů speciálních pedagogů 2025"
    - "online speciální pedagog a školní psycholog pro školy na dálku služba platforma"
    - "soukromé školské poradenské zařízení online diagnostika podpůrná opatření bez čekání"
    - "online logopedie pro děti přes video platforma Česko startup"
    - "externí školní psycholog pro školy služba sdílený psycholog online konzultace žáci Hedepy OR Terap.io OR Mindwell"
    - "online diagnostika dyslexie pro školy aplikace"
    - "screening specifických poruch učení software škola"
    - "externí školní psycholog pro školy služba"
    - "software pro pedagogicko-psychologické poradny zpráva z vyšetření evidence klientů Didanet"
    - "online speciální pedagog pro školy"
    - "online logoped pro školy teleterapie logopedie děti firma"
    - "online vyšetření dítěte psycholog na dálku diagnostika poruch učení doporučení pro školu"
    - "školní psycholog na zkrácený úvazek pro malé školy sdílený psycholog nabídka služby školám"
    - "česká firma zabezpečení mobilního bankovnictví software"
  checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
  expires: '2026-12-17'
- type: price
  url: https://www.hlidacstatu.cz/Detail/39484917
  name: "ZŠ Mikulov — a school buys a psychologist's services"
  gist: "a school's psychologist contract"
  why: "A Czech primary school signed a contract for a self-employed psychologist's services, the manual way schools buy this today."
  note: 'Registr smluv via Hlídač státu, read 2026-09-18: "Smlouva o poskytování služeb
    psychologa", buyer Základní škola Mikulov, Valtická 3, p.o. (IČO 70262179), supplier a
    self-employed psychologist (not named here), 180,000 Kč incl. VAT, signed 1 Sep 2026; a prior
    contract of 144,000 Kč on 11 Nov 2025 (/Detail/35662009). The period and hours are in the
    attached document, not read, so the unit is per-project. One buyer. Rescore 2026-09-19: the
    attachment read in Hlídač''s text view: "psychologické služby, v rozsahu 10 hodin týdně,
    zaměřené na podporu žáků, rodičů, pedagogických pracovníků, individuální konzultace a
    poradenskou činnost", 450 Kč an hour, 1 Sep 2026 to 30 Jun 2027, supplier licensed for
    "Psychologické poradenství a diagnostika". That is this job bought in by hand, so it is
    tagged dims: [money]: a paid receipt within 24 months.'
  date: '2026-09-01'
  payer: 'Základní škola Mikulov, a public primary school'
  amount_czk: 180000
  unit: per-project
  basis: signed-contract
  dims: [money]
- type: price
  url: https://pppp.cz/cenik
  name: "Pražská PPP — a paid assessment outside the free route"
  gist: "a paid assessment, list price"
  why: "What a family pays a Prague counselling centre for an assessment of a primary-school pupil outside the free route that leads to a formal recommendation."
  note: 'pppp.cz/cenik, undated, read by the research pass 2026-09-18: "Vyšetření včetně zprávy a
    doporučení ŠPZ dle § 16 Školského zákona jsou bezplatná"; paid assessments outside §16:
    "Vyšetření žáků 1. – 5. tříd ZŠ 2 300 Kč", pre-school 1,800 Kč, secondary 2,700 Kč. Dated
    here by the read date. One buyer type; dims omitted.'
  date: '2026-09-18'
  payer: 'A family buying a primary-school pupil''s assessment at a Prague counselling centre'
  amount_czk: 2300
  unit: per-case
  basis: list-price
- type: price
  url: https://smlouvy.gov.cz/smlouva/35662009
  name: "ZŠ Mikulov — the school year before"
  gist: "the same school, 2025"
  why: "The same school's earlier contract with the same freelance psychologist, for the 2025/26 school year."
  note: 'Restated from the S12 note on 2026-09-19, the rescore tagging pass. Registr smluv
    35662009 via Hlídač státu (/Detail/35662009 and its text view, read 2026-09-19): "Smlouva o
    poskytování služeb psychologa", buyer Základní škola Mikulov, Valtická 3, p.o. (IČO 70262179),
    supplier a self-employed psychologist (not named here), signed 11 Nov 2025, 144,000 Kč incl.
    VAT; the same scope as S12 ("podporu žáků, rodičů, pedagogických pracovníků"), 320 hours at
    450 Kč an hour, 1 Nov 2025 to 30 Jun 2026. This job bought in by hand: a paid receipt within
    24 months.'
  date: '2025-11-11'
  payer: 'Základní škola Mikulov, a public primary school'
  amount_czk: 144000
  unit: per-project
  basis: signed-contract
  dims: [money]
created: '2026-09-18'
updated: '2026-09-19'
---

Pupils who need extra help at school wait months for a counselling-centre assessment, and more centres now miss their legal deadline [S1,S2].

- Waits run around half a year, and up to 18 months in places [S2].
- Only 24% of centre workplaces meet the three-month limit every time [S1].
- Pupils with support measures rose 20% in a year, to nearly 160,000 [S2].

A counselling centre assesses a pupil and recommends the support the school should give [S1]. There are two kinds, pedagogical-psychological centres and special-education centres [S1].

- In 2024/25 80% of workplaces kept the three-month limit at all, down from 85% [S1]. They miss it mostly for lack of capacity [S1].
- The number of psychologists has stagnated, and two thirds of centres say they need more specialists [S1].
- Pedagogical-psychological centres served 212,653 clients in 2023/24, up from 198,404 in 2018/19 [S1].
- The Liberec centre states a wait of about 10 months [S3].
- About half of centre staff time goes to notes, reports and returns [S4].
- The education ministry asked researchers how centres could decide support in one uniform way [S9].

Existing non-solutions: Czech firms sell counselling centres their record systems and tests, and none was found selling schools remote specialists [S11].

- Record systems for the centres keep files and write reports [S1,S11].
- Test publishers and reading apps sell to centres, schools and families [S11].
- Online speech therapy is sold to families, and one centre also serves kindergartens [S11].
- Schools that buy a psychologist's time buy it from freelancers [S11].
- The centres themselves offer some online consultations, but they are the public providers, not sellers [S11].

The sellers are listed under [Market gap](#competition).

Why now: No dated rule forces schools to act, but demand for support grew a fifth in a year and centres fall behind [S1,S2].

- Families wait half a year or more for a recommendation [S2].
- Centre staff lose about half their day to paperwork [S4].
- Schools are asked to handle lighter needs without any assessment [S2].

The growth is largest among pupils with lighter needs, the first degree of support, which a school can give without a recommendation [S2]. The Brno centre's director has asked schools to do just that [S2].

The dates on file:

- In 2024/25 the share of workplaces keeping the three-month limit fell to 80% [S1].
- From 1 January 2026 the state funds school psychologist and special educator posts through a standing allocation by school size [S8].
- From January 2027 a new decree and a new way of funding the centres are planned, with about 270 more staff [S10]. The finance ministry disputes the cost [S10].

Who pays: Some schools already buy a psychologist's time from freelancers, and the state pays schools for psychologists every year [S7,S11].

- About 905M CZK a year pays 1,215 school psychologist and special educator posts [S7].
- A school gets half a post at 180–299 pupils, rising to 2.5 posts [S8].
- Schools that buy this time buy it from individual freelancers, not firms [S11].

The ministry took these posts over from EU funding at the start of 2025 [S7]. What one school paid a freelance psychologist, and what a family pays for an assessment outside the free route, are in the table of what one buyer pays.

- The centres' own software costs each centre a yearly licence [S11].
- The planned 2027 funding would add about 244M CZK for new centre staff [S10].

Solved elsewhere: Two established US companies sell schools psychologists, speech therapists and special educators over video [S5,S6].

- One has served schools remotely since 2009, and now works with 10,000+ schools [S6].
- The other serves 10,000+ students in 25 states [S5].
- Both run assessments over video as well as therapy [S5,S6].

The younger company raised a USD 20M Series B in December 2025, USD 48.9M in total [S5]. It says its services begin within days rather than after the usual wait of months [S5].

## First moves

1. Build a video service that gives a small school a psychologist and a special educator for a few hours a week. The specialists help teachers set up the lighter, first degree of support, which a school may give without waiting for a counselling centre, and they prepare the cases that do need the centre. Keep a simple record of what was tried with each pupil, because the centre will ask for it; see [The opportunity](#opportunity).
2. Call the heads of small primary schools that have no psychologist of their own and offer a term's trial. The state pays schools for these posts by school size, and the smallest schools get too little for a post of their own; see [Willing to pay](#willing-to-pay). Some schools already pay freelancers for a psychologist's time, so the purchase is familiar.
3. Recruit psychologists and special educators who want part-time remote work, including those on parental leave or outside the big cities. Psychologists are scarce, as [The opportunity](#opportunity) shows, so the service works only if it reaches people who are not in the job market full time.
4. Visit the director of one regional counselling centre and agree how the school's cases reach it. The centre keeps the formal assessment and the recommendation, and it gains cases that arrive prepared; see [Why now](#why-now). A centre that trusts the service may send schools on its waiting list your way.
5. Watch the planned new rules for counselling centres, and apply to register as a private centre if the service outgrows the school role. Only a registered centre can issue the formal recommendation, as [Execution difficulty](#execution-difficulty) explains.

## Revisions

2026-09-18 · record created — Minted from the monthly broad scan's us-parallel-learning signal after Czech research. Proof 2 on Parallel Learning and Presence, both established in the US [S5,S6]; no comparable in a second market sells remote school specialists on file, so proof stays below 3. Lexplore (Sweden) sells reading screening, not specialists, and was left off the ledger rather than used to lift proof. Money 2 on recurring state spend on school psychologist and special educator posts [S7,S8]. Urgency 1, freshness only: the 2027 counselling-centre rules are a plan, not a compliance date [S10], and the 2025 school-entry amendment was not confirmed to add work for the centres. Demand 2 on the school inspectorate's report, two ČT24 reports, a centre's own 10-month notice and the ministry's research ask [S1,S2,S3,S4,S9]. Gap 2: no Czech seller of remote school specialists found, with a passing positive control; seven adjacent players recorded [S11]. Flagged as inference: that the smallest schools get too little for a post of their own is our reading of the allocation table, which starts at 180 pupils [S8]. The school inspectorate's 168 and 127 clients-per-worker figures are left out because the report uses them two different ways. The Mikulov price is per-project because the contract's period was not read [S12].

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 1 → 0 and the total 9 → 8; the band stays STRONG. Willing to pay stays 2, now on paid receipts instead of state spending. Why now: the old 1 was the freshness point alone, which is retired. No `regulation` source is on file. The three-month limit falls on the counselling centres, not the schools, and it is the status quo. The 2027 rules are a plan [S10]. So rung 0. Willing to pay: the old 2 rested on state pay for school psychologist posts [S7,S8]. That is public money nearby, and it pays posts, not bought-in services, so it cannot lift a price. Tagging pass, settling the worksheet's judgement call by the owner's rule that a payment counts only if it buys this job: ZŠ Mikulov's contract [S12] was read in full on 2026-09-19. It buys a freelance psychologist for the school, 10 hours a week to support pupils, parents and teachers with individual consultations, at 450 CZK an hour, from 1 September 2026 to 30 June 2027. That is this job, done in person instead of over video, bought in by the school. It is now tagged money: a paid receipt, 180,000 CZK incl. VAT, signed 1 September 2026, within 24 months. The same school's earlier contract with the same psychologist, named in S12's note, is restated as a receipt [S14]: 144,000 CZK incl. VAT, signed 11 November 2025, 320 hours at the same rate and the same scope. Two paid receipts within 24 months give rung 2. Not tagged: the Prague centre's 2,300 CZK assessment [S13] is paid by families, not schools. The adjacent prices in the gap check [S11] (Didanet's licence, Kolín's reading-app licence, Frýdek-Místek's test order) buy software or tests, not a psychologist's time. Body: the `[Competition](#competition)` link now reads `[Market gap](#competition)`. Why now's opening sentence says no dated rule forces schools to act, and no longer names "their legal deadline", which is the centres' own, not the schools'. Willing to pay's opening sentence leads with the schools that pay, and its third item, which repeated it, now says schools buy the time from individual freelancers [S11]. S7's note no longer claims money 2, and S12's note records the contract's scope and its tag. No other score, status, marker or `entry` gate changed.
