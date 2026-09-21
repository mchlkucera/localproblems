---
id: p-0047
region: cz
title: 'Many Czech food buyers still take farm deliveries on spoken deals. One was fined 1,040,000 CZK, and by 2028 farm deliveries need a written contract.'
brief: 'The competition office looked at 488 food buyers and found spoken orders still common, and fruit collection points buying with no contract at all [S3]. From 19 August 2028 every farm delivery needs a written contract agreed first [S1].'
solution: 'Build software inside a produce buyer''s own trading and weighing system that writes each delivery contract with the price rule the law wants, sends it for electronic signature before the load moves and files it, as 3 companies already do in 2 other countries.'
good_for: 'Someone who knows how grain and produce are bought and can sell to traders.'
price_search: 'Ask a grain or fruit collection point what its harvest paperwork costs in staff time, read a Czech law firm''s published rate for drafting a supply contract, and search the public contracts register for what Czech buyers pay the electronic-signature vendors per document.'
category: legal-compliance
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 0
  urgency: 1
  demand: 2
  gap: 2
status: candidate
entry:
  level: moderate
  buyer: large-firms
  permission: none
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed to sell this, the buyers already run trading and weighing software it can sit in, and no Czech firm sells the contract side. Harder: the first customers are commodity traders and processors with their own systems, and the duty starts in 2028, so nobody is in a hurry yet.'
comps:
- name: Docuten
  url: https://docuten.com/
  geo: ES
  since: 2009
  traction: 'Sells electronic signature and invoicing, and since 2024 an agrifood line that writes
    food-chain contracts with the fields Spanish law requires, signs them, files them in the state
    food-contract register and keeps them the 4 years the law demands (company blog, read 2026-09-21).
    Claims more than 100 clients in the agrifood sector; Danone, Coosur, Estrella Galicia and Monbake
    are named on the company site; it is a qualified trust service provider under the EU e-signature
    rules. Founded 2009 (FHalmería, 3 October 2024).'
- name: Perfarmer
  url: https://perfarmer.com/
  geo: FR
  since: 2018
  traction: 'Sells cooperatives and grain merchants a mobile app that publishes their purchase prices
    to member farmers, generates the contracts and runs the collection campaign. More than 28,000
    farmers, about 50 cooperatives and merchants, and 2 million tonnes sold through the app in 2024,
    close to double 2023 (FrenchWeb, 1 March 2025). A named customer, the Lorraine farm cooperative
    with about 2,500 members and 350,000-400,000 tonnes a year, signed up more than 400 farmers in
    the first week (La Ferme Digitale, 24 October 2023). Founded 2018 (FrenchWeb).'
- name: Asape
  url: https://www.asape.fr/
  geo: FR
  since: 2005
  traction: 'Sells cooperatives and grain merchants a customer system whose market module runs grain
    contracts online: contract entry, price fixing and a back office that validates or refuses each
    sale order (product page, read 2026-09-21). 160 clients, 5,000 users, 35 staff and "20 ans
    d''expertise" on its own site (2026); Euralis, Cérésia, Océalia, Agrial, Vivescia and Groupe Carré
    are named as clients.'
locals:
- name: Prosystem
  url: https://www.prosystem.cz/cz/aplikace/nadas-trade
  ico: '46579982'
  since: 1992
  competes: adjacent
  maturity: established
  evidence: 'Sells NADAS Trade, a back office for firms that trade farm commodities: contracts and
    how far they have been filled, industrial weighing, stock, trader commissions and invoicing
    (product page, 2026). 20 named customers on its reference page, which does not say which of them
    use this product. It is the buying firm''s own system, and it neither sends a farmer a contract to
    sign nor keeps the signed contracts [S11].'
- name: CleverFarm
  url: https://www.cleveranalytics.ag/
  ico: '05215480'
  since: 2016
  competes: adjacent
  maturity: established
  evidence: 'Sells precision farming, farm records, land-lease records and CleverAnalytics, which
    shows commodity buying prices refreshed every 15 minutes and lets a farmer sell to a chosen
    trader inside the app; ASTUR Straškov and AZOS Zakřany are named customers (site, 2026). It
    closes the deal and lists the orders, and offers no written delivery contract, signature or
    archive [S11].'
- name: AG info
  url: https://www.aginfo.cz/
  ico: '60931906'
  since: 1994
  competes: adjacent
  maturity: established
  evidence: 'Sells Agronom and land records to farms, with 1,711 customers and 5,815 active
    installations on its own site (2026). The contracts its software writes are land leases between a
    farm and a landowner, not contracts for the produce the farm sells [S11].'
- name: Geocentrum
  url: https://www.gcupravy.cz/
  ico: '47974460'
  since: 1993
  competes: adjacent
  maturity: established
  evidence: 'Sells the GC ÚPRAVY land, agronomy and livestock records to more than 750 farms covering
    1.2 million hectares, with 14 named customers on its site (2026). Its contract machinery writes
    land leases and the rent paid on them, not the sale of a harvest [S11].'
- name: Legito
  url: https://www.legito.com/cs
  ico: '02649659'
  since: 2014
  competes: adjacent
  maturity: established
  evidence: 'Sells contract automation, templates and electronic signature to firms in any trade, with
    named customers PwC, Deloitte Legal, Santander and Škoda on its site (2026). Its Czech marketplace offers a
    general purchase-contract template and nothing built for farm deliveries: no price rule from cost
    indicators, no quality deductions, no tie to a weighbridge [S11].'
sources:
- type: regulation
  name: 'Regulation (EU) 2026/1739 — written contracts in the farm and food chain'
  gist: 'the 2028 contract duty'
  why: 'The EU law that rewrites Article 168 of the farm-market regulation: from 19 August 2028 a delivery of farm produce by a farmer, a farmers'' association or a producer organisation to a processor, distributor or retailer must be covered by a written contract agreed before delivery, with a price or a price formula, quantity, quality, timing, duration, payment period, collection and force majeure.'
  url: https://eur-lex.europa.eu/eli/reg/2026/1739/oj
  note: 'reg-agri-pisemne-smlouvy-2028. CELEX 32026R1739 read in full 2026-09-21 from the run''s own
    payload (data/raw/2026-09-21/regulation/pages/eu/32026R1739-en.txt, 83,560 chars). Header:
    "Official Journal ... L series 2026/1739 29.7.2026 REGULATION (EU) 2026/1739 ... of 8 July 2026
    amending Regulations (EU) No 1308/2013, (EU) 2021/2115 and (EU) 2021/2116 as regards the
    strengthening of the position of farmers in the food supply chain". Art 5: "shall enter into force
    on the twentieth day following that of its publication" (so 18 Aug 2026) and "Article 1, points
    (3), (4), (7)(d), (9) and (14) shall apply from 19 August 2028"; point (9) is the new Article 168.
    New Art 168(1): "Deliveries in the Union of agricultural products from a sector listed in Article
    1(2) other than milk and milk products and sugar by farmers, including farmers'' associations, or
    by producer organisations ... to processors, distributors or retailers, shall be covered by a
    written contract between the relevant parties." Art 168(4): "(a) be made in advance of the
    delivery; (b) be made in writing, including in electronic form" and content "(i) the price payable
    ... static and set out in the contract, or ... calculated by combining various factors ... which
    shall include objective indicators, indices or methods of calculation of the final price ... that
    reflect changes in market conditions and changes in relevant elements of production costs";
    (ii) quantity, quality and timing; (iii) duration, and "in the case of contracts with a minimum
    duration longer than 12 months, a revision clause that can be triggered by the farmer"; (iv)
    payment periods and procedures; (v) collection or delivery arrangements; (vi) force majeure.
    Art 168(5)(a): no contract needed for a member delivering to its own producer organisation or
    cooperative where the statutes "provide for transparent and democratically decided rules, made
    known in advance, for methods for determining the price". Art 168(6): Member States MAY exempt a
    micro or small first purchaser, deliveries worth no more than EUR 10 000, delivery and payment
    within 3 working days, seasonal or perishable products, and traditional selling practices; Art
    168(7): where such an exemption applies, the farmer "may require that any delivery ... be the
    subject of a written contract". Art 168(9): Member States may require purchasers to register the
    contracts. No penalty is set in the regulation itself; enforcement is left to Member States.
    Recital (8): "The use of written contracts plays a crucial role in the accountability of operators
    ... and prevents and addresses unfair trading practices."'
  date: '2026-07-29'
  signal: reg-agri-pisemne-smlouvy-2028
- type: regulation
  name: 'Czech act 395/2009 Sb. on significant market power in the food chain'
  gist: 'today''s narrower duty'
  why: 'The Czech law that already requires a written contract, concluded before deliveries start, between a buyer with significant market power and its supplier of farm or food products — but only where the buyer is large enough against that supplier. The competition office supervises it and can fine up to 10,000,000 CZK or 10% of net turnover.'
  url: https://www.zakonyprolidi.cz/cs/2009-395
  note: 'zakonyprolidi text read 2026-09-21. § 3b(1): "Smlouva mezi odběratelem s významnou tržní silou
    a dodavatelem, jejímž předmětem je nákup, prodej, zpracování nebo distribuce zemědělských produktů
    nebo potravinářských výrobků ... vyžaduje písemnou formu, musí být uzavřena před zahájením
    dodávek", with required content: price and how discounts are set, payment method and a due date no
    longer than 30 days from the invoice, quantity, any services and their cost, and purchase
    campaigns. § 3 sets the turnover bands (a buyer over EUR 2m against a supplier under EUR 2m, and
    so on up to EUR 350m; a Czech buyer over 5bn CZK). § 5(1): "Dozor nad dodržováním zákona vykonává
    Úřad pro ochranu hospodářské soutěže". § 8(3): "pokuta do 10000000 Kč nebo 10 % z čistého obratu".
    The written-contract duty came with act 359/2022 Sb., in force 1 January 2023, which transposed
    EU directive 2019/633 on unfair trading practices.'
  date: '2023-01-01'
- type: complaint
  name: 'Competition office — sector inquiry into the food chain, final report'
  gist: 'spoken deals, counted'
  why: 'The office examined 488 buyers of farm and food products across 19 sectors and read 4,058 contracts, orders and invoices: spoken contracts are still common in the lower links of the chain, 13 of the 59 meat buyers were working with no written contract before deliveries, fruit collection points mostly buy with no prior contract at all, and grapes are still largely ordered by word of mouth.'
  url: https://uohs.gov.cz/cs/vyznamna-trzni-sila/aktuality-z-vyznamne-trzni-sily/4068-urad-dokoncil-sektorova-setreni-v-oblasti-vyznamne-trzni-sily-vysledky-shrnul-v-zaverecne-zprave.html
  note: 'ÚOHS "Závěrečná zpráva o výsledku sektorového šetření", published 18 Dec 2024; press page read
    2026-09-21 ("téměř 500 odběratelů", "přes 4 000 smluv a dalších dokumentů", "15 správních řízení",
    9 closed with 7 fines and 2 commitment decisions, most often for missing the 30-day payment
    deadline). The 132-page report itself read 2026-09-21 as text (pdftotext) from the copy at
    ekonomickydenik.cz/app/uploads/2024/12/zaverecna-zprava-ze-sektoroveho-setreni-zvts-final.pdf.
    Table 1 totals 488 buyers and 4,058 documents over 19 named sectors (meat 59 buyers / 309
    documents; wine and spirits 66; beer 57; bread and cereals 39). p.: "Z předchozí činnosti je Úřadu
    známo, že v nižších článcích dodavatelsko-odběratelského řetězce na trhu s potravinami byly ústní
    smlouvy velmi časté." Meat chapter: "U 13 odběratelů Úřad zjistil, že obchodní spolupráce probíhala
    bez uzavřených smluv v písemné formě před zahájením dodávek ... a to i s dodavateli, vůči kterým
    mají tito odběratelé významnou tržní sílu" (10 of them got a recommendation of good practice).
    Grain chapter: "Na rozdíl od výkupen ovoce, kde je výkup většinou zajišťován bez předchozí smlouvy,
    je výkup merkantilních komodit většinou zajišťován na základě předchozích smluv", followed by the
    description of delivery windows, intake testing and delivery notes. Wine chapter: framework or
    realisation contracts in about 30% of relationships, written orders in another 25%, and "V případě
    nákupu hroznů nebo dalších výpěstků byla identifikována nadále velká míra ústních objednávek."
    Buyers'' own objection, meat chapter: "požadavek písemnosti se jeví jako poněkud problematický
    například v oblasti nákupu jatečných zvířat, především u obratově menších jatek, kdy potřeba
    flexibilní reakce na určitou situaci zužuje časový prostor pro sjednání písemné smlouvy
    předcházející samotné dodávce"; the office answers that even an ad-hoc telephone offer must be
    covered by a written order. Bread and cereals: "písemné smlouvy jsou využívány ve velké míře a
    ústní podoba smluv se v tomto sektoru prakticky nevyskytuje."'
  date: '2024-12-18'
  dims: [demand]
- type: news
  name: 'Competition office fines a farm cooperative 1,040,000 CZK'
  gist: 'a fine for no contract'
  why: 'The office fined a Czech farm cooperative for taking three deliveries of farm or food products from one supplier between February and May 2024 with no written contract concluded, and for paying four suppliers later than the law allows.'
  url: https://uohs.gov.cz/cs/vyznamna-trzni-sila/aktuality-z-vyznamne-trzni-sily/4186-uohs-ulozil-zd-trhovy-stepanov-milionovou-pokutu-za-nekale-obchodni-praktiky.html
  note: 'ÚOHS press release read 2026-09-21; decision of 16 April 2025, file S0504/2024, ZD Trhový
    Štěpánov a.s., fine 1,040,000 CZK. "převzal v období od února do května 2024 od jednoho z
    dodavatelů tři dodávky zemědělských produktů nebo potravinářských výrobků bez uzavření písemné
    smlouvy"; plus longer-than-lawful payment terms towards four suppliers in more than twenty cases.
    The fine was cut by 20% because the company admitted the conduct and agreed with the legal
    assessment. Other 2026 fines under the same act, from the office''s news index: OBI ČR 4,800,000 CZK
    (16 Jun 2026), HERO CZECH 2,280,000 CZK (22 Jun 2026), UNI HOBBY 2,200,000 CZK (29 Jun 2026),
    all for late payment rather than missing contracts.'
  date: '2025-04-16'
  dims: [demand]
- type: statistic
  name: 'Statistics office — farm output in 2025'
  gist: 'what the chain buys'
  why: 'The statistics office''s agricultural account for 2025: farm output 193.4bn CZK, of which crops 98.5bn CZK, up 7.7% on the year, with cereals 39.9% of the crop total and technical crops 22.6%; livestock output 81.4bn CZK.'
  url: https://statistikaamy.csu.gov.cz/produkce-zemedelskeho-odvetvi-mezirocne-rostla
  note: 'ČSÚ Statistika&My, "Produkce zemědělského odvětví meziročně rostla", published 24 Mar 2026,
    read 2026-09-21; source data souhrnný zemědělský účet. Total output 193.4bn CZK (+10.7%); crop
    output 98.5bn CZK (+7.7%), cereals 39.9% of it (+13.0%), technical crops 22.6% (+9.3%), vegetables
    +18.9%, potatoes +12.1%, sugar beet -13.9%; livestock output 81.4bn CZK (+15.5%).'
  date: '2026-03-24'
- type: statistic
  name: 'Statistics office — the 2020 farm census'
  gist: 'how many farms'
  why: 'The 2020 agricultural census counted 28,909 holdings in Czechia, 24,648 of them run by individuals and 4,261 by companies and cooperatives, with the average holding at 121 hectares.'
  url: https://statistikaamy.csu.gov.cz/ceske-zemedelstvi-proslo-vyraznymi-zmenami-i-diky-dotacni-politice
  note: 'ČSÚ Statistika&My on Agrocenzus 2020, read 2026-09-21: 28,909 holdings meeting the census
    threshold against 39,082 in 2000 (-26%); individuals 24,648 (85.3%), legal persons 4,261 (14.7%);
    cooperatives down 33.7% between 2000 and 2020; average area 93 ha in 2000 and 121 ha in 2020, with
    legal persons falling from 930 ha to 575 ha and individuals rising from 26 ha to 42 ha. The census
    threshold is why this number is lower than the farm register''s count of subjects.'
  date: '2021-12-09'
- type: news
  name: 'A commodity buyer''s published purchase terms'
  gist: 'contract with no price'
  why: 'The 2024 purchase terms of a mid-size Czech crop buyer show how deliveries are papered today: the framework purchase contract is concluded with no price in it, and where it refers to the price list, the price is whatever the buyer''s own list says at the time and place of delivery.'
  url: https://www.mjm.cz/exe/file/7e6d57bbb50a940e9889fcb52.pdf/MJMagro_DRP_VOP_n%C3%A1kup_2024.pdf
  note: 'MJM agro, a.s., "Všeobecné obchodní podmínky pro nákup rostlinných produktů", in force
    1 Jan 2024; PDF fetched and read as text 2026-09-21. Art 7(1): "Rámcová kupní smlouva je uzavírána
    bez konkrétní kupní ceny zboží s dohodou smluvních stran o tom, jak bude kupní cena dále sjednána."
    Art 7(3): a reference to the list price means "cena uvedená v ceníku nákupu rostlinných produktů
    kupujícího v dané době a místě dodání zboží", and the seller signs to confirm that setting the
    price this way is "dostatečně určité sjednání kupní ceny". The terms also carry moisture and
    impurity tables, drying and storage fees charged from the price, and a deemed sale at the buyer''s
    list price for goods left uncollected. One buyer''s terms, so they show what one buyer does, not
    what every buyer does.'
  date: '2024-01-01'
  dims: []
- type: arbitrage
  name: 'Docuten'
  gist: 'Spanish contract filing'
  why: 'A Spanish seller of the same job: contracts for food-chain deliveries written from templates carrying the fields the law requires, signed electronically, filed with the state food-contract register and kept for the years the law demands.'
  url: https://docuten.com/es/blog/como-automatizar-el-registro-de-contratos-alimentarios-en-el-aica/
  note: 'Docuten blog page read 2026-09-21: signature of the contract from editable templates with the
    mandatory fields, automatic identification and upload to the AICA food-contract register using a
    digital certificate, confirmation by e-mail, custody for the 4-year retention period, search for
    inspections; "contracts must be registered before delivery of the product". The duty comes from
    Real Decreto 1028/2022 of 20 Dec 2022, which set up the digital register. Docuten describes itself
    as a qualified trust service provider, which lets it file on a client''s behalf. Launch of the
    Agrotech line and the company''s age from FHalmería, 3 Oct 2024 (read 2026-09-21): launched 2024,
    "more than a decade of experience and more than 100 clients in the agrifood sector", company
    founded 2009, clients named on the company site include Danone, Coosur, Estrella Galicia and
    Monbake. The customer count is the company''s own claim carried by trade press, not an audited
    figure.'
  date: '2024-10-03'
- type: arbitrage
  name: 'Perfarmer'
  gist: 'French contracts by app'
  why: 'A French seller of the buyer-side half: cooperatives and grain merchants publish their purchase prices in its app, the member farmer sells from the phone, and the contract is generated from that.'
  url: https://www.frenchweb.fr/perfarmer-la-startup-qui-digitalise-la-commercialisation-des-cereales/451701
  note: 'FrenchWeb, 1 Mar 2025, read 2026-09-21: founded 2018 by a farmer and a former Google and Lydia
    manager; more than 28,000 farmers, about 50 cooperatives and merchants, 2 million tonnes sold
    through the app in 2024, close to double 2023; EUR 250k raised in 2018 from Thibaud Elzière,
    Frédéric Montagnon and Nicolas Steegmann. La Ferme Digitale, 24 Oct 2023 (read 2026-09-21): the
    Coopérative Agricole de Lorraine, about 2,500 active members and 350,000-400,000 tonnes a year,
    took the app to "diffuser ses prix d''achat aux adhérents, générer ses contrats et animer sa
    collecte"; more than 400 farmers registered in the first week. The tonnage and farmer counts are
    the company''s figures carried by trade press.'
  date: '2025-03-01'
- type: arbitrage
  name: 'Asape'
  gist: 'French grain contracts online'
  why: 'A French seller whose market module runs grain contracts online for cooperatives and merchants: contract entry, price fixing, and a back office that validates or refuses each sale order.'
  url: https://www.asape.fr/logiciel-crm-agricole/gestion-commerciale/
  note: 'Product page read 2026-09-21: "ASAP''marchés, contractualisation céréales en ligne" with
    "consultation, saisie des contrats et des fixations de prix", technicians contracting on a
    farmer''s behalf and head office validating or refusing sale orders. Home page (same day): "20 ans
    d''expertise", 160 clients, 5,000 users, 35 staff; client logos Euralis, Cérésia, Océalia,
    Savencia, Groupe Carré, Agrial, Vivescia, Vivadour. `since: 2005` is our arithmetic from the "20
    ans" claim, not a founding date the company publishes.'
  date: '2026-09-21'
- type: gap-check
  name: 'Czech check — who sells this here'
  gist: 'the Czech field, searched'
  why: 'Czech-language web search, the state business register and our own funding ledger: no Czech seller writes, signs and files delivery contracts for farm produce. Farm software writes land leases, one trading back office tracks contracts for the buying firm, the contract-automation tools carry no farm templates, and one commodity buyer has built its own ordering app.'
  url: https://www.prosystem.cz/cz/aplikace/nadas-trade
  note: 'Gap check 2026-09-21. SURFACES: Czech-language web search (31 queries, recorded below), ARES
    by name and by IČO, data/signals/funded. NOBODY SELLS THIS: no Czech vendor offering contract
    creation, price indexation, electronic signature and archiving for deliveries of farm produce, to
    farms or to the firms that buy from them. FOUND, ADJACENT, all recorded in locals[]: Prosystem
    spol. s r.o. (46579982, ARES 1992-06-24) with NADAS Trade, a commodity trader''s back office
    tracking contract fulfilment, weighing, stock and invoicing — the closest feature overlap found,
    and the only Czech product that models a commodity contract as an object; its 20 named reference
    customers do not say which use it. CleverFarm, a.s. (05215480, ARES 2016-07-01) with
    CleverAnalytics: buying prices every 15 minutes, MATIF, and a binding sale to a chosen trader in
    the app, named farm customers ASTUR Straškov, VITA-ZEL, AGROAPLIKACE, Exata Group, AZOS Zakřany;
    no contract document. AG info, s.r.o. (60931906, ARES 1994-02-17), 1,711 customers and 5,815
    installations, contracts = pachtovní/podpachtovní. Geocentrum spol. s r.o. (47974460, ARES
    1993-03-01) trading as GC ÚPRAVY, 750+ farms, 1.2m ha, 14 named customers, contracts = land
    leases and rent. Legito s.r.o. (02649659, ARES 2014-02-12), generic contract automation and
    signature, marketplace template "Rámcová kupní smlouva", no agri vertical. SEEN, NOT RECORDED AS
    SELLERS: ADW AGRO, a.s. (28348982, ARES 2009-06-30) runs Efektivní farma, its OWN online purchase
    channel — the farmer confirms a price and books a load to its silos, with no contract, signature
    or archive in the flow; it is a buyer building in-house, not a vendor. GrainTerminal, the 2017
    Czech grain marketplace where a binding purchase contract arose in-portal, is gone as a
    standalone: grainterminal.cz now redirects to app.cleveranalytics.ag and the shell IČO 05372585
    reads as JLF AGRO s.r.o. in ARES. WinFAS software s.r.o. (43378200), SOFTbit, AGROSOFT Tábor,
    Agdata s.r.o. (05171750), FARMTEC, AgroScan, AGRI-PRECISION: farm ERP, agronomy, livestock, land
    and telematics; Agdata''s marketing line about "obchodní i pachtovní smlouvy" is not backed by any
    product page found. Helios (via INMEDIAS), ABRA, K2, KARAT, Money, Vision: generic contract or
    kontrakt modules, no agri commodity module marketed. Aptien, Vema, Inventive, ABRA Flexi, Manažer
    smluv a dokumentů, Signi, Software602, ELO, Legisway: generic contract registers and signing. No
    buyer portal found at NAVOS, Primagra, ZZN Svitavy, MJM agro, Soufflet Agro or Agrovýkup; no model
    contract published by Agrární komora, Zemědělský svaz or SPZO. No Czech price for this job found.
    POSITIVE CONTROL: the descriptive Czech query "software pro evidenci hnojiv a postřiků pro
    zemědělce" surfaced five small Czech vendors by name — GC ÚPRAVY, CleverFarm Agroevidence, AG
    info, AgroScan, AGRI-PRECISION — plus the state''s own EPH register: PASSED, the method finds
    bootstrapped Czech agri vendors. A second, unplanned control: the query on trading systems
    surfaced Prosystem''s NADAS Trade, a 1992 Český Těšín shop that appears in no other query. Gap 2
    rests on 31 Czech queries finding land-lease software, a trader''s back office, generic contract
    tools and one buyer''s own app, and no seller of this.'
  date: '2026-09-21'
  queries:
    - "software pro evidenci smluv zemědělský podnik"
    - "smlouvy na dodávky obilí software evidence"
    - "výkupní smlouva zemědělské komodity software systém výkup obilí"
    - "správa smluv zemědělství software odběratelé dodávky komodit"
    - "software pro obchodníky s obilím kontrakty sklad vážní systém výkup zemědělských komodit ČR"
    - "\"smlouva o dodávce\" obilí zemědělec aplikace software generování smluv výkupce"
    - "elektronické podepisování smluv zemědělci družstvo digitální podpis dodávky"
    - "portál pro dodavatele obilí smlouvy online ZZN Navos Primagra"
    - "Navos ZZN portál pro zemědělce smlouvy online dodávky komodit přihlášení"
    - "Signi Legito Smlouvomat šablona kupní smlouva zemědělské komodity obilí"
    - "Aptien Signi Contractbox správa smluv modul pro zemědělství odvětvové řešení agro"
    - "Helios ABRA K2 Vision ERP modul zemědělství výkup komodit smlouvy kontrakty"
    - "Softbit informační systém zemědělská výroba výkup komodit vážní lístek smlouvy"
    - "WinFAS moduly pro zemědělce smlouvy odbyt rostlinná výroba prodej komodit"
    - "Agdata software zemědělství moduly smlouvy odbyt"
    - "AG info Agronom software moduly odbyt prodej produkce smlouvy zemědělský podnik"
    - "Agrosoft Tábor software moduly zemědělství odbyt smlouvy"
    - "Farmtec Datalogic-agro software zemědělství smlouvy prodej produkce moduly"
    - "\"Efektivní farma\" aplikace nákup komodit online smlouva"
    - "efektivnifarma.cz Efektivní farma aplikace výkup komodit ADW nebo MJM"
    - "CleverAnalytics CleverFarm prodej komodit obchodníkovi aplikace kontrakty"
    - "GrainTerminal Pawlica obchodní platforma obilí kupní smlouva elektronicky podepsat"
    - "CleverFarm GrainTerminal akvizice převzetí platforma obchodování komodity"
    - "\"evidence kontraktů\" komodity zemědělství program prodej sklizně dodávky plnění"
    - "\"digitalizace smluv\" potravinářský řetězec dodavatelé nekalé obchodní praktiky software"
    - "zemědělská prvovýroba povinné písemné smlouvy 2028 novela zákon o potravinách smluvní vztahy"
    - "povinné písemné smlouvy zemědělci nařízení 2026 článek 168 nařízení 1308/2013"
    - "nařízení 2026/1739 písemné smlouvy zemědělské produkty"
    - "PROAGRO software zemědělství smlouvy komodity portál"
    - "EU regulation 2026/1739 written contracts agricultural products mandatory CMO amendment"
    - "software pro evidenci hnojiv a postřiků pro zemědělce"
  checked: [google-cz, ares, own-funded-ledger]
  expires: '2026-12-20'
created: '2026-09-21'
updated: '2026-09-21'
---

Czech buyers of farm produce will need a written contract with each farmer before the goods move, and many have none today [S1,S3].

- 13 of 59 meat buyers checked had no written contract before deliveries [S3].
- Fruit collection points mostly buy with no prior contract at all [S3].
- Grape orders are still largely placed by word of mouth [S3].

The duty comes from a 2026 EU regulation rewriting the Union's farm-market law; milk and sugar keep their own rules [S1].

- The contract is agreed before delivery, may be electronic, and sets a price or a formula from production-cost indicators [S1].
- It also gives quantity, quality, timing, duration, payment, collection and force majeure, plus a revision clause over 12 months [S1].
- Members delivering to their own cooperative are exempt where its statutes set transparent, democratically decided price rules [S1].
- Czech farms sold 98.5bn CZK of crops in 2025, cereals almost 40% of that [S5]; the 2020 census counted 28,909 holdings [S6].
- One buyer's own terms show today's shape: a framework contract signed with no price, and its price list deciding [S7].

Existing non-solutions: No Czech seller writes, signs and files delivery contracts for farm produce; the nearest products handle land leases or the buying firm's back office [S11].

- Farm software here writes land-lease contracts, not contracts for the produce sold [S11].
- One trading back office tracks contracts for the buying firm [S11].
- Czech contract-automation tools are general and carry no farm templates [S11].

One buyer built its own ordering app, which stops before any contract, and the one grain marketplace that closed contracts in its portal was absorbed into a farm-software company [S11]. The rows are under [Market gap](#competition).

Why now: From 19 August 2028 a buyer that takes a delivery without a written contract is breaking directly applicable EU law [S1].

- A buyer was fined 1,040,000 CZK in 2025 for deliveries with no contract [S4].
- Buyers say the duty is hard at small slaughterhouses taking phone offers [S3].
- Today's duty binds only large buyers, so smaller ones owe nothing yet [S2].

The dates behind this:

- The regulation was published on 29 July 2026 and came into force on 18 August 2026 [S1].
- Its contract rules apply from 19 August 2028 [S1].
- Czech law has required a written contract before deliveries since January 2023, but only from large buyers [S2].
- The competition office supervises that law and can fine up to 10,000,000 CZK or 10% of net turnover [S2].
- Member States may exempt small buyers, deliveries worth up to EUR 10,000 and sales paid within 3 working days, and a farmer can still demand a contract [S1].

Who pays: Nobody in Czechia is on record paying for this job, so it sits with the buyers' own staff and their lawyers [S11].

- No Czech seller publishes a price for writing, signing and filing these contracts [S11].
- Buyers carry it in-house, in their own terms and orders [S3,S7].
- The other side of the bill is fines, one already 1,040,000 CZK [S4].

Solved elsewhere: In Spain and France, buyers of farm produce already buy software that writes the contract, signs it and files or fixes its price [S8,S9].

Spain has required food-chain contracts to be filed with the state since 2023, and a seller there offers that filing as a product [S8]. French cooperatives and merchants buy apps and modules that publish purchase prices, generate each member's contract and record the price fixing [S9,S10]. See [Validated abroad](#validated-abroad).

## First moves

1. Build a contract generator for one crop and one collection point, and give it to a mid-size grain buyer for the coming harvest. Take that buyer's own purchase terms, turn them into a contract that names the price rule, the quantity, the quality deductions and the payment period, and let the farmer sign it on a phone before the first load arrives. The buyer keeps its process; you own the document.
2. Call the purchasing managers at fruit and vegetable collection points. They are the part of the chain the competition office found buying with no prior contract at all, as [The opportunity](#opportunity) shows, so they have the furthest to travel and the least in place. Ask what they send a grower today, and who writes it.
3. Sell the cooperative route as the second product. A cooperative whose statutes set transparent, democratically decided price rules needs no contract with each member, as [Why now](#why-now) explains, so the statute rewrite and the member price rules are a service a lawyer and a developer can sell together.
4. Ask each buyer what the paperwork costs it in staff time over one harvest. Those answers are the price nobody has on record yet; see [Willing to pay](#willing-to-pay).

## Revisions

2026-09-21 · record created — Born from the regulation signal reg-agri-pisemne-smlouvy-2028, read in full from the run's own payload [S1]. Scores on the 2026-09-19 ladders: proof 2, two established sellers abroad in Spain and France and a third French one, none in a neighbouring market, so rung 3 is out [S8,S9,S10]; money 0, no price receipt for this job exists in Czechia, and `price_search` says where to look; urgency 1, the regulation is enacted and binds the buyer, but the contract rules apply on 19 August 2028, about 23 months after this date, so the deadline fails the 18-month test [S1]; demand 2, the competition office's inquiry counts the practice across 488 buyers and 19 sectors and its fines recur [S3,S4]; gap 2, no Czech seller found, with a positive control that surfaced five small Czech agri vendors by name [S11]. No `draft_law:` badge: the regulation is published and directly applicable, which the badge rules exclude. No `process:` figure: the duty is new, and while the grain intake flow is described by the inquiry [S3], the work this problem is about — writing and signing a contract before each delivery — is not a workflow Czech buyers perform today, so drawing one would be inventing it. Our readings, flagged: that harvest intake leaves little room for paperwork is the buyers' own objection as the office records it, not our claim [S3]; the Asape founding year is our arithmetic from its "20 ans" claim [S10]; the 2020 census count is lower than the farm register's count of subjects because of the census threshold, as its own source says [S6]; one buyer's published terms show what one buyer does, not the whole trade [S7]. The headline's "many" rests on the counted sectors in [S3], not on a count of all buyers.
