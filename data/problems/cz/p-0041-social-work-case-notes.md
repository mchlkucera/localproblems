---
id: p-0041
region: cz
title: 'Czech child-protection offices are hundreds of workers short, and paperwork eats the time of those left'
brief: 'Social workers write up their home visits and client meetings by hand, and paperwork takes more of their time than almost anything else [S2,S4]. Child-protection offices would need 20–30% more staff to keep up [S3].'
solution: 'Build an app that records a social worker''s visit, with the client''s consent, and drafts the note in the office''s own case-file software for the worker to check, as 2 companies already do in 2 other countries.'
good_for: 'Developers who handle sensitive data and can sell to town halls.'
category: govtech
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
  level: hard
  buyer: public
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed; the app plugs into case-file software the office already runs; and a state grant for social work already pays for software and sound recording. Harder: the buyers are town halls, so each sale runs through public purchasing; and the notes hold sensitive data about children and families.'
comps:
- name: Beam (Beam Notes, formerly Magic Notes)
  url: https://beam.org/
  geo: GB
  since: 2017
  traction: 'Founded 2017; Magic Notes launched in 2023, records and transcribes social-work meetings and drafts summaries, and is now called Beam Notes; used by 65,000 practitioners across over 200 organisations (Social Enterprise UK, 2026); named customers include Kent, Swindon, Shropshire, Oxfordshire, Birmingham and North Yorkshire councils (beam.org, read 2026-09-18); Angus Council approved a GBP 240,000 contract in June 2026 (Resultsense, 2026)'
  signal: gb-beam-up
- name: voize
  url: https://www.voize.ai/
  geo: DE
  since: 2020
  traction: 'Founded 2020 in Berlin; turns what nurses and carers say into care documentation; USD 50M Series A led by Balderton Capital; 1,500+ care facilities and 100,000+ nurses use it (Y Combinator company page, read 2026-09-18)'
  signal: yc-voize
- name: Northwoods
  url: https://www.teamnorthwoods.com/
  geo: US
  since: 2003
  traction: 'Founded 2003 in Dublin, Ohio; its Traverse software handles mobile casework, documents and forms for human-services caseworkers; named customers include Carver, Scott and Houston county human-services agencies in Minnesota and Jackson County Job and Family Services in Ohio (teamnorthwoods.com, read 2026-09-18). No AI note drafting is stated on the pages read.'
locals:
- name: Flins (Arasoft)
  url: https://arasoft.cz/
  ico: '08977402'
  since: 2025
  competes: direct
  maturity: early
  evidence: 'Sells Flins, a record system for social-service providers whose AI module turns the notes workers have already typed into reports and client summaries in seconds. It does not record the visit itself. The AI module went live in September 2025 after a pilot at one organisation. Arasoft s.r.o. was founded in February 2020. Praha 7''s town hall pays 89,000 CZK a year for Flins client records and two project modules, under a January 2025 contract that lists no AI module. Its website names no price.'
- name: IRESOFT (CYGNUS)
  url: https://iresoft.cz/
  ico: '26297850'
  since: 2002
  competes: adjacent
  maturity: established
  evidence: 'Sells CYGNUS, a record system that more than 1,400 social-service providers in Czechia and Slovakia run, and the state contracts register shows 2 public buyers paying it. Its AI assistant, part of the paid licence from June 2026, answers questions, searches documents and writes or edits text on request; care homes have signed for it since May 2026. Voice entry is the phone keyboard''s own dictation. It is a chat and document assistant sold to social-service providers such as care homes, not to child-protection offices, and it does not record a visit and draft the case note.'
- name: Marbes (PROXIO sociální agendy)
  url: https://www.proxio.cz/socialky/
  ico: '29108373'
  since: 2010
  competes: adjacent
  maturity: established
  evidence: 'Sells PROXIO, a case-file system for town-hall social departments with 16 child-protection agendas and a mobile app for field workers, and claims 35+ customers. Named customers include Kroměříž, Karviná, Přerov and Uherský Brod, which signed contracts for it in 2022–2023. No AI or voice drafting is mentioned. Marbes s.r.o. was founded in 2010.'
- name: Therappic (BugBeaters)
  url: https://therappic.cz/
  ico: '09996605'
  since: 2021
  competes: adjacent
  maturity: established
  evidence: 'Sells Therappic, a client-record system for social services, from 1,050 CZK a month plus a 9,000 CZK setup fee. Named customers include SOS dětské vesničky, ZSI Kladno, Proxima Sociale and Rozum a Cit. No AI, recording or drafting is mentioned. BugBeaters s.r.o. was founded in March 2021.'
- name: ASPIK IS
  url: https://aspik.is/
  ico: '21218587'
  since: 2024
  competes: adjacent
  maturity: early
  evidence: 'Sells a record system for field and outpatient social services, from 3,000 CZK a month including VAT, where workers type notes into the individual plan. No AI, recording or drafting is mentioned, and no customer is named. Aspik IS s.r.o. was founded in February 2024.'
process:
  summary:
    today: 'A caseworker visits the family or meets the client, then writes the visit up in the case file by hand, logs every phone call, and writes court reports from that file [S2].'
    after: 'The visit is recorded with consent, the app drafts the note inside the office''s case-file software, and the caseworker only checks and approves it.'
  steps:
  - who: Caseworker
    today: 'Visits the family or meets the client'
    known: documented
    cites: [2]
    change: changes
    after: 'Visits with the client''s consent to record'
  - who: Caseworker
    today: 'Writes the visit record into the case file'
    known: documented
    cites: [2]
    change: changes
    after: 'Checks and approves the drafted record'
  - who: Caseworker
    today: 'Notes down every phone call'
    known: documented
    cites: [2]
    change: changes
    after: 'Dictates a short call note to the app'
  - who: Caseworker
    today: 'Writes reports for the court from the file'
    known: documented
    cites: [2]
    change: changes
    after: 'Edits a report drafted from the file'
  - who: '?'
    today: 'Who reviews the records, and when, is not known'
    known: unknown
    cites: []
    change: stays
    after: 'Unchanged: review stays with the office'
sources:
- type: arbitrage
  name: "Beam — Magic Notes in social care"
  gist: "British social-work note taker"
  why: "Magic Notes, launched in 2023, transcribes and summarises meetings for social workers and other frontline staff, and is used by 65,000 practitioners across over 200 organisations, local councils among them."
  url: https://www.socialenterprise.org.uk/member-updates/public-backs-use-of-beams-ai-tool-in-social-care/
  note: 'gb-beam-up: Social Enterprise UK member update, read 2026-09-18: "Launched in 2023, Magic
    Notes uses AI to transcribe and summarise meeting notes for social workers and other frontline
    professionals"; "used by 65,000 practitioners across over 200 organisations, including local
    authorities, central government, health, social care and employability services". beam.org,
    read 2026-09-18: "Since 2017"; "TRUSTED BY OVER 100,000 FRONTLINE WORKERS ACROSS HUNDREDS OF
    GOVERNMENT PARTNERS"; named councils Shropshire, Swindon, Oxfordshire, Birmingham, Kent, North
    Yorkshire; Magic Notes renamed Beam Notes. Resultsense 2026-08-07: Angus Council contract
    GBP 240,000, approved June 2026; the tool "captures conversations, distinguishes between
    speakers automatically, produces summaries with action points". Established: selling since
    2023 under a company founded 2017, named public customers.'
  date: '2026-01-27'
  signal: gb-beam-up
- type: complaint
  name: "VÚPSV — child-protection work at town halls"
  gist: "where caseworker time goes"
  why: "The state labour and social affairs research institute's study of child-protection offices at town halls: keeping the case file was the second-largest use of time, and administration ranked among the most burdensome and time-consuming tasks."
  url: https://katalog.vupsv.cz/fulltext/vz_326.pdf
  note: 'Barvíková, Svobodová, Šťastná, "Podmínky výkonu sociálně-právní ochrany dětí na úrovni
    obecních úřadů ORP", VÚPSV 2010, read by the research pass 2026-09-18. p. 24: "Na druhém
    místě se umístilo vedení a správa spisové dokumentace, která zabrala pracovníkům 13 % z
    celkového času"; other administration another 6 %. p. 64: "Kvantitativní šetření prokázalo,
    že administrativa jednoznačně patří mezi nejvíce zatěžující a nejvíce času pohlcující
    činnosti"; "Největší podíl na administrativě má vedení spisové dokumentace, záznamy z jednání
    s klientem, z šetření, dále pak zprávy pro účely soudu". p. 65: workers record every phone
    call in case of a complaint; the only remedy named is fewer cases per worker. Old (2010) but
    the only quantified time study found.'
  date: '2010-12-31'
- type: news
  name: "Novinky — Czechia is hundreds of child-protection workers short"
  gist: "the staff shortage"
  why: "There are 2,716 child-protection workers, and 20–30% more would be needed; in Brno's city office 9 of 12 caseworkers left within three years, over low pay and a psychologically demanding job."
  url: https://www.novinky.cz/clanek/ekonomika-nizke-platy-a-stres-v-cesku-chybi-stovky-zamestnancu-ospod-40514560
  note: 'Novinky.cz, Pavel Cechl, 28 Mar 2025, fetched 2026-09-18: "Vzhledem k tomu, že jich
    momentálně je 2716"; "by bylo vhodné navýšit počet pracovníků OSPOD o zhruba dvacet až
    třicet procent"; "V Brně na magistrátním OSPOD bylo dvanáct referentek. Během tří let se z
    toho devět otočilo". Reasons given: specialised, psychologically demanding work, low pay
    (Svaz měst a obcí). MPSV suggested recruitment bonuses of up to 5,000 CZK.'
  date: '2025-03-28'
- type: complaint
  name: "Sociální práce — the 2024 child-protection issue"
  gist: "time lost to paperwork"
  why: "The Czech social-work journal's 2024 issue on child protection names a rapid loss of time for direct work with clients because of the administrative burden."
  url: https://socialniprace.cz/nezarazene/2-2024-promeny-socialni-prace-v-socialne-pravni-ochrane-deti/
  note: 'Sociální práce / Sociálna práca, issue 2/2024 "Proměny sociální práce v SPOD", fetched
    2026-09-18: "rapidní úbytek času na přímou práci s klientem v důsledku administrativní zátěže".
    It is the issue''s call for papers, so it frames the problem rather than measuring it.'
  date: '2024-01-01'
- type: news
  name: "České důchody — AI drafts the records at a Zlín care home"
  gist: "a Czech care home already does it"
  why: "At a Zlín care home a conversation is recorded with the client's consent, AI transcribes it and drafts the written note, and the social worker checks and approves it; writing up one assessment is up to 75% faster."
  url: https://ceskeduchody.cz/zpravy/umela-inteligence-uz-pomaha-v-domovech-duchodcu
  note: 'ceskeduchody.cz, 10 Sep 2026, fetched 2026-09-18, on Domov pro seniory Burešov (Zlín),
    project DIGI-PÉČE Burešov: "Místo rozsáhlých ručních poznámek vznikne při rozhovoru se
    souhlasem klienta zvukový záznam. AI ho přepíše a připraví návrh zápisu"; "Sociální pracovník
    výstup zkontroluje, podle potřeby opraví nebo doplní a poté schválí"; "se čas potřebný ke
    zpracování jednoho šetření zkrátil až o 75 procent"; "roční úsporu na 1 286 pracovních hodin,
    tedy 561 971 Kč". No vendor is named. Also reported by Zlínský deník, 2 Jul 2026. Demand
    point: a Czech social-service provider paid for and measured this workflow.'
  date: '2026-09-10'
- type: regulation
  name: "Act No. 363/2021 Coll. (child-protection amendment)"
  gist: "no institutions for under-7s"
  why: "The amendment to the child-protection act that bars placing young children in institutional care: under 4 from January 2025, and under 7 from 1 January 2028."
  url: https://www.zakonyprolidi.cz/cs/2021-363
  note: 'Zákon č. 363/2021 Sb., kterým se mění zákon č. 359/1999 Sb., o sociálně-právní ochraně
    dětí, of 9 Sep 2021; divided effect 1.1.2022, 1.1.2025 and 1.1.2028 (zakonyprolidi.cz, read
    2026-09-18). Sociopoint Ostrava, 7 Nov 2024: "děti mladší 4 let nebudou umísťovány do
    ústavních zařízení" from 1.1.2025; "V roce 2028 se má hranice posunout ještě výše – na 7 let
    věku." MPSV''s own project statement (S7) reads the act as banning institutional placement
    of children under 7 "s účinností od 1. 1. 2028". The date is under 18 months from 2026-09-18.
    That the ban adds casework for child-protection offices is our reading of S7, flagged in
    Revisions; the ban binds placement, not the offices'' paperwork, so on the 2026-09-19 ladder it
    reaches the buyer only indirectly: Why now rung 1.'
  date: '2028-01-01'
- type: subsidy
  name: "MS2021+ — MPSV's child-protection support project"
  gist: "the ministry's 61M CZK project"
  why: "The labour ministry's EU-funded project, running from January 2026, to support child-protection practice ahead of the ban on placing children under 7 in institutions from 2028."
  url: https://ms21opendata.mssf.cz/SeznamOperaci_21_27.xml
  note: 'MS2021+ approved-project open data (data/lookup/ms21-public-projects.jsonl), project
    CZ.03.02.02/00/25_110/0006346, výzva 681797329, beneficiary MPSV (IČO 00551023), "Podpora
    systému sociálně-právní ochrany dětí a rozvoj kompetencí pracovníků SPOD", total 60,929,588
    CZK (EU 46,754,319), start 2026-01-01. Problem statement: "Projekt reaguje na potřebu
    podpory systému SPOD v oblasti prevence umisťování dětí do 7 let věku do ústavní péče ve
    vazbě na zákon o sociálně-právní ochraně dětí, jež s účinností od 1. 1. 2028 zakazuje
    umisťování dětí do 7 let věku do ústavní péče." Goal: methodological support for at least
    175 OSPOD workers. The url is the whole dataset; the project code is the key. It funds
    methodology, not software.'
  date: '2026-01-01'
- type: subsidy
  name: "MPSV — rules of the 2025 social-work grant"
  gist: "software and recording paid"
  why: "The state grant for social work at town halls and regions pays for software licences up to 7,000 CZK per full-time worker a year, and for phones and tablets used to take sound recordings."
  url: https://mpsv.gov.cz/cms/documents/afd916c3-85c3-2649-a02f-83061eb0481a/Metodika%20MPSV%20pro%20poskytov%C3%A1n%C3%AD%20p%C5%99%C3%ADsp%C4%9Bvku%20na%20v%C3%BDkon%20%C4%8Dinnost%C3%AD%20soci%C3%A1ln%C3%AD%20pr%C3%A1ce%202025.pdf
  note: 'Metodika MPSV pro poskytování příspěvku na výkon činností sociální práce 2025 (annex to
    ministerial order 7/2025), read by the research pass 2026-09-18; undated in the fetch, dated
    here by its budget year. p. 10: "Uznatelným výdajem je pořízení kancelářského softwaru MS
    Office ... případně další softwarová licence nezbytná pro výkon činností sociální práce.
    Maximální výše čerpání je 7 000 Kč na každý jeden celý úvazek na sociální práci a rok". p. 7:
    phones or tablets are eligible "pro pořizování snímků, obrazových a zvukových záznamů při
    výkonu činností sociální práce". p. 2: the total is set each year in the MPSV chapter of the
    state budget. Covers social work at kraje, ORP and POU, not the separate OSPOD grant.
    Recurring annual public money that may pay for this product. Rescore 2026-09-19: public
    money nearby, which earns no money point; it cannot lift one, since no 2026 round is on file
    and it does not cover the child-protection offices. Willing to pay search 2026-09-19: the
    2026 round is on file as S15, where the lift was tested and fails on the buyer; the child-protection offices''
    own payment is S16.'
  date: '2025-01-01'
- type: contract
  name: "Registr smluv — Kroměříž social-agenda system (1.03M CZK)"
  gist: "town halls buy case-file systems"
  why: "Kroměříž signed about 1.03M CZK for its social department's case-file system, one of several town halls that bought one in 2022–2023."
  url: https://www.hlidacstatu.cz/Detail/26197271
  note: 'Hlídač státu / registr smluv, read 2026-09-18: Kroměříž, "dodávka informačního systému
    sociálních agend", Marbes s.r.o. (IČO 29108373), 1,026,249 Kč incl. VAT, 16 Oct 2023. Same
    supplier: Karviná "Informační systém pro Odbor sociální" 1,154,918 Kč, 23 Nov 2022
    (/Detail/22461653); Přerov "Náhrada informačního systému Sociální agenda" 905,685 Kč, 21 Dec
    2022 (/Detail/22854053); Uherský Brod 615,890 Kč, 31 Mar 2023 (/Detail/23961193). CityVizor
    invoices show Kroměříž paying Marbes 43,881 Kč per support period for "TP Proxio sociální
    agenda" (cv-44-d72b06eb6661, Jan 2026). Recurring public spend on the software this app would
    plug into; not a price for this product.'
  date: '2023-10-16'
- type: arbitrage
  name: "voize"
  gist: "German voice care notes"
  why: "A Berlin company that turns what nurses and carers say into care documentation, used in more than 1,500 care facilities after a USD 50M Series A."
  url: https://www.ycombinator.com/companies/voize
  note: 'yc-voize: Y Combinator company page, read 2026-09-18: founded 2020, Berlin, team 140;
    "We build the AI companion for nurses, to create time for care"; speech recognition
    automates nursing documentation; 1,500+ care facilities, 100,000+ nurses; USD 50M Series A
    led by Balderton Capital with HV Capital and Y Combinator. Established, CEE-adjacent (DE).
    Company site voize.de redirects to voize.ai.'
  date: '2026-09-18'
  signal: yc-voize
- type: arbitrage
  name: "Northwoods"
  gist: "US caseworker documentation"
  why: "An Ohio company founded in 2003 whose software lets human-services caseworkers handle casework, documents and forms on the move, with named county customers."
  url: https://www.teamnorthwoods.com/about
  note: 'teamnorthwoods.com/about, read 2026-09-18: founded 2003, Dublin, OH; Traverse is "our
    flagship cloud-based software" for "mobile casework, document and forms management, and case
    discovery"; named customers Wood County DJFS (OH), Houston County DHS (MN), Carver County HHS
    (MN), Scott County HHS (MN), Mesa County DHS (CO), Jackson County JFS (OH). No AI note feature
    stated on that page; its AI product page returned 404. Not counted in the solution''s
    abroad clause.'
  date: '2026-09-18'
- type: gap-check
  name: "Czech check — record systems exist, visit-to-note drafting is thin"
  gist: "the Czech field, searched"
  why: "Twelve Czech query shapes, the business register and the contracts register: many Czech record systems for social services and town-hall social departments, one young one that drafts reports from typed notes, and none found that records a visit and drafts the note."
  url: https://arasoft.cz/
  note: 'Gap check 2026-09-18, two passes (this agent and a research sub-pass), Czech-language
    web search, ARES, Hlídač/registr smluv full text and data/lookup (cz-contract-parties,
    cityvizor-invoices, ms21). FOUND, DIRECT and EARLY: Flins by Arasoft s.r.o. (IČO 08977402,
    ARES 2020-02-25), whose AI module "dokáže automaticky zpracovávat rozsáhlé záznamy, generovat
    zprávy, podklady i souhrny o klientech během pár sekund" (arasoft.cz) from typed notes; no
    customer or price named. FOUND, ADJACENT: IRESOFT CYGNUS (26297850, 2002; 1,400+ providers;
    2 public buyers in cz-contract-parties; CYGNUS AI Asistent is chat and document search, voice
    only via keyboard dictation, vylepsujemecygnus.cz); Marbes PROXIO sociální agendy (29108373,
    2010; 16 OSPOD agendas, 35+ customers, proxio.cz/socialky; contracts Kroměříž, Karviná,
    Přerov, Uherský Brod); Therappic by BugBeaters (09996605, 2021; named customers; from 1,050
    CZK/month); ASPIK IS (21218587, 2024; from 3,000 CZK/month). SEEN, NOT OPENED OR NOT
    RELEVANT: eQuip (Rytmus), Azylák, IS PePa, Evička2, Chytrá organizace, HIPPO (record systems
    for social services, surfaced by the control query below); EVIX by Dalibor Smitka (records for
    children''s homes, no AI); ORTEX spol. s r.o. (00529745) sold "vedení agendy OSPOD" to
    Stříbro for 121,000 Kč in 2021, product not verified; DelpSys (03605400) sells a 990 CZK AI
    training course, not a tool; Domovy online sells an enquiry chatbot; horizontal Czech
    transcription (NEWTON Technologies 28479777 / Beey, Česky.AI, coalbrain.cz, Notta) has no
    social-work templates. VITA software (61060631) was checked and sells no social agenda.
    UNKNOWN: the supplier of the Burešov care home''s AI drafting tool (S5) is not named in three
    articles. Not in own-funded-ledger. POSITIVE CONTROLS PASSED: the same Czech web search at
    "česká firma zabezpečení mobilního bankovnictví software" surfaced Wultra (Wultra App
    Shielding), the p-0017 incumbent; and a domain control, "evidenční software pro poskytovatele
    sociálních služeb dokumentace klientů individuální plánování", surfaced ten Czech record
    systems including Flins and Therappic. Gap 1 rests on Flins being direct and early; the
    adjacent entries move nothing.'
  date: '2026-09-18'
  queries:
    - "AI zápis z rozhovoru sociální pracovník automatický záznam OSPOD aplikace"
    - "umělá inteligence pro sociální služby dokumentace záznam o průběhu služby hlasem aplikace pro pracovníky v sociálních službách"
    - "software pro OSPOD evidence spisové dokumentace sociálně-právní ochrana dětí modul AI asistent"
    - "evidenční software pro poskytovatele sociálních služeb dokumentace klientů individuální plánování"
    - "AI přepis rozhovoru sociální pracovník záznam"
    - "umělá inteligence OSPOD záznam z šetření"
    - "AI asistent pro sociální služby dokumentace hlasem"
    - "hlasový zápis dokumentace sociální služby aplikace"
    - "automatický zápis z jednání sociální pracovník AI"
    - "DIGI-PÉČE Burešov umělá inteligence dodavatel nástroj sociální šetření"
    - "CYGNUS IRESOFT přepis řeči hlasové zadávání záznamů AI sociální služby průběh služby"
    - "NEWTON Technologies Beey sociální pracovníci OR sociální služby OR OSPOD přepis"
    - "česká firma zabezpečení mobilního bankovnictví software"
  checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
  expires: '2026-12-17'
- type: price
  url: https://ceskeduchody.cz/zpravy/umela-inteligence-uz-pomaha-v-domovech-duchodcu
  name: "Burešov care home — hand-written records, costed"
  gist: "hand-written records a year"
  why: "What the hand-written records an AI draft replaced cost one Czech care home in a year: 1,286 working hours."
  note: 'Manual equivalent from S5 (ceskeduchody.cz, 10 Sep 2026): the home put the annual saving
    at "1 286 pracovních hodin, tedy 561 971 Kč" after AI drafting cut the time per assessment by
    up to 75 %. So 561,971 CZK is what those hours of writing cost by hand each year, about 437
    CZK an hour. One buyer. Tagged dims: [money] on 2026-09-19 (rescore): the manual equivalent
    of this job, an asking receipt.'
  date: '2026-09-10'
  payer: 'Domov pro seniory Burešov, a town-run care home in Zlín'
  amount_czk: 561971
  unit: per-year
  basis: manual-equivalent
  dims: [money]
- type: statistic
  name: "Deník veřejné správy — what child protection costs"
  gist: "about 1.5bn CZK a year"
  why: "About 1.5bn CZK a year is spent on the work of child-protection offices, 14.4% of all child-protection spending."
  url: https://www.dvs.cz/clanek.asp?id=6759063
  note: 'Deník veřejné správy, M. Macela, 30 Aug 2018, fetched by the research pass 2026-09-18: "Na
    jejich činnost je ročně vynakládáno cca 1,5 mld. Kč (tj. 14,4 % celkových výdajů)." Old, but
    the recurring annual public spend on OSPOD work. Rescore 2026-09-19: dims emptied; a
    statistic is neither a price for this job nor a programme that could lift one.'
  date: '2018-08-30'
  dims: []
- type: subsidy
  name: "MPSV — the 2026 round of the social-work grant"
  gist: "software and recording, 2026"
  why: "The labour ministry's 2026 grant pays part of the cost of social work at regions and town halls, including software licences and the phones or tablets used for sound recordings. Child-protection work is left out."
  url: https://mpsv.gov.cz/cms/documents/90a700c6-b603-3a3a-0d3f-aff7ae1b1ac0/Metodika%20SP%202026.docx
  note: 'Willing to pay search 2026-09-19. mpsv.gov.cz/dotace-2026 (last updated 5 Mar 2026)
    lists "Vyhlášení dotačního řízení na výkon činností sociální práce 2026" and "Metodika MPSV
    pro poskytování příspěvku na výkon činností sociální práce 2026" (Příloha č. 1 k příkazu
    ministra č. 2/2026); both documents read on this date. THE CALL, "Vypracováno, zveřejněno
    dne: 25. února 2026": "Dotaci lze poskytnout pouze krajům, hl. m. Praze, obcím s rozšířenou
    působností a obcím s pověřeným obecním úřadem"; applications "od zveřejnění výzvy do 2. dubna
    2026", evaluation 7–17 April, corrections 20 April–7 May 2026; purpose code 13015. THE
    METHODOLOGY, part III: "Dotace má charakter účelové neinvestiční dotace, která je určena k
    částečnému pokrytí osobních a provozních nákladů". Part IV, software: "Uznatelným výdajem je
    pořízení kancelářského softwaru MS Office ... případně další softwarová licence nezbytná pro
    výkon činností sociální práce. Maximální výše čerpání je 7 000 Kč na každý jeden celý úvazek
    na sociální práci a rok". Phones and tablets: "pro pořizování snímků, obrazových a zvukových
    záznamů při výkonu činností sociální práce", capped at 6,500 CZK a tablet and 8,000 CZK a
    phone. Title and part I exclude "agendy sociálně-právní ochrany dětí". AWARDED IN 2026:
    Statutární město Děčín, an ORP, budget change no. 103 "Dotace na výkon sociální práce",
    approved by the council 18 Aug 2026 (resolution RM 26 14 35 01; mmdecin.cz, budget changes
    approved in August 2026): "přerozdělení rozdílu obdržených finančních prostředků na výkon
    přenesené působnosti v oblasti sociální práce", on budget lines under purpose code 13015.
    Ostrava-Jih''s 2026 budget report plans "neinvestiční transfer ze SR na výkon sociální práce
    ze SR 4 910 tis. Kč". THE LIFT (SCORING.md MONEY) WAS TESTED AND FAILS on the buyer
    condition, decided 2026-09-19 by the coordinator under the owner''s delegation: the title and
    brief name the child-protection offices as the buyer that is short of staff, and this grant
    excludes their work. The other four conditions hold: the base is 1 from S13; a software
    licence and a recording device for social work are eligible spend; it was awarded to town
    halls in 2026, within 12 months of updated; it covers part of the cost with a cap per
    worker. The child-protection offices are paid under S16, which repays their costs and
    cannot lift. So money stays 1 and this source carries dims: [], public money nearby.'
  date: '2026-02-25'
  dims: []
- type: subsidy
  name: "MPSV — the state's payment for child-protection work"
  gist: "child-protection costs repaid"
  why: "The state repays the town halls that run child-protection offices the cost of that work, including the software their caseworkers use and recorders for meetings with children and parents."
  url: https://mpsv.gov.cz/cms/documents/915e5dc6-47b5-d2ee-de24-33d7b307280c/Metodika+transferu+SPOD+od+roku+2022_ve+zn%C4%9Bn%C3%AD+dodatku+%C4%8D.+2+(platnost+od+13.1.2023).pdf
  note: 'Willing to pay search 2026-09-19. "Metodika Ministerstva práce a sociálních věcí pro
    poskytování transferu ze státního rozpočtu obcím s rozšířenou působností a hl. m. Praze na
    financování výkonu přenesené působnosti v oblasti sociálně-právní ochrany dětí", příloha k
    PM č. 5/2022 ve znění dodatku č. 2, valid from 13 Jan 2023, read on this date; no later
    version was found. Its basis, Act 359/1999 § 58(1) (zakonyprolidi.cz, read on this date):
    "Obcím s rozšířenou působností se ze státního rozpočtu poskytuje náhrada výdajů" connected
    with child protection. Paid ex-ante as a lump sum per post; where actual costs exceed it,
    the town may ask "o dodatečné prostředky na dokrytí skutečných a odůvodněných výdajů v
    agendě SPOD" after the year. Item 26: "Software, který používají pracovníci vykonávající
    agendu SPOD ... Z transferu lze hradit roční paušál a běžná údržba ke speciálnímu programu
    (software)"; item 18: recording equipment "pro pořizování obrazových a zvukových záznamů z
    jednání zaměstnanců OSPOD s dítětem, rodiči". Still paid in 2026: Ostrava-Jih''s 2026 budget
    report plans "neinvestiční transfer na financování sociálně-právní ochrany dětí ze SR", 22,092
    thousand CZK. This is the "grant of their own" S8 refers to. NOT A LIFT: it repays the cost
    of the work, so the office does not co-pay (SCORING.md MONEY, the fifth condition). dims: []
    so it backs no score.'
  date: '2023-01-13'
  dims: []
- type: contract
  name: "Registr smluv — what town halls and care homes bought, 2025–2026"
  gist: "records and AI add-ons, not this"
  why: "The public contracts register shows town halls and care homes paying for client-record systems and a general AI assistant in 2025–2026, and no contract for software that records a visit and drafts the note."
  url: https://smlouvy.gov.cz/smlouva/31677812
  note: 'Hlídač státu API full-text search of the contracts register, 2026-09-19, contract texts
    read where named. QUERIES (hits): "Flins" (7); icoPrijemce:08977402 (3); "Sofal" (1);
    "umělá inteligence" AND (OSPOD OR "sociálně-právní ochrany dětí") (9, none relevant);
    "umělá inteligence" AND "sociální práce" (59, none relevant); "přepis" AND ("sociální
    pracovník" OR "sociální pracovníci" OR OSPOD) (300, no transcription purchase); Beey (45);
    ("hlasový záznam" OR "hlasové zadávání" OR "přepis řeči") AND sociální (90, phone
    contracts); and since 2024-09-19: "OSPOD" AND (software OR licence OR aplikace) (86); AI
    AND social departments or social services (154); ("přepis" OR "převod řeči na text") AND
    social work (12); "sociálně-právní ochrany dětí" AND (software OR licence OR "informační
    systém") (91); plus Cygnus AND AI (93), icoPrijemce Therappic 09996605 (2), ASPIK 21218587
    (0), "DIGI-PÉČE" OR Burešov (956), and ico:70851042 since 2025-06-01 (73). FOUND: (1) Městská
    část Praha 7 and Arasoft s.r.o., registr smluv 31677812, 8 Jan 2025, "Licenční smlouva ...
    aplikace Flins a moduly Sofal a Eurad". Clause 2.1: licence "pro činnost uživatele související
    s činností sociálních pedagogů a sledování podpory klientů v rámci projektů ESF"; 2.2:
    "základní licenci Flins upravenou dle požadavků uživatele na evidenci klientů a výkonů", Eurad
    for OPZ+ project monitoring, Sofal "určený ke sběru dat a měření dopadu aktivit"; 5.2:
    "poplatek 89 000 Kč ročně"; to 31 Dec 2025, then renewing by 2 years; it replaces all earlier
    Flins contracts. No AI module is listed. The AI module went live later: neposeda.org, 18 Sep
    2025, "testování a pilotní fáze probíhaly v letech 2023–2024, s ostrým nasazením modulu od
    září 2025", piloted at Neposeda z.ú., "připravuje se rozšíření do cca 60 organizací"
    (ksocp.ff.cuni.cz describes the same project). So Praha 7 is a customer of Flins''s records,
    not of this job; Flins''s since moves 2020 → 2025 and it stays early. (2) IRESOFT CYGNUS AI
    Asistent: Domov Seniorů Dobříš, 38218545, 12 May 2026, addendum 2, "AI Asistent 100
    kliento-služeb 1 234 Kč" a month excl. VAT; its annex: "Modul AI Asistent umožňuje využívat
    funkce umělé inteligence integrované v počítačovém programu, zejména AI chat, generování a
    úpravy textů, vyhledávání odpovědí nad zpřístupněnými nebo nahranými dokumenty a zpracování
    uživatelských dotazů". Centrum služeb pro seniory Kyjov, 38345725, 11 Jun 2026, AI Asistent
    1,734 CZK a month; Domov sociálních služeb Slatiňany, 39203958, 18 Aug 2026, "rozšíření
    licence o modul AI Asistent" (metadata only; its value covers the whole licence).
    iscygnus.cz/podminky-cygnus-ai-asistent describes a virtual assistant answering questions on
    the user''s own directives and uploaded documents, plus a general AI chat. It does not record
    a visit or turn it into the note, so IRESOFT stays adjacent and these are not receipts. (3)
    Case-file systems, the S9 kind, inside 24 months: Kaplice, 33660977, 12 Jun 2025, ORTEX,
    "Informační systém pro sociální agendy a SPOD", 645,000 CZK, IROP eGovernment funded;
    Beroun, 35233201, 15 Oct 2025, Marbes, "Rozvoj PROXIO o dodávku modulu Sociální agendy",
    650,000 CZK excl. VAT (metadata only); Hlinsko, 37236213, 19 Mar 2026, Marbes, "Dodávka,
    implementace a podpora informačního systému sociálních agend", no value published. Records,
    not drafting. (4) Domov pro seniory Burešov (S5), 37213269, 13 Mar 2026: a Nadace ČEZ grant
    of 150,000 CZK for "DIGI-PÉČE BUREŠOV - Digitální základna pro moderní sociální práci"; it
    names no supplier or price for the tool, and none of the home''s 73 contracts since June 2025
    buys it. (5) NEWTON Technologies (Beey) sells transcription to courts, police, universities
    and broadcasters, e.g. Policejní prezidium 38726332, 8 Jul 2026, 60,000 CZK excl. VAT; no
    social department. POSITIVE CONTROLS PASSED: "asistent vykazování" returns the paid ICZ
    contracts p-0036 restates (Znojmo 36862509, FN Brno 31554612, Kolín 34396449); "sociální
    agenda" AND icoPrijemce:29108373 returns S9''s Přerov, Kroměříž and Uherský Brod contracts.
    The method finds paid software contracts of this shape; none buys visit-note drafting.'
  date: '2025-01-08'
  dims: []
created: '2026-09-18'
updated: '2026-09-19'
---

Czech social workers spend much of their day writing up visits and meetings, while child-protection offices are hundreds of workers short [S2,S3].

- Paperwork and the case file took about a fifth of caseworkers' time [S2].
- 2,716 child-protection workers are employed, and 20–30% more are needed [S3].
- A Czech care home cut assessment write-ups by up to 75% with AI [S5].

OSPOD — the child-protection department of a town hall — works with children at risk and their families [S2]. A 2010 study by the state's research institute for labour and social affairs measured where its time goes [S2]:

- Keeping the case file was the second-largest use of time, at 13%, and other administration took another 6% [S2].
- Administration ranked among the most burdensome and time-consuming tasks [S2]. The case file, records of client meetings and home visits, and reports for the court make up most of it [S2].
- Workers note down every phone call in case of a complaint [S2].

The Czech social-work journal's 2024 issue on child protection names a rapid loss of time for direct work with clients because of the administrative burden [S4].

The care home is Domov pro seniory Burešov in Zlín, run by the town [S5]. With the client's consent a conversation is recorded, AI transcribes it and drafts the written note, and the social worker checks, corrects and approves it [S5]. The home counts 1,286 working hours saved a year [S5].

Existing non-solutions: One young Czech record system drafts reports from notes already typed, and no Czech firm was found selling a tool that records the visit [S12].

- Town halls' and care homes' case-file systems store notes, but none drafts them [S12].
- The best-known one's AI assistant chats and writes text, but records no visit [S12,S17].
- Czech transcription tools exist, but none is built for social-work case files [S12].
- That assistant joined the paid licence in June 2026 and searches documents [S12]. Voice entry there is the phone keyboard's own dictation [S12].
- Care homes have signed for that assistant as a paid add-on since May 2026 [S17].
- The young system drafts reports and client summaries from notes a worker has already typed [S12].
- The care home in Zlín has not named who supplies its tool [S5].

The sellers are listed under [Market gap](#competition).

Why now: Child-protection offices are short of staff, and from January 2028 no child under 7 may be placed in an institution [S3,S6].

- A caseworker's hours go to the case file instead of the family [S2,S4].
- Brno's city office lost 9 of 12 caseworkers in three years [S3].
- One care home saved 1,286 hours a year once AI drafted its records [S5].

The reasons given for leaving are low pay and a psychologically demanding job [S3]. The labour ministry suggested bonuses of up to 5,000 CZK to recruit and keep staff [S3].

The dates behind the new work:

- From 1 January 2025 children under 4 may no longer be placed in institutions [S6].
- From 1 January 2028 the limit rises to children under 7 [S6,S7].
- In January 2026 the labour ministry started a 60.9M CZK EU-funded project to support child-protection workers ahead of that ban [S7].
- In September 2026 the Zlín care home's results were reported [S5].

Who pays: Nobody on file pays for this yet; the 2026 state grant pays town halls' software for other social workers, not child-protection offices [S15,S17].

- The grant pays other social workers' software, up to 7,000 CZK a worker [S15].
- Child-protection offices are left out; the state repays their costs in full [S15,S16].
- Town halls signed contracts of 0.6–1.2M CZK for social-department case-file systems [S9].

The 2026 grant also pays for phones and tablets that social workers use to take photos and sound recordings on the job [S15]. It pays only part of the cost, and it leaves out child-protection work [S15]. Town halls applied by 2 April 2026, and Děčín's council recorded its grant as received in August 2026 [S15]. The 2025 rules set the same software limit, and the grant's total is set each year in the state budget [S8].

The child-protection offices have a payment of their own: the state repays the cost of their work [S16]. It covers the software their caseworkers use and recorders for meetings with children and parents [S16]. It is paid at the start of the year and can be topped up afterwards if the costs run higher [S16].

- About 1.5bn CZK a year was spent on child-protection work in 2018 [S14].
- Kroměříž, Karviná, Přerov and Uherský Brod bought such systems in 2022–2023 [S9].
- Kroměříž also pays for support of its system several times a year [S9].
- Three more town halls signed for such systems in 2025–2026 [S17].
- Town halls and care homes also paid for client records and a general AI assistant [S17].
- None of these contracts buys software that records a visit and drafts the note [S17].
- The Zlín care home's digital project got a 150,000 CZK foundation grant in March 2026 [S17].
- What hand-written records cost one care home is in the table of what one buyer pays [S5].

Solved elsewhere: Two established companies sell this abroad, one to British councils' social workers and one to German care homes [S1,S10].

- A British firm drafts social-work notes for 65,000 practitioners, councils among them [S1].
- A German firm turns carers' speech into care records in 1,500+ care facilities [S10].
- A US firm founded in 2003 sells caseworkers mobile casework and forms software [S11].

The British one records and transcribes meetings and drafts summaries, in over 200 organisations [S1]. The German one turns what nurses and carers say into their care documentation [S10].

## First moves

1. Build a phone app that records a home visit with the family's consent and drafts the case note for the caseworker to check. The caseworker taps record at the start of the visit, and the app turns the conversation into a draft record written the way a child-protection file needs it: who was there, what was seen, what was agreed. The caseworker corrects and approves it, and nothing enters the file without that approval. A Czech care home already works this way, as [The opportunity](#opportunity) shows, so start from what it does.
2. Visit the heads of social departments at a few town halls and ask to pilot the app with their child-protection team. Choose towns that already bought a case-file system for their social department, because they have shown they spend on this kind of software; see [Willing to pay](#willing-to-pay). Their teams are short of staff and losing people, as [Why now](#why-now) explains, so an hour saved on every visit is easy to explain. The state grant for social work can pay part of the licence for a town's other social workers, and the state repays the software a child-protection team uses.
3. Connect the draft to the case-file systems town halls and care homes already run, starting with the most common one. Caseworkers will not copy text from one app into another, so the approved record has to land in the file they already keep. The systems in use are listed under [Market gap](#competition); none of them drafts the note today.
4. Keep the recordings and the drafts on servers in Czechia, and delete each recording once its record is approved. The files hold sensitive data about children and families, so a town hall will ask where the data lives before it asks about the price. Say it plainly in the first meeting, because it is the question that stops a pilot.
5. Once one team uses it daily, offer the same app to care homes and other social services. Their social workers write the same kind of records, and one Czech home has already measured what it saves; see [Willing to pay](#willing-to-pay). Abroad the same pattern sells both to councils and to care homes, as [Validated abroad](#validated-abroad) shows.

## Revisions

2026-09-18 · record created — Minted from the monthly broad scan's gb-beam-up signal after Czech research. Proof 3 on Beam (Britain) and voize (Germany), both established [S1,S10], with Northwoods (US) on the ledger but not counted in the solution's abroad clause because no AI drafting is stated on its pages [S11]. Money 2 on recurring public spend: the annual social-work grant that pays software licences and sound recording [S8], town halls' case-file system contracts [S9] and the 2018 figure for yearly child-protection spending [S14]. Urgency 3: the 1 January 2028 ban on placing children under 7 in institutions, under 18 months away [S6,S7], plus sources under 90 days old [S5]. Flagged as inference: that the ban adds casework for child-protection offices is our reading of the ministry's own project statement [S7]; no source counts the extra work. Demand 2 on the 2010 time study, the 2024 journal issue, the 2025 staffing report and the Zlín care home's measured saving [S2,S3,S4,S5]. Gap 1: Flins sells AI drafting of reports from typed notes and is early, so the field is contested; four adjacent record systems are recorded and move nothing [S12]. The brief's "more of their time than almost anything else" rests on the 2010 study ranking administration among the most time-consuming tasks and the 2024 journal issue [S2,S4]. The price receipt is a manual equivalent: the hours of hand-written records one care home saved, costed by the home itself [S13].

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 3 → 1 and Willing to pay 2 → 1, so the total goes 11 → 8 and the band falls from PRIME to STRONG. Why now: the old 3 was deadline 2 for the 1 January 2028 ban on placing children under 7 in institutions [S6,S7], plus the freshness point, which is retired. The ban is enacted and under 18 months away, but it binds placement, not the offices' paperwork. That it adds casework for the offices is our reading of S7, already flagged on 2026-09-18. A duty that reaches the buyer only indirectly is rung 1. Willing to pay: the old 2 rested on public money: the social-work grant [S8], town halls' contracts for case-file systems [S9] and a 2018 spending figure [S14]. None of these is a price for this job. Tagging pass: the one receipt on file for this job is its manual equivalent, what hand-written records cost the Burešov care home a year, 561,971 CZK [S13]. It is now tagged money: an asking receipt, rung 1. The case-file contracts [S9] buy the systems this app would plug into, not the drafting, and stay public money nearby. ORTEX's 121,000 CZK sale to Stříbro (2021, in the gap check [S12]) is for case records, not drafting, and is older than 24 months. The care home paid for its AI drafting tool [S5], but no amount or contract is on file. A Hlídač search on 2026-09-19 ("DIGI-PÉČE", "Domov pro seniory Burešov") found none. The lift is not on file either: the grant's rules on file are for 2025, with no 2026 round, and they cover social work at regions and town halls but not the child-protection offices [S8]. S14, a 2018 statistic tagged money, is now dims: [], since a statistic is not a programme. Notes: S6, S8 and S14 no longer name the deadline sub-score or money 2. Body: the 2 `[Competition](#competition)` links now read `[Market gap](#competition)`. Why now's opening sentence says no child under 7 may be placed in an institution from January 2028; the old "they must keep children under 7 out of institutional care" put the duty on the offices. Willing to pay now opens by saying no price paid for this is on file, and a new sentence says the grant covers social work at regions and town halls, not the child-protection offices [S8]. Move 2 no longer says the grant can pay a child-protection team's licence. No other score, status, marker or `entry` gate changed.

2026-09-19 · Willing to pay search, owner-approved — No score moved: money stays 1, `score` stays 8, band STRONG, gap 1, status candidate. The rescore above held money at 1 because no 2026 round of the social-work grant was on file and that grant leaves out the child-protection offices [S8]. The search looked for the round, for what the offices themselves are paid, and for any Czech office that paid for this job in the last 24 months.

The 2026 round was found and is now S15. The call was published on 25 February 2026, and town halls applied by 2 April 2026. Ministerial order 2/2026 keeps a software licence for social work as eligible spend, up to 7,000 CZK per full-time worker, and phones or tablets for sound recordings [S15]. Děčín's council recorded its 2026 grant as received on 18 August 2026 [S15]. The lift was tested and fails on SCORING.md's condition that the programme names this record's buyer type as eligible. Four conditions hold: the base price [S13], the eligible spend, the 2026 award, and the town's co-pay. The fifth fails. Decided on 2026-09-19 by the coordinator, under the owner's delegation: the title and brief name the child-protection offices as the ones short of staff, and the grant excludes their work [S15]. The offices' own money is S16, a state payment under § 58 of the child-protection act that repays the cost of their work, software and recorders included [S16]. It cannot lift either, because the state pays in full, topping up any shortfall after the year, so the office does not co-pay [S16]. So money stays 1. S15, S16 and S17 all carry `dims: []`; only the price receipt S13 backs money. During this pass S15 briefly carried `dims: [money]` and money 2; both were reverted on the same date by that decision.

No paid receipt for this job was found. The contracts-register search, 17 queries and 2 positive controls through the Hlídač státu API, with the named texts read, is S17. Praha 7's town hall pays Arasoft 89,000 CZK a year for Flins client records and two project modules under a contract of 8 January 2025. It lists no AI module, and the AI module went live only in September 2025, so this is a customer of the records system, not of this job [S17]. Care homes pay IRESOFT for its CYGNUS AI assistant from May 2026, for example 1,234 CZK a month at Domov Seniorů Dobříš. The contract describes AI chat, writing and editing text, and answers from documents. It does not record a visit and draft the case note, so it is adjacent and not a receipt [S17]. Kaplice, Beroun and Hlinsko bought social-agenda case-file systems in 2025–2026, the kind S9 already records. The Burešov care home got a 150,000 CZK Nadace ČEZ grant for its digital project in March 2026, but no supplier or price for its tool is on file. Beey sells transcription to courts and police, not to social departments. Positive controls passed: the same method returns p-0036's paid coding-software contracts and S9's case-file contracts.

Ledger: Flins's `since` moves 2020 → 2025. The field reads the year it started selling this, and its AI module went live in September 2025 after a pilot at one organisation [S17]. It stays early, and its evidence now names the Praha 7 contract and says it lists no AI module; "names no customer" is gone. IRESOFT stays adjacent, decided on 2026-09-19 by the coordinator: its assistant is a chat and document assistant sold to social-service providers such as care homes, voice entry is keyboard dictation, and it neither records a visit and drafts the case note nor sells to child-protection offices [S12,S17]. Its evidence now says so, and adds that the assistant writes or edits text on request and that care homes signed for it from May 2026.

Body: Willing to pay now opens by saying nobody on file pays for this yet, and that the 2026 grant pays town halls' software for other social workers, not child-protection offices [S15,S17]. Its first three items are the grant's software limit, the offices left out and repaid in full, and the case-file contracts [S15,S16,S9]. That the state repays the offices "in full" rests on S16's top-up of actual justified costs, flagged here as our reading. The grant paragraph now cites the 2026 rules, and a new paragraph describes the child-protection payment [S16]. Four items were added below: three more case-file contracts, the paid records and AI assistant, no contract for this job, and the care home's foundation grant [S17]. Market gap's second item now says the assistant chats and writes text but records no visit, and a new item says care homes have signed for it since May 2026 [S12,S17]. Move 2 now says the grant can pay part of the licence for a town's other social workers and that the state repays the software a child-protection team uses. S8's note gained a dated line pointing to S15 and S16. Searched and not added as sources: Ostrava-Jih's 2026 budget report, which plans both payments and is quoted in the notes on S15 and S16; the ministry's page for the child-protection payment, which returned 404; and the 2020 rules of the old child-protection grant, which S16 replaced. Not changed: title, brief, solution, good_for, `entry`, urgency, proof, demand, gap and status.
