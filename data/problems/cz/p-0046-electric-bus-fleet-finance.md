---
id: p-0046
region: cz
title: 'Czech city bus companies must now buy mostly clean buses, and one late delivery can cost them the EU grant that pays for them'
brief: 'Since January 2026 a law requires 60% of the city buses they buy to be clean, half with zero emissions [S1]. In 2023 an electric bus cost 14M CZK against 6M for diesel, and a late one can cost the grant [S2].'
solution: 'Build a company that finances electric buses and their batteries and builds and runs the depot chargers, charging city bus companies a fee per bus, as a company already does in Britain and Spain.'
good_for: 'People who can raise large sums and sell to city bus companies through tenders.'
category: mobility
geo: CZ-national
score: 10
scores:
  proof: 2
  money: 2
  urgency: 2
  demand: 2
  gap: 2
status: candidate
entry:
  level: very-hard
  buyer: public
  permission: none
  incumbents: adjacent
  integration: national-system
  money: outside-money
  why: 'Easier: the law pushes every city bus company to add clean buses now, grants do not cover every bus, and no licence is needed to rent buses out. Harder: the buyers are public companies that buy through tenders, each bus costs millions up front, and chargers must be built in the bus yards and wired to the grid.'
process:
  summary:
    today: 'A city bus company applies for an EU grant, tenders the buses and the depot chargers as separate purchases, and must repay part of the grant if the buses arrive late or run too few kilometres [S2,S3].'
  steps:
  - who: Bus company
    today: 'Applies for an EU grant for the buses'
    known: documented
    cites: [3, 4]
    change: changes
    after: 'Compares a fee per bus with the grant'
  - who: Bus company
    today: 'Tenders and buys the electric buses outright'
    known: documented
    cites: [2, 3]
    change: changes
    after: 'Rents the buses for a fee per bus'
  - who: Bus company
    today: 'Tenders the depot chargers as a separate contract'
    known: documented
    cites: [8, 13]
    change: changes
    after: 'Gets chargers built and run with the buses'
  - who: Bus company
    today: 'Runs the buses to the grant''s planned kilometres'
    known: documented
    cites: [2]
    change: changes
    after: 'Runs the buses while the provider keeps them going'
  - who: Bus company
    today: 'Repays part of the grant if targets slip'
    known: documented
    cites: [2]
    change: goes
    after: null
comps:
- name: Zenobē
  url: https://www.zenobe.com/
  geo: GB
  since: 2017
  traction: 'Finances electric buses and trucks and designs, builds, maintains and runs their depot
    charging for operators; began operations in 2017; named customers include National Express (130
    buses in Coventry), Go-Ahead (104 charge points in Oxford) and Grupo Julià (44 buses in
    Barcelona); supports over 3,400 electric fleet vehicles in 120 depots; closed a EUR 325M debt
    facility in July 2025 to expand in continental Europe (company release, 2025).'
  signal: gb-zenobe
  markets: [ES]
locals:
- name: ČEZ ESCO
  url: https://www.cezesco.cz/
  ico: '03592880'
  since: 2014
  competes: adjacent
  maturity: established
  evidence: 'Designs and builds depot and route chargers for electric buses, bought outright by the
    bus company: 48 charging points for the Liberec and Jablonec transport company and 8 for the
    Opava one, plus a charging hub in Kladno. Named customers, founded 2014. It sells the chargers,
    not the buses or their financing [S11].'
- name: E.ON Energie
  url: https://www.eon-drive.cz/reseni-pro-dobijeni-elektrobusu-v-tabore/
  ico: '26078201'
  since: 2004
  competes: adjacent
  maturity: established
  evidence: 'Designed and built two charging depots for a private bus operator''s 14 electric buses
    in Tábor, a named customer; company founded 2004. It sells charging design and building, not the
    buses or their financing [S11].'
- name: SOR Libchavy
  ico: '15030865'
  since: 1991
  competes: adjacent
  maturity: established
  evidence: 'Czech bus maker that sells electric buses to city transport companies, named customers
    in Prague and Opava; in Opava its winning offer included the chargers and ten years of charger
    service. The buses are bought outright, so it sells no financing or fee per bus [S11].'
- name: SOLARIS CZECH
  ico: '25914723'
  since: 2002
  competes: adjacent
  maturity: established
  evidence: 'Czech arm of a Polish bus maker; won the Ostrava and Olomouc transport companies''
    electric-bus tenders, named customers. It sells the buses with service and mobile chargers,
    bought outright, not financing or a fee per bus [S11].'
- name: MAN Truck & Bus Czech Republic
  ico: '46965904'
  since: 1992
  competes: adjacent
  maturity: established
  evidence: 'Czech company of the MAN bus and truck group; won the Frýdek-Místek and Karviná city
    bus operator''s electric-bus tender and signed for 6 buses, a named customer; registered 1992.
    It sells the buses outright, not financing, chargers or a fee per bus [S12].'
- name: Deutsche Leasing ČR
  ico: '25723758'
  since: 1998
  competes: adjacent
  maturity: early
  evidence: 'Prague leasing company, registered 1998, that leases transport equipment, buses
    included, with full-service leasing among its products. No electric-bus or charger offer was found,
    and nothing found meets the second half of the maturity test. It
    finances vehicles in general and does not build or run chargers [S11].'
sources:
- type: regulation
  name: 'Act 360/2022 Sb. on clean vehicles in public contracts'
  gist: 'the clean-bus shares and the fine'
  why: 'The Czech law that sets how many of the city buses a public buyer purchases, leases or orders through a bus-service contract must be clean: 60% from 2026 to 2030, half of them zero-emission, with fines up to 20M CZK.'
  url: https://www.zakonyprolidi.cz/cs/2022-360
  note: 'zakonyprolidi.cz, saved as data/raw/2026-09-19/funded/mobility/cz-zakon-360-2022.html, read
    2026-09-19. § 2(1): applies to contracts signed until 31 Dec 2030 for a) above-threshold public
    contracts to buy, lease or rent vehicles, which the zadavatel under § 4(1) and (3) of the public
    procurement act had to award, and c) public passenger transport services above the EU
    thresholds. § 4(1): "Zadavatel a objednatel ... jsou povinni dodržet minimální podíly
    nízkoemisních vozidel", for class I and A M3 buses and trolleybuses "41 % ode dne nabytí
    účinnosti tohoto zákona do 31. prosince 2025" and "60 % od 1. ledna 2026 do 31. prosince 2030".
    § 4(4): half of the share by vehicles without a combustion engine or under 1 g CO2/kWh. § 3(c):
    a low-emission bus is one using an alternative fuel. § 5: joint fulfilment allowed. § 11(1)(a):
    a zadavatel or objednatel commits an offence by not meeting § 4; § 11(5): fine up to 20,000,000
    Kč; § 12: ÚOHS hears it. Private operators that are not zadavatel are not named in § 4; a
    region or town is bound as objednatel for bus-service contracts. No enforcement receipt was
    found (web search 2026-09-19).'
  date: '2022-11-03'
- type: news
  name: 'E15 — electric buses may cost transport companies more'
  gist: 'grant clawbacks and the price gap'
  why: 'A business-news report on Czech city transport companies: electric buses pay off only with EU grants, a grant is repaid in part if buses run too few kilometres or arrive late, and the transport companies'' association says others face the same risk.'
  url: https://www.e15.cz/byznys/doprava-a-logistika/elektrobusy-se-mohou-dopravnim-podnikum-prodrazit-hrozi-ze-prijdou-o-prislibene-dotace-1411340
  note: 'Saved data/raw/2026-09-19/funded/mobility/cz-e15-elektrobusy-dotace.html, read 2026-09-19;
    dated 2023-11-02 per the arb-scan manifest. "Tyto vozy se ale dopravcům vyplácí pořizovat jen v
    případě, že dostanou dotace od Evropské unie"; DPP spokesman: "musí alikvotní část dotace
    vrátit" if vehicles miss planned kilometres; "může podnik přijít o dotaci ve výši téměř 206
    milionů korun" over late trolleybuses from SOR; "Cena nového elektrobusu se na trhu nyní pohybuje
    kolem čtrnácti milionů korun ... Naftový autobus stejné kategorie vyjde podniky na asi šest
    milionů"; chargers must be built and "Na tyto investice musí podnik vytvářet odpisy"; without
    grants e-bus operation "dražší o zhruba patnáct procent"; Prague budget burden "zvýšila asi o
    miliardu ročně" without grants; Sdružení dopravních podniků ČR spokeswoman: "žadatel o dotaci
    přijde kvůli nedodržení termínů", and without grants "platí veškeré náklady". The article''s "do
    konce roku 2035 ... šedesát procent jejich flotil" misstates the law (S1) and is not used.'
  date: '2023-11-02'
  dims: [demand]
- type: news
  name: 'Československý Dopravák — Prague operator tenders up to 40 electric buses'
  gist: 'a grant for only part of the fleet'
  why: 'A Prague bus operator tendering up to 40 electric buses got a grant for 41% of the cost of 22 of them and none for one size class, and its current city contracts to 2031 do not allow a change of drivetrain.'
  url: https://www.cs-dopravak.cz/dopravce-about-me-vypsal-soutez-na-az-40-elektrobusu/
  note: 'Read 2026-09-19, article 2026-08-19. ABOUT ME s.r.o. (ROPID/PID operator) tenders 10 Sd at
    12.401M, 10 Md+ at 10.508M and 20 Md at 10.041M CZK each (estimated values); grant 146M CZK, 41%
    of 353.32M, for 22 buses (20 Md, 2 Sd) from MODF-TRANSGOV 1/2025; no grant for Md+. "Ani jedna z
    uvedených smluv ale neumožňuje změnu pohonu vozidel"; contracts for lines 153, 164, 194, 242,
    243, 117, 203 run to 30 Apr 2031. Battery warranty 60 months at 80% capacity required. Bids due
    17 Sep 2026. Ledger: ted-572969-2026, ted-574507-2026, ted-575233-2026.
    Added 2026-09-19 (weekly match): the three tenders were re-notified on TED on 14 Sep 2026
    (ted-631809-2026 Sd, ted-630176-2026 Md+, ted-631151-2026 Md), each a change notice
    "Prodloužení lhůty pro podání nabídek do 01.10.2026, 10:00 hodin", reason "Vyhovění žádosti
    dodavatele": bids now due 1 Oct 2026, at a supplier''s request. Not cited separately. The TED
    lot values are 124,005,400 CZK for 10 Sd, 100,409,250 CZK for 10 Md+ and 210,165,500 CZK for
    20 Md, i.e. 12.401M, 10.041M and 10.508M a bus: the article''s per-bus figures for Md and Md+
    appear swapped. No rendered sentence uses the per-class figures.'
  date: '2026-08-19'
  dims: [demand]
- type: subsidy
  name: 'IROP call 121 — zero-emission vehicles for public transport'
  gist: 'the grant for electric buses'
  why: 'The EU-funded grant call for electric and hydrogen buses in public transport, open to regions, towns and bus operators with public-service contracts in the less developed regions, from April 2026 to March 2027 or until the money runs out.'
  url: https://irop.gov.cz/cs/vyzvy-2021-2027/vyzvy/121vyzvairop
  note: 'Read 2026-09-19 via fetch. "121. výzva IROP - Bezemisní vozidla pro veřejnou dopravu - SC
    6.1 (MRR)"; eligible "Kraje, obce, dopravci na základě smlouvy o veřejných službách v přepravě
    cestujících"; allocation 685,060,360 CZK from ERDF incl. a 291M increase announced 3 Sep 2026;
    applications 14 Apr 2026 14:00 to 31 Mar 2027 14:00, earlier if exhausted; "Naplnění alokace
    výzvy 74,6 %" as of 18 Sep 2026; projects to finish by 30 Jun 2029; less developed regions only;
    subsidy rate not stated on the page. The ledger signal (dotace-irop-121-122-bezemisni-vozidla)
    recorded call 121 as 129.7% subscribed before the increase; the page no longer says so.'
  date: '2026-09-18'
  signal: dotace-irop-121-122-bezemisni-vozidla
- type: arbitrage
  name: 'Zenobē — €325M for fleets as a service in Europe'
  gist: 'British e-bus fleets as a service'
  why: 'A London company that finances electric buses and runs their depot charging for bus operators, with named customers in Britain and Spain, raising debt in 2025 to expand in continental Europe.'
  url: https://www.zenobe.com/news-and-events/zenobe-raises-e325-million-to-fund-electric-vehicle-fleet-investment-as-part-of-european-expansion-initiative/
  note: 'gb-zenobe (ledger). Re-read 2026-09-19 via fetch: "financing of the vehicles and design,
    construction, maintenance and operation of the charging infrastructure"; began operations in
    2017; National Express Coventry 130 buses, Go-Ahead Oxford 104 charge points, Grupo Julià 44
    buses; 3,400+ vehicles across 120 depots; EUR 325M debt facility closed 24 Jul 2025 from seven
    lenders, for up to 1,000 more buses, trucks and chargers in the EU/EEA. The release lists teams
    in Germany, Spain, Belgium, the Netherlands and Sweden; only Spain carries a named customer, so
    only ES is recorded in markets.'
  date: '2025-07-24'
  signal: gb-zenobe
- type: arbitrage
  name: 'Deutsche Leasing — electric-bus fleet for Lübeck'
  gist: 'German e-bus and charger leasing'
  why: 'A German leasing company''s case study: it finances 85 electric buses for the Lübeck city bus company, charging infrastructure included.'
  url: https://www.deutsche-leasing.com/de/themenwelt/beitraege/luebeck-setzt-auf-55-e-busse
  note: 'Read 2026-09-19 via fetch, article 10 Jul 2025: "Wir finanzieren 85 Elektrobusse inklusive
    Ladeinfrastruktur und technischer Anlagen"; knapp EUR 66M over 2023-2027; "rund 28 Millionen
    Euro über die Deutsche Leasing AG refinanziert" in 2025, paid in tranches. The ÖPNV page
    (deutsche-leasing.com/de/loesungen/transport-logistik/oepnv) offers leasing to transport
    operators and names Lübeck (85 e-buses), Stadtrundfahrt Dresden and Ettenhuber. Founded 10 Jan
    1962 (Wikipedia). It finances the buses and chargers; it does not build or run the chargers.'
  date: '2025-07-10'
- type: price
  name: 'Opava transport company — electric buses with chargers'
  gist: 'buses, chargers and charger service'
  why: 'The winning offer in the Opava city transport company''s first electric-bus tender: 8 buses, the chargers and ten years of charger service.'
  url: https://www.cs-dopravak.cz/prvni-elektrobusy-do-opavy-doda-sor-libchavy/
  note: 'Read 2026-09-19 via fetch, article 8 Nov 2024: SOR Libchavy offered "106 576 500 Kč, jeden
    vůz pak vycházel na 12 300 000 Kč, zbytek byly náklady na zřízení nabíjecí infrastruktury a
    vyčíslené servisní náklady na nabíjecí systém po dobu deseti let"; 8 buses in four deliveries of
    two. Awarded: a ČEZ press release of 21 Feb 2026 (parlamentnilisty.cz) reports SOR buses in
    service in Opava with 8 DC charging points from ČEZ ESCO. VAT treatment not stated. Ledger
    ted-558233-2026 is a later Opava tender.'
  date: '2024-11-08'
  dims: [money]
  payer: 'Městský dopravní podnik Opava (city transport company)'
  amount_czk: 106576500
  unit: per-project
  basis: tender-line
- type: price
  name: 'Liberec and Jablonec transport company — depot chargers'
  gist: '48 electric-bus charging points'
  why: 'The Liberec and Jablonec city transport company''s contract for 48 electric-bus charging points at three sites, won in a tender and signed in November 2025.'
  url: https://www.busportal.cz/clanek/do-liberce-prijedou-v-prosinci-nove-elektrobusy-21145
  note: 'Busportal, 4 Dec 2025, read 2026-09-19 via fetch: ČEZ ESCO won the tender; contract signed
    12 Nov 2025; 138.9M CZK without VAT for 48 charging stations (40 at the bus depot, 4 at the tram
    depot, 4 at a turnaround); 360 days to finish. The same article: the company buys used Solaris
    e-buses, one Urbino 18 for 7.55M and three Urbino 12 for 15.45M CZK.'
  date: '2025-11-12'
  dims: [money]
  payer: 'Dopravní podnik měst Liberce a Jablonce nad Nisou (city transport company)'
  amount_czk: 138900000
  unit: per-project
  basis: signed-contract
- type: price
  name: 'Ostrava transport company — 70 electric buses'
  gist: 'the largest Czech e-bus contract'
  why: 'The Ostrava city transport company signed for up to 70 electric buses with software, service equipment, training and 8 mobile chargers, more than half paid by EU grants.'
  url: https://www.dpo.cz/aktualne/novinky/2026-07-30-tz-elektrobusy.html
  note: 'DPO press release 30 Jul 2026, read 2026-09-19 via fetch: contract signed with Solaris,
    "Vítězná nabídka společnosti Solaris má hodnotu téměř devíti set milionů korun (895 603 610
    Kč)"; more than half covered by EU grants (Modernisation Fund, national and ITI IROP). Busportal
    17 Aug 2026: 895.6M CZK without VAT, up to 30 buses with 350 km and 40 with 250 km range; price
    includes "software, servisní a diagnostické vybavení, školení, technickou podporu a osm
    mobilních nabíjecích zařízení". Ledger ted-567801-2026.'
  date: '2026-07-30'
  signal: ted-567801-2026
  dims: [money]
  payer: 'Dopravní podnik Ostrava (city transport company)'
  amount_czk: 895603610
  unit: per-project
  basis: signed-contract
- type: news
  name: 'Dopraváček — nearly 50 electric buses for Central Bohemia'
  gist: 'chargers in operators'' own yards'
  why: 'The Central Bohemian region approved nearly 50 electric buses on its bus lines from 2028 to 2030, with chargers to be built in the bus operators'' own yards or at end stops.'
  url: https://dopravacek.eu/2026/09/13/temer-padesat-elektrobusu-pro-stredocesky-kraj-zamiri-na-devet-oblasti/
  note: 'Saved data/raw/2026-09-19/funded/mobility/cz-dopravacek-stc-elektrobusy.html, read
    2026-09-19; canonical url and article:published_time 2026-09-13 from the saved page. "Téměř padesát nových elektrobusů ... mezi
    lety 2028 až 2030"; nine areas; "Dobíjecí stanice vzniknou v areálech jednotlivých dopravců nebo
    na vhodných konečných zastávkách".'
  date: '2026-09-13'
  dims: [demand]
- type: gap-check
  name: 'Czech check — who sells electric buses as a service'
  gist: 'the Czech field, searched'
  why: 'Czech-language web search, the state business register and our own funding ledger: Czech bus makers and energy companies sell electric buses and depot chargers outright, and leasing firms finance vehicles in general, but nobody offers the buses, batteries and chargers for a fee per bus.'
  url: https://www.eon-drive.cz/reseni-pro-dobijeni-elektrobusu-v-tabore/
  note: 'Gap check 2026-09-19. SURFACES: the agent web-search tool, Czech-language (logged as
    google-cz, which it is not); ARES name search (Zenob 0; ČEZ ESCO 03592880 2014-11-25; E.ON
    Energie 26078201 2004-07-27; Deutsche Leasing ČR 25723758 1998-12-23; SOR Libchavy 15030865
    1991-12-06; SOLARIS CZECH 25914723 2002-08-23; Daimler Buses Česká republika 25657704, no Czech
    e-bus or charger offer found, not recorded as a player); data/signals/funded (no Czech e-bus
    finance entrant); data/lookup/cz-contract-parties.jsonl (ČEZ ESCO and E.ON one public buyer
    each, so their established limb is named customers). The arb-scan pass for gb-zenobe ran five
    further Czech queries the same day with the same result (listed below). FOUND, ADJACENT: ČEZ
    ESCO — Liberec/Jablonec 48 charging points (busportal 4 Dec 2025, S8), Opava 8 DC points (ČEZ
    press release 21 Feb 2026 via parlamentnilisty.cz), Kladno hub for Arriva (search results; the
    Arriva release returned 404). E.ON Energie — two depots for COMETT PLUS''s 14 e-buses, privately
    financed by the operator (eon-drive.cz, 2025). SOR Libchavy — Opava offer incl. chargers and
    10-year charger service (S7); DPP up to 100 e-buses incl. chargers (ČT24 search result). SOLARIS
    CZECH — Ostrava 70 (S9), Olomouc 20 (dpmo.cz search result). Deutsche Leasing ČR — its Czech
    page lists "Dopravní a manipulační technika" and "Leasing s kompletními službami", no e-bus
    offer. UniCredit Leasing CZ and ČSOB Leasing finance transport equipment per search snippets,
    pages not read, not recorded. No Czech offer of electric buses plus battery finance plus depot
    charging for a fee per bus was found; a 2016 conference report (mhdzive.cz) lists loans and
    operating leases as options without naming a seller. POSITIVE CONTROLS: (1) in-market — the
    descriptive query "elektrobusy jako služba pronájem elektrobusů včetně nabíjení dopravce"
    surfaced E.ON Drive''s Tábor charging page without naming it: PASSED. (2) register control —
    "systém řízení přeprav a rezervace časových oken na rampách česká firma" surfaced Ringil
    (ringil.com, LinkedIn): PASSED. Query 4 names ČEZ ESCO and is a follow-up, not a control.'
  date: '2026-09-19'
  queries:
    - "elektrobusy jako služba pronájem elektrobusů včetně nabíjení dopravce"
    - "operativní leasing elektrobusů dopravní podnik baterie nabíjecí stanice"
    - "výstavba nabíjecí infrastruktury pro elektrobusy depo dopravce na klíč ČEZ ESCO"
    - "ČEZ ESCO elektrobusy nabíjení dopravní podnik Kladno hub smlouva provoz"
    - "\"elektrobusy\" \"jako službu\" OR \"formou služby\" dopravce nabíjení financování Česko"
    - "pronájem elektrobusů dopravcům měsíční poplatek včetně baterie servis nabíjení"
    - "financování elektrobusů bez dotace pro autobusové dopravce ve veřejné linkové dopravě nabídka firma"
    - "leasing elektrobusů pro dopravce financování ČSOB Leasing OR \"Deutsche Leasing\" OR \"UniCredit Leasing\" elektrobus"
    - "Škoda Group elektrobusy dodávka včetně nabíjecí infrastruktury servis dopravní podnik smlouva na klíč"
    - "Solaris Czech OR \"SOR Libchavy\" elektrobusy dodávka nabíječek a servisní smlouva full service dopravní podnik"
    - "Deutsche Leasing ČR financování autobusů dopravci"
    - "elektrobusy jako služba financování nabíjecí infrastruktura dopravce pronájem elektrobusů Česko"
    - "operativní leasing elektrobusů včetně baterií a nabíjení pro dopravce"
    - "\"elektrobus jako služba\" OR \"bus as a service\" Česko dopravce nabídka"
    - "výstavba a provoz nabíjecí infrastruktury pro elektrobusy v depu dopravce na klíč financování"
    - "dopravce autobusy přechod na elektrobusy kvóty zákon 360/2022 nabíjení depo řešení na klíč firma"
    - "systém řízení přeprav a rezervace časových oken na rampách česká firma"
  checked: [google-cz, ares, own-funded-ledger]
  expires: '2026-12-18'
- type: price
  name: 'Frýdek-Místek and Karviná bus operator — 6 electric buses'
  gist: '6 electric city buses, signed'
  why: 'The operator of city buses in Frýdek-Místek and Karviná bought 4 electric buses in a tender and took up its option on 2 more in August 2026, with EU grant money behind the project.'
  url: https://ted.europa.eu/en/notice/-/detail/636484-2026
  note: 'ted-636484-2026, TED contract-modification notice published 16 Sep 2026, XML read
    2026-09-19 (saved in the run scratchpad). Buyer Transdev Slezsko a.s. (IČO 45192081), supplier
    MAN Truck & Bus Czech Republic s.r.o. (IČO 46965904). Original contract: "Nákup 4 ks městských
    elektrobusů délkové kategorie 11,5-13 m", winner chosen 13 Apr 2026, purchase contract dated
    25 May 2026, option for 2 more. Modification: "Rozšíření plnění o další 2 elektrobusy, zvýšení
    celkové kupní ceny na 75.447.000,- Kč bez DPH", reserved change under § 100(1) ZZVZ; the buses
    are zero-emission M3 buses meeting § 3(c) and § 4(4) of act 360/2022; "Smlouva na pořízení
    dalších 2 ks elektrobusů byla podepsána 17.8.2026". Funded from IROP, project "Navazující
    projekt částečné elektrifikace MHD Frýdek-Místek a MHD Karviná". 75,447,000 CZK without VAT
    for 6 buses, about 12.6M a bus (our division). Outright purchase, read as the manual form of
    a fee per bus, as for S7-S9.'
  date: '2026-08-17'
  signal: ted-636484-2026
  dims: [money]
  payer: 'Transdev Slezsko (city bus operator in Frýdek-Místek and Karviná)'
  amount_czk: 75447000
  unit: per-project
  basis: signed-contract
- type: tender
  name: 'TED — Olomouc transport company re-tenders its depot chargers'
  gist: 'charger tender, second attempt'
  why: 'The Olomouc city transport company closed its tender for electric-bus chargers at four sites without a winner and tendered them again the next day; the chargers must fit the specific electric buses it already bought.'
  url: https://ted.europa.eu/en/notice/-/detail/627506-2026
  note: 'ted-627506-2026, contract notice published 11 Sep 2026, XML read 2026-09-19: Dopravní
    podnik města Olomouce (IČO 47676639), "Výstavba dobíjecích stanic pro bezemisní vozidla MHD",
    charging stations for electric buses at four sites incl. design, estimated 206,500,000 CZK, bids
    due 18 Oct 2026, IROP call "Plnicí a dobíjecí stanice pro veřejnou dopravu (SC 6.1)"; "konkrétní
    pořizovaná vozidla jsou Solaris new Urbino 12 electric a Solaris new Urbino 18 electric.
    Nabíjecí infrastruktura ... proto musí být kompatibilní". The first attempt, ted-623121-2026
    (result notice published 10 Sep 2026, estimated 188,500,000 CZK, same title and scope), closed
    with winner-selection-status clos-nw (no winner, competition closed), 2 tenders received,
    non-award code tch-pr-error, 1 review request logged; the notice gives no reason in words. Not
    awarded, so not a price receipt; the charger half of the job bought separately. Backs no score.'
  date: '2026-09-11'
  signal: ted-627506-2026
  dims: []
- type: tender
  name: 'TED — Prague transport company, up to 200 diesel and hybrid buses'
  gist: 'hybrids counted as clean buses'
  why: 'Prague''s city transport company is tendering a five-year framework for up to 100 diesel and 100 mild-hybrid city buses, and requires the hybrids to meet the clean-vehicle law''s definition of a low-emission bus.'
  url: https://ted.europa.eu/en/notice/-/detail/624737-2026
  note: 'ted-624737-2026, change notice published 10 Sep 2026 ("Prodloužení lhůty pro podání
    nabídek", bids due 5 Oct 2026), XML read 2026-09-19; earlier notices ted-487706-2026 and
    ted-558632-2026. Dopravní podnik hl. m. Prahy (IČO 00005886), "Rámcová dohoda na nákup až 200
    ks městských standardních autobusů", estimated 1,581,000,000 CZK: "maximálně 100 kusů naftových
    autobusů a maximálně 100 kusů mild-hybridních autobusů"; "Mild-hybridní autobusy musí splnit
    definici nízkoemisního vozidla kategorie M3 dle § 3 odst. c) zákona 360/2022 Sb." No electric
    bus in it. Context on how a large buyer meets the low-emission half of the share (S1 § 4(4)
    requires only half of it to be zero-emission); not this job, backs no score.'
  date: '2026-09-10'
  signal: ted-624737-2026
  dims: []
created: '2026-09-19'
updated: '2026-09-19'
---

Czech city bus companies must add electric buses they can barely afford without EU grants, and those grants can be taken back [S1,S2].

- In 2023 an electric bus cost 14M CZK, a diesel one 6M [S2].
- Prague's transport company risked a 206M CZK grant over a late delivery [S2].
- One Prague operator got a grant for only 22 of its 40 buses [S3].

What a bus company carries today:

- A grant is repaid in part if the buses run fewer kilometres than planned [S2].
- The company must also build chargers and write them off over the years [S2].
- Before grants, Prague's electric buses cost about 15% more to run than diesel ones [S2].
- Without grants, Prague's budget would carry about 1bn CZK more a year [S2].
- The transport companies' association says others can lose grants over late deliveries too [S2].
- The Central Bohemian region plans nearly 50 electric buses for 2028 to 2030, with chargers in the operators' own yards [S10].
- A Prague operator's city contracts run to 2031 and do not allow a change of drivetrain [S3].
- Olomouc's transport company closed its first tender for depot chargers without a winner in September 2026, and tendered them again the next day [S13].
- Those chargers must fit the particular electric buses the company has already bought [S13].

Existing non-solutions: Czech bus makers and energy companies sell electric buses and depot chargers outright, and nobody offers them for a fee per bus [S11].

- Bus makers sell the buses, sometimes with chargers and years of charger service [S11].
- Energy companies design and build depot chargers [S11].
- Leasing companies finance vehicles in general, with no offer for electric buses found [S11].

So the bus company still pays up front and needs a grant to afford it [S2,S11]. The rows are under [Market gap](#competition).

Why now: City bus companies buying buses since January 2026 must make 60% of them clean, or face a fine of up to 20M CZK [S1].

- A bus company missing the share can be fined up to 20M CZK [S1].
- In 2023 an electric bus cost more than twice a diesel one [S2].
- A bus delivered late can cost the company its grant [S2].

The dates behind this:

- From 1 January 2026, 60% of the city buses a public buyer contracts for must be clean [S1].
- Half of that share must be buses with zero emissions [S1].
- The rest of the share can be low-emission buses: Prague's transport company is tendering up to 100 diesel and 100 mild-hybrid buses, and requires the hybrids to meet the law's low-emission definition [S1,S14].
- The first period's share of 41% ran until the end of 2025 [S1].
- The 60% share runs until 31 December 2030 [S1].
- Regions and towns that order bus lines from private operators must meet the same shares in those contracts [S1].
- The current EU grant call for electric buses is open until 31 March 2027, or until its money runs out [S4].

Who pays: Yes, city transport companies already pay for electric buses and depot chargers, with EU grants covering part of the cost [S2,S4].

- The grant is open to regions, towns and bus operators with public contracts [S4].
- It covers only the less developed regions, not Prague [S4].
- A Prague operator got 41% of the cost of 22 buses [S3].

The contracts they signed are under [Willing to pay](#willing-to-pay).

Solved elsewhere: In Britain and Germany, bus companies already get electric buses and their chargers financed by a specialist instead of buying them [S5,S6].

- The British company raised €325M in July 2025 to expand into Europe [S5].

See [Validated abroad](#validated-abroad).

## First moves

1. Ask the fleet manager of a mid-size Czech city bus company what monthly fee per electric bus, chargers included, would beat buying one. The companies in [The opportunity](#opportunity) carry the price and the clawback risk themselves, so they know exactly what it costs them. Their answer is the price you have to reach.
2. Partner with one of the energy companies under [Market gap](#competition) that already build depot chargers for bus companies. They bring the charging work and the grid connection; you bring the money and the fee per bus, so neither of you has to start from nothing.
3. Take that price to a bank or leasing company that finances buses, and ask what funding a first small fleet would take. Show them the signed contracts under [Willing to pay](#willing-to-pay) to prove city bus companies spend this money already.
4. Talk to a regional transport organiser about its next bus-line contracts. The law under [Why now](#why-now) makes regions meet the same shares, so a private operator that can bring electric buses without a grant has an easier way to win those lines.

## Revisions

2026-09-19 · record created — Created from gb-zenobe with the ledger's Czech e-bus tenders, contracts and grant call. Scores on the 2026-09-19 ladders. Proof 3: Zenobē runs the whole model in Britain and Deutsche Leasing finances e-buses with their chargers in Germany, both established [S5,S6]; counting a finance-only comp is a judgement call. Money 2: three paid receipts within 24 months, for buses, chargers and a bus-plus-charger tender [S7,S8,S9]; reading an outright purchase as the manual form of a fee per bus is our judgement. Urgency 2: the law binds public buyers, which the city transport companies are, and its 60% share applies from 1 January 2026, within 12 months; a fine is named but no enforcement receipt was found, so not 3 [S1]. Private operators are not bound directly, only through the regions' contracts [S1]. Demand 2: the association and two operators on record [S2,S3]. Gap 2: nobody sells the bundle; the Ringil and in-market controls passed [S11]. Our readings, flagged: "more than twice" is 14M against 6M, a 2023 price, so the headline does not use it (coordinator edit, same day) [S2]; the 14M price is from 2023, and 2026 tenders run about 10M to 12.8M a bus [S3,S9]; the E15 claim of a 2035 fleet share misstates the law and is not used [S2]. The ledger's 129.7% grant oversubscription is no longer on the call page, which now shows 74.6% taken after a top-up [S4]. No draft-law badge: the law is in force. Build-gate fix, same day: Deutsche Leasing left comps[] because the comps schema cannot hold a founding year before 1980 (it was founded 1962) and a false year would dodge the gate; its Lübeck case stays as a source [S6]. Proof 3 to 2 (one established player, Zenobē, in Britain and Spain; Spain is not CEE-adjacent), score 11 to 10; the solution now counts one company. Same date, weekly match, merged here: evidence audit — linked a signed contract for 6 electric buses in Frýdek-Místek and Karviná [S12], whose seller joins `locals[]` as adjacent; Olomouc's charger tender, closed without a winner and re-run the next day [S13]; and Prague's diesel and mild-hybrid framework [S14]. S3's note records the Prague operator's extended bid date. Gap re-checked: no one sells a fee per bus, stays 2. No score moved: money was already 2.
