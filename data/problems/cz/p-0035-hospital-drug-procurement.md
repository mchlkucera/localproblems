---
id: p-0035
region: cz
title: Czech hospitals each buy their medicines alone, and the state keeps finding they overpay
fix: 'A price comparison for hospital medicines, assembled from the hospitals'' own published
  purchasing notices, so a hospital pharmacy can see what its peers paid for the same molecule
  before it opens the next order.'
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
build:
  capital: garage
  first_revenue: year-plus
  builder: small-team
  note: 'Public tender notices supply the raw material, so a small team can assemble a first
    comparison cheaply; but the unit prices that would make it authoritative are contractually
    withheld, and every buyer is a public hospital on a procurement clock.'
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

Between 6 July and 2 September 2026, fifteen Czech public hospitals and regions published 106 separate notices to buy medicines, each under its own dynamic purchasing system — a standing supplier list re-opened for every order [S1]. Všeobecná fakultní nemocnice v Praze ran 38, split by drug class: separate systems for antithrombotics, immunosuppressants and cancer drugs [S1]. Fakultní nemocnice Olomouc ran 24, Bulovka 16, Motol and Homolka 10 [S2,S3].

The state keeps finding the result. Its supreme audit office found three university hospitals buying medicines very often by direct order, one paying 956 CZK a pack for an antibiotic another bought at 3,300 CZK [S7]. Six years later the same office called medicines the largest area of failings it sees in healthcare buying [S9]. The competition authority wrote hospitals a manual because it meets the problem ever more often [S10].

Why now: since 1 January 2026 the public health insurance act lets health insurers tender centrally, for providers, the high-cost medicines given only in specialised hospital centres [S5]. A health ministry price ruling took effect the same day and dropped the split trade margin on purely hospital medicines [S6].

Who pays: fifteen named public hospitals, regions and state institutes, none of which has a budget line for the buying itself [S1]. The national health insurer paid 22.5bn CZK for those centre medicines in one year, over a 3.5bn CZK grey zone of retrospective supplier bonuses [S8]. Nine Prague notices repeat one 2bn CZK figure — the system ceiling, not spend [S1]. No source states what running one system by hand costs a hospital.

Existing non-solutions: the field is not empty. eCENTRE has pooled Czech public buying through electronic auctions since 2006 and sells it to hospitals; Ostrava's city hospital reports 21, 34 and 25 percent savings on three supply groups [S18]. The procedures run on established Czech platforms — JOSEPHINE from PROEBIZ, E-ZAK from QCM, Tender arena and eGordion (each hosts calls, none pools the buying) [S18]. The ministry and the pharmaceutical industry association have compared unit prices since 2019, but only across the ministry's own hospitals, and may not pass them on [S11].

Solved elsewhere: Denmark buys almost all public-hospital medicines through Amgros, one body owned by the five regions that own the hospitals; it reports nearly 10 billion Danish crowns of savings in 2024 [S13]. Germany's Vivecti Group, trading since 1993, intermediates over €7bn a year for more than 6,000 providers, clinic pharmacies included [S15]. Intrakoop, a Dutch cooperative founded in 1959, sells the comparison rather than the buying: members report what they paid and see who overpays [S16].

## First moves

1. Read the notices you already hold. Fifteen buyers published 106 medicine calls in nine weeks, and most name the winning wholesaler alongside the buyer [S1,S2]. Build the first price picture out of those before asking any hospital for anything, and print nothing that is a system ceiling as if it were spend [S1].
2. Call Fakultní nemocnice Olomouc and Fakultní nemocnice Bulovka. Between them they ran 40 medicine calls in the same nine weeks [S2,S3]. Ask what one call costs in pharmacist and procurement-officer hours — nobody has published that number, and it is the price your product has to beat.
3. Price against eCENTRE, not against an empty field. It has pooled Czech public buying since 2006, sells it to hospitals, and Ostrava's city hospital publishes what it saved [S18]. The platforms — JOSEPHINE, E-ZAK, Tender arena, eGordion — host the calls and do not pool them [S18].
4. Sell the comparison, not the buying. Intrakoop's members report what they paid and see who is overpaying [S16]. The Czech version of that data exists and is closed: the ministry database covers only its own hospitals and its unit prices may not be passed on [S11]. Public notices are the way in that nobody has to grant you.
5. Take it to the insurers. Since 1 January 2026 they may tender centre medicines centrally [S5], and the national insurer has already argued for it with its own numbers — 22.5bn CZK a year and a 3.5bn CZK bonus grey zone [S8].
6. Expect no grant. The open state eHealth call runs to 2 December 2026 but funds interoperable clinical documentation, not purchasing, and no other call found funds this [S18].

## Revisions

2026-09-03 · record created — Minted from a topic sweep on Czech hospital drug purchasing. The scale leg was already committed: 106 drug-object notices from 15 named public buyers in nine weeks [S1]. The window is dated twice on 1 January 2026 [S5,S6]. Demand is the state's own — audit office, competition authority, ministry, national insurer [S7,S9,S10]. eCENTRE sells this to hospitals and passes the established test, so gap is 0 and status is watching [S18].
