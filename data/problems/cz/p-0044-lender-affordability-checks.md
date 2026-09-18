---
id: p-0044
region: cz
title: 'Czech lenders can be fined 4M CZK for not checking what borrowers earn and spend. A bill now extends that check to buy-now-pay-later.'
brief: 'Some lenders take borrowers at their word on expenses instead of checking bank statements, and non-bank lenders were fined 19M CZK last year [S6,S7]. A bill the lower house passed in September extends the check to buy-now-pay-later from February 2027 [S2,S3].'
solution: 'Build a service that reads a borrower''s bank transactions, with consent, and gives the lender a documented affordability check, as 2 companies already do in 2 other countries.'
good_for: 'Someone who knows credit risk and bank data and can sell to lenders.'
price_search: 'No public buyer pays for this, so ask the head of risk at a non-bank lender on the Czech National Bank''s register what it pays per bank-data check, or ask the account-data sellers under Competition for a quote per client; registr smluv holds no such contract because the buyers are private.'
category: fintech
geo: CZ-national
score: 8
scores:
  proof: 3
  money: 0
  urgency: 3
  demand: 2
  gap: 0
status: watching
entry:
  level: moderate
  buyer: large-firms
  permission: none
  incumbents: direct
  integration: software
  money: bootstrap
  why: 'Easier: no licence is needed when the bank data comes through a licensed provider, the new rules name bank data as a source, and lenders already pay fines for weak checks. Harder: the buyers are lenders that want an audit trail the central bank accepts, and established sellers already offer this in Czech.'
comps:
- name: Algoan
  url: https://www.algoan.com/en
  geo: FR
  since: 2017
  traction: 'Registered with the French banking supervisor as an account-information provider; turns
    bank-transaction data into credit scores and affordability analysis for consumer credit and
    buy-now-pay-later. Named customers include Cofidis, BNP Paribas, Alma and Revolut (company site,
    2026); 25 lenders signed in 2021, profitable and aiming for EUR 5M a year in recurring revenue
    by early 2025 (mind Fintech, 2025). Company registered October 2017 (French company register).'
  signal: fr-algoan
- name: Tink (Income Check)
  url: https://tink.com/products/income-check/
  geo: SE
  since: 2012
  traction: 'Income Check verifies a borrower''s income straight from the bank account through an
    API; named customers include Bank Norwegian and GF Money. Founded in Stockholm in 2012, part of
    Visa since 2022, 3,000+ bank connections in 19 European markets (company site, 2026).'
locals:
- name: Kontomatik
  url: https://www.kontomatik.com/cz/podporujeme-rozvoj-firem-technologii-otevreneho-bankovnictvi
  since: 2011
  competes: direct
  maturity: established
  evidence: 'Sells lenders a check that verifies a customer''s income and expenses from bank data
    "in seconds", on a Czech-language page, and lists the Czech Republic among its markets. Its site
    claims 15+ years on the market and 150+ customers, with named customers such as Raiffeisen
    Digital Bank, Smartney and Allegro Pay, and account-information authorisations in Lithuania and
    Poland. It sells from Poland, no Czech company of that name is in the state business register,
    and no Czech customer is named [S11].'
- name: Dateio (Tapix)
  url: https://www.tapix.io/solutions/smart-data-for-credit-scoring
  ico: '02216973'
  since: 2013
  competes: direct
  maturity: established
  evidence: 'A Prague firm selling bank-transaction data prepared for credit decisions: verified
    income, sorted expenses and risk flags such as gambling and payday loans, marketed for the new
    EU consumer-credit rules. Named customers include the Czech buy-now-pay-later firm Twisto,
    quoted on the page, with Erste, Raiffeisen and UniCredit among its logos. It sells the inputs to
    the check rather than the lending decision. Founded October 2013 [S11].'
- name: CRIF – Czech Credit Bureau (NEOS)
  url: https://www.crif.cz/sluzby/business-inteligence-reseni/open-banking-data/
  ico: '26212242'
  competes: direct
  maturity: early
  evidence: 'Offers NEOS, which reads payment accounts with the borrower''s consent to speed up the
    creditworthiness check, sorts the transactions and builds a credit score. The page names no
    customer and no launch year, so for this product it counts as new; the company itself has
    traded since November 2000 [S11].'
- name: Finbricks
  url: https://www.finbricks.com/
  ico: '10669205'
  since: 2021
  competes: adjacent
  maturity: established
  evidence: 'Sells raw account information, transaction history and payment initiation, as part of
    the Komerční banka group. Named customers on its site include GoPay, ThePay and Essox. It offers
    no credit score or affordability decision, so a builder would buy its data rather than compete
    with it. Founded March 2021 [S11].'
- name: SOLUS
  url: https://www.solus.cz/
  ico: '69346925'
  since: 1999
  competes: adjacent
  maturity: established
  evidence: 'An association of lenders and utilities that runs registers of people''s and firms''
    payment history, which lenders query before lending. Its members are its named customers,
    Raiffeisenbank, UniCredit Bank and Home Credit among them. It reports whether someone paid in
    the past, not what they earn and spend now. Registered June 1999 [S11].'
process:
  summary:
    today: 'A lender takes the income and expenses the borrower declares, or flat-rate amounts, and may not check them against a bank statement it already holds [S7].'
  steps:
  - who: Borrower
    today: 'Declares income and expenses on the application'
    known: documented
    cites: [7]
    change: changes
    after: 'Shares bank data with consent instead'
  - who: Lender
    today: 'Uses declared or flat-rate expenses'
    known: documented
    cites: [7]
    change: changes
    after: 'Reads expenses from the bank transactions'
  - who: Lender's staff
    today: 'Leaves declared expenses unchecked against statements'
    known: documented
    cites: [7]
    change: changes
    after: 'Reviews only the items software flags'
  - who: '?'
    today: 'How the check is kept for later disputes is not known'
    known: unknown
    cites: []
    change: changes
    after: 'Keeps each check as evidence for disputes'
sources:
- type: regulation
  name: 'Directive (EU) 2023/2225 on consumer credit'
  gist: 'the EU rules and their date'
  why: 'The new EU consumer-credit directive: member states apply it from 20 November 2026; it requires a thorough check of income and expenses before lending, based on verified information, and forbids social-network data.'
  url: https://eur-lex.europa.eu/eli/dir/2023/2225/oj
  note: 'reg-ccd2-consumer-credit. Text read 2026-09-18 via EUR-Lex CELEX 32023L2225. Art 48(1):
    "adopt and publish, by 20 November 2025 ... They shall apply those measures from 20 November
    2026." Art 18(1): the creditor carries out "a thorough assessment of the consumer''s
    creditworthiness"; Art 18(3): based on "relevant and accurate information on the consumer''s
    income and expenses", "appropriately verified"; "Social networks shall not be considered as an
    external source". Art 18(6): credit made available only where the assessment indicates the
    obligations "are likely to be met". Art 2(2)(h): the deferred-payment exclusion covers only a
    supplier giving time to pay "without a third party offering credit", interest-free, within 50
    days (14 days for large online sellers), so third-party buy-now-pay-later is in scope.'
  date: '2026-11-20'
  signal: reg-ccd2-consumer-credit
- type: regulation
  name: 'Sněmovní tisk 145 — the Czech consumer-credit amendment'
  gist: 'the bill and its status'
  why: 'The Czech bill that brings in the EU rules: the government sent it to the lower house on 25 March 2026, and the house passed it in third reading on 11 September 2026; it had not yet reached the Senate.'
  url: https://www.psp.cz/sqw/historie.sqw?o=10&t=145
  note: 'psp.cz bill history read 2026-09-18: "Novela z. o spotřebitelském úvěru - EU"; "Vláda
    předložila sněmovní návrh zákona 25. 3. 2026"; 1st reading 22–23 Apr 2026, 2nd 25 Jun 2026,
    3rd reading 11 Sep 2026 at the 29th session, "Návrh zákona schválen" (vote 104); the approved
    text "se připravuje k zveřejnění a předání do dalších kroků legislativního procesu" — not yet
    with the Senate. Transposition deadline was 20 Nov 2025 (S1), so Czechia is late. Supersedes
    the Feb 2025 inter-ministerial draft held as reg-ccd2-bnpl-2026.'
  date: '2026-09-11'
- type: regulation
  name: 'Finance ministry — the lower house passes the consumer-credit bill'
  gist: 'the February 2027 start'
  why: 'The ministry expects the law to take effect on 1 February 2027; shops selling on interest-free instalments up to about 50,000 CZK get a simpler check that can pull income and expense data from employers'' monthly reports, bank data shared with consent and debtor registers; small short-term loans get no presumption of creditworthiness.'
  url: https://mf.gov.cz/cs/ministerstvo/media/tiskove-zpravy/2026/snemovna-schvalila-vyssi-ochranu-spotrebitelu-nove-65160
  note: 'MF press release dated 11.09.2026, read 2026-09-18: "zákon by měl nabýt účinnosti 1. února
    2027"; a "zjednodušený režim posuzování úvěruschopnosti" for interest-free goods sold on
    instalments, capped at about "50 tisíc korun" (e.g. mobile phones); sellers may get income and
    expense data automatically "z jednotného měsíčního hlášení zaměstnavatele, z bankovních údajů
    se souhlasem spotřebitele a z dlužnických registrů"; a new "domněnka úvěruschopnosti" for
    fully repaid loans does not apply to small short-term credit, where the lender must always
    prove repayment capacity. The release body says "dnes 26. srpna 2026", contradicting its own
    date line and psp.cz; 11 Sep 2026 is used.'
  date: '2026-09-11'
- type: news
  name: 'ČTK — lower house approves stricter consumer-credit rules'
  gist: 'the vote and what it covers'
  why: 'Wire report of the vote: 134 of 136 deputies present voted for; interest-free credit now needs a creditworthiness check; a deferred payment may not exceed the average wage; social-network data is banned from the check; the start moves to 1 February 2027.'
  url: https://www.ceskenoviny.cz/zpravy/snemovna-schvalila-prisnejsi-podminky-pro-spotrebitelske-uvery/2873058
  note: 'ČTK, 11 Sep 2026, read 2026-09-18: "Směrnice dopadá i na úvěry zdarma, poskytovatelé
    budou muset i v takovém případě posuzovat úvěruschopnost klientů"; a deferred payment "nebude
    smět přesáhnout průměrnou mzdu v celé ekonomice za první až třetí čtvrtletí předcházejícího
    roku"; effective date moved to 1 February on a proposal by Vojtěch Munzar (ODS); 134 of 136
    present in favour. Cites urgency only.'
  date: '2026-09-11'
  dims: [urgency]
- type: news
  name: 'KPMG — buy-now-pay-later becomes full consumer credit'
  gist: 'what BNPL firms now owe'
  why: 'A Big Four firm''s note: every buy-now-pay-later product where a third party lends falls under the full consumer-credit law, with a creditworthiness check on each buyer and a central-bank licence or registration.'
  url: https://danovky.cz/cs/kup-ted-zaplat-pozdeji-sluzby-bnpl-budou-nove-jako-plnohodnotny-spotrebitelsky-uver
  note: 'KPMG Česká republika on danovky.cz, 1 Jun 2026, read 2026-09-18: "Nově spadnou všechny BNPL
    produkty, u nichž úvěr poskytuje třetí osoba odlišná od obchodníka, pod plnou působnost zákona o
    spotřebitelských"; obligations: individual creditworthiness assessment from income, expenses,
    liabilities and registers; ČNB licensing or registration. Written before the start moved to
    1 Feb 2027 (it states 20 Nov 2026). Cites urgency only.'
  date: '2026-06-01'
  dims: [urgency]
- type: statistic
  name: 'Czech National Bank — supervision report 2025'
  gist: 'the regulator''s findings and fines'
  why: 'The central bank supervised 73 non-bank lenders in 2025, found less serious systemic shortcomings in how point-of-sale lenders verify income, debts and expenses, fined non-bank lenders 19M CZK in ten final decisions, and saw their complaints rise over 70% in a year.'
  url: https://www.cnb.cz/export/sites/cnb/cs/dohled-financni-trh/.galleries/souhrnne_informace_fin_trhy/zpravy_o_vykonu_dohledu/download/dnft_2025_cz.pdf
  note: 'ČNB Zpráva o výkonu dohledu nad finančním trhem 2025, §3.10, read 2026-09-18 (publication
    date not on the pages read; dated here by the read). "V roce 2025 dohlížela ČNB na 73
    nebankovních poskytovatelů spotřebitelského úvěru"; new licence applications show "využití
    nových technologií a automatizace zpracování dat, zejména při posuzování úvěruschopnosti"; at
    selected lenders of tied credit ČNB "Zjistila méně závažné systémové nedostatky v ověřování
    příjmů a finančních závazků spotřebitele a také nedostatky ve zjišťování a ověřování výdajů";
    ten decisions became final in 2025, all with a fine, the largest 8 mil. Kč (Provident Financial),
    "Celková výše uložených pokut v tomto sektoru činila 19 010 tis. Kč" — not all ten are stated
    to concern the creditworthiness check; complaints to non-bank lenders "vzrostl o více než 70 %"
    while lending grew "o necelých 13 %", driven by lawyers challenging loan-contract validity.'
  date: '2026-09-18'
  dims: [demand]
- type: complaint
  name: 'Czech National Bank — 4M CZK fine for unchecked incomes and expenses'
  gist: 'one lender''s 4M CZK fine'
  why: 'A central-bank decision fining a consumer lender 4M CZK: its goods and car financing could be granted without proof of income, it took expenses from flat amounts or the borrower''s own figures, and it did not check declared expenses even when it held the bank statement.'
  url: https://www.cnb.cz/export/sites/cnb/cs/dohled-financni-trh/.galleries/prilohy/S-Sp-2024_00105_CNB_658.pdf
  note: 'ČNB rozhodnutí č.j. 2025/66794/650 of 9 June 2025, sp.zn. Sp/2024/105/658, party ESSOX
    s.r.o. (IČO 26764652), read 2026-09-18. Products "Financování zboží" and "Financování
    automobilů" could be granted "bez doložení a ověření příjmů spotřebitele"; for real expenses it
    "bez dalšího vycházela z paušálně stanovených částek nebo z hodnot deklarovaných spotřebitelem";
    footnote 47: "Deklarované výdaje účastník řízení manuálně neověřuje, a to ani v případě, kdy mu
    v rámci doložení příjmů byl poskytnut výpis z bankovního účtu. Jedinou výdajovou položkou,
    kterou zaměstnanci účastníka řízení kontrolují, jsou výdaje na gambling." Fine "4 000 000 Kč"
    under § 154(3)(c) of Act 257/2016 as in force to 31.12.2023. One lender: shows what can happen.'
  date: '2025-06-09'
  dims: [demand]
- type: complaint
  name: 'Financial arbiter — annual report 2025'
  gist: 'disputes traced to weak checks'
  why: 'The state''s out-of-court forum for financial disputes opened 12,050 cases in 2025, 11,386 of them about consumer credit, and names systemic problems above all in how lenders assess creditworthiness.'
  url: https://finarbitr.gov.cz/cs/informace-pro-verejnost/aktuality/vyrocni-zprava-financniho-arbitra-za-rok-2025-425.html
  note: 'fa-spotrebitelske-uvery; page read 2026-09-18: "V roce 2025 bylo před finančním arbitrem
    zahájeno celkem 12.050 řízení"; consumer credit "zahájeno 11.386 řízení"; systemic problems
    "především při posuzování úvěruschopnosti klientů". The same caseload, seen from the lender
    answering each case, is a separate problem on this register; here it is cited only as
    evidence that the check at origination fails.'
  date: '2026-05-29'
  signal: fa-spotrebitelske-uvery
  dims: [demand]
- type: arbitrage
  name: 'Algoan'
  gist: 'French bank-data credit scores'
  why: 'A Paris company that turns a borrower''s bank transactions into a credit score and affordability decision for consumer lenders and buy-now-pay-later, used by large French consumer lenders.'
  url: https://mind.eu.com/fintech/services-bancaires/open-banking/michael-diguet-algoan-veut-devenir-le-leader-europeen-du-score-open-banking-de-credit
  note: 'fr-algoan (mind Fintech, 2025-01-22): profitable, aiming for EUR 5M ARR in H1 2025;
    25 lenders signed in 2021 incl. Alma, Cetelem, Cofidis, Oney, Floa (mind Fintech 2021). Site
    read 2026-09-18 (algoan.com/en): ACPR-registered AISP; credit score, affordability, BNPL use
    case; logos incl. Revolut, BNP Paribas, Cofidis, Alma, Franfinance. French company register
    (recherche-entreprises.api.gouv.fr, per the 2026-09-18 research pass): SIREN 832872436,
    created 9 Oct 2017 — the signal''s "founded 2018" is corrected to 2017 on the comps row.'
  date: '2025-01-22'
  signal: fr-algoan
- type: arbitrage
  name: 'Tink — Income Check'
  gist: 'Swedish income check from bank data'
  why: 'A Stockholm company, part of Visa, whose Income Check verifies a borrower''s income from the bank account through an API, with Nordic lenders named as customers.'
  url: https://tink.com/products/income-check/
  note: 'Read 2026-09-18: "Income Check lets you verify an end-user''s income directly from their
    bank account through an API"; named customers Bank Norwegian and GF Money; 19 European
    countries, 3,000+ bank connections. tink.com/about-us: "Tink was founded in 2012", Stockholm,
    "became part of Visa in 2022". No launch year for Income Check itself is given; since is the
    company''s founding year.'
  date: '2026-09-18'
- type: gap-check
  name: 'Czech check — bank-data checks already sold here'
  gist: 'the Czech field, searched'
  why: 'Czech-language search, the state business register and our own funding ledger: two established firms already sell income and expense checks from bank data to Czech lenders, a credit bureau offers a new one, and two more sell the data or the payment history around it.'
  url: https://www.kontomatik.com/cz/podporujeme-rozvoj-firem-technologii-otevreneho-bankovnictvi
  note: 'Gap check 2026-09-18, two passes (the arb-scan harvest noted on fr-algoan, and a research
    pass for this problem). FOUND, DIRECT, ESTABLISHED: Kontomatik — Czech-language page "ověřujte
    příjmy a výdaje zákazníků během několika sekund"; kontomatik.com lists Czech Republic among its
    markets, "15+ years on the market", "150+ customers", testimonials Aasa Polska, Finiata,
    Raiffeisen Digital Bank, Smartney, simpl.rent, logos incl. Revolut, Alior, PKO BP, Allegro Pay;
    AISP authorised by the Bank of Lithuania and the Polish KNF; ARES name search "Kontomatik"
    returns 0 Czech entities; no Czech customer named. since 2011 is the latest year consistent
    with "15+ years" read in 2026, not a stated founding year. Dateio s.r.o. (IČO 02216973, ARES
    datumVzniku 2013-10-15) — tapix.io/solutions/smart-data-for-credit-scoring: "verified income,
    categorised expenses, and surfaced risk flags", positioned for CCD2 creditworthiness checks incl.
    micro-credit under EUR 200; Twisto testimonial (Pavel Prucek, about customers seeing what they
    paid for), logos incl. Erste, Raiffeisen, UniCredit, OTP, Société Générale; priced per client or
    per transaction with a 12+ month commitment, no figure. FOUND, DIRECT, EARLY: CRIF – Czech
    Credit Bureau, a.s. (IČO 26212242, ARES 2000-11-21) — crif.cz open-banking page: NEOS gives
    "přístup k platebním účtům s cílem urychlit hodnocení úvěruschopnosti", transaction
    categorisation, "inovativní úvěrové skóre"; no customer, launch year or price named. FOUND,
    ADJACENT: Finbricks, s.r.o. (IČO 10669205, ARES 2021-03-25), KB group, account information and
    payment initiation, logos GoPay, ThePay, PatronGo, GPE, Essox, no scoring product; SOLUS,
    zájmové sdružení právnických osob (IČO 69346925, ARES 1999-06-18), payment-history registers,
    member logos incl. Raiffeisenbank, UniCredit, Home Credit. Also seen: Raiffeisenbank terms
    (lawinsider.com) showing it verifies applicants'' accounts in-house — a buyer building its own,
    not a seller. ARES-only, products not checked: Profinit EU (04434081), Datamole (03742709),
    Algotech (24775487), Dun & Bradstreet CZ (63078201), SPENDEE (05912890). No public Czech price
    for a bank-data check (SOLUS publishes only consumer self-check prices). METHOD NOTE: the
    descriptive Czech queries below surfaced none of Kontomatik, Tapix or CRIF NEOS — all three
    were found by name — so descriptive-query recall on this market is poor; the web-search tool
    is not google.cz. POSITIVE CONTROL: run by the arb-scan harvest 2026-09-18 — the descriptive
    Czech query "TMS systém řízení přepravy tendrování dopravců česká firma" surfaced Ringil without
    naming it (PASSED); ARES name search "Wultra" returned Wultra s.r.o. IČO 03643174 (PASSED). Not
    re-run in the research pass (search budget spent). Gap 0 rests on the named established direct
    players, not on an absence.'
  date: '2026-09-18'
  queries:
    - "posouzení úvěruschopnosti z bankovních transakcí open banking scoring API pro poskytovatele úvěrů"
    - "skóring žadatele o úvěr z transakční historie účtu PSD2 AIS česká fintech nebankovní poskytovatelé"
    - "ověření příjmů žadatele přes bankovní účet open banking pro nebankovní poskytovatele půjček česká služba"
    - "ověření příjmu přes bankovní účet API pro nebankovní poskytovatele úvěrů"
    - "kategorizace transakcí scoring úvěruschopnost software česká firma"
    - "BNPL posouzení úvěruschopnosti řešení pro e-shopy bankovní data"
    - "open banking scoring Česko startup analýza výpisu z účtu"
    - "automatická analýza bankovních výpisů pro poskytovatele úvěrů ověření bonity software Česko"
    - "\"úvěruschopnost\" \"PSD2\" služba pro věřitele"
    - "licence AISP ČNB úvěrové skóre fintech"
    - "Finbricks open banking API česká firma licence ČNB poskytovatel informací o účtu"
  checked: [google-cz, ares, own-funded-ledger]
  expires: '2026-12-17'
- type: regulation
  name: 'Finance ministry — impact assessment of the consumer-credit bill'
  gist: 'what the new rules cost'
  why: 'The ministry''s impact assessment: banks of similar size put the cost of adapting their IT at 5M to 120M CZK, and no count exists of the shops that lend or arrange interest-free credit and now fall under the rules.'
  url: https://www.zakonyprolidi.cz/media2/file/2502/File73658.pdf
  note: 'RIA (Závěrečná zpráva z hodnocení dopadů regulace) to the MF draft amending Act 257/2016,
    mirrored from odok.cz attachment KORNDDVHGXTK, read 2026-09-18: banks'' estimates for adapting
    internal IT systems "v intervalu od 5 až do 120 milionů Kč, přičemž se jednalo o banky podobné
    velikosti"; merchants giving or arranging interest-free credit (e.g. BNPL) "se nově dostane do
    plné působnosti směrnice ... Statistika o počtu takových subjektů přitom není k dispozici"; a
    non-bank lender licence carries "požadavek kapitálu ve výši 20 milionů Kč". Dated to the draft''s
    February 2025 posting (the veklep record on p-0027). Cites urgency by type; the figures are
    context, not a price receipt.'
  date: '2025-02-14'
created: '2026-09-18'
updated: '2026-09-18'
---

Czech lenders must check that a borrower can repay, and the central bank keeps finding lenders that skip part of the check [S6,S7].

- One lender was fined 4M CZK for taking expenses on the borrower's word [S7].
- Complaints to non-bank lenders rose over 70% in a year [S6].
- The financial arbiter traces loan disputes above all to weak checks [S8].

The check is the creditworthiness assessment: before lending, the lender looks at what the borrower earns, owes and spends [S1].

- The central bank looked at lenders that finance goods at the point of sale. It found less serious but systemic shortcomings in how they verify income, debts and expenses [S6].
- In the fined case, goods and car loans could be granted without proof of income, and expenses came from flat amounts or the borrower's own figures [S7].
- That lender did not check declared expenses even when it already held the borrower's bank statement [S7].
- The central bank supervises 73 non-bank lenders, and new applicants increasingly automate the data work, above all the creditworthiness check [S6].
- The complaints rose while lending grew under 13%, driven by lawyers who invite borrowers to challenge their loan contracts [S6].
- The financial arbiter, the state's out-of-court forum for money disputes, opened 12,050 cases in 2025, 11,386 of them about consumer credit [S8].

Existing non-solutions: Two established firms already sell income and expense checks from bank data to Czech lenders [S11].

- A Polish firm checks income and expenses in seconds, on a Czech page [S11].
- A Prague firm sells verified income, sorted expenses and risk flags [S11].
- The Czech credit bureau also offers a bank-data credit score [S11].

Two more firms sell what sits around the check: one the raw account data and payments, one the registers of past repayments [S11]. No Czech price for a bank-data check is published [S11]. The rows are under [Competition](#competition).

Why now: Buy-now-pay-later firms and shops selling on interest-free instalments must run the same check once the Senate passes the bill [S2,S3].

- Buy-now-pay-later firms need a central-bank licence and a full check on every buyer [S5].
- A shop selling phones on instalments must check the buyer's income and spending [S3].
- On small short-term loans the lender must always prove the check was sound [S3].

The dates and rules behind this:

- The EU directive applies from 20 November 2026, and Czechia missed its November 2025 deadline to write it into law [S1,S2].
- On 11 September 2026 the lower house passed the Czech bill, 134 of the 136 deputies present voting for it [S2,S4]. It still has to pass the Senate [S2].
- The finance ministry expects the law to take effect on 1 February 2027 [S3,S4].
- The check must rest on verified information about income and expenses, and the lender may lend only if the result says the borrower can likely repay [S1].
- Every buy-now-pay-later product where a third party lends falls under the full law [S1,S5].
- Interest-free credit needs the check too, a deferred payment may not exceed the average wage, and social-network data is banned [S4].
- For interest-free instalment sales up to about 50,000 CZK, a shop may fetch the data from employers' monthly reports, bank data shared with consent and debtor registers [S3].
- A borrower who repaid in full is presumed able to repay, but that does not cover small short-term loans [S3].
- Nobody counts the shops that lend or arrange interest-free credit, so the number newly covered is unknown [S12].

Who pays: Lenders pay for the check themselves, and today they also pay fines when it falls short [S6,S7].

- 19M CZK in fines hit non-bank lenders in ten decisions in 2025 [S6].
- Banks put their IT cost of the rules at 5M to 120M CZK [S12].
- No Czech price for a bank-data check is public yet [S11].

The largest single fine in 2025 was 8M CZK [S6]. Not all ten fines are stated to be about the creditworthiness check [S6]. The bank estimates came from banks of similar size, which is how far apart they were [S12]. A non-bank lender also needs 20M CZK of its own capital for its licence [S12].

Solved elsewhere: In France and Sweden, lenders already buy income and affordability checks read from bank data [S9,S10].

In France a company turns a borrower's bank transactions into a credit score and an affordability decision for consumer lenders and buy-now-pay-later [S9]. Large French consumer lenders use it, and by early 2025 it was profitable [S9]. In Sweden a company that is now part of Visa verifies a borrower's income straight from the bank account, with Nordic lenders named as customers [S10]. See [Validated abroad](#validated-abroad).

## First moves

1. Build a check for shops selling on interest-free instalments that reads the buyer's bank data and returns a yes or no with its reasons. The bill gives these shops a simpler check that may use bank data shared with consent, and nobody counts how many of them there are; see [Why now](#why-now). Start with one electronics or phone seller that already offers instalments, run your check beside its current one for a month, and show where the two disagree.
2. Call the heads of risk at mid-size non-bank lenders and ask what the central bank found in their checks. Ask too what they pay for bank data today. The regulator's findings and fines are under [The opportunity](#opportunity) and [Willing to pay](#willing-to-pay), and those findings are what a lender has to fix. Ask each one which seller under [Competition](#competition) they already use and what it leaves them to do by hand.
3. Build on a licensed account-data provider's feed rather than reading bank accounts yourself. The firms under [Competition](#competition) include one that sells raw account data and no score, and buying from it spares you the central bank's authorisation; see [Execution difficulty](#execution-difficulty).
4. Keep every check as a file the lender can show the central bank or the financial arbiter later. On small short-term loans the lender must always prove its check was sound, as [Why now](#why-now) explains, so a kept check is worth as much as the decision.

## Revisions

2026-09-18 · record created — Created from the CCD2 cluster: the French comparable fr-algoan and the regulation signals reg-ccd2-consumer-credit and reg-ccd2-bnpl-2026, plus sources fetched for this problem and cited directly rather than written to the ledgers (the lower-house bill history, the finance ministry's release and impact assessment, the ČTK and KPMG notes, the central bank's 2025 supervision report and its ESSOX decision, Tink's product page) [S2,S3,S4,S5,S6,S7,S10,S12]. Kept apart from the lender's-side arbiter caseload problem: that one answers disputes after the loan; this one is the check before it, bought by the same lenders and newly by buy-now-pay-later firms and instalment sellers [S5,S8]. Scores: proof 3 on two established sellers in France and Sweden, Sweden being Nordic [S9,S10]; money 0, no public budget near; urgency 3, the start on 1 February 2027 is under 18 months away and the sources are fresh [S2,S3]; demand 2 on the regulator's recurring findings, a fine and the arbiter's report [S6,S7,S8]; gap 0 because two established firms already sell the check here [S11]. Status watching under the de-rank rule. No draft-law badge: the fines and findings arise under the law in force today, and the pending bill widens the check rather than creating the pain [S6,S7]; the bill's status is stated in Why now. Flagged as inference: Kontomatik's since 2011 is the latest year consistent with its own "15+ years on the market", not a stated founding year [S11]. Corrected against the sources: the French comparable's company was registered in October 2017, not 2018 as the signal says [S9]; the ministry's release is dated 11 September 2026 although its body says 26 August [S3]. The 19M CZK of fines covers ten decisions not all stated to concern the check, so the brief says fined, not fined for this [S6]. Descriptive Czech searches did not surface the three direct sellers, which were found by name; the positive control is the harvest's own [S11].
