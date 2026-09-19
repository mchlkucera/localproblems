---
id: p-0035
region: cz
title: 'Czech hospitals are overpaying for medicine'
solution: 'Build a price-comparison service where hospital pharmacies share what they paid.'
brief: 'Each hospital buys medicine on its own [S1]. A state audit found one paying over 3 times what another paid for the same antibiotic [S7].'
good_for: 'Someone who''d like to work with hospitals and price data.'
price_search: 'Registr smluv full-text for "eCENTRE" with "léčiv" or "elektronická aukce" —
  Městská nemocnice Ostrava''s coordinated-purchasing contract is what a hospital already pays
  for pooled buying — and for "administrace dynamického nákupního systému" for what a hospital
  pays an outside administrator per purchasing system; otherwise ask the head pharmacist or
  procurement head of Fakultní nemocnice Olomouc what one medicine call costs in staff hours;
  the MS2021+ index under "léčiv" returns only drug research.'
category: health
geo: CZ-national
score: 9
scores:
  proof: 3
  money: 1
  urgency: 3
  demand: 2
  gap: 0
status: watching
entry:
  level: very-hard
  buyer: public
  permission: none
  incumbents: direct
  integration: national-system
  money: outside-money
  why: 'Easier: no licence is needed, and hospitals publish their medicine notices openly. Harder: every buyer is a public hospital or region buying under procurement law, a Czech firm has pooled that buying since 2006 and sells it to hospitals, and the first fee is over a year out, so money goes in before any comes back.'
comps:
- name: Vamstar
  url: https://vamstar.io/
  geo: GB
  since: 2019
  traction: 'USD 9.5m Series A closed June 2022, led by Alpha Intelligence Capital and Dutch
    Founders Fund with btov Partners and Antler (BusinessWire, 2022); sourcing platform pairing
    hospital, laboratory, insurer and group-purchasing drug tenders with suppliers'
  signal: gb-vamstar
- name: Vivecti Group (Prospitalia, Sana Einkauf)
  url: https://www.prospitalia.de/
  geo: DE
  since: 1993
  traction: 'More than 6,000 European healthcare providers and over EUR 7bn of annual purchasing
    volume after the September 2025 combination with Sana Einkauf (company release, 2025);
    Prospitalia alone served more than 1,300 clinics and clinic pharmacies'
  signal: de-vivecti-prospitalia
- name: Trulla (SpendMend)
  url: https://spendmend.com/
  geo: US
  since: 2018
  traction: 'Over 300 pharmacy sites served in one year (company release, 2022); customers including
    Froedtert Health, which adopted it in June 2024; acquired by SpendMend in August 2022'
  signal: us-trulla
locals:
- name: eCENTRE
  url: https://ecentre.cz/
  ico: '27149862'
  since: 2006
  competes: direct
  maturity: established
  evidence: It sells coordinated purchasing run through electronic auctions, pooling the demand
    of many public buyers into one negotiated contract, and it sells it to hospitals — with hospital
    customers including Ostrava's city hospital, which reports 21 percent savings on suture material,
    34 percent on anaesthesia and oxygen-therapy supplies and 25 percent on infusion solutions
    [S18]. eCENTRE, a.s. was incorporated on 12 May 2004 and its pooled purchasing dates to 2006.
- name: PROEBIZ
  ico: '64616398'
  since: 1996
  competes: adjacent
  maturity: established
  evidence: It sells JOSEPHINE and TENDERBOX, the e-procurement platforms used by Czech health
    buyers to publish and run their medicine purchasing procedures [S18]. That is the software
    the call is filed on, not the pooling of demand across hospitals and not a comparison of
    what each one paid. PROEBIZ s.r.o., of Moravská Ostrava, has traded since 19 March 1996.
- name: QCM (E-ZAK)
  ico: '26262525'
  since: 2001
  competes: adjacent
  maturity: established
  evidence: It sells E-ZAK, the e-procurement system Fakultní nemocnice Brno runs its medicine
    purchasing systems on [S18] — again the filing surface, not the buying and not the price
    comparison. QCM, s.r.o., of Brno, has traded since 9 October 2001, and the state contracts
    register pairs it with 2 distinct public buyers, one of them Fakultní nemocnice Olomouc [S18].
- name: Tender systems (Tender arena, eGordion)
  url: https://www.tendersystems.cz/
  ico: '29145121'
  since: 2012
  competes: adjacent
  maturity: established
  evidence: It sells Tender arena and eGordion, the two contracting-authority platforms used
    by Všeobecná fakultní nemocnice v Praze, the largest buyer here, to publish its purchasing
    profile [S18]. Both host procedures; neither pools demand or compares prices between hospitals.
    Tender systems s.r.o., of Prague, has traded since 19 December 2012.
sources:
- type: tender
  name: "TED — Všeobecná fakultní nemocnice v Praze, 38 medicine purchasing systems"
  gist: "the 38 Prague notices"
  why: "Prague's general university hospital published 38 separate medicine notices in nine weeks under dynamic purchasing systems split by drug class — antithrombotics, immunosuppressants, cancer drugs."
  url: https://ted.europa.eu/en/notice/-/detail/461139-2026
  note: 'ted-461139-2026 represents 38 drug-object dynamic-purchasing notices from Všeobecná
    fakultní nemocnice v Praze [00064165] inside a cluster of 106 such notices from 15 distinct
    Czech public buyers between 2026-07-06 and 2026-09-02, all committed in the tenders ledger
    for 2026-09-02 and verified by id on 2026-09-03; 90 of the 106 rows also name the winning
    supplier alongside the buyer. THE CLUSTER TOTAL IS NOT SPEND AND MUST
    NEVER BE SUMMED: nine of the Prague rows repeat one identical 2,000,000,000 CZK value
    (ted-463504-2026, ted-502862-2026, ted-503241-2026, ted-550358-2026, ted-562802-2026,
    ted-563168-2026, ted-581118-2026, ted-592160-2026, ted-592492-2026), which is the system
    ceiling advertised on the notice rather than a call-off value. The scale receipt this
    source carries is the COUNT of notices and the NAMES of the buyers, not a sum. Money is
    held at 1 for the reason stated in the who-pays paragraph: every crown of this buys
    medicines, and no budget line for procurement tooling appears anywhere in the evidence.'
  date: '2026-07-06'
  signal: ted-461139-2026
- type: tender
  name: "TED — Fakultní nemocnice Olomouc, 24 medicine purchasing systems"
  gist: "the 24 Olomouc notices"
  why: "Olomouc's university hospital ran its own parallel dynamic purchasing system for medicine supply, one of 24 such notices from that buyer alone in the same nine weeks."
  url: https://ted.europa.eu/en/notice/-/detail/472200-2026
  note: 'ted-472200-2026: Fakultní nemocnice Olomouc [00098892], supplier BAXTER CZECH,
    dynamic purchasing system for medicinal product supply, Jul 2026. Represents 24 notices
    from this buyer in the 106-notice cluster. Same ceiling caution as [S1]: cite the count
    and the named buyer, never a sum.'
  date: '2026-07-09'
  signal: ted-472200-2026
- type: tender
  name: "TED — Fakultní nemocnice Bulovka, 16 medicine purchasing systems"
  gist: "the 16 Bulovka notices"
  why: "A third Prague teaching hospital running its own separate system for medicines, nutrition and selected devices — 16 notices from this buyer in nine weeks."
  url: https://ted.europa.eu/en/notice/-/detail/489593-2026
  note: 'ted-489593-2026: Fakultní nemocnice Bulovka [00064211], supplier PROMEDICA PRAHA
    GROUP, Jul 2026. Represents 16 notices from this buyer in the 106-notice cluster. Same
    ceiling caution as [S1].'
  date: '2026-07-15'
  signal: ted-489593-2026
- type: tender
  name: "TED — Fakultní nemocnice Motol a Homolka, 10 medicine purchasing systems"
  gist: "the 10 Motol-Homolka notices"
  why: "Prague's merged mega-buyer opened a call for a single antifungal molecule under its own dynamic purchasing system — one of 10 notices from this buyer in the same window."
  url: https://ted.europa.eu/en/notice/-/detail/495094-2026
  note: 'ted-495094-2026: Fakultní nemocnice Motol a Homolka [00064203], call No. 274 for
    anidulafungin, supplier ViaPharma, Jul 2026. Represents 10 notices from this buyer in the
    106-notice cluster. The per-molecule call numbering (č. 274) is itself the receipt for how
    many minitenders one hospital pharmacy runs. Same ceiling caution as [S1].'
  date: '2026-07-17'
  signal: ted-495094-2026
- type: regulation
  name: "Zákon 289/2025 Sb. — health insurers may tender centre medicines centrally"
  gist: "the 1 January 2026 power shift"
  why: "The amendment of the public health insurance act that took effect on 1 January 2026 and carries the power for insurers to run central tenders for medicines used in specialised-care centres."
  url: https://e-sbirka.gov.cz/sb/2025/289
  note: 'reg-mzd-289-2025-pojisteni, committed 2026-08-14. THE LEDGER TITLE HIDES THIS
    PROVISION: the record describes cross-border provider contracts, dental reimbursement,
    cashless insurers and benefit funds, and says nothing about medicine procurement, so a
    keyword pass over the regulation ledger cannot find it. The 2026-09-03 sweep drafted a
    second row for the drug-procurement provision and withdrew it before staging, because the
    identity-key index matched it to this same act at this same URL; the enrichment therefore
    lives here. WHAT IS VERIFIED: bill 849 contained the provision; bill 849 became 289/2025
    Sb., published 12 August 2025, in force 1 January 2026; section 40d ("Centrální zadávání
    veřejných zakázek na nákup léčivých přípravků pro poskytovatele") now exists in the
    consolidated text of zákon 48/1997 Sb. WHAT IS NOT: the sweep never read the amending
    article that inserts section 40d — e-sbirka, zakonyprolidi (HTTP 403), fulsoft, mesec and
    podnikatel all failed to return the paragraph body — so the 289/2025-to-40d link is
    inference from three verified facts and a future pass owes that read. Deadline sub-score
    2: an instrument already in force, not a date in the future.'
  date: '2026-01-01'
  signal: reg-mzd-289-2025-pojisteni
- type: regulation
  name: "Cenový výměr 1/2026/OLZP — the split trade margin drops off hospital medicines"
  gist: "the same-day margin change"
  why: "The health ministry price ruling in force from 1 January 2026 stops applying the split trade margin to purely hospital medicinal products — the economics of the goods these notices buy changed on the same day."
  url: https://mzd.gov.cz/cenovy-vymer-ministerstva-zdravotnictvi-c-1-2026-olzp/
  note: 'reg-cz-cenovy-vymer-1-2026-olzp: issued 24 October 2025, published in ministry
    bulletin 18/2025 on 31 October 2025, in force 1 January 2026. Companion rulings
    2/2026/OLZP (ATC groups with special availability price rules) and 3/2026/OLZP (devices
    and in vitro diagnostics) share the date. The ministry page carries only a header and a
    link to the ruling PDF, so no verbatim quote was taken from the primary; the hospital-margin
    change is reported by havelpartners.blog (6 January 2026) and epravo.cz article 120661,
    and a future pass owes a read of the PDF. Two dated instruments landing on 1 January 2026
    are what carries the deadline sub-score, together with [S5].'
  date: '2026-01-01'
  signal: reg-cz-cenovy-vymer-1-2026-olzp
- type: complaint
  name: "NKÚ audit 17/19 — the same antibiotic at 956 and at 3,300 CZK"
  gist: "the state audit price spread"
  why: "The supreme audit office found three university hospitals buying medicines very often by direct order without any tender, and paying sharply different prices to the same supplier for identical products."
  url: https://www.nku.cz/cz/pro-media/tiskove-zpravy/zadavaci-rizeni-na-nakupy-leku--u-fakultnich-nemocnic-spise-vyjimka--leky-porizovaly-casto-naprimo-a-bez-souteze-id9842/
  note: 'civic-nku-1719-nakup-leciv: audit action 17/19, published 3 September 2018, covering
    Fakultní nemocnice Brno, Fakultní nemocnice v Motole and the central military hospital over
    2014-2016. MEROPENEM KABI at 956 CZK a pack against 3,300 CZK (3.45x); PIPERACILLIN/TAZOBACTAM
    KABI at 385 CZK against 2,103 CZK (5.46x); around 1bn CZK of supplier bonuses across the
    three. AGE STATED HONESTLY: eight years old, so it carries no urgency and the body dates it.
    Its value is that the price dispersion is the state auditor''s own finding, not a vendor
    claim, and [S9] shows the same office saying six years later that the pattern persists.'
  date: '2018-09-03'
  signal: civic-nku-1719-nakup-leciv
- type: complaint
  name: "VZP — 22.5bn CZK of centre medicines, over a 3.5bn CZK bonus grey zone"
  gist: "the payer's own numbers"
  why: "The national health insurer's deputy director put its centre-medicine spend at 22.5bn CZK in one year and the grey zone of retrospective supplier bonuses at an estimated 3.5bn CZK, and argued for insurers tendering these medicines jointly."
  url: https://www.vzp.cz/o-nas/aktuality/bodnar-soutezeni-centrovych-leku-pojistovnami-prinese-stamilionove-uspory-i-transparentnost
  note: 'civic-vzp-centrove-leky-bonusy, 10 March 2025. The payer''s own account, and the
    demand-side twin of the section 40d power in [S5] — the article argues for exactly the
    legal instrument that entered force on 1 January 2026. 22.5bn CZK is VZP''s spend on
    centre drugs in the previous year; the 3.5bn CZK bonus estimate is separate and is NOT
    added to it. THIS IS DRUG SPEND, NOT SPEND ON A PROCUREMENT PRODUCT: it sizes the pot the
    buying moves, and money stays at 1 because of that distinction.'
  date: '2025-03-10'
  signal: civic-vzp-centrove-leky-bonusy
- type: complaint
  name: "Transparency International — medicines named the worst procurement area"
  gist: "the 2024 confirmation"
  why: "At a round table on corruption risk in hospital procurement, the supreme audit office said the largest volume of failings it finds sits in medicines and medicine buying, done often without proper competition."
  url: https://www.transparency.cz/jak-predchazet-korupcnim-rizikum-ve-zdravotnictvi-u-verejnych-zakazek-a-jmenovani-vedeni-nemocnic/
  note: 'ngo-ti-zdravotnictvi-zakazky-2024, 10 October 2024. NKÚ''s Miroslava Roubalová on the
    record: failings concentrate in medicines, bought "bez řádné soutěže, tedy napřímou". A
    second speaker put the tendered share of pharmaceutical purchases at around 60 percent.
    Recorded alongside [S7] rather than instead of it: six years apart, same finding, which is
    what makes the demand recurring rather than a single audit.'
  date: '2024-10-10'
  signal: ngo-ti-zdravotnictvi-zakazky-2024
- type: complaint
  name: "ÚOHS — a manual for hospitals because the problem keeps arriving"
  gist: "the regulator's guidance"
  why: "The competition authority published guidance on buying medicines because it meets the problem ever more often, and acknowledged that delivery clocks measured in hours have to be reconciled with a procurement procedure."
  url: https://uohs.gov.cz/cs/informacni-centrum/tiskove-zpravy/verejne-zakazky/3293-urad-pripravil-metodicke-doporuceni-pro-zdravotnicka-zarizeni-jak-postupovat-pri-nakupu-leciv.html
  note: 'civic-uohs-metodika-nakup-leciv, 6 April 2022. This is the MECHANISM behind the notice
    cluster in [S1]: hours-long delivery clocks against a full procurement procedure is exactly
    why Czech hospitals answer with dynamic purchasing systems split by therapeutic group. The
    regulator''s own phrase is "stále častěji". Independent 2026 corroboration that the answer
    is still dynamic purchasing systems and framework agreements: arws.cz, 9 February 2026,
    advisory rather than complaint and therefore not a source of its own.'
  date: '2022-04-06'
  signal: civic-uohs-metodika-nakup-leciv
- type: complaint
  name: "Ministry drug price database — the state had to build one to see the spread"
  gist: "the closed price database"
  why: "The health ministry and the innovative-pharma association built a database of real unit prices delivered to directly-managed hospitals, live since 2019, because the founder could not otherwise compare what its own hospitals paid; its unit prices may not be passed on."
  url: https://mzd.gov.cz/tiskove-centrum-mz/ministerstvo-bude-od-noveho-roku-znat-ceny-za-ktere-nemocnice-nakupuji-leky/
  note: 'civic-mz-aifp-cenova-databaze, 23 November 2018; pilot from 1 January 2019, full
    operation from 1 February 2019. Reports show each product''s weighted average price and its
    highest and lowest real unit price. It stays a demand signal rather than a solution for
    three reasons on the page or in its terms: it covers only the ministry''s own hospitals, it
    is hosted and financed by the industry association, and its unit prices may not be published
    or handed to parties without access. This is the Czech half-answer to what [S16] sells in
    the open, and it is the constraint the build note names.'
  date: '2018-11-23'
  signal: civic-mz-aifp-cenova-databaze
- type: complaint
  name: "Health ministry joint purchasing — the second attempt in eight years"
  gist: "the July 2026 memorandum"
  why: "On 29 July 2026 the ministry signed a memorandum with six university hospitals to start analysing what could be bought together — eight years after running a joint-purchasing pilot on selected medicines, and this time led by facility management."
  url: https://mzd.gov.cz/tiskove-centrum-mz/ministerstvo-zdravotnictvi-zahajuje-projekt-spolecnych-nakupu-a-provoznich-sluzeb-ve-fakultnich-nemocnicich/
  note: 'civic-mz-spolecne-nakupy-fn-2026, 29 July 2026. Signatories: Motol, Královské Vinohrady,
    Bulovka, Všeobecná fakultní nemocnice v Praze, Brno and Saint Anne''s in Brno. WHY THIS IS
    DEMAND AND NOT A SOLUTION: the June 2018 pilot already covered selected medicines with ten
    coordinated tenders planned and savings "ve výši desítek miliónů korun" claimed; eight years
    later the same ministry is signing a memorandum to begin analysing which areas to pool, and
    the 2026 scope leads with facility management rather than medicines. NO DATED DEADLINE is
    published, so this carries no urgency of its own — it is the newest source on the record and
    is what the freshness sub-score rests on.'
  date: '2026-07-29'
  signal: civic-mz-spolecne-nakupy-fn-2026
- type: arbitrage
  name: "Amgros — Denmark buys its hospital medicines through one body"
  gist: "the national buyer"
  why: "Almost all medicines used in Danish public hospitals are procured by one organisation owned by the five regions that also own the hospitals; it reports nearly 10 billion Danish crowns of savings in 2024."
  url: https://amgros.dk/en/about-amgros/
  note: 'dk-amgros: the structural opposite of the Czech pattern — Denmark runs one national
    tender where 15 Czech buyers run their own. NOT LISTED IN comps[] AND THE REASON IS THE
    RULE, NOT AN OVERSIGHT: the signal record carries no founding year, and a comp without a
    verifiable founding year cannot be listed, so it is cited here instead. The DKK 10bn figure is
    savings obtained, not turnover, not contract value and not capital raised; Amgros publishes
    no funding round because it is region-owned. Denmark is Nordic and therefore CEE-adjacent,
    but proof rung 3 does not depend on it — Germany carries that limb through [S15].'
  date: '2026-09-03'
  signal: dk-amgros
- type: arbitrage
  name: "Vamstar — the matching layer above the tender"
  gist: "the $9.5M sourcing platform"
  why: "A London platform that pairs hospital, laboratory, insurer and group-purchasing drug tenders with suppliers, funded at Series A — the layer above the individual notice."
  url: https://vamstar.io/
  note: 'gb-vamstar: founded London 2019, USD 9.5m Series A announced 22 June 2022 led by Alpha
    Intelligence Capital and Dutch Founders Fund, existing investors btov Partners and Antler;
    no later round found in the sweep. Passes the established test on the Series A limb with
    seven years of selling. Domain vamstar.io verified live on 2026-09-03; the ledger URL is
    the funding release.'
  date: '2022-06-22'
  signal: gb-vamstar
- type: arbitrage
  name: "Vivecti Group — a EUR 7bn German hospital buying block"
  gist: "the German buying group"
  why: "Prospitalia, trading since 1993, combined with Sana Einkauf in September 2025 to cover more than 6,000 European healthcare providers and over EUR 7bn of annual purchasing volume, clinic pharmacies explicitly included."
  url: https://www.prospitalia.de/vivecti-group-und-sana-einkauf-buendeln-ihre-kraefte/
  note: 'de-vivecti-prospitalia, 19 September 2025. The private, commercially-run answer to the
    same fragmentation: hospitals stay independent buyers and a vendor aggregates the volume and
    the negotiation. Prospitalia''s pre-merger figures: 1,300+ clinics and clinic pharmacies,
    purchasing volume above EUR 3bn, price negotiation across more than a million articles, plus
    the Prospitalia Cockpit software. The EUR 7bn is BUYING VOLUME RUN THROUGH THE GROUP, not
    revenue and not capital raised. Germany is the CEE-adjacent market that carries proof rung 3;
    with Britain, the Netherlands and the United States that is four markets with an established
    player each. P.E.G., AGKAMED, EKK plus and EK UNICO are real German peers deliberately not
    given rows of their own, because each would restate this one.'
  date: '2025-09-19'
  signal: de-vivecti-prospitalia
- type: arbitrage
  name: "Intrakoop — the Dutch cooperative that benchmarks what members paid"
  gist: "the medicines benchmark"
  why: "A care purchasing cooperative founded in 1959 whose member pharmacies report volumes and prices so members can see whether they are overpaying — the tool extended from care homes to hospitals."
  url: https://cooperatie.nl/leden/intrakoop/
  note: 'nl-intrakoop: around 550 Dutch care organisations across more than 7,000 locations. THE
    BENCHMARK, NOT THE BUYING, IS THE TRANSFERABLE PART, which is why it is the shape the fix
    names. COVERAGE GAP CARRIED FORWARD: intrakoop.nl could not be fetched by the sweep (TLS chain
    error) on two attempts and was still unreachable on 2026-09-03, so both the ledger record and
    this entry are anchored on cooperatie.nl, which was fetched and quoted; a future pass owes a
    direct read of intrakoop.nl/diensten/medisch-en-farmacie. The Netherlands is NOT CEE-adjacent
    on the SCORING list and is not what carries proof rung 3.'
  date: '2026-09-03'
  signal: nl-intrakoop
- type: arbitrage
  name: "Trulla — buyer-side pharmacy procurement software"
  gist: "the pharmacy-side product"
  why: "Cloud software letting a hospital system run pharmacy ordering, pricing, product standardisation and supplier selection across all its sites, founded 2018 and acquired by a healthcare spend firm four years later."
  url: https://spendmend.com/
  note: 'us-trulla: founded 2018 in Draper, Utah by a former Intermountain Healthcare pharmacy
    sourcing executive; "In the last year, we''ve provided compliance and optimization services
    for over 300 pharmacies" (company release, 16 August 2022); Froedtert Health adopted it in
    June 2024; acquired by SpendMend August 2022, price not disclosed. The buyer-side workflow
    product a Czech hospital pharmacy running parallel systems per therapeutic group does not
    have. The comps URL is the acquirer''s site, verified live 2026-09-03; the ledger URL is the
    acquisition release.'
  date: '2022-08-16'
  signal: us-trulla
- type: gap-check
  name: "eCENTRE and the Czech purchasing platforms"
  gist: "the occupied Czech field"
  why: "A Czech-language sweep of who already sells hospital purchasing here: eCENTRE pools the buying and sells it to hospitals; PROEBIZ, QCM and Tender systems sell the platforms the procedures run on."
  url: https://ecentre.cz/
  note: 'Sweep 2026-09-03, and the headline is that there is NO absence. AGGREGATION LAYER,
    OCCUPIED AND DIRECT: eCENTRE (IČO 27149862, already on file as an established player on
    p-0031) sells coordinated purchasing with electronic auctions to Czech hospitals — Ostrava
    city hospital reports 21 percent savings on suture material, 34 percent on anaesthesia and
    oxygen-therapy supplies and 25 percent on infusion solutions. Nemocnice Pardubického kraje
    runs a "Centrální nákup" function for its region and MZ ČR runs joint purchasing across its
    own hospitals [S12]; both are buyers coordinating for themselves rather than vendors, so
    they are named here and not in locals[]. TOOL LAYER, OCCUPIED AND ADJACENT: PROEBIZ sells
    JOSEPHINE and TENDERBOX and publishes live dynamic-purchasing procedures for Czech health
    buyers; Fakultní nemocnice Brno runs its systems on E-ZAK (ezak.fnbrno.cz, the QCM product);
    Všeobecná fakultní nemocnice v Praze publishes its contracting-authority profile on Tender
    arena and eGordion. Company identities and founding dates read from the state business
    register on 2026-09-03: PROEBIZ s.r.o. 64616398, 19 March 1996, Moravská Ostrava; QCM, s.r.o.
    26262525, 9 October 2001, Brno; Tender systems s.r.o. 29145121, 19 December 2012, Praha;
    eCENTRE, a.s. 27149862, 12 May 2004, Ostrava. egordion.cz redirects to
    egordion.tendersystems.cz and tendersystems.cz names Tender arena, which is what pairs both
    products with that company. The contracts-register lookup gives QCM two distinct public
    payers, Fakultní nemocnice Olomouc and Centrum investic, rozvoje a inovací; it gives none
    for the other three, so their maturity rests on named customers instead. PRICE-INTELLIGENCE
    LAYER, THE THINNEST: no commercial Czech cross-hospital medicine price benchmark was found,
    and NO ABSENCE IS ASSERTED from that — not finding one is not evidence that none exists. The
    ministry and industry database [S11] covers only directly-managed hospitals and bars its unit
    prices from wider release, and ÚZIS''s reference-hospital benchmark at drg.uzis.cz compares
    performance, not purchase prices. POSITIVE CONTROL PASSED: the same method (Czech-language
    search plus a read of the vendor''s own site) surfaced Wultra (Praha, IČO 03643174, PowerAuth
    and the Talisman FIDO2 device) and SOFTLINK (Kralupy nad Vltavou, founded 1993, more than
    100,000 metered devices, acquired by Quantcom 30 June 2022), two of the register''s standing
    controls. NOT CHECKED AND THEREFORE NOT CLAIMED: ares by NACE, cz-saas-directories,
    startupjobs, app-stores, eshop-addon-marketplaces. NO OPEN FUNDING FOR THIS: the subsidy
    sweep returned nothing that funds hospital procurement digitisation or joint purchasing —
    IROP call 79 is open to 2 December 2026 with roughly 1.15bn CZK but funds interoperable
    clinical documentation, not purchasing; NPO call 22 closed on 14 November 2024; OP TAK
    "Digitální podnik" admits only enterprises, so public hospitals cannot apply; the MZ ČR
    quality-and-efficiency programme has not been announced since 2025; EU4Health 2026 procurement
    calls are medical-countermeasure work.'
  date: '2026-09-03'
  queries:
    - "dynamický nákupní systém léčiv"
    - "sdružený nákup léků nemocnice"
    - "centrální nákup léčiv nemocnice"
    - "sdružené nákupy nemocnic"
    - "software pro nákup léčiv nemocnice"
    - "elektronický nástroj zadávání veřejných zakázek nemocnice"
    - "e-aukce léčiva nemocnice"
    - "benchmarking nákupních cen léčiv nemocnice"
    - "srovnání cen léků mezi nemocnicemi"
    - "databáze jednotkových cen léčiv nemocnice"
    - "nemocniční lékárna objednávání léčiv software"
    - "profil zadavatele Všeobecná fakultní nemocnice dynamický nákupní systém"
    - "hospital drug tender aggregation Czech"
    - "group purchasing organisation hospitals Czech Republic"
  checked: [google-cz, own-funded-ledger, cz-contract-parties]
  expires: '2026-12-02'
created: '2026-09-03'
updated: '2026-09-03'
---

Czech hospitals each buy their own medicines, and a state audit found some paying over 3 times what others paid [S1,S7].

- 15 public buyers published 106 medicine notices in nine weeks of 2026 [S1].
- In 2014–2016 an antibiotic cost one hospital 956 CZK a pack, another 3,300 [S7].
- In 2024 the state auditor said it finds most failings in medicine buying [S9].

The notices came out between 6 July and 2 September 2026 [S1]. Each runs under a dynamic purchasing system: a standing list of approved suppliers that the hospital asks again for every order [S1]. Four hospitals ran most of them:

- Všeobecná fakultní nemocnice v Praze, Prague's general university hospital, ran 38 [S1]. It keeps separate systems for drug classes such as anti-clotting drugs, immune-suppressing drugs and cancer drugs [S1].
- Fakultní nemocnice Olomouc, the university hospital in Olomouc, ran 24 [S2].
- Fakultní nemocnice Bulovka, a third Prague teaching hospital, ran 16, for medicines, nutrition and selected medical devices [S3].
- Motol and Homolka, two merged Prague hospitals that buy as one, ran 10 [S4]. One of them was call No. 274, for a single antifungal drug [S4].
- 90 of the 106 notices also name the supplier that won [S1].

The state keeps finding what this costs:

- The supreme audit office, the state's auditor, checked three university hospitals over 2014–2016 and published its findings in 2018 [S7]. It found them buying medicines very often by direct order, without a tender [S7].
- The antibiotic above was meropenem [S7]. For another antibiotic, piperacillin with tazobactam, one hospital paid 385 CZK a pack and another 2,103 CZK, both from the same supplier [S7].
- Bonuses from suppliers to the three hospitals, for medicines and medical supplies, came to about 1bn CZK over those years [S7].
- At a 2024 round table on corruption risk in hospital buying, reported by Transparency International, the audit office said medicines are often bought directly, without proper competition [S9]. Another speaker put the share of drug purchases that go through a tender at about 60 percent [S9].
- In 2022 the competition authority, which oversees public buying, wrote hospitals a guide to buying medicines, because it meets the problem ever more often [S10].

Existing non-solutions: The field is not empty: a Czech firm has pooled public buying since 2006 and sells it to hospitals [S18].

It pools the demand of many public buyers into one negotiated contract, run as electronic auctions [S18]. No Czech firm selling a comparison of what each hospital paid for its medicines has been found, and nothing here proves that none exists [S18]. The rest of the field sells pieces:

- Three established Czech firms sell the platforms the medicine calls run on [S18]. Each hosts the calls, and none pools the buying or compares prices [S18].
- The health ministry and the association of innovative drug makers have compared real unit prices since 2019, but only for the ministry's own hospitals [S11]. The association hosts and pays for the database, and its unit prices may not be passed on [S11].
- The ministry built that database because it could not otherwise compare what its own hospitals paid [S11]. Each report shows a product's average price and its highest and lowest real price [S11].
- Some buyers pool for themselves: the Pardubice region's hospital company runs central purchasing for the region [S18]. The health ministry's joint buying for its own hospitals is under [Why now](#why-now).
- The state health-statistics institute compares how hospitals perform, not what they pay [S18].

Why now: Since January 2026 insurers may buy drugs for specialist centres in one tender, and a hospital buying a tendered drug alone is not reimbursed [S5].

- The national health insurer paid 22.5bn CZK for specialist-centre drugs in 2024 [S8].
- It puts the grey-zone bonuses suppliers pay hospitals at about 3.5bn CZK [S8].
- Some medicines are needed within hours, yet the law requires a purchasing procedure [S10].

Two rules changed on 1 January 2026, and in July the health ministry agreed to try joint buying again:

- On 1 January 2026 an amendment to the public health insurance law, Act No. 289/2025, let health insurers tender medicines centrally for hospitals the state has named centres of highly specialised care [S5].
- The rule covers a drug that is the only registered product with its active ingredient, and that is billed with a treatment or used only on hospital wards [S5].
- The insurer then pays the hospital the price its tender reached, and does not pay a hospital that bought the drug outside that tender [S5].
- The national insurer argued for this power in March 2025, saying each hospital now tenders these drugs differently and to a different standard [S8].
- On 1 January 2026 a health ministry price ruling also stopped applying the split trade margin, a mark-up the ministry regulates, to medicines used only in hospitals [S6].
- On 29 July 2026 the health ministry signed a memorandum with six university hospitals to start analysing what they could buy together [S12]. They are Motol, Královské Vinohrady, Bulovka and the general university hospital in Prague, and the university hospital and St Anne's in Brno [S12].
- It is the ministry's second try: a 2018 pilot already covered selected medicines, with ten coordinated tenders planned and savings of tens of millions of crowns claimed [S12]. This time facility management leads, not medicines, and no deadline has been published [S12].

Who pays: Hospitals already pay a Czech firm to pool their buying, but what anyone would pay to compare prices is not known [S18].

- Ostrava's city hospital buys supplies through that firm and reports 21–34 percent savings [S18].
- Olomouc's university hospital has a paid contract with a purchasing-software maker [S18].
- Every crown in the hospitals' medicine notices buys medicines, not purchasing tools [S1].

The bigger numbers around this problem buy the drugs themselves:

- Nine of the Prague general university hospital's notices repeat one 2bn CZK figure, which is the ceiling of its purchasing system, not money spent [S1].
- The national insurer's spending under [Why now](#why-now) pays for the drugs, not for how they are bought [S8].

What one medicine call costs a hospital in pharmacist and purchasing-staff hours is not known.

No open grant pays for this [S18]. The state's eHealth grant call, open to 2 December 2026, pays for clinical records that other systems can read, not for purchasing [S18]. A national recovery-plan call closed on 14 November 2024, and the business-digitisation programme admits only companies, so public hospitals cannot apply [S18].

Solved elsewhere: Companies in Germany, Britain and the US already sell pieces of the job: pooled medicine buying for hospitals, drug-tender matching and pharmacy purchasing software [S14,S15,S17].

In Germany a buying group trading since 1993 buys for more than 6,000 European healthcare providers, clinic pharmacies among them, and runs over €7bn of purchasing a year [S15]. It reached that size by combining with another hospital buyer in September 2025; before that it served more than 1,300 clinics and clinic pharmacies [S15].

A London platform funded at Series A matches drug tenders from hospitals, laboratories, insurers and buying groups with suppliers [S14]. A US product lets a hospital system run pharmacy ordering, pricing and supplier choice across all its sites, and a healthcare spending firm bought it four years after it started [S17].

Two more answers are not on the map, a public buyer and a cooperative:

- Denmark buys almost all medicines for its public hospitals through one body, Amgros, owned by the five regions that also own the hospitals [S13]. It reports nearly 10 billion Danish crowns of savings in 2024 [S13].
- Intrakoop, a Dutch care-purchasing cooperative founded in 1959, sells the price comparison itself rather than the buying: member pharmacies report volumes and prices, and each member sees whether it is overpaying [S16]. About 550 Dutch care organisations with more than 7,000 locations use its services [S16].

## First moves

1. Build a first map of who buys which medicines from whom, using the hospitals' own public purchasing notices, before asking any hospital for anything. Most notices name the supplier that won as well as the hospital, so the map starts from what is already public; see [The opportunity](#opportunity). Print a system's ceiling as a ceiling, never as money spent, as [Willing to pay](#willing-to-pay) explains. The map is what you show the pharmacists in the next move.
2. Call the head pharmacists of Olomouc's university hospital and Prague's Bulovka hospital, and ask what one medicine call costs them in staff hours. Between them they ran dozens of medicine calls in one summer; see [The opportunity](#opportunity). Nobody has published what a call costs in pharmacist and purchasing hours, and that cost is the price your product has to beat. Show them the map from the first move and ask which comparison they would use.
3. Sell the comparison of what each hospital paid, not the pooled buying, because a Czech firm already sells pooled buying to hospitals. It has done so for years, and the purchasing platforms host the calls without pooling them or comparing prices; see [Competition](#competition). A Dutch cooperative sells exactly this comparison: pharmacies' prices go in, and each member sees whether it overpays; see [Validated abroad](#validated-abroad). The Czech version of that data exists but is closed to all but the ministry's own hospitals, also under [Competition](#competition). Public notices are the way in that nobody has to grant you.
4. Take the comparison to the health insurers, who may now buy drugs for specialist centres in one tender on the hospitals' behalf. The national insurer argued for that power with its own numbers, and the law now gives it; see [Why now](#why-now). An insurer planning such a tender will want to know what each hospital pays today, and a hospital that keeps buying such a drug alone is not reimbursed, so both sides need the same picture. The health ministry's new joint-buying project with the big university hospitals is a second buyer to show it to, under the same section.
5. Plan to fund the first year yourself or with investors, because no open grant pays for hospital purchasing tools. The open state eHealth call pays for clinical records, not purchasing, and no other call was found that funds it; see [Willing to pay](#willing-to-pay). Public buyers also buy slowly, so expect the first fee to come late; see [Execution difficulty](#execution-difficulty).

## Revisions

2026-09-03 · record created — Minted from a topic sweep on Czech hospital drug purchasing. The scale leg was already committed: 106 drug-object notices from 15 named public buyers in nine weeks [S1]. The window is dated twice on 1 January 2026 [S5,S6]. Demand is the state's own — audit office, competition authority, ministry, national insurer [S7,S9,S10]. eCENTRE sells this to hospitals and passes the established test, so gap is 0 and status is watching [S18].

2026-09-16 · headline copy — The headline was rewritten for a general builder as three lines under the title: a `brief:` on what is happening and why it matters now, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "Czech hospitals are overpaying for medicine"; brief: "Each hospital buys medicine on its own [S1]. A state audit found one paying over 3 times what another paid for the same antibiotic [S7]."; solution: "Build a price-comparison service where hospital pharmacies share what they paid, as a Dutch buyers' cooperative already does."; good_for: "Someone who'd like to work with hospitals and price data.". Previous title, verbatim: "Czech hospitals each buy their medicines alone, and the state keeps finding they overpay". Previous solution, verbatim: "A price comparison for hospital medicines, assembled from the hospitals' own published purchasing notices, so a hospital pharmacy can see what its peers paid for the same molecule before it opens the next order.". There was no previous brief or good_for. Corrected against the evidence before it was written, from the owner-reviewed draft, then cut to the owner's length limits. "Can't see what the others pay" was cut: the only price comparison on file, the ministry and industry database, covers only the ministry's own hospitals and bars its unit prices from wider release [S11], and no source shows that no hospital can see what others pay; the gap check on file asserts no absence [S18]. "One paid 3x more than another" became "over 3 times what another paid", attributed to the state audit it comes from: 956 against 3,300 CZK a pack of meropenem is 3.45 times, over 2014 to 2016 [S7]. "As companies already do abroad" became "as a Dutch buyers' cooperative already does": the share-what-you-paid comparison is Intrakoop's, a members' cooperative on the sources ledger and not in comps[] [S16]; the three comps sell buying, tender matching and pharmacy ordering, not that comparison. The good_for line is the owner's. No score, status, source, note, marker or body sentence changed. Same date, abroad count (owner: fill "do abroad" with "X companies do in Y countries"): solution "…share what they paid, as a Dutch buyers' cooperative already does." became "…share what they paid." The clause is removed, not counted, because the count is taken from comps[] and none of the three comps sells this comparison: Vamstar (comps[0], GB) matches tenders with suppliers, Vivecti Group (comps[1], DE) buys on its members' behalf, and Trulla (comps[2], US) runs one hospital system's own pharmacy ordering and pricing. Intrakoop, the Dutch cooperative that does sell it, is cited [S16] but is not in comps[]; putting it there would restore the clause as "as 1 company already does in the Netherlands".

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the three sections whose items the page shows carry their three most important ones first, and the rest of each section follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on hospitals buying alone and the audit's price spread, with the notice counts per hospital, the audit, the 2024 round table and the competition authority's guide below its first three items [S1,S2,S3,S4,S7,S9,S10]. Competition opens on the pooled-buying firm and describes it, the three purchasing-platform firms and the German buying group by what they sell; eCENTRE, PROEBIZ (JOSEPHINE), QCM (E-ZAK), Tender systems (Tender arena, eGordion) and Vivecti Group left the body and the moves, and their names, dates and per-group savings stay in their own rows [S15,S18]. Why now opens on what the 1 January 2026 insurance-law change does to a hospital, with the insurer's spend and bonus estimate and the hours-long delivery clock as its three items, and the law dates, the price ruling and the July 2026 memorandum below them [S5,S6,S8,S10,S12]. Willing to pay answers whether anyone pays now and carries the 2bn CZK ceiling caution, the unpublished staff-hours cost and the grant calls that do not fund this [S1,S8,S18]. Validated abroad became one answer sentence and four short paragraphs [S13,S14,S15,S16,S17]. The six moves became five: move 6 (no grant) folded into move 5, with its facts under Willing to pay [S18]; every move lost its markers, figures and company names for links, and the move-only facts now live in the body: the 90 of 106 notices that name the winning supplier under The opportunity [S1], and the insurer's March 2025 argument for central tenders under Why now [S8]. `entry.why` was rewritten as "Easier: … Harder: …" on the same gates the level derives from. Detail added from sources already on file, none of it new evidence: the second antibiotic, piperacillin with tazobactam at 385 against 2,103 CZK from the same supplier, and the ~1bn CZK of supplier bonuses [S7]; the ~60 percent tendered share [S9]; what the ministry's price database shows and why it was built [S11]; the memorandum's six signatories, its facility-management lead, its missing deadline and the 2018 pilot's ten planned tenders [S12]; Bulovka's scope [S3]; Motol and Homolka's call No. 274 [S4]; Intrakoop's roughly 550 organisations [S16]; the Pardubice region's central purchasing, the health-statistics institute's performance benchmark and the closed or ineligible grant calls [S18]; and one-line descriptions of the London tender-matching platform and the US pharmacy-ordering product [S14,S17]. Verified at the primary on 2026-09-18, resolving what S5's note left as inference: Act No. 289/2025, art. I point 226, inserts sections 40c–40e into the public health insurance act, and art. XI puts it in force on 1 January 2026 with point 226 not among the exceptions (zakonyprolidi.cz/cs/2025-289, the same act as S5's URL). The section 40d detail now in Why now is read from that text: centres of highly specialised care, a drug that is the only registered product with its active ingredient and is billed with a treatment or used only on wards, the insurer paying the tendered price, and no payment for a drug bought outside that tender [S5]. The note itself is unchanged. Corrected against the sources rather than the old sentences: Motol and Homolka's 10 notices were cited [S2,S3] and are [S4]; "fifteen Czech public hospitals and regions" and "fifteen named public hospitals, regions and state institutes" became "15 public buyers", because S1's note counts 15 distinct public buyers without typing them and the tenders ledger (data/signals/tenders/2026-09-02.jsonl) lists a region, an ambulance service, a university faculty and the interior ministry among them; "most name the winning wholesaler" became "90 of the 106 notices also name the supplier that won", S1's own word, since the winners include a manufacturer (S2's note: BAXTER CZECH); "none of which has a budget line for the buying itself" became "every crown in the hospitals' medicine notices buys medicines, not purchasing tools", because S1's note says no such budget line appears in the evidence, not that the buyers have none; the insurer's 22.5bn CZK "over a 3.5bn CZK grey zone" became two sentences, because the VZP article (read 2026-09-18) gives the 3.5bn CZK as a separate estimate of retrospective bonuses in hospitals, as S8's note says, and "in 2024" is derived from its "za minulý rok" in an article of 10 March 2025; and the NKÚ press release (read 2026-09-18) confirms that the 956 and 3,300 CZK prices were paid by two different hospitals [S7]. Intrakoop is described as S16's why describes it, member pharmacies reporting volumes and prices; its "extended from care homes to hospitals" was not repeated in the body, because intrakoop.nl's medicines page (read 2026-09-18) describes the benchmark for care organisations and its hospital service as a knowledge platform mainly on medical devices. Flagged as inference: that "a hospital buying a tendered drug alone is not reimbursed" applies only once an insurer has tendered that drug centrally, and nothing on file says any insurer has done so yet [S5]; "four hospitals ran most of them" is arithmetic from S1–S4, 88 of 106; "hospitals already pay a Czech firm to pool their buying" rests on the firm selling to hospitals and Ostrava's city hospital being a customer, with no contract price on file [S18]; and in `entry.why`, "the first fee is over a year out", carried from the previous why, rests on the buyers being public bodies buying under procurement law, not on a source. Nothing was dropped: "No source states what running one system by hand costs a hospital" is now "What one medicine call costs a hospital in pharmacist and purchasing-staff hours is not known". No score, status, source, `note:`, `sources[]` order, entry gate value, title, brief, solution or good_for changed; the record has no `process` block and none was added.

2026-09-19 · Validated abroad answer rewritten (owner-approved) — The answer sentence named Denmark's central buyer and a Dutch cooperative, while the section's map and rows show the three companies on the comps ledger, in Britain, Germany and the US, so the page's first line and its map disagreed. Before, verbatim: "Solved elsewhere: Denmark buys its hospital medicines through one body, and a Dutch cooperative sells the price comparison itself [S13,S16]." After: "Solved elsewhere: Companies in Germany, Britain and the US already sell pieces of the job: pooled medicine buying for hospitals, drug-tender matching and pharmacy purchasing software [S14,S15,S17]." Each part is checked against its source: the German buying group pools purchasing for clinics and clinic pharmacies [S15], the London platform matches drug tenders with suppliers [S14], and the US product runs pharmacy ordering, pricing and supplier choice for a hospital system [S17]. "Pieces of the job" because none of the three sells the price comparison between hospitals that the solution names. The detail now follows the same order: the three companies first, then Denmark's public buyer and the Dutch cooperative as two answers that are not on the map, each with every fact and marker it had [S13,S16]; [S13]'s note says why Amgros has no comps row (no verifiable founding year). No fact was removed; no score, status, source, note, marker target, headline field or other body sentence changed.
