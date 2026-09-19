# The site — front page, row card, record page and ledger rulebook

The rules that shaped `lib/site/front.tsx` + `styles/front.css`, the record page
(`problem/[region]/[id]/page.tsx` + `styles/problem.css`, its figures
`lib/figures/*` + `styles/kit.css`), and the ledgers (`lib/site/ledger.tsx` +
`styles/signals.css`). The reasons behind the record-page rules are in the
design-language skill, §7. Each line: the rule, its value,
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
- Share previews (`lib/og/share.ts`): the root layout sets `metadataBase`
  (`https://www.localproblems.org`), og:site_name, og:type `website`, og:locale
  and the `summary_large_image` Twitter card. Each page's og:title is its title
  without "— localproblems.org", og:description its description, og:url its own
  path. A record's og:url is also its canonical.
- Share images are 1200×630 PNGs drawn by `next/og` at BUILD time
  (`lib/og/card.tsx`), in Inter cut from the site's own font files
  (`lib/og/fonts`). A record draws its own card
  (`problem/[region]/[id]/opengraph-image.tsx`): title, brief (else category),
  "Opportunity n/12" with the five section dots in the score scale, and the
  entry level's dot and word. Every other page uses the site card
  (`app/opengraph-image.tsx`): the front title, the lede and the Venn.
- Record anchors keep the live site's: every source row `id="s1…sN"` (the
  `sources[]` index), the drawer `id="sources"`, and every older section id as an
  alias (see "Record page: sections"). `#sources` / `#sN` open the drawer on that
  row (`peek-hover.tsx`). No sources section at the foot of the page.

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
  its own breadcrumb bar (Problems / Czechia / P-00xx; "Record page: crumb bar").
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
  - Czechia is the one link: current, solid tick. Five "Coming soon" rows,
    muted, not focusable, flag at 70% opacity: India, Brazil, Nigeria,
    Ukraine, Germany — a guess at where the most motivated builders meet the
    most problems, most likely first ("replace the mock … countries … make an
    educated guess. Keep it 5", 2026-09-17). The reasons live in country.tsx.
  - Opens with the tooltip entrance (fade + 3px rise, 140ms), closes
    instantly; reduced motion: fade only.
- Flags: inline SVG, 20×14, 2px radius, 0.5px hairline border (16% black) so
  white stripes read on white. Never emoji (letters on Windows), never an
  image request. Official colours; exact halves / thirds; Czechia's wedge to
  half the length; India's chakra as a navy ring and hub; Brazil's rhombus,
  globe and white band without stars or motto.
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
  native `<details>`, closed by default. Summary row, on its own tighter grid
  (not the rail; "for the categories the previous version was better"): 16px,
  the drawing (96px), 16px ("more left space next to image, less right
  space"), then the name in the title style at 128px (the solid glyph before
  it on phone), meta "N problems" only ("remove the opportunity up to X in
  categories", 2026-09-17), caret at the end; hover washes it like a row. Open,
  its rows sit 128px in, on the name's edge, their rules and washes spanning
  the whole content box, without their
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
- The same rule holds on the record page: the rail rows (`.ls-toc-row`,
  `.ls-mixrow`) paint an always-present `--l-bg-3` wash in `::before` and fade
  only its opacity; the row itself transitions colour only.

## Record page: keyboard and tooltips
- Citation pills: focus alone opens nothing. Tab focuses the pill; Enter,
  Space, click or hover (~140ms) opens its card; only an open card's links
  join the Tab order; Escape closes it and returns focus to the pill.
- The rail (contents, Evidence) comes BEFORE `main` in the
  source, so it is reached right after the head.
  Grid areas keep it drawn in the right column; at ≤1080px, where it is drawn
  after main, `reading-flow: grid-rows` makes focus follow the drawn order.
- Rail tooltips (`.ls-tip`) show on hover or keyboard focus, and Escape hides
  a showing one without moving pointer or focus (WCAG 1.4.13). It returns
  once the pointer leaves the row or focus moves off it.

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

## Sources (private, LP_ADMIN only)
`/sources` is the signals ledger's compact ledger with its own columns
(`styles/sources.css`, scoped `.lsr`, on top of `signals.css`).
- Columns: feed (flexible) · Type 88 · Cadence · runner 120 · Last run 60 (right) ·
  7 days 60 (right) · Status 64 · State 64 · Last success 88 (right). At ≤1000px
  Type and Cadence go; on a phone the cells name themselves ("Last run 78").
- Feed name ink blue with ↗ when it has a URL; plain `--l-text-1` when not.
- The `<details>` caret opens what the feed yields, then Access · Blocker · Last
  run · Script · Last known good as a 112px label column.
- Status (intent) and State (observed) stay two columns. No alarm hue exists:
  a BROKEN state is 600 `--l-text-1`.
- Blockers, Errors on last run, and unregistered health rows follow as 16/24 600
  headings over key 160 · text · status 72 lists; the key links to its row.

## Record page: grid
The p-0008 design, owner-approved 2026-09-16/17 and live on every record page.
- `.ls-shell`: main 680px (`--ls-main`) · gap 88px · rail 272px (`--ls-rail`),
  centred; padding 0 32px 160px. The head spans both columns on the same grid.
- ≤1080px: one column (main up to 680px), padding 0 24px 120px; the rail follows
  main, 120px below it, as two cards side by side (20px gap); `reading-flow:
  grid-rows`. ≤640px: padding 0 16px 88px; the rail cards stack, 16px apart.
- Footer: the front page's footer line on this grid ("localproblems.org ·
  Czechia" · "Report a correction"), 13px `--l-text-2` over a `--l-line-2` rule.

## Record page: crumb bar
- 48px (`--ls-bar`), sticky at the top, **z-index 30**, so it stays above the
  sticky rail (z 6) that rises under it at the page end. Solid `--l-bg`, 1px
  `--l-line` bottom, 13px `--l-text-3`. The crumb starts on the content's left
  edge (owner): side padding max(32px, (100% − 680 − 88 − 272px) / 2); at
  ≤1080px max(24px, (100% − 680px) / 2); 16px on phone.
- "Problems / Czechia / P-0008". Both links go to `/` (Czechia is the one
  country with data), `--l-text-2`, hover `--l-text-1`; "/" in `--l-text-4`;
  the id `--l-text-1`, 500, tabular, 0.01em. ("Problems / Czechia / P-…",
  2026-09-16)

## Record page: head
- Everything in the main column, left-aligned, at every width. ("the centred
  first section got all over the place")
- Padding 72px top / 104px bottom, 48px top when the drawing shows (always, today:
  `SHOW_HEAD_ART`). Phone 24 / 52.
- Category drawing 128px wide, `#c3c4c9`, 24px above the title; phone 96px, 16px.
  No colour fade behind it. ("without it the page at top would be just plain";
  "Remove the color")
- Title 40px / 1.14, 600, −0.028em, `--l-text-1`, balance. Phone 26px / 1.22,
  −0.022em; over 120 characters it wraps `pretty` on phone.
- Headline copy 28px under the title (20 on phone): 17px / 1.6 `--l-text-2`
  (15.5 / 1.55 on phone). The "Good for" label is on its own line, 12px / 16px
  `--l-text-3`, 2px above its words; story → label 14px. No bullets, no run-in
  label, no bold. The "Draft law" badge stands where a label would ("Badges").
- **Facts column** in the rail's column, on the brief's grid row with the same
  28px top margin, so its first line is level with the brief's: Category ·
  Entry · Verified. A hairline over the list and under each row; rows 10px
  top and bottom; label 13px `--l-text-3` left, value 13px `--l-text-1` right,
  no wrap. Entry is the level dot (7px, 7px before the word) and word in its
  ink, linking `#execution-difficulty` with a 30% `currentColor` underline
  (full on hover). No Locality, no Window. ≤1080px: the facts follow the
  brief, 36px above (28 on phone).

## Record page: sections
- Order and ids: The opportunity `#opportunity` · Suggested solution
  `#solution` · Why now `#why-now` · Willing to pay `#willing-to-pay` ·
  Validated abroad `#validated-abroad` · Market gap `#competition` ·
  Execution difficulty `#execution-difficulty` · Suggested first moves
  `#first-moves` (only when the problem has moves).
- Aliases, each an empty span at its section's top edge that lands where the
  section id does: `problem` → opportunity; `how-it-works` → solution;
  `who-pays`, `how-big` → willing-to-pay; `proven-abroad`, `who-sells-this` →
  validated-abroad; `local-competition` → competition; `difficulty-to-enter` →
  execution-difficulty.
- Gap `--ls-sec-gap` 120px (72 on phone), split around the rule: 60px margin,
  1px `--l-line`, 60px padding to the heading. ("a line before each heading
  clearly separating the sections") The first section has no top margin. A
  heading lands 32px under the bar.
- Heading (h2) 20px / 28px, 600, −0.014em, `--l-text-1`, 16px to the answer.
- Answer line 17px / 26px, 500, `--l-text-1`, max 62ch (16.5 / 25 on phone).
- One scan block (keyed list, bullets, steps or figure) 32px under the answer;
  numbered steps 24px. At most **3** list items on the page (`PAGE_CAP`, page
  code only).
- Prose 15px / 24px `#3b3d43` (`--ls-prose`; 15.5 on phone). Bullets 15 / 24
  `--l-text-2`: a 5px `--l-text-4` dot 3px in, text 18px in, 8px between
  items. Keyed list: key column 148px (132 in a sheet; stacked on phone),
  16px gap, 10px between rows; key 500 `--l-text-1` tabular, value
  `--l-text-2`. A date inside six months hangs its 7px warm dot 14px into the
  gutter.
- **Suggested solution** box: 64px under the section above (48 on phone),
  padding 20 24 22 (16 18 18), `--l-bg-2`, 1px `--l-line`, radius 12. Its own h2
  (12px below it), then the sentence 15 / 24 `--l-text-1`, then ProcessSteps
  24px under, then Read more 20px under. ("Suggested solution could use a bigger
  heading")
- **Why now** page rows: the nearest dated rows still ahead of the register date
  (`extractDate()`), soonest first; the sheet holds the whole list.
- **Execution difficulty** page: "Makes it easier" · "Makes it harder" (labels
  13px / 20px 500 `--l-text-2`, 6px above their list), two columns 32px apart,
  row gap 20px, 20px under the heading; stacked on phone; "Nothing." when a list
  is empty. No level line on the page: the word is in the badge. Sheet: the level
  22px / 1.25, 600, −0.02em (20 on phone) after a 9px hue dot 10px before it;
  the reason 10px under it (15 / 24 prose, only when the reason isn't already
  written as the two lists); the lists in whole sentences 28px under; then "Local
  competition does not change this level. It is covered under Market gap." 28px under.
- **Suggested first moves** page: each move's lead sentence, 500 `--l-text-1`,
  in 24px number squares (radius 6, `--l-bg-3`, 12px 600 `--l-text-2`), text
  40px in (34 on phone), 20px between moves.

## Record page: Read more and the sheet
- **Read more**: a `<button popovertarget>`, 28px under the section's last block;
  padding 7px 14px; 1px `--l-line-2`; radius 8; `--l-bg`; 13px / 20px 500
  `--l-text-1`; hover `--l-bg-3`; focus 2px `--l-text-2` at 2px. Name "Read more:
  {section}". Never filled. ("Read more is an outlined button")
- **Sheet**: `popover="auto"`, `role="dialog"`, labelled by its heading. Width
  min(720px, 100vw − 48px), max height 100dvh − 72px, centred; radius 8; shadow
  `0 0 0 1px rgb(0 0 0 / .07), 0 2px 8px rgb(0 0 0 / .04), 0 28px 72px rgb(0 0 0
  / .14)`; backdrop `rgb(20 20 24 / .32)`. In: 140ms fade + 3px rise. Out:
  instant. Reduced motion: fade only.
- Sticky bar 52px, padding 0 12px 0 56px: the × (28px, radius 6, hover
  `--l-bg-3`) on the right. The section name (13px / 600) and the bar's hairline
  fade in over 64–112px of sheet scroll (scroll-driven, opacity only).
- Page padding 4px 56px 56px. Head: the meta line "P-0008 · {title}" 12px / 16px
  `--l-text-3`, one line, ellipsis; the section heading 8px under it, 30px /
  1.2, 600, −0.024em, balance; 20px to the About panel.
- **About this section**: 32px under it (28 on phone); padding 14 20 16 (12 16 14
  on phone); `--l-bg-2`; radius 10; no edge. "About this section" 13px / 20px 500
  `--l-text-3`, 6px under. One column: label (dt) 13 / 20 500 `--l-text-2`, 2px
  under; text (dd) 14 / 22 `--l-text-3`; 12px between items. What this shows ·
  Why it matters to a builder · How to read the score (scored sections only).
  The words are the page's `SECTION_ABOUT` map, the same on every problem.
  ("one muted column")
- Body: the answer is the lede at 19px / 28px, full width (17 / 26 on phone).
  Blocks 16px apart; scan blocks 32px; a paragraph introducing a list sits 14px
  above it; whatever follows a list is 32px under it; bullets 10px apart.
- **Sub-group heading** (h3): 48px above, 20px / 28px 600, −0.014em
  `--l-text-1`, 10px padding over a hairline, 8px to its rows; its count in
  `--l-text-3`. ("CLEARLY with bigger heading separate")
- Validated abroad sheet: the map full width with no list, then the company rows
  32px under it, a hairline over the first. Market gap sheet: the matrix, then
  "Sells this" and "Sells something nearby" as h3 groups. ("listed two times")
- Company row: padding 14 0 16 (12 0 14 on phone), hairlines between; name 500
  ↗ with the 10px maturity dot; meta 12px `--l-text-3` tabular; source pills (or
  "No source on file", 12px `--l-text-3`) on the right; what it sells 13.5px /
  1.55 `--l-text-2`.
- Phone: a bottom sheet, height 100dvh − 16px, radius 16 16 0 0, a 36×4px
  `--l-line-2` grab handle 6px from the top; bar 48px, padding 0 8 0 20; page
  padding 4 20 40 plus the safe area; heading 26px.

## Record page: scores
- `lib/site/score-proto.ts`, on the ladders the owner approved on 2026-09-19
  (SCORING.md, "PRESENTATION"):
  - The opportunity = `scores.demand` /2
  - Why now = `scores.urgency` /3 (how close and how real the deadline is; no
    freshness point)
  - Willing to pay = `scores.money` /2 (is someone paying for this job now? read
    from price receipts; public money nearby only lifts it)
  - Validated abroad = `scores.proof` /3
  - Market gap = `scores.gap` /2 (more points, a more open field; renamed from
    Competition so a full bar always means good; no contents suffix)
  - Execution difficulty = `entry.level`, Easy 3 · Moderate 2 · Hard 1 · Very
    hard 0 /3
- Words, 0 → max: Unclear pain · Some pain · Clear, recurring pain | No deadline ·
  Soft deadline · Firm deadline · Deadline with penalties | No sign yet · Some
  signs · Clear signs | Not yet · Early abroad · Proven once · Proven in 2+
  markets | Crowded · Early rivals only · Open | Very hard · Hard · Moderate ·
  Easy.
- **Until a record is rescored** (`lib/scoring-v2.ts`, mirrored by
  `SCORING_V2_ENFORCED` in `scripts/check-records.py`), its Why now and Willing to
  pay keep the old words (No deadline · Deadline later · Deadline soon, read off
  the deadline part; No sign yet · Some buyers · Already paying), the old tooltip
  ladders and the old About lines. Delete that branch when the last record joins.
- **Total** = the five rubric checks = the front page's /12. Execution difficulty
  is not in it (`inTotal: false`).
- **Tone** (`scoreTone`): n = max → `--ls-score-good` `#3f8f7f`; n/max ≥ 0.5 →
  `--ls-score-mid` `#b58a2e`; below, 0 included → `--ls-score-bad` `#c4564f`.
- **Heading badge**: beside the h2 on one flex line, vertically centred on it,
  12px after the title (it wraps under, 6px below, when the line is too
  narrow); 16px to the answer. Padding 3px 10px 3px 8px; radius 999px;
  background the tone at 7% over `--l-bg`; text "n/max · word" 13px / 18px 500
  `--l-text-2`, tabular (≥ 5.6:1 on every tint); a 7px tone dot, 6px gap. A
  sibling of the h2, never inside it. ("Make the badge colors more subtle. try
  putting the badges next to the heading")

## Record page: rail
- Sticky at bar + 32px, z-index 6, cards 20px apart, 13px. At ≥1081px, where
  anchor positioning exists, a rail taller than 100dvh − bar − 48px scrolls
  inside itself.
- Card: padding 18 18 16 (16 16 14 on phone), 1px `--l-line`, radius 12. Head
  14px above the rows (10 at ≥1081px): eyebrow 12px 500 `--l-text-2`; the total
  "n/12" with n at 22px / 600 `--l-text-1`.
- **Contents rows**, one per section: min-height 42px, content vertically
  centred, padding 4px 8px 4px 26px, radius 7, 18px line, label `--l-text-2`
  (a zero score `--l-text-3`; the current section `--l-text-1`). A scored row:
  label over its word (12px / 16px `--l-text-3`) on the left; n/max (12px
  `--l-text-3`, opacity 0 → 1 on hover or focus, 0.12s) and the 8px score dot
  on the right, 8px apart. Hover wash `--l-bg-3`, inset 20px from the left so
  the stepper line never breaks; opacity only.
- **Stepper**: a 1px `--l-line-2` line 11px in, drawn from each dot to the next.
  Dots are 8px drawn at 0.75 (6px): at rest a 1.5px `--l-text-4` ring on
  `--l-bg`; read = `--l-text-4` fill; current = `--l-text-1` fill at full size
  (transform). A section becomes current when its top crosses a line 30% down
  the viewport (`view-timeline-inset: 30% 69%`); the last row is current in the
  page's last 24px; The opportunity is current from the top. CSS only;
  unsupported → every dot hollow. ("something cleaner like dots or a line")
- **Tooltips** (scored rows, the total): 320px, padding 14 16, radius 10, pop
  shadow, 13px / 1.5 `--l-text-2`; anchored left of the row, flipping up when
  there's no room below; under the row at ≤1080px. Shown 0.3s after hover or
  keyboard focus (0.12s fade), hidden at once, Escape dismisses. Ladder rungs
  12px; this problem's rung on `--l-bg-3` with its number in teal ink; last line
  "This problem: … n of max."
- **Evidence card**: "Evidence" · "N sources"; one row per source type (min-height
  36px, 30 at ≥1081px): type · 64px bar (4px, `--l-bg-3` track, `--l-text-4`
  fill) · count (20px, 12px `--l-text-3`). Each row is a button that opens the
  drawer at its type's group (`data-src-group`). "View all N sources →" 13px
  500 `--l-text-3`, 12px above.
- No "Who is here". ("remove the Who is here from the right sidebar")
- **Phone** (`.ls-toc-mini`, ≤640px only): after the facts, 28px above; head
  "Opportunity" · n/12 (n 18px); rows 9px top and bottom on hairlines: label ·
  word (12px `--l-text-3`) · n/max (always shown) · dot.

## Record page: figures
("use interaction to simplify, not decoration"; "Make the diagram clearly self
explanatory, less text!") No caption, legend or explanatory paragraph on any of
them. Every dot or column is a `DotPeek`-style `<button popovertarget data-peek>`
opening an `.ls-peek` card (140ms in, instant out). A figure drawn twice on the
page passes `scope` (`"s"` in sheets) so its popover ids stay unique.
- **LocalMatrix** (Market gap): an 18px axis gutter, then two equal columns
  (Early · Established) over two rows (Sells this · Sells something nearby).
  Quadrant min-height 168px, padding 10 8 10 10. Left and bottom axes
  `--l-text-4` with solid 7×6px arrowheads; the inner cross `--l-line`. Dots are
  the 10px MaturityDot (hollow early, filled established) on a lattice of 42px
  rows, 12px clear of every edge, with a fixed jitter hashed from the name.
  Favour quadrants (new and selling this; established and selling this while
  empty) have a `#f4f9f7` wash. "The space is still open" 13px / 18px 500 in
  teal ink `#2e7466`, only in the empty established-and-sells-this quadrant.
  Axis words 11px / 14px 500 `#6e7077`.
- **CompMap** (Validated abroad): at ≥560px of its own width the map is 62% and
  the list 38%, 28px apart; narrower, they stack 16px apart. Map width capped at
  300px ÷ crop ratio beside the list (260 stacked), so its height stays ≤300px;
  the crop is ≈0.72 high per 1 wide. Countries `#efeff2`; Czechia outlined
  `--l-text-1` 1.4 and labelled "CZ"; home bases `#b6b8be`; other markets
  `#dcdde1`. Pins are 17px numbered discs (`--l-text-1`, 10px / 600 white, a 1.5px
  white ring) on 24px targets; several in one country sit as a small centred
  cluster. Pointing at a pin or row, or opening its card, highlights that company
  instantly: base `#8e9097`, markets `#c8cad0`, both outlined; other shaded
  countries `#ebebee`; other pins at 0.35; its list row `--l-bg-2` (indices
  0–11). List 13px / 18px, rows 8px 6px on hairlines: number, name ↗, then 12px
  `#6e7077` meta with 9px swatches (home country, other market codes). Sheet:
  `list={false}`, the map full width. ("make the map less high, maybe keep the
  company list on right … one company through multiple countries")
- **PayDots** (Willing to pay, page and sheet): 40px above, 36 below (32 / 28 on
  phone). Plot 168px (140), a 52px tick gutter (44); up to three labelled log
  gridlines (`--l-line`, 11px `--l-text-3`, "CZK" on the top one). Groups 28px
  apart (16), each at least 64px (56). A column is clamp(6px, 56%, 22px) wide,
  radius 2 2 0 0, at least 3px tall, `#3f8f7f`; a recurring-unit group (per seat
  monthly, per case, per year …) is the teal at 60% over white; hover, focus or
  open `#2e7466`, instantly. A buyer word under each column (11px / 13px
  `--l-text-3`), hidden over 16 columns, or over 8 on phone; a group label 11px /
  14px under a hairline, 8px below. ("could we choose another graph? maybe
  columns"; "use some other color for the graph not gray")
- **PayTimeline** (Willing to pay sheet only): one column per month, 4px apart
  (2 on phone), 16px teal dots stacked from a `--l-line-2` baseline, month 11px
  `--l-text-3` 6px under it; open grant calls as a last group behind a hairline,
  12px + 16px in (6 + 8 on phone).
- **ProcessSteps** (Suggested solution): **the hub** (owner, 2026-09-18). Two
  blocks stacked at every width, the second under a `--l-line` rule (22px above,
  20 below). Headings 13px / 18px `--l-text-2` with the block name in 600
  `--l-text-1` ("Today · …", "With the suggested solution · …"). Each block is a
  three-column grid: people `minmax(0,1fr)`, a 32px wire column (24 on phone),
  places `minmax(0,.62fr)` (`.5fr / 1fr` when the buyer is the hub). Wires are 1px
  `#c9cbd0` (teal `--lk-teal-line` into the one box): every tick starts at the wire
  column's left edge, the bracket sits 16px in (12 on phone) and runs from the
  first tick to the last, and bracketed blocks use equal rows so the join to the one
  box leaves the bracket's midpoint at the box's centre. A person is a 22px gray
  (`#919399`) glyph, name 13px / 18px 600, line 12.5px / 17px `--l-text-2` (teal ink
  after). A place is a white box, 1px `--l-line-2`, radius 8, 16px object glyphs and
  its words 12.5px 500. The one box is 1px `--lk-teal-line` on `--lk-teal-tint`,
  radius 10, a 24px teal-mark glyph, its name 13px 600 `--lk-teal`, then what it
  does itself 12.5px `--lk-teal`. "Nobody does this today" is a dashed box and a
  dashed tick. Open questions: one "Not known: …" line each, 12.5px / 18px
  `#6e7077`, 16px under the picture.
- Figure placement on the page and in the sheet: 32px above (26 on phone), no box.

## Record page: sources drawer
- Right-side `popover="auto"`, width min(440px, 100vw) (full width on phone),
  full height, 1px `--l-line` left edge, shadow `-16px 0 48px rgb(0 0 0 / .07)`,
  backdrop `rgb(20 20 24 / .14)`; slides 24px with a fade at 180ms.
- Head 52px: "Sources N" 14px 600, × on the right. Body padding 4px 20px 32px.
- Groups by source type. The group heading is sticky at the top of the list:
  12px 500 `--l-text-3` with its count, padding 10px 20px 8px full bleed,
  `--l-bg`, hairline under. ("make sure headings are sticky")
- Row: 24px monogram; publisher · host · date (12px); title ↗ 500; why 13px /
  1.55 `--l-text-2`; an "In the source's words" fold; "Cited in …" 12px
  `--l-text-3`.
- An Evidence row opens the drawer and scrolls only the list so its group heading
  sits at the top (a group near the end gets bottom padding while open). Without
  JS it opens at the top.

## Record page: copy and print
- Never "record" to readers: "This problem: 2 of 3.", "Found by the register's
  market check", "No source on file".
- Print: the bar, tooltips, peeks, Read more, sheet bars and footer hide; every
  sheet prints in place (static, no shadow); the rail prints before main as
  plain cards; the drawer prints as the source list, each source unbroken.
