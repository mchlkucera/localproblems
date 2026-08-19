---
name: design-language
description: Binding design system for the localproblems.org website. Use whenever generating, editing, or reviewing ANY page, layout, CSS, or HTML for the problems repository site — index pages, problem record pages, category pages, newsletter web versions. Enforces the gazette × land-registry × issue-tracker aesthetic and prevents generic AI design. The weekly pipeline task MUST follow this skill and may never modify assets/style.css or invent new visual elements.
---

# The localproblems.org design language

You are rendering a **state gazette that a very good contemporary designer redesigned in 2026** — official, dense, trustworthy, quietly witty. You are NOT designing a SaaS product, a startup landing page, or a blog.

## Why this file exists

LLMs converge on generic design. The first generation of AI slop was purple gradients, Inter, icon cards, emoji bullets. The second generation — documented by Anthropic's own frontend-design skill — is *fake editorial*: cream paper + high-contrast serif + terracotta accent, or broadsheet layouts with hairline rules used as decoration. **This site is genuinely gazette-derived, which puts it one step from generic-broadsheet slop. The difference is specificity.** Every visual device here encodes something true about the content: rules mark document boundaries, stamps mark lifecycle events, zero-padding marks registry entries, dot leaders join a label to its recorded value. If you add a device that encodes nothing, you have produced slop. Remove it.

The design is fully decided. Your job is to APPLY it, never to reinterpret it. When in doubt between plain and fancy, choose plain. When in doubt between stating a number and describing it, state the number.

## The two voices (the fundamental rule)

**If a human wrote it, it is serif. If a clerk recorded it, it is mono.** No third case.

- **Source Serif 4** (400/600/700): problem titles, body prose, section headings, masthead.
- **IBM Plex Mono** (400/500/600): IDs, dates, sums, scores, deadlines, table cells, labels, buttons, nav, breadcrumbs, footer — anything that could appear in a ledger.
- Both loaded from Google Fonts with `latin-ext` (diacritics in proper nouns verified).
- Never any other font family. Not system-ui. Not Inter, Roboto, Space Grotesk, Geist, Instrument Serif.

## The seven colors (there is no eighth)

```
--paper:     #F8F6F1   page background (the only background)
--paper-2:   #EFECE5   row hover, thead, panels
--ink:       #1A1814   text, strong rules
--ink-muted: #6E6A5F   secondary text, timestamps
--rule:      #CBC6B9   hairlines, dotted leaders
--stamp:     #BB271A   official-stamp red — stamps, urgency, scores 10-12. Max ~5% of any viewport.
--signal:    #1A7A3C   status lifecycle ONLY — currently dormant (dot retired, claiming cut; token stays in the stylesheet)
```

**No dark mode.** A gazette is printed on paper; the paper is the brand. `color-scheme: light only`. The site must photocopy beautifully — there is a `@media print` block and it matters.

## Data formatting (data always looks like evidence)

- Money: mono, euro-first: compact `€450k` / `€7M` for rounded sums, space-grouped `1 250 000` for exact figures. Currency always stated.
- Dates in data positions: ISO `2026-08-13` in `<time>`. Long dates only inside serif prose.
- Alignment (v2): every table column is left-aligned — numerics, dates and sums included. No right-aligned columns anywhere.
- Deadlines: `by 2026-09-30 · T−48`; when T < 14, class `.urgent` (stamp red).
- IDs: `{CITY3}-{NNN}` zero-padded: `BRN-041`. Scores `09/12`. Issue `no. 33`. **Zero-padding is the house tic** — everything countable is padded.
- Scores render as **tally ticks** (survey chain marks) + zero-padded fraction: the 12-tick total tally in the index, and per-dimension tallies (`--s` of `--max`) in the scorecard. Never progress bars, gauges, stars, or rings.
- Score verdicts: one word, mono, uppercase, taken verbatim from SCORING.md's verdict tables (e.g. `VALIDATED`, `UNFUNDED`, `STRONG`). Never invent a verdict word per page.

## Page anatomy

- **Masthead on every page**: 4px ink bar, then `localproblems.org` (serif 700) with `vol. {YYYY} · no. {ISO-week}` (mono) right-aligned, then 1px rule. The weekly build IS a publication issue — the automation is the brand.
- **Index = a register table**, not cards: 6 columns (ID / title / category / locality / score / updated — all left-aligned per v2; the dot column is retired with the status dot). Title is the ONLY serif cell. ~20–24 rows per viewport. Pre-sorted by score desc at build time; caption states the sort and extract date. **Zero JavaScript** — filtering is a build-time concern: the register carries a **category filter nav** (mono `.filters` line, v1 grammar `All (31) · B2B (07) · …`, counts zero-padded, current entry `aria-current`) linking to pre-generated category pages.
- **Category pages** (reinstated by owner mandate 2026-08-19): `/category/[slug]` for ALL twelve categories, slug = the category id verbatim. Same masthead, crumb (`Problems / {Category}`), site nav, the same filter nav with the current category marked, and the register table filtered — identical column grammar, category column kept (one table grammar everywhere). A category with no problems still gets its page with the house empty-category string — an empty register is a registered fact. The record page's crumb category links back to its category page.
- **Problem page** (v1.4 rebuild, 2026-08-19 — fixed-role sections a reader learns once): **docket** (3px double rule, mono ID, serif title, then the **dek** — one muted serif standfirst sentence, derived at build from the who-pays paragraph's opening sentence(s) (absorbing until ≥40 chars so a punch opener never ships alone), never a stored field; facts grid reduced to Category (linked to its category page) / Locality / Window (`by <ISO>`, only when a future deadline is on file); housekeeping demoted to one quiet mono **meta line** at the docket's bottom edge: `S01–S{NN} on file · updated … · created …` — Updated/Created/Sources never render as loud facts) → **scorecard** (the top-line band, see below) → **The problem** (lead prose + the existing-non-solutions paragraph, serif, max 62ch, every figure carries a source link) → **The window** (why-now prose + a ledger of the urgency receipts; a future-dated receipt renders as the `.deadline` device — `by 2026-09-30 · T−48` at h2 size, `.urgent` inside T−14) → **How big** (who-pays prose + a ledger of the money receipts with their recorded euro figures; no receipts → the house absence line — never an estimate) → **Who builds this** (the buildability facts grid: CAPITAL with its ladder range muted beside it, FIRST REVENUE, BUILDER; one muted serif `.buildnote` sentence under it) → **Where it works** (solved-elsewhere prose + the comps ledger: two-line `.entry` rows — serif linked name · geo · since, dot-leader to the evidence-layer ref; traction as a muted serif note line; empty comps → the house absence line) → **First moves** (records scoring ≥ 7 only: numbered `ol.prose` steps, named competition, the open subsidy call cross-linked into the tenders ledger) → **Record updates** (dated update tails; CORRECTION paragraphs carry the `.correction` 4px left rule — a correction interrupts the record) → **Sources** (one-line ledger entries S1…Sn: S-number, linked name, dot leader, date — the name IS the link, no note or URL lines) → footer with record provenance. **Score rundown dialogs** unchanged (native `popover` — each scorecard dimension is a button opening a centered dialog with an ink scrim: dimension label · figure · wide tally · verdict → hairline rule → rubric criterion → the embedded source records it references; close cross `×` top-right, declarative `popovertargetaction=hide`; light-dismiss, no scripting; the score is explained in exactly ONE place), except the **total dialog**: one quiet sentence (`Five dimensions — proof, money, urgency, demand, gap — each point justified by a source on file.`) above the borderless `.bands` legend — four band rows, the current band marked `→` and set 600. Market math stays a hand-curated device (grammar retained for curated exhibits); the comps ledger is now generated from record frontmatter.

## The scorecard (the "how good is it" band)

Sits immediately under the docket on every problem page — the first thing a solver reads, comparable across every record. It answers "how good is this opportunity, objectively?" before a single line of prose. Rules:

- **Five dimensions + total**, exactly as defined in SCORING.md: PROOF / MONEY / URGENCY / DEMAND / GAP. Never invent, drop, or reorder a dimension per page.
- Each dimension is a stacked mono column: uppercase label → zero-padded figure (`3/3`) → tally ticks sized by `--s`/`--max` → one-word uppercase **verdict** from SCORING.md. Nothing else — no sentences, no icons, no color-coding beyond the rules below.
- The **TOTAL** sits right, separated by hairlines like every dimension, and carries the largest figure on the page (`--fs-title`). Totals 10–12 take `.score-high` (stamp red on the number).
- **Zero-scoring dimensions render muted** (`.is-zero` greys number and verdict) — absence is stated, never hidden. A 0 with a source-less note is honest; an omitted dimension is a lie.
- Every dimension is a **button** (`popovertarget`) opening its rundown dialog (`#d-proof` …, total → `#d-total`) — native popover, no JavaScript. The scorecard asserts, the rundown proves, the sources testify.
- Hairline separators only; no cards, no backgrounds beyond the `--paper-2` hover on the anchor.

## The five signature moves (the only permitted flourishes)

1. **The stamp**: mono 600 uppercase, 2px border, `rotate(-2deg)`, `mix-blend-mode: multiply`. Overlay variant (`rotate(-8deg)`, centered) ONLY for CLAIMED / SOLVED / CLOSED. Max one overlay per page. DORMANT with claiming cut (owner, 2026-08-13) — no lifecycle event currently earns a stamp; grammar retained in the stylesheet.
2. **Cadastral rules**: exactly three meanings — 4px solid = page begins; 3px double = major boundary; 1px solid = row hairline. No other border weights (2px reserved for buttons/stamps).
3. **Gazette numbering**: `vol. 2026 · no. 33` in masthead, echoed in breadcrumbs.
4. **The status dot** — RETIRED (owner, 2026-08-13): kept in the stylesheet grammar, never emitted; returns only if lifecycle states actually diverge. When live it is the ONLY circle and ONLY icon on the site: hollow green = open, filled = claimed, filled + outline ring = solved, hollow grey = closed.
5. **Dot leaders**: label→value pairs may be joined by a 1px dotted leader ONLY where the pair has no rule of its own (forms, facts). In ruled ledger lists (sources, comps, market math) the leader is a blank spacer — one row, one line, never two.

## Spacing and rhythm (v1.1)

- **One 4px scale**: `--sp-1…--sp-8` = 4 / 8 / 16 / 24 / 32 / 48 / 64px (with 12px as `--sp-3`). Every margin, padding, and gap is a step on this scale — no ad-hoc values. Sole exceptions: optical micro-padding inside the stamp and exhibit chip, and the 7.5rem receipts indent column.
- **Sections breathe from above**: `h2` carries 48px above, 16px below — roughly 3:1. Air binds a heading to what follows, not to what precedes.
- **The docket is the title block**: it gets the most air on the site — 24px above the ID, 24px around the title, 48px clearance before the prose begins.
- **Ledger density**: register and signals rows sit at 8px vertical padding; 12px cell gutters; 24px page gutter; 32px facts-grid column gap. Dense is fine, squeezed is not.

## Signals architecture (v2 — implemented 2026-08-13)

- One ledger page per **evidence type**, generated by the web app from `data/signals/<type>/*.jsonl`: `/sources/funded` (companies founded and financed — market scans, YC, rounds), `/sources/regulation` (triggers with dates), `/sources/tenders` (public money on record), `/sources/demand` (documented complaints and unmet needs). These replace the v1 per-feed pages; the earlier origin-group hub design was superseded by SPEC.md's evidence types before being built.
- The problem register and the source ledgers are clearly separated surfaces: nav reads `Problems` then `Sources: Funded · Regulation · Tenders · Demand`. Source pages live under `/sources/[type]` (moved from `/signals/[type]`); the data directory stays `data/signals/`.
- All signal tables share one fixed column layout, declared by a `<colgroup>` of column classes (`c-name c-src c-cat c-geo c-val c-rec c-date` — widths live in the stylesheet, `:has(col.c-name)` switches the table to fixed layout): Name / Source / Sector / Origin / Value / Record / Date. The Source column names where the signal came from — the **country** for market scans, the feed for everything else (Regulations, TED, Contract registry, Y Combinator, Rounds).
- Name is the only serif cell, links to the source URL, carries the recorded summary as its `title` attribute, truncates with ellipsis. Each row's anchor is its signal id — the provenance target for record-footer links.
- An empty evidence type still gets its page with the empty-category line — a pending feed is a registered fact, not a hidden one.
- These pages are GENERATED (Next.js app in `web/`, pure SSG — SPEC.md §5). Never hand-edit output; change the data or the app.

**Implementation status:** v2 is live — every column left-aligns, the source ledgers are generated from the evidence layer, and `scripts/build_sources.py` + hand-built `site/` pages are retired. The stylesheet is at **v1.4** (2026-08-19 record-page rebuild: `.dek`, docket `.meta`, `.deadline`, `.rundown .bands`, two-line `.comps .entry`, `ol.prose`, `.correction`, `.absent`, `.buildnote` — all on the existing tokens and scale). `web/shared.css` must stay a verbatim copy of `assets/style.css`; the app's build asserts checksum equality.

## The anti-slop rulebook (hard NEVERs)

1. NEVER any font beyond Source Serif 4 + IBM Plex Mono.
2. NEVER center or right-align text — every column, numerics included, left-aligns (v2). The dot cell centers; nothing else.
3. NEVER `box-shadow` or blur — elevation does not exist on paper.
4. NEVER `border-radius` except the status dot. Corners are square. Zero, not 2px.
5. NEVER gradients as color (sole exception: the hard-stop tick pattern inside `.tally`).
6. NEVER icons, emoji, or SVG decoration. Text `→`, `·`, and the dialog close `×` are permitted.
7. NEVER a color outside the seven tokens. No hover tints, no rgba improvisation.
8. NEVER animate. No transitions. Hover changes are instant.
9. NEVER set a figure, date, ID, or sum in serif.
10. NEVER progress bars, gauges, star ratings, percentage rings.
11. NEVER marketing adjectives in chrome ("amazing", "🔥"). Every claim links to its source.
12. NEVER more than one overlay stamp per page; never spend stamp red on >5% of a viewport.
13. NEVER JavaScript. Sorting/filtering are build-time concerns.
14. NEVER more than 7 index columns; titles truncate with ellipsis, never wrap.
15. NEVER cards or section backgrounds beyond `--paper-2`. There are no cards; there are ruled records.
16. NEVER modify `assets/style.css` during a content run. Invent no classes, colors, or sizes — if a needed class doesn't exist, flag it in the run summary instead of improvising.

## Sanctioned exceptions (owner-approved)

1. **Relative dates**: `time.rel[datetime]` may render Notion-style relative text (today / yesterday / N days ago; 7+ days stays ISO) via the tiny progressive script. The ISO date always remains in `datetime` + `title`; the page must read identically with JS off. This narrows NEVER 13 — no other JavaScript is permitted.

The v1.3 facts-glyphs exception (`⚡︎` category, `⌖` locality in the facts grid) was REVOKED by the owner 2026-08-13 — no glyphs anywhere; NEVER 6 applies in full.

## Copy for UI chrome (exact strings)

The site is English-only; render these strings exactly.

| Slot | String |
|---|---|
| Empty category | `No open problems on record in this category. As of {date}.` |
| Table caption | `Sorted by score, descending · extract generated {date}` |
| Corrections | `Source wrong? Corrections →` |
| Footer | `Data as recorded, no warranty. Sources with links. Extract no. {NN}/{YYYY}, generated automatically.` |
| 404 | `Record not found. Either it never existed, or it was solved so thoroughly it disappeared.` |
| No money receipts | `No sized figure on file.` |
| No comparables | `No verified foreign comparable on file. As of {date}.` |
| Total-dialog rubric | `Five dimensions — proof, money, urgency, demand, gap — each point justified by a source on file.` |

Buttons: uppercase mono, verb-first, one verb. Never an exclamation mark in chrome. "Problem" is never softened to "challenge".

## Implementation

The complete reference stylesheet is in `assets/style.css` (part of this skill). It implements every token and component above and is the ONLY stylesheet the site uses. Its live copy is `web/shared.css` — the web app's build fails on any checksum drift between the two. Content runs never touch either file.

Weekly build rules: compute `no. NN` as zero-padded ISO week; compute `T−n` from deadlines; sort index by score desc then updated desc; set tally fill via inline `style="--s:9"` (scorecard tallies additionally carry `--max`); pull dimension scores and verdict words from SCORING.md; verify every page against the NEVER list before committing.

## Quality gate (optional but recommended)

After generating HTML, run `npx impeccable detect` (59 deterministic anti-slop rules, no API key) and treat any finding as a build failure to fix before commit.
