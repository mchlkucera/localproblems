---
id: p-0037
region: cz
title: Czech sewer operators must bill rainwater from surfaces nobody has measured
category: environment
geo: CZ-national
fix: 'A service that maps every roof and paved surface draining into a public sewer from the state orthophoto and cadastre, sends each owner a pre-filled area statement, and hands the sewer operator a billing-ready file.'
score: 9
scores:
  proof: 2
  money: 1
  urgency: 2
  demand: 2
  gap: 2
status: candidate
build:
  capital: garage
  first_revenue: months
  builder: small-team
  note: 'Orthophoto and cadastre segmentation plus a mail-and-verify workflow with owners, sold to sewer operators and to the cities that will suddenly owe the charge; the German firms that do this run 11 to 50 people.'
comps:
  - name: CAIGOS
    url: https://www.caigos.de/index.php/themen/datendienstleistungen/gesplittete-abwassergebuehr
    geo: DE
    since: 1987
    traction: 'Founded 1987 in Kirkel; more than 1,200 customers among German municipalities and utilities; since 2010 it has introduced or re-surveyed the split sewer charge for more than 40 municipalities, with named customers including Meissen, Zwickau, Speyer, Ludwigshafen, Lübeck and Regensburg on its service page (caigos.de, read 2026-09-04). Part of the VIVAVIS group.'
    signal: de-caigos
  - name: Phoenics
    url: https://phoenics.de/fachkataster/versiegelungskataster/
    geo: DE
    since: 1994
    traction: 'Founded 1994 in Seelze, 11 to 50 staff; calls itself the market leader in capturing and updating sealed-surface data for more than 25 years, and its named customers include Hamburg and Frankfurt, where it has re-run the survey (phoenics.de and its LinkedIn page, read 2026-09-04).'
    signal: de-phoenics
locals:
  - name: USYS (UTILITIES SYSTEMS)
    url: https://www.usys.cz/en/implementations/
    ico: '17772796'
    since: 1992
    competes: adjacent
    maturity: established
    evidence: 'It sells USYS.net, the customer information and billing system most Czech water companies run, with customers including Pražské vodovody a kanalizace, Brněnské vodárny a kanalizace and Ostravské vodárny a kanalizace, in use since 1992 (usys.cz, read 2026-09-04). It bills the rainwater charge from whatever area the operator keys in; it does not measure the area. The current legal entity dates from 2022, the product line from 1992.'
  - name: DATAINFO
    url: https://www.datainfo.cz/vodne-stocne/
    ico: '15046265'
    since: 1991
    competes: adjacent
    maturity: established
    evidence: 'It sells ZIS Datainfo Vodné a Stočné, a billing program for small and mid-size water utilities that invoices water, sewerage and rainwater charges; it publishes a public customer count in words — hundreds of customers — and has developed the program for over 35 years (datainfo.cz, read 2026-09-04). It invoices from a declared area and does not map surfaces.'
  - name: Softbit software
    url: https://www.softbit.cz/informacni-system-vodarenske-spolecnosti
    ico: '27473716'
    since: 2005
    competes: adjacent
    maturity: early
    evidence: 'It sells an information system for water companies covering meter points, readings and the billing of water and sewerage charges (softbit.cz, read 2026-09-04); its page says nothing about rainwater and names no customer, so how much it sells is unknown.'
  - name: Energie AG Kolín (formerly VODOS)
    ico: '47538457'
    since: 1993
    competes: adjacent
    maturity: established
    evidence: 'The Kolín water and sewer operator: it made the 2019 register of surfaces liable for the rainwater charge for its own city, with customers including Město Kolín, which paid about 1.45M CZK for it and later awarded it the 2026 to 2035 sewerage concession [S9]. It surveys for the city it operates and does not sell surface mapping to other operators.'
sources:
  - type: arbitrage
    url: https://www.caigos.de/index.php/themen/datendienstleistungen/gesplittete-abwassergebuehr
    name: 'CAIGOS'
    gist: 'the German split-charge surveyor'
    why: 'A Kirkel GIS house that has flown, mapped and handed to billing the sealed surfaces of more than 40 German municipalities since 2010.'
    note: 'Sweep 2026-09-04, staged as de-caigos in data/raw/2026-09-04/staged-sweep-wastewater.jsonl.
      Verbatim: "Bereits seit dem Jahr 2010 haben wir in mehr als 40 Kommunen unterstützend die
      gesplittete Abwassergebühr mit eingeführt bzw. über eine komplette Neuerfassung der
      versiegelten Flächen die Überarbeitung ... umgesetzt." Founded 1987 (business-geomatics.com,
      2017-08-15); "Mehr als 1.200 Kunden" (vivavis.com/caigos-gmbh). Service page lists the steps:
      Befliegung, Luftbild, ALKIS matching, owner questionnaires, hotline, fee calculation, handover
      to the billing system. No signal ref on purpose: the staged id lands only when the
      orchestrator completes the run.'
    date: '2026-09-04'
  - type: arbitrage
    url: https://phoenics.de/fachkataster/versiegelungskataster/
    name: 'Phoenics'
    gist: 'Hamburg and Frankfurt re-surveyed'
    why: 'A Seelze photogrammetry firm, founded 1994, that captures and updates sealed-surface registers for the split sewer charge and has re-run the survey for Hamburg and Frankfurt.'
    note: 'Sweep 2026-09-04, staged as de-phoenics. Verbatim: "Das Update-Verfahren wurde bereits
      für die Großstädte Hamburg und Frankfurt angewendet." and "Seit über 25 Jahren ist Phoenics
      Marktführer im Bereich der Neuerfassung und des Updates von Versiegelungsdaten." Founded 1994
      per its LinkedIn company page ("Phoenics was founded in 1994"), 11-50 employees. No signal
      ref on purpose, as for S1.'
    date: '2026-09-04'
  - type: regulation
    url: https://odok.gov.cz/portal/services/download/attachment/KORNDXCB3K8H/
    name: 'Draft amendment to the water-utilities act — every rainwater exemption deleted'
    gist: 'the July 2027 draft'
    why: 'The agriculture ministry draft deletes the paragraph that exempts roads, railways, cemeteries and homes from paying for rainwater discharged to a public sewer; its impact assessment prices the new bill at almost 5bn CZK a year for municipalities and about 0.5bn for regions, effective July 2027.'
    note: 'reg-vak-srazkove-vody-poplatek (reg-scan, 2026-09-03), read from the RIA attachment
      KORNDXCB3K8H. Dated here 2026-08-27, the day the material was authorised for the comment
      procedure; the RIA summary sheet gives effective 07/2027. It is a DRAFT: the deadline point is
      scored at 1, not 2, because the forcing function is not yet law and the same deletion was
      proposed and dropped in 2006 [S7].'
    date: '2026-08-27'
    signal: reg-vak-srazkove-vody-poplatek
  - type: regulation
    url: https://odok.cz/portal/veklep/material/KORNDXBH65S3/
    name: 'The bill itself in the legislative library'
    gist: 'in comment procedure'
    why: 'The government bill amending the Water Act and the water-utilities act, submitted by the Ministry of Agriculture and in the inter-ministerial comment procedure since 27 August 2026.'
    note: 'veklep-KORNDXBH65S3 (scripted veklep feed, 2026-09-02). The newest dated source on this
      record; carries the freshness point of urgency.'
    date: '2026-08-27'
    signal: veklep-KORNDXBH65S3
  - type: regulation
    url: https://eur-lex.europa.eu/legal-content/EN/LSU/?uri=CELEX:32024L3019
    name: 'Directive (EU) 2024/3019 — transposition by 31 July 2027'
    gist: 'the EU deadline behind the draft'
    why: 'The recast urban wastewater directive that treats urban runoff as part of urban wastewater and must be transposed by 31 July 2027 — the reason the Czech draft carries a July 2027 date.'
    note: 'reg-uwwtd-epr (reg-scan, 2026-08-13). The directive itself does not order member states
      to charge households or roads for rainwater; that choice is the Czech draft''s [S3]. Cited for
      the transposition date only.'
    date: '2027-07-31'
    signal: reg-uwwtd-epr
  - type: news
    url: https://www.ivodarenstvi.cz/lidem-hrozi-zvyseni-stocneho-problem-by-vyresilo-zruseni-vyjimek-ze-zakona/
    name: 'iVodárenství — water industry asks to scrap the exemptions'
    gist: 'industry pressure, 2020'
    why: 'The water industry, through František Barák, argues in 2020 that households and roads pay nothing for the rainwater they send to the sewer and that scrapping the exemption would spare residents a rise in sewerage charges.'
    note: 'Article dated 2020-05-27. Verbatim: "všichni vlastníci komunikací nebo domů určených k
      trvalému bydlení neplatí za odvedení a vyčištění srážkových vod nic" and "Kdyby byla
      odstraněna výjimka a všichni znečišťovatelé by zaplatili, nemusíme řešit problém, spojený s
      měřením"; the alternative — metering ~6,000 overflow chambers — is put at hundreds of millions
      of crowns. Demand point: industry pressure for the very change the draft now makes.'
    date: '2020-05-27'
  - type: news
    url: https://voda.tzb-info.cz/normy-a-pravni-predpisy-voda-kanalizace/3757-srazkove-vody-a-zakon-o-vodovodech-a-kanalizacich
    name: 'TZB-info — the ministry proposed the same deletion in 2006'
    gist: 'first attempt, 2006'
    why: 'The agriculture ministry official in charge of water utilities wrote in 2006 that the ministry had proposed deleting the exemptions and that the transport ministry and the union of towns and municipalities objected, citing 1.5 to 2bn and 2 to 3bn CZK a year respectively.'
    note: 'Article by Ing. Vladimír Chaloupka, MZe, dated 2006-12-13. The same paragraph 20(6)
      exemptions, the same objectors, the same order of magnitude; 2026 is the second documented
      attempt. Demand point: a recurring, documented dispute over who pays for rainwater from exempt
      surfaces.'
    date: '2006-12-13'
  - type: news
    url: https://www.vodovody-vm.cz/pro-zakazniky/vypocet-odvadeni-srazkovych-vod
    name: 'VaK Vysoké Mýto — how an operator computes the charge today'
    gist: 'declared areas, by hand'
    why: 'A mid-size operator''s own instructions: annual rainwater volume equals the sum of the customer''s reduced areas times the long-term rainfall normal, from surface categories the customer declares and must keep updated.'
    note: 'Read 2026-09-04. Verbatim: "Roční množství odváděných srážkových vod Q v m3 = součet
      redukovaných ploch v m2 krát dlouhodobý srážkový normál" (644 mm/year from 2022-01-01) and
      "Veškeré změny je odběratel povinen neprodleně oznámit"; the page repeats the § 20(6)
      exemption list. Moravská vodárenská (smv.cz) publishes the same procedure. Demand point: the
      area behind every bill is self-declared and unverified.'
    date: '2026-09-04'
  - type: price
    url: https://smlouvy.gov.cz/smlouva/8041799
    name: 'Kolín — a register of the surfaces liable for the rainwater charge'
    gist: 'about 1.45M CZK, one city'
    why: 'What one Czech city paid its water operator in 2019 for a one-off register of the surfaces already liable for the rainwater charge — the manual equivalent of the product, priced.'
    note: 'Registr smluv 8041799 (contract 01419/2018), "Smlouva o dílo na zhotovení pasportu ploch
      podléhajících platbě za odvádění srážkových vod", signed 2019-01-14; payer Město Kolín (IČO
      00235440), contractor VODOS s.r.o. (IČO 47538457, now Energie AG Kolín a.s.); 1,449,918.80 CZK
      ex VAT, 1,754,500 CZK incl. VAT (amount rounded to the crown). Found by Hlídač full-text
      search on 2026-09-04; not a ledger signal, so no signal ref. The same pair signed the
      2026-2035 sewerage concession (hlidac-33820213). Tagged money: one signed public contract for
      the manual equivalent is rung 1.'
    date: '2019-01-14'
    payer: 'Město Kolín, a town of about 32,000 people'
    amount_czk: 1449919
    unit: one-off
    basis: signed-contract
    dims: [money]
  - type: tender
    url: https://sfzp.gov.cz/dotace-a-pujcky/financni-nastroje-a-pujcky/vyzva-2-2026-fn-cov/
    name: 'SFŽP call 2/2026 — 1.36bn CZK of loans for the same plants'
    gist: 'plant money, not billing money'
    why: 'The state environmental fund lends 1,355.2M CZK at one percent to upgrade treatment plants above 10,000 population equivalent for the same directive; it funds treatment, not the billing of rainwater, so it backs no score here.'
    note: 'dotace-sfzp-2-2026-fn-cov (dotace-scan, 2026-09-03). Applications 2026-07-02 to
      2027-03-31, capped at 200M CZK a project. Cited so the reader sees where the directive''s
      public money sits; dims empty on purpose.'
    date: '2027-03-31'
    signal: dotace-sfzp-2-2026-fn-cov
    dims: []
  - type: regulation
    url: https://odok.gov.cz/portal/services/download/attachment/KORNDXCB3K8H/
    name: 'The same draft — four-yearly energy assessment for 200-plus plants'
    gist: 'the bill''s energy duty'
    why: 'The same amendment makes owners of plants above 10,000 population equivalent commission an energy assessment of the plant and sewer network every four years; recorded here as context, it backs no score on this record.'
    note: 'reg-vak-energeticke-posouzeni-cov (reg-scan, 2026-09-03). The sweep examined this duty
      as a record of its own and did not write one: the audit is already sold by licensed
      specialists and Veolia''s own engineers, and the software field holds early Czech vendors —
      see data/raw/2026-09-04/manifest-sweep-wastewater.md. dims empty on purpose.'
    date: '2027-07-01'
    signal: reg-vak-energeticke-posouzeni-cov
    dims: []
  - type: regulation
    url: https://odok.gov.cz/portal/services/download/attachment/KORNDXCB3K8H/
    name: 'The Water Act draft — producer-funded fourth treatment stage'
    gist: 'the bill''s micropollutant duty'
    why: 'The companion amendment to the Water Act builds a producer-responsibility scheme in which medicine and cosmetics makers fund the fourth treatment stage that removes micropollutants; context only, no score here.'
    note: 'reg-vodni-zakon-epr-mikropolutanty (reg-scan, 2026-09-03). Examined by the sweep and not
      written up: capex engineering sold through Czech branches of foreign equipment makers, with
      carbon-regeneration contractors already domestic. dims empty on purpose.'
    date: '2027-06-01'
    signal: reg-vodni-zakon-epr-mikropolutanty
    dims: []
  - type: gap-check
    url: https://www.usys.cz/en/implementations/
    name: 'Czech check — billing engines exist, the measuring does not'
    gist: 'the Czech field, searched'
    why: 'Five Czech query shapes, an English one, the state contracts register in full text and the business register: the billing systems that invoice the charge are named, no Czech vendor sells the surface mapping, and the one register on file was made by a city''s own operator.'
    note: 'Gap check 2026-09-04 (sweep). FOUND, ADJACENT: USYS/UTILITIES SYSTEMS (IČO 17772796,
      product since 1992) and DATAINFO (15046265, 1991) invoice the charge from a keyed-in area;
      Softbit (27473716, 2005) bills water and sewerage; Energie AG Kolín, formerly VODOS
      (47538457, 1993), made the 2019 Kolín register for its own city (registr smluv 8041799).
      NOT FOUND: any Czech firm selling impervious-surface mapping from orthophoto and cadastre
      with an owner statement and a billing handover. GIS and orthophoto vendors looked up in ARES
      (T-MAPY 47451084, GEOVAP 15049248, TopGis 29182263, ARCDATA PRAHA 14889749) surfaced on none
      of the stormwater queries and are not entered. Registr smluv full text via Hlídač:
      "srážkových vod" plochy pasport (1,136 hits, one on subject — Kolín), pasport "zpevněných
      ploch" (2,238 hits, none on subject), "srážkových vod" (ortofoto OR "letecké snímky" OR
      "odvodňovaných ploch" OR GIS) stočné (59 hits, none on subject). POSITIVE CONTROL PASSED: the
      same method at a p-0026 incumbent — "dálkové odečty vodoměrů jako služba pro vodárenské
      společnosti platforma" — surfaced VODÁRENSKÁ AKCIOVÁ SPOLEČNOST first, then KAPKA, ČEVAK
      and AQUA SERVIS; Softlink did not surface on that query shape. Gap 2 rests on this check; the
      four adjacent entries move nothing.'
    date: '2026-09-04'
    queries:
      - "srážkové vody poplatek výpočet odvodňované plochy software vodárny zákaznický informační systém"
      - "evidence zpevněných ploch letecké snímky srážkové vody vodárenská společnost GIS dodavatel odvodňované plochy"
      - "pasport zpevněných ploch odvodňované plochy srážkové vody GIS služba obce dodavatel stanovení plochy stočné"
      - "výpočet stočného ze srážkových vod z ortofotomapy automaticky software plochy střech vodárenská společnost aplikace"
      - "zaměření odvodňovaných ploch pro výpočet srážkových vod nabídka geodetické služby stočné srážkové vody firma"
      - "Czech Republic impervious surface mapping stormwater sewer fee software vendor Czechia startup"
    checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
    expires: '2026-12-03'
created: '2026-09-04'
updated: '2026-09-04'
---

Czech sewer operators may charge for rainwater only from the surfaces the law lets them charge, and the law exempts most of them: roads, motorways, railways, cemeteries and every home [S8]. A draft amendment to the water-utilities act, in comment procedure since 27 August 2026, deletes that exemption in full [S3,S4]. The state's own impact assessment prices the new annual bill at almost 5bn CZK for municipalities and about 0.5bn CZK for regions [S3].

Why now: the draft takes effect in July 2027, the month the EU urban wastewater directive must be transposed [S3,S5]. It is a draft, and the same deletion was proposed and dropped in 2006 after the transport ministry and the municipal union objected [S7]. Operators compute the charge today from areas customers declare on a form, times a runoff coefficient and the local rainfall normal [S8]. Nobody has measured the roofs and yards of households or the roads of every municipality at the parcel level a bill needs. The same bill also makes owners of 200-plus plants commission an energy assessment every four years [S11] and builds a producer-funded fourth treatment stage [S12].

Who pays: the sewer operators that must invoice the new surfaces, and the cities, regions and road authorities that will owe the charge and want the area right. Kolín paid its water operator about 1.45M CZK in 2019 for a one-off register of the surfaces already liable [S9]. Both sides are public bodies; the 1.36bn CZK state loan call for the same plants funds treatment upgrades, not billing [S10].

Existing non-solutions: the billing engines exist and the measuring does not. USYS — the customer billing system most Czech water companies run, in use since 1992 — and Datainfo's billing program both invoice rainwater from an area someone keys in [S13]. No Czech firm sells the mapping — orthophoto plus cadastre, owner statement, billing file — as a product; the one register on file was made by Kolín's own operator for Kolín [S9,S13].

Solved elsewhere: Germany went through this after courts forced municipalities, from 2010, to split the sewer charge into a wastewater part and a rainwater part billed per square metre of roof and paving. CAIGOS — a municipal mapping-software house founded 1987, with more than 1,200 customers — has surveyed sealed surfaces from aerial imagery for more than 40 municipalities since 2010 and hands the result to the billing system [S1]. Phoenics, founded 1994, has re-surveyed Hamburg and Frankfurt [S2].

## First moves

1. Build the surface classifier on the state surveying office's free orthophoto and the building footprints in the state address-and-building register for one operator's territory, and check it against a sample of the areas that operator already bills [S8].
2. Sell the first job to a mid-size operator as a one-off register at the Kolín price point, then as an annual update subscription [S9].
3. Package the owner side: a pre-filled area statement per parcel, mailed or shown in the operator's customer portal, with the dispute workflow the German firms run [S1,S2].
4. Deliver the billing file in the formats USYS and Datainfo import, so the operator changes nothing else [S13].
5. Offer cities and road authorities the mirror product — their own billable surface, computed before the operator's invoice arrives [S3].

## Revisions

2026-09-04 · created — Written by the wastewater sweep after the 2026-09-03 weekly run deferred the cluster for want of a foreign comparable and a controlled Czech check. Proof 2 on two established German firms in one market [S1,S2]; money 1 on one signed public contract for the manual equivalent [S9]; urgency 2 on a draft effective July 2027 (deadline 1, because it is a draft) authorised 27 August 2026 (freshness 1) [S3,S4]; demand 2 on industry pressure and a ministry proposal documented since 2006 [S6,S7]; gap 2 on a Czech check with a passing control and no vendor selling this [S13]. The energy-assessment and micropollutant duties in the same bill were examined and not written up — see data/raw/2026-09-04/manifest-sweep-wastewater.md.
