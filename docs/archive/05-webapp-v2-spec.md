# 05 — localproblems.org v2: the generated register (Next.js app spec)

*Spec date 2026-08-13. Status: draft for owner review. Supersedes the "no build step" serving model of docs/04 §4 for the site only — the pipeline, repo-as-database, and scoring model are unchanged.*

## 1. Why v2 exists

v1 serves hand-built HTML from `site/`. Today's second pipeline run proved the failure mode: the register grew from 17 to 26 problems and the site silently kept showing the old extract until a human noticed. Hand-updating HTML does not survive a weekly automated pipeline.

v2 makes the site a **pure function of `data/`**: the weekly task commits markdown, Vercel builds, the register is current. Nobody edits HTML again.

**Decisions taken (owner, 2026-08-13):** platform **Vercel** · claiming **deferred to v3** · scope **full register at launch**.

## 2. Non-goals (v3+ or never)

- **Claiming** — v3. v2 renders the claim block per the design language, but the button is a prefilled `mailto:` link. No fake UI, no accounts, no database.
- Alerts / B2B Radar, API access, search, i18n of chrome (site chrome stays English; content carries Czech proper nouns; newsletter archive renders Czech with `lang="cs"`).
- Dark mode — never (design law: the paper is the brand).
- A CMS. The repo is the CMS.

## 3. Architecture

```
localproblems/
├── data/                  ← canonical content (unchanged; written by the weekly task)
│   ├── problems/*.md      ← 26 records, YAML frontmatter + prose body
│   └── normalized/<src>/  ← signals (now carry `title:` for display)
├── site/                  ← v1 static pages; retired at Phase 3
└── web/                   ← NEW: the Next.js app (v2)
    ├── app/               ← App Router routes (all React Server Components)
    ├── lib/data.ts        ← reads ../data at build time, zod-validated
    ├── lib/scorecard.ts   ← v1→v2 score mapping + verdict words (one file)
    └── shared.css         ← the design system stylesheet (see §6)
```

- **Next.js, latest stable, App Router, TypeScript.** Server Components only; no client components. The single sanctioned script (relative dates, design-language v1.3 exception 2) ships as the same inline progressive snippet v1 uses.
- **Pure SSG.** Every route is statically generated at build (`generateStaticParams`). No runtime data reads, no ISR — content changes arrive as git commits, and commits trigger deploys. `dynamicParams = false`; an unknown id is a built 404.
- **Deployment:** Vercel project rooted at `web/`, production = push to `main`. No runtime secrets (public data only). The weekly pipeline's `git push` (TASK.md step 7) is the deploy trigger — no extra wiring.

## 4. Data contract (`lib/data.ts`)

Single module that reads and validates the repo at build time. **Validation failure = build failure = deploy blocked.** This replaces TASK.md step 5's "verify frontmatter is valid YAML" with something enforceable.

- **Problem schema** (zod): `id (p-\d{4})`, `title`, `category` (the fixed CONVENTIONS.md list), `geo`, `score (0-12)`, `signals{arbitrage 0-3, money 0-2, deadline 0-2, demand 0-2, gap 0-2, freshness 0-1}`, `status (candidate|active|watching|stale|claimed|solved|rejected)` — the enum includes every state TASK.md's decay rules produce (`active→watching→stale`), `receipts[]{type, url, note, date, dims?}`, `created`, `updated`, markdown body. Assert: `score == sum(signals)`; `receipts.length ≥ 1`; dates ISO. Receipt `type` is an open set with known values `arbitrage | tender | contract | subsidy | regulation | complaint | news | gap-check | round`; unknown types are valid (build warning, ledger-only rendering).
- **Status → rendering**: `candidate/active/watching/stale` → open dot, listed in the register; `claimed` → claimed dot + stamp; `solved` → solved dot + overlay stamp; `rejected` (quarterly-dedup tombstones) → closed dot, **excluded from the register table**, page renders the "merged into P-00XX" note with a redirect link.
- **Signal schema**: `id`, `title`, `source`, `url`, `date`, `category`, `tier (1|2|3)`, `geo`, `summary_en`, `money_eur (number|null)`, `money_note`. Directory name must equal `source`.
- **Frontmatter stays v1.** The v2 scorecard (SCORING.md: PROOF / MONEY / URGENCY / DEMAND / GAP + verdict words) is **derived** in `lib/scorecard.ts`: `proof = arbitrage`, `urgency = deadline + freshness`, verdict words and total bands (PRIME 10–12 · STRONG 8–9 · FAIR 5–7 · FAINT 0–4) hardcoded as constants **with a build-time assertion that each word appears verbatim in SCORING.md** — drift breaks the build instead of the page. Index tie-break: score desc, then (urgency.deadline, money), then id.
- **Receipts → page elements**: receipts render as the Sources ledger `S1…Sn`. Display name: if `note` begins with `<signal-id>:` and that signal exists, use the signal's `title` (and link its `url`); otherwise a label derived from `type` + URL host. `→ S` refs are **on-page anchors** to the record's own ledger (`#s1`, v1 behavior); ledger entries additionally link the signal's anchor on the sources pages.
- **Rundown-drawer refs** (`→ S1, S3`) resolve per dimension, in priority order:
  1. an explicit `dims:` tag on a receipt (optional list, overrides everything);
  2. receipt type → dimension: `arbitrage→proof`, `tender|contract|subsidy→money`, `regulation→urgency(deadline)`, `complaint|news→demand`, `gap-check→gap`; additionally a `gap-check` receipt whose note contains `"Demand point"` also maps to **demand** (the recorded v1 convention — 6 current records carry it; the seventh, p-0002, carries an explicit `dims: [proof, demand]` tag);
  3. the **freshness** component of urgency always refs the newest receipt dated < 90 days, regardless of type (freshness is justified by recency, not receipt kind).
  Drawer text = the SCORING.md criterion for the achieved level (rubric words, not invented prose) + refs. `—` is rendered **only for a dimension scored 0** (per the design skill). A **nonzero** dimension that resolves no ref after all three rules renders `→ see sources` (linking `#sources`) and logs a build warning — the audit of current data says this should be zero cases; the warning exists to catch future drift.
- Markdown body → HTML with a minimal renderer (paragraphs, links, strong, the `---`-separated CORRECTION blocks styled as the corrections device). No MDX, no plugins.

## 5. Routes

| Route | Content |
|---|---|
| `/` | The register table (7 columns, tally scores, crumb stats — all counts computed from data) + category filter nav |
| `/problem/[id]` | Docket → scorecard band → rundown drawers (native `popover`, zero JS) → problem prose → Sources ledger → claim block (`mailto:`) → provenance footer |
| `/category/[slug]` | Pre-filtered register per category; empty-state house string |
| `/sources` + `/sources/[group]` | Follows the design skill's **"Sources architecture (v2)"** verbatim: a hub page plus the four origin-group pages (market / top-down / bottom-up / capital) with the skill's fixed table columns. Source keys map to groups in one `lib/` constant: `de,dk,pl → market`, `reg,ted,hlidac → top-down`, complaint/civic feeds → `bottom-up`, `yc,round → capital` (yc placed per the skill's feed listing — confirm with the design-skill owner; moving it is a one-line change). Anchor per signal id (the target of provenance links from record footers). |
| `/map` | **Re-implementation, not a port**: locality shapes rendered as inline SVG at build time from the simplified GeoJSON (server-side, zero client JS — v1's Leaflet is dropped; it violates the no-JS rule). Precondition: the map-layout classes flagged in v1 `map.html` are folded into the skill stylesheet first (README checklist #8, a design-skill change, not app code). |
| `/newsletter` + `/newsletter/[date]` | Buttondown signup + web archive of `newsletter/*.md` (rendered, `lang="cs"`). **Only issues with frontmatter `status: published` appear**; the weekly task writes drafts without it and the owner flips it after review — the archive can never auto-publish an unreviewed draft. This gate ships with the route (Phase 2), and TASK.md step 6 gains the corresponding note at Phase 2, not Phase 3. |
| `/about` | Short static page: what the register is, the anti-slop covenant, corrections policy |
| 404 | House string: "Record not found. Either it never existed, or it was solved so thoroughly it disappeared." |

`next.config` redirects map v1 paths (`/site/problem-p-0001.html`, `/problem-p-0001.html` → `/problem/p-0001`) so existing links survive.

Per-route metadata (title, description) from data; OG images deferred (a gazette does not need social cards to launch — revisit with v3).

## 6. Design system (binding)

- The **design-language skill governs all markup this app emits.** The generated pages reproduce the v1.3 gazette structures verbatim: masthead, register table, docket, scorecard + rundowns, sources ledger, claim block, footer strings — the exact class vocabulary of `shared.css`.
- `web/shared.css` is a **verbatim copy of the skill's `assets/style.css`**, imported as the app's only global stylesheet. Build step asserts checksum equality with the skill asset and fails on drift — the skill remains the single design source; app code never adds classes, colors, or sizes (NEVER 16).
- **Fonts:** served via `next/font` (self-hosted Source Serif 4 + IBM Plex Mono, `latin-ext`) instead of the Google Fonts `<link>`. Same families, same weights; removes the render-blocking third-party request. ⚠ This is a loading-mechanism deviation from the skill's wording ("loaded from Google Fonts") — needs design-skill owner sign-off; if declined, keep the `<link>`.
- All NEVER rules apply to generated output. CI runs `npx impeccable detect` against the built HTML as a warning-level gate.

## 7. Claim seam (so v3 is additive)

- Problem frontmatter already carries `status`; v3 adds `claimed{date, handle, link}` — a schema extension, not a break.
- v2's claim block links `mailto:claim@localproblems.org?subject=CLAIM P-00XX` with a body template. Claims arriving by mail are recorded by editing frontmatter (status + stamp render automatically).
- v3 upgrades the button to a form + moderation without touching any v2 page structure.

## 8. Testing

- **Unit** (vitest): frontmatter parsing edge cases; scorecard mapping — verdict words, band edges (4/5, 7/8, 9/10), tie-break order; receipt→source-name resolution; receipt-type→dimension refs.
- **Fixture snapshots**: one synthetic problem + signals fixture → index row HTML and record page HTML snapshots (catches accidental structure drift against the design system).
- **Build asserts** (the real gate): schema validation over all real data, score-math equality, SCORING.md verdict-word presence, stylesheet checksum.
- **Smoke e2e** (playwright, 3 tests): index row count equals the number of non-rejected problem records (never a hardcoded count — the pipeline grows it weekly); a record page's rundown anchors resolve; 404 string renders. Runs on CI only.

## 9. Migration plan

1. **Phase 1 — parity:** scaffold `web/`, implement data layer + index + record pages; side-by-side **structural** fidelity check against `site/index.html` and `site/problem-p-0001.html` — structure and class vocabulary must match; content comes from `data/`, which is fresher than the hand pages (the v1 P-0001 page shows a stale score and a hand-picked source list). P-0001's hand-written Market-math and Solved-elsewhere sections become the first entries of an optional `extras/` include slot — hand-authored HTML fragments injected under the sources section, per problem id, so hand curation survives generation. The docket's "Solved elsewhere: N comparables" facts row renders only when the record's extras fragment exists and declares its comps count (`data-comps` attribute); otherwise the row is omitted.
2. **Phase 2 — full register:** categories, sources, map, newsletter, about, redirects; deploy to Vercel; wire `localproblems.org` when registered (README checklist #1).
3. **Phase 3 — retirement:** move `site/` to `site-v1-static/` alongside the existing `site-v1/`; update README §3/§4, TASK.md step 5 ("run `npm --prefix web run build`; a failing build means invalid data — fix data, never the app"), the design-language skill's implementation note, and session memory. Hand-editing HTML is dead from this point.

Rollback at any phase: the static site is one git revert away, and Vercel keeps instant deployment rollbacks.

## 10. Risks & open items

- **Concurrent design work:** `shared.css` / SKILL.md are actively evolving (v1.2→v1.3 today). Phase 1 starts from whatever the skill ships when implementation begins; the checksum gate then locks them together. Coordinate before starting.
- **`next/font` deviation** needs explicit sign-off (§6).
- **Map weight:** the existing ~60KB simplified-GeoJSON asset carries over unchanged at launch (it feeds the build-time SVG rendering of §5 — the *Leaflet page* is not ported, the *data asset* is); further geometry simplification is a later optimization.
- **Signal `title` coverage:** new field, added today across normalized files; zod makes it required — build will name any file still missing it.
- **Newsletter publish gate** is frontmatter-based (`status: published`, §5) — resilient even though TASK.md commits drafts weekly; the operational note lands in TASK.md with Phase 2.
- **README §4 conflict:** the README still describes the retired "v2 modern register" design (Schibsted Grotesk / Spline Sans Mono); the binding system is the skill's gazette v1.3. The Phase 3 README update reconciles this (the section is already marked historical in session memory, not yet in the file).
