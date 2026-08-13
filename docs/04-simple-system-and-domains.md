# The Simple Version + Verified Domains

*August 13, 2026 · Replaces the VPS/Postgres design for v1*

---

## Part 1 — Signals ranked by value (the short list)

| # | Signal | Value | Verdict |
|---|---|---|---|
| 1 | **Geographic arbitrage** (proven abroad, absent in CZ) | ★★★★★ | The only signal that pre-validates demand AND business model. Build around it. |
| 2 | **Regulatory triggers** (new law + compliance deadline) | ★★★★★ | Rare, but highest conviction — you know the date demand arrives. |
| 3 | **Tenders & grant calls** | ★★★ | Real budgets = receipts. But mostly serves consultants/dev shops, not product founders. |
| 4 | **Bottom-up complaints** (reviews, forums, civic data) | ★★★ | Authentic and local; noisy; rarely says who pays. |
| 5 | **Diagnostic docs** (IMF/OECD/Semester) | ★★ | Credibility garnish ("OECD says…"). Never actionable alone. |
| 6 | **VC theses & rounds** | ★ | Lagging confirmation, not discovery. A stamp on a card, never a source of cards. |

Rule: an item ships when Tier 1 (rows 1–2) provides the *why now* and Tier 2 (rows 3–4) provides the *receipts*.

---

## Part 2 — The radically simplified system

**One git repo, three curl scripts, one weekly scheduled Claude task. Infra cost: $0 + domain. Setup: one afternoon.**

### The three stages, mapped to folders

```
cz-problems/                     # one public GitHub repo = the entire system
├── TASK.md                      # the scheduled-task prompt (versioned)
├── SCORING.md                   # ranking rubric Claude applies every run
├── CONVENTIONS.md               # fixed categories, ID scheme, statuses
├── scripts/                     # STAGE 1: SOURCE — 3 curl scripts (~15 lines each)
│   ├── fetch_ted.sh             #   TED API, no auth, CZ filter
│   ├── fetch_hlidac.sh          #   Hlídač státu, free key
│   └── fetch_feeds.sh           #   CzechCrunch/Vestbee RSS, yc-oss, EUR-Lex RSS
├── sources/2026-08-13/          #   raw dated fetches, pruned after 28 days
├── normalized/                  # STAGE 2a: one .md per signal; FILENAME = canonical ID
│   └── ted-2026-489123.md       #   file exists → already seen → skip (dedup = filesystem)
├── problems/                    # STAGE 2b: one .md per problem = THE DATABASE
│   ├── INDEX.md                 #   id | title | category | score | status | aliases
│   └── p-0031-....md            #   YAML frontmatter + 3-6 paragraph statement
├── newsletter/2026-08-13.md     # STAGE 3: weekly draft — you review, paste, send
└── _layouts/problem.html        #   GitHub Pages renders problem files DIRECTLY
```

The key deletion: **there is no site generator and no build step.** GitHub Pages' built-in Jekyll renders the problem markdown files as landing pages directly — one layout file written once, an index sorted by score with a Liquid template. "Deploying the site" = `git push`.

### How dedup works without a vector database

Signal level: deterministic — canonical ID from the source (TED notice number etc.); if the file exists, skip. Exact, free, never breaks. Problem level: Claude reads INDEX.md (300 problems ≈ 8k tokens, fits easily), shortlists 2–3 candidates, opens them, decides merge vs. new. At this scale an LLM beats embeddings — it knows "povinné datové schránky pro OSVČ" and "mandatory e-boxes for freelancers" are the same problem; cosine similarity often doesn't. Honest limit: past ~400–800 problems this gets sloppy — that's tripwire #1.

### The scheduled task prompt (paste into a weekly Cowork scheduled task, Mon 06:00)

```
You are the weekly pipeline for the cz-problems repo at ~/cz-problems.
Work autonomously; do not ask questions. If a step fails, note it in
sources/<today>/manifest.md and continue with what you have.

0. SYNC: cd ~/cz-problems && git pull. Read CONVENTIONS.md and SCORING.md.

1. FETCH: mkdir sources/<today>. Run scripts/fetch_ted.sh, fetch_hlidac.sh,
   fetch_feeds.sh. Write manifest.md (per source: item count or FAILED + error).
   First run of each month only: also web-fetch the EC Have Your Say open
   consultations page, the Dealroom Czech Republic page, and skim any new
   OECD/IMF CZ country notes; save relevant extracts under sources/<today>/.
   Delete sources/ folders older than 28 days.

2. NORMALIZE: For each raw item, canonical ID = source + native ID (TED notice
   no., Hlídač ID, sha1-8 of URL for feeds). If normalized/<id>.md exists, SKIP.
   Otherwise create it with frontmatter (id, source, url, date, category from
   the fixed list in CONVENTIONS.md, tier 1/2/3, geo) and a 2-sentence summary.
   Discard items with no plausible CZ problem/opportunity angle - be strict;
   fewer, better signals. Expect to keep well under half.

3. SYNTHESIZE: Read problems/INDEX.md in full. For each new normalized signal
   (or cluster of related signals):
   - If it matches an existing problem (check titles AND aliases; open the 2-3
     closest candidate files to confirm): append to its receipts[], update the
     body if the picture changed, add any new alias, bump `updated`.
   - Only create a NEW problem file when signals evidence a distinct problem:
     next id from INDEX, kebab-case slug, use the frontmatter template, write a
     3-6 paragraph statement (problem, why-now, who-pays, existing non-solutions,
     comparable foreign players). Never create a problem from a single Tier-3
     signal alone.
   - Prioritize Tier 1 (geographic arbitrage, regulatory triggers), then Tier 2
     (tenders/grants, bottom-up complaints). Tier 3 is supporting evidence only.

4. SCORE: For every problem created or touched, set signals{} and score per
   SCORING.md exactly. Decay: any problem whose newest receipt is >120 days old
   loses freshness and moves status active->watching; >240 days -> stale.

5. INDEX + SITE: Regenerate problems/INDEX.md (sorted by score desc). The site
   is rendered by GitHub Pages from the problem files directly - verify
   frontmatter is valid YAML on every file you touched; that is the entire
   "site build".

6. NEWSLETTER: Write newsletter/<today>.md: top 3 problems by score this week
   (2 short paragraphs + receipts links each), 3-5 one-line "movers" (new or
   rescored), 1 regulatory deadline to watch. Czech language, direct tone,
   no filler. This is a DRAFT for human review - do not send anything.

7. COMMIT: git add -A && git commit -m "weekly run <today>: +N signals,
   +X new / Y updated problems" && git push. End by printing a 5-line run
   summary (fetched / kept / new problems / updated / top mover).

Quarterly (first run of Jan/Apr/Jul/Oct): dedup sweep - scan INDEX.md for
near-duplicate problems, merge them (union receipts, keep older id, add
redirect note in the dropped file, status: rejected, body: "merged into X").
```

### The scoring rubric (SCORING.md — matches the re-ranked signal tiers)

```
score = arbitrage + money + deadline + demand + gap + freshness    (0-12)

arbitrage (0-3)  0: no foreign analog · 1: one weak analog · 2: funded analog in
                 DE/AT/PL/Nordics + no CZ player found · 3: analogs in 2+ markets
                 AND validated CEE-adjacent
money (0-2)      0: none · 1: relevant tender/grant exists · 2: OPEN tender/grant
                 >= ~5M CZK or recurring annual spend
deadline (0-2)   0: no regulatory trigger · 1: compliance date >18mo out ·
                 2: compliance date <18mo (forcing function live)
demand (0-2)     0: assumed · 1: scattered complaints · 2: recurring documented
                 complaints, petition, or industry pressure
gap (0-2)        0: CZ incumbent check not done · 1: quick search found no CZ
                 player · 2: absence confirmed or only weak/legacy incumbents (named)
freshness (0-1)  1: newest receipt < 90 days

Rules: every point must be justified by a receipts[] entry - no receipt, no point.
Tie-break by (deadline, money). Tier-3 sources can never lift arbitrage or demand
above 1 on their own. Score >= 8 = newsletter-lead material.
```

Note how the caps encode your re-ranking: arbitrage maxes at 3 (dominates), regulatory deadline and money co-drive, VC/diagnostic garnish can never move a rank on its own.

### Cadence, cost, serving

Weekly (Mon 06:00) — tenders move weekly, regulation moves monthly; daily runs would burn ~7× tokens for ~1.1× signal. A run: ~50–150 new signals, ~20–45 min, comfortably inside a Claude subscription's weekly budget (would be ~$2–6/run at API prices). Missed run because laptop was off = nothing lost; next run backfills (fetch windows overlap, IDs dedup exactly).

Hosting: **GitHub Pages** (free, renders the markdown natively; public repo required — fine, the data is public-web-derived and openness is marketing). Custom domain = CNAME file + 4 A records, 15 minutes. Newsletter: **Buttondown free tier**, manual paste of the draft — the human-review step is a feature; an LLM-drafted newsletter should not auto-send.

### Graduation tripwires (when to un-simplify)

1. **>~400 problems or the quarterly sweep merges >5% of the index** → add SQLite/embeddings for candidate shortlisting only; files stay the source of truth.
2. **>~10 sources or two consecutive silent fetch failures** (or laptop-off misses 2+ runs/quarter) → move the fetch scripts to a GitHub Actions cron; Claude still does synthesis.
3. **Need for subscriber alerts or >100 newsletter subs** → paid Buttondown + a small always-on worker. That's the moment part of the VPS design returns — not before.

### One-afternoon setup

1. `git init` + folder skeleton · 2. commit TASK.md / SCORING.md / CONVENTIONS.md · 3. write 3 curl scripts, get free Hlídač key, test by hand · 4. have Claude generate `_config.yml`, one layout, index + 11 category pages (30 min) · 5. push public repo, enable Pages · 6. CNAME + A records · 7. Buttondown account, embed subscribe form · 8. create the weekly scheduled task · 9. fire it once manually, review the first commit. Live.

Total maintenance surface forever: **3 curl scripts, 1 prompt file, 1 layout file.**

---

## Part 3 — Domains, actually verified

Method: DNS (NXDOMAIN) cross-checked against registry RDAP endpoints (404 = free, data = taken). The .eu registry blocks RDAP from this environment, so .eu results are DNS-only.

### ✅ VERIFIED FREE — the purchase shortlist (both checks agree)

| Domain | Why |
|---|---|
| **problems.cz** | The literal category-owner name — confirmed genuinely free |
| **problems.city** | The expansion twin: problems.city works city-by-city across Europe |
| **homefield.city** | Best available Homefield (com/cz/io/eu/app/dev all taken) |
| **mezera.io** | The Mezera brand's flagship (+ mezerahq.com free for email/.com credibility) |
| **domacivyhoda.cz** | "Home-field advantage" in Czech — exact phrase |
| **domacivyhoda.com** | International protection for the CZ brand |
| **heimvorteil.app** | The Munich twin — "home-field advantage" in German (de/com/eu taken, .io also free) |
| **claimed.city** | The claim mechanic; great for share links (claimed.city/04) |
| **mojeparketa.cz** | Sleeper pick: "moje parketa" = Czech idiom for "my turf/my forte" — literally the product's matching promise |
| **najdimezeru.cz** | "Find the gap" imperative — campaign domain for Mezera |
| **rajon.io / myrajon.com** | "Rajón" = colloquial Czech for home turf; reads via "Rayon" in German |
| Also free: | gapfield.com, problemfeed.com, openproblems.cz, openissues.dev, gapmap.cz, opengaps.cz, claimspot.cz, resito.cz, nevyreseno.cz, themezera.com, domaci-vyhoda.com |

### Agent's top 5 registration bundles

1. **problems.cz + problems.city** — category-defining defensive pair, pennies
2. **mezera.io + mezerahq.com** — the Mezera identity fully securable
3. **domacivyhoda.cz/.com + heimvorteil.app** — the "home-field advantage" concept in the native language of both launch markets
4. **homefield.city** — the one open Homefield door
5. **mojeparketa.cz** — ownable native idiom, zero competition

### ❌ Notable takens (newly determined)

heimvorteil.de/.com/.eu · myhomefield.com · homefieldhq.com · skulina.cz · problems.io · problemmap.com · openproblems.com · claimspot.com · rajon.cz · parketa.cz · solvery.cz · gaps.cz · vyzvy.cz · resimo.cz · claimed.app

*(Likely free, DNS-only, unconfirmable .eu: solvery.eu, vyzvy.eu, localproblems.eu, openproblems.eu.)*
