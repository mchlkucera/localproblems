---
id: p-0038
region: cz
title: 'Czech village mayors must handle the money and hospital consents of adults who can''t manage alone. A bill would let them hand this on from July 2027.'
brief: 'When a court decides an adult can''t manage alone and nobody else can help, their town or village is made responsible [S2,S5]. In a village with no staff, the mayor does it, which can mean signing hospital consents at weekends [S1,S2].'
solution: 'Build case-management software for the town offices that take on this work, with a file per person, their money and the yearly accounts for the court, as 1 company already does in Sweden.'
good_for: 'Someone who can sell software to town halls and understands social work.'
category: govtech
geo: CZ-national
score: 4
scores:
  proof: 1
  money: 1
  urgency: 0
  demand: 2
  gap: 0
status: watching
entry:
  level: hard
  buyer: public
  permission: none
  incumbents: direct
  integration: software
  money: bootstrap
  why: 'Easier: towns already buy add-ons to their office software for this work, and no licence is needed to sell one. Harder: the buyers are public bodies with yearly budgets, and established suppliers of town-hall software already sell this.'
comps:
- name: Provisum
  url: https://provisum.se/
  geo: SE
  since: 2013
  traction: 'A case system for the Swedish municipal offices that supervise people running adults'' affairs (överförmyndare), developed with
    the cities of Stockholm and Västerås and offered to every Swedish office through the municipal
    cooperative Sambruk with no licence fee; the yearly cost depends on a town''s population
    (provisum.se, read 2026). Its supplier, Resursen Sverige AB, was registered in 2013
    (allabolag.se). No count of towns using it is published.'
locals:
- name: Marbes (PROXIO)
  url: https://www.proxio.cz/
  ico: '25212079'
  since: 2018
  competes: direct
  maturity: established
  evidence: 'Sells PROXIO, a family of information systems for public administration, with a
    module for towns that run the affairs of adults in their care. Named customers: Hradec Králové
    bought that module from MARBES CONSULTING s.r.o. in July 2018, and Chrudim ordered further work
    on the module, tracking a person''s money on several accounts at once, from Marbes s.r.o. (IČO
    29108373) in 2022 [S9]. Marbes says it has supplied software since 1993.'
- name: VERA (VERA Radnice)
  ico: '62587978'
  since: 2022
  competes: direct
  maturity: established
  evidence: 'Sells VERA Radnice, town-hall software with a module for this work that keeps each
    person''s details and plans the official''s tasks. Named customer: the town of Rožnov pod
    Radhoštěm bought its social-department software in November 2022, with this work and a cash
    ledger in the order [S9].'
- name: Aptien
  url: https://aptien.com/cs/evidence-verejne-opatrovnictvi
  ico: '26397668'
  competes: direct
  maturity: early
  evidence: 'Sells an online register for the officials who do this work, with a file per person, their money,
    deadlines and printed yearly reports, on top of a general records tool for firms and towns. It
    names no town that bought it for this work, and no contract for it was found in the state
    contracts register [S9]. Aptien Labs s.r.o. has existed since 2005.'
- name: ICZ (traffic-offence system)
  url: https://www.iczgroup.com/
  ico: '25145444'
  since: 2023
  competes: adjacent
  maturity: established
  evidence: 'Sells a system for handling traffic offences, the other agenda small municipalities
    call a burden. Named customers: the cities of Most and Chomutov signed for it in 2023 [S9]. It
    serves large towns and their camera-caught traffic offences; it does not help with this work.
    ICZ a.s. has traded since 1997.'
process:
  summary:
    today: 'A court makes the village responsible for an adult who can''t manage alone, and the mayor or an official then handles the person''s money, court hearings, hospital consents and yearly accounts, often without training [S1,S2,S5].'
    after: 'A town office that takes on people from several villages keeps each person''s file, money and deadlines in one place, and prints the yearly accounts from it.'
  steps:
  - who: Court
    today: 'Makes the village responsible for the person'
    known: documented
    cites: [2, 5]
    change: stays
    after: 'Unchanged: the court still decides this'
  - who: Mayor or a town-hall official
    today: 'Takes on the work, often untrained'
    known: documented
    cites: [1, 2]
    change: stays
    after: 'Unchanged: the town still names who does it'
  - who: The mayor or official
    today: 'Keeps the person''s money and property'
    known: documented
    cites: [5, 9]
    change: changes
    after: 'Keeps each account in one shared ledger'
  - who: The mayor
    today: 'Goes to court hearings and gives hospital consents'
    known: documented
    cites: [1]
    change: stays
    after: 'Unchanged: these still need a person'
  - who: The mayor or official
    today: 'Sends the court yearly accounts by 30 June'
    known: documented
    cites: [5]
    change: changes
    after: 'Prints the yearly accounts from the ledger'
  - who: '?'
    today: 'How deadlines across many people are tracked is not known'
    known: unknown
    cites: []
    change: changes
    after: 'The software reminds the office of each deadline'
sources:
- type: complaint
  name: "Ombudsman — state tasks on small municipalities"
  gist: "the 2,331-municipality survey"
  why: "The public defender of rights surveyed 2,191 small villages and 140 larger towns in April–May 2025. Among those that do each task, 69% call misdemeanour cases and 61% call looking after these adults a burden, and mayors describe court hearings, hospital consents and losing track of the people in their care."
  url: https://www.ochrance.cz/uploads-import/ESO/V%C3%BDzkumn%C3%A1%20zpr%C3%A1va%203626-24-VBG.pdf
  note: 'ombud-male-obce-statni-sprava: Výzkumná zpráva Výkon státní správy na malých obcích, sp.
    zn. 3626/2024/VOP/VBG, č. j. KVOP-12306/2026, read in full 2026-09-18 (pdftotext). Survey
    April–May 2025: 2,191 type-I municipalities (36% response) and 140 of 183 type-II (77%). Graph
    4 (N = 2,331): public guardianship performed by 1,065 (46%), misdemeanour proceedings by only
    412 (18%) — 1,919 do not handle misdemeanours themselves. Graph 6: burdensome (rather + very)
    for misdemeanours 69% of n = 391 and for guardianship 61% of n = 1,033 — THE SHARES ARE OF THE
    MUNICIPALITIES THAT DO THE AGENDA, not of all respondents. Summary point 2: about two fifths
    see guardianship (39%) and misdemeanours (38%) as of little benefit. Summary point 6: funding
    judged not or only partly covering costs by 61% above 3,000 inhabitants, rising to 90% above
    10,000 (that last group is n = 10). Chapter 9 quotes, verbatim: "Jezdím často na soudní stání
    kolem nich, pak si práci z ostatních oblastí nosím domů"; "pokud po mně chtějí o víkendu v
    nemocnici souhlas se zákrokem"; "začínám ztrácet přehled"; "Umožnit přenos agendy veřejného
    opatrovnictví veřejnoprávní smlouvou."; misdemeanours: "Náklady spojené s odměnami právníků a
    členů komise výrazně převyšují přínosy z vybraných pokut". Some municipalities already use
    public-law contracts, mostly with ORP towns. No recommendations section, no staff hours, no
    ward counts in the report.'
  date: '2026-03-10'
  signal: ombud-male-obce-statni-sprava
  dims: [demand]
- type: regulation
  name: "The bill — the justice ministry's impact assessment"
  gist: "the bill and its numbers"
  why: "The justice ministry's bill would let a village hand the affairs of adults in its care to another town or a group of municipalities by contract from 1 July 2027. Its impact assessment counts 15,527 people in a town's care, 330 mayors doing the work themselves in 2020, and 430M CZK a year paid to towns for it."
  url: https://odok.gov.cz/portal/services/download/attachment/ALBSDXHBQ872/
  note: 'reg-verejne-opatrovnictvi-prenos-2027: RIA to the civil-code amendment on public
    guardianship (VeKLEP KORNDTFC490H), downloaded 2026-09-18 with a browser user agent (the
    odok firewall blocks plain curl) and read in full. Verbatim: "V České republice je 15 527
    fyzických osob, jejichž opatrovníkem je obec; veřejným opatrovníkem je 1 466 obcí (z
    celkového počtu 6 254)"; "(75 % obcí vykonávajících agendu veřejného opatrovnictví)" are
    type-I; "V roce 2022 vykázalo 1282 obcí z celkových 1406 péči o 1–3 opatrovance"; MV 2020
    data: "1429 zaměstnanců úřadů (81 %) a 330 starostů (19 %)"; "na malých obcích není žádný
    zaměstnanec, který by se mohl agendě plně věnovat (výkon veřejného opatrovnictví realizuje pak
    sám starosta)"; "Formou výkonové platby pro obce je rozdělováno 430 mil. Kč a dalších 21 mil.
    Kč pro kraje"; for 2027 "Výše paušální částky na jednoho opatrovance je uvažována ve výši 30
    500 Kč"; the ministry costing: one guardian costs "913 267 Kč" a year and can properly look
    after "16,05 osob", so 877 guardians and "800 935 159 Kč" in total; 2016 survey: "50 %
    oslovených obcí by možnost uzavřít veřejnoprávní smlouvu ... přivítalo"; společenství obcí
    under Act 418/2023, effective 1 January 2024, can use a shared official. Effective date
    proposed 1 July 2027. Rescore 2026-09-19: the 430M CZK is a lump-sum payment to towns with no
    eligible-spend list on file, so it is public money nearby and backs no money point, and dims
    no longer carries money; the bill only permits a hand-over and sets what the state pays, so
    on the Why now ladder it is no deadline (rung 0).'
  date: '2027-07-01'
  signal: reg-verejne-opatrovnictvi-prenos-2027
  dims: [urgency]
- type: regulation
  name: "Chamber of Deputies — bill No. 294 (civil code amendment)"
  gist: "the bill before parliament"
  why: "The government sent the bill to the Chamber of Deputies on 3 September 2026, and it can be debated from 14 September 2026."
  url: https://www.psp.cz/sqw/historie.sqw?o=10&t=294
  note: 'psp.cz history of sněmovní tisk 294, read 2026-09-18: "Vláda předložila sněmovně návrh
    zákona 3. 9. 2026"; organising committee recommended it on 9 September 2026 with the
    constitutional-legal committee as guarantor; further proceedings possible from 14 September
    2026. The previous term''s version (tisk 755, 2024) lapsed with that term (research pass,
    not re-read). Status receipt for the bill; not passed.'
  date: '2026-09-03'
  signal: veklep-KORNDTFC490H
- type: news
  name: "Česká justice — ten years of promises to villages"
  gist: "villages caring for dozens"
  why: "The chair of the association of local governments says some small villages that host institutions for disabled people must care for dozens of people, as the government takes up the bill again."
  url: https://www.ceska-justice.cz/2026/08/vlada-znovu-zmena-pravidla-verejne-opatrovnictvi/
  note: 'Česká justice (ČTK), 15 August 2026, read 2026-09-18: "Některé malé obce, v nichž sídlí
    ústavy pro handicapované, se musejí starat o desítky chovanců" (Eliška Olšáková, Sdružení
    místních samospráv); proposed effect "od 1. července 2027". The article also cites a Svaz měst
    a obcí estimate that towns look after "téměř pětinu všech opatrovaných osob" — not used here,
    because the RIA''s own count (15,527) is the receipt this problem relies on.'
  date: '2026-08-15'
  dims: [demand]
- type: regulation
  name: "Civil Code § 485 — inventory and yearly accounts"
  gist: "the yearly court accounts"
  why: "Whoever manages the person's property for them sends the court an inventory within two months of appointment and yearly accounts by 30 June."
  url: https://www.zakonyprolidi.cz/cs/2012-89
  note: 'Zákon 89/2012 Sb., § 485, read 2026-09-18: "(1) Opatrovník, který spravuje jmění
    opatrovance, vyhotoví do dvou měsíců od svého jmenování soupis spravovaného jmění a doručí jej
    soudu ... (2) Za trvání opatrovnictví vyhotoví opatrovník vyúčtování správy jmění každoročně
    vždy do 30. června". § 471(3) sets who may be a public guardian. Context for the process
    figure; backs no score.'
  date: '2026-09-18'
  dims: []
- type: regulation
  name: "Společenství obcí — the state's page on this work"
  gist: "the shared-official option"
  why: "Since 2024 a formal association of municipalities can share a trained official for this work; the state pays 30,500 CZK a year per person looked after, and 1,465 municipalities did this work in 2024."
  url: https://www.spolecenstviobci.gov.cz/verejne-opatrovnictvi
  note: 'spolecenstviobci.gov.cz, read 2026-09-18: "Od roku 2024 je možné v rámci
    profesionalizace výkonu veřejného opatrovnictví využívat funkci sdíleného úředníka"; "Pro rok
    2025 činí tento příspěvek 30 500 Kč na jednoho opatrovance"; "V roce 2024 vykonávalo tuto
    agendu 1465 obcí". Context; backs no score.'
  date: '2026-09-18'
  dims: []
- type: contract
  name: "Registr smluv — Slavkov u Brna takes misdemeanours from seven villages"
  gist: "the misdemeanour handover"
  why: "In June 2024 seven villages handed all their misdemeanour cases to the town of Slavkov u Brna by public-law contract — the model the bill copies."
  url: https://smlouvy.gov.cz/smlouva/29165876
  note: 'Hlídač státu contract search predmet:"projednávání přestupků", 2026-09-18 (120 hits):
    "Veřejnoprávní smlouva o výkonu veškeré příslušnosti k projednávání přestupků" between Město
    Slavkov u Brna and Křenovice, Bošovice, Nížkovice, Hostěrádky-Rešov, Holubice, Hrušky and
    Zbýšov, 8–15 June 2024 (registr smluv 29165876, 29165788, 29165740, 29165616, 29165488,
    29165380, 29164252). The research pass read per-case prices in similar contracts between 1,500
    and 4,500 CZK per misdemeanour (e.g. Terezín to Hodonín, 4,000 CZK per case from March 2025).
    Evidence that the handover model already works for the other agenda; dims empty, backs no
    score.'
  date: '2024-06-15'
  dims: []
- type: arbitrage
  name: "Provisum — case system for Swedish supervising offices"
  gist: "the Swedish municipal system"
  why: "Swedish towns' offices that oversee this work can use a shared case system developed with Stockholm and Västerås, offered to every office through a municipal cooperative with no licence fee."
  url: https://provisum.se/
  note: 'provisum.se, read 2026-09-18: "Verksamhetssystemet som kvalitetssäkrar och
    effektiviserar överförmyndarförvaltningen"; "utvecklat i samverkan med Stockholms och Västerås
    stad"; through agreements between Sambruk and Resursen Sverige AB "utgår ingen licensavgift
    för systemet", the yearly cost depending on the number of inhabitants. Supplier Resursen
    Sverige AB, org. nr 556933-8899, registered 2013-06-06 (allabolag.se). No customer count is
    published, so the established test is not met on file: proof stays at rung 1. Note what an
    överförmyndare is: the municipal office that supervises guardians and checks their yearly
    accounts, the closest municipal analogue found. German, UK and US guardianship software could
    not be verified in this pass (web search budget exhausted; btplus.de, butler21.de and owi21.de
    did not resolve; PROSOZ sells no guardianship product; OnView, Netherlands, publishes no year
    or customer count).'
  date: '2026-09-18'
- type: gap-check
  name: "Czech software for this work — two established suppliers already sell it"
  gist: "the taken Czech field"
  why: "Two suppliers of town-hall software sell towns a module for this work and have named buyers for it, so the product already exists here; a third seller offers an online register for it with no named buyer."
  url: https://smlouvy.gov.cz/smlouva/17954927
  note: 'Czech sweep 2026-09-18. POSITIVES, THE CONTRACT REGISTER (Hlídač státu API): predmet:
    opatrovnictví (79 hits) returned "Rozšíření informačního systému PROXIO o PROXIO - SA (Modul
    opatrovnictví fyzické osoby)", Statutární město Hradec Králové to MARBES CONSULTING s.r.o. (IČO
    25212079), 199,000 CZK excl. VAT, 18 July 2018 (registr smluv 17954927), and "Rozvoj modulu
    opatrovnictví" — "evidence peněžních prostředků na více účtech zároveň" — Město Chrudim to
    Marbes s.r.o. (IČO 29108373, Plzeň), 57,000 CZK excl. VAT, April 2022 (registr smluv
    19332327). A research-pass query "veřejného opatrovnictví" AND software returned Město Rožnov
    pod Radhoštěm to VERA, spol. s r.o. (IČO 62587978), "Software pro sociální odbor", 16 November
    2022 (registr smluv 22384845), whose specification includes "Agenda veřejného opatrovnictví:
    veřejný opatrovník peněžní deník" — attachment text re-read 2026-09-18. VERA Radnice''s own
    page (via the Seznam snippet; vera.cz did not respond) lists "Veřejný opatrovník – nabízí
    komplexní evidenci údajů o opatrovanci, plánování i přehled o činnostech a úkonech
    opatrovníka". Aptien Labs s.r.o. (IČO 26397668, since 2005) sells "Evidence opatrovnictví" from
    1,470 CZK a month (aptien.com); 31 register contracts, none a municipality buying it for
    guardianship. ICZ a.s. sells traffic-offence handling to Most (1,626,000 CZK, 2023, registr
    smluv 27318959) and Chomutov (registr smluv 25986367) — adjacent. Marbes: two named public
    buyers since 2018 and eight years selling, so DIRECT + ESTABLISHED — gap 0, status watching.
    VERA: one named buyer since 2022 — recorded established on the named-customer limb; the gap
    rests on Marbes either way. The cz-contract-parties lookup holds none of these IČOs except ICZ
    (1 buyer) and GORDIC (3). NOT LEDGERED: GORDIC''s misdemeanour module (reported by the research
    pass, not confirmed on gordic.cz); law firms paid for guardianship legal work (a service to the
    buyer, recorded as a price receipt instead); training providers. MISDEMEANOURS: 82% of small
    municipalities already hand them to a bigger town (S1, S7), so the software question there is
    the bigger towns'' problem. METHOD AND CONTROLS: the session''s web-search budget ran out
    part-way, so queries 1–7 ran through the web-search tool and the rest through the contract
    register and Seznam. Standing controls on Seznam MISSED: the Wultra query shapes returned
    Monet+ and others but not wultra.cz, and the water-metering shapes returned Softbit, Eurosat
    and ČEVAK but not Softlink. A contract-register control ("dálkový odečet" vodoměrů) also
    missed Softlink on page 1. IN-MARKET CONTROL PASSED: the Seznam descriptive query "program pro
    veřejného opatrovníka evidence opatrovanců peněžní deník obec" surfaced VERA''s guardian
    module, a vendor already known from the contract register. The score rests on what was found,
    not on an absence.'
  date: '2026-09-18'
  queries:
    - "software pro veřejné opatrovníky obce evidence opatrovanců vyúčtování soudu"
    - "software pro veřejné opatrovníky evidence opatrovanců obec"
    - "aplikace veřejné opatrovnictví vyúčtování soudu hospodaření opatrovance program"
    - 'opatrovnický software OR "program pro opatrovníky" OR "evidence opatrovanců" firma'
    - "přestupková agenda software obce evidence přestupků program modul"
    - 'VERA Radnice přestupky modul OR ALIS "přestupky" program pro obce OR Triáda "přestupky" obecní úřad'
    - "outsourcing přestupkové agendy pro obce právní kancelář předseda přestupkové komise externí služba obcím"
    - "registr smluv: predmet:opatrovnictví"
    - 'registr smluv: predmet:"projednávání přestupků"'
    - 'registr smluv: "veřejného opatrovnictví" AND software'
    - 'registr smluv: "evidence opatrovanců"'
    - "registr smluv: Aptien"
    - "registr smluv: ico:25145444 AND přestupků"
    - "program pro veřejného opatrovníka evidence opatrovanců peněžní deník obec"
    - "české řešení pro zabezpečení mobilního bankovnictví silná autentizace podpisy v mobilu dodavatel"
    - "dálkové odečty vodoměrů software pro vodárny česká firma"
  checked: [google-cz, cz-contract-parties, ares]
  expires: '2026-12-17'
- type: price
  url: https://smlouvy.gov.cz/smlouva/31722884
  name: "Břeclav — a law firm for this work"
  gist: "120,000 CZK a year"
  why: "The town of Břeclav pays a law firm 120,000 CZK including VAT for legal help with this work in 2025, and has placed a similar order most years since 2020."
  note: 'Registr smluv 31722884, order DO/9630/2025/OKT dated 8 January 2025, "Právní služby
    (výkon opatrovnictví)", 99,173.55 CZK excl. VAT, 120,000 CZK incl. VAT, performance by 31
    December 2025, supplier MELKUS KEJLA & PARTNERS advokátní kancelář s.r.o. (IČO 04504330);
    earlier orders of the same subject 2020 (100,000), 2021, 2023, 2024 (registr smluv 11417716,
    15485255, 23388301, 27913415). The supplier is a law firm serving the buyer, so it is a price
    for the manual equivalent, not a competitor in locals[]. dims omitted: backs no score.'
  date: '2025-01-08'
  payer: 'Město Břeclav, a town doing this work'
  amount_czk: 120000
  unit: per-year
  basis: signed-contract
- type: price
  url: https://odok.gov.cz/portal/services/download/attachment/ALBSDXHBQ872/
  name: "The ministry's costing — one full-time official"
  gist: "913,267 CZK an official-year"
  why: "By the state's own costing method, one full-time official doing this work costs a town 913,267 CZK a year and can properly look after about 16 people."
  note: 'RIA, the same document as S2, citing the government''s 2020 costing method (usnesení
    vlády č. 731/2020): "Celkové roční náklady ... spojené s výkonem činnosti jednoho opatrovníka
    činí 913 267 Kč" and 16.05 people per guardian. The cost of doing the job by hand, so
    manual-equivalent. dims omitted: backs no score.'
  date: '2026-09-01'
  payer: 'A Czech town employing one full-time official for this work'
  amount_czk: 913267
  unit: per-year
  basis: manual-equivalent
- type: price
  url: https://aptien.com/cs/evidence-verejne-opatrovnictvi
  name: "Aptien — the online register"
  gist: "from 1,470 CZK a month"
  why: "A Czech online register for the officials who do this work is listed from 1,470 CZK a month."
  note: 'aptien.com/cs/evidence-verejne-opatrovnictvi, read 2026-09-18: "od 1 470 Kč,-
    měsíčně"; the higher tiers are priced by number of users. The seat here is the subscribing
    office. Tagged dims: [money] on 2026-09-19 (rescore): a published price for this product,
    an asking receipt.'
  date: '2026-09-18'
  payer: 'A Czech town office using an online register for this work'
  amount_czk: 1470
  unit: per-seat-month
  basis: list-price
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/17954927
  name: "Hradec Králové — an add-on for this work"
  gist: "199,000 CZK, 2018"
  why: "What one Czech city paid in 2018 to add a module for this work to its town-hall software."
  note: 'Restated from the gap check (S9) on 2026-09-19, the rescore tagging pass. Registr smluv
    17954927, "Smlouva o dílo - Rozšíření informačního systému PROXIO o PROXIO - SA (Modul
    opatrovnictví fyzické osoby)", contract 2018/1352, signed 18 Jul 2018 (register record read
    2026-09-19); payer Statutární město Hradec Králové (IČO 00268810), supplier MARBES CONSULTING
    s.r.o. (IČO 25212079); 199,000 CZK excl. VAT, 240,790 CZK incl. VAT. Yearly support orders for
    the module are attached to the same record, the latest dated 6 Oct 2021. A signed contract for
    this job older than 24 months: an asking receipt.'
  date: '2018-07-18'
  payer: 'Statutární město Hradec Králové, a regional city'
  amount_czk: 199000
  unit: one-off
  basis: signed-contract
  dims: [money]
- type: price
  url: https://smlouvy.gov.cz/smlouva/19332327
  name: "Chrudim — more work on its add-on"
  gist: "57,000 CZK, 2022"
  why: "What one Czech town paid in 2022 to extend its add-on for this work, so it tracks a person's money on several accounts at once."
  note: 'Restated from the gap check (S9) on 2026-09-19, the rescore tagging pass. Registr smluv
    19332327, "Rozvoj modulu opatrovnictví", contract CR 010481/2022, signed 14 Jan 2022 and
    published 9 Feb 2022 (register record read 2026-09-19; S9 says April 2022, which the record
    does not support); payer Město Chrudim (IČO 00270211), supplier Marbes s.r.o. (IČO 29108373);
    57,000 CZK excl. VAT, 68,970 CZK incl. VAT. Scope per S9: "evidence peněžních prostředků na
    více účtech zároveň". Older than 24 months: an asking receipt.'
  date: '2022-01-14'
  payer: 'Město Chrudim, a town doing this work'
  amount_czk: 57000
  unit: per-project
  basis: signed-contract
  dims: [money]
created: '2026-09-18'
updated: '2026-09-19'
---

Small Czech villages must look after the affairs of adults a court says can't manage alone, and in many the mayor does it personally [S1,S2].

- 15,527 adults rely on a town or village to run their affairs [S2].
- In 2020, 330 mayors did this work themselves [S2].
- 61% of small municipalities doing it call it a burden [S1].

The law calls this public guardianship: when no relative or other person can look after an adult's affairs, a court hands them to a town or village [S2,S5]. The town then manages the person's money and property, and sends the court yearly accounts [S5].

- 1,466 of the country's 6,254 municipalities do this work, and 75% of them are small villages [S2].
- In 2022, 1,282 of the 1,406 municipalities doing it looked after only one to three people [S2].
- Where there is no employee for it, the mayor does the work [S2].
- Mayors describe court hearings, weekend requests to consent to a medical procedure, and losing track of each person [S1].

The ombudsman, the public defender of rights, surveyed 2,191 small villages and 140 larger towns in April and May 2025 [S1]:

- 46% do this work, and 18% still handle minor-offence cases themselves [S1].
- Of those that handle minor offences, 69% call them a burden [S1].
- About two in five see this work and minor-offence cases as of little benefit to their residents [S1].
- The lawyers and commission members that minor-offence cases require cost more than the fines bring in [S1].
- Municipalities asked for the right to hand this work to another town by contract [S1]. In 2016, half of the municipalities asked said they would welcome it [S2].

Existing non-solutions: Two established Czech suppliers of town-hall software already sell towns an add-on for this work [S9].

A third Czech seller offers an online register for the officials who do it, with no named town buying it; see [Market gap](#competition) [S9]. Towns also pay lawyers for help with the work; see [Willing to pay](#willing-to-pay).

- Minor-offence cases already have a way out: a village pays a bigger town to handle them under a contract between the two municipalities [S7]. Seven villages handed all their cases to one town this way in June 2024 [S7].
- Since 2024 a formal association of municipalities in one district can share one trained official for this work [S2,S6].
- Today it is unclear whether a village may hand this work to another town by contract, which the bill would settle [S2].

Why now: Mayors lose days to court hearings and hospital calls, and a bill would only let villages hand this on, not require it [S1,S2].

- A mayor takes other town-hall work home after court hearings [S1].
- Villages with a care institution can look after dozens of people [S4].
- State money covers about half the cost its own costing finds [S2].

The dates behind this:

- On 1 January 2024 the association of municipalities with a shared official became possible [S2,S6].
- On 3 September 2026 the government sent the bill to parliament [S3].
- From 1 July 2027 the bill would let a village hand this work to another town, or to an association of municipalities, by contract [S2].
- Every year by 30 June the town sends the court the accounts of each person's money it manages [S5].

Who pays: Towns pay, and the state gives them 430M CZK a year for this work, less than its own costing says it needs [S2].

- The state pays a town about 30,500 CZK a year for each person [S6].
- Towns bought add-ons for this work in 2018 and 2022 [S9].
- Towns hire lawyers to help; see [Willing to pay](#willing-to-pay).

Regions get another 21M CZK a year on top of the 430M CZK for towns [S2]. The ministry's own costing needs 877 full-time officials at about 801M CZK a year to look after everyone properly [S2]. The bill does not change the money: its impact assessment calls it budget-neutral [S2].

Solved elsewhere: Swedish towns' offices that oversee this work can use a shared case system, offered to every office through a municipal cooperative [S8].

It was developed with the cities of Stockholm and Västerås, carries no licence fee, and costs each town a yearly sum set by its population [S8]. The Swedish office supervises the people who run adults' affairs and checks their yearly accounts, the closest match to a Czech town office doing the same work [S8]. The Czech bill's impact assessment also points to Sweden's volunteers who take on this role and to trust companies that manage property in England [S2].

## First moves

1. Build a register for a town office that looks after people from several villages: each person's file, money, deadlines and yearly court accounts. It should keep money on several accounts per person. The bill under [Why now](#why-now) would let villages hand this work to a bigger town, so the offices that take it on will look after people from many villages at once. The modules sold today serve one town's own caseload; see [Market gap](#competition). Keep the money ledger and the yearly accounts in the same file, because the court asks for both.
2. Call the social departments of towns that already handle minor-offence cases for nearby villages, and ask whether they plan to take on this work too. They already run this kind of arrangement, as [Market gap](#competition) shows, and the villages around them are the ones asking for it; see [The opportunity](#opportunity). Ask how they track each person's money and deadlines today, and what the court asks them for.
3. Offer the register to associations of municipalities that already share one trained official, since they already pool this work. The state money follows each person looked after, as [Willing to pay](#willing-to-pay) shows, so price the register the same way, per person.

## Revisions

2026-09-18 · record created — Minted from the ombudsman's small-municipality survey [S1] and the guardianship bill's impact assessment [S2]. Demand 2 on the survey of 2,331 municipalities, its mayors' own accounts and the association chair's statement [S1,S4]. Money 2 on the 430M CZK paid to towns every year for this exact work [S2]. Urgency 2: the bill's 1 July 2027 date is under 18 months away but it is still a bill, so the deadline scores 1, plus sources fresher than 90 days [S2,S3]. Proof 1: the one foreign comparable found, a Swedish case system, publishes no customer count, so it does not pass the established test on file; that is a missing receipt, not a finding that it is early [S8]. Gap 0 and status watching: Marbes has sold a guardianship module to named towns since 2018, and VERA sells one too [S9]. Corrections to the signals: the ombudsman's 69% and 61% are shares of the municipalities that do each task, not of all respondents; and 82% of small municipalities no longer handle misdemeanours themselves, so this problem is written about guardianship, with misdemeanours as context [S1]. Flagged as inference: "covers roughly half" compares the 430M CZK paid with the ministry's own 801M CZK costing, both from the impact assessment [S2]. No draft-law badge: mayors carry this work today whatever happens to the bill. The web search budget ran out during this pass, so the standing positive controls were run on Seznam and missed; an in-market control passed [S9].

2026-09-19 · plain language (owner-approved) — Owner: "I would appreciate not using or explaining of legal guardian (idk what it means)". The title, brief, solution, body and every rendered line now say what actually happens, and the word appears once, explained in the same sentence: "The law calls this public guardianship: when no relative or other person can look after an adult's affairs, a court hands them to a town or village [S2,S5]." Title before, verbatim: "Czech village mayors act as legal guardians for vulnerable adults, with no staff to help. A bill would let them hand it on from July 2027." After: "Czech village mayors must handle the money and hospital consents of adults who can't manage alone. A bill would let them hand this on from July 2027." Brief before: "Village mayors run the money, court hearings and hospital consents of adults a court placed in their care, often without any training for it [S1,S2]. A bill would let them pass this to a bigger town from July 2027 [S2]." After: "When a court decides an adult can't manage alone and nobody else can help, their town or village is made responsible [S2,S5]. In a village with no staff, the mayor does it, which can mean signing hospital consents at weekends [S1,S2]." Solution: "the town offices that act as guardian" became "the town offices that take on this work". Checked against the sources: the money and yearly accounts [S5], court hearings and a weekend request for consent to a medical procedure in the mayors' own words [S1], and the mayor doing the work where a village has no employee for it [S2]; "can mean" because the weekend consent is one mayor's account. "Often without any training" left the brief: it rests on the process summary, and no note on file counts training. "With no staff to help" left the title for length, and the brief carries it; the court hearings are in the body [S1]. The bill moved from the brief to the title only. Body: every "guardian", "guardianship" and "ward" became what the work is ("look after the affairs of adults a court says can't manage alone", "this work", "the officials who do it"), and "misdemeanour" became "minor offence"; the facts, figures and markers are unchanged. Two small corrections: "One mayor describes court hearings, weekend requests … and losing track" became "Mayors describe", since [S1]'s note gives these as several quotes from chapter 9 and its public line says "mayors"; and "A mayor takes her other town-hall work home" lost "her", since the quoted Czech does not show the speaker's sex [S1]. The same wording changed in the rendered lines: `entry.why`, the process summary and steps (the step actor "The guardian" became "The mayor or official"), the Provisum row, the Marbes, VERA, Aptien and ICZ evidence lines, two ledger names ("Marbes (PROXIO guardianship module)" became "Marbes (PROXIO)", "Aptien (guardianship register)" became "Aptien"), three price payers, and the public `name`, `gist` or `why` of [S1], [S2], [S3], [S4], [S5], [S6], [S7], [S8], [S9], [S10], [S11] and [S12]. No `note:` was touched; the notes keep the legal terms for anyone checking them. No fact was removed. No score, status, source order, note, marker, good_for or `entry` gate value changed.

2026-09-19 · rescored to the 2026-09-19 ladders — Why now 2 → 0 and Willing to pay 2 → 1, so the total goes 7 → 4 and the band falls from FAIR to FAINT. This departs from the rescore worksheet, which gave Why now 1 and a total of 5. Why now: the old 2 was deadline 1 for the bill plus the freshness point, which is retired. The bill [S2,S3] only lets a village hand this work to another town by contract, and sets what the state pays per person. The ladder scores 0 for a rule that only permits something or changes what the state pays, and the bill is not yet law either. The yearly accounts to the court [S5] have been due for years, so they are the status quo, not a trigger. No dated duty falls on the towns. Willing to pay: the old 2 rested on the 430M CZK the state pays towns each year [S2]. That is public money nearby, and with no eligible-spend list on file it cannot lift a price, so S2's dims are now [urgency]. Tagging pass, every payment on file: the Aptien list price, 1,470 CZK a seat-month [S12], is a published price for this product and is now tagged money. Two signed contracts for this job, found by the gap check [S9], are restated as receipts. The first is Hradec Králové's module, 199,000 CZK excl. VAT, signed 18 July 2018 [S13]; its yearly support orders on the same register record end in October 2021. The second is Chrudim's extension of its module, 57,000 CZK excl. VAT, signed 14 January 2022 [S14]; the gap check's "April 2022" is not what the register record says. Both are older than 24 months, so they are asking receipts. Not restated: Břeclav's law firm [S10] is paid for legal help with this work, not for the files, money and yearly accounts the product keeps, so it does not buy this job and stays untagged. Flagged as inference: the order's subject reads "Právní služby (výkon opatrovnictví)" on the register record (read 2026-09-19), its scope was not read, and legal services are taken to mean the legal acts and hearings the process keeps with a person. The ministry's costing of a full-time official [S11] prices the whole job done by a person, most of which the software does not replace, and stays untagged. Rožnov pod Radhoštěm's 465,850 CZK incl. VAT (16 November 2022, registr smluv 22384845) buys a whole social-department system with this work as one part, so that amount does not price this job. Three asking receipts and no paid one within 24 months give 1. Body: the 3 `[Competition](#competition)` links now read `[Market gap](#competition)`. Why now's opening sentence now says the bill would only let villages hand the work on, not require it; it no longer gives the July 2027 date, which stays in the dates below. Willing to pay's second item dates the software purchases on file (2018 and 2022) instead of saying towns buy; its opening sentence is unchanged. S2's note no longer claims money 2 or the deadline point, and S12's note records its tag. No other score, status, marker or `entry` gate changed.
