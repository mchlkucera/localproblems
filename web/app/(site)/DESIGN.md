# The site — front page, row card and ledger rulebook

The rules that shaped `lib/site/front.tsx` + `styles/front.css` (and, for the
ledgers, `lib/site/ledger.tsx` + `styles/signals.css`). Each line: the rule, its value,
and (in quotes) the owner correction that produced it, where there was one.
Tokens (`--l-*`) come from `styles/tokens.css`, except the contrast override below.
Change a value here and in the CSS together.

## Routes and metadata
- Two STATIC routes share one component (`front.tsx` `FrontPage`):
  `/` (by opportunity, `page.tsx`) and `/by-category`
  (`by-category/page.tsx`). No page reads `searchParams`, `cookies()` or
  `headers()`: a query string would make the route dynamic (audit B1).
- Titles end "— localproblems.org", never "lab": front "Czech problems worth
  solving", How it works "How it works", a record its own title.
- Descriptions are existing copy, one plain sentence: front = the lede;
  How it works = its first line; a record = its `brief` with `[Sn]` markers,
  links and emphasis stripped, else its `solution`.
- Record anchors keep the live site's: every source row `id="s1…sN"` (the
  `sources[]` index), the drawer `id="sources"`, and `how-big` as an alias at
  the top of Who pays. `#sources` / `#sN` open the drawer on that row
  (`peek-hover.tsx`). No sources section at the foot of the page.

## Contrast (WCAG AA)
- Every text gray reads ≥4.5:1 on every ground it sits on. The modern pages
  override `--l-text-3` to **`#6e7077`** in `.lab.lf` (front.css) and `.lab.ls`
  (problem.css), never in tokens.css: 4.95:1 on white, 4.78 on `#fbfbfc`,
  4.58 on the row wash `#f6f6f8`, 4.50 on `--l-bg-3` `#f4f4f6`. It is the
  lightest gray of the old hue (`#8a8c93`, 3.36:1) that passes on `#f4f4f6`.
- `--l-text-4` (`#a1a3a9`, 2.52:1) is for non-text only: dots, rules, carets,
  bars, underlines. Text that used it (facts labels, counts, hosts, the figure
  kit's small labels) takes `--l-text-3`.
- Drawn lines keep the old gray as `--lf-ring` `#8a8c93` (Venn circles;
  non-text needs 3:1). The "Coming soon" countries are `aria-disabled`
  (inactive components, exempt) and stay `--l-text-4`.

## Page grid
- Max width 1120px, side padding 32px (20px on phone ≤720px).
- Two columns below the header: rail 232px, gap 56px, then the reading column
  (rail 152px / gap 32px at ≤960px; one column on phone). Kept to few edges
  (owner, 2026-09-17: "simplify the grid"; then "the opportunity before was
  better", so the rail stays):
  - nothing passes the content box: the sticky tabs, an open category's
    sticky summary, every rule and wash end at the content edges.
  - the page edge: tabs, band labels, category drawings.
  - the text edge (rail + gap): every title, category name and line of copy.
  - a row's rule and its hover wash are one box: 28px before the text edge
    (16px at ≤960px) to the content edge. A category summary spans the
    whole content box.
- Phone: one column; sticky strips run to the screen edges.
- Top bar 48px, sticky, hairline bottom: brand · "/" · country switcher,
  then Problems · Signals · How it works on the right.

## Top bar
- "How it works", not "About", linking to `/how-it-works` (built
  separately in `./how-it-works/`; `/about` redirects there). ("rename About to How it works")
- Links: Problems `/` · Signals `/signals/funded` · How it works
  `/how-it-works`.
- One bar for every modern page: `<TopBar current="problems" | "signals" |
  "how-it-works" />` from `bar.tsx` (omit `current` on the 404); the current
  page's link gets `aria-current="page"` (primary gray). The record page keeps
  its own breadcrumb bar (Problems / P-00xx).
- All three links show at every width above 720px; none is ever dropped to
  make room. Phone ≤720px: they move behind one menu button (three solid
  bars, 44px target) that opens a native popover, full width under the bar,
  one link per 48px row on hairlines, the current page at 600. No script.
  ("there should be always problems, signals, how it works visible on all
  devices … on mobile lets just hide it behind a burger menu", 2026-09-17)
- Country switcher (`country.tsx`), not a plain "Czechia" crumb. ("a modern
  dropdown with nice flags")
  - Button: "Czechia" + solid caret, no flag, 13px / 500 `--l-text-2`;
    `aria-label="Country: Czechia"`. Hover / open: `--l-bg-3` fill, no fade.
    Flags appear only in the menu. ("hide the flag in the currently selected
    selector, show it only in the dropdown")
  - Native: `<button popovertarget>` + `popover="auto"` menu, CSS anchor
    positioning (under its own button, `bottom span-right`; each trigger has
    its own menu instance, anchor name set inline). No script: click,
    Enter/Space open; Escape and outside click close; Tab walks into the menu.
  - Menu 248px, radius 10px, pop shadow, 4px padding; "Country" heading in
    the meta style; rows 32px: flag · name · right slot.
  - Czechia is the one link: current, solid tick. Slovakia, Poland, Germany,
    Austria, Hungary are listed muted with "Coming soon", not focusable, flag
    at 70% opacity.
  - Opens with the tooltip entrance (fade + 3px rise, 140ms), closes
    instantly; reduced motion: fade only.
- Flags: inline SVG, 20×14, 2px radius, 0.5px hairline border (16% black) so
  white stripes read on white. Never emoji (letters on Windows), never an
  image request. Official colours; exact halves / thirds; Czechia's wedge to
  half the length; Slovakia's arms simplified (white-edged red shield, white
  double cross, blue hills) toward the hoist.
- Phone ≤720px: the bar's switcher reads "CZ" + caret; its menu is pinned 12px
  from the left (the heading's menu stays anchored under "Czech"); links never
  wrap. Sized for the widest pair ("Problems" + "How it works"): 6px bar gaps,
  6px link padding, no gap between links. ≤359px: 12px links, 4px padding, 2px
  bar gaps, no "/". No sideways scroll at 375 or 320 on any page.

## Header
- Title "Czech problems worth solving" (28px / 600, 26px on phone) + ONE plain
  sentence (16px, `--l-text-2`, max 34em). No counts line, no stats.
- "Czech" in the title is the country selector (`<CountryWord />`): a button
  inside the h1 in the heading's own font, weight and colour, with a 2px dotted
  underline (`--l-text-4`, offset 6px) and a 14px solid caret. Hover or open:
  underline `--l-text-2`, caret `--l-text-1`, no fade. The heading still reads
  "Czech problems worth solving" (adjective in the heading, country names in the
  menu); "Choose a country" is a description, never part of the name. The menu
  (`<CountryWordMenu />`) sits after the h1, never inside it, and is the same
  component and list as the top bar's. ("make 'Czech' also a selectable thing")
- The Venn on the right: three monoline circles (1.25 stroke), labels inside
  the 344×160 box so it scales on a phone.
- Every Venn part (each circle + label, and the core) has a plain-language
  hover/focus/tap card; hovering elsewhere on the figure explains the whole
  diagram. Non-technical words; describes what the register looks FOR, never
  promises every problem meets all three. ("make sure we can hover over the
  SVG diagram showing a message … non-technical simple language")
- Text block vertically centred on the diagram: grid rows `1fr auto auto 1fr`,
  diagram `align-self: center` across all four. The diagram's box includes its
  labels; hover cards are absolute and don't count. ("make sure 'Czech
  problems worth solving' is vertically centered with the diagram")
- Padding 96px top, 80px bottom (phone 40 / 48). ("add a bit more negative
  space before the lines start")
- ≤960px: title, sentence, diagram stack.

## Tabs
- "By opportunity" / "By category". No "Group by" label. ("remove 'Group by'
  and just have 'By opportunity' and 'By category'")
- Start on the page edge (x=192 at 1440). ("line up 'By opportunity' to the leftmost column")
- 13px / 500, `--l-text-3`; current one `--l-text-1` + 1px underline, offset 6px.
- Plain links between the two static routes
  (`/`, `/by-category`), no JS, no query string; the
  current one carries `aria-current="page"`. No deadline grouping. ("Remove
  deadline sort")

## Grouping rail (by opportunity)
- Label (13px / 600, `--l-text-1`) + count line "N problems" (13px, `--l-text-3`).
- Opportunity bands at the SCORING.md thresholds as numbers: "Opportunity
  10–12", "8–9", "5–7", "0–4". No verdict words.
- Sticky under the tabs; its first line sits on the first title's cap height.
  Darker rule between bands. (A full-width semibold header strip on desktop
  was tried and rejected, 2026-09-17: "out of place".)
- The tabs are sticky under the bar (48px, 44 on phone), frosted white, their
  bottom rule the list's first rule; band labels stick under them. ("By
  opportunity/category should be also sticky", 2026-09-17)
- Category grouping is an INDEX first, at every width: each category is a
  native `<details>`, closed by default. Summary row: the drawing (96px) in
  the rail (the solid glyph on phone), the name in the title style on the text
  edge, meta "N problems" only ("remove the opportunity up to X in
  categories", 2026-09-17), caret at the end; hover washes it like a row. Open,
  its rows follow on the text edge, titles on the name's edge, without their
  category item or drawing, and the summary sticks under the tabs. ("make the
  by category all hidden first so that we can see the category list first!
  Both on desktop and mobile", 2026-09-17)
- Phone: the band label + count become one line, 15px, a full-bleed frosted
  strip sticky under the tabs; open categories stick the same way. By
  category the name carries the category's solid glyph and the drawing is not
  shown. ("make the categories … sticky so that its clear
  where are we"; "category heading is almost not visible and image is weirdly
  aligned", 2026-09-17)

## Row card — order
1. Title (the one link).
2. Story — `brief`, one plain paragraph. Omitted when absent.
3. "Suggested" label on its own line, then the solution.
4. "Good for" label on its own line, then the text. Omitted when absent.
5. Meta line: opportunity meter, then category.
- A row without the new copy is the same card with only "Suggested" — never a
  different design.
- Category drawing (112px) in a right column; not shown on phone (the meta
  line names the category).
- Phone ≤720px: the row is FOLDED — title, a two-line clamp of the first
  paragraph, the meta line with "Show more" + caret at its right end
  ("Hide" when open). The fold is a visually hidden checkbox + label, CSS only;
  all copy is in the HTML. Above 720px the row is always open. ("make the items
  expandable … just heading, small peek, and toggle to expand", 2026-09-17)

## Exactly three text styles
("there's just too many text styles, figure out how to simplify")
1. **Title** — 18px / 26px, 500, `--l-text-1` (17px / 24px on phone).
2. **Body** — 15px / 24px, 400, `--l-text-2`. Story, solution and good-for alike.
3. **Meta** — 12px, 400, `--l-text-3`. The two labels, the "n/12" figure, the category.
- No bold inside the story, no darker solution. Emphasis comes from the label
  and position, never a fourth style. Citation markers and markdown are stripped.

## Labels
- Never inline with their text: label on its own line (line-height 16px, 2px
  below it), text below. "Suggested Build a small…" must never read as one
  run. ("Suggested and Good for shouldn't mix with the text on the right")
- No colons, no bullets.

## One left content edge
- Title, story, labels, texts and the meter line all start on the title's left
  edge (x=480 at 1440). No label column, no indents. ("can we align the
  scoring with the right col" — resolved by removing the column)

## Measure and clearance
- Copy max 64ch (≈590px); title max 640px.
- ≥50px clear of the category drawing at desktop (measured).
- No bullet glyphs: hanging dots sat in the hover wash / phone gutter and read
  as overflow. ("the visual with the bullets is very messy right now, they're
  overflowing")
- No horizontal page scroll at 375px.

## Wrapping
- Titles: `text-wrap: balance`. Body: `text-wrap: pretty`. No JS fallback.
- No title or paragraph ends on a lone word. ("only 'law' is being broken to a
  new line … we need more balanced wrapping")
- Record-page titles >120 characters use `pretty` on phone: `balance` gives up
  past six lines and left an orphan there.
- Verify at 1440 and 375 on real data, both groupings, every record title.

## Spacing
- Row padding 36px top / 40px bottom (phone 22 / 18); rows separated by a 1px
  `--l-line` hairline. ("these cards need more space")
- Title → story 10px · story → label 14px · text → next label 10px ·
  label → its text 2px · copy → meta line 16px.
- Meter → category 22px. ("increase space between the score meter and
  category", then "lessen … a bit")

## Opportunity meter
- 12 segments, 4×8px, radius 1, gap 2px; filled = score in teal `#3f8f7f`
  (the record page's "in the builder's favour"), empty `--l-bg-4` (`#e3e3e7`
  on the hover wash). Then "n/12" in the meta style; "Opportunity" is
  screen-reader text. ("make the opportunity meter somehow visible")
- It leads the meta line, so meters line up down the page.
- Hover / focus / tap card is specific to THIS record, never generic:
  "Opportunity n of 12", then the five checks (`SCORE_ROWS`), each with its
  own mini bars, score/max and its `scoreRead()` line; sorted most-filled
  first, then the longer bar. ("on hover show specific information, not generic")

## Category
- One 14px SOLID icon per category: 16-unit grid, `fill: currentColor`,
  even-odd fill, no strokes. Colour `#919399`, lighter than the label beside
  it (`--l-text-3`), and still 3.07:1 on white, above the 3:1 a non-text glyph
  needs (`--l-text-4` would be 2.5:1). ("make them a tiny bit grayer") ("add relevant icons instead of
  just boxes", then "choose solid icons instead of outlined ones")
- fintech card (stripe gap + number-line hole) · health cross · housing house
  (door cut out) · energy bolt · mobility truck (wheels clear of the body) ·
  govtech pediment + three columns + step · retail bag with handle · b2b
  lidded crate (slot hole) · legal shield (tick cut out) · education open book
  (spine gap) · environment leaf (vein cut out) · other solid dot.
- The telling detail is always negative space, ≥1px at 14px, so it survives
  the fill.
- Ink density balanced: 0.30–0.42 of the box for eleven; the bolt 0.17 is thin
  by nature and spans the full height.
- Every small UI glyph is solid (menu caret, tick). The large category
  drawings stay line illustrations.
- Icon + label, plain: no hover card. ("remove the category hover, doesn't
  add value")
- No deadline item on the row. ("remove the deadline info")

## Badges
- ONE badge: "Draft law", on records with `draft_law` (the main pain depends
  on a law not passed yet). ("add some badge to all problems that are
  'probably': based on a law that's not yet released")
- Look: neutral outlined gray pill: 1px `--l-line-2` outline, 4px radius,
  18px tall, 6px side padding; label 12px / 500 `--l-text-2` (6.2:1 on white,
  5.7:1 on the hover wash). No fill. It is a UI chip, not a fourth text style.
- Colour meaning: uncertainty, not urgency, so never the favour teal (in the
  builder's favour) or a warm hue (time pressure).
- Row card: last on the meta line, after the meter and the category (22px
  gap). Category pages get it through the shared `Entry`.
- Card on hover / focus / tap, in the tooltip style: the record's `draft_law`
  line (markers stripped) in bold, then "Based on a law that is not passed
  yet, so this may change." It has a card, so it is keyboard-focusable
  (`tabIndex 0`); one card at a time on the meta line.
- Record page: in the head's brief block, the badge standing where a label
  would, over the line (its `[Sn]` as the source pill, a full stop added if
  missing) and the same plain sentence, in the body style.
- Motion: none of its own; the card uses the tooltip entrance. Hover and
  focus darken the outline gray to gray, instantly.

## Motion
- Hover fades change ONE thing: an opacity, or one gray to another. Never
  transition to or from `transparent` — it interpolates through black. The
  row wash is always painted and only its opacity fades. ("flashing through
  black on hover")
- Tooltips (meter card, Venn cards): fade + 3px rise, 140ms ease-out on
  appear, instant exit. Opacity and transform only.
- `prefers-reduced-motion: reduce`: opacity fade only, no movement.
- The same rule holds on the record page: the rail rows (`.ls-dim`,
  `.ls-mixrow`) paint an always-present `--l-bg-3` wash in `::before` and fade
  only its opacity; the row itself transitions colour only.

## Record page: keyboard and tooltips
- Citation pills: focus alone opens nothing. Tab focuses the pill; Enter,
  Space, click or hover (~140ms) opens its card; only an open card's links
  join the Tab order; Escape closes it and returns focus to the pill.
- The rail (Opportunity, Who is here, Evidence) comes BEFORE `main` in the
  source, so it is reached right after the head (tab stop 5 on p-0008).
  Grid areas keep it drawn in the right column; at ≤1080px, where it is drawn
  after main, `reading-flow: grid-rows` makes focus follow the drawn order.
- Rail tooltips (`.ls-tip`) show on hover or keyboard focus, and Escape hides
  a showing one without moving pointer or focus (WCAG 1.4.13). It returns
  once the pointer leaves the row or focus moves off it.

## Record page: header copy
- The front card's rules apply to the head's `brief` / `good_for`: the brief
  a plain paragraph, then "Good for" as a meta label on its own line (12px /
  16px, `--l-text-3`, 2px above) with the words under it. No bullets, no
  run-in "Good for:", no bold. One body style for both (17px / 1.6,
  `--l-text-2`; 15.5px on phone), story → label 14px. The block is
  left-aligned, centred under the centred title; the facts rows are unchanged.

## Whole row is one target
- The title's link is stretched over the row (`::after`); hover or focus
  anywhere washes the row (`#f6f6f8`, radius 8px) and underlines the title.
  ("make the whole page hoverable")
- Wash and click area share one inset: 4px top/bottom (never over the
  hairlines), **28px past the text edge on the left** ("the grey of the card
  should reach more to the left"; 16px at ≤960px) and exactly to the content
  edge on the right. The rule above a row is the same box, so grey and rule
  are one width. On phone the wash runs to the screen edges.
- The meta line sits above the stretched link and is only as wide as its
  items, so the meter takes its own pointer; it is tabIndex −1, so the
  keyboard tabs title to title.

## Signals ledgers: a compact ledger
Data-dense pages trade air for rows; the front page and the record keep theirs.
("The Signals view needs something better: less negative space, more cramped,
fit more on the page, more compact. Love the blue you've chosen.")
- One 34px line per signal (7px above and below a 20px line, hairline between):
  about 24 rows in a 1440×900 window.
- Columns, in a fixed grid so each reads down the page: title (flexible) ·
  Source 200 · Sector 104 · Origin 84 · Value 64 (right) · Date 84 (right),
  16px apart, 28px kept clear on the right for the summary caret. One quiet
  column-head line (12/500, `--l-text-3`) over the first month. At ≤1000px the
  Origin column goes.
- Title 14/20 500 in ink blue `#3d5a96` (a source you can open), ending in ↗.
  It truncates with an ellipsis; the full title is the link's native `title`.
- Meta cells 12/20 `--l-text-3`, tabular figures, ellipsis. The §7.3 review
  flag rides in the Source cell ("TED · Read by LLM").
- The summary (and the source's own words, when ingest kept them) sits in a
  native `<details>` whose caret is the row's last element: it opens on click,
  tap or Enter, never on hover alone, with no script.
- The month is a slim sticky line under the bar (12px: month 600 `--l-text-1`,
  count `--l-text-3`), painted white with a hairline, never a rail block.
- Row wash `#f6f6f8` under the pointer and on the `:target` row (a deep link),
  always painted, opacity only, instant. Deep links clear the bar and the
  month line (`scroll-margin-top`).
- Header tightened: 40px above the title, a 14/22 description, the six tabs.
- Phone (≤720px): no column heads; two lines per row, the title (clamped to
  two lines) then Source · Value · Date. Sector and Origin go. No sideways scroll.
- Unchanged: row ids (= signal ids), 100 rows per page, the pager, the honest
  empty state.
