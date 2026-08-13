# The Missing Repository of Problems

## Deep research: signals, data sources, existing players, and a blueprint for a repository of local problems & opportunities

*Research date: August 12, 2026*

---

## 1. Your thesis, stress-tested

Your intuition — "there are lots of solvers, but not enough stated problems" — holds up remarkably well against the landscape. After mapping ~80 platforms, datasets, and players, the picture is:

**The pieces all exist. The assembly doesn't.**

- Institutions state problems at scale (challenges, tenders, grant calls, strategy documents) — but scattered across hundreds of silos, in bureaucratic language, aimed at contractors and researchers, not problem-solvers.
- Citizens state problems at scale (311 data, FixMyStreet, participatory budgets, petitions, reviews, Reddit) — but framed as complaints, locked in per-city silos, never reframed as opportunities.
- Algorithms infer problems at scale (the 2023–26 wave of AI pain-point miners like BigIdeasDB, Ideabrowser) — but almost exclusively for English-speaking, online, SaaS-shaped problems. **None of them are geographic. None are local.**

The empty quadrant, stated precisely:

| | **Institution-stated** | **Citizen-stated / inferred** |
|---|---|---|
| **Global** | XPRIZE, InnoCentive/Wazoku, MIT Solve — *crowded* | Ideabrowser, BigIdeasDB, GummySearch heirs — *newly crowded* |
| **Local** | 311, SeeClickFix, city challenges — *mature but closed to solvers* | **← EMPTY. This is your idea.** |

An open, structured, cross-domain, solver-agnostic repository of **local** problems and opportunities does not exist anywhere. The closest precedents are government-gated (CivTech Scotland, Singapore's Open Innovation Platform, Smart India Hackathon) or report-shaped rather than database-shaped (UNDP Accelerator Labs).

---

## 2. The signal taxonomy

You named four signal families in your brain dump. All four check out, and research surfaced three more. Here is the full taxonomy with the concrete data behind each.

### Signal family A — Businesses succeeding abroad (geographic arbitrage)

*"It works there, it doesn't exist here yet."*

This is the most validated signal family — an entire industry was built on it (Rocket Internet: Zalando, Lazada, Jumia, HelloFresh) and institutional money still prices it: **Fluent Ventures raised a $40M fund in 2025 explicitly on "geographic alpha,"** and FJ Labs (~1,100 portfolio companies) runs marketplace pattern-matching across geographies as its core strategy and publishes its theses for free.

Key mechanics established by academic diffusion research (Tellis et al., *Marketing Science*):

- Average time-to-takeoff for a new product category is **~6 years even between European countries** — arbitrage windows are real and measurably wide.
- The "lead-lag effect": follower markets adopt **faster** than the origin did (the market learns from abroad) — clones scale quicker than originals.
- 2026 caveat: windows have collapsed to ~zero for thin software (AI makes copying instant; Stripe/OpenAI launch globally at once). Arbitrage survives in **ops-heavy, regulated, infrastructure-dependent models**: fintech, logistics, healthcare, B2B marketplaces, anything needing licenses or local supply chains.
- Transfer success is conditional, not automatic: quick-commerce died in EU/US clones (Gorillas, Getir's retreat) but thrived in India (Zepto, Blinkit) because density and labor costs differed. Iterative VC publishes a 6-criteria transferability checklist (same problem? same infra assumptions? revenue model fit? defensibility? cultural gap? regulation?).

**How to compute it:** signal = [proven-model set in origin markets] MINUS [target-geo company set], gated by transferability filters.

| Data source | What it gives you | Access |
|---|---|---|
| yc-oss API (GitHub) | All 5,000+ YC companies, batch/industry/country tagged | **Free JSON** |
| Dealroom country platforms | Free searchable startup DBs for dozens of countries incl. gov-sponsored national ones | **Free** |
| Tracxn | 2,000+ theme "feeds" × business model × geography — literally a clone-detection matrix | ~$550/mo (free quarterly geo×sector PDF reports) |
| CB Insights market maps | Enumerations of all players per model category (mostly US = origin set) | Free on blog |
| Google Trends interest-by-region | S-curve phase gap between countries per model keyword | Free |
| Sensor Tower top charts | App category divergence between country stores | Free tier |
| LinkedIn job postings | "First country manager" posting = your window is closing (6–12 mo lead) | Free alerts |
| Crunchbase API | Founding/funding timestamps to measure diffusion lag | $49–99/mo |

### Signal family B — Investors investing (smart money as problem-validator)

Every funding round is a paid-for statement that "this problem is worth solving." Regional VC theses and market maps (FJ Labs, a16z Big Ideas, Sequoia, regional maps from Sifted/TechCabal/Contxto/Tech in Asia) are free, forward-looking problem lists. YC's Requests for Startups — refreshed every batch since 2024 — is the canonical "problems we want solved" document. Track Series B+ rounds in origin markets as a clock-start on the replication window.

### Signal family C — Users complaining (bottom-up demand)

The largest raw corpus of *stated local problems on Earth* is civic complaint data:

- **NYC 311**: 30M+ geolocated, categorized complaints, free Socrata API. Chicago, SF, Boston, Toronto similar. The **Open311 standard** means one connector can ingest dozens of cities.
- **FixMyStreet** (UK + deployments in Sweden, Switzerland, Malaysia...), **SeeClickFix** (hundreds of US municipalities, free REST + Open311 API).
- **Czech Republic specifically**: the civic-reporting landscape is fragmented across ZmapujTo (~37k reports), Munipolis/Mobilní rozhlas (thousands of municipalities), Změňte.to (Prague, via Operátor ICT), and T-MAPY per-city instances — **all public-but-not-open, no APIs**. Slovakia's Odkaz pre starostu has been successfully scraped and analyzed by independents. This CZ/CEE fragmentation is itself a gap your repository could fill first.
- **Participatory budgeting proposals** are expressed unmet needs with citizen votes attached: Decidim (400+ cities, GraphQL API), Consul, and 100+ Czech PB sites (participativni-rozpocet.cz, Decision 21) — no unified dataset exists; scraping them would itself be a novel repository.
- **Consumer complaint registries**: US CFPB database (millions of complaints, ZIP-code granular, free public API — the best model of what an open complaint registry looks like), ČOI open data (inspections/sanctions CSV), EU ECC-Net (aggregate only).
- **Petitions**: UK Parliament petitions expose signature counts **by constituency** as free JSON — exemplary geo-granular demand data. EU Citizens' Initiatives publish per-member-state stats. Czech ePetice on Portál občana is scrapeable; e-petice.cz and petice.com carry municipal-level grievances.
- **Review mining**: Google Maps reviews are arguably the best hyperlocal complaint corpus (every local business, geocoded) — scraping-only. App-store reviews per country storefront; G2/Capterra for SaaS gaps.
- **Platform risk warning**: GummySearch — the Reddit pain-mining category leader — shut down in 2025 when Reddit closed its API. Reddit/X/Meta/Nextdoor all went closed or expensive 2023–25. **Government and civic sources are the durable, legally clean backbone; social sources are garnish.**

### Signal family D — Governments allocating money & publishing visions (top-down)

This family is far richer than most people realize, and almost all of it is free and machine-readable:

- **Procurement = a stream of stated problems with budgets.** EU TED publishes every above-threshold tender — the Search API needs **no authentication**. Prior Information Notices are early "we will need X" signals. CZ: NEN has a documented public API, Hlídač státu wraps contracts/tenders/subsidies in a free API, and Registr smluv exposes every public contract over 50k CZK in full text — revealing what institutions already pay to solve.
- **Grant calls = problems with money attached.** Horizon Europe work programme topics are literally structured problem statements with expected outcomes and budgets (free JSON API). EU Missions carry quantified 2030 targets. TA ČR + STARFOS show everything the Czech state pays to research. Národní plán obnovy milestones are an explicit national reform list.
- **Diagnostic documents = each country's problems, professionally diagnosed, annually, for free.** This is the most underexploited source found in the entire research: **European Semester country-specific recommendations** (an annual EU-issued list of each member state's problems), **IMF Article IV consultations** (annual per-country diagnosis — the 2026 Czech one is out), **OECD Economic Surveys** (2025 Czechia edition: innovation, business dynamism, net-zero). All PDFs — meaning an LLM extraction layer over them is the differentiator nobody has built.
- **Regulatory pipeline = markets created on a schedule.** Every horizontal EU regulation (CSRD, AI Act, DORA, NIS2, CBAM) spawns a compliance-tooling market, and the implementing-acts timeline is a published opportunity calendar. EU Have Your Say portal + Commission Work Programme + EUR-Lex SPARQL let you watch legislation before it lands. Czech VeKLEP publishes draft laws with RIA impact assessments that literally state the problem being solved.
- **Development banks** publish structured "problem + money" records: World Bank Projects API (every project since 1947, incl. pipeline), EBRD pre-approval project summaries, IATI as one normalized feed across all donors.

### Three signal families you didn't mention (found in research)

- **E. Expiring/failing solutions**: contract expiry dates in procurement data = re-procurement windows (this is UK startup Stotles' entire business — "pre-tender signals"). Government vendor lock-in complaints, aging infrastructure registers.
- **F. Research gap maps**: Convergent Research's Gap Map (launched April 2025) is the best modern structured problem repository in any domain — R&D gaps linked to capabilities and resources across 13 fields. A design template worth studying closely. Also SBIR.gov topics (thousands of US agency problems with money attached).
- **G. Solution-mapping in reverse**: UNDP Accelerator Labs (90+ labs, 115 countries) map grassroots problems *and* local improvised solutions — improvisation is evidence of an unmet need strong enough that people hack around it.

---

## 3. Who is already doing pieces of this

### The problem-marketplace incumbents (global, institutional)
| Player | Model | Status 2026 |
|---|---|---|
| Wazoku/InnoCentive | Corporate R&D challenges, ~700k solvers, >$60M awarded since 2001 | Active |
| HeroX | Self-service prize challenges (NASA etc.) | Active |
| XPRIZE | $5M–$120M moonshots | Active |
| Halo (halo.science) | Modern R&D problem marketplace — companies post problems, scientists respond | Active, the freshest take |
| Challenge.gov | US federal prize hub | **Sunset March 2026** — the US federal problem list just lost its home |

### Government problem banks (the models to copy)
- **Smart India Hackathon** — ministries publish hundreds of formal, theme-tagged problem statements annually into a browsable database; hundreds of thousands of students compete. Proof that government-as-problem-supplier works at national scale.
- **Singapore GovTech Open Innovation Platform** — explicitly a national problem-statement marketplace with prize/dev funding.
- **CivTech Scotland** — government states problems, startups get paid to solve them, procurement-backed. 10+ rounds.
- **GovTech Poland** — the best CEE model: agencies post problems, SMEs compete.
- Czech equivalent: doesn't exist. CzechInvest Technologická inkubace (~250 startups) is the closest vehicle but is not a problem marketplace.

### The AI idea-mining wave (2023–2026)
Ideabrowser (Greg Isenberg, ~$1M ARR trajectory, $299/yr), BigIdeasDB (scrapes 10 sources — Reddit, G2, app stores, Upwork — into a problems database, even ships an MCP server), PainMap, PainOnSocial, NeedGap, ProblemHunt. **All global/English/SaaS-shaped. None local, none geographic, none where a problem-owner states the problem.** This wave proves willingness-to-pay for problem discovery ($45–$349 price points) while leaving your quadrant untouched.

### Aggregators of "government money + problems"
Stotles (UK/EU pre-tender intelligence), OpenOpps/Spend Network (700+ procurement sources normalized), TenderAlpha (procurement as investment signal, sold via FactSet), OpenGrants (US). **All silo by instrument (tenders OR grants) and audience (bid teams, not founders). Nobody merges strategy documents + grants + tenders + regulation into one "problems with money attached" feed.**

---

## 4. Why the gap persists (the honest part)

Three structural reasons no one has built this — each one a design requirement for you:

1. **The incentive problem.** Open problem boards where real people state problems (NeedGap, ProblemHunt) stay tiny: problem-owners have no reason to invest effort stating problems well for strangers. Every scaled platform solves this either with money (challenges, tenders) or by *inferring* problems from exhaust data instead of asking. → Your repository should be **inference-first, contribution-second**: seed it from the data sources above; let humans verify/enrich rather than cold-start.
2. **The freshness/state problem.** Nobody maintains whether a problem is still open, who's working on it, what's been tried. Repositories rot. → Problems need lifecycle state, and automated re-checking against the source signals.
3. **The framing problem.** A 311 complaint, a tender, an IMF paragraph and a Reddit rant about the same underlying problem look nothing alike. → The core IP is a **normalization schema**: every record = problem statement + location + evidence links + money attached (if any) + who owns it + status + comparable solutions elsewhere. This is exactly what LLMs became good enough to do cheaply in 2024–26, which is why this idea is timely *now* and wasn't buildable in 2019.

There's also a bias warning from the academic literature: 311-type reporting has strong socio-spatial bias — *who complains ≠ where problems are*. A serious repository should model this rather than ignore it.

---

## 5. Blueprint: how you could actually build this

### The one-sentence version
**Ingest free institutional feeds → LLM-extract normalized problem statements → cross-reference against "solved elsewhere" data → publish as an open, browsable, geographic problem map.**

### Phase 0 — Prove the extraction (a weekend)
Take three free, no-auth sources for Czechia: the latest European Semester country report + IMF Article IV (problems diagnosed), TED API filtered to CZ (problems with budgets), and one scraped city (Prague's Změňte.to or a Decidim instance). Run LLM extraction into a common schema. If ~200 clean, deduplicated, geolocated problem records come out the other side, the thesis works.

### Phase 1 — The Czech/CEE wedge (months 1–3)
Czechia is a genuinely good starting market, not just a home-field choice: civic data is public-but-not-open (so aggregation adds real value, unlike the US where portals already exist), the market is small enough to cover completely, and no local player exists. Ingest: Hlídač státu API, NEN/VVZ, dotaceeu + NPO + TA ČR calls, Semester/IMF/OECD diagnostics, ~100 participatory budgeting sites, ZmapujTo/municipal defect maps, petitions. Output: "Problémy Česka" — every stated problem in the country, one map, one taxonomy, freshness dates, money attached where applicable.

### Phase 2 — The arbitrage layer (months 3–6)
Add the "solved elsewhere" dimension: for each problem cluster, diff against yc-oss + Dealroom country databases + Tracxn free reports → "this problem has 4 funded solutions in Germany and Poland, zero in CZ." This is the layer nobody on Earth currently productizes, and it converts a civic database into an opportunity engine.

### Phase 3 — Marketplace mechanics (later)
Only after the repository has gravity: let municipalities/companies post verified problems (the SIH/CivTech model), let solvers claim problems publicly ("who's working on this"), attach bounties/procurement. Business model options proven by adjacent players: freemium subscriptions (Ideabrowser: $299/yr), government SaaS (FixMyStreet Pro, SeeClickFix→CivicPlus), data feeds (TenderAlpha→FactSet), or matchmaking fees (Halo).

### The moats
- The normalization schema + extraction pipeline (compounding data asset)
- Cross-source deduplication (same problem seen in a tender + a petition + an IMF paragraph = high-confidence problem)
- The arbitrage diff layer (unique)
- CZ/CEE language coverage (English-only players structurally can't follow)

### Signal-quality ranking (where to spend effort first)
1. **Procurement + grant calls** — problems with money attached, free APIs, legally clean, updated daily
2. **Diagnostic documents** (Semester, IMF, OECD, RIAs) — highest insight density, zero competition for extraction
3. **Startup-diff / arbitrage** — highest opportunity value, moderate effort
4. **Civic complaints + PB proposals** — most authentically local, needs scraping + bias correction
5. **Petitions, reviews, social** — garnish; social sources carry platform risk (the GummySearch lesson)

---

## 6. Key sources

**Landscape**: [Wazoku/InnoCentive](https://www.wazoku.com/innocentive-marketplace/) · [HeroX](https://www.herox.com/) · [XPRIZE](https://www.xprize.org/) · [Halo](https://www.halo.science/) · [MIT Solve](https://solve.mit.edu/) · [YC RFS](https://www.ycombinator.com/rfs) · [Ideabrowser](https://www.ideabrowser.com/) · [BigIdeasDB](https://bigideasdb.com/) · [NeedGap](https://needgap.com/) · [Smart India Hackathon](https://sih.gov.in/) · [Singapore OIP](https://www.openinnovationnetwork.gov.sg/) · [CivTech Scotland](https://www.civtech.scot/) · [GovTech Poland](https://konkursy.govtech.pl/) · [Gap Map (Convergent Research)](https://www.gap-map.org/) · [UNDP Accelerator Labs](https://www.undp.org/acceleratorlabs) · [80,000 Hours problem profiles](https://80000hours.org/problem-profiles/)

**Arbitrage**: [Fluent Ventures (TechCrunch)](https://techcrunch.com/2025/04/23/fluent-ventures-backs-replicated-startup-models-in-emerging-markets/) · [FJ Labs investment strategy](https://fabricegrinda.com/fj-labs-investment-strategy/) · [Iterative: should you copy startup ideas](https://www.iterative.vc/post/should-you-copy-startup-ideas-from-other-markets) · [Tellis et al., International Takeoff of New Products](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=904142) · [yc-oss API](https://github.com/yc-oss/api) · [Dealroom country platforms](https://dealroom.co/countries/) · [Tracxn](https://tracxn.com/) · [Rocket Internet retrospective (TechCrunch)](https://techcrunch.com/2020/09/01/as-it-delists-rocket-internets-ill-fated-experiment-with-public-markets-is-over/)

**Bottom-up**: [NYC 311 dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9) · [Open311](https://www.open311.org/) · [SeeClickFix API](https://www.civicplus.help/seeclickfix/docs/available-seeclickfix-apis) · [FixMyStreet Platform](https://fixmystreet.org/) · [Decidim](https://decidim.org/) · [CFPB complaint API](https://cfpb.github.io/api/ccdb/) · [ZmapujTo](http://www.zmapujto.cz/) · [Munipolis](https://www.munipolis.cz/) · [Změňte.to](https://zmente.to/) · [Odkaz pre starostu](https://novy.odkazprestarostu.sk/) · [UK petitions (JSON by constituency)](https://petition.parliament.uk/petitions) · [participativni-rozpocet.cz](https://www.participativni-rozpocet.cz/) · [ČOI open data](https://www.coi.cz/pro-spotrebitele/otevrena-data/kontroly/)

**Top-down**: [TED API (no auth)](https://docs.ted.europa.eu/api/latest/index.html) · [EU Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/) · [Hlídač státu API](https://www.hlidacstatu.cz/api/v1/doc) · [NEN public API](https://podpora.nipez.cz/en/verejne-api-systemu-nen/latest) · [Opentender.eu](https://opentender.eu/cz) · [European Semester — Czechia](https://commission.europa.eu/business-economy-euro/european-semester/european-semester-your-country/european-semester-documents-czechia_en) · [IMF Article IV Czechia 2026](https://www.imf.org/en/publications/cr/issues/2026/03/30/czech-republic-2026-article-iv-consultation-press-release-staff-report-staff-supplement-575034) · [OECD Economic Survey Czechia 2025](https://www.oecd.org/en/publications/oecd-economic-surveys-czechia-2025_7a70af5c-en.html) · [STARFOS](https://starfos.tacr.cz/en) · [Kohesio](https://kohesio.ec.europa.eu/) · [World Bank Projects API](https://datacatalog.worldbank.org/search/dataset/0037800/world-bank-projects-operations) · [Have Your Say](https://have-your-say.ec.europa.eu/index_en) · [Stotles](https://www.stotles.com/) · [Spend Network/OpenOpps](https://www.spendnetwork.com/) · [SAM.gov API](https://open.gsa.gov/api/get-opportunities-public-api/)
