---
id: p-0051
region: cz
title: 'Czech sole traders can borrow 300,000 CZK and be chased for 1.4M CZK within 3 months'
brief: 'Lenders sign people up as businesses, so the consumer-credit rules do not protect them, and a notary''s deed lets the lender enforce without a court [S1,S2]. More of those deeds end in fast enforcement every year [S1].'
solution: 'Build a check where a sole trader uploads a business-loan contract and sees the grounds to fight it, and a partner lawyer takes the case for a share of what is saved, as 2 companies already do in the United States.'
good_for: 'Lawyers who fight lenders in Czech courts and can build or run simple software.'
price_search: 'Ask Czech advocates who defend debtors against non-bank lenders what they charge to review a business loan signed as a sole trader and to move to stop enforcement on a notary''s deed; search law-firm price lists for "revize úvěrové smlouvy" and "návrh na zastavení exekuce"; and ask the debt non-profits what their clients were quoted.'
category: fintech
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
  level: hard
  buyer: small-firms
  permission: licence
  incumbents: adjacent
  integration: software
  money: bootstrap
  why: 'Easier: debtors already pay lawyers to look at enforcement cases; the check is ordinary software; and nobody sells it for business loans. Harder: paid legal advice is reserved to advocates, so a lawyer must run the service; established law firms take such cases one by one; and each case turns on its facts.'
comps:
- name: Tayne Law Group
  url: https://attorney-newyork.com/
  geo: US
  since: 2001
  traction: 'New York debt-relief law firm serving clients since 2001; defends small businesses
    against merchant cash advances, negotiates settlements and vacates confessions of judgment;
    its site counts 1,000+ clients, 11,000+ cases and $11.5M+ settled (own site, 2026).'
- name: Delancey Street
  url: https://www.delanceystreet.com/our-difference/
  geo: US
  since: 2023
  traction: 'New York business-debt relief firm for merchant cash advances, working with a network
    of independent attorneys; flat fee as a share of enrolled debt; $100M+ settled for 1,000+
    owners (own site, 2026); BBB lists the business as started 2023-02-23.'
locals:
- name: Úrokzpět (JUDr. Diana Albastová, advokátka)
  url: https://www.urokzpet.cz/
  ico: '19557990'
  since: 2023
  competes: adjacent
  maturity: early
  evidence: 'It sells the consumer half of this job: an advocate wins back overpaid interest, penalties
    and fees from non-bank lenders and keeps 20% of what she recovers, nothing if she recovers
    nothing [S8]. Its own page takes only contracts signed as a consumer, "nikoliv na IČO v postavení
    podnikatele", so a sole trader''s business loan is exactly what it turns away [S8]. ARES dates
    the practice to 1 September 2023; it claims a success rate above 95% but publishes no client
    count.'
- name: ARROWS advokátní kancelář
  url: https://arws.cz/novinky-v-arrows/podnikatelske-uvery-a-soudni-spory
  ico: '06717586'
  since: 2018
  competes: adjacent
  maturity: established
  evidence: 'It sells general legal work, and a May 2026 article offers business borrowers contract
    analysis, a defence against a loan being called in, negotiation and court representation [S8].
    The article is aimed at bank loans and whether the bank checked the borrower could repay, and
    it publishes no fixed or success-based price, so it is a law firm taking cases one by one, not
    a check a sole trader can run. ARES dates the company to 1 January 2018, and its home page names
    a client, the chief executive of KEESTRACK-CZ, and counts 60+ advisers [S8]; no public buyer
    pairs with it on the state contracts register.'
- name: Dostupný advokát
  url: https://dostupnyadvokat.cz/blog/zastaveni-a-promlceni-exekuce
  ico: '09788336'
  since: 2021
  competes: adjacent
  maturity: established
  evidence: 'It sells fixed-price online legal help across every area of law, including a first
    look at an enforcement case with a proposed next step [S7]. Nothing in it is aimed at business
    loans or at the lenders behind them, so it is the general door a debtor walks through today,
    not this product. ARES dates the company to 1 January 2021, and its home page reports thousands
    of resolved cases and 150+ new customers a month [S8].'
- name: AZ LEGAL, advokátní kancelář
  url: https://azlegal.cz/pravni-sluzby/smlouva-o-uveru/
  ico: '05030323'
  since: 2016
  competes: adjacent
  maturity: established
  evidence: 'It sells loan-contract drafting at a fixed price, pitched to the person lending the
    money, reviews an existing contract by arrangement, and represents both lenders and borrowers
    in disputes [S8]. That is contract work for the lending side, not a check or a defence built
    for a sole trader already caught by a business loan. ARES dates the firm to 27 April 2016, and
    its page counts more than 1,500 clients [S8].'
- name: Člověk v tísni (Lichvolapka)
  url: https://jakprezitdluhy.cz/lichvolapka/
  ico: '25755277'
  competes: non-seller
  evidence: 'A charity that runs free debt advice and a free online check of whether a lender broke
    consumer-credit law [S8]. It charges nothing, and its own page says the defence against a loan
    signed "na IČO" is more complicated, so its check stops where this problem starts. A builder
    needs it as a partner that already meets the borrowers, not as a rival.'
- name: Institut prevence a řešení předlužení
  url: https://www.institut-predluzeni.cz/novinky/moderni-lichvari-cili-na-byty-a-domy-studie-odkryva-skryty-byznys/
  ico: '07753268'
  competes: non-seller
  evidence: 'A non-profit that studies over-indebtedness and advises people caught by it [S3]. It
    wrote the 2026 study on loans signed as a business and supplied the Finance Ministry its worked
    case [S1,S3]. It sells nothing; it is where the victims and the case files already are.'
- name: Kancelář finančního arbitra
  url: https://finarbitr.gov.cz/cs/oblasti/uver.html
  competes: non-seller
  evidence: 'The state''s free dispute service for financial products. It hears a loan dispute only
    if the borrower proves they signed as a consumer, so a real business loan never reaches it and
    a disguised one reaches it only once that proof is made [S4].'
process:
  summary:
    today: 'A broker signs the sole trader to a business loan with a notary''s deed, the lender calls the whole debt due after days of arrears, and a bailiff enforces without a court until the borrower finds a lawyer [S1,S2].'
  steps:
  - who: The sole trader
    today: 'Signs a business loan and a notary''s deed'
    known: documented
    cites: [1]
    change: changes
    after: 'Runs the contract through a check first'
  - who: The lender
    today: 'Calls the whole debt due after days late'
    known: documented
    cites: [1]
    change: stays
    after: 'Unchanged: the lender still decides'
  - who: A bailiff
    today: 'Starts enforcement on the deed, no court'
    known: documented
    cites: [1]
    change: stays
    after: 'Unchanged: enforcement can still start'
  - who: The sole trader
    today: 'Needs a lawyer to stop enforcement'
    known: documented
    cites: [2]
    change: changes
    after: 'Gets the grounds and a lawyer together'
  - who: A partner lawyer
    today: null
    known: inferred
    cites: []
    change: new
    after: 'Takes the case for a share saved'
sources:
- type: regulation
  name: 'Finance Ministry bill on business loans — impact assessment'
  gist: 'the draft, effective 2028'
  why: 'The Finance Ministry''s own assessment of its draft law: it describes how some lenders use
    business loans to sole traders, gives the market size, a worked case and the Justice Ministry''s
    count of notary deeds, and proposes a start date of January 2028.'
  url: https://www.odok.cz/portal/services/download/attachment/KORNDY9CPRR1/
  note: 'Signal reg-uvery-osvc-ochrana-2028. RIA for "Návrh zákona, kterým se mění některé zákony
    v oblasti sjednávání úvěrů pro podnikatele a zákon č. 358/1992 Sb., o notářích" (VeKLEP
    KORNDY9BQZVI, "2 - v připomínkovém řízení", authorised 25 Sep 2026, comments due 26 Oct 2026),
    read from data/raw/2026-09-28/regulation/pages/veklep/ria_KORNDY9BQZVI.txt. Effective date
    "1/2028". Problem: non-consumer natural-person borrowers get only the civil code; predatory
    practice = lending to uncreditworthy borrowers at high rates, non-standard amortisation,
    acceleration, notarial deed with consent to enforcement; plus disguised consumer loans "na IČO".
    Worked case (source IPŘP): signed 20 Jul 2023, 460,000 CZK contracted, 300,000 CZK paid out,
    160,000 CZK broker commission, 1.7 % p.m., 10 years without principal repayment, acceleration
    after >3 days arrears, accelerated 27 Sep 2023, enforcement 3 Oct 2023 on the notarial deed,
    1,402,800 CZK enforced (principal, future interest, one-off and contractual penalty). Scale:
    1,996,027 natural-person entrepreneurs with 3,079,454 trade licences (MPO, Q2 2026); ~1.2M OSVČ
    in social insurance (MPSV); ~60bn CZK outstanding to sole traders (ČNB ARAD 1053, 7/2026).
    §1797 OZ bars a borrower acting in business from invoking usury (§1796); §433 presumes a consumer
    weaker, an entrepreneur must prove it. §122(5) ZSÚ (since 2020) caps late-payment charges for
    non-consumer natural persons after 90 days. 2025 comment round: MPSV, MZe, MMR, MPO, MSp, AMSP,
    HK, UZS, KZPS, APNÚ and the ombudsman asked to extend protection; MF promised a separate bill.
    MSp table: deeds with direct enforceability 9,501 (2021), 9,933, 10,997, 12,149, 12,643 (2025);
    share enforced 19/19/23/23/24 %; share of "fast" enforcements (within 1–2 years of the deed)
    4/9/15/41/37 %. Model: 1M CZK bank loan, 700k principal left, 90k future interest; today 790k,
    under the bill 700k (12 % less). Chosen: C.1 var. 1 (acceleration limited to unpaid principal,
    no 30-day notice for entrepreneurs), C.2 var. 2 (deeds only by a notary, only in person).
    Working group: some members held the current law sufficient and asked for a minimal rule.
    Abroad: BE and FR protect small firms in B2B contracts; DE, PL, AT have no special protection.'
  date: '2026-09-25'
  signal: reg-uvery-osvc-ochrana-2028
  dims: [urgency, demand]
- type: news
  name: 'ČT24 — predators abuse business loans'
  gist: 'Czech TV report, 2025'
  why: 'Czech public television on lenders making people register a trade to get a business loan,
    with the same worked case and the advice that a victim should get a lawyer and move to stop the
    enforcement.'
  url: https://ct24.ceskatelevize.cz/clanek/domaci/predatori-zneuzivaji-podnikatelske-uvery-popsali-reporteri-ct-365344
  note: 'ČT24, 23 Sep 2025, read 2026-09-28. Radek Hábl (IPŘP): business loans became a tool of
    usurers; the victim should take a lawyer and file a motion to stop the enforcement, arguing it
    was a consumer loan ("V tu chvíli se může bránit a může poukazovat na to, že nešlo o skutečný
    podnikatelský úvěr, ale šlo o spotřebitelský úvěr"). Same 460k/300k case, stated there as 1.5M
    CZK enforced (the RIA gives 1,402,800 CZK, which is the figure used). A mother: "Byla tam
    podmínka, že si musím udělat živnost". Mrs. Hana: 50,000 CZK borrowed, 800 CZK a week, 1,500 CZK
    penalty per late payment, family home at risk. Quotes also ČNB spokeswoman and a debt lawyer.'
  date: '2025-09-23'
  dims: [demand]
- type: complaint
  name: 'IPŘP — "Moderní lichva v praxi"'
  gist: 'the 2026 usury study'
  why: 'A non-profit''s study of modern usury in Czechia: people in acute debt are pushed to borrow
    as a business so consumer protection does not apply, and the authors estimate tens of
    thousands of victims.'
  url: https://www.institut-predluzeni.cz/novinky/moderni-lichvari-cili-na-byty-a-domy-studie-odkryva-skryty-byznys/
  note: 'IPŘP news item, 20 Jan 2026, read 2026-09-28. Study "Moderní lichva v praxi: Skrytý byznys
    se zadlužením a nemovitostmi v Česku" (authors incl. Petra Lomozová, Jakub Sosna); estimate of
    "desítky tisíc" victims from cadastre, trade-register and other data; three methods: loans na
    IČO, P2P loans through intermediaries, reverse leasing of homes; notarial deeds so that "není
    potřeba soud". "Lidé v akutní finanční krizi jsou lichváři cíleně tlačeni k využití" of an IČO.
    The victims estimate covers all three methods, not business loans alone.'
  date: '2026-01-20'
  dims: [demand]
- type: complaint
  name: 'ČNB — warning on loans signed as a business'
  gist: 'central bank warning, 2025'
  why: 'The Czech National Bank warns that loans dressed up as business loans strip borrowers of
    consumer protection, and says it has received complaints disputing the business nature of such
    loans.'
  url: https://www.cnb.cz/cs/dohled-financni-trh/vykon-dohledu/upozorneni-pro-verejnost/Varovani-pro-spotrebitele-mozna-rizika-uveru-sjednavanych-na-ICO-tzv.-zastrenych-spotrebitelskych-uveru/
  note: 'ČNB public warning dated 11 Dec 2025, read 2026-09-28. "K tomuto tématu ČNB obdržela v
    uplynulých letech několik podání, jejichž předmětem bylo zpochybnění podnikatelské povahy úvěrů".
    "Finanční arbitr je však příslušný rozhodovat pouze o návrzích spotřebitelů, tj. pouze v případě,
    že se v řízení podaří prokázat" consumer status. No count of complaints is given.'
  date: '2025-12-11'
  dims: [demand]
- type: arbitrage
  name: 'Tayne Law Group'
  gist: 'US business-debt law firm'
  why: 'An American law firm that defends small businesses against merchant cash advances, the
    US version of a predatory business loan, including undoing the pre-signed consent to judgment.'
  url: https://attorney-newyork.com/
  note: 'Home page read 2026-09-28: "Serving clients since 2001", merchant cash advance defence
    and settlement, vacating confessions of judgment; counters "1,000+ Trusted clients", "11,000+
    Cases solved", "$11.5M+ Debt settled". Founder Leslie H. Tayne. Established: selling since 2001
    and a public client count.'
  date: '2026-09-28'
- type: arbitrage
  name: 'Delancey Street'
  gist: 'US business-debt relief'
  why: 'An American firm that settles merchant cash advance debt for small-business owners and
    coordinates lawyers to undo pre-signed consents to judgment, paid as a share of the debt it
    handles.'
  url: https://www.delanceystreet.com/our-difference/
  note: 'Our-difference page read 2026-09-28: flat fee "calculated as a percentage of your total
    enrolled debt"; "We''ve resolved over $100M in business debt for 1,000+ owners"; attorney network
    in 49 states; COJ-vacate playbook. BBB profile (bbb.org, Delancey Street Group LLC) gives
    business started 2023-02-23. PR Newswire 19 Mar 2026: network expanded to 50 states; "not a law
    firm". Established on the test by trading since 2023 (three years by 2026) and a public customer
    count.'
  date: '2026-09-28'
- type: news
  name: 'Dostupný advokát — stopping enforcement, 2026'
  gist: 'a law firm''s enforcement guide'
  why: 'A Czech online law firm''s guide to stopping enforcement, which offers a fixed-price first
    look at any enforcement case; it is general legal triage, not a price for fighting a business
    loan, so it backs no score.'
  url: https://dostupnyadvokat.cz/blog/zastaveni-a-promlceni-exekuce
  note: 'Page "Zastavení a promlčení exekuce v roce 2026", 30 Jun 2026, read live 2026-09-28:
    "Váš případ posoudíme a navrhneme, jak ho vyřešit za 390 Kč"; "390 Kč včetně DPH"; the fee is
    waived if the client then orders the proposed service. A generic triage across all areas of law,
    not priced for business loans specifically: basis list-price, so ASKING, rung 1. What the full
    defence costs is not published.'
  date: '2026-06-30'
  dims: []
- type: gap-check
  name: 'Market scan — who fights a sole trader''s business loan'
  gist: 'the Czech sweep, 2026'
  why: 'Czech searches in a borrower''s words found success-fee lawyers and free checks for consumer
    loans that turn business loans away, general law firms, and nobody selling a check or a
    success-fee defence for a sole trader''s business loan.'
  url: https://www.urokzpet.cz/
  note: 'Run 2026-09-28. POSITIVE CONTROL, run first: the known category of Czech consumer-loan
    claims and checks (p-0027 records claims firms filing in bulk at the arbiter) was surfaced on the
    first page of query 1 — Úrokzpět (advocate, IČO 19557990, 20 % of recovered money, success fee
    only) and Člověk v tísni''s free Lichvolapka check. PASSED. BOTH explicitly exclude business
    loans: Úrokzpět takes only contracts signed "v postavení spotřebitele (tj. nikoliv na IČO v
    postavení podnikatele)"; Lichvolapka says "U podnikatelských úvěrů (tzv. půjčka na IČO) je obrana
    proti nevýhodnému úvěru složitější". NOT FOUND: any Czech service that checks a sole trader''s
    business-loan contract or takes its defence on a success fee. FOUND, all in locals[]: ARROWS
    advokátní kancelář s.r.o. (IČO 06717586, ARES 2018-01-01; article of 22 May 2026, updated 5 Aug
    2026, offering analysis, defence against acceleration, negotiation, court representation on
    business loans, bank-focused, no price); Dostupný advokát s.r.o. (IČO 09788336, ARES 2021-01-01;
    390 CZK case review, all areas); IPŘP (IČO 07753268, ARES 2019-01-02, non-profit); finanční
    arbitr (consumer disputes only). SEEN, NO ROW: Poradna při finanční tísni, o.p.s. (IČO 28186869)
    is in liquidation per ARES; nine ARES entities named "Dluhová poradna" (debt-relief and insolvency
    filing firms, e.g. IČO 03974928, 04826124) sell personal insolvency, not loan defence; many
    lenders advertise "půjčka na IČO" to indebted sole traders — the other side of the problem.
    ARES name searches for "lichv", "Stop lichv", "Proti lichv", "Úrokzpět" returned 0.
    data/lookup/cz-contract-parties.jsonl: 0 rows for IČO 19557990, 25755277, 06717586, 07753268,
    09788336. Own funded ledger: no Czech or foreign business-loan defence company. ADDED THE SAME DAY on
    coordinator review: AZ LEGAL, advokátní kancelář, s.r.o. (IČO 05030323, ARES 2016-04-27; loan
    contract drafting "od 5 990 Kč", pitched to lenders, "pokud již máte stávající smlouvu, můžeme
    se domluvit na její revizi", represents "jak věřitele, tak dlužníky", "Více než 1 500 klientů";
    first-page result of query 1, missed in the first pass). Maturity re-checked on live home pages:
    dostupnyadvokat.cz "Tisíce úspěšně vyřešených případů. 150+ nových zákazníků každý měsíc"
    (p-0004 records it established on the same page); arws.cz names a client testimonial from
    Pavel Doležel, CEO of KEESTRACK-CZ, and "60 + poradců"; urokzpet.cz shows only first-name
    testimonials ("Petr K., Praha") and "Úspěšnost více než 95 %", no count, so it stays early.
    No Czech price for reviewing or defending a sole trader''s business loan was found.'
  date: '2026-09-28'
  queries:
  - 'kontrola úvěrové smlouvy OSVČ úvěr na IČO lichva pomoc'
  - 'zastřený spotřebitelský úvěr na IČO advokát obrana exekuce notářský zápis podnikatel'
  - 'posouzení smlouvy o úvěru podnikatel zesplatnění notářský zápis pomoc živnostník'
  - 'půjčka na IČO neplatná vymáhání obrana živnostník bezplatná poradna odměna z úspěchu'
  - '"úvěr na IČO" pomoc podnikatel exekuce dům advokátní kancelář "podnikatelský úvěr" lichva obrana'
  - 'návrh na zastavení exekuce advokát cena Kč ceník notářský zápis'
  checked: [google-cz, ares, cz-contract-parties, own-funded-ledger]
  expires: '2026-12-27'
- type: regulation
  name: 'Act No. 85/1996 Coll. (advocacy), §§ 1–2'
  gist: 'paid legal advice is for advocates'
  why: 'The Czech advocacy act: giving legal advice, drafting documents and representing clients
    regularly and for payment is reserved to advocates and a few other listed professions, so a
    paid check of a loan contract has to run through an advocate.'
  url: https://www.zakonyprolidi.cz/cs/1996-85
  note: 'Zákon č. 85/1996 Sb., o advokacii, read on zakonyprolidi.cz 2026-09-28 (aktuální znění
    od 1. 1. 2026, verze 36; platnost 22. 4. 1996, účinnost 1. 7. 1996). § 1 odst. 2: "Poskytováním
    právních služeb se rozumí zastupování v řízení před soudy a jinými orgány, obhajoba v trestních
    věcech, udělování právních porad, sepisování listin, zpracovávání právních rozborů a další formy
    právní pomoci, jsou-li vykonávány soustavně a za úplatu." § 2 odst. 1: "Právní služby na území
    České republiky jsou oprávněni poskytovat za podmínek stanovených tímto zákonem a způsobem v něm
    uvedeným a) advokáti, b) ... evropský advokát"; § 2 odst. 2 keeps the rights of notaries,
    bailiffs, patent attorneys, tax advisers and others a special law names, and of employees
    advising their own employer. This is what entry.permission: licence rests on: a paid review of
    a loan contract and a motion to stop enforcement are legal services under § 1(2). A statute in
    force since 1996 is the status quo, not a dated duty on this buyer, so it backs no score and
    does not move urgency (dims empty); urgency stays on the draft bill [S1].'
  date: '1996-03-13'
  dims: []
created: '2026-09-28'
updated: '2026-09-28'
---

Sole traders who borrow for their business get none of the consumer-credit rules, and some lenders design loans to be lost [S1].

- A loan paying out 300,000 CZK became 1.4M CZK enforced in 75 days [S1].
- A notary's deed signed with the loan skips the court [S1].
- People with no business are pushed to register one for the loan [S2,S3].

How the worked case ran, from the Finance Ministry's own assessment [S1]:

- The contract, signed on 20 July 2023, said 460,000 CZK, and 160,000 CZK of it went to the broker [S1].
- Interest was 1.7% a month, with no principal repaid for 10 years [S1].
- The whole loan fell due after more than 3 days late, and the lender called it on 27 September 2023 [S1].
- Enforcement started on 3 October 2023 for 1,402,800 CZK, including future interest and penalties [S1].

Why the borrower is exposed:

- The law presumes a consumer is the weaker party, and a sole trader has to prove it case by case [S1].
- A borrower who signed in business cannot have the loan voided as usury [S1].
- Some loans are consumer loans only labelled as business ones, and the borrower has to prove that too [S1,S4].

How big the group is:

- Almost 2 million people hold a Czech trade licence, and about 1.2 million pay self-employed social insurance [S1].
- Sole traders owed about 60bn CZK in loans in July 2026 [S1].
- A 2026 study by a debt non-profit estimates tens of thousands of victims of this kind of lending, much of it aimed at people's homes [S3].

Existing non-solutions: Czech services that win money back from lenders work only for consumers, and turn business loans away [S8].

Each one's details are in its row. What they do:

- A Czech lawyer wins back overpaid interest on consumer loans for a share of what she recovers, and her page excludes loans signed as a business [S8].
- A debt charity runs a free online check of consumer loans, and says a business loan is harder to fight [S8].
- The state's financial dispute service hears a case only once the borrower proves they signed as a consumer [S4].
- Law firms take business-loan disputes one by one, and publish no fixed or success-based price [S8].
- A Prague law firm drafts loan contracts, mostly for lenders, and reviews existing ones by arrangement [S8].
- An online law firm sells a first look at any enforcement case, with nothing aimed at business loans [S8].

Nobody sells a sole trader a check of the business-loan contract, or a defence paid out of what it saves [S8].

Why now: Sole traders in these loans lose money now, and the draft fix would only start in January 2028 [S1].

- In 2025, 12,643 deeds allowing enforcement were written, against 9,501 in 2021 [S1].
- In 2025, 37% of enforcements on them came within 1–2 years [S1].
- A borrower a few days late can owe the loan plus future interest [S1].

In 2021 only 4% of enforcements on those deeds came that fast [S1].

The dates:

- In December 2025 the Czech National Bank warned borrowers about loans signed as a business, after complaints [S4].
- In January 2026 a debt non-profit published its study of lending signed as a business [S3].
- The Finance Ministry's bill went out for comment in September 2026, with comments due on 26 October 2026 [S1].
- It would let a lender call in only the unpaid principal, not the future interest, from January 2028 [S1].
- In the ministry's own example, that cuts what a sole trader owes on a called-in bank loan by 12% [S1].
- It would also let only a notary write the deed, and only with the borrower there in person [S1].
- Caps on late-payment charges after 90 days already cover sole traders, since 2020 [S1].
- It is a draft, and some lenders in the working group said today's law is enough [S1].

Who pays: No Czech price for fighting a sole trader's business loan is public, though debtors pay lawyers for general help [S7,S8].

- An online law firm sells a fixed-price first look at any enforcement case [S7].
- A lawyer wins back consumer-loan overcharges for a share, and refuses business loans [S8].
- A law firm sells loan-contract work at a fixed price, pitched at lenders [S8].

None of these is a price for this defence, so nothing here shows a sole trader paying for it yet. The consumer-loan share is taken only when money comes back [S8]. The money a defence could be paid from sits in the gap between what the lender paid out and what it enforced, which in the worked case was about 1.1M CZK [S1]; whether a sole trader will give up a share of it is not yet shown.

Solved elsewhere: Two American firms defend small businesses against predatory business advances and have served more than 1,000 owners each [S5,S6].

In the United States the closest thing is the merchant cash advance: an advance to a small business that often comes with a signed consent to judgment, so the lender can enforce without a trial, much like the Czech notary's deed [S6]. A New York law firm serving clients since 2001 fights these advances, settles them and undoes the pre-signed judgments, and counts more than 1,000 clients [S5]. A New York firm started in 2023 does the same through a network of independent lawyers, charges a fee set as a share of the debt it handles, and says it has resolved more than $100M for more than 1,000 owners [S6].

In Europe the law does part of the job instead: Belgium and France protect small firms against unfair terms between businesses, while Germany, Poland and Austria have no special protection [S1].

## First moves

1. Build a simple check that reads a sole trader's business-loan contract and flags the clauses courts and the ministry have already named as abusive. Start with the ones in the worked case in [The opportunity](#opportunity): the whole loan falling due after a few days late, future interest demanded at once, a broker's cut taken from the payout, and a notary's deed signed through someone else. Show the borrower, in plain words, which clause they can challenge and what to do next.
2. Offer the check free to the debt non-profit that wrote the study and the charity running the consumer-loan check. They already meet these borrowers and turn the business-loan cases away, as [Market gap](#competition) shows. Ask them for a handful of real contracts to test against, with the client's consent.
3. Sign one advocate who will take the strong cases for a share of what the client saves. Legal advice for money has to come from a lawyer, as [Execution difficulty](#execution-difficulty) explains, so the service runs through that person from day one. Keep the first look cheap, as the general case reviews in [Willing to pay](#willing-to-pay) are, and take the rest only from money saved.
4. Follow the Finance Ministry's bill through comments and parliament, and update the check the day it passes. The dates are in [Why now](#why-now). A new rule that limits what a lender may call in is one more clause the check can flag, and one more reason a sole trader has a case.

## Revisions

2026-09-28 · record created — Minted from the regulation signal reg-uvery-osvc-ochrana-2028, the Finance Ministry's draft law on loans to sole traders and its impact assessment [S1], and judged against Czech evidence gathered on this date. DISTINCT FROM p-0027: that problem is lenders answering consumer disputes at the financial arbiter; this one is the borrower who is not a consumer at all, whom the arbiter cannot hear unless consumer status is proven [S4]. The buyer is the opposite side of the counter, so it is its own problem, not a duplicate. THE BUYER WAS THE HARD PART, and this is the reading: the sole trader pays, as a small first-look fee and then a share of what the defence saves, the model a Czech advocate already runs for consumer loans and explicitly refuses to run for business ones [S8], and the model two US firms run for small businesses [S5,S6]. Debt charities are partners and channels, not buyers: they charge nothing [S8]. Lenders complying with the bill were considered and rejected as the buyer, because the bill changes two clauses and needs no product. DEMAND 2: the ministry's assessment records the 2025 push by five ministries, business and lender associations and the ombudsman, plus the Justice Ministry's rising deed statistics [S1]; Czech public television reported the pattern [S2]; a non-profit study estimates tens of thousands of victims across three methods, not business loans alone, which the body says [S3]; the central bank warned after complaints [S4]. MONEY 1 on one asking receipt, a 390 CZK lawyer's first look at an enforcement case [S7]: it is generic triage, not a price for this defence, and the body says so. URGENCY 1: the only dated instrument is a draft whose duties fall on lenders, so it fails REAL. NO draft_law key, a judgement call for the owner: the losses in the worked case happened in 2023 under today's law, and the bill would shrink the pain rather than create it; take the bill away and the problem still stands, so the main pain does not depend on it. PROOF 2: two established US firms, one market, none in Europe [S5,S6]. Delancey Street's start date comes from its BBB profile (2023-02-23), which makes it exactly three years old by the calendar year. GAP 2 on a controlled check [S8] with a passing positive control. Figures: the ČT24 report gives 1.5M CZK for the same case; the assessment's 1,402,800 CZK is used, rounded to 1.4M. OUR CALCULATIONS, flagged: "within 75 days" is 20 July to 3 October 2023; "about 1.1M CZK" is 1,402,800 less 300,000 CZK. INFERENCES, flagged: that a sole trader will pay a share of what is saved (resting on [S5,S6,S8], none Czech for business loans); the new partner-lawyer step in the process. permission is licence because paid legal advice is an advocate's monopoly in Czechia, stated from general knowledge of the advocacy act and not from a source on file. Same date, coordinator review, merged here: MONEY 1 → 0 and score 8 → 7, STRONG → FAIR. The 390 CZK first look at an enforcement case is general legal triage, not the price of reviewing or defending a sole trader's business loan, so it was not an asking receipt for this job; [S7] is now filed as `news` with no dimension and backs no score, and the Who pays section was rewritten to say no price for this defence is public. A further search found AZ LEGAL's loan-contract service "od 5 990 Kč", but it is drafting pitched to lenders with review of an existing contract only by arrangement, so it is not this job either; it is recorded in locals[] and in [S8], and price_search now says where a real price would be found. MATURITY re-checked by the established test on each firm's live home page: Dostupný advokát (trading since 2021, thousands of cases and 150+ new customers a month, as p-0004 already records) and ARROWS (since 2018, a named client) are established; AZ LEGAL (since 2016, 1,500+ clients) is established; Úrokzpět shows only first-name testimonials and no count, so it stays early. All four stay competes: adjacent, so gap stays 2, and entry.incumbents now derives to `adjacent`. The [S8] note was extended with these findings in the same creation change, and entry.why gained the item that established law firms take such cases one by one. The first pass had called these firms early without checking their home pages, which was a false maturity claim. Same date, owner review, merged here: the licence gate now rests on a source on file, not general knowledge. The advocacy act, Act No. 85/1996 Coll., §§ 1–2, reserves legal services given regularly and for payment, including legal advice, drafting documents and representing clients before courts, to advocates and a few other listed professions [S9]; it is added as [S9], behind entry.why's line that paid legal advice is reserved to advocates; First moves step 3 keeps no marker, because moves carry none and link to Execution difficulty, where that line renders. It is a statute in force since 1996, so it is the status quo, not a dated duty, and it moves no score: urgency stays 1 on the draft bill [S1]. The earlier sentence that the licence gate was stated from general knowledge is superseded by this one. Two stray lines of tool markup that had been left between this entry's sentences were removed; no words of the entry were lost.
