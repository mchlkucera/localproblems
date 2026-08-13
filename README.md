# localproblems.org

**A public register of local problems and opportunities — with receipts.**

*Project state as of 2026-08-13. Everything in this folder was produced in one Cowork session; this README is the map.*

---

## 1. The vision

The age of AI shifts people from doing jobs to solving problems — but there is no repository of well-stated problems to solve. Solvers are abundant; **stated problems are scarce**. Institutions state problems in silos (tenders, grant calls, diagnostic reports), citizens state them as complaints (civic apps, reviews, petitions), and algorithms infer them from exhaust (the Ideabrowser wave) — but nobody assembles them into one open, structured, geographic register that a builder can browse and **claim**.

The landscape research (docs/01) found the empty quadrant: **local + openly browsable + solver-agnostic**. Global challenge platforms exist (XPRIZE, Wazoku), global AI idea-miners exist (BigIdeasDB, Ideabrowser), closed civic systems exist (311, FixMyStreet) — but a register of *local* problems any solver can pick up exists nowhere. That's this project.

**The product in one sentence:** ingest public signals → LLM-extract normalized problem statements → cross-reference against "solved elsewhere" → publish as a ranked, evidence-backed register + weekly newsletter, where every claim links to a source and every problem can be publicly claimed.

**The user:** someone in Brno — or Munich — opens the site and finds a problem that fits exactly who they are, what their network is, what their skills are. Users are **solvers**; the verb is **claim**.

**Differentiator (the anti-slop covenant):** every number links to a primary source; corrections are printed prominently; scores decompose into receipted components; follow-ups keep a public hit-rate. Evidence, not ideas.

## 2. Signals, ranked by value (the settled hierarchy)

1. **Geographic arbitrage** (proven abroad, absent locally) — the only signal that pre-validates demand AND business model. Build around it.
2. **Regulatory triggers** (compliance deadline creates a market on a date) — rare, highest conviction.
3. **Tenders & grant calls** — real budgets = receipts; mostly serves consultants/dev shops.
4. **Bottom-up complaints** (civic data, reviews, forums) — authentic, local, noisy.
5. **Diagnostic documents** (IMF Article IV, OECD surveys, European Semester) — credibility garnish, never actionable alone.
6. **VC theses & rounds** — lagging confirmation, never discovery. A stamp on a card, not a source of cards.

Scoring encodes this: `score(0-12) = arbitrage(0-3) + money(0-2) + deadline(0-2) + demand(0-2) + gap(0-2) + freshness(0-1)`. Every point requires a receipt. Full rubric: `SCORING.md`.

## 3. Architecture (deliberately minimal)

One git repo, three curl scripts, one weekly scheduled Claude task. No servers, no database — markdown files ARE the database, GitHub Pages renders them, dedup is filesystem-exact at signal level and LLM-judged at problem level. Full design: docs/04 (the simple version) and docs/02 (the earlier full version, kept for when tripwires fire).

- `TASK.md` — the weekly scheduled-task prompt, paste into a recurring Claude task (Mon 06:00)
- `SCORING.md` — the rubric the task applies
- `data/` — the live pipeline output: 66 normalized signals (sorted per source: `normalized/{reg,yc,round,de,dk,pl,ted}/`) → **26 scored problem records** (runs of 2026-08-13; second run added TED procurement + arbitrage/regulatory scans)
- `scripts/` — fetch connectors: `fetch_ted.sh` (TED API v3, paginated CPV groups), `fetch_hlidac.sh` (needs HLIDAC_TOKEN), `fetch_feeds.sh`, `filter_ted.py` (shortlist ranking)
- `site/` — design v2 (current): index, record page P-0001, map view
- `site-v1/` — v1 retro-gazette pages, kept for reference
- `skills/design-language/` — the binding design skill. `site/` follows it as of 2026-08-13; `site/shared.css` is a verbatim copy of the skill's `assets/style.css` (content runs never edit either).

Graduation tripwires (when to un-simplify): >~400 problems or recurring dupes → add SQLite/embeddings for shortlisting; >~10 sources or silent fetch failures → move fetch to GitHub Actions cron; >100 newsletter subs or alert demand → paid Buttondown + small worker.

## 4. Design language (v2)

Modern register, not SaaS, not retro-gazette. Fonts: **Schibsted Grotesk** (voice) + **Spline Sans Mono** (evidence) — both Google Fonts, latin-ext. The governing rule survives from v1: *if a human wrote it, it's grotesk; if a clerk recorded it, it's mono.* Seven-ish tokens (warm paper #FAF9F6, ink #16140E, evidence red #C42B1C used sparingly, status green #177A3D). Score = 12-segment meter. Receipts = numbered source cards with dates. No icons except the status dot, no gradients, no dark mode. Brand is the domain: **localproblems**.org wordmark.

## 5. Current data (runs of 2026-08-13, extract no. 33/2026)

26 problem records, Czechia, ranked — top five after the second (local) run:

| ID | Problem | Score |
|---|---|---|
| P-0001 | Energy communities lose up to ~50% of shared-electricity value; no settlement software — now with a municipal tender receipt (Petrovice u Karviné D&B) | 9/12 |
| P-0008 | NIS2 capacity gap, 6,000+ obligated entities — money now receipted (Motol ~€6.1M, Praha SIEM ~€5.3M + district platform) and CER (zák. 266/2025) piles on | 7/12 |
| P-0002 | Heat-pump/solar installers (23,338 pumps sold 2025) drown in NZÚ paperwork; no vertical SaaS | 7/12 |
| P-0006 | Investment intermediary compliance (ČNB/MiFID + AMLR 2027) | 6/12 |
| P-0010 | Trucking back-office — eFTI regulation (9 Jul 2027) gives the paper CMR an expiry date | 6/12 |

The second run closed the known money gap: the TED connector ran locally (3,048 CZ notices, 5 CPV groups since June), re-scoring p-0017 (EUDIW client tender, ~€78M open, 2→5), p-0008 (4→7) and p-0010 (4→6), and adding 9 new problems (p-0018–p-0026: pay transparency, battery passport, e-shop accessibility enforcement, Data Act, hospital eHealth interop, AI-first accounting, EPBD retrofit analytics, insulation execution, water-utility smart metering). Hlídač státu still needs a token (checklist #3). Two fact-check corrections remain appended inside p-0003 and p-0004.

## 6. Business path (honest math)

Newsletter → landing page is the launch product (docs/02 §3): weekly, one deep receipted card + 4-5 signals. Free → Pro (~2,490 Kč/yr) → B2B Radar (~29,000 Kč/yr, alerts for agencies/dev shops). Czech-only ceiling ≈ 1.2M CZK ARR — a lifestyle business. **The month-9 fork, named on day 1:** (a) English CEE/global expansion (this is why the brand is localproblems.org, English, global-ready), or (b) the B2B alerts/data product becomes the business. Decide by which pulls harder: Radar demand vs. reader geography.

## 7. Do-next checklist

1. **Register domains** (verified free via DNS+RDAP on 2026-08-13 — recheck at registrar): `localproblems.org` (the brand), `problems.cz` + `problems.city` (defensive/expansion, cheap). Optional: `claimed.city` for share links.
2. `git init` this folder; push to GitHub (public repo → free Pages).
3. Get a free Hlídač státu API token (hlidacstatu.cz/api); export as `HLIDAC_TOKEN`.
4. Run the TED connector locally (works outside the sandbox) — this fills the MONEY dimension and re-ranks everything.
5. Set up the weekly scheduled Claude task with `TASK.md` (Mon 06:00), pointing at this folder.
6. Wire GitHub Pages (Jekyll renders `data/problems/*.md` directly — see docs/04 §4 serving notes) or keep hand-built HTML in `site/` short-term.
7. Buttondown account (free ≤100 subs); **issue #0 by hand** — the go/no-go test: ≥300 subs in 14 days from one LinkedIn post + reposts, or reposition.
8. Fold the map-page layout CSS (flagged in `site/map.html`) into the skill's reference stylesheet.
9. Corrections to fold into records at next run: p-0003 permit framing, p-0004 recipient count (already appended in-file).

## 8. Documents index

| File | Contents |
|---|---|
| `docs/01-research-signals-landscape.md` | Deep research: signal taxonomy, ~80 platforms/datasets, who does what, the empty quadrant, data-source stack with API/access notes |
| `docs/02-system-product-design.md` | Full product design (users barbell, newsletter format, monetization, growth loops) + original VPS/Postgres architecture (the "graduate to this later" version) + VC-signal subsystem |
| `docs/03-brand-naming-domains.md` | Brand manifesto, voice, naming territories, visual identity, first domain sweep |
| `docs/04-simple-system-and-domains.md` | **The operative architecture**: repo-as-database, weekly Claude task (TASK.md source), scoring rubric, RDAP-verified domain shortlist |

*Generated with Claude (Cowork). Every factual claim in the data carries its source; treat anything unsourced as an assumption to challenge.*
