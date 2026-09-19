---
name: design-language
description: Binding design system for localproblems.org, the modern design adopted by the owner on 2026-09-16. Use whenever generating, editing or reviewing ANY page, layout, CSS or HTML for the site (front page, row cards, problem record pages, How it works, category and signals pages, the 404). One font (Inter), a gray ramp, three colours that each mean one thing (plus one owner-approved score scale), quiet motion, native popovers plus one sanctioned hover script. Guards against generic SaaS design. Exact values live in web/app/(site)/DESIGN.md and the page CSS; this file carries the rules and the reasons behind them.
---

# The localproblems.org design language (modern)

**Adopted 2026-09-16 by owner decision.** It replaces the gazette design, which is
archived unchanged at `skills/design-language-gazette-archive/`.

> **Live since the migration of 2026-09-16.** The modern pages are the public routes
> (`/`, `/by-category`, `/problem/…`, `/category/…`, `/signals/…`, `/how-it-works`,
> the 404) and the private `/sources` admin page, the last to move (2026-09-17). No
> gazette stylesheet remains; the archive holds its only copy.

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
| Record page: crumb bar, head, sections, sheets, scores, rail, figures, drawer (owner-approved on p-0008, 2026-09-16/17) | `web/app/(site)/DESIGN.md` "Record page" sections |
| Record page tokens (semantic hues, score tones, measure, rail width, section gap), phone and print rules | `web/app/(site)/styles/problem.css` |
| Figures | `web/lib/figures/` (`index.ts` names each slot and width) and `web/app/(site)/styles/kit.css` |
| Score mapping and judgement words (§7; SCORING.md "PRESENTATION") | `web/lib/site/score-proto.ts` |

Change a
value in the CSS and in `DESIGN.md` **together**.

## 1. Principles

1. **Hierarchy comes from size, weight and gray shade.** It never comes from a
   second font or a decorative colour.
2. **Colour encodes, never decorates.** Three hues, each with one meaning, plus
   the score scale, which reuses their tones for one more meaning (§3).
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
- **A record section has four levels and no more:** heading (20/600) → answer line
  (17/26, 500, `--l-text-1`) → body and lists (15/24) → meta (12–13, `--l-text-3`).
  A section sheet adds only its presenting heading (30/600) and a larger lede.
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
(`front.css`, audit B13). The record page does the same (`problem.css`, `.lab.ls`).

**The semantic hues.** These are the only hues. All are low-saturation, and each has
a graphic tone and a darker ink tone for text:

| Hue | Means | Used for | Never for |
|---|---|---|---|
| **Teal** (`#3f8f7f`, ink `#2e7466`) | **in the builder's favour** | filled opportunity segments, the current rung in a ladder, "Easy" entry, the open quadrant of the Market gap matrix ("The space is still open"), the columns and dots of money already being paid, the process band the solution changes | links, headings, brand, anything neutral |
| **Warm** (amber `#b58a2e` → rust `#d0763f` → brick `#c4564f`) | **friction and time pressure** | entry level Moderate → Hard → Very hard; a deadline under six months (`.ls-soon`) | errors, alerts, emphasis |
| **Ink blue** (`#3d5a96`; pill `#eef1f7` / text `#54607c`) | **a source you can open** | citation pills, source titles in peeks and the drawer, in-prose links | buttons, nav, anything that isn't a source or a link |

A level or deadline shows its hue as a 7px dot plus the word in the ink tone, never
as a filled badge. Category icons are gray (`#919399`).

**The score scale: an owner-approved exception** (2026-09-17: a green, amber and red
scale, then *"make the badge colors more subtle"*). A record section's score has a tone.
It is the one place a hue means "how this score stands" instead of the three
meanings above:

| Tone | When (`scoreTone` in `page.tsx`) | Value (`--ls-score-*`) |
|---|---|---|
| **Good** (teal) | full marks, n = max | `#3f8f7f` |
| **Mid** (amber) | half or more, n/max ≥ 0.5 | `#b58a2e` |
| **Bad** (brick) | under half, 0 included | `#c4564f` |

Why it is allowed: a reader should see at a glance which sections are strong, and
the scale adds no new colour. It reuses the teal and warm tones, and it keeps close
to their meanings (full marks are in the builder's favour; a weak score is
friction). Limits: it appears **only** as a score dot (8px in the contents, 7px in a
badge) and as a badge's 7% tint behind gray text. Never as text colour, never on a
fill larger than a dot, and never outside a score.

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
  Czechia / P-00xx** (§7).
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
- **Record page:** 120px between sections (72 on phone), split evenly around the
  hairline above each heading (owner: *"more space between sections"*). The head
  has 48 above (with the drawing) and 104 below.
- **Measure:** copy max 64ch and titles max 640px on cards. Record prose runs to
  the 680px column; answer lines stop at 62ch. Keep ≥50px clear of the category
  drawing on a front-page card at desktop.
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
  - Its hover, focus and tap card is **specific to this problem**: "Opportunity n of
    12", then the record page's five scored sections in page order, each with its
    score dot (§3 scale), name, judgement word, n/max and one-line reason; Execution
    difficulty sits apart, "Not added to the total" (owner: *"on hover show specific
    information, not generic"*; *"make sure the scoring changes are written to
    mainpage as well"*).
  - An open card's row rises above every row and every later group header, so a card
    held open by focus or tap is never covered (owner: *"overlap problems on
    mainpage"*).
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

Owner-approved on p-0008 (2026-09-16/17), live at `/problem/cz/p-0008`. The brief:
no complex language, walls of text or facts said twice, and **scannability first**.
Someone who reads only the headings and answer lines still gets the story. Exact
values are in `DESIGN.md`, "Record page".

**Head: one left edge, a small drawing, the facts beside it.**
- Everything starts on the main column's left edge, at every width (owner: the
  centred first section *"got all over the place"*).
- A **small category drawing**, 128px (96 on phone), very light gray. It stays because
  *"without it the page at top would be just plain"*. It stays small because it only
  says "category".
- **No category colour fade** (owner: *"Remove the color"*). A category isn't one of
  the meanings in §3.
- Title, then the headline copy under the front card's rules: `brief` as a plain
  paragraph, "Good for" as a meta label on its own line, the "Draft law" badge where
  a label would stand.
- **Facts column** in the rail's column, level with the brief's first line: Category
  · Entry · Verified, label left and value right, on hairlines. Each fact once. There
  is no Locality (every record is national, and the crumb says Czechia) and no Window
  (Why now holds the dates). Entry is the level dot and word, and it links to
  `#execution-difficulty`.
- **Crumb bar:** "Problems / Czechia / P-xxxx". It is solid white and stacks above the
  sticky rail, so the rail never shows through it at the page end.

**Sections, in the builder's order**, one question each: The opportunity ·
Suggested solution · Why now · Willing to pay · Validated abroad · Market gap ·
Execution difficulty · Suggested first moves.
- "Who already sells this" is split (owner: *"separate abroad and in Czechia"*):
  **Validated abroad** carries the map and **Market gap** the matrix. A company has
  one home.
- **A hairline above every section heading** (owner: *"a line before each heading
  clearly separating the sections"*), with the section gap split around it. Suggested
  solution stays a subtle box whose edge is its line, and it has a **real h2** like
  every other section (owner: *"could use a bigger heading"*).
- **Old anchors stay as aliases**, so deep links still land (`#problem`, `#who-pays`,
  `#how-big`, `#proven-abroad`, `#local-competition`, `#difficulty-to-enter` and the
  rest; the list is in DESIGN.md).

**The page is the outline, and the sheet is the section** (owner: *"make the without
modal really short and scannable, all detail goes in the modal which is
in-depth"*).
- On the page a section is: heading → **answer line** (one sentence) → **at most 3
  items or one figure** → **Read more**. The cap lives in page code. The data is
  never trimmed.
- **Read more** is an outlined button, never a filled CTA. It opens a **sheet**, a
  paper-like native `popover="auto"` dialog (owner: *"read more into paper like modal
  with heading that presents"*). The sheet has a meta line with the ID and title, a
  large section heading, and the answer as its lede. A section with nothing beyond
  its outline gets no button.
- The sheet opens with a muted **About this section** panel in one column: *What
  this shows · Why it matters to a builder · How to read the score* (the last only
  on scored sections). The words are the same on every problem. They restate the
  rubric's rungs and add none.
- Then everything, in depth. **Sub-groups get real h3 headings**, never meta labels
  (owner: *"CLEARLY with bigger heading separate"*). **Nothing is listed twice**
  (owner: *"listed two times"*). The Validated abroad sheet shows its map without the
  company list, because the company rows follow it.
- No URL opens a sheet, because a closed popover can't open from a fragment without a
  script. On paper every sheet prints in place under its outline.

**Scores.** The section scores come from `lib/site/score-proto.ts`, which reads the
rubric onto the sections with the names and words in SCORING.md "PRESENTATION"
(owner, 2026-09-19). A record not yet rescored to the 2026-09-19 money and urgency
ladders (`lib/scoring-v2.ts`) shows those two with their old words until it is.
- **Points stay visible** as n/max, never "out of 10". Each score has a **reasonable
  judgement word**, never a verdict: "Clear, recurring pain", "Firm deadline",
  "Some signs", "Early rivals only", "Proven in 2+ markets".
- Each scored heading carries a **badge beside the title** (owner: *"try putting the
  badges next to the heading"*). The badge is a faint tint, gray "n/max · word" text
  and a dot in the score's tone (§3). It is a sibling of the h2, so it stays out of
  the heading's name, and it wraps under the title when the line is too narrow.
- **The total stays the rubric score /12**, so the record page and the front page
  never disagree. **Execution difficulty** (easier = more points, /3) is shown beside
  the total, in the contents, and is **never summed** into it. Every summed row reads
  more = better, which is why the local-competition section is **Market gap** (a full
  bar is an open field); its anchor stays `#competition`.

**The rail: contents and evidence** (sticky under the bar; after main at ≤1080px).
- **Contents card**, "Opportunity n/12": every section in page order, with a **thin
  stepper line and one dot per section** (owner: *"something cleaner like dots or a
  line"*). The section in view fills its dot dark, and sections already read keep a
  gray dot. CSS scroll-driven animations drive it, with **no JS**. Where they are
  unsupported every dot stays hollow.
- **Every row is one height**, with its content vertically centred. A scored row
  shows its word under the label and a **coloured score dot** (owner: *"lets use
  dots instead of the circles"*). **n/max appears only on hover or focus**, and it
  stays in the DOM for screen readers.
- Scored rows keep their ladder tooltips: what the check asks, why it matters, the
  rungs with this problem's rung highlighted, then "This problem: … n of max." They
  restate the rungs, add nothing, and use no verdict words.
- **"Who is here" isn't in the rail** (owner: *"remove the Who is here from the
  right sidebar"*).
- **Evidence card:** the source count, one row per source type as a small gray bar
  with a plain note, and "View all N sources →". **A type row opens the sources
  drawer scrolled to its group** (through the sanctioned script, §9; without JS the
  drawer opens at the top). **Drawer group headings are sticky** (owner: *"make sure
  headings are sticky"*).
- On phone a compact score list follows the facts, with n/max visible because a
  phone has no hover. The full contents card follows main.

**Figures: "use interaction to simplify, not decoration"** (owner).
- **Simple dots or columns.** Detail opens in a peek card on hover, focus or tap. **No
  captions, no legends, no explanatory paragraphs, less text** (owner: *"make the
  diagram clearly self explanatory, less text!"*). The axes and the marks carry the
  meaning.
- **LocalMatrix** (Market gap) is a 2×2: Early / Established across, Sells something
  nearby / Sells this up. Each Czech player is one dot (hollow early, filled
  established), and a dot's position inside its quadrant means nothing. It is **dots
  only**, drawn taller. The only words inside it are **"The space is still open"**, in
  teal, in the empty established-and-sells-this quadrant.
- **CompMap** (Validated abroad) is a **shorter map beside a numbered company list**.
  A company that sells in several countries shows **all its markets** (home darker,
  other markets lighter), and pointing at its dot or its row **highlights them
  together**, instantly. In the sheet the map runs **full width without its list**,
  and the company rows sit under it.
- **PayDots** (Willing to pay): **teal columns, one per real price or purchase**, on
  a log CZK scale, with a **buyer word under each**. Monthly and other recurring
  prices form a **separate, lighter group**, so they never read as something to add
  to the purchases. Nothing is summed. **PayTimeline** (purchases stacked by month,
  open grant calls last) appears only in the Willing to pay sheet.
- **ProcessSteps** (Suggested solution) is **the hub** (owner, 2026-09-18: *"The
  hub is good"*; *"imagine this person has to interact here, this there, this there
  vs how they interact with one provider"*). Two blocks, stacked at every width,
  each heading telling its half of the story ("**Today** · each person works
  separately, in their own place"; "**With the suggested solution** · everyone works
  in one system"). Today each person is **wired to their own place**, named in the
  step's own words; after, everyone is **wired by one bracket into ONE teal box**,
  named from the record's words ("Hospital system with report templates"), which
  also lists what the system now does itself. When the solution is a provider, the
  buyer is the hub: one wire per seller today, one wire to one provider after.
  **The wires are one grid**: ticks start at one x, the bracket runs exactly from the
  first tick to the last, the join leaves it at the box's centre (equal rows). An
  unknown actor is **never drawn as a person**: each open question is one plain
  "Not known: …" line under the figure. Only work nobody does today is a dashed
  "Nobody does this today" box. Glyphs are gray, teal only in the one box.
- A figure **rendered twice** (page and sheet) takes a **`scope`**, so popover ids
  stay unique.
- Each figure is a server function that returns `null` when its data is thin. **Call
  it before the JSX and test it** before drawing anything around it. A figure gets
  air, never a box.

**Execution difficulty.** The page shows two short lists, **Makes it easier** and
**Makes it harder** (owner: *"which is making it easier and which harder"*). The
level word is already in the badge. The sheet adds the level (a large word with its
hue dot), the problem's own reason, the same lists in whole sentences, and one line:
competition doesn't change this level. The warm hue is the level dot only. The level
is never re-derived on the page: the record carries it and `check-records.py`
asserts it.

**Company rows** (in the sheets): name ↗, maturity dot, meta ("Germany · since
2019", "IČO …"), and one line of what it sells. Every company names the sources that
back it or says **"No source on file"** (owner: *"isn't it connected to sources? …
why isn't it mentioned?"*). Czech rows group under the h3s "Sells this" and "Sells
something nearby".

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
  it. The hover script (§9) only adds hover-intent and click-to-pin.
- **↗ means another site, everywhere, and nowhere else.** Every link that leaves the
  site ends in ↗ plus screen-reader text "(another site)". An in-page link never
  carries it.
- The **drawer** is a right-side popover listing every source, grouped by type under
  sticky headings. Each entry has publisher · host · date, the title ↗, why, an "In
  the source's words" fold, and "Cited in …". `#sources` and `#sN` open it on that
  row.

**Reader-facing copy never says "record"** (owner). Readers see a *problem*: "This
problem: 2 of 3.", "Found by the register's market check". "Record" is the
register's internal word, for code and rulebooks only.

**Phone (≤640px)** (owner: *"simple rows: left label, right value"*):
- The head stays on the left edge. The drawing shrinks to 96px and the title to 26px.
- The facts become full-width rows on hairlines, label left and value right, followed
  by the score list.
- Peek cards, sheets and the drawer take the full width. Peeks and sheets become
  **bottom sheets** with a grab handle.
- The easier and harder lists stack. The rail follows main in one column.

**Print:** no bar, buttons or tooltips. Every sheet prints in place, and the drawer
prints as the source list.

## 8. Motion and hover

- **Only `opacity` and `transform` animate.** Never width, height, position, margin
  or colour-through-transparent.
- **Never transition to or from `transparent`.** Some browsers interpolate through
  black (owner: *"flashing through black on hover"*). A wash is always painted, and
  only its opacity fades. A hover otherwise changes one thing: an opacity, or one
  gray to another gray.
- **Entrance:** tooltips, peeks, section sheets and menus fade in with a 3px rise,
  about 140ms ease-out. **Exit is instant.** The sources drawer slides 24px at 180ms.
- **Scroll-driven, not timed:** the contents stepper and a sheet's compact bar title
  follow scroll position through CSS scroll-driven animations. They still change
  only opacity and transform (and a label's gray), and where the browser lacks
  support they simply stay at rest.
- **`prefers-reduced-motion: reduce`:** opacity fade only, no movement (or no
  transition at all).
- Menus and country hovers change instantly, with no fade.
- Focus is always visible: a 2px gray outline (`--l-text-1` or `--l-text-2`) at a
  1–2px offset. Hover and focus look different.

## 9. JavaScript, popovers, static pages

**Client scripts are small islands** (owner decision, 2026-09-18, widening the
2026-09-16 rule that allowed only the hover script). An island is allowed when it
clearly improves comprehension, and on these terms:
- **Never for content.** An island adds no word, row or figure to the page. It only
  shows, hides, focuses or opens what the server HTML already holds, and it changes
  counts only so that they stay true to what is showing.
- **The page reads fully with scripts off** (the rules below). A control that only
  an island can make work is hidden by CSS until scripts run
  (`@media (scripting: enabled)`), never by a class the script adds.
- **Small, with no dependency:** one `"use client"` component that renders nothing
  and sets one listener set in an effect. It first touches the DOM after hydration,
  so the server HTML and the hydrated tree never disagree.
- **Each island is named on the allow-list with its job**: `ISLANDS` in
  `web/scripts/check-site.mjs`, which fails the build on any other `"use client"`,
  on an entry whose file is gone, and on an entry with no job. A new island needs
  the owner's sign-off and an entry there.

The islands and devices in use today:

1. **The source-peek hover script** (`PeekHover`, a `"use client"` component with one
   document-level listener set and no per-pill hydration). Hover-intent (~140ms)
   opens a peek, the card stays open while the pointer is inside it, and a click pins
   it. Focus alone opens nothing (audit B13). Escape hides a showing rail tooltip. A
   `#sources` or `#sN` URL opens the drawer on that row, and an Evidence type row
   opens the drawer scrolled to its group.
2. **Native popovers and CSS**, which aren't scripts but are sanctioned devices:
   `popovertarget` peeks and figure dots, section sheets, the sources drawer, the
   country menu, CSS hover/focus tooltips, `<details>` folds, and scroll-driven
   animations (the contents stepper).

Rules for all of it:
- **The page reads fully with every `<script>` stripped.** All text renders, and
  every popover opens on click, tap or Enter. Nothing is reachable only by hover.
- **Pages stay static:** `generateStaticParams` + `dynamicParams = false`. **No
  `searchParams`, `cookies()` or `headers()`** anywhere under `web/app`. Reading
  `searchParams` makes the route dynamic, and a Vercel function has no `data/`, so
  it 500s. A second view is a second static path (`/by-category`), never `?group=`.
- **No wall clock:** relative dates use `extractDate()`.
- Any other island needs explicit owner sign-off first (SPEC §10 tripwire). The
  front-page search (option B plus `/`) was built as one and then cancelled by the
  owner on 2026-09-19; it is parked in `docs/mockups/front-search/`, not installed.

## 10. The anti-slop NEVER list

1. NEVER a second font family, and never a mono or serif face for figures or data.
2. NEVER a hue that doesn't encode one of the three meanings in §3. The one
   exception is the score scale (teal `#3f8f7f` at full marks, amber `#b58a2e` at
   half or more, brick `#c4564f` below half), and only as a score dot or a badge's
   7% tint. No brand accent, purple, gradient, glow, coloured shadow, or category
   colour fade.
3. NEVER a fourth text style on a row card, and never bold inside the story.
4. NEVER a label inline with its text, and never colons or bullet glyphs on a card.
5. NEVER a generic tooltip. Every hover card says something about *this* record, or
   it isn't there.
6. NEVER content reachable only by hover or only with JS.
7. NEVER `searchParams`, `cookies()`, `headers()` or any request-time data.
8. NEVER transition from or to `transparent`, never animate a layout property, never
   an exit animation, never ignore reduced-motion.
9. NEVER emoji, flag emoji, or a stock icon set (outlined or not). Small glyphs are
   solid and drawn for this site: the category icons and the process figure's role
   and object glyphs (`web/lib/figures/role-icons.tsx`, one bust plus one detail,
   on the category icons' 16-unit grid). Category drawings are line illustrations.
10. NEVER marketing chrome: no hero stats, counts line, "trusted by" or award
    badges, filled CTA buttons or exclamation marks. "Problem" is never softened to "challenge".
11. NEVER a verdict word (PRIME, STRONG, …) on a public page. Bands are number ranges
    with plain words.
12. NEVER ↗ on an in-page link, and never an external link without ↗.
13. NEVER an empty figure, a boxed figure, a caption, a legend or an explanatory
    paragraph under a figure. Thin data draws nothing or states the absence.
14. NEVER a title or paragraph ending on a lone word, and never horizontal page
    scroll at 320–375px.
15. NEVER a text gray under 4.5:1 on its ground. `--l-text-4` is for non-text only.
16. NEVER restate SCORING.md or CONVENTIONS.md vocabulary in different words, and
    never add a rung, band or gate the rubric doesn't have.
17. NEVER bring back gazette CSS, fonts or chrome. The retired design lives only in
    `skills/design-language-gazette-archive/`, as history.
18. NEVER "record" in reader-facing copy. Readers see a problem.
19. NEVER more than three items, or one figure, under a section's answer line on
    the page. NEVER the same company, fact or list twice in one sheet.
20. NEVER sum Execution difficulty into the total, and never show a record-page
    total that differs from the front page's /12.

## 11. Not yet ruled

These are known open questions. They aren't rules yet, so don't invent answers in a
content or page run. **Check the code and the named docs before acting on an item.**
When one is settled, move its answer into the sections above and delete the bullet.

- **Scoring v2, the rescore.** The owner settled the rungs on 2026-09-19 (SCORING.md):
  Why now without freshness, Willing to pay read from price receipts, Market gap,
  Execution difficulty outside the total, the total still /12 with its bands. The
  records are rescored one by one (`docs/scoring-v2/rescore-2026-09-19.md`); until
  the last joins `lib/scoring-v2.ts`, the page keeps a v1 branch for Why now and
  Willing to pay. When it does, delete the branch and recheck the score scale's
  thresholds in §3 against the new distribution.
- **The other records.** The p-0008 design renders on every record, but only p-0008
  is written for it. The writing rules for answer lines, keyed lists, first moves and
  in-page links, and the `check-records.py` invariants that enforce them, are being
  codified in `data/RECORD-TEMPLATE.md`, `pipeline/REWRITE.md` and
  `scripts/check-records.py` now. Until each record is rewritten, its outline is
  whatever its current prose yields.

## 12. Implementation

- **Modern CSS:** `assets/tokens.css` (the `--l-*` tokens), copied verbatim to
  `web/app/(site)/styles/tokens.css` and locked by `web/scripts/check-css.mjs`:
  edit the asset, then copy it. The per-page sheets in `web/app/(site)/styles/`
  (`front.css`, `problem.css`, `signals.css`, `sources.css`, `category.css`,
  `how-it-works.css`, `not-found.css`, `kit.css`) are not locked; their rules live here and in
  `web/app/(site)/DESIGN.md`. Selectors are prefixed per page (`lf-`, `ls-`,
  `lg-`, `lsr-`, `lc-`, `lh-`, `lk-`, `lnf-`).
- **Static contract:** `web/scripts/check-site.mjs` fails the build on
  `searchParams`/`cookies(`/`headers(`, a `"use client"` outside its allow-list,
  `href="/lab/`, a rejected record's page, and a record page without `id="sN"`.
- **Verify every page change** with screenshots at 1440 and 375 on real data (both
  groupings, several records, one long title), with scripts stripped once, and
  against the NEVER list.
