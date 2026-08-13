# Díra na trhu — System & Product Design Doc

## The repository of local problems & opportunities, v1 (CZ/CEE)

*Design date: August 12, 2026 · Companion to `problem-repository-research.md`*

---

## 1. What we're building, in one paragraph

A weekly opportunity-intelligence product for Czechia/CEE where **every problem comes with receipts**: a budget line from a tender or grant, a source document, proof the solution already works in another country, and — new in this design — a **VC validation edge** ("this sits inside Credo's stated thesis"). Under the hood: one Postgres database fed by free public APIs, an LLM extraction pipeline, and an embedding-based dedup/matching layer. On the surface: an email newsletter → landing page. Total infra cost: **~$25–30/month**. Buildable by one person in 6 weeks.

The sentence that is the product:

> *"Brno's parking-enforcement gap — an 18.4M CZK tender — sits inside Credo's stated urban-tech thesis; 6 YC companies solve this in the US, none in CEE."*

---

## 2. The VC signal layer (your addition — and why it matters)

VC signals are the highest-quality validator in the stack because investment is a **costly signal** — someone staked real money on "this problem is worth solving." Three ingestion streams:

1. **Fund theses & vision docs** (monthly, ~$1/mo LLM cost). A hand-maintained YAML of ~30 URLs: FJ Labs' published theses, a16z Big Ideas, YC Requests for Startups (refreshed per batch), and the "what we invest in" pages + blogs of CZ/CEE funds (Credo, Kaya, Presto, J&T, Tensor, Purple, Zero One). Scrape → diff against last month → LLM-extract discrete funding appetites: *{fund, "wants to fund X for Y in geo Z at stage S", verbatim quote, domain, valid_until}*. Theses expire (default +12 months; YC RFS = one batch).
2. **Portfolio diffing** (quarterly). Scrape the 7 CZ/CEE fund portfolios + load the free yc-oss JSON of all YC companies. Tag every company with a domain slug, then pure SQL: domains with high global density and **zero CEE coverage** = whitespace candidates. Important nuance: a gap is ambiguous (could be whitespace, could be a graveyard) — so it prompts editor judgment, never auto-publishes.
3. **Round events on a budget.** Skip Crunchbase ($49–99/mo) at MVP. Regional press catches every CEE round that matters: RSS of CzechCrunch, Vestbee, EU-Startups → LLM extracts {company, round, amount, sector, investors}. Add Crunchbase only when a paying customer demands completeness.

**Join mechanic:** weekly, each problem record is embedded-matched against active VC signals (cosine top-3 → cheap LLM judge scores whether the thesis genuinely validates *this* problem → edges >0.6 stored with a one-line rationale). These edges render in the newsletter as the validation line.

---

## 3. Product design

### 3.1 Users — the barbell

Ranked by willingness-to-pay × reachability × data fit:

| Segment | Role | Score |
|---|---|---|
| Consultants, agencies, dev shops, grant advisors | **Primary payer** | 80 |
| Aspiring founders / indie hackers CZ/CEE | **Audience core** (volume, virality) | 50 |
| VC/angels (~30 people) | Comped strategic tier — distribution multiplier | 36 |
| SMEs expanding | Payer, reached via consultants & content | 32 |
| Corporate innovation | Year-2 enterprise upsell | 30 |
| Municipalities | Content *source*, not customer | 16 |

Founders are the audience; consultants are the money (the Stotles freemium logic). A dev shop that wins one 2M CZK contract from a tip has paid for 50 years of subscription.

**The "holy shit" moment for issue #1:** *"Kraj Vysočina just budgeted 18M CZK for exactly the thing I could build, here's the tender document, here's the German startup that raised €12M doing it, and nobody in Czechia does it."* Specificity + money + absence of competition, verifiable in two clicks. What these users do today instead: doom-scroll US-centric Ideabrowser/Twitter, read CzechCrunch (news, not opportunities). Nobody reads the Věstník or OECD surveys — the data is public and *unread*. That's the arbitrage.

### 3.2 Format: newsletter → landing page is not just enough, it's optimal

Curation businesses die from building product before proving editorial pull (Trends.vc ran to ~$500k/yr as essentially email + Notion). The database is a **pricing tier**, not a launch requirement.

**Cadence:** weekly, Tuesday 07:00 CET. **Discipline:** one deep item + 4–5 shallow signals, 6–8 min read. One item with full receipts beats ten without — the #1 failure mode of this category is half-researched slop.

**Issue structure:**

1. Cold open (3 sentences): what moved in CZ money-land this week
2. 🕳️ **Díra týdne** (Gap of the Week) — the flagship ~700-word card
3. 📄 **Tendrový radar** — 3 tenders/grant calls, 2 lines each, incl. one pre-tender signal
4. 🔁 **Ozvěna odjinud** — geographic arbitrage: "raised €Xm in Germany; Czech equivalent: none found"
5. 🧾 **Diagnóza** — one IMF/OECD/Semester finding translated into an opportunity sentence
6. 👀 **Kdo na tom dělá** — follow-ups on claimed problems (the retention loop)
7. One-line CTA

**The card, mocked with realistic content** (this is the quality bar — every deep card hits it or doesn't ship):

> ### 🕳️ DÍRA TÝDNE #04: Komunitní energetika nemá správce
> **One-liner:** Czech law now allows electricity sharing between buildings — but ~6,300 municipalities and thousands of SVJs who could profit have no one to run it for them. Austria solved this with a service layer; Czechia hasn't.
>
> **🧾 RECEIPTS**
> - **Regulatory trigger:** Lex OZE II in force; energy sharing via EDC live since Aug 2024. Registered CZ energy communities: low double digits. Austria, same framework since 2021: **1,500+**. [→ EDC registry] [→ zákon 469/2023 Sb.]
> - **Money attached:** Modernizační fond RES+ call for municipalities — **billions of CZK allocated**, hundreds of approved projects in the public SFŽP registry *right now* — each a named, funded lead needing sharing administration within 18 months.
> - **Proven elsewhere:** Exnaton (CH) sells energy-community billing SaaS across DACH; Cloover (DE) raised **$114M** in 2024; Austrian "EEG service" firms charge €2–6/member/month recurring.
> - **Demand, bottom-up:** Brno/Prague participatory budgets repeatedly feature solar-on-schools proposals; SVJ forums full of "jak na sdílení?" threads.
>
> **WHO PAYS:** municipality (grant-funded, low price sensitivity) or SVJ; realistic 2–5k CZK/month per community, or rev-share on saved energy.
> **COMPETITION SCAN:** one-off consultants exist; **no dedicated CZ community-administrator SaaS/service found**. (Tell us if we missed someone — we'll print the correction.)
> **EFFORT/FIT:** ⚙️⚙️⚙️ 3/5 — service-first, software later. Wrong for a weekend project, right for a 2-person team with one energy insider. Defensible via boredom.
> **48-HOUR NEXT STEP:** pull 20 municipalities with approved RES+ grants from the SFŽP registry, email the starosta: "You'll need sharing administration by [date]. We do it for X CZK/month."
> **CONFIDENCE: 🟢 High.** Main risk: ČEZ/E.ON bundle it free — mitigant: municipalities distrust incumbents; Austrian independents coexist with utilities.
>
> *[Klaimni tento problém →] [Sdílet kartu →]*

**Subject line formulas (rotate):** money-forward ("18 mil. Kč na problém, který nikdo neřeší"), arbitrage-forward ("V Rakousku 1 500 firem. V Česku nula."), diagnosis-forward ("OECD právě popsala díru na českém trhu, str. 47").

**Landing page:** positioning + one permanently-unlocked best-ever card + subscribe form + archive index where locked cards show *title + receipts count + confidence badge* — the tease is the titles. Email is the product; the page is the funnel.

**Database trigger:** first as a filterable Airtable behind the paywall (2 days of work, ships with paid launch). A real app only when ALL of: 100+ cards, 3,000+ subs, ≥30% of paid-user requests are search/filter/alert-shaped. The true app trigger is **alerts demand** — custom sector/region alerts can't live in email and are the B2B price unlock.

### 3.3 The So-What Test — a card ships only if it answers all five

1. **Who pays, how much?** (named payer + CZK figure; "TAM $4B" is banned vocabulary)
2. **Why now?** (a dated trigger: law, grant call, tender, round, expiring contract)
3. **What's the proof it works?** (foreign comp with revenue/funding, or completed public contract)
4. **Who else is on it?** (honest competition scan, incl. "nobody found — correct us")
5. **What do you do Monday morning?** (48-hour step involving a real, reachable entity)

Anti-slop covenant, printed publicly: every number links to a primary source; corrections printed prominently (being correctable is the moat); confidence scores with stated main risk; +6-month follow-ups on every card (**a public hit-rate is an unfair advantage no trend-mill can copy**); max 1 deep card/week.

### 3.4 Monetization

| Tier | Price | Contents |
|---|---|---|
| Free | 0 | Weekly issue with card *summary*, full Tendrový radar, 1 arbitrage echo |
| **Pro** | 299 Kč/mo · 2 490 Kč/yr (~$110) | Full cards + receipts + next steps, searchable archive, monthly sector report, claim board |
| **Radar (B2B)** | 29 000 Kč/yr (~$1,250) | Pro ×5 seats + custom sector/region alerts + quarterly briefing + white-label PDF |
| Founding cohort | 1 990 Kč/yr locked, cap 100 | Presale from issue #5 — doubles as the willingness-to-pay test |
| Sponsorship | 8–25k Kč/issue | One clearly-marked slot |

Flip paid on after ~10 free issues AND 1,500+ subs AND 45%+ open rate.

**Honest revenue math:** 1,000 subs → ~250k CZK ARR (signal, not business). 5,000 subs (the realistic Czech-language ceiling) → ~1.2M CZK (~$53k) ARR — a great solo business, not venture. **The month-9 fork, decided out loud on day 1:** (a) English-language CEE expansion (Poland alone 4×'s the market, the engine is identical), or (b) the B2B alerts/data product eats the newsletter (become the Stotles of CEE opportunity intel, 100k+ CZK/yr corporate deals). Watch which pulls harder: Radar demand vs. reader geography.

### 3.5 Growth loops (built into product, not marketing)

Shareable card PNGs (auto-rendered per issue — "V Rakousku 1 500, v Česku 0" is native LinkedIn material); the **Claim Board** (public "problem #04 claimed by @jan.novak" — claiming is a public commitment people share themselves, and it generates the follow-up section); hackathon/university brief pipeline (VŠE xPORT, ČVUT InQbay, JIC, MUNI — they chronically lack good problem briefs; free license with attribution = hundreds of exactly-right subscribers per semester, zero CAC); the "correct us" mechanic (corrected parties share their mention); 30 VCs on free-forever Pro (they forward cards to founders: "someone should build this").

**First 500 subs:** issue #0 before any code → founder's LinkedIn post with the full card pasted inline + 10 pre-arranged reposts (~150–250 signups) → CzechCrunch meta-story pitch ("čte za vás věstník a OECD reporty") → Hlídač státu adjacency (approach Michal Bláha, same civic-data DNA) → newsletter swaps (StartupJobs, Lupa, Kaya's letter) → 20 personal DMs with early access.

### 3.6 Naming directions

**Díra na trhu** (diranatrhu.cz) — "Každý týden jedna díra na trhu. S účtenkami." — the pick: the Czech idiom literally means "gap in the market," instantly legible, meme-able (🕳️). Alternatives: Mezera (cleaner, CEE-expandable), Hlídač příležitostí (needs Bláha's blessing), Druhá vlna (names the arbitrage mechanic), Receipts (the name if the fork goes English/B2B). Category claim: **opportunity intelligence** — never "idea database" (that's the slop shelf we differentiate against).

---

## 4. System design

### 4.1 Core stance

One Postgres database **is** the product; pipeline, newsletter, and site are thin functions over it. The unit of truth is **Evidence, not Problem**: evidence rows are immutable LLM extractions from source documents; problem records are mutable clusters over evidence — dedup stays reversible, LLM errors stay quarantined. Human-in-the-loop is the QC system at MVP scale (automate triage, not judgment). **Under-merge, never over-merge.**

### 4.2 Data model (three layers + overlays)

```
raw_document (what we fetched, immutable, content-hashed)
   └─> evidence (LLM extraction: statement EN+CS, verbatim quote, domain slug,
                 geo country/NUTS3/municipality, money normalized to EUR,
                 confidence, model_version, embedding vector(768))
          └─> problem (curated cluster: title, summary, status lifecycle
                       candidate→reviewed→published→stale|solved|merged,
                       money_attached, distinct_sources, confidence composite,
                       centroid embedding)
overlays:
  solution_ref + problem_solution   (solved-elsewhere edges: YC/Dealroom/Tracxn)
  vc_signal + problem_vc_signal     (validation edges: theses, portfolio gaps, rounds)
  opportunity                       (derived: angle, arbitrage_score, demand_score,
                                     featured_in_issue)
```

Key decisions: geography as **codes not names** (ISO2 → NUTS3 → RÚIAN municipality; LLM outputs names, a static lookup resolves them; NUTS generalizes to all of CEE for free). Evidence auto-attaches only to problems at the **same geo_level and domain** — cross-level links ("IMF national diagnosis corroborates a Brno instance") are an editor action, which prevents everything collapsing into "healthcare is bad, nationally." Confidence is composite and recomputed, never hand-edited: `max(extraction_conf) × avg(source_trust) × log(1+distinct_sources)` — corroboration breadth deliberately dominates. Freshness: published → stale after 12 months without new evidence.

### 4.3 Pipeline (boringly simple, on purpose)

No queues, no Airflow, no microservices. One repo, one VPS, plain cron; each stage an idempotent Python script; status columns are the state machine:

```
cron → ingest_<source>.py → raw_document
cron → extract.py     (Gemini Flash batch, strict JSON schema, ~7 prompts by source type)
cron → dedupe.py      (pgvector cosine >0.80 shortlist → Flash-Lite judge SAME/RELATED/DIFFERENT)
cron → enrich.py      (weekly: solved-elsewhere diff, VC matching, opportunity scoring)
manual → Datasette    (editor: promote candidates, fix merges — do NOT build an admin panel)
cron → publish.py     (Astro JSON commit + drafted issue → Buttondown API; founder cuts 10→5)
```

MVP ingests **4 connectors only**: TED-CZ (no-auth API), Hlídač státu (free key), one PDF pipeline (IMF/OECD/Semester, quarterly), yc-oss (free JSON). Everything else is a YAML backlog. A cheap pre-filter (CPV-code whitelist + Flash-Lite yes/no) triages the tender flood before full extraction.

Sample extraction rule-set (tender prompt): statement pattern *"<actor> in <place> lacks/cannot <capability>, evidenced by <what they're buying>"*; verbatim quote ≤300 chars mandatory — **publish.py mechanically refuses any record whose quote isn't a substring of the source text** (hallucination guard); routine commodity buying returns zero signals; confidence <0.4 → don't emit.

### 4.4 Stack & monthly cost

| Layer | Pick | Cost |
|---|---|---|
| Compute + cron | Hetzner CX22 VPS (stable IP > GitHub Actions for scraping) | €4/mo |
| DB | Postgres 16 + pgvector on same box (not Supabase — free tiers pause; not SQLite — concurrent writers) | $0 |
| Extraction | Gemini 2.5 Flash **Batch API** (50% off), structured output | ~$3/mo |
| Triage/judges | Gemini 2.5 Flash-Lite | ~$2/mo |
| Embeddings | gemini-embedding-001 @ 768d | <$1/mo |
| Newsletter | Buttondown (real API, markdown-native) | $9/mo @ 1k subs |
| Site | Astro on Cloudflare Pages + Pagefind search | $0 |
| Monitoring | healthchecks.io + Sentry free tiers (silent cron failure = the #1 solo-founder killer) | $0 |

Token math @ 5k docs/month ingested: triage $0.75 + extraction $2.40 + PDFs $0.10 + dedup $0.65 + enrichment <$1 ≈ **$5–8/mo LLM; total ~$25–30/mo all-in.** Scales linearly — 50k docs/mo still ~$60. The scarce resource is founder review time, not money.

### 4.5 Build order (6 weeks, solo)

- **W1 — walking skeleton:** VPS + Postgres + TED-CZ connector + extraction v1 + publish top-10-by-money to Buttondown. **Send issue #0 to yourself + 5 friends on Friday.** Success = a stranger-readable email produced by the pipeline from live data.
- **W2:** Hlídač státu connector + dedup stage + Datasette editor flow + start the 50-doc golden set. Issue #1.
- **W3:** PDF pipeline (Semester + IMF + OECD = 3 documents, semi-manual) — national-level evidence that makes records feel authoritative. Astro landing page. Issue #2; start posting cards to LinkedIn.
- **W4 — the differentiation week:** yc-oss loader, 60-slug taxonomy finalized, solved-elsewhere enrichment. Cards now carry the arbitrage line.
- **W5:** VC subsystem v1 (theses YAML + extraction + validation edges + press round-watcher). Auto-drafted "top 10 candidates" editor view.
- **W6:** hardening (healthchecks, Sentry, golden-set regression in CI, pg_dump→R2) + publish the browsable static archive (SEO engine). First actively-promoted issue.

Deferred: NEN, STARFOS, civic scrapers, participatory budgets (a 100-site scraping tarpit — later, 5 biggest cities only), Crunchbase, public API, auth, re-clustering.

### 4.6 Risks

| Risk | Mitigation |
|---|---|
| Scraping fragility | MVP = stable APIs only; raw payloads stored (re-runnable, never data loss); per-connector contract test in CI; fail-soft — one dead connector never blocks an issue |
| Extraction quality | Golden set (50→150 hand-labeled docs) scored on every prompt change; mandatory verbatim-quote grounding; editor gate on everything published; rejection-rate-per-source as the live metric |
| Dedup errors | Under-merge bias; merges are auditable edges (merged_into + attached_by), reversible; weekly 20-min editor pass on the 0.75–0.85 gray zone |
| Cost blowup | Content-hash gate, pre-filter before any LLM call, batch API, hard $40/mo alarm (stops extraction, keeps ingestion — catch-up is free) |
| ToS/legal | MVP sources are open data / free APIs; scrapers polite (1 req/2s, attribution — which is also good product); we publish *our normalized statements with citations* — both the legal safe harbor and the actual value |
| **Content-market fit (the real one)** | Structural: ship an issue every week from week 1 to real readers; editor time > engineering time from week 3; every deferred feature is deferred to protect that loop |

---

## 5. Riskiest assumptions → cheapest tests

| # | Assumption | Test | Kill/go |
|---|---|---|---|
| 1 | Anyone in CZ wants this | **Issue #0 in a Google Doc/beehiiv, 3 evenings, 0 Kč, before writing any code** | ≥300 subs in 14 days, ≥45% open → go; <150 → reposition |
| 2 | Receipts change behavior | Source-link CTR + "pursuing this? hit reply" + claim board from issue #2 | ≥5 "I'm on it" per 1,000 readers by issue #6 |
| 3 | Someone pays CZ prices | Founding cohort presale (1 990 Kč/yr) from issue #5, refund if <30 | 30+ from first ~1,000 subs |
| 4 | Production is sustainable solo | Time-track issues 0–4 | ≤1.5 days/issue by #4, else biweekly-deep |
| 5 | B2B Radar demand exists | 10 cold emails offering a manual sector-alert pilot @ 5 000 Kč/quarter — concierge, no product | 3 paid pilots by month 4 |
| 6 | Arbitrage items surprise insiders | 3 sector insiders pre-read each draft | <1 "everyone knows this" per issue |
| 7 | CZ-only is big enough (probably not) | Month 6: one English CEE mirror issue | English traction decides the month-9 fork |

**Sequencing:** Test 1 before any engineering — v1 is beehiiv + Airtable + a PNG template. The 6-week technical build (§4.5) runs only after issue #0 clears its threshold.

---

## 6. How the pieces reinforce each other

The newsletter funds and focuses the database; the database makes each issue cheaper to produce (candidates auto-drafted, receipts auto-attached); the claim board turns readers into content; follow-ups turn the archive into a public track record; the track record is the moat that no US trend-mill or future copycat can shortcut — because it can only be accumulated weekly, in public, with receipts.
