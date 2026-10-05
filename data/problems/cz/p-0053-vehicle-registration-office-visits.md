---
id: p-0053
region: cz
title: 'Czech car buyers stood in office queues over 1.2M times last year just to change a car''s owner'
brief: 'Even when the paperwork starts online, the buyer must still go to one of 206 registration offices to finish it [S1,S4]. The state expects to save about 2.4bn CZK a year by ending most of these visits [S1].'
solution: 'Build a registration service for car dealers, leasing firms and fleets that takes their papers under a power of attorney, files each change in bulk and returns plates and papers, as 3 companies already do in 2 other countries.'
good_for: 'Someone who knows car dealers or leasing firms and can run a reliable back office.'
category: mobility
geo: CZ-national
score: 6
scores:
  proof: 3
  money: 1
  urgency: 0
  demand: 2
  gap: 0
status: watching
entry:
  level: moderate
  buyer: small-firms
  permission: none
  integration: national-system
  incumbents: direct
  money: bootstrap
  why: 'Easier: dealers, leasing firms and owners already pay to have registrations done for them; a power of attorney is all the permission needed; and one trip to the office can carry many cars. Harder: every change runs through the state vehicle register and its offices; and established Czech firms already sell the service.'
comps:
- name: Kroschke
  url: https://www.kroschke.de/unternehmen/zahlen-fakten
  geo: DE
  since: 1957
  traction: 'German registration services group: about 1 million vehicle registrations a year,
    about 60 registration-service locations and over 13,000 dealer customers, with about 1,800
    staff and about 130M EUR revenue (own figures, 2024).'
- name: Computerized Vehicle Registration (CVR)
  url: https://www.cdkglobal.com/media-center/cdk-global-acquires-full-ownership-computerized-vehicle-registration-cvr
  geo: US
  since: 1992
  traction: 'Electronic vehicle registration for car dealers: nearly 15 million vehicle
    transactions and over 4 million state-registry inquiries a year in 17 states, backed by 15
    dealer associations; CDK Global took full ownership on 30 June 2023 (CDK, 2023).'
- name: Vitu
  url: https://vitu.com/company/timeline.html
  geo: US
  since: 2005
  traction: 'Digital vehicle registration and titling for dealers, lenders and state
    agencies; bought the registration and titling business of Cox Automotive''s Dealertrack in
    2025, and its title exchange passed 1 million electronic title transactions (own timeline,
    2025).'
locals:
- name: SPZ Servis
  url: https://www.spzservis.cz/
  ico: '26704340'
  since: 2002
  competes: direct
  maturity: established
  evidence: 'Registers vehicles for owners under a power of attorney, with separate offers for
    leasing firms, dealers, importers and company fleets, including bulk work. Established:
    registered 2002 (ARES) and "od roku 2002" on its site, with a public customer count of
    50,000+ clients.'
- name: SPZ služby
  url: https://spzsluzby.cz/prepis-vozidla/online/
  ico: '61019127'
  since: 2012
  competes: direct
  maturity: established
  evidence: 'Takes the owner''s power of attorney online and handles the change of owner at the
    office in Prague, for private owners, dealers, fleets and leasing firms. Established: selling
    since 2012 by its own account, with a public customer count of more than 5,000 completed
    requests in Prague and around.'
- name: D-FENS CZ (registrace-vozidel.cz)
  url: http://www.registrace-vozidel.cz/
  ico: '03975894'
  since: 2015
  competes: direct
  maturity: early
  evidence: 'Registers vehicles in Brno under a power of attorney and offers bulk transfers of 10
    or more vehicles. Registered 2015 (ARES); no customers or counts were found, so the test is
    not passed.'
- name: CENTRUM SPZ
  url: https://www.centrumspz.cz/
  ico: '03791246'
  since: 2015
  competes: direct
  maturity: early
  evidence: 'Sells registration for company fleets and long-term work for dealers and leasing
    firms, alongside insurance. Registered 2015 (ARES); no customers or counts were found.'
- name: PřepiServis (registr-vozidel.cz)
  url: https://www.registr-vozidel.cz/cenik
  competes: direct
  maturity: early
  evidence: 'Sells changes of owner, new registrations and deregistrations in Prague at a
    published price per job. No company number or customer count could be found on its site or
    in ARES.'
- name: Vít Hovorka (registracevozidel.cz)
  url: https://www.registracevozidel.cz/
  ico: '61497452'
  competes: direct
  maturity: early
  evidence: 'A Prague sole trader who registers vehicles for firms and private owners. No
    selling-since year for this service and no customers were found.'
- name: Renata Hrabýová
  url: https://www.hrabyova.cz/
  ico: '49199528'
  competes: direct
  maturity: early
  evidence: 'A Plzeň sole trader who represents car dealers and hauliers at the registration
    office, alongside insurance broking. No customers or counts were found.'
- name: SPZone
  url: https://www.spzone.cz/
  ico: '28147421'
  since: 2012
  competes: adjacent
  maturity: early
  evidence: 'Sells the technical and emissions checks an imported car needs, with registration
    added on. It sells the checks, not a registration service for dealers or fleets. Registered
    2012 (ARES); no customers or counts were found.'
- name: Ministerstvo dopravy
  url: https://ares.gov.cz/ekonomicke-subjekty?ico=66003008
  ico: '66003008'
  competes: non-seller
  evidence: 'The transport ministry runs the state vehicle register and the online transport
    portal, and its bill would let owners finish most of these changes online. It sells nothing,
    and its portal is what any service has to work through.'
process:
  summary:
    today: 'The seller can start a change of owner online, but the buyer, or someone with a power of attorney, still goes to a registration office to finish it, pay and collect the papers [S1,S4].'
  steps:
  - who: The seller
    today: 'Starts the change online or at the office'
    known: documented
    cites: [4]
    change: stays
    after: 'Starts the change as before'
  - who: The buyer
    today: 'Goes to the office with the papers'
    known: documented
    cites: [1, 4]
    change: changes
    after: 'Hands the papers to the service once'
  - who: A paid agent
    today: 'Queues at the office for the owner'
    known: documented
    cites: [1]
    change: changes
    after: 'Files many cars together, by power of attorney'
  - who: The buyer or agent
    today: 'Pays the fee and collects plates and papers'
    known: documented
    cites: [1]
    change: changes
    after: 'Plates and papers come back by courier'
sources:
- type: regulation
  name: 'Transport ministry — vehicle registration bill, impact assessment'
  gist: 'the state''s own visit count'
  why: 'The impact assessment of the government''s bill to move vehicle registration online: how many changes still need a visit to an office, what they cost, and who does them for pay.'
  url: https://www.odok.cz/portal/services/download/attachment/KORNDXBHK7HB/
  note: 'reg-registrace-vozidel-online-2027 (ria_KORNDX9FJCDB.docx, VeKLEP KORNDQLEC77O), re-read
    2026-10-05 from ODok. Visits table "počty úkonů, které jsou v současnosti spojeny s osobní
    návštěvou úřadu" 2023/2024/2025: změna vlastníka / provozovatele 1 083 198 / 1 181 579 / 1 223 130;
    první registrace 519 254 / 514 917 / 540 827; vydání ORV 1 939 151 / 2 163 009 / 2 208 646;
    vyřazení z provozu 133 364 / 135 430 / 154 668; zánik 160 149 / 184 767 / 197 689. "I v případě
    udělení plné moci jiné osobě je osobní účast k dokončení úkonu, k úhradě správních poplatků a
    převzetí nových dokladů ... na registračním úřadu nezbytná." "Žádosti nebo oznámení podávané
    elektronicky jsou v současné době možné, ale jejich dokončení je vázáno na osobní účast
    žadatele". "uspoří kapacita na 206 registračních úřadech a bude celková úspora cca 2,4 miliardy
    Kč (1,81 mld. Kč ... a 0,64 mld. Kč ...)" — the bill''s expected yearly saving, mid scenario.
    "Na trhu působí také subjekty, které za úplatu zprostředkovávají vyřízení úkonů v agendě
    registrace vozidel (zejména autobazary, dovozci ojetých vozidel a leasingové společnosti) ...
    jejich počet proto nelze z dat registru samostatně vyčíslit. Navrhovaná úprava ... snižuje
    potřebu placeného zprostředkování ...; zprostředkovatelé se přitom mohou na nový model napojit
    prostřednictvím Portálu dopravy." "významná část úkonů v agendě vozidel je vedena leasingovými
    společnostmi a autobazary". STATUS: government approved 2026-07-27; sněmovní tisk 293,
    submitted 31 Aug 2026, first reading not yet held (psp.cz historie t=293, read 2026-10-05 by
    the research pass); core changes proposed from 1 Jul 2027. A bill: it binds no buyer and
    carries no Why now point; cited for its figures.'
  date: '2026-08-26'
  signal: reg-registrace-vozidel-online-2027
  dims: [demand]
- type: news
  name: 'Autoživě — selling a car online, plates by post'
  gist: '1.2 million in the queue'
  why: 'A car-news report on the bill: over 1.2 million people queued at offices last year to buy or sell a car.'
  url: https://www.autozive.cz/prodej-auta-vyridite-online-znacky-vam-prijdou/
  note: 'Autoživě, Daniel Karban, 2 Oct 2026, read 2026-10-05: "Loni si na úřadech kvůli koupi či
    prodeji auta vystálo frontu přes 1,2 milionu lidí." "Ministerstvo dopravy přitom eviduje, že
    jen v roce 2025 šlo o 1 223 130 případů změny majitele." Timeline: November 2026 partial
    provisions; "1. července 2027 – jádro novely: online převody, doručování dokladů a značek"; 1
    July 2028 automation. The government frames it as a recovery-plan milestone; missing it could
    put up to 25bn CZK of EU money at risk, per the Government Office.'
  date: '2026-10-02'
  dims: [demand]
- type: news
  name: 'Chamber of Commerce seminar — digitising car sales'
  gist: 'dealers and lessors ask for it'
  why: 'A Chamber of Commerce event where the largest used-car dealer and the leasing association asked for online car transfers; the dealer registers about 60,000 used cars a year.'
  url: https://www.blesk.cz/clanek/zpravy-udalosti/776400/digitalizace-obchodovani-s-automobily-vyrazne-zvedne-komfort-pro-zakazniky-a-snizi-naklady-pro-podnikatele.html
  note: 'Blesk, 22 Jan 2024 (Hospodářská komora ČR seminar; the businessinfo.cz original returned
    403), read 2026-10-05. Karolína Topolová, AURES Holdings: "jsme patrně v tuzemsku subjektem s
    nejvyšším počtem registrací ojetých vozů, který se pohybuje kolem 60 000 ročně" and
    "Digitalizace převodů vozů by ještě více přispěla k zefektivnění obchodování na sekundárním
    automobilovém trhu". Speakers also from ČLFA (leasing association), ČAP, Cebia and the chamber.
    Industry pressure; no costs quantified.'
  date: '2024-01-22'
  dims: [demand]
- type: news
  name: 'Auto.cz — changing a car''s owner online'
  gist: 'the buyer still goes in'
  why: 'A how-to on the online change of owner: only the seller can start it, the buyer still has to go to the office, and firms cannot use it yet.'
  url: https://www.auto.cz/prepis-auta-online-postup-a-co-je-potreba-na-urad-stejne-musite-160062
  note: 'Auto.cz, Jan Faltýsek, 23 Feb 2026, read 2026-10-05: "Iniciátorem je vždy prodávající";
    the buyer must at the office "dokončit převod, předložit fyzické dokumenty a převzít nové
    doklady"; fee 800 Kč at the counter, 640 Kč online; the online service is for natural persons
    only and "by se měly rozšířit i na právnické osoby".'
  date: '2026-02-23'
  dims: [demand]
- type: price
  name: 'SPZ služby — change of owner done for you'
  gist: 'per change, list price'
  why: 'What a Prague service charges to take an owner''s power of attorney and complete one change of owner at the office.'
  url: https://spzsluzby.cz/prepis-vozidla/online/
  note: 'Read 2026-10-05: "Cena služby 1 000 Kč (+ správní poplatek)"; "Vy udělíte plnou moc
    online, my fyzicky zajistíme registraci"; "Již více než 5 000+ vyřízených žádostí v Praze a
    okolí"; power of attorney to Jindřich Pipota, IČ 61019127. Price list (spzsluzby.cz/cenik-sluzeb)
    900–1,500 Kč per job, volume discounts by agreement (research pass, not re-read). Asking price.'
  date: '2026-10-05'
  payer: 'Czech car owners and dealers in Prague'
  amount_czk: 1000
  unit: per-case
  basis: list-price
  dims: [money]
- type: price
  name: 'SPZ Servis — registration job for firms'
  gist: 'per job, list price'
  why: 'What a national registration service charges per job in Prague, for private owners, dealers, leasing firms and fleets.'
  url: https://www.spzservis.cz/
  note: 'Read 2026-10-05: Praha and surroundings 400 Kč bez DPH per úkon; other regions 600 Kč bez
    DPH; individual import 3,000 Kč bez DPH; state fees on top; "Již od roku 2002 pomáháme
    jednotlivcům i firmám"; "50.000+" spokojených klientů; segments for leasing companies, dealers,
    importers and company fleets. Amount excl. VAT. Asking price.'
  date: '2026-10-05'
  payer: 'Czech dealers, leasing firms and fleets in Prague'
  amount_czk: 400
  unit: per-case
  basis: list-price
  dims: [money]
- type: arbitrage
  name: 'Kroschke'
  gist: 'German registration services'
  why: 'A German group that registers about a million vehicles a year for over 13,000 car dealers.'
  url: https://www.kroschke.de/unternehmen/zahlen-fakten
  note: 'Zahlen & Fakten, read 2026-10-05, figures as of 2024: founded 1957 (first plate shop in
    Braunschweig); ~1,800 staff; ~130M EUR revenue; "ca. 1 Mio" Zulassungen pro Jahr; ~60
    Zulassungsdienste; "über 13.000" dealer customers. OEM page (kroschke.de/branchenloesungen/oem)
    sells registration to manufacturers, dealers and fleets. Germany opened online registration
    (i-Kfz) to firms and dealers in 2023 (search listing, not read), and the group still sells the
    service. Established, CEE-adjacent (DE).'
  date: '2026-10-05'
  dims: [proof]
- type: arbitrage
  name: 'Computerized Vehicle Registration (CVR)'
  gist: 'US dealer e-registration'
  why: 'An American company that registers vehicles electronically for car dealers in 17 states, nearly 15 million transactions a year.'
  url: https://www.cdkglobal.com/media-center/cdk-global-acquires-full-ownership-computerized-vehicle-registration-cvr
  note: 'CDK Global press release, 30 June 2023, read 2026-10-05: "CVR provides automotive dealers
    and other key members of the vehicle lifecycle with fast, secure, certified electronic vehicle
    registration"; "nearly 15 million vehicle transactions and more than 4 million DMV inquiries
    annually"; 17 states; 15 dealer associations; founded 1992. Established.'
  date: '2023-06-30'
  dims: [proof]
- type: arbitrage
  name: 'Vitu'
  gist: 'US digital registration'
  why: 'An American firm that sells digital vehicle registration and titling to dealers, lenders and states, and bought Dealertrack''s registration business in 2025.'
  url: https://vitu.com/company/timeline.html
  note: 'Company timeline, read 2026-10-05: founded 2005 by Don Armstrong and Kelly Kimball;
    electronic registration and titling for dealers, lenders and jurisdictions; 2025 acquisitions
    of Dealertrack Registration & Titling (Cox Automotive) and DDI Technology; NTX passed one
    million e-title transactions; leading EVR provider in California (2014) and Indiana (2023).
    Established.'
  date: '2025-12-31'
  dims: [proof]
- type: gap-check
  name: 'Czech check — who registers cars for others'
  gist: 'the Czech field, searched'
  why: 'Czech-language search, a business directory and the state business register: established Czech firms already register cars for owners, dealers, leasing firms and fleets.'
  url: https://www.firmy.cz/Auto-moto/Auto-moto-sluzby/Zprostredkovani-registrace-a-prevodu-automobilu
  note: 'Gap check 2026-10-05 for this problem. Surfaces: Czech web search (queries below), the
    Firmy.cz category "Zprostředkování registrace a převodů automobilů" (59 listed firms, mixed with
    car bazaars, inspection stations, scrapyards and plate makers; first page of 14 read), ARES REST
    (IČO lookups), data/lookup/cityvizor-invoices.jsonl and cz-contract-parties.jsonl (no public
    payer found for any of these IČOs). POSITIVE CONTROL: "přepis vozidla online spzsluzby"
    returned spzsluzby.cz at once, and the generic "přepis vozidla za vás" query also surfaced it
    with PřepiServis. PASSED. FOUND, DIRECT, ESTABLISHED (in locals[]): SPZ Servis, s.r.o. 26704340
    (2002-06-10; 50,000+ clients; leasing, dealers, importers, fleets, bulk work); SPZ služby
    (Jindřich Pipota, 61019127, ARES 1996-04-10, selling since 2012 by its site; 5,000+ requests).
    FOUND, DIRECT, EARLY (in locals[]): D-FENS CZ 03975894 (Brno; bulk transfers of 10+); CENTRUM SPZ
    03791246; PřepiServis (registr-vozidel.cz, price list from 1 Jan 2025, 1,000 Kč per change; no
    IČO found); Vít Hovorka 61497452; Renata Hrabýová 49199528. ADJACENT (in locals[]): SPZone
    28147421. SEEN, NOT LEDGERED: e-spz s.r.o. 02768208 (site returned an empty page); REGISTER
    SYSTEM, s.r.o. (Firmy.cz only, IČO not matched); prepisy-vozidel.cz (operator not identified).
    In-house: the largest used-car dealer registers about 60,000 cars a year itself [S3]. The RIA
    itself names paid intermediaries for dealers, importers and leasing firms [S1].'
  date: '2026-10-05'
  queries:
  - 'přepis vozidla za vás cena služba'
  - 'registrace vozidel pro autobazary služba hromadné přepisy'
  - 'hromadná registrace vozidel leasingové společnosti zajištění registrace flotily'
  - 'zajištění registrace vozidel pro firmy registrační služba Brno Ostrava'
  - 'registrační služba vozidel Praha vyřízení registrace na plnou moc firmy'
  - 'přepis vozidla online spzsluzby'
  checked: [google-cz, ares, cz-saas-directories]
  expires: '2027-01-03'
created: '2026-10-05'
updated: '2026-10-05'
---

Czech car buyers, dealers and leasing firms still have to go to a registration office to finish almost every change to a car's registration [S1].

- Over 1.2 million people queued last year to buy or sell a car [S2].
- Even with a power of attorney, someone must go in to finish [S1].
- Only the seller can start online, and only as a private person [S4].

The state counts the visits each change still needs [S1].

- 1,223,130 changes of owner went through the offices in 2025, up from 1,083,198 in 2023 [S1].
- 540,827 first registrations and 154,668 deregistrations were also done in person in 2025 [S1].
- There are 206 registration offices across the country [S1].
- Leasing firms and car dealers handle a large share of these changes, the state says [S1].
- The largest used-car dealer says it registers about 60,000 used cars a year [S3].

Existing non-solutions: Established Czech firms already register cars for owners, dealers, leasing firms and fleets, by taking their papers to the office [S10].

- Firms registered as far back as 2002 sell this to dealers and fleets [S10].
- Smaller firms do the same in single cities [S10].
- Large dealers do their own registrations in house [S3].

These services still queue at the office for the owner; they save the owner the trip, not the visit [S1]. The state says it cannot count how many changes they handle [S1]. The rows are under [Market gap](#competition).

Why now: No deadline forces anyone to act, but every sale still costs a buyer a trip, and the state's fix is still a bill [S1,S2].

- A buyer can lose an afternoon at the office for each car [S2].
- The largest used-car dealer asked for online transfers at a 2024 chamber event [S3].
- Firms cannot use the online start at all yet [S4].

The dates behind this:

- In February 2026 the online start still needed the buyer to go in person [S4].
- In August 2026 the government sent its bill to parliament, and it has not passed [S1].
- From July 2027 the bill would move changes of owner online and send plates and papers to pickup boxes [S2].
- The state expects to save about 2.4bn CZK a year if it passes [S1].

Who pays: Yes, owners, dealers and leasing firms already pay Czech firms per job to do their registrations for them [S10].

- Services publish fixed prices for each change of owner [S10].
- Firms sell bulk deals to dealers and leasing companies [S10].
- The state names these paid go-betweens in its own assessment [S1].

What a change of owner costs through such a service is under [Willing to pay](#willing-to-pay).

Solved elsewhere: In Germany and the United States, established firms register cars for dealers in bulk, by hand and electronically [S7,S8].

In Germany, a registration group handles about a million registrations a year for over 13,000 dealers [S7]. In the United States, 2 firms file registrations electronically for dealers and lenders across many states [S8,S9]. See [Validated abroad](#validated-abroad).

## First moves

1. Ask a few used-car dealers and a leasing firm how many registrations they do a month, and who takes the papers to the office today. The state says these firms handle a large share of all changes, as [The opportunity](#opportunity) shows, so their answer sizes the work.
2. Build a simple order screen where a dealer drops the papers for many cars at once and sees each one's status. Offer it on top of the courier work the firms under [Market gap](#competition) already do, or as a partner to one of them.
3. Follow the transport ministry's bill through parliament, and be ready to file through its online portal for firms the day it opens. The state says paid go-betweens can connect to the new online route, as [Why now](#why-now) shows.
4. Talk to a fleet manager about deregistering old cars in bulk, which today also needs plates handed back in person. That job stays with the owner until the bill passes.

## Revisions

2026-10-05 · record created — Created from owner decision 19 (docs/weekly/2026-09-28.md), candidate B, on the signal reg-registrace-vozidel-online-2027 [S1], whose impact assessment was re-read from ODok on this date, plus three news reports [S2,S3,S4]. Scores: proof 3 on established sellers in Germany and the United States [S7,S8,S9]; money 1 on two published per-job prices [S5,S6], with no paid receipt found; urgency 0, because the only dated change is a bill not yet passed and it would remove a duty rather than add one, flagged for the owner; demand 2 on the state's own visit count, the queue report and the largest dealer's call at a chamber event [S1,S2,S3]; gap 0 because two established Czech firms sell this to dealers, leasing firms and fleets [S10]. Status watching under the de-rank rule. No draft_law key: the queues exist today under the law in force, and the bill is the fix, not the pain. The 2.4bn CZK is the bill's expected yearly saving, mid scenario, not a measured cost [S1]. "An afternoon" for each car is the news report's phrase [S2]. The impact assessment says the bill would reduce the need for paid go-betweens, so the opportunity shrinks if it passes, and go-betweens may connect to the new online route [S1]; the German comp kept selling after Germany opened online registration to firms (search listing only, recorded in the S8 note). The solution counts all 3 comps as doing this. SPZ služby's since 2012 is its own statement; ARES dates the sole trader to 1996.
