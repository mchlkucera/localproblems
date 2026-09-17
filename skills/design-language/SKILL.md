---
name: design-language
description: Binding design system for localproblems.org, the modern design adopted by the owner on 2026-09-16. Use whenever generating, editing or reviewing ANY page, layout, CSS or HTML for the site (front page, row cards, problem record pages, How it works, category and signals pages, the 404). One font (Inter), a gray ramp, three colours that each mean one thing, quiet motion, native popovers plus one sanctioned hover script. Guards against generic SaaS design. Exact values live in web/app/(site)/DESIGN.md and the page CSS; this file carries the rules and the reasons behind them.
---

# The localproblems.org design language (modern)

**Adopted 2026-09-16 by owner decision.** It replaces the gazette design, which is
archived unchanged at `skills/design-language-gazette-archive/`.

> **Live since the migration of 2026-09-16.** The modern pages are the public routes
> (`/`, `/by-category`, `/problem/…`, `/category/…`, `/signals/…`, `/how-it-works`,
> the 404). The gazette stylesheet `assets/style.css` and its copy `web/shared.css`
> remain only for the private `/sources` admin page; `check-css` still locks the pair.

## Why this file exists

The gazette's risk was fake-editorial slop. **This design's risk is generic-SaaS
slop**: Inter, grays, rounded cards and soft shadows are what every AI-generated
dashboard already looks like. The difference is the same as before: **specificity.**
Every colour, glyph, card and hover here encodes one true thing about the record.
Teal means "in your favour", so it never decorates. A hover card is about *this*
record, so it never gives generic help. If a device encodes nothing, it is slop:
remove it.

The design is decided. Apply it; don't reinterpret it. When plain and fancy are
both options, choose plain.

## Where the exact values live

This skill states the rules. It does not repeat every pixel, because two copies of
a number drift apart.

| What | Source of exact values |
|---|---|
| Front page, top bar, country selector, row card, meter, category icons, motion, the compact signal ledger | `web/app/(site)/DESIGN.md` (owner-approved rule by rule, 2026-09-16) |
| Gray ramp, type scale, 4px grid, radius, popover shadow | `assets/tokens.css` in this skill, copied verbatim to `web/app/(site)/styles/tokens.css` (the `--l-*` tokens) |
| Front-page contrast override, wash insets | `web/app/(site)/styles/front.css` |
| Record page tokens (semantic hues, measure, rail width, section gap), phone rules | `web/app/(site)/styles/problem.css` |
| Figures | `web/lib/figures/` (`index.ts` names each slot and width) and `web/app/(site)/styles/kit.css` |

Change a
value in the CSS and in `DESIGN.md` **together**.

## 1. Principles

1. **Hierarchy comes from size, weight and gray shade.** It never comes from a
   second font or a decorative colour.
2. **Colour encodes, never decorates.** Three hues, each with one meaning (§3).
3. **One field, one meaning, on the page too.** A label, glyph or hue that shows up
   for two different reasons is two devices, so split it.
4. **The page reads fully without JavaScript.** Scripts only add convenience (§9).
5. **Static.** Every page is a pure function of `data/` at build time. Nothing
   depends on the request.
6. **Honest absence.** When data is thin, the page says so in a plain line ("No
   sized figure on file.") or draws nothing. It never shows an empty figure or a
   dangling caption.

## 2. Type

- **One family: Inter** (400 / 500 / 600), self-hosted through `next/font` in the
  root layout (no request to Google from a reader's browser), with `font-feature-settings: "cv11"` on
  the record page. There is no serif and no mono. Figures use
  `font-variant-numeric: tabular-nums` so they line up; they don't switch face.
- **Exactly three text styles on a row card** (owner: *"there's just too many text
  styles, figure out how to simplify"*):
  1. **Title**: 18/26, 500, `--l-text-1` (17/24 on phone).
  2. **Body**: 15/24, 400, `--l-text-2`. The story, the solution and "Good for"
     all use it.
  3. **Meta**: 12px, 400, `--l-text-3`. The labels, "n/12" and the category.
  - No bold inside the story and no darker solution. Emphasis comes from the label
    and its position, never from a fourth style. Citation markers and markdown are
    stripped on the card.
- **Page headings are the only larger sizes:** the front title at 28/600 (26 on
  phone) and the record title at 40/600 (26 on phone), set tight (negative
  tracking). Record prose uses the Body size. Rail and ledger text step down to the
  13px and 12px tokens.
- **Wrapping:** titles use `text-wrap: balance` and body text uses `pretty`, with no
  JS fallback. No title or paragraph may end on a lone word (owner: *"only 'law' is
  being broken to a new line … we need more balanced wrapping"*). Record titles
  over 120 characters switch to `pretty` on phone, because `balance` gives up past
  six lines. Check at 1440 and 375 on real data, for every record title.
- **Dates** read as "4 Sep 2026" (`fmtDate`). Relative distances ("~4 months out")
  are computed against `extractDate()`, **never the wall clock**. Scores read
  `11/12`, not zero-padded.

## 3. Colour

**The gray ramp** (`--l-*` in `tokens.css`) runs from light to dark: backgrounds
`--l-bg` white → `--l-bg-2` → `--l-bg-3` (hover, chip) → `--l-bg-4` (pressed,
empty meter segment); lines `--l-line` (hairline) → `--l-line-2` (control edge);
text `--l-text-4` → `--l-text-3` → `--l-text-2` → `--l-text-1`. The ground is
white. There is no dark mode.

**Contrast:** every gray used for text passes WCAG AA (4.5:1) on the ground it
sits on, including the hover wash. `--l-text-4` is for non-text only (dots, rules,
carets, bars). The front page scopes `--l-text-3` to `#6e7077` for this reason
(`front.css`, audit B13). The record page must do the same before it goes live.

**The semantic hues.** These are the only hues. All are low-saturation, and each has
a graphic tone and a darker ink tone for text:

| Hue | Means | Used for | Never for |
|---|---|---|---|
| **Teal** (`#3f8f7f`, ink `#2e7466`) | **in the builder's favour** | filled opportunity segments, the current rung in a ladder, "Easy" entry, a field nobody here sells (figures) | links, headings, brand, anything neutral |
| **Warm** (amber `#b58a2e` → rust `#d0763f` → brick `#c4564f`) | **friction and time pressure** | entry level Moderate → Hard → Very hard; a deadline under six months (`.ls-soon`) | errors, alerts, emphasis |
| **Ink blue** (`#3d5a96`; pill `#eef1f7` / text `#54607c`) | **a source you can open** | citation pills, source titles in peeks and the drawer, in-prose links | buttons, nav, anything that isn't a source or a link |

A level or deadline shows its hue as a 7px dot plus the word in the ink tone, never
as a filled badge. Category icons are gray (`#919399`).

## 4. Page grid and top bar

- **Front page:** max width 1120px with 32px side padding (20 on phone). Below the
  header come a 232px rail, a 56px gap and the reading column (152/32 at ≤960px;
  one column on phone). Few edges: nothing passes the content box; tabs, band
  labels and category drawings on the page edge; every title and line of copy on
  the text edge; a row's rule and hover wash are one box (owner, 2026-09-17:
  *"simplify the grid"*).
- **Record page:** a full-width head on the main column's left edge, then a 680px main column and a 272px
  rail with an 88px gap. It becomes one column at ≤1080px (rail after main, two
  rail cards side by side) and phone rules apply at ≤640px.
- **Top bar**, 48px, sticky, hairline bottom. It holds the brand, "/", and the
  country selector, then **Problems · Signals · How it works** on the right. The
  label is "How it works", never "About" (owner: *"rename About to How it works"*).
  There is one bar component for every page, and the current link carries
  `aria-current="page"`. The record page keeps its own crumb bar, **Problems /
  P-00xx**.
- **Country selector** (owner: *"a modern dropdown with nice flags"*):
  - The button reads "Czechia" with a solid caret and **no flag**. Flags appear only
    in the menu (owner: *"hide the flag in the currently selected selector, show it
    only in the dropdown"*).
  - The menu is a native `popovertarget` + `popover="auto"`, positioned with CSS
    anchor positioning. It needs no script.
  - Czechia is the one link, marked with a solid tick. Other countries are muted,
    say "Coming soon" and can't be focused.
  - The "Czech" in the front title is the same selector (owner: *"make 'Czech' also a
    selectable thing"*). It's a dotted underline and caret in the heading's own font.
    Its menu sits after the h1, never inside it.
  - Flags are inline SVG, 20×14, in official colours, with a hairline border. They
    are never emoji and never an image request.
  - On phone the button reads "CZ", the three links move behind a menu button (a
    native popover, full-width rows), and the bar fits at 320px.

## 5. Spacing

- 4px grid (`--l-1…--l-8`). Air is part of the design (owner, record head: *"when
  you open up the page, it's too much, we need more negative space"*; row cards:
  *"these cards need more space"*).
- **Row card rhythm:**
  - padding 36 top / 40 bottom (28/32 on phone), with 1px `--l-line` hairlines
    between rows
  - title → story 10 · story → label 14 · text → next label 10 · label → its text 2
    · copy → meta 16 · meter → category 22
- **Front header:** 96 top / 80 bottom (56/72 on phone). The text block is centred
  vertically on the Venn (owner: *"make sure 'Czech problems worth solving' is
  vertically centered with the diagram"*).
- **Record page:** 88px between sections (60 on phone). The head has 72 above and
  104 below.
- **Measure:** copy max 64ch and titles max 640px on cards. Record prose runs to
  the 680px column. Keep ≥50px clear of the category drawing at desktop.
- No horizontal page scroll at 375px or 320px. Wide figures scroll inside their own
  container.

## 6. The front page and the row card

- **Header:** "Czech problems worth solving" plus **one** plain sentence. No counts
  line and no stats. The Venn sits on the right: three monoline circles with labels
  inside the box. Every part of it has a plain-language hover, focus and tap card
  that says what the register looks *for*, never a promise that every problem meets
  all three (owner: *"… non-technical simple language"*).
- **Tabs:** "By opportunity" and "By category", with no "Group by" label (owner:
  *"remove 'Group by'"*). They start at the page edge (owner: *"line up 'By
  opportunity' to the leftmost column"*). They are plain links. There is no
  deadline grouping (owner: *"Remove deadline sort"*). **Each grouping is its own
  static path, never a query string** (§9).
- **Grouping rail:** a label and "N problems". Opportunity bands appear as numbers
  only ("Opportunity 10–12", "8–9", "5–7", "0–4"), never verdict words. The rail is
  sticky under the sticky tabs. On phone it becomes a one-line sticky strip.
- **By category is an index first**, at every width: one closed native `<details>`
  per category (drawing, name, "N problems"). Opening one
  lists its rows, which drop their own category item and drawing.
- **On phone (≤720px) a row is folded:** title, a two-line peek of its first
  paragraph, and the meta line ending in "Show more". The fold is a CSS
  checkbox and label, never a script, and every word stays in the HTML. Above 720px
  rows are always open (owner, 2026-09-17: *"just heading, small peek, and toggle
  to expand"*).
- **Row card anatomy, in this order:**
  1. Title, the one link.
  2. Story (`brief`), one plain paragraph. Omitted when absent.
  3. **Suggested** label, then the solution.
  4. **Good for** label, then the text. Omitted when absent.
  5. Meta line: opportunity meter, then category.
  - A row without the new copy is the same card with only "Suggested". It is never a
    different design. Copy rules for these fields are in
    `data/RECORD-TEMPLATE.md`, "The headline block".
- **Labels sit on their own line.** A label is never inline with its text:
  "Suggested Build a small…" must never read as one run (owner: *"Suggested and Good
  for shouldn't mix with the text on the right"*). No colons, no bullets.
- **One left content edge.** Title, story, labels, texts and meter all start on the
  title's left edge. There is no label column and no indent (owner: *"can we align
  the scoring with the right col"*, resolved by removing the column). There are no
  bullet glyphs either (owner: *"the visual with the bullets is very messy right
  now, they're overflowing"*).
- **Opportunity meter:**
  - 12 segments at 4×8px, filled teal up to the score, empty `--l-bg-4`. Then "n/12"
    in meta, with "Opportunity" as screen-reader text (owner: *"make the opportunity
    meter somehow visible"*).
  - It leads the meta line, so meters line up down the page.
  - Its hover, focus and tap card is **specific to this record**: "Opportunity n of
    12", then the five checks with their mini bars, scores and plain read lines,
    most-filled first (owner: *"on hover show specific information, not
    generic"*).
- **Category icons** are **solid**, never outlined:
  - one 14px icon per category, on a 16-unit grid, `fill: currentColor`, even-odd,
    no strokes, colour `#919399` (owner: *"add relevant icons instead of just
    boxes"* → *"choose solid icons instead of outlined ones"* → *"make them a tiny
    bit grayer"*)
  - the telling detail is always negative space ≥1px, and ink density is balanced
    across the set
  - every small UI glyph is solid too (caret, tick). The large category drawings
    stay line illustrations.
  - icon plus label, plain, with no hover card (owner: *"remove the category hover,
    doesn't add value"*). No deadline item on the row (owner: *"remove the deadline
    info"*).
- **The whole row is one target:**
  - The title link stretches over the row. Hover or focus anywhere washes the row
    `#f6f6f8` (radius 8) and underlines the title (owner: *"make the whole page
    hoverable"*).
  - The wash reaches 28px left of the text and to the content edge on the right,
    never over the hairlines, and the rule above a row is the same width (owner:
    *"the grey of the card should reach more to the left"*).
  - The meter sits above the stretched link so it takes its own pointer. The keyboard
    tabs from title to title.

## 7. The record page

**Head: one left edge, with air** (owner, 2026-09-16: the centred head "got all over
the place"; *"make it all left"*). The category drawing (216px, very light gray;
120px on phone), the title, the headline copy (`brief`, `good_for`) and the fact row
all start on the main column's left edge, at every width. The **fact row**: Category · Locality · Window ·
Entry · Verified. Each fact appears once, with a small label over its value and
hairline dividers between facts. Window shows only when there is no `brief`, because
a brief already says why it is urgent. The Entry value is the level dot and word, and
it links to `#difficulty-to-enter`.

**Sections, in the builder's order:** The problem (+ ProcessToday figure) →
**Suggested solution** box (`--l-bg-2`, hairline, radius 12, + ProcessAfter figure)
→ Proven abroad → Local competition → Who pays → Why now → Difficulty to enter →
First moves. Every section reads **prose first, then its ledger**.

**Company rows** (comps and locals):
- Each row has the name ↗ (another site), a maturity tag, meta ("Germany · since
  2019", "IČO …"), its **source pills**, then one clamped line of what it sells.
  "Details" opens a native popover modal for the rest.
- Every company names the sources that back it, or says **"No source on file"**,
  never nothing (owner: *"isn't it connected to sources? … why isn't it
  mentioned?"*).
- Locals group into "Sells this" and "Nearby".

**Receipts** (prices, public money, dates on file): figure, one line, meta, pill at
the row end. "Public money nearby" folds in a native `<details>`.

**Difficulty to enter is three lines** (owner: *"difficulty to enter is needlessly
complex now"*, then *"typographically consistent"*):
1. The **level**: a 22px/600 word with its hue dot (Easy · Moderate · Hard · Very
   hard).
2. **One sentence** naming the gates that set it (only the top-weight gates; an easy
   record names its open gates).
3. **One quiet line**: "Already here: … That counts under Local competition, not in
   this level."

Lines 2 and 3 share one voice (same size, weight and leading); line 3 is one gray
lighter. The level is never re-derived on the page: the record carries it and
`check-records.py` asserts it.

**Figures** come from the kit:
- ProcessToday, ProcessAfter, CompMap, FieldTimeline and MoneyScale go in the main
  column. FieldGrid is not on the record page (owner, 2026-09-16: *"remove the Who
  is here from the right sidebar"*).
- Each is a server function that returns `null` when its data is thin, so **call it
  before the JSX and test it** before drawing anything around it.
- A figure belongs to the section it explains. It gets air and nothing else: it's
  never boxed and never captioned twice. In the rail it takes the rail's card.

**The rail** (sticky under the bar; after main at ≤1080px):
- **Opportunity card**, "Opportunity **n**/12":
  - Five rows: label, segment bars (teal), n/max. **Sorted most-filled first, then
    the longer bar (higher max), then the fixed order.** Never sort by ratio (owner:
    *"longer bars are first"*).
  - A zero row is muted. Each row links to the section with its evidence.
- **Ladder tooltips** on each row and on the total (owner: *"expand on the tooltips
  in the scoring"*):
  - what the check asks, why it matters to a builder, and the SCORING.md rungs in
    plain words, with this record's rung highlighted (teal number)
  - then "This record: … n of max."
  - the total's tip shows the four bands by number range. **No verdict words
    anywhere.**
  - these tips are CSS only (hover or keyboard focus, short delay) and must not
    change wording from SCORING.md: restate the rungs, add nothing
- **Evidence card:** source count, a mix of source types as small gray bars (each
  with a plain note), and "View all N sources →", which opens the sources drawer.

**Sources: pills plus peek cards.** This is the record page's signature.
- **At rest:** a quiet ink-blue pill in the sentence with the publisher's short name
  ("NÚKIB"). A run collapses to the first name plus "+2", and the pill is glued to
  the word before it.
- **On peek:** a card anchored under the pill. It shows the monogram, publisher,
  domain and date; **the source title is the link** ("Title ↗"); then one plain line
  on why it backs the claim; then the source's own words when ingest captured them
  (owner: *"just like you can click 'Lexnova Energy', you should be able to click
  'Act No. 264/2025 Coll.'"*).
- **Native first.** The pill is a `<button popovertarget>` and the card is a
  `popover="auto"`. Click, tap or Enter opens it; Escape and an outside click close
  it. The hover script (§9) only adds hover-intent, focus-to-open and click-to-pin.
- **↗ means another site, everywhere, and nowhere else.** Every link that leaves the
  site ends in ↗ plus screen-reader text "(another site)". An in-page link never
  carries it.
- The **drawer** is a right-side popover listing every source, grouped by type. Each
  entry has publisher · host · date, the title ↗, why, a "In the source's words"
  fold, and "Cited in …".

**Phone (≤640px)** (owner: *"simple rows: left label, right value"*):
- The head stays on the left edge. The art shrinks to 120px and the title to 26px.
- The fact row becomes full-width rows on hairlines, label left and value right.
- A peek card becomes a **bottom sheet** with a grab handle, and so do the Details
  modals. The drawer goes full width.
- The rail is one column after main, and receipts stack figure over line with the
  pill on the right.

## 8. Motion and hover

- **Only `opacity` and `transform` animate.** Never width, height, position, margin
  or colour-through-transparent.
- **Never transition to or from `transparent`.** Some browsers interpolate through
  black (owner: *"flashing through black on hover"*). A wash is always painted, and
  only its opacity fades. A hover otherwise changes one thing: an opacity, or one
  gray to another gray.
- **Entrance:** tooltips, peeks and menus fade in with a 3px rise, about 140ms
  ease-out. **Exit is instant.** The sources drawer slides 24px at 180ms.
- **`prefers-reduced-motion: reduce`:** opacity fade only, no movement (or no
  transition at all).
- Menus and country hovers change instantly, with no fade.
- Focus is always visible: a 2px gray outline (`--l-text-1` or `--l-text-2`) at a
  1–2px offset. Hover and focus look different.

## 9. JavaScript, popovers, static pages

Owner decision, 2026-09-16: client JavaScript is allowed **for the named progressive
enhancements below, and nothing else**. SPEC §5 and §7 carry the same list.

1. **The source-peek hover script** (`PeekHover`, a `"use client"` component with one
   document-level listener set and no per-pill hydration): hover-intent (~140ms)
   opens a peek, the card stays open while the pointer is inside it, Tab onto a pill
   opens it, and a click pins it.
2. **Native popovers and CSS**, which aren't scripts but are sanctioned devices:
   `popovertarget` peeks, Details modals, the sources drawer, the country menu, CSS
   hover/focus tooltips, and `<details>` folds.
3. The gazette-era relative-dates and table-sort scripts stay only while their
   gazette routes exist, and go with them.

Rules for all of it:
- **The page reads fully with every `<script>` stripped.** All text renders, and
  every popover opens on click, tap or Enter. Nothing is reachable only by hover.
- **Pages stay static:** `generateStaticParams` + `dynamicParams = false`. **No
  `searchParams`, `cookies()` or `headers()`** anywhere under `web/app`. Reading
  `searchParams` makes the route dynamic, and a Vercel function has no `data/`, so
  it 500s. A second view is a second static path (`/by-category`), never `?group=`.
- **No wall clock:** relative dates use `extractDate()`.
- Any other client component needs explicit owner sign-off first (SPEC §10
  tripwire).

## 10. The anti-slop NEVER list

1. NEVER a second font family, and never a mono or serif face for figures or data.
2. NEVER a hue that doesn't encode one of the three meanings in §3. No brand accent,
   purple, gradient, glow or coloured shadow.
3. NEVER a fourth text style on a row card, and never bold inside the story.
4. NEVER a label inline with its text, and never colons or bullet glyphs on a card.
5. NEVER a generic tooltip. Every hover card says something about *this* record, or
   it isn't there.
6. NEVER content reachable only by hover or only with JS.
7. NEVER `searchParams`, `cookies()`, `headers()` or any request-time data.
8. NEVER transition from or to `transparent`, never animate a layout property, never
   an exit animation, never ignore reduced-motion.
9. NEVER emoji, flag emoji, or an outlined stock icon set. Small glyphs are solid and
   drawn for this site. Category drawings are line illustrations.
10. NEVER marketing chrome: no hero stats, counts line, "trusted by", badges, CTA
    buttons or exclamation marks. "Problem" is never softened to "challenge".
11. NEVER a verdict word (PRIME, STRONG, …) on a public page. Bands are number ranges
    with plain words.
12. NEVER ↗ on an in-page link, and never an external link without ↗.
13. NEVER an empty figure, a boxed figure, or a caption stated twice. Thin data draws
    nothing or states the absence.
14. NEVER a title or paragraph ending on a lone word, and never horizontal page
    scroll at 320–375px.
15. NEVER a text gray under 4.5:1 on its ground. `--l-text-4` is for non-text only.
16. NEVER restate SCORING.md or CONVENTIONS.md vocabulary in different words, and
    never add a rung, band or gate the rubric doesn't have.
17. NEVER edit `assets/style.css` or `web/shared.css`. They are the frozen gazette
    stylesheet, kept only for the private `/sources` page.

## 11. Not yet ruled: settle these in the migration

These gaps are known from the 2026-09-16 audit. They aren't rules yet, so don't
invent answers in a content run; the migration checklist owns them. Other sessions
were already closing some of them the same day (anchor aliases, metadata), so
**check the code before acting on an item**. When one is settled, move its answer
into the sections above and delete the bullet.

- **Print:** the modern CSS has no `@media print`, and a printed record carries no
  sources (audit B12). Whether "photocopies beautifully" survives is an open owner
  question.
- **Record head vs row card:** the record head renders `brief` and `good_for` as
  dotted bullets with an inline "Good for:" label. The row card rule (labels on their
  own line, no colons, no bullets) doesn't hold there yet.
- **Record page contrast:** `problem.css` doesn't yet scope `--l-text-3` the way
  `front.css` does (audit B13). Keyboard: tabbing onto a pill opens its card, and the
  rail comes after main in DOM order.
- **Hover rows in the rail** (`.ls-dim`, `.ls-mixrow`) transition `background-color`
  from an unpainted state, which conflicts with §8.
- **Record content cuts** (audit D9): `entry.why`, the gates list, the comps ledger
  links, the whenline, past urgency receipts, the corrections link.

## 12. Implementation

- **Modern CSS:** `assets/tokens.css` (the `--l-*` tokens), copied verbatim to
  `web/app/(site)/styles/tokens.css` and locked by `web/scripts/check-css.mjs`:
  edit the asset, then copy it. The per-page sheets in `web/app/(site)/styles/`
  (`front.css`, `problem.css`, `signals.css`, `category.css`, `how-it-works.css`,
  `not-found.css`, `kit.css`) are not locked; their rules live here and in
  `web/app/(site)/DESIGN.md`. Selectors are prefixed per page (`lf-`, `ls-`,
  `lg-`, `lc-`, `lh-`, `lk-`, `lnf-`).
- **Static contract:** `web/scripts/check-site.mjs` fails the build on
  `searchParams`/`cookies(`/`headers(`, a `"use client"` outside its allow-list,
  `href="/lab/`, a rejected record's page, and a record page without `id="sN"`.
- **Gazette CSS:** `assets/style.css` = `web/shared.css`, locked by
  `web/scripts/check-css.mjs`. It stays while the private `/sources` page uses it.
- **Verify every page change** with screenshots at 1440 and 375 on real data (both
  groupings, several records, one long title), with scripts stripped once, and
  against the NEVER list.
