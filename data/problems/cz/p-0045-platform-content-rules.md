---
id: p-0045
region: cz
title: 'Czech marketplaces and forums must tell users why each post was removed. A bill would let the regulator fine them up to 6% of turnover.'
brief: 'Czech marketplaces and forums must handle reports of illegal posts and explain each removal to the user [S1]. Nobody can fine them yet [S4], but a bill awaiting its last lower-house vote would allow fines up to 6% of turnover [S2,S3].'
solution: 'Build Czech-language software that logs reports of illegal posts, sends users the reason for each removal, files it in the EU database and writes the yearly report, as 2 companies already do in 2 other countries.'
good_for: 'Developers who know content moderation and can sell to Czech marketplaces and forums.'
price_search: 'Ask the Czech law firms under Market gap what they charge to set up report handling, removal reasons and the yearly report for one platform, or ask the person who handles reported posts at a mid-size Czech marketplace what the work costs in staff time; the public contracts register holds no such contract because the buyers are private.'
category: legal-compliance
geo: CZ-national
score: 8
scores:
  proof: 2
  money: 0
  urgency: 3
  demand: 1
  gap: 2
status: candidate
entry:
  level: moderate
  buyer: large-firms
  permission: none
  incumbents: open
  integration: national-system
  money: bootstrap
  why: 'Easier: no licence is needed to sell the software, 2 firms abroad already sell the same thing, and no Czech firm sells it yet. Harder: the software must file each decision with an EU database, the buyers are mid-size and large platforms, and until the Czech bill passes nobody can fine them for skipping the work.'
comps:
- name: Tremau
  url: https://tremau.com/
  geo: FR
  since: 2021
  traction: 'Sells Nima, a platform that runs report handling, removal reasons and yearly transparency
    reporting under the EU rules for online platforms. Named customers include Bluesky, Ko-Fi,
    Eventbrite and Pinterest; raised EUR 3M in April 2025 and reports profit since 2024 (EU-Startups,
    2025). Founded 2021 (same source).'
  signal: fr-tremau
- name: Checkstep
  url: https://www.checkstep.com/
  geo: GB
  since: 2020
  traction: 'Sells content-moderation software with tools for handling reports of illegal content and
    one-click yearly transparency reports under the EU rules (company site, 2026). Named customers
    include Trustpilot, JustGiving, Daily Mail and MoneySavingExpert; handles more than 60 million
    pieces of content a month; GBP 3M seed round in April 2026 (UK Tech News, 2026). Founded in 2020
    (company site).'
locals:
- name: elv.ai
  url: https://elv.ai/
  competes: adjacent
  maturity: early
  evidence: 'Sells comment moderation to media and institutions, with AI and human moderators; Prima
    television and the publisher Economia are named as its Czech clients. Based in Slovakia, with no
    Czech company of that name in the state business register. It moderates discussions for its
    clients, and does not run the report handling, removal reasons, EU filings and yearly reports a
    platform owes [S11].'
- name: ARROWS advokátní kancelář
  url: https://arws.cz/novinky-v-arrows/narizeni-o-digitalnich-sluzbach-cast-druha-povinnosti-a-sankce
  ico: '06717586'
  since: 2024
  competes: adjacent
  maturity: early
  evidence: 'A Prague law firm that sells legal advice and publishes an explainer of what the EU rules
    require of platforms and hosting services and of the fines, first posted in April 2024 and
    updated in September 2026. It offers no software that runs the steps each day [S11].'
- name: ROWAN LEGAL
  url: https://rowan.legal/aktualne/koho-se-tyka-narizeni-o-digitalnich-sluzbach-dsa-a-jake-jsou-jejich-nove-povinnosti/
  ico: '28468414'
  competes: adjacent
  maturity: early
  evidence: 'A Prague law firm that sells legal advice and publishes a guide to who the EU rules cover
    and what they require. The page offers no software and names no client for this work [S11].'
- name: SEDLAKOVA LEGAL
  url: https://www.sedlakovalegal.cz/akt-digitalni-sluzby
  ico: '05669871'
  competes: adjacent
  maturity: early
  evidence: 'A Brno law firm for technology firms that sells advice on the EU rules to apps, software
    services and web hosts: their terms, the yearly moderation report and the contact point. It
    sells advice and documents, not software that does the daily handling [S11].'
- name: Cisek, advokátní kancelář
  url: https://www.akcisek.cz/blog/dsa-a-mechanismy-moderace-obsahu
  ico: '09761098'
  since: 2024
  competes: adjacent
  maturity: early
  evidence: 'A Brno law firm that sells legal services on a monthly plan, runs a blog series on the
    EU rules from August 2024 and offers a free guide to them. The price it lists is for general
    legal support, not for this work, and it sells no software [S11].'
- name: Feichtinger Žídek Fyrbach advokáti
  url: https://www.akfz.cz/blog/dsa
  ico: '29304873'
  since: 2023
  competes: adjacent
  maturity: early
  evidence: 'A Brno and České Budějovice law firm that sells legal advice, with an explainer of the
    EU rules from March 2023 and a free checklist of the duties for apps, software services and web
    hosts. It offers advice, not software that runs the steps [S11].'
- name: Advokátní kancelář Šmarda
  url: https://www.aksmarda.cz/rady-a-tipy/nove-pravidla-pro-online-prostredi-narizeni-o-digitalnich-sluzbach-dsa/
  competes: adjacent
  maturity: early
  evidence: 'An Olomouc and Prague law firm that sells legal advice and publishes an explainer of the
    EU rules and whom they cover. It offers no software for the daily handling [S11].'
- name: PwC Česká republika
  url: https://ctu.gov.cz/sites/default/files/obsah/soubory-ke-stazeni/%C4%8CT%C3%9A_PwC_Studie_DSA_.pdf
  since: 2024
  competes: adjacent
  maturity: early
  evidence: 'A consultancy that wrote the regulator''s 2024 study of which Czech firms the EU rules
    cover. It sold that study to the regulator, the other side of the counter from the platforms,
    and no product for platforms was found [S6,S11].'
sources:
- type: regulation
  name: 'Regulation (EU) 2022/2065 — the Digital Services Act'
  gist: 'the EU rules and their duties'
  why: 'The EU law on how online platforms handle illegal content and complaints: every host must take reports and explain each removal, and platforms that are not small firms must also run a complaint system, file every removal decision in a public EU database and publish a yearly report.'
  url: https://eur-lex.europa.eu/eli/reg/2022/2065/oj
  note: 'reg-dsa-cz (ledger signal on the Czech side). EUR-Lex CELEX 32022R2065 read 2026-09-19.
    Art 93(2): "This Regulation shall apply from 17 February 2024." Art 16(1): providers of hosting
    services "shall put mechanisms in place to allow any individual or entity to notify them" of
    illegal content. Art 17(1): hosting providers "shall provide a clear and specific statement of
    reasons to any affected recipients" for restrictions incl. removal. Art 19(1): Section 3 (Arts
    20-28), except Art 24(3), does not apply to online platforms that are micro or small enterprises.
    Art 20(1): internal complaint-handling "electronically and free of charge", for at least six
    months after the decision. Art 24(5): platforms "shall, without undue delay, submit to the
    Commission the decisions and the statements of reasons" for a public machine-readable database.
    Art 15(1): yearly transparency reports; Art 15(2): not for micro or small enterprises. Art 52(3):
    Member States set maximum fines at "6 % of the annual worldwide turnover".'
  date: '2024-02-17'
  signal: reg-dsa-cz
- type: regulation
  name: 'Sněmovní tisk 69 — the Czech digital economy bill'
  gist: 'the bill and its status'
  why: 'The Czech bill that gives the telecoms regulator its powers under the EU rules: sent to the lower house in December 2025, past its second reading on 1 July 2026, and able to go to its final lower-house vote from 5 September 2026; the Senate and the president come after.'
  url: https://www.psp.cz/sqw/historie.sqw?o=10&t=69
  note: 'psp.cz bill history read 2026-09-19 ("Stav projednávání ke dni: 19. září 2026"): "Vláda
    předložila sněmovně návrh zákona 12. 12. 2025", distributed as tisk 69/0 on 15 Dec 2025; first
    reading 10 Mar 2026; committee resolutions 69/1-69/7 (Mar-Jun 2026); second reading "1. 7. 2026
    na 24. schůzi"; guarantee committee statement 69/9 delivered 4 Sep 2026; "Další projednávání možné
    od 5. 9. 2026 11:06". No third-reading entry on the page, so it awaits the third reading.'
  date: '2026-09-05'
- type: regulation
  name: 'Sněmovní tisk 69/0 — text of the bill'
  gist: 'the offences and the 6% fine'
  why: 'The bill as sent to parliament: a host that sets up no reporting channel or gives a user no reason for a removal commits an offence, as does a platform that files no decisions with the EU; both can be fined up to 6% of worldwide turnover, and the law takes effect 15 days after publication.'
  url: https://www.psp.cz/sqw/text/orig2.sqw?idd=266214
  note: 'Tisk 69/0 PDF (t006900.pdf, 137 pages) read 2026-09-19. § 51 "Přestupky poskytovatelů
    hostingových služeb": offences incl. "a) nezavede mechanismus oznamování a přijímání opatření
    podle čl. 16" and "e) neposkytne dotčenému příjemci zprostředkovatelské služby odůvodnění jemu
    uloženého omezení podle čl. 17"; "(2) Za přestupek podle odstavce 1 lze uložit pokutu do výše 6 %
    z ročního celosvětového obratu". Online-platform offences incl. "l) nepředloží Komisi odůvodněné
    rozhodnutí o omezení v rozporu s čl. 24 odst. 5" and "k) nesplní uveřejňovací povinnost podle čl.
    24 odst. 1 nebo 2". § 75: "Tento zákon nabývá účinnosti patnáctým dnem po jeho vyhlášení", with
    listed exceptions. The approved text may change at third reading; the 6% cap is the DSA''s own
    Art 52(3) maximum (S1).'
  date: '2025-12-15'
- type: complaint
  name: 'Czech Telecommunication Office — report on the EU platform rules, 2025'
  gist: 'complaints, questions, no powers'
  why: 'The regulator''s yearly report: 98 complaints of breaches in 2025, 15 about providers based in Czechia and none leading to an investigation; 123 written questions, some on the EU database and yearly reports; no inspections or fines possible without the Czech law; 13 staff on these rules.'
  url: https://ctu.gov.cz/sites/default/files/obsah/stranky/522420/soubory/vyrocni_zprava_dsa.pdf
  note: 'ČTÚ "Výroční zpráva ... podle článku 55 nařízení DSA Za rok 2025", read 2026-09-19; dated
    by the PDF creation date (24 Mar 2026); ČTÚ press release on its annual reports 21 May 2026.
    "V roce 2025 ČTÚ vyřídil celkem 98 stížností ... Z toho 15 stížností se týkalo poskytovatelů
    služeb usazených v ČR"; "Převážná část stížností se týkala nepřiměřené či nedostatečně odůvodněné
    blokace uživatelských účtů ze strany poskytovatelů velmi velkých online platforem"; "V roce 2025
    nevedly žádné stížnosti k zahájení formálního šetření"; "nebylo možné ... provádět kontroly nebo
    ukládat sankce"; "vyřídil 123 písemných dotazů" incl. "registrací do databází transparentnosti,
    zpráv o transparentnosti"; the DSA unit "mělo na konci roku 2025 13 zaměstnanců"; outlook: "Po
    přijetí legislativy bude možné zahájit certifikaci subjektů a dozorovou činnost"; the complaints''
    "narůstající počet" noted in the conclusion.'
  date: '2026-03-24'
  dims: [demand]
- type: complaint
  name: 'Czech Telecommunication Office — report on the EU platform rules, 2024'
  gist: 'the first year''s complaints'
  why: 'The regulator''s first yearly report: 25 complaints of breaches in 2024, none leading to proceedings because it lacked the powers; 45 written questions; it helped platforms register with the EU database.'
  url: https://ctu.gov.cz/sites/default/files/obsah/stranky/522421/soubory/vyrocni_zprava_koordinatora_dig._sluzeb_cz.pdf
  note: 'ČTÚ annual DSA report for 1 Jan-31 Dec 2024, read 2026-09-19; dated by the PDF creation date
    (15 Apr 2025). "ČTÚ přijal 25 stížností na porušení nařízení DSA, z toho 8 postoupil do Irska.
    Žádná stížnost nevedla k formálnímu řízení kvůli absenci zákonného zmocnění"; "vyřídil 45
    písemných dotazů"; "ČTÚ pomáhal online platformám s registrací do databáze transparentnosti";
    "devět zaměstnanců na plný úvazek" at end-2024.'
  date: '2025-04-15'
  dims: [demand]
- type: statistic
  name: 'Czech Telecommunication Office — study of the firms the rules cover'
  gist: 'who the rules cover in Czechia'
  why: 'A 2024 study written for the regulator: 2,659 providers in Czechia fall under the EU rules, including 564 hosting services, 182 online platforms and 76 online marketplaces; 17 of the platforms and 27 of the marketplaces are medium-sized or large firms.'
  url: https://ctu.gov.cz/sites/default/files/obsah/soubory-ke-stazeni/%C4%8CT%C3%9A_PwC_Studie_DSA_.pdf
  note: 'PwC, "Studie poskytovatelů zprostředkovatelských služeb podle Nařízení DSA", for ČTÚ,
    contract CTU/2024_0032, dated 25 Oct 2024, read 2026-09-19 (NEN N006-24-V00011790). Hosting
    (not platforms or marketplaces): 564. Online platforms 182: large 8, medium 9, small and micro
    120, not stated 45. Online marketplaces 76: large 7, medium 20, small and micro 35, not stated
    14. Total relevant providers 2,659. The "44 medium or large" is our sum of 8+9+7+20; "59 with no
    size on record" is 45+14. Two very large platforms (XVideos, XNXX operators) are established in
    Czechia and supervised by the Commission.'
  date: '2024-10-25'
- type: news
  name: 'European Commission — Czechia referred to the EU Court of Justice'
  gist: 'the state sued for the missing law'
  why: 'The Commission decided to take Czechia to the EU Court of Justice for failing to give its regulator the powers the EU rules require and to set the fines, both due by 17 February 2024.'
  url: https://digital-strategy.ec.europa.eu/en/news/commission-decides-refer-czechia-spain-cyprus-poland-and-portugal-court-justice-european-union-due
  note: 'EC news, 7 May 2025, read 2026-09-19 via fetch: "Although Czechia, Cyprus, Spain and
    Portugal each designated a DSC, they have failed to entrust them with the necessary powers";
    Czechia also failed to lay down rules on penalties; "The DSA required Member States to designate
    and empower a DSC by 17 February 2024". A search result (changeflow.com) names the case as
    C-168/26; not read at the Court. Cites urgency only.'
  date: '2025-05-07'
  dims: [urgency]
- type: statistic
  name: 'EU transparency database of removal decisions'
  gist: 'which Czech services file'
  why: 'The EU''s public database of platforms'' removal decisions: of 372 services listed, 22 are run from Czechia, and 16 of those filed no decision in the six months the search covers.'
  url: https://transparency.dsa.ec.europa.eu/statement
  note: 'Read 2026-09-19. The statement search covers "the last 6 months of data submitted"; its
    platform filter lists 372 services. Czech-run services identified BY NAME by us (our reading, not
    a field in the database), with the count of statements of reasons for each platform_id:
    Zboží.cz 70,720; Rajče 4,915; Živě.cz 3,746; eMimino.cz 943; e15 270; Mimibazar 1; and 0 for
    Atmoskop, Benu (Poradna), Blog.iDNES.cz, Heureka Group, hotely.cz, jobs.cz, Letákomat, MATY,
    Mimiaukce, Najisto.cz, Práce.cz, Práce za rohem, Printables.com, Seduo, Teamio, Vareni.cz.
    Excluded as not clearly Czech: Kimbino, Profesia.cz. Filing nothing can also mean a service
    removed nothing; the database does not say which. A 2026-09-19 pre-read by an earlier pass gave
    Zboží.cz 70,879 and the same zeros; the window moves daily.'
  date: '2026-09-19'
- type: arbitrage
  name: 'Tremau'
  gist: 'French platform-rules software'
  why: 'A Paris company whose platform runs report handling, removal reasons and transparency reporting under the EU rules for online platforms, profitable since 2024.'
  url: https://www.eu-startups.com/2025/04/tremau-secures-e3-million-to-scale-its-ai-powered-trust-safety-platform/
  note: 'fr-tremau (EU-Startups, 2025-04-04): EUR 3M round; Nima runs notice-and-action, statements
    of reasons and transparency reporting; names Bluesky, Ko-Fi, Eventbrite and Pinterest as clients;
    profitable since 2024; founded 2021. tremau.com read 2026-09-19: "We build Nima, the content
    moderation platform that protects online platforms and their users"; logos incl. Alibaba.com,
    AliExpress, Bluesky, Eventbrite, Pinterest, Ko-fi.'
  date: '2025-04-04'
  signal: fr-tremau
- type: arbitrage
  name: 'Checkstep — tools for the EU platform rules'
  gist: 'British report-handling software'
  why: 'A London company that sells content-moderation software with tools for handling reports of illegal content and producing the yearly transparency report, used by platforms such as Trustpilot.'
  url: https://www.checkstep.com/dsa-tools-compliance/
  note: 'Read 2026-09-19 via fetch: Transparency Reports "generate a Transparency report for your
    European users instantly"; Notice and Action Management "streamline the process of reviewing
    notices, taking appropriate actions, and documenting these steps"; no statement-of-reasons or
    database-filing feature named on this page. UK Tech News, 28 Apr 2026: GBP 3M seed led by Alea
    Capital Partners; "customers including Trustpilot, JustGiving, Daily Mail, MoneySavingExpert";
    "more than 60 million pieces of content each month". checkstep.com seed post: "Checkstep was
    founded in 2020". A USD 99 and 499 monthly price reported by review sites could not be read at
    source (TrustRadius returned 403) and is not used.'
  date: '2026-04-28'
- type: gap-check
  name: 'Czech check — who sells this work here'
  gist: 'the Czech field, searched'
  why: 'Czech-language web search, the state business register, our own funding ledger and the Czech e-shop add-on catalogues: nobody in Czechia sells software that runs these steps; law firms sell advice on them, a Slovak firm moderates comments, and a consultancy mapped the market for the regulator.'
  url: https://search.seznam.cz/?q=DSA%20compliance%20slu%C5%BEby%20pro%20online%20platformy%20a%20tr%C5%BEi%C5%A1t%C4%9B
  note: 'Gap check 2026-09-19. SURFACES: Seznam web search (search.seznam.cz, fetched directly, top
    10-12 organic results per query) and the agent web-search tool, both Czech-language; the checked
    vocabulary has no Seznam token, so both are recorded as google-cz, which neither is. ARES name
    search; data/signals/funded; data/lookup/cz-eshop-addons.jsonl (grep DSA / digitálních služ /
    nezákonného obsahu / moderac: one hit, a Shoptet page builder, irrelevant). FOUND, ADJACENT:
    elv.ai (SK; CzechCrunch 15 Jan 2024, cc.cz: AI plus human comment moderation, EUR 500k seed,
    Czech clients Prima and Economia; ARES "elv.ai"/"Elv ai" 0 hits; also round-elv-ai on our
    ledger). Law firms selling DSA advice, pages read: ARROWS advokátní kancelář s.r.o. (06717586,
    ARES 2018-01-01; article 25 Apr 2024, updated 15 Sep 2026), ROWAN LEGAL (28468414, ARES
    2008-10-01), SEDLAKOVA LEGAL s.r.o. (05669871, ARES 2017-01-01; also sedlakovalegal.cz/cs/
    moderovani-obsahu-DSA), Cisek, advokátní kancelář s.r.o. (09761098, ARES 2021-01-01; blog 11 Aug
    2024; e-book "Praktický průvodce DSA"; monthly plans from 14,700 CZK are general legal support),
    Feichtinger Žídek Fyrbach advokáti s.r.o. (29304873; blog 20 Mar 2023), AK Šmarda (IČO not on
    the pages read). None of the six IČOs has a public buyer in cz-contract-parties.jsonl. PwC wrote
    the ČTÚ study (S6); the contracting entity was not resolved (NEN page not readable), so no IČO.
    SEEN, NOT RECORDED AS PLAYERS: TrollWall AI (SK, round-trollwall-ai; social-profile moderation;
    no Czech client found; ARES 0); eLegal, gdpr.cz, muj-pravnik.cz, pravopropodnikatele.cz (DSA
    explainers in search results, pages not read); Religis (Ostrava e-shop agency, a DSA blog post,
    no DSA service offered); Orange Academy (training courses, article only); Replient and Textie
    (AI comment and text tools, no DSA workflow); IRESOFT, Edaxo, Modrý koník, Muziker, eyerim,
    3Dfind, eMimino (their OWN DSA pages as obligated services, i.e. buyers not sellers). No Czech
    price for this work found. POSITIVE CONTROLS: (1) in-market — Seznam descriptive query "moderace
    komentářů pro média umělá inteligence služba" surfaced elv.ai (businessinfo.cz article, rank 8)
    without naming it: PASSED. (2) register control via the web-search tool — "TMS systém řízení
    přepravy tendrování dopravců česká firma" surfaced Ringil (ringil.com/funkce/sprava-tendru and
    its LinkedIn article): PASSED. (3) The same Ringil query on Seznam, and the Wultra query
    "zabezpečení mobilního bankovnictví a ověřování plateb česká firma" on Seznam, both MISSED in
    the top 10 (Schaeffler, SAP and directories; banks): Seznam''s recall for small B2B vendors on
    descriptive queries is weaker, recorded rather than hidden. Gap 2 rests on 17 Czech queries
    across two engines finding law firms, a moderation service and obligated platforms, and no
    seller of the software.'
  date: '2026-09-19'
  queries:
    - "moderace komentářů pro média umělá inteligence služba"
    - "nařízení o digitálních službách DSA implementace pro online platformy advokátní kancelář"
    - "DSA compliance služby pro online platformy a tržiště"
    - "software pro vyřizování oznámení o nezákonném obsahu DSA"
    - "odůvodnění omezení obsahu databáze transparentnosti DSA nástroj"
    - "moderace obsahu pro inzertní portály a diskuzní fóra služba"
    - "outsourcing moderace uživatelského obsahu česká firma"
    - "vypracování zprávy o transparentnosti podle DSA pro platformu"
    - "systém pro vyřizování stížností uživatelů online platformy podle DSA"
    - "DSA balíček pro e-shopy a tržiště obchodní podmínky kontaktní místo"
    - "audit souladu s nařízením o digitálních službách poradenství"
    - "advokátní kancelář služby DSA nastavení postupů moderace obsahu pro platformy"
    - "pomůžeme vám splnit povinnosti podle nařízení o digitálních službách"
    - "trust and safety moderátoři obsahu agentura Praha"
    - "nástroj pro hlášení nezákonného obsahu na webu plugin DSA"
    - "česká firma software pro moderaci obsahu a plnění DSA pro online platformy odůvodnění databáze transparentnosti"
    - "DSA compliance balíček advokátní kancelář cena online platforma tržiště kontaktní místo zpráva o transparentnosti"
    - "TMS systém řízení přepravy tendrování dopravců česká firma"
    - "zabezpečení mobilního bankovnictví a ověřování plateb česká firma"
  checked: [google-cz, ares, own-funded-ledger, eshop-addon-marketplaces]
  expires: '2026-12-18'
created: '2026-09-19'
updated: '2026-09-19'
---

Czech marketplaces, job boards and forums must handle reports of illegal posts and explain each removal, and few file their decisions with the EU [S1,S8].

- 16 of 22 Czech services listed filed no removal in six months [S8].
- Complaints to the regulator rose from 25 in 2024 to 98 in 2025 [S4,S5].
- The regulator answered 123 written questions in 2025, some on the EU database [S4].

The rules come from the Digital Services Act, the EU law on how online platforms handle illegal content and complaints [S1].

- Every site that stores users' posts owes this, whatever its size [S1].
- Platforms that are not small firms must also handle complaints, file each removal in a public EU database and report yearly [S1].
- A 2024 study for the regulator counted 182 online platforms and 76 marketplaces in Czechia, 44 of them medium-sized or large [S6].
- Filing nothing can also mean removing nothing [S8].
- 15 of the 98 complaints concerned providers based in Czechia [S4].

Existing non-solutions: No Czech firm sells software for these steps; law firms sell advice, and a Slovak firm moderates comments [S11].

- Czech law firms publish guides to the duties and sell advice [S11].
- A Slovak firm moderates comments for Czech media with AI and people [S11].
- A consultancy mapped the market for the regulator, not for platforms [S6].

None of them runs the daily steps [S11]. The rows are under [Market gap](#competition).

Why now: A Czech bill would let the telecoms regulator fine a marketplace or forum up to 6% of worldwide turnover for skipping these steps [S2,S3].

- Removing a post without telling the user why becomes an offence [S3].
- Sending no removal decisions to the EU database becomes one too [S3].
- The regulator plans to start supervising once the law passes [S4].

The dates behind this:

- The EU rules have applied since 17 February 2024 [S1].
- In May 2025 the European Commission decided to take Czechia to court over the missing powers [S7].
- The bill can reach its last lower-house vote from 5 September 2026 and takes effect 15 days after publication [S2,S3].
- Through 2025 the regulator could not inspect or fine, and no complaint led to an investigation [S4,S5].

Who pays: The platforms carry this work themselves, and no Czech price for software or help with it is published [S1,S11].

- No Czech seller publishes a price for running these steps [S11].
- Law firms advising on the rules list no price for it [S11].

Solved elsewhere: In France and Britain, online platforms already buy software that handles reports, removal reasons and yearly reports [S9,S10].

See [Validated abroad](#validated-abroad).

## First moves

1. Build a Czech-language tool that files a platform's removal decisions in the EU database, and offer it free to one job board or classifieds site. Many Czech services listed there file nothing, as [The opportunity](#opportunity) shows, so a site that can start filing without new staff sees the point quickly. Then add report intake and the reason sent to each user.
2. Call the person who handles reported posts at a few mid-size Czech marketplaces and job boards. Ask how they answer reports and write the yearly report today, what it costs in staff time, and who helps them. Those answers are the price you do not have yet; see [Willing to pay](#willing-to-pay).
3. Offer one of the Czech law firms under [Market gap](#competition) a partnership. They advise platforms on the rules and bring the clients; you bring the software that does the daily work and writes the yearly report they would otherwise draft by hand.
4. Time your sales to the bill described under [Why now](#why-now). Once it passes, the telecoms regulator can inspect and fine, so have a working product ready for the first platforms it contacts.

## Revisions

2026-09-19 · record created — Created from fr-tremau and reg-dsa-cz, finishing a pass that stopped before its Czech-language check. Scores (v1 ladders, the set this checker runs): proof 2, two established sellers in France and Britain, none in a neighbouring market [S9,S10]; money 0, no public budget near the buyer's work and no price receipt; urgency 3, the rules apply now and the fining bill is at its last lower-house stage, plus fresh sources [S1,S2,S3]; demand 1, complaints recur but mostly target very large platforms [S4,S5]; gap 2, nobody sells the software, controls passed [S11]. Read under the 2026-09-19 ladders it would be money 0 and urgency 1, since the 2024 duty is older than 12 months and the fining law is still a bill, so 6. No draft-law badge: the EU rules bind platforms today, as on the AI Act problem, and the bill only adds fines [S1,S3]. Our readings, flagged: 44 is our sum of the study's medium and large rows [S6]; the 22 Czech services were picked by name [S8]; "few" rests on that count. The earlier pass's foreign monthly price could not be read at source and is left out [S10]. Abroad count: both comps sell report handling and yearly reports; the British one's page names no reason letters or database filing, so it counts on that half [S9,S10]. Czech check: Seznam and the web-search tool, both logged as google-cz for want of a Seznam token; the market control passed on Seznam and the Ringil control on the web-search tool, while Seznam missed Ringil and Wultra [S11].
