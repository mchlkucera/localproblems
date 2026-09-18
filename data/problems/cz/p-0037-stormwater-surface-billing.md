---
id: p-0037
region: cz
title: 'A draft Czech law would charge towns almost 5bn CZK a year for rainwater'
category: environment
geo: CZ-national
solution: 'Build a service that measures roofs and paving from aerial photos and gives sewer operators a ready billing file, as 2 companies already do in Germany.'
brief: 'Each bill depends on the size of every roof and road, and today owners mostly fill that in themselves [S8,S13]. Measuring the surfaces of just one town has cost over 1M CZK (which is way too much!) [S9].'
good_for: 'Someone who can map from aerial photos and would like to work with sewer operators.'
draft_law: 'Draft change to the Czech water-utilities law, still out for comment [S4]'
score: 9
scores:
  proof: 2
  money: 1
  urgency: 2
  demand: 2
  gap: 2
status: candidate
entry:
  level: hard
  buyer: public
  permission: none
  incumbents: adjacent
  integration: national-system
  money: bootstrap
  why: 'Easier: no licence is needed; no Czech firm sells the measuring yet; and a first job needs no outside money. Harder: the payers are towns, regions and road authorities, so most sales go through public purchasing rules; and the work depends on the state''s aerial photos and land register.'
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
    why: 'The same amendment makes owners of plants above 10,000 population equivalent commission an energy assessment of the plant and sewer network every four years; context only, it backs no score here.'
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

A draft law would charge owners of roads and homes for rainwater, and every bill depends on how much roof and paving they own [S3,S8].

- Towns would owe almost 5bn CZK a year for roads, regions almost 0.5bn [S3].
- Sewer operators mostly bill from areas their customers declare themselves [S8,S13].
- The water industry asked in 2020 for roads and homes to pay too [S6].

The charge is for rainwater that runs off a roof or paved surface into a public sewer [S8]. Under the water-utilities law in force, owners of motorways, roads, public service roads, national and regional railways, zoos, cemeteries and homes pay nothing for it [S3,S8].

- The draft, from the agriculture ministry, deletes that exemption in full [S3]. Its dates are under [Why now](#why-now) [S4].
- The ministry's impact assessment is its own estimate of what the change costs [S3]. It puts the new bill at almost 5bn CZK a year for towns, for rainwater from their local roads, and almost 0.5bn for regions, for their second- and third-class roads [S3].
- The state itself would owe less: under 30M CZK a year for motorways and first-class roads, and under 27M CZK for the railways [S3].
- The ministry argues that sewers carry rainwater from every surface, exempt or not, so the cost is not paid by whoever causes it [S3].
- An operator works out each bill from the customer's surfaces, each weighted by how much water it sheds, times the local long-term rainfall [S8]. One operator uses 644 mm a year, from 2022 [S8].
- The customer declares the surfaces and must report every change at once [S8]. Moravská vodárenská, a second operator, publishes the same procedure [S8].
- The water industry argued in 2020 that owners of roads and homes pay nothing for their rainwater, while residents face higher sewerage charges [S6]. It put the alternative, metering about 6,000 sewer overflow chambers, at hundreds of millions of crowns [S6].

Existing non-solutions: Czech billing systems already invoice the charge, but no Czech firm has been found selling the measuring [S13].

- Two billing systems invoice the charge from a keyed-in area, but measure nothing [S13].
- A third system bills water and sewerage for water companies [S13].
- Kolín's water operator made the one surface register on file, for Kolín alone [S13].
- No Czech firm was found selling the whole job as a product: measuring surfaces from aerial photos and the land register, a statement for each owner, and a file for billing [S13].
- Czech mapping and aerial-photo firms exist, but none came up in any search for this service [S13].

Why now: If the draft passes, sewer operators would have to bill roads and homes from July 2027, and towns would pay [S3,S4].

- A sewer operator would have to bill roads and homes it never billed [S3,S8].
- A town would pay for rainwater off every local road, from its budget [S3].
- Homeowners whose roofs drain to a public sewer would start paying [S3,S8].

Because roads and homes were never billed, an operator has no declared area on file for them [S8]. And no Czech firm sells the measuring; see [Competition](#competition) [S13].

The dates, and why it is still only a draft [S3,S7]:

- On 27 August 2026 the draft went out for comment to the other ministries [S4]. It is a government bill that amends both the Water Act and the water-utilities law [S4].
- In July 2027 the draft would take effect [S3].
- By 31 July 2027 Czechia must write the EU's new urban wastewater directive into its own law [S5]. The directive counts rainwater running off towns as part of their wastewater, but it does not require charging for it; that choice is the Czech draft's [S3,S5].
- On 31 March 2027 the state's loan call for treatment plants closes; what it pays for is under [Willing to pay](#willing-to-pay) [S10].
- In 2006 the agriculture ministry proposed the same deletion [S7]. The transport ministry and the union of towns and municipalities objected, putting their cost at 1.5–2bn and 2–3bn CZK a year, and the exemption stayed [S7,S8].
- The finance ministry did not back the 2006 proposal either, since the transport ministry's share would come from the state budget [S7].

The same bill would bring two more duties [S11,S12]:

- Owners of the 200-plus treatment plants sized for more than 10,000 people would have to commission an energy check of each plant and its sewers every four years [S11].
- Makers of medicines and cosmetics would have to fund a fourth treatment stage that removes trace pollutants [S12].

Who pays: Some money is spent already: one Czech city paid for a surface register, and water companies buy billing software for the charge [S13].

- In 2019 Kolín paid its water operator to register its billable surfaces [S13].
- No other contract like it has been found in the public contracts register [S13].
- The state's 1.36bn CZK loan call pays for treatment plants, not for billing [S10].

Kolín's price is in the table of what one buyer pays [S13]. The billing software takes whatever area the operator keys in; see [Competition](#competition) [S13]. If the draft passes, two sides would need the new areas measured [S3]:

- The sewer operators, which would have to invoice every newly billed surface [S3].
- The towns, regions and road authorities that would owe the charge, and would likely want to check the area before they pay [S3].

The loan call is from the State Environmental Fund, for the same EU directive [S10]. It lends 1,355.2M CZK at 1% to upgrade treatment plants sized for more than 10,000 people, up to 200M CZK a project [S10]. Applications opened on 2 July 2026, and the closing date is under [Why now](#why-now) [S10].

Solved elsewhere: In Germany, two firms map roofs and paving from aerial photos so towns can bill rainwater by area [S1,S2].

After several court rulings, German towns must, with a few exceptions, split the sewer charge in two: one part for wastewater and one for rainwater, billed by each plot's paved area [S1].

The first firm runs the whole job, from the flight to the fee notice [S1]:

- It flies over the town and traces every roof and paved surface from the photos, matched to the official land register map [S1].
- It sends each owner a form for each plot, to check the measured areas [S1].
- A phone hotline and a desk at the town hall help owners fill the forms in for several weeks [S1].
- It feeds the answers back in and fixes the final billable areas [S1].
- With a partner engineering firm it works out the fee rate [S1]. It hands the town the finished data, and sells software that keeps it up to date through to the fee notice [S1].

The second firm re-measures a town from fresh aerial photos at a better resolution, and has done so in many towns of every size and in two big cities [S2]. It estimates that paved area in mid-size towns grows by 2 to 3% a year [S2]. In some German states the aerial photos are free to get [S2]. With partners it also runs the owners' self-check, recalculates the fees and loads the data into the town's software [S2].

## First moves

1. Build a tool that measures every roof and paved yard in one sewer operator's area from the state's free aerial photos. Use the aerial photos of the state surveying office and the building outlines in the state's address and building register. Ask the operator for a sample of the areas its customers have declared, and check your numbers against them; how those areas are declared today is under [The opportunity](#opportunity). A tool that agrees with the declared areas where they are right, and shows where they are wrong, is what you show every buyer after that.
2. Offer one mid-size sewer operator a register of the surfaces it bills, at the price one Czech city already paid. That price, and who paid it, are under [Willing to pay](#willing-to-pay); there the city paid, so offer it to the town as well as to its operator. The operator gets its declared areas checked now, and a head start on the new surfaces if the draft passes; see [Why now](#why-now). Then sell a yearly update, since towns keep paving, as the German firms found; see [Validated abroad](#validated-abroad).
3. Send each owner a pre-filled statement of the measured areas on their plot, with an easy way to correct it. Mail it, or show it in the operator's customer portal. The German firms send each owner a form per plot and run a phone hotline while owners check it; see [Validated abroad](#validated-abroad). An owner who has agreed the area before the first bill has less reason to dispute it.
4. Hand the operator a billing file its current billing system can import, so nothing else changes for it. Czech water companies already run billing systems that invoice the charge from an area someone keys in; see [Competition](#competition). Match their import formats, and the measured areas go straight onto the invoices.
5. Offer towns, regions and road authorities their own billable area, worked out before the operator's invoice arrives. If the draft passes, they would owe the charge on every road they run; see [The opportunity](#opportunity). Knowing the area first lets them check the invoice, and the data you already hold for the operator answers it.

## Revisions

2026-09-04 · created — Written by the wastewater sweep after the 2026-09-03 weekly run deferred the cluster for want of a foreign comparable and a controlled Czech check. Proof 2 on two established German firms in one market [S1,S2]; money 1 on one signed public contract for the manual equivalent [S9]; urgency 2 on a draft effective July 2027 (deadline 1, because it is a draft) authorised 27 August 2026 (freshness 1) [S3,S4]; demand 2 on industry pressure and a ministry proposal documented since 2006 [S6,S7]; gap 2 on a Czech check with a passing control and no vendor selling this [S13]. The energy-assessment and micropollutant duties in the same bill were examined and not written up — see data/raw/2026-09-04/manifest-sweep-wastewater.md.

2026-09-16 · headline copy — The headline was rewritten for a general builder as three lines under the title: a `brief:` on what is happening and why it matters now, the `solution:` as a call to action, and a new `good_for:` line. New copy, verbatim — title: "A Czech draft law would charge towns almost 5bn CZK yearly for rainwater"; brief: "Owners of roads, railways and homes would start paying for rainwater drained into sewers from July 2027 [S3]. Sewer operators would bill them, and it is only a draft [S4]."; solution: "Build a service mapping roofs and paving from aerial photos into a billing file for sewer operators, as in Germany."; good_for: "Mapping and aerial-photo people who'd like to work with sewer operators.". Previous title, verbatim: "Czech sewer operators must bill rainwater from surfaces nobody has measured". Previous solution, verbatim: "A service that maps every roof and paved surface draining into a public sewer from the state orthophoto and cadastre, sends each owner a pre-filled area statement, and hands the sewer operator a billing-ready file.". There was no previous brief or good_for. The owner-reviewed draft was verified against its sources, then cut to the owner's length limits. "Almost 5bn CZK" is the impact assessment's annual figure for municipal budgets, for rainwater from roads [S3]. "Roads, railways, cemeteries and homes would start paying" now reads "owners of" them, since a surface does not pay; cemeteries were cut for length and remain in the body [S3,S8]. "As in Germany" rests on CAIGOS and Phoenics [S1,S2]. No score, status, source, note, marker or body sentence changed. Same date, good-for opener (owner: "Good for should always start with a person"): "Mapping and aerial-photo people who'd like to work with sewer operators." became "Someone who can map from aerial photos and would like to work with sewer operators." — same meaning, person first. Same date, owner-approved final copy, written verbatim with only the [Sn] markers added. Title "A Czech draft law would charge towns almost 5bn CZK yearly for rainwater" became "A draft Czech law would charge towns almost 5bn CZK a year for rainwater" (the 5bn is the impact assessment's yearly figure for municipalities [S3]). Brief "Owners of roads, railways and homes would start paying for rainwater drained into sewers from July 2027 [S3]. Sewer operators would bill them, and it is only a draft [S4]." became "Each bill depends on the size of every roof and road, and today owners mostly fill that in themselves [S8,S13]. Measuring the surfaces of just one town has cost over 1M CZK (which is way too much!) [S9]." Markers checked against the ledger: [S8] is VaK Vysoké Mýto's own method, the charge computed from reduced areas the customer declares and must keep updated, with Moravská vodárenská publishing the same procedure; [S13] is the gap check finding that the Czech billing systems invoice the charge from a keyed-in area. Neither counts operators, so "mostly" rests on two operators' published procedures and the billing systems, not on a survey. [S9] is Kolín's 2019 surface register, 1,449,918.80 CZK ex VAT. "Which is way too much" is the owner's judgment and is left as written. The draft status and July 2027 date stay in the body [S3,S4]. Solution "Build a service mapping roofs and paving from aerial photos into a billing file for sewer operators, as in Germany." (owner: "as in Germany" does not make sense) became "Build a service that measures roofs and paving from aerial photos and gives sewer operators a ready billing file, as 2 companies already do in Germany." The abroad count is taken from comps[] only: CAIGOS (comps[0], geo DE), which surveys sealed surfaces from aerial imagery for 40+ municipalities and hands the result to the billing system [S1]; Phoenics (comps[1], geo DE), which captures sealed-surface registers from its own aerial surveys and runs the fee calculation, re-surveying Hamburg and Frankfurt [S2]. None excluded. good_for unchanged. No score, status, source, note or body sentence changed. Same date, draft law: added `draft_law:` for the "Draft law" badge. The whole pain — a rainwater charge on roads, railways and homes — exists only in the agriculture ministry's draft amendment, out for inter-ministerial comment since 27 August 2026 [S3,S4]; under the law in force those surfaces are exempt [S8]. No other field changed.

2026-09-18 · body rewritten to the writing rules — Every section now opens with ONE answer sentence, the sections whose items the page shows carry their three most important first, and the rest follows as plain bullets and short paragraphs (pipeline/REWRITE.md; data/RECORD-TEMPLATE.md, "Writing the body"; p-0008 and p-0036 as the pattern). What moved where: The opportunity opens on the draft charge and the area every bill depends on, with the exemption list, the impact assessment's figures, how an operator works out a bill today and the water industry's 2020 push as its detail [S3,S6,S8]. Competition opens on the billing systems existing and the measuring missing; the billing systems and Kolín's operator are described by what they do, and their names, years and customer claims (USYS "most Czech water companies", since 1992; Datainfo) stay in their locals[] rows [S13]. Why now opens on who would bill and who would pay from July 2027; the comment date, the effective date, the EU transposition deadline, the loan call's closing date and the 2006 attempt follow as plain bullets, then the bill's two other duties [S3,S4,S5,S7,S10,S11,S12]. Willing to pay answers whether money is spent now: Kolín's register is cited to the market check [S13] and its price is left to its receipt [S9], which the body and moves no longer cite; the loan call's detail sits below [S10]. Validated abroad became one answer sentence, the German court rule, the first firm's method step by step, and the second firm's update method [S1,S2]; CAIGOS and Phoenics left the body, and their founding years, customer counts and named cities stay in comps[]. The moves lost every marker and figure for links: "USYS and Datainfo" became the billing systems water companies already run, and "the Kolín price point" became a link to Willing to pay. `entry.why` was rewritten as "Easier: … Harder: …". S11.why lost "this record" ("recorded here as context, it backs no score on this record" became "context only, it backs no score here"). Detail added from sources already on file, none of it new evidence: zoos and public service roads in the exemption list [S8]; the state's own smaller bills for motorways, first-class roads and railways, and the ministry's argument that the cost is not paid by whoever causes it, both from the reg-scan reading of the impact assessment [S3]; the 644 mm rainfall normal, the customer's duty to report changes and Moravská vodárenská publishing the same procedure [S8]; the water industry's 2020 argument and its metering alternative [S6]; that the EU directive does not itself require the charge [S3,S5]; the finance ministry's reluctance in 2006 [S7]; the loan call's 1,355.2M CZK at 1%, its 200M CZK cap and its application window [S10]; the first German firm's method, from the flight and the tracing matched to the land-register map through the owner forms, the hotline and town-hall desk, the returns and the fee rate worked out with an engineering partner, to the data and software it hands over [S1]; and the second firm's update method, its estimate that paved area in mid-size towns grows 2–3% a year, free aerial photos in some German states, and the owner self-check and fee recalculation it runs with partners [S2]. Corrected against the sources rather than against the old sentences: the exemption list was cited to [S8] alone, but S8 names zoos and not cemeteries, so cemeteries rest on [S3] and the sentence now cites both (the law's current text, read at zakonyprolidi.cz on 2026-09-18 and not a ledger source, lists both); the regions' share is "almost 0.5bn", the impact assessment's own "téměř 0,5 mld.", not "about" [S3]; "courts forced municipalities, from 2010" joined two facts S1 keeps apart, since S1 dates no court ruling and 2010 is when that firm began its split-charge work, so the body now says court rulings require the split, with a few exceptions, and the 2010 date stays in its comps row [S1]; move 3's "dispute workflow the German firms run" became the owner check form and phone hotline [S1] and the owner self-check [S2], since neither source describes a dispute process; "declare on a form" lost "on a form", which S8 does not say; and "both sides are public bodies" and `entry.why`'s "town-owned sewer operators" rest on no source (Kolín's register was bought by the city from its operator [S9,S13], and no source gives operators' ownership), so `entry.why` now names the payers, towns, regions and road authorities, as the public buyers [S3]. Flagged as inference: "an operator has no declared area on file" for roads and homes rests on their never having been billed [S8]; it replaces the unsourced "Nobody has measured the roofs and yards of households or the roads of every municipality at the parcel level a bill needs", which no source states (S13 finds no seller and one register, not an absence of all measurement). Also flagged: that payers "would likely want to check the area before they pay" [S3]; that operators "mostly" bill from declared areas rests on two operators' procedures and the billing systems [S8,S13], as the 2026-09-16 entry already says; and move 1's "free" aerial photos rest on no source on file. No score, status, source, `note:`, `sources[]` order, `entry` gate value, title, brief, solution, good_for or draft_law changed; the record has no `process` block.
