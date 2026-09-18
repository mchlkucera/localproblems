---
id: p-0040
region: cz
title: 'Czech hotels and guesthouses report the same guests to several authorities. A bill would merge this into one register in 2028.'
brief: 'Hosts send the same guest details to the foreign police, the town and the statistics office, each in its own way [S1,S3]. A bill would replace this with one state register from January 2028 [S4].'
solution: 'Build an online guest check-in that files each guest once to the foreign police, the town''s fee records and the statistics office, and later to the new register, as 1 company already does in Spain.'
good_for: 'Someone who can connect software to state systems and likes working with hosts.'
category: retail-services
geo: CZ-national
score: 7
scores:
  proof: 2
  money: 1
  urgency: 2
  demand: 2
  gap: 0
status: watching
entry:
  level: moderate
  buyer: small-firms
  permission: none
  incumbents: direct
  integration: national-system
  money: bootstrap
  why: 'Easier: hosts buy it themselves, and no licence is needed to sell it. Harder: it must connect to the police reporting system and later to the state register, and established hotel software already files for hotels.'
comps:
- name: Chekin
  url: https://chekin.com/en/
  geo: ES
  since: 2017
  traction: 'Automated guest registration, filing to the authorities and tourist-fee calculation;
    trusted by more than 200,000 properties and over 25 million check-ins, in more than 45
    countries, with named filing for Spain, Italy, Portugal and the Czech Republic (chekin.com,
    read 2026). Chekin Soluciones Digitales S.L., Seville, founded May 2017 (empresia.es)'
  markets: [IT, PT, CZ]
locals:
- name: Previo
  url: https://www.previo.cz/
  ico: '25975234'
  since: 2004
  competes: direct
  maturity: established
  evidence: 'Sells hotel software for hotels, guesthouses and apartments; its foreign-guest book
    sends foreign guests to the foreign police by hand or automatically. Public customer count:
    5,573 clients, and it calls itself the most used hotel system in Czechia; developed since 2004
    (previo.cz, read 2026) [S9].'
- name: Chekin
  url: https://chekin.com/cs/
  since: 2017
  competes: direct
  maturity: established
  evidence: 'The Spanish check-in service sells in Czech: online check-in, sending guest data to the
    authorities through the police system and the planned state register, an electronic guest book
    and tourist-fee calculation. Trusted by more than 200,000 properties worldwide, by its own count;
    founded in Seville in 2017 [S10].'
- name: Best Guest
  url: https://bestguest.cz/
  ico: '06723756'
  competes: direct
  maturity: early
  evidence: 'Sells online guest registration, self check-in and foreign-police reporting for Airbnb
    hosts and hotels, charged per completed check-in. It publishes no customer count [S9].'
- name: Trevlix
  url: https://www.trevlix.cz
  ico: '14091887'
  competes: direct
  maturity: early
  evidence: 'Sells booking software for small hosts with automatic foreign-guest reporting to the
    police system, from 90 CZK a month after 30 free days. It publishes no customer count [S9].'
- name: Checkinn.cz
  url: https://www.checkinn.cz/ubyport
  ico: '17613485'
  competes: direct
  maturity: early
  evidence: 'Sells foreign-guest reporting to the police system for hosts, priced by the month. Its
    company was registered in October 2022, and it publishes no customer count [S9].'
- name: Superhostem
  ico: '29503825'
  competes: direct
  maturity: early
  evidence: 'Sells online check-in, a digital guest book, local-fee records and a connection to the
    police system for apartment hosts, with three months free. It publishes no customer count [S9].'
- name: Ubytovačka (Evidence hostů)
  url: https://ubytovacka.cz/
  ico: '23427078'
  competes: direct
  maturity: early
  evidence: 'Sells a booking system with foreign-guest reporting, the guest book and the records for
    the local fee in one place, from 69 CZK a month. Its company was registered in 2025 [S9].'
- name: ubytovaci-kniha.cz
  url: https://www.ubytovaci-kniha.cz/
  competes: direct
  maturity: early
  evidence: 'Sells a desktop and web guest-book program for hosts, 1,200 CZK for a licence and then
    600 CZK a year. Whether it files to the police system itself was not confirmed [S9].'
- name: Hostivio
  url: https://hostivio.cz/en/ubyport/
  competes: direct
  maturity: early
  evidence: 'Sells automatic foreign-guest reporting through the police system''s newer interface.
    No company number was found in the state business register [S9].'
- name: Vezpa
  url: https://vezpa.it/cz/blog/ubyport-automaticke-hlaseni/
  competes: direct
  maturity: early
  evidence: 'A host tool from Italy with a Czech page; it says its automatic sending to the police
    system is being finished [S9].'
process:
  summary:
    today: 'Reception staff record each guest, retype foreign guests into the police system within 3 working days, and keep separate records for the town''s fee and the statistics office [S1,S3,S5].'
  steps:
  - who: Reception
    today: 'Records each guest on arrival'
    known: documented
    cites: [1]
    change: changes
    after: 'The guest fills in details online first'
  - who: Reception
    today: 'Retypes foreign guests into the police system'
    known: documented
    cites: [3, 5]
    reenters: true
    change: changes
    after: 'The check-in files the police report itself'
  - who: The host
    today: 'Keeps separate records for the town''s fee'
    known: documented
    cites: [1]
    reenters: true
    change: changes
    after: 'The fee records fill from the same check-in'
  - who: The host
    today: 'Reports guest numbers to the statistics office'
    known: documented
    cites: [1]
    change: changes
    after: 'Statistics come from the same records'
  - who: '?'
    today: 'How private apartment hosts file today is not known'
    known: unknown
    cites: []
    change: changes
    after: 'A phone check-in covers hosts without software'
sources:
- type: regulation
  name: "eTurista bill — the ministry's impact assessment"
  gist: "the state's own diagnosis"
  why: "The regional-development ministry's impact assessment says hosts file the same guest data to several authorities, counts 10,012 collective establishments, and estimates about 190M CZK of one-off costs for hotels to connect to the new register."
  url: https://www.odok.cz/portal/services/download/attachment/ALBSDXWLCRBA/
  note: 'reg-eturista-registr-ubytovani-2028: RIA to the Tourism Act amendment (VeKLEP
    ALBSDXWJ7VQX, in comment procedure from 14 September 2026), downloaded 2026-09-18 with a
    browser user agent and read in full. Verbatim: "Poskytovatelé ubytování plní souběžně
    evidenční, oznamovací a statistické povinnosti podle několika právních předpisů";
    "neodůvodněnou zátěž v podobě opakovaného zadávání stejných údajů vůči jednotlivým složkám
    státu"; "V ČR bylo dle dat ČSÚ v r. 2025 provozováno 10 012 HUZ s 217 701 pokoji a 562 467
    lůžky" and the true count is much higher; nearly 8 million nights via Airbnb, Booking, Expedia
    Group or Tripadvisor in 2024; STR hosts cannot be found "v žádné úředně vedené evidenci".
    MMR survey of 236 hotels: 3.9 staff on guest registration on average, 80% use a hotel system,
    more than 35 different systems named; adapting a system about 20,000 CZK, 160M CZK in total,
    training 30M CZK, "kolem 190 000 000 Kč" one-off. Register run by MMR: data environment 1.3M
    CZK, operation about 960,000 CZK a month, 30M CZK from the National Recovery Plan. ORP towns
    get about 44,709,620 CZK or about 47,970,000 CZK (the RIA gives both). The RIA gives no hours or
    CZK per host per year ("nelze určit obecně"). Effect 1 January 2028; still a draft, so the
    deadline scores 1. The state''s own statement of the duplicate burden also backs demand.'
  date: '2028-01-01'
  signal: reg-eturista-registr-ubytovani-2028
  dims: [urgency, demand]
- type: regulation
  name: "EU Regulation 2024/1028 on short-term rentals"
  gist: "the EU data-sharing rule"
  why: "Since 20 May 2026 platforms must display hosts' registration numbers and share activity data with the authorities wherever a country runs a registration scheme; Czechia does not run one yet."
  url: https://eur-lex.europa.eu/eli/reg/2024/1028/oj
  note: 'reg-str-registration: Regulation (EU) 2024/1028, applies from 20 May 2026 (Art. 19),
    in force since June 2024. The RIA confirms it is directly applicable but needs national
    adaptation, and that no Czech registration procedure operates yet.'
  date: '2026-05-20'
  signal: reg-str-registration
- type: regulation
  name: "Foreigners' Residence Act § 102 — reporting a foreign guest"
  gist: "the 3-working-day rule"
  why: "A host must report every foreign guest to the police within 3 working days of arrival."
  url: https://www.zakonyprolidi.cz/cs/1999-326
  note: 'Zákon 326/1999 Sb., § 102(1), read 2026-09-18: "Ubytovatel je povinen oznámit ubytování
    cizince do 3 pracovních dnů po jeho ubytování; oznámení učiní útvaru policie." The bill makes
    a register entry count as this report and as the domovní kniha. Context for the process;
    backs no score.'
  date: '2026-09-18'
  dims: []
- type: regulation
  name: "eTurista bill — the text"
  gist: "the 24-hour rule and fines"
  why: "The bill would take effect on 1 January 2028, require each guest to be entered within 24 hours, and fine a private host up to 100,000 CZK and a platform up to 10M CZK."
  url: https://www.odok.cz/portal/services/download/attachment/ALBSDXWLCP2Z/
  note: 'Bill text read 2026-09-18: § 9h(2) the host enters the guest "bezprostředně po" arrival,
    "nejpozději však do 24 hodin"; § 10c(3) fines "a) 100 000 Kč" (a natural person acting as
    host, § 10c(2)) and "b) 1 000 000 Kč" (§ 10c(1)); § 10b(11)(d) "10 000 000 Kč" for a platform;
    "Tento zákon nabývá účinnosti dnem 1. ledna 2028." Draft in comment procedure.'
  date: '2028-01-01'
  dims: []
- type: news
  name: "Podnikatel.cz — hoteliers welcome eTurista but fear the cost"
  gist: "retyping and upgrade fears"
  why: "A Prague hotel director says receptionists already retype guest details into the police system; a guesthouse owner fears a new booking system costing tens of thousands of crowns; the hotel association has long called for equal rules."
  url: https://www.podnikatel.cz/clanky/eturista-jako-alternativa-eet-vetsina-hotelieru-zmeny-vita-ale-ma-i-obavy/
  note: 'Podnikatel.cz, 16 September 2024, read from the research pass''s saved copy 2026-09-18:
    Miroslav Bukva, GM of Aquapalace Hotel Prague: "Již nyní recepční povinně přepisují požadované
    údaje o bydlících do domovní knihy, respektive do systému Ubyport"; Tomáš Macek, Penzion
    Kvilda – Luční: "budou ubytovatelé nuceni měnit rezervační systém, což jsou náklady v
    desítkách tisíc (program, zaškolení, poplatky atd.)" and "denní ruční přepisování" from
    Booking and Airbnb into the state system; Václav Stárek, AHR ČR president: "místo třech
    hlášení systém zajistí přenos relevantních informací automaticky", and the association has
    long called for equal rules for all accommodation. Demand receipt.'
  date: '2024-09-16'
  dims: [demand]
- type: news
  name: "Česká justice — towns lose fees on unreported stays"
  gist: "the 55M CZK fee gap"
  why: "The ministry says towns lose about 55M CZK a year in unpaid accommodation fees, and that 40–70% of stays booked through online platforms went unreported."
  url: https://www.ceska-justice.cz/2024/09/bic-v-podobe-platformy-eturista-ceka-hotely-a-penziony-pristi-rok-cast-provozovatelu-je-vsak-proti/
  note: 'Česká justice, 27 September 2024, MMR spokesperson: "Obce navíc tratí asi 55 milionů za
    rok na poplatcích z pobytu"; "zhruba 40 až 70 procent pobytů přes online platformy nebylo
    nahlášených"; the state may lose almost 800M CZK a year in taxes (ministry calculation, not
    used here). Demand receipt.'
  date: '2024-09-27'
  dims: [demand]
- type: news
  name: "Podnikatel.cz — the new government's eTurista bill"
  gist: "the bill's status"
  why: "The ministry sent the eTurista bill out for comments in September 2026, with effect from 2028; the previous government's version was never passed by parliament."
  url: https://www.podnikatel.cz/clanky/take-babisova-vlada-chce-aby-se-do-eturisty-registrovaly-jak-hotely-tak-airbnb/
  note: 'Podnikatel.cz, 17 September 2026: "MMR poslalo do připomínkového řízení návrh novely";
    "Pokud novela projde legislativním procesem, měla by nabýt účinnosti na začátku ledna 2028";
    the Fiala government''s version "Do konce volebního období však novelu ve Sněmovně neprojednala
    ve třetím čtení". Status context; dims empty.'
  date: '2026-09-17'
  dims: []
- type: contract
  name: "Registr smluv — the ministry orders the eTurista system"
  gist: "the 34M CZK build contract"
  why: "The regional-development ministry signed about 34.4M CZK including VAT with a software firm to build the eTurista system, and has amended the contract five times since."
  url: https://smlouvy.gov.cz/smlouva/31013084
  note: 'Registr smluv 31013084, 15 November 2024, "Vytvoření informačního systému e-Turista",
    Ministerstvo pro místní rozvoj to InQool, a.s. (IČO 29222389), 28,424,650 CZK excl. VAT,
    34,393,827 CZK incl. VAT; amendments 1–5 to 6 May 2026 (Hlídač state search "eTurista", 11
    contracts, including a 64M CZK cloud-services framework of 8 August 2025, registr smluv
    34407937). MONEY 1: public money is moving on this problem, but it builds the state''s own
    register and pays no host or vendor for this product.'
  date: '2024-11-15'
  dims: [money]
- type: gap-check
  name: "Czech guest-reporting software — taken by an established hotel system"
  gist: "the taken Czech field"
  why: "The most used Czech hotel software already sends foreign guests to the police automatically, a Spanish check-in service sells the same in Czech, and at least seven small Czech apps sell it to hosts."
  url: https://www.previo.cz/
  note: 'Czech sweep 2026-09-18. DIRECT, ESTABLISHED: Previo (PREVIO s.r.o., IČO 25975234):
    "Přidejte se k 5 573 spokojeným klientům. Previo je nejpoužívanější hotelový systém v Česku";
    "Previo je vyvíjeno od roku 2004"; its help page on the foreign-guest book: lists "které přímo
    z Previa odešlete ručně nebo automaticky cizinecké policii (CP)"; price list PMS PRO 9,490
    CZK / LITE 6,490 CZK setup plus 300 / 250 CZK a month (previo.cz/en/pricelist). Chekin''s
    Czech page (see S10). DIRECT, EARLY (no customer count found): Best Guest (Hotel Analytics
    s.r.o., IČO 06723756, 2018), 10 CZK per completed check-in, "hlášení cizinecké policii pro
    Airbnb pronájmy"; Trevlix (IČO 14091887, 2021), automatic Ubyport reporting, from 90 CZK a
    month; Checkinn.cz (anniversary s.r.o., IČO 17613485, October 2022), about 590 CZK a month;
    Superhostem (IČO 29503825, ARES date read by the research pass as April 2026), "Napojeno na
    UbyPort"; Ubytovačka / Evidence hostů (AI Universe s.r.o., IČO 23427078, June 2025), "za 69 Kč
    měsíčně"; ubytovaci-kniha.cz, licence 1,200 CZK then 600 CZK a year; Hostivio (no ARES match),
    Ubyport v2 reporting; Vezpa, automatic sending "ve fázi dokončení". HOTELTIME''s site did not
    load: named, unverified, not ledgered. TOWN SIDE: no Czech vendor and no contract for finding
    unregistered hosts or collecting the fee — contract-register queries Airbnb (199 hits, public
    bodies booking lodging), krátkodobé pronájmy (873, premises rentals) and "Airbnb poplatek z
    pobytu" (0 CZK) found none; the RIA itself names the US firms Host Compliance/Granicus and
    Airbnb Watch. Not claimed as open: the state register is being built to do much of that job
    (S8). METHOD AND CONTROLS: queries 1–6 ran through the web-search tool until the session''s
    budget ran out; the rest through the contract register and Seznam. Standing controls on Seznam
    MISSED (Wultra and Softlink, same shapes as p-0038). IN-MARKET CONTROL PASSED: the Seznam
    query "online check-in ubytování hlášení cizinců Ubyport aplikace" surfaced Best Guest, a
    vendor already known from the web-search pass. The gap score rests on Previo and Chekin, which
    were found, not on any absence.'
  date: '2026-09-18'
  queries:
    - "AHR ČR eTurista duplicitní hlášení ubytovatelé Ubyport evidenční kniha"
    - "ubytovací kniha online hlášení cizinců Ubyport aplikace pro malé ubytovatele poplatek z pobytu"
    - "online check-in pro apartmány Airbnb automatické hlášení cizinecké policii Ubyport česká aplikace"
    - "hotelový systém napojení Ubyport ČSÚ statistika poplatek z pobytu export evidenční kniha"
    - "Previo ceník hotelový systém Ubyport napojení cena měsíčně"
    - "obec monitoring krátkodobých pronájmů dohledání nabídek Airbnb kontrola poplatku z pobytu software"
    - "registr smluv: eTurista"
    - "registr smluv: Airbnb"
    - "registr smluv: krátkodobé pronájmy"
    - "registr smluv: Airbnb poplatek z pobytu"
    - "online check-in ubytování hlášení cizinců Ubyport aplikace"
    - "české řešení pro zabezpečení mobilního bankovnictví silná autentizace podpisy v mobilu dodavatel"
    - "dálkové odečty vodoměrů software pro vodárny česká firma"
  checked: [google-cz, cz-contract-parties, ares]
  expires: '2026-12-17'
- type: arbitrage
  name: "Chekin — automated guest registration, Seville"
  gist: "the Spanish check-in service"
  why: "A Seville company founded in 2017 automates guest registration with the authorities and tourist-fee calculation for more than 200,000 properties, and already sells Czech police filing on a Czech page."
  url: https://chekin.com/cs/
  note: 'chekin.com/en, read 2026-09-18: "+200,000 properties worldwide", "+25M check-ins
    completed", "+45 countries served"; filing for Spain, Italy, Portugal and the Czech Republic
    named. chekin.com/cs: "Odesílání údajů o hostech úřadům (Ubyport & e-Turista) a elektronická
    ubytovací kniha", "Turistické poplatky – výpočet a platba online", "Důvěřuje nám více než 200
    000 ubytovacích zařízení po celém světě". Legal entity from the privacy policy: CHEKIN
    SOLUCIONES DIGITALES, S.L, NIF B21579990, Seville; constituted 23 May 2017 (empresia.es).
    Funding not verified. Passes the established test on its public count and nine years; proof 2
    (one established foreign player, Spain not being a CEE-adjacent market). It sells in Czechia,
    so it is also in locals[].'
  date: '2026-09-18'
- type: price
  url: https://bestguest.cz/cenik/
  name: "Best Guest — price per check-in"
  gist: "10 CZK a check-in"
  why: "A Czech online check-in that also reports foreign guests to the police charges 10 CZK for each completed check-in, with no monthly fee."
  note: 'bestguest.cz/cenik, read 2026-09-18: "Platíte 10 Kč za každý dokončený check-in hosta.
    Žádné měsíční paušály". dims omitted: backs no score.'
  date: '2026-09-18'
  payer: 'Czech hosts and hotels using an online check-in'
  amount_czk: 10
  unit: per-case
  basis: list-price
- type: price
  url: https://www.previo.cz/en/pricelist/
  name: "Previo — hotel software licence"
  gist: "9,490 CZK to set up"
  why: "The most used Czech hotel software charges 9,490 CZK to set up its full version, plus a monthly service fee that starts at 300 CZK and depends on the number of rooms."
  note: 'previo.cz/en/pricelist, read 2026-09-18: hotel software (PMS) "PRO or LITE version 9 490
    Kč 6 490 Kč + 300 Kč + 250 Kč" (setup fee, then service fee per month; the calculator depends
    on room count). The PRO setup fee is recorded. dims omitted: backs no score.'
  date: '2026-09-18'
  payer: 'A Czech hotel or guesthouse'
  amount_czk: 9490
  unit: one-off
  basis: list-price
created: '2026-09-18'
updated: '2026-09-18'
---

Czech hotels, guesthouses and private hosts send the same guest details to several authorities, each in its own way [S1].

- Foreign guests go to the police within 3 working days [S3].
- The town's accommodation fee needs its own guest records [S1].
- The statistics office asks for its own reports [S1].

The state's own impact assessment calls this repeated entry of the same data an unjustified burden [S1].

- In the ministry's survey of 236 hotels, an average of 3.9 staff registered guests, and 80% used hotel software [S1].
- A Prague hotel's director says receptionists already retype guest details into the police system [S5].
- 10,012 hotels and other collective establishments had 562,467 beds in 2025, and the true number is higher [S1].
- Private hosts letting through online platforms appear in no official register [S1].
- Nearly 8 million nights were booked through the big booking platforms in 2024 [S1].

Existing non-solutions: The most used Czech hotel software and several small Czech check-in apps already send foreign guests to the police [S9].

The hotel software is established, with thousands of clients; the apps are young and publish no customer counts; see [Competition](#competition) [S9]. A Spanish check-in service also sells police filing and the planned register on its Czech page [S10]. Prices run from a charge per check-in to a licence with a monthly fee; see [Willing to pay](#willing-to-pay).

- None of these tools removes the separate duties themselves, which only the law can merge [S1].
- No Czech seller or contract was found for helping towns find hosts who do not pay the fee [S9].

Why now: Hosts keep filing several ways until 2028 at the earliest, and the bill would then require each guest within 24 hours [S1,S4].

- Towns lose about 55M CZK a year in unpaid accommodation fees [S6].
- Adapting one hotel system to the register is put at about 20,000 CZK [S1].
- A guesthouse owner fears a new booking system costing tens of thousands [S5].

The dates and rules behind this:

- On 20 May 2026 the EU rule on short-term rental data began to apply, and Czechia runs no registration scheme yet [S1,S2].
- In September 2026 the ministry sent the bill out for comments [S7]. The previous government's version was never passed by parliament [S7].
- On 1 January 2028 the bill would take effect [S4].
- Under the bill, a private host who breaks its rules could be fined up to 100,000 CZK, and a platform up to 10M CZK [S4].
- Between 40% and 70% of stays booked through online platforms went unreported, the ministry says [S6].

Who pays: Hosts already pay for check-in software, and the state is paying to build its own register [S8,S9].

- Hosts pay per check-in or a monthly fee; see [Willing to pay](#willing-to-pay).
- The ministry signed about 34M CZK to have the register built [S8].
- Connecting the whole industry is put at about 190M CZK, one-off [S1].

Of that 190M CZK, about 160M CZK is for adapting hotel software and 30M CZK for training staff [S1]. Hotels in the ministry's survey named more than 35 different hotel systems, each needing its own connection [S1]. Running the register is put at about 960,000 CZK a month, with 30M CZK from the EU recovery plan [S1]. Regional towns would get about 45M to 48M CZK more in the first year for the new registration work; the impact assessment gives both figures [S1].

Solved elsewhere: A Spanish check-in service files guests to the authorities and works out tourist fees, for more than 200,000 properties [S10].

It was founded in Seville in 2017 and names filing for Spain, Italy, Portugal and the Czech Republic [S10].

## First moves

1. Build a phone check-in for private apartment hosts that reads a guest's passport and files the police report. Private hosts letting through platforms appear in no register today, as [The opportunity](#opportunity) shows, and the police report has the shortest deadline; see [Why now](#why-now). Start with that one report, then add the town's fee records.
2. Call guesthouse owners who still retype guests by hand, and ask what they would pay to stop. Hotel software already covers most hotels, as [Competition](#competition) shows, so the hosts left are small ones without it. The prices they will compare you with are under [Willing to pay](#willing-to-pay).
3. Offer the move to the state register as part of the price, once the state publishes how software connects to it. Every hotel system will need its own connection, as [Willing to pay](#willing-to-pay) shows, so a host who already uses your check-in is spared that upgrade. The bill's date is under [Why now](#why-now).

## Revisions

2026-09-18 · record created — Minted from the eTurista bill and its impact assessment [S1,S4] and the EU short-term rental regulation [S2]. Demand 2 on the state's own statement of the duplicate burden [S1], hoteliers' statements [S5] and the ministry's figures on unpaid fees [S6]. Money 1 on the ministry's contract to build the register, which is public money on this problem but pays for the state's own system [S8]. Urgency 2: the bill's 1 January 2028 date is under 18 months away but it is still a draft, so the deadline scores 1, plus sources fresher than 90 days [S4,S7]. Proof 2 on one established Spanish comparable [S10]. Gap 0 and status watching: the most used Czech hotel software already files foreign guests to the police automatically, and the Spanish comparable sells the same in Czech [S9,S10]. Correction to the signal: the ministry's plan date of 1 January 2027 could not be confirmed from a primary source; the bill itself says 1 January 2028 [S4]. No draft-law badge: hosts file several ways today whatever happens to the bill. The web search budget ran out during this pass, so the standing positive controls were run on Seznam and missed; an in-market control passed [S9].
