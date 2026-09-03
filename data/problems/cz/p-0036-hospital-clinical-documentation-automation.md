---
id: p-0036
region: cz
title: Czech hospitals write reports as free text, then pay people to read them again
fix: 'Report templates inside the hospital system, so a radiology or oncology report is captured
  as data at the moment it is written and can be turned into insurer codes and registry entries
  for a coder to confirm rather than re-read.'
category: health
geo: CZ-national
score: 10
scores:
  proof: 3
  money: 2
  urgency: 2
  demand: 2
  gap: 1
status: candidate
build:
  capital: funded
  first_revenue: year-plus
  builder: small-team
  note: 'Hospital-grade software wired into a hospital system and read by insurers, needing a
    clinician co-founder and Czech medical-text models; Tiplu reached 80 German hospitals from a
    2016 start through pilots, and the first Czech pilot is a cancer institute that has already
    written the specification.'
comps:
- name: Jacobian (Smart Reporting)
  url: https://www.jacobian.com/
  geo: DE
  since: 2014
  traction: 'EUR 23M Series C led by TVM Capital Life Science with Bayern Kapital, April 2024;
    more than 16,000 physicians in over 90 countries; distributed by Siemens Healthineers, GE
    Healthcare and Canon (TVM release, 2024). Announced the acquisition of Fluency for Imaging
    to form Jacobian, over 80 million exams a year combined (company release, Oct 2025)'
  markets: [US, CA, AU]
- name: Rad AI
  url: https://www.radai.com/
  geo: US
  since: 2018
  traction: 'USD 60M Series C led by Transformation Capital at a USD 525M valuation, January
    2025; customers include Advocate Health, Memorial Hermann Health System, Corewell Health,
    Atlantic Health System and Yale New Haven Health; thousands of radiologists daily at
    practices covering nearly 50 percent of US imaging (company release, 2025)'
- name: ID Berlin (ID DIACOS)
  url: https://www.id-berlin.de/en/
  geo: DE
  since: 1985
  traction: 'ID DIACOS coding software in more than 1,200 hospitals in Germany, Austria and
    Switzerland (company site, read 2026); trading since 1985 (it-dock vendor profile)'
  markets: [AT, CH]
- name: Tiplu (MOMO)
  url: https://tiplu.de/produkte/momo/
  geo: DE
  since: 2016
  traction: 'MOMO AI-assisted coding in more than 80 hospitals (medconweb, 2023); customers
    include Charité, Universitätsklinikum Schleswig-Holstein, Schön Klinik, BG Kliniken and
    Klinikum Lüneburg (company site, read 2026)'
locals:
- name: STAPRO (AI asistent výkaznictví)
  url: https://www.stapro.cz/
  ico: '13583531'
  since: 2026
  competes: direct
  maturity: early
  evidence: 'It sells FONS Enterprise, a hospital information system, and in 2026 added an AI
    assistant that reads a patient''s documents and discharge summary and
    proposes diagnosis and procedure codes for a coder to check. That assistant is a pilot: 23
    hospitals were using it free of charge in August 2026, coders ran 2,200 cases through it in
    July, and its price after 31 August 2026 is not published [S4]. STAPRO itself has traded since
    1990; the coding assistant has not.'
- name: ICZ (Asistent vykazování AV(D))
  url: https://www.iczgroup.com/podpora-vykazovani-zdravotni-pece/
  ico: '25145444'
  since: 2023
  competes: direct
  maturity: early
  evidence: 'It sells Asistent vykazování AV(D), a tool that runs machine-learning models over a
    discharge report and proposes the diagnoses to bill, each with a probability, built with the
    University of West Bohemia and presented as a product on its site since October 2023 [S16].
    The product page names no hospital that has bought it and gives no count; in November 2023 a
    first pilot at Fakultní nemocnice Brno was still being prepared [S16]. ICZ itself has sold
    hospital systems since 1997.'
- name: Medicalc
  url: https://www.medicalc.cz/
  ico: '26350513'
  since: 2026
  competes: direct
  maturity: early
  evidence: 'It sells a hospital information system to more than 100 Czech facilities, and in
    January 2026 its director described AI inside it that turns a phone recording of a ward round,
    consultation, operation or autopsy into a structured report and builds structured data out of
    free text [S16]. The interview does not say whether any hospital runs those AI features yet, so
    for this product it counts as new; the company itself dates from 2002.'
- name: Datlowe (HAIDI)
  ico: '02931737'
  since: 2014
  competes: adjacent
  maturity: established
  evidence: 'It sells HAIDI, which reads a hospital''s free-text clinical documentation by machine
    to flag hospital-acquired infections — the same Czech clinical text, read for a different
    question. Used in Fakultní nemocnice Brno, Krajská nemocnice T. Bati in Zlín and the Liberec
    regional hospitals since January 2024, covering more than a third of Czech hospital beds [S16].
    It does not write reports, code them for the insurer or fill registries; it is the local proof
    that Czech clinical text can be read by machine, and the firm best placed to turn toward this.'
- name: NEWTON Technologies (NEWTON Dictate)
  url: https://www.newtontech.net/en/newton-dictate/
  ico: '28479777'
  since: 2008
  competes: adjacent
  maturity: established
  evidence: 'It sells NEWTON Dictate, Czech speech-to-text with medical dictionaries that types a
    dictated finding straight into the hospital system as free text; used in IKEM, Všeobecná
    fakultní nemocnice, the university hospitals in Hradec Králové and Ostrava and the regional
    hospitals in Liberec and Kolín, more than 350 licences in healthcare by 2015 [S16]. It makes the
    free text faster to produce, not structured — the report still has to be read again.'
- name: Carebot
  ico: '10898263'
  since: 2021
  competes: adjacent
  maturity: established
  evidence: 'It sells certified AI that reads chest X-rays and flags findings for the radiologist,
    available in roughly 50 to 60 Czech hospitals by March 2025 after a EUR 1.2M round [S16]. It
    reads the image, not the report: the radiologist still writes the finding as free text, which
    is the step this problem is about. Founded June 2021.'
sources:
- type: ask
  name: "Hack jak Brno 2026 — StructREP, Masarykův onkologický ústav"
  gist: "the structured-reporting ask"
  why: "Brno's cancer institute asks for a tool that lets doctors write structured radiology reports straight into the hospital system from smart templates, so the report is data at the moment it is written."
  url: https://www.hackjakbrno.cz/
  note: 'hack-5d646892: owner Masarykův onkologický ústav; challenge StructREP at Hack jak Brno
    2026, 27–29 November 2026, Fakultní nemocnice u sv. Anny v Brně, organised by Insane Business
    Ideas s.r.o. (InBui). Card text: "Vytvořte nástroj, který umožní lékařům jednoduše psát
    strukturované radiologické nálezy přímo v nemocničním systému pomocí chytrých šablon." Stated
    benefits: faster and more accurate reports, better communication between doctors, parametric
    data collected at the moment of writing. AN ASK CITES DEMAND ONLY (MATCH.md §11): no prize,
    budget or team count is recorded, and nothing here backs money, gap or urgency beyond the
    freshness of the date. Page read 2026-09-03.'
  date: '2026-09-03'
  signal: hack-5d646892
  dims: [demand]
- type: ask
  name: "Hack jak Brno 2026 — AI DocuHelper, Masarykův onkologický ústav"
  gist: "the oncology-extraction ask"
  why: "The same institute states that extracting data from oncology records is slow and demanding today, and asks for an AI assistant that finds the key facts in a report, filters them and pre-fills forms for documentation staff, registries and research."
  url: https://www.hackjakbrno.cz/
  note: 'hack-582e2346: owner Masarykův onkologický ústav; challenge AI DocuHelper, same event and
    page as S1. Card text: "Extrakce dat z onkologické dokumentace je dnes pomalá a náročná. Cílem
    je vytvořit AI asistenta, který dokumentátorům usnadní práci: rychle najde klíčové údaje ve
    zprávách, nabídne přehledné" [filtering, pre-filled forms; fewer errors; better data for
    registries, research and clinical practice]. Second ask from the same owner in the same week:
    together with S1 and S3 this is the recurrence that lifts demand to 2. Demand only, per
    MATCH.md §11.'
  date: '2026-09-03'
  signal: hack-582e2346
  dims: [demand]
- type: ask
  name: "Hack jak Brno 2026 — AutoCode AI, JINAG"
  gist: "the insurer-coding ask"
  why: "The South Moravian public-innovation agency states that a hospital coding department spends hours transcribing discharge summaries into procedure and material codes for insurers by hand, that errors and omissions cost money and overload staff, and asks for an AI that proposes the codes for a coder to validate."
  url: https://www.hackjakbrno.cz/
  note: 'hack-cf9cd96f: owner JINAG — Jihomoravská agentura pro veřejné inovace, the South
    Moravian regional innovation agency (jinag.eu, read 2026-09-03: a regional agency with social
    and health services as one of five themes; not itself a hospital). Card text: "Kodérské
    oddělení nemocnice tráví hodiny ručním přepisem epikríz do kódů výkonů a materiálů pro
    pojišťovny. Chyby nebo opomenutí znamenají finanční ztráty a přetížení personálu." The card
    does not name the hospital whose coding department it describes. Demand only, per MATCH.md
    §11; it says nothing about whether a vendor sells this, which S16 answers.'
  date: '2026-09-03'
  signal: hack-cf9cd96f
  dims: [demand]
- type: news
  name: "STAPRO — AI coding assistant in 23 Czech hospitals, free to 31 August 2026"
  gist: "the 23-hospital pilot"
  why: "The hospital-system vendor Stapro reports its AI assistant for insurer coding running in 23 hospitals on a free pilot, with 2,200 unique cases coded through it in July 2026 alone — the buyer side voting with its coders' time."
  url: https://www.stapro.cz/ai-asistent-vykaznictvi-uz-pomaha-ve-23-ceskych-nemocnicich-vyzkousejte-ho-take-zdarma-jen-do-konce-srpna/
  note: 'STAPRO company article, 11 August 2026: "AI asistent výkaznictví" inside FONS Enterprise
    reads the patient documentation and discharge summary and proposes diagnoses and procedures;
    "Umělá inteligence projde požadované dokumenty, na základě pacientských dat navrhne možné
    diagnózy a člověk pak vše už jen zkontroluje." 23 hospitals in the pilot; 2,200 unique cases in
    July 2026; free until 31 August 2026, price thereafter not stated; no hospital named; no
    partner named. TWO USES, KEPT APART: as DEMAND it is 23 named-in-aggregate buyers adopting a
    coding tool; as LOCAL SUPPLY it puts STAPRO in locals[] at competes: direct — and EARLY for
    this product, because the assistant is a 2026 pilot however old the company. It backs no
    money: a free pilot is not a budget.'
  date: '2026-08-11'
  dims: [demand]
- type: news
  name: "AKESO — a private hospital group pilots AI case-grouping from discharge summaries"
  gist: "the 80-percent pilot"
  why: "A private Czech hospital group reports piloting AI that reads discharge summaries, sets the primary and secondary diagnoses and assigns the insurer case group at about 80 percent accuracy — the same job, on the buyer's own initiative."
  url: https://www.zdravotnickydenik.cz/2026/04/jak-akeso-vyuziva-umelou-inteligenci/
  note: 'Zdravotnický deník, 2 April 2026, on the AKESO holding: among seven AI uses, "medical
    documentation processing and billing — determines primary/secondary diagnoses and assigns DRG
    classification from discharge summaries", pilot October 2025 to January 2026, 330 patients, 11
    physicians, DRG assignment accuracy about 80 percent; a pre-visit questionnaire is said to
    halve the doctor''s documentation time for basic history. NO VENDOR IS NAMED, so this is
    recorded as a buyer doing it for itself and not as a local player. Demand receipt: a third
    named institution, private and outside Brno, with the same problem.'
  date: '2026-04-02'
  dims: [demand]
- type: regulation
  name: "European Health Data Space — Regulation (EU) 2025/327, imaging and discharge reports from 2031"
  gist: "the 2031 report deadline"
  why: "The regulation makes medical imaging reports and hospital discharge reports exchangeable across the EU in a common format from 26 March 2031 — a dated end state that requires the report to exist as data, not prose."
  url: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en
  note: 'reg-ehds: Regulation (EU) 2025/327, in force 26 March 2025; general application 26
    March 2027; priority category 1 (patient summary, ePrescription, eDispensation) from 26 March
    2029; priority category 2 — medical imaging studies and related reports, laboratory results,
    discharge reports — from 26 March 2031 (Commission page, corroborated 2026-09-03 by Noerr and
    EY summaries). THE DATE ON THIS SOURCE IS THE 2031 MILESTONE, not the signal''s 2029 headline
    date, because the two categories this problem is about — imaging reports and discharge
    reports — are in the later group. More than 18 months out: deadline sub-score 1. Freshness
    comes from the September 2026 asks, not from here.'
  date: '2031-03-26'
  signal: reg-ehds
- type: regulation
  name: "Zákon 236/2025 Sb. — the Czech e-health act amendment in force since 1 January 2026"
  gist: "the standards now binding"
  why: "Since 1 January 2026 Czech providers must follow the health ministry's electronic-health standards, including a unified data standard — but the standards are deliberately lightly structured for now, with structured documentation planned for later."
  url: https://e-sbirka.gov.cz/sb/2025/236
  note: 'reg-mzd-236-2025-ezdrav / reg-ez-standardy-2026: amendment 236/2025 Sb. to the e-health
    act 325/2021 Sb., in force 1 January 2026 — providers must comply with ministry-issued
    electronic-health standards; national portal, core registries, shared health record and
    e-requests launched. Medical Tribune (Co se změní od ledna 2026) quotes the national e-health
    centre that the data standards "zatím se připravují v základní verzi, která umožní jejich
    výměnu, ale budou poměrně málo strukturovaná", structured documentation to follow; e-requests
    not mandatory from the start. The national discharge-report standard (NCEZ, Propouštěcí zpráva)
    stands at v1.0.2 of March 2023 with v2.0 scheduled for late 2025, and its page states no
    binding date. CONTEXT ONLY: no dated obligation to structure reports exists in Czech law yet,
    so this backs no urgency point and dims is empty.'
  date: '2026-01-01'
  signal: reg-mzd-236-2025-ezdrav
  dims: []
- type: subsidy
  name: "IROP call 79 — eHealth for transition regions, open to 2 December 2026 (~1.14bn CZK)"
  gist: "the open 1.14bn CZK call"
  why: "The open state eHealth grant call funds how hospitals keep their medical documentation so it can be exchanged, shared, stored and interpreted — up to 28M CZK per provider — and its list of eligible applicants names Masarykův onkologický ústav, the institute that wrote two of the three asks."
  url: https://irop.gov.cz/cs/vyzvy-2021-2027/vyzvy/79vyzvairop
  note: '79. výzva IROP — eHealth — SC 1.1 (PR), announced 26 October 2023; applications from
    28 November 2023; deadline extended by the change notice of 26 May 2026 (MMR-37627/2026-26)
    from 2 June 2026 to 2 December 2026, 14:00, because the allocation was unspent; projects
    complete by 31 December 2027. Allocation: 1,144,629,052 CZK ERDF plus 490,555,308 CZK state
    budget. Cap: 28M CZK of eligible expenditure per healthcare provider (5M CZK per ambulance
    service); no minimum. Regions: Středočeský, Jihočeský, Plzeňský, Vysočina, Jihomoravský.
    Named eligible applicants include Masarykův onkologický ústav, Úrazová nemocnice v Brně,
    Vojenská nemocnice Brno, Nemocnice Břeclav, Kyjov, Znojmo, Vyškov, Třebíč and about sixty
    others (call text PDF, read 2026-09-03). Purpose, from the call page: "zlepšení způsobu
    vedení zdravotnické dokumentace umožňující její interoperabilní výměnu, sdílení, bezpečné
    uložení a interpretaci". Companion calls 78 (less developed regions) and 80 exist and were
    not read. WHY MONEY 2 AND NOT 1: the call is OPEN, far above 5M CZK, funds documentation
    systems at the exact hospitals asking, and names the asker. WHAT IT IS NOT: it pays the
    hospital, not a vendor, no line in the change notice names structured reporting or coding,
    and the detailed activity list in the full call text was not read from the primary — the
    purpose sentence above was.'
  date: '2026-12-02'
  dims: [money]
- type: regulation
  name: "NCEZ — ministry requirements for IROP eHealth projects: imaging-report and discharge-report specifications"
  gist: "the report specifications"
  why: "The national e-health centre's requirements page for those grant projects lists the functional specifications a funded hospital must be able to work with: the discharge report, the laboratory report, the imaging-examination report and the patient summary."
  url: https://ncez.mzcr.cz/cs/pozadavky-mz-pro-vyzvy-irop-ehealth-npo-interoperabilita-ii/pozadavky-mz-pro-vyzvy-irop-ehealth-npo
  note: 'Národní centrum elektronického zdravotnictví, "Požadavky MZ pro výzvy IROP eHealth a NPO
    Interoperabilita II", read 2026-09-03: lists "Souhrn specifikace Propouštěcí zprávy v1.0.0",
    "Souhrn specifikace zprávy z laboratorního vyšetření v1.0.0", "Funkční specifikace zpráva z
    obrazového vyšetření v1.0.0" and "Funkční specifikace — Pacientský souhrn v2.1"; states
    "Poskytovatelé zdravotních služeb musí být schopni správné interpretace výsledků" and that
    results are to be recorded and passed on using standardised code lists. Undated page ("stránky
    se průběžně připravují"); no HL7 FHIR profile named. Dated here at the read date. CONTEXT: it
    ties the grant in S8 to the two report types in S1 and S3; it carries no deadline and backs no
    score, dims empty.'
  date: '2026-09-03'
  dims: []
- type: arbitrage
  name: "Smart Reporting (Jacobian) — EUR 23M Series C for structured reporting, Munich"
  gist: "the German structured-reporting company"
  why: "A Munich company founded by radiologists in 2014 sells structured, machine-readable radiology and pathology reporting to more than 16,000 physicians in over 90 countries, raised a EUR 23M Series C in April 2024 and is distributed by Siemens Healthineers, GE Healthcare and Canon."
  url: https://tvm-capital.com/tvm-capital-life-science-leads-e23-million-series-c-financing-round-for-medical-reporting-technology-pioneer-smart-reporting/
  note: 'TVM Capital Life Science release, 22 April 2024: EUR 23M Series C led by TVM with Bayern
    Kapital and existing investors; founded 2014, Munich; "over 16,000 physicians across more than
    90 countries"; distribution partners Siemens Healthineers, GE Healthcare, Canon; "a fully
    voice-controlled and data-driven documentation solution for doctors that forms the basis for
    workflow automation and machine-readable data". Company release of 16 October 2025
    (jacobian.com): definitive agreement to acquire Fluency for Imaging and rename to Jacobian,
    HQ Munich and Pittsburgh, over 80 million exams a year combined, ranked first in Australia and
    second in the US and Canada. smart-reporting.com now redirects to jacobian.com, which is the
    comps URL. Passes the established test on Series C and twelve years of selling; Germany is the
    CEE-adjacent market that carries proof rung 3.'
  date: '2024-04-22'
- type: arbitrage
  name: "Rad AI — USD 60M Series C for AI-drafted radiology reports, San Francisco"
  gist: "the US report-drafting company"
  why: "A radiologist-founded US company whose AI drafts the impression and, since 2025, the whole radiology report from the dictation, funded at Series C in January 2025 and used daily by thousands of radiologists at practices covering nearly half of US imaging."
  url: https://www.prnewswire.com/news-releases/rad-ai-closes-60m-series-c-to-further-solidify-leadership-in-healthcare-generative-ai-302363999.html
  note: 'PRNewswire, 30 January 2025: USD 60M Series C led by Transformation Capital at a USD
    525M valuation; Rad AI Reporting "reducing dictated words by up to 90 percent"; "thousands of
    radiologists every day"; practices accounting for "nearly 50% of all medical imaging done in the
    US"; Strategic Radiology and Yale New Haven Health named; USD 8M extension from four health
    systems in May 2025. Founded February 2018, San Francisco, by Dr Jeff Chang and Doktor Gurson
    (Contrary Research profile, read 2026-09-03), which also names Advocate Health, Memorial
    Hermann, Corewell Health and Atlantic Health System as customers. Passes the established test on
    Series C and eight years of selling; the US is the second market for rung 3.'
  date: '2025-01-30'
- type: arbitrage
  name: "ID Berlin — ID DIACOS coding software in more than 1,200 hospitals"
  gist: "the German coding incumbent"
  why: "A Berlin company trading since 1985 whose coding software, with plausibility checks and rule-based code suggestions, runs in more than 1,200 hospitals in Germany, Austria and Switzerland — what the coding half looks like once it is an incumbent."
  url: https://www.id-berlin.de/en/products/codierung/id-diacos/
  note: 'ID Information und Dokumentation im Gesundheitswesen GmbH & Co. KGaA, Platz vor dem
    Neuen Tor 2, Berlin. Company product page, read 2026-09-03: "more than 1,200 hospitals" in
    Germany, Switzerland and Austria; determines fees directly in G-DRG, SWISS-DRG, EBM; German,
    English, French, Italian. Founding "seit 1985" from the it-dock.de vendor profile, read the same
    day; the company site itself states no founding year, and no customer is named on either page.
    Passes the established test on the public customer count and four decades of selling; the
    Slovenian and Luxembourg deployments a reseller page mentions are not recorded as markets
    because the company site does not state them.'
  date: '2026-09-03'
- type: arbitrage
  name: "Tiplu — MOMO, AI-assisted coding in more than 80 German hospitals since 2016"
  gist: "the German AI-coding entrant"
  why: "A Hamburg company founded in 2016 whose MOMO software proposes ICD and OPS codes from operative and discharge documents by semantic search and machine learning, in more than 80 hospitals including Charité and the Schleswig-Holstein university hospital — the entrant-shaped comparable."
  url: https://tiplu.de/produkte/momo/
  note: 'tiplu.de product page, read 2026-09-03: "KI-gestützte Komplettlösung für das operative
    Medizincontrolling", coding proposals in ICD-10 and OPS for DRG and PEPP; listed clients UKSH,
    RegioMed Kliniken, Klinikum Lüneburg, Charité, Schön Klinik, BG Kliniken, Universität
    Heidelberg, Universität Essen; HQ Karnapp 25, Hamburg. medconweb.de (updated 29 August 2023):
    "MOMO wird aktuell in über 80 Krankenhäusern eingesetzt", "2016 gegründeter Softwareanbieter".
    Fully automated primary coding was a project with Carl-Thiem-Klinikum from 2021 (tiplu.de
    release). Passes the established test on named customers and ten years of selling.'
  date: '2026-09-03'
- type: arbitrage
  name: "CodaMetrix — USD 40M Series B for autonomous coding, Boston"
  gist: "the autonomous-coding company"
  why: "A Boston company founded in 2019 with Mass General Brigham that codes radiology, pathology and surgery autonomously for Mass General Brigham, Yale Medicine, Mount Sinai and Henry Ford, reporting a 60 percent cut in coding cost and 70 percent fewer denials."
  url: https://www.codametrix.com/resources/codametrix-announces-40m-series-b-financing
  note: 'Company release, 12 March 2024: USD 40M Series B led by Transformation Capital, with
    SignalFire and Frist Cressey Ventures; founded 2019, built in partnership with Mass General
    Brigham, 399 Boylston St, Boston; customers Mass General Brigham, University of Colorado
    Medicine, Mount Sinai Health System, Yale Medicine, Henry Ford Health, University of Miami
    Health System; "60% reduction in coding costs, 70% reduction in claims denials, a 5-week
    acceleration in time to cash". Epic Toolbox listing August 2024. Cited as proof; not in comps[]
    to keep the ledger at four, since Rad AI already carries the US limb of rung 3.'
  date: '2024-03-12'
- type: arbitrage
  name: "Arintra — USD 21M Series A for autonomous medical coding"
  gist: "the YC coding company"
  why: "A Y Combinator company that raised a USD 21M Series A in August 2025 for autonomous coding integrated with Epic and Athena, with Mercyhealth and Reid Health as customers — a third US coding company funded inside eighteen months."
  url: https://www.arintra.com/resources/press-release/arintra-raises-21m-series-a-to-expand-beyond-autonomous-medical-coding-and-build-the-future-of-healthcare-revenue-assurance
  note: 'yc-arintra (YC W22, "Medical coding automation"). Company release, 12 August 2025: USD
    21M Series A led by Peak XV Partners with Endeavor Health Ventures, Y Combinator, Counterpart
    Ventures, Spider Capital and Ten13; founders Preeti Bhargava and Nitesh Shroff; San Francisco
    and Austin; customers Mercyhealth and Reid Health; "processed over a billion dollars in
    healthcare charges"; native Epic and Athena integration. Founding year not stated in the
    release, so not in comps[]. Cited as proof, alongside S14, that the coding half is a funded
    category in the US and not one company.'
  date: '2025-08-12'
  signal: yc-arintra
- type: gap-check
  name: "Czech clinical-documentation supply — three hospital-system vendors moving, nobody established on it"
  gist: "the contested Czech field"
  why: "A Czech-language sweep of who sells this here: Stapro, ICZ and Medicalc each sell or pilot one half of it inside their hospital systems, none with a paying named customer for it; Datlowe, NEWTON Dictate and Carebot sell something adjacent; no vendor of structured radiology templates was found."
  url: https://www.iczgroup.com/podpora-vykazovani-zdravotni-pece/
  note: 'Sweep 2026-09-03, method: Czech-language descriptive web search plus a read of each
    vendor''s own page, ARES for identities and founding dates, the funded ledger and the
    contracts-register lookup. DIRECT, ALL EARLY FOR THIS PRODUCT. (1) STAPRO, IČO 13583531,
    trading since 1990: "AI asistent výkaznictví" in FONS Enterprise, 23 hospitals on a free pilot,
    2,200 cases in July 2026, price after 31 August 2026 unpublished (stapro.cz, 11 August 2026 —
    S4). since 2026. (2) ICZ a.s., IČO 25145444, incorporated 21 July 1997: "Asistent vykazování
    AV(D)" — "Nástroj pro efektivní kódování využívající modely strojového učení pro analýzu
    propouštěcí zprávy", developed with doc. Pavel Král''s team at FAV ZČU, EU co-financed, product
    page dated October 2023 (iczgroup.com/podpora-vykazovani-zdravotni-pece, read 2026-09-03), no
    customer or count on the page; vedavyzkum.cz, 19 November 2023: pilot at FN Brno "being
    prepared", "desítky procent" productivity claimed. since 2023 — three years, so ONE NAMED
    PAYING HOSPITAL WOULD MAKE IT ESTABLISHED AND TAKE THE SPACE; none is published. (3) Medicalc
    software s.r.o., IČO 26350513, founded 2002, "více než 54 000 zdravotníků" daily, 100+
    facilities: Zdravotnický deník, 12 January 2026, director Jan Kupka — AI to "pořizovat
    nahrávkou strukturovanou zprávu z vizity, návštěvy ordinace, operace nebo pitvy" and to map
    code lists and build structured data from free text; the interview does not say the AI
    features are live anywhere. since 2026. ADJACENT, ESTABLISHED. (4) Datlowe, s.r.o., IČO
    02931737, incorporated 24 April 2014: HAIDI reads free-text documentation by machine for
    hospital-acquired infections; Roklen24, 3 January 2024: FN Brno, KNTB Zlín, Liberec, Frýdlant,
    Turnov added, 3,453 beds, "více než třetinu českých lůžek"; also five Krajská zdravotní
    hospitals and Trnava (insmart.cz). Infection surveillance, not reporting, coding or registries.
    (5) NEWTON Technologies, a.s., IČO 28479777, incorporated 27 October 2008: NEWTON Dictate,
    Czech speech-to-text with medical dictionaries into the hospital system; Technický týdeník, 7
    December 2015: 350+ healthcare licences, IKEM, VFN, FN Hradec Králové, FN Ostrava, Pardubice,
    Krajská zdravotní, Liberec, Kolín; free text, not structure. (6) Carebot s.r.o., IČO 10898263,
    incorporated 3 June 2021: certified AI reading chest X-rays; FocusOn, 14 March 2025, "50–60
    nemocnic", EUR 1.2M round (cc.cz). Reads the image, not the report. NOT VENDORS, NOT IN
    locals[]: AKESO (a buyer piloting for itself, S5) and ÚZIS (the state running its own AI on the
    cancer registry, S17). CONTRACTS REGISTER, distinct public payers by IČO: STAPRO 2 (MMN a.s.,
    Vsetínská nemocnice), ICZ a.s. 1 (Český statistický úřad), ICZ.HEA 07240091 1 (Nemocnice
    Břeclav), Datlowe 0, NEWTON 0, Carebot 0, Medicalc 0 — the machine limb helps nobody here.
    FUNDED LEDGER: no Czech entrant on clinical documentation, coding or medical text; the Czech
    health rows are Aireen, MediSearch, Upheal, Hedepy and the like. THE ABSENCE HALF, STATED
    WITHOUT A CLAIM: three query shapes on structured radiology reporting returned Medicalc''s
    radiology module, hospital patient pages, the NCEZ imaging-report specification and German
    literature, and no Czech vendor selling structured radiology templates as a product. NO
    ABSENCE IS ASSERTED from that; gap is 1 on the positive findings above, not 2 on this. POSITIVE
    CONTROLS, RECORDED HONESTLY: the in-market control PASSED — the descriptive query "umělá
    inteligence lékařská dokumentace vytěžování zpráv česká firma nemocnice 2026" surfaced Datlowe,
    a known Czech clinical-text vendor, unprompted, and the coding query surfaced STAPRO''s
    assistant unprompted; the register''s two standing controls MISSED on one shape each through
    this search tool — the PowerAuth query returned Monet+ and a PowerAuth slide deck but not
    wultra.com, and the smart-water-metering query returned OVAK, BVK, ČEVAK, Pokorný and ista but
    not Softlink. The method finds Czech health-IT vendors; it is not proven for every market, and
    that is one more reason the score rests on what was found rather than on what was not. NOT
    CHECKED AND NOT CLAIMED: ares by NACE, cz-saas-directories, startupjobs, app-stores,
    eshop-addon-marketplaces, zivnostensky-rejstrik, company-job-feed. WHAT MOVES THIS: a named
    paying hospital for ICZ''s AV(D) drops gap to 0 now; STAPRO''s and Medicalc''s products cannot
    pass the three-year limb before 2029 whatever they sell.'
  date: '2026-09-03'
  queries:
    - "strukturované radiologické nálezy software nemocnice český dodavatel"
    - "strukturovaný radiologický nález šablony RIS česká radiologie strukturovaný popis software"
    - "strukturovaný nález CT MR šablona software lékař radiologické oddělení česká firma nabízí"
    - "software kódování DRG vykazování výkonů pojišťovnám nemocnice umělá inteligence česká firma"
    - "grouper CZ-DRG software dodavatel nemocnice kódování hospitalizačních případů modul NIS"
    - "ICZ vykazovací asistent AV(D) automatické kódování diagnóz nemocnice nasazení 2025"
    - "umělá inteligence lékařská dokumentace vytěžování zpráv česká firma nemocnice 2026"
    - "automatické vytěžování onkologické dokumentace hlášení do Národního onkologického registru software umělá inteligence dokumentátor"
    - "Medicalc umělá inteligence standardizovaná dokumentace nemocniční informační systém AI asistent lékařská zpráva"
    - "Datlowe zpracování lékařské dokumentace NLP nemocnice"
    - "NEWTON Dictate Medical diktování lékařských zpráv rozpoznávání řeči nemocnice"
    - "Carebot umělá inteligence rentgen nemocnice CE certifikace česká firma"
    - "zabezpečení mobilního bankovnictví autentizace česká firma PowerAuth"
    - "chytré měření vody dálkové odečty vodoměrů česká firma systém pro vodárny"
  checked: [google-cz, own-funded-ledger, cz-contract-parties]
  expires: '2026-12-02'
- type: news
  name: "ÚZIS — AI on the cancer registry, 25.4M CZK to June 2026"
  gist: "the state's registry-side AI"
  why: "The state health-statistics institute is running a 25.4M CZK EU-funded project to June 2026 that uses AI to complete and validate cancer-registry reporting from the registry's own data and the paid-care register — the registry side of the problem, done by the state, leaving the hospital side open."
  url: https://www.uzis.cz/index.php?pg=o-nas--projekty&prid=37
  note: 'Ústav zdravotnických informací a statistiky ČR project "Zvýšení dostupnosti onkologické
    a další zdravotní péče prostřednictvím využití systémů automatického učení a umělé
    inteligence", ESF+ / OP Zaměstnanost plus, 1 July 2023 to 30 June 2026, 25,394,400 CZK.
    Activity KA1: AI methods to optimise National Oncology Register reporting using NOR and NRHZS
    data; KA2 cause-of-death validation; KA3 regional access; KA4 visualisation and training. It
    works from registry data, not from the hospital''s clinical record, which is what S2 asks to
    read. CONTEXT for First moves; dated at the project start; backs no score.'
  date: '2023-07-01'
  dims: []
created: '2026-09-03'
updated: '2026-09-03'
---

A Czech doctor writes a radiology finding or a discharge summary as free text. A coder reads it again to produce the codes the insurer pays on; a documentarian reads it a third time to fill the cancer registry [S1,S3].

Masarykův onkologický ústav, the Brno cancer institute, calls that extraction slow and demanding and asks for structured radiology reports written into the hospital system from smart templates [S1,S2]. The third challenge: a coding department spends hours transcribing discharge summaries by hand, and every omission is lost money [S3].

Why now: hospitals are already buying the coding half. The hospital-system vendor Stapro has an AI coding assistant in 23 hospitals — 2,200 cases in July, free until 31 August 2026 [S4]. AKESO (a private hospital group) piloted case-grouping from discharge summaries at 80 percent accuracy [S5]. Since 1 January 2026 providers must follow ministry e-health standards, still lightly structured [S7]. From 26 March 2031 the European Health Data Space makes imaging and discharge reports exchangeable across borders [S6].

Who pays: Czech hospitals, which pay for every report twice — the doctor's time to write it, then a coder's time to read it back into insurer codes [S3]. The institute is a named eligible applicant to IROP call 79 — the state's open eHealth grant call — funding hospital documentation systems up to 28M CZK per provider from a 1.14bn CZK pot until 2 December 2026 [S8]. The ministry's requirements for those projects name the imaging-report and discharge-report specifications [S9]. No source states what coding by hand costs a hospital.

Existing non-solutions: the coding half is contested, not empty. Stapro's assistant is a 2026 pilot [S4]. ICZ (a hospital-systems vendor) has offered AV(D), which reads a discharge report and proposes diagnoses to bill, since October 2023, naming no buyer [S16]. Medicalc says its system's AI turns a dictated ward round into a structured report [S16]. Nobody found sells structured radiology templates. Nearby: Datlowe reads Czech clinical text for infections across a third of hospital beds, NEWTON Dictate (dictation software) types findings as free text, Carebot reads chest X-rays [S16].

Solved elsewhere: both halves sell as products in Germany. Smart Reporting, now Jacobian (Munich, since 2014), sells structured radiology and pathology reporting to 16,000 physicians in 90 countries and raised €23M in 2024 [S10]. ID Berlin (a Berlin coding-software house, since 1985) codes in 1,200 hospitals across Germany, Austria and Switzerland [S12]; Tiplu's MOMO (an AI coder, since 2016) in 80, Charité among them [S13]. In the US, Rad AI raised $60M in 2025 to draft radiology reports for practices covering half of American imaging [S11]; CodaMetrix codes for Mass General Brigham and Yale [S14], Arintra raised $21M in 2025 [S15].

## First moves

1. Build the report, not the coder. Structured templates at the point of writing are the half nobody in Czechia sells, and a report born structured makes the coding step at Stapro, ICZ and Medicalc a formality [S4,S16]. Start with radiology: the institute that asked will judge it on 27–29 November 2026 [S1].
2. Sell into the open grant window. Masarykův onkologický ústav and some seventy other providers in five regions can apply to IROP call 79 until 2 December 2026, up to 28M CZK each, projects finished by the end of 2027 [S8]. Build to the ministry's own imaging-report and discharge-report specifications, which it lists as requirements for those projects [S9].
3. Price against a free pilot. Stapro's assistant costs 23 hospitals nothing until 31 August 2026 and its price after that is unpublished [S4]; ICZ's has no named buyer after three years [S16]. Coding alone will not carry a company here — the structured report and the registry feed have to.
4. Follow Tiplu's route, not ID Berlin's. Tiplu started in 2016 with pilot hospitals and reached 80, Charité included [S13]; ID Berlin needed four decades to reach 1,200 [S12]. The cancer institute that wrote the challenge is the pilot.
5. Read the registry side before building extraction. The state health-statistics institute is spending 25.4M CZK to 30 June 2026 on AI that completes the cancer registry from the registry's own data [S17]; the hospital side — pulling the facts out of the record — is what the institute still asks for [S2].

## Revisions

2026-09-03 · record created — Minted from the first asks ledger: three owner-set challenges at Hack jak Brno 2026, two from Masarykův onkologický ústav and one from JINAG, each cited as demand only [S1,S2,S3]. Demand 2 on those plus Stapro's 23-hospital pilot and AKESO's [S4,S5]. Proof 3 on established sellers in Germany and the US [S10,S11,S12,S13]. Money 2 on the open IROP 79 call, which names the asking institute as eligible [S8]. Urgency 2: the 2031 European deadline for imaging and discharge reports, plus sources fresher than 90 days [S6]. Gap 1: Stapro, ICZ and Medicalc each sell or pilot one half of this inside their hospital systems and none is established for it; six local players recorded, three of them adjacent, and the standing positive controls that missed are written down rather than hidden [S16].
