# Record page redesign: the p-0008 pilot

*Spec, 2026-09-16. Answers the owner's feedback of the same day on
`/lab/modern/cz/p-0008`. **Scope: ONE page, p-0008, for owner approval.** Other
records must still render and pass the build, but nobody rewrites them in this
pass. Rulebooks (RECORD-TEMPLATE.md, MATCH.md, SKILL.md, DESIGN.md,
check-records.py) are NOT edited until the owner approves. §9 lists what gets
written into them afterwards.*

Owner's brief, condensed: *complex language, walls of text, fluff, the same
fact said many times. Make it clear. Diagrams serve understanding, not
decoration. More space. Link between sections. "Suggested first moves", and the
first one builds something or contacts someone, never "Sell".* Clarification
from the owner: **scannability comes first.** Someone who reads only the
headings and first lines still gets the story.

---

## 1. Decisions (read this first)

| # | Decision | Why |
|---|---|---|
| D1 | **Eight sections, each answering one builder question, in this order:** The problem, Suggested solution, How it works, Who already sells this, Who pays, Why now, Difficulty to enter, Suggested first moves. | One question per section, and the reader's order: what's wrong → what to build → what changes → who's there → money → timing → cost of entry → what to do Monday. |
| D2 | **Every section has the same anatomy:** heading → **answer line** (one sentence that answers the section's question) → at most ONE scannable block (keyed list, bullets, table or figure) → folds for detail. | Scannability. Read only the headings and answer lines and you still get the whole story. |
| D3 | **Say it once.** Every fact type has ONE home (§4). Other places link to that home with an in-page link and never restate the fact. | Owner: "minimize saying one information twice". |
| D4 | **Proven abroad and Local competition merge** into one section, **"Who already sells this"**. It opens with a small count graphic in the Isotype style (one dot per company, filled = established, hollow = early), followed by the company rows grouped the same way. **Removed from the page:** the Europe map, the field timeline, both figure captions, and the long "Existing non-solutions" / "Solved elsewhere" paragraphs. | Each company appears once, as its row. The graphic shows counts and maturity, never names, so it restates nothing. Any figure that needs a paragraph to be read is cut. |
| D5 | **The process diagram becomes an HTML step table:** numbered rows, with a "Today" column and a "With the suggested solution" column. No cards, no chevrons, no legend. Uncertainty sits in the row itself ("? Not known", "Our reading"). It is drawn ONCE, not twice. **No external diagram service** (§6). | The data is a straight sequence of 2 to 8 steps in two states. That is a table, not a graph. |
| D6 | **Who pays** = answer line → a keyed list of 2 to 4 money facts → a **"What one buyer pays"** table built from the price receipts → a folded "Public money nearby". **The MoneyScale figure is removed** (it needed a legend, S-numbers and a caption). Two absence lines become one. | "Who pays — so complex". |
| D7 | **Why now** = answer line → a **keyed list of dated events** (date in the key column, event in plain words), oldest first. The generated "Dates on file" list is removed: it printed source-document dates such as "31 Dec 2026 · the 6,000-firm alarm". | Dates are what readers scan for, so they get their own column. |
| D8 | **Difficulty to enter** shrinks to two lines: the level (dot + word) and one sentence naming the gates that set it. The "Already here: … counts under Local competition" line is cut. | That line was about competition, which now has one home. |
| D9 | **Suggested first moves**: 3 to 5 numbered moves. Each is one short imperative sentence (≤12 words), plus at most one sentence, plus at least one in-page link to the section that holds the evidence. Move 1 builds something or contacts someone. No `[Sn]`, amounts or dates inside moves: they link instead. | Owner: "first move should not be to Sell … build something. Or contact someone"; "use linking inside the text". |
| D10 | **The head's category drawing is removed** from the record page (the owner's option 3). The drawings stay where they do a job: the front page's by-category rail and category pages. | The drawing only says "category", which the facts column already says in words and with its icon. It is the same picture on every record in the category, it is the largest thing above the fold, and it pushes the title down about 250px. Cropping or shrinking it (options 1 and 2) fixes the alignment but not the fact that it tells the reader nothing about this problem. **This changes SKILL.md §7 (Head).** It is recorded for §9, not edited now. |
| D11 | **Facts column** (the coordinator is making the move now): Category · Entry · Verified, stacked in the right column beside the title, label on the left and value on the right, on hairlines. **Locality is dropped** (all 37 records are `CZ-national`, and the breadcrumb already says Czechia). **Window is dropped** (Why now holds the dates). | Say it once, and use the empty right half of the head. |
| D12 | **Hierarchy is flatter, with more air.** Inside a section there are four levels: heading (20/600) → answer line (17/26, 500, text-1) → body and list (15/24, text-2) → meta and fold (12–13, text-3). The gap between sections goes from 88 to **120px** (72 on phone). The rail keeps the Opportunity and Evidence cards. | Owner: "more space between sections … More hierarchy? Less?" Fewer levels, more space, less content. |

## 2. Work packages (pilot)

The content rewrite of `data/problems/cz/p-0008-nis2-implementation-capacity.md`
**is already running under the coordinator's agent, which owns that file.** §7 is
its brief. The three packages below run in parallel with it and with each other.
Every file has exactly one owner.

| WP | Goal | Owns (only these files) | Depends on |
|---|---|---|---|
| **WP1 Page** | Skeleton, section order, anatomy, company rows, Who pays table, Why now hook, Difficulty (2 lines), moves, no head art, spacing | `web/app/lab/modern/[region]/[id]/page.tsx`, `web/app/lab/modern/problem.css` | The coordinator's head edit (facts column, "Suggested first moves") lands FIRST, so re-read both files before editing. It codes against the WP2 and WP3 contracts in §5, which it can do before they land. |
| **WP2 Figures** | `ProcessSteps`, `FieldStrip`, `MaturityDot` | `web/app/lab/parts/figures/kit/process.tsx`, `kit/field.tsx`, `kit/index.ts`, `kit/kit.css` | None. `comp-map.tsx` and `money.tsx` stay untouched on disk (unused, and deleted in migration step 2). Keep the old exports until WP1 no longer imports them, then remove `ProcessToday`, `ProcessAfter`, `FieldTimeline`, `FieldGrid`, `CompMap` and `MoneyScale` from `index.ts`. |
| **WP3 Prose** | Answer line, keyed lists, `#anchor` links, dek split that knows about newlines | `web/app/lab/modern/prose.tsx`, `web/lib/md.ts`, `web/lib/sections.ts` | None. The gazette must keep rendering (§8). |

**Constraints for everyone**
- **The dev server is already running.** Never start another one, and never run
  `next build` while it runs. Check your work with screenshots from the dev
  server, plus `cd web && npx tsc --noEmit` and
  `python3 scripts/check-records.py --strict` (use a python that has PyYAML,
  e.g. `/usr/local/bin/python3`).
- The dev server reads `data/register.db`. After p-0008 changes, rebuild the db
  with `python3 scripts/db.py rebuild`, serialised under
  `mkdir $SCRATCH/db.lock && … ; rmdir $SCRATCH/db.lock`.
- **The coordinator runs the integration build once**, after all packages land
  and with the dev server stopped: `npm --prefix web run build` (all four gates),
  then `npm --prefix web run parity`, then restart dev.
- No new hue, no new font, no new client JS, no `searchParams`.

**Acceptance (all packages, checked together)**
1. Screenshots at 1440×1000 and 375×812, full page, of **p-0008** (the pilot),
   **p-0010** (has a `process`, legacy prose) and **p-0009** (no process, 7
   locals, legacy prose), saved to the session scratchpad.
2. p-0008 passes the skim test: its headings and answer lines, read alone,
   tell the story (§3).
3. Every section on p-0008 matches its §3 anatomy. The page shows no map, no
   timeline, no money scale, no figure caption, no "?" card, no legend
   paragraph and no head drawing.
4. On p-0008, Secfix, Copla and every local company name appear **exactly once**
   in the rendered main column (as their row), not counting the sources drawer
   and peek cards. Check with
   `agent-browser eval "document.querySelector('.ls-main').innerText.split('Secfix').length-1"`,
   which must print `1`.
5. Legacy records (p-0009, p-0010) render without errors or empty headings, and
   their longer prose is folded (§3.4).
6. Page reads with scripts stripped, there is no horizontal scroll at 375 or 320,
   and text contrast is unchanged.
7. Integration build and parity pass.

---

## 3. Page skeleton and section anatomy

```
bar      Problems / Czechia / P-0008
head     title · brief · Good for · [Draft law]          │ facts column (right)
main     1 The problem                                   │ rail (sticky):
         2 Suggested solution (box)                      │   Opportunity card
         3 How it works            (only with process)   │   Evidence card
         4 Who already sells this                        │
         5 Who pays                                      │
         6 Why now                                       │
         7 Difficulty to enter                           │
         8 Suggested first moves                         │
drawer   Sources (unchanged)
```

**Skim test.** Reading only the h2s and answer lines of p-0008 should give:
*The problem → "Organisations under the new law must register and put security
measures in place within a year." Solution → "Build a small security agency…"
Who already sells this → "Four small Czech products sell the paperwork, and none
does the security work." Who pays → "The covered organisations pay, and towns and
hospitals can get half back from an EU grant." Why now → "The first one-year
deadlines run out in late 2026." Moves → "Build a fixed-price readiness check for
one town."*

### 3.1 The head (the coordinator's edit, plus D10)

```
Problems / Czechia / P-0008
────────────────────────────────────────────────────────────────────────────────

   6,000 Czech towns and firms have months                     Category    ▪ Legal
   left to meet a new cybersecurity law                        ─────────────────────
                                                               Entry        ● Hard
   Many small firms don't even know the law covers them,       ─────────────────────
   and the first deadlines hit in late 2026. [Zákony +1]       Verified  4 Sep 2026
   A firm that misses its deadline can be fined …
   Good for
   Someone with cybersecurity skills who's interested in …
            ↑ 680px main column edge                            ↑ 272px rail column
```
- No category drawing. The title starts 72px under the bar.
- Facts: label 12px text-3 on the left, value 14px text-1 on the right, rows at
  least 36px tall, hairlines between them, top aligned with the h1's first line.
  Entry links to `#difficulty-to-enter`. At ≤1080px the facts become a row under
  Good for. On phone, full-width label and value rows (as now).
- Nothing else changes (brief, Good for, Draft law badge).

### 3.2 Section anatomy (every section)

| Level | Style | Rule |
|---|---|---|
| h2 | 20/28, 600, text-1; 16px below | The section's plain title. No counts beside it. |
| **Answer line** | 17/26, 500, text-1, max 62ch; 16px below | The FIRST block of the section, when it is exactly one sentence. It answers the section's question. |
| Body | 15/24, 400, `--ls-prose`; 16px between blocks | At most one short paragraph (≤2 sentences) after the answer line. |
| Scan block | a keyed list, bullets, a table or a figure; 32px above and below | At most ONE per section. |
| Fold | `<details>`, summary 13/500 text-2 with a solid caret; 24px above | Detail that the answer doesn't need. |

**Keyed list**: a markdown bullet list where every item starts with
`**key:**`. It renders as a two-column `<dl>`: key column 148px, 15/24, 500,
text-1, tabular-nums, colon dropped; value column text-2; 10px between rows.
On phone the key sits on its own line above the value (the "labels on their
own line" rule). Use it wherever the reader scans for a number or a date.

### 3.3 The sections

**1. The problem** (`#problem`). *Question: what goes wrong, and for whom?*
Answer line, then a keyed list or bullets of 2 to 4 facts, each with a number
pulled into the key. No figure. The process moves to section 3.

**2. Suggested solution** (`#solution`, the existing box). *What could someone
build?* The `solution:` sentence, then `process.summary.after` as one body
sentence when present. The ProcessAfter figure is no longer inside the box.

**3. How it works** (`#how-it-works`, only when `process` exists). *Which steps
does the solution change?* Answer line = `process.summary.today` (pills via
`citedText`), then `ProcessSteps` (§5.1).

**4. Who already sells this** (`#who-sells-this`). *Who would I compete with
here, and has it worked elsewhere?*

```
Who already sells this

Four small Czech products sell the paperwork, and none does the security work. [Market check]

                                               ● established   ○ early
In Czechia · sells this          ○ ○ ○ ○        4 · all early                 ← teal read
In Czechia · sells something     ●              1 · established
nearby
Abroad                           ● ●            2 · established in several markets
─────────────────────────────────────────────────────────────────────────────
In Czechia · sells this   ○ NIS2 Průvodce ↗  since 2025          [Market check +1]
(id=local-competition)      A Czech compliance platform sold by subscription.  Details
                          ○ Compligen ↗  since 2026                   [Market check]
                            An online generator for the required documents.   Details
                          …
In Czechia · sells        ● ICZ Risk*Guide ↗  since 1997              [Market check]
something nearby            A security platform bought as a big project.       Details
─────────────────────────────────────────────────────────────────────────────
Abroad                    Two funded European companies sell this to small firms. [Vestbee +1]
(id=proven-abroad)        ● Secfix ↗  Germany · since 2021                  [Vestbee]
                            Raised €10.2M (Series A, Feb 2026).               Details
                          ● Copla ↗  Lithuania · since 2023                 [Vestbee]
```
- Order: Czechia first (who you would compete with), then Abroad (who proves it
  works). Owner question Q1.
- The answer line is the first sentence of `Existing non-solutions:`. The Abroad
  group opens with the first sentence of `Solved elsewhere:` as one body line.
  Anything left in those paragraphs (legacy records) goes into a `<details>`
  fold, "More detail", under its group.
- The strip (`FieldStrip`, §5.2) shows counts and maturity only, never names.
  The group label column shows the label only, with no "4 players" counts (the
  strip has them).
- Row: `MaturityDot` · name ↗ · meta (Czechia: `since YYYY`; abroad:
  `Country · since YYYY`; the IČO moves into Details) · pills at the row end ·
  one line (the first sentence of `evidence` / the first clause of `traction`,
  never clamped mid-word) · Details (the native popover, unchanged).
- Abroad dots are drawn gray (`--l-text-3`, filled) because `comps[]` carries no
  maturity yet (added in §9). The Abroad read comes from `scoreRead(p, "proof")`.
  Legend line: "In Czechia: ● established ○ early".
- Teal (in the builder's favour) is used only in reads: the Czechia "sells this"
  read when no row there is established ("4 · all early", "Nobody sells this
  here yet"), and the Abroad read when proof ≥ 2.
- Anchors: the Czechia block carries `id="local-competition"` and the Abroad
  block `id="proven-abroad"`, so rail links and gazette-era deep links still land.
- No CompMap, no FieldTimeline.

**5. Who pays** (`#who-pays`, alias `#how-big`). *Who pays, and how much?*
```
Who pays

The covered organisations pay, and towns and hospitals can get half back from an EU grant. [pills]

About €33M          Public cyber-security contracts, June–August 2026. [Registr smluv]
About 121,000 CZK   What one town paid a consultant just to write its grant application. [pill]
€500–6,000 a year   What compliance software costs per firm abroad. [reglyze.com]

What one buyer pays
3,000 CZK a month   A Czech company · list price · Aug 2026            [nis2pruvodce.cz]
91,000 CZK once     A care home · signed contract · Jun 2026           [Registr smluv]
9M CZK once         A town of about 7,000 · signed contract · Aug 2026 [Registr smluv]

▸ Public money nearby · 13
```
- The table comes from `type: price` receipts, sorted by amount ascending.
  Amount + plain unit (page-local labels: one-off "once", per-seat-month "a
  month", per-year "a year", per-case "per case", per-project "per project",
  per-hour "an hour"), then payer · basis · month, then the pill. Heading
  "What one buyer pays" (13/500, text-2).
- Fold rows: amount (when on file) · gist · month · pill, sorted by amount
  descending.
- With no receipt, ONE line replaces both absence lines: "No price paid by a
  Czech buyer is on file yet." When `price_search` exists, it goes in a fold,
  "Where to look".
- No MoneyScale.

**6. Why now** (`#why-now`). *What forces buyers to act, and when?* Answer line,
then a keyed list with dates as keys, oldest first. The page passes
`keyedSoon(key)` (§5.3): a key that parses as `D Mon YYYY` or `Mon YYYY` and
falls between `extractDate()` and 183 days after it gets the warm 7px dot
(`.ls-soon`). "Dates on file" is removed on every record.
```
1 Nov 2025     The new cybersecurity law took effect. [pill]
15 Sep 2026  • EU money for building security tools closes. [ECCC]
Late 2026      The first one-year deadlines for security measures run out. [pill]
17 Dec 2026  • The EU grant for towns, regions and hospitals stops taking applications. [IROP]
```

**7. Difficulty to enter** (`#difficulty-to-enter`). The level line and the
reason sentence, as now. Line 3 is deleted.

**8. Suggested first moves** (`#first-moves`). The numbered list (`ls-steps`).
Each move's first sentence is its 500-weight lead. In-page links are ink blue
with no ↗.

### 3.4 Legacy records (every record except p-0008)
They render with the same skeleton. Differences: a first paragraph longer than
one sentence keeps today's run-in lead instead of an answer line. The
competition and solved paragraphs show their first sentence, with the rest in
the "More detail" fold. Why now shows its prose without "Dates on file". Names
still repeat inside their prose until each record is rewritten. That is
expected, and it is the follow-up.

---

## 4. Say it once: one home per fact

| Fact | Its ONE home, in full | Everywhere else |
|---|---|---|
| A company (comps/locals) | Its row in **Who already sells this** (name ↗, meta, one line, pills, Details) | A link: `[the Czech sellers](#local-competition)`, `[the companies abroad](#proven-abroad)`. Never named in prose, the process table, the solution or moves. |
| A price one buyer paid | Its row in **What one buyer pays** | A link to `#how-big`. Not restated in a company line or a move. |
| A public award or grant pot | Its row in the **Public money nearby** fold | Prose gives only aggregates ("about €33M across 77 contracts"). |
| A deadline or dated event | Its key in the **Why now** list | The head's brief may say "late 2026" (the head is the abstract). Moves link to `#why-now`. |
| An agency, law or programme | Named in plain words where first used ("the national cyber-security agency", "the new cybersecurity law", "the EU grant for towns and hospitals"). The official name and Act number live in the source pill and drawer. | No acronym without a gloss, and no Act numbers in prose. |
| A source | The drawer, and the peek card behind each pill | A pill only. |
| A score or rung | The rail | Nowhere in the main column. |
| Entry gates | Difficulty to enter | The facts column shows the level word only. |
| Maturity | The row's dot, and the strip | Not written as words in prose ("early", "one person"). |

---

## 5. Component contracts (so WP1 can code before WP2 and WP3 land)

### 5.1 `ProcessSteps` (WP2, `kit/process.tsx`)
```ts
export function ProcessSteps(props: {
  process?: ProcessField | null; sources: readonly ProblemSource[]; ctx?: CiteCtx;
}): ReactNode   // null without process or with < 2 steps
```
```
     Today                                      With the suggested solution
─────────────────────────────────────────────────────────────────────────────
1    A consultant                               ● One fixed-price provider makes
     Works out whether the law applies and        the same check, before the
     what the organisation owes. [SME Union +1]   deadline.
─────────────────────────────────────────────────────────────────────────────
2    The town or care home                      Same as today
     Registers with the national cyber-
     security agency, which starts its
     one-year clock. [Zákony +1]
─────────────────────────────────────────────────────────────────────────────
5    Nobody in-house · Our reading              ● The provider does the security
     The security measures have nobody to         work itself.
     carry them out. [SME Union +1]
─────────────────────────────────────────────────────────────────────────────
6    ? Not known                                Same as today
     Who checks the measures after the
     deadline, and when.
```
- An `<ol>` with a grid of 28px number, 1fr Today and 1fr After, and hairlines
  between rows. Column heads (12px text-3) are `aria-hidden`, and each cell
  carries screen-reader text ("Today:" / "With the suggested solution:").
- Actor line 13/500 text-1; step text 14/22 text-2; pills after the text.
- `known: inferred` → " · Our reading" after the actor (text-3).
  `known: unknown` → actor reads "? Not known" (the 16px solid `?` glyph plus
  the words) and the text goes text-3. **No legend, no dashed or gray cards.**
- After column: `changes`/`new` → text-1 with a 6px teal dot (in the builder's
  favour); `stays` → "Same as today" text-3; `goes` → "No longer needed" text-3;
  a `new` step's Today cell → "Not done today" text-3. `reenters` → a meta line
  "Re-types what someone already wrote". The tally line is removed.
- Phone: each row stacks as number + actor, then the "Today" label on its own
  line above its text, then the "With the suggested solution" label above its
  text.

### 5.2 `FieldStrip` and `MaturityDot` (WP2, `kit/field.tsx`)
```ts
export type Maturity = "established" | "early" | null;   // null = not on file (comps today)
export function MaturityDot(props: { m: Maturity }): ReactNode  // 10px, aria-hidden
export function FieldStrip(props: { p: Problem }): ReactNode    // null when comps and locals are both empty
```
- Three rows, always in this order: "In Czechia · sells this" (`competes:
  direct`), "In Czechia · sells something nearby" (`adjacent`, row omitted when
  empty), "Abroad" (`comps`, row omitted when empty). The first row always shows:
  when empty it reads "Nobody sells this here yet" in teal ink.
- Grid: label 200px (13/500 text-2) · dots (6px gap, wrapping) · read (13px).
  Established = filled `--l-text-1`; early = 1.5px ring `--l-text-1`;
  null = filled `--l-text-3`.
- Reads: Czechia rows give `n · all early` / `n · all established` /
  `n · k established`; Abroad gives `n · ` + the tail of `scoreRead(p, "proof")`.
  Teal ink only under the rule in §3.3.
- One legend line above, right-aligned, 12px: "In Czechia: ● established ○ early".
- HTML, not SVG. Each row has screen-reader text ("4 companies in Czechia sell
  this, all early"). On phone the label sits on its own line.
- Class prefixes `lk-strip-*` and `lk-dot`. WP1 imports `MaturityDot` for rows,
  so the strip and the rows draw the same mark.

### 5.3 Prose (WP3)
- **Answer line:** in `Prose(md, ctx, { lead: true })`, a FIRST paragraph that is
  exactly one sentence (`splitLead(text).rest === ""`) renders as
  `<p className="ls-answer">`. A longer first paragraph keeps today's run-in lead.
  WP1 styles `.ls-answer`.
- **Keyed list:** when every line of a bullet block matches
  `^- \*\*([^*]{1,40}?):\*\*\s+(.+)$`, render `<dl className="ls-keyed">`, each
  item a `<div className="ls-keyed-row"><dt className="ls-keyed-k">key</dt><dd className="ls-keyed-v">…</dd></div>`.
  New option `ProseOpts.keyedSoon?: (key: string) => boolean`; when it returns
  true the `dt` also gets `ls-soon`. WP1 styles all of these.
- **In-page links:** extend `INLINE` so `[text](#anchor)` (anchor
  `[a-z0-9-]+`) becomes `<a className="ls-link" href="#anchor">`, with no `EXT`
  and no ↗.
- **Gazette `web/lib/md.ts`:** accept `#anchor` targets in its link regex, or
  the live page would print raw markdown. Keyed bullets already render there as
  bold-key bullets, which is fine.
- **`web/lib/sections.ts`:** `splitFirstSentence` also ends a sentence at `.\n`
  / `.` + newline, so a Who pays paragraph followed by list lines still gives a
  one-sentence dek on the gazette page.
- A new helper for WP1: `export function splitProse(md): { first: string; rest: string }`,
  which splits at the first sentence boundary, for the "More detail" folds.

---

## 6. The diagram question: why no external service

| Option | Verdict |
|---|---|
| A hosted renderer at request time (Kroki, mermaid.ink, embeds) | **Out.** Pages are static, the CSP blocks it, and there is no request-time data. |
| A hosted renderer called at build time | **Out.** A network call during the build makes builds non-reproducible, and the output looks like the vendor, not our tokens. |
| Mermaid, rendered at build time (mermaid-cli) | **No.** It pulls a headless Chromium into the build. Its SVG sets its own label boxes and fonts, so fitting it to one font, a gray ramp and three hues is a fight. For a straight line of steps it draws a row of boxes, which is the mess we have now. |
| D2 | **No.** A Go binary outside npm, its own look, and the good layout engine is proprietary. |
| elkjs / dagre (layout only, our own SVG) | **Not now.** Pure JS, and it would fit the tokens. But it solves branching layout, and `process.steps` is a straight list by contract. SVG text also doesn't wrap, which is the current kit's weakness. **Our fallback if a record ever needs branches.** |
| A Figma diagram | **No.** It is hand-made, so it drifts from the record: "if a derived figure draws wrong, the ledger is wrong". |
| **An HTML step table (chosen)** | Text wraps naturally, it reads on a phone, a screen reader gets it, it needs no JS and costs nothing at build, and it fits the design system. Two columns side by side make the before/after comparison without drawing the steps twice. |

---

## 7. Brief for the p-0008 content agent (the owner's voice = the headline block)

The agent owns the p-0008 file. It may rewrite body prose and `process` step
text only. **No score, status, `sources[]` entry, `note` or marker numbering
changes. Every claim is checked against its source** (RECORD-TEMPLATE rules
10–20 still apply). Add a dated `## Revisions` entry. It must still pass
`check-records.py --strict`.

**Writing rules for this pass (to be written into RECORD-TEMPLATE after approval, §9):**
1. **Answer first.** Each section's first paragraph is ONE sentence of at most 25
   words that answers the section's question. Put "who" and "what happens" in
   it, and no aside.
2. **Short blocks.** After the answer: at most one paragraph of at most 2
   sentences, OR one list of 2 to 5 items. A sentence has at most 25 words, at
   most one parenthesis or dash pair, and at most two `[Sn]`.
3. **Lists over runs.** Three or more parallel items make a list. Items where
   the reader scans for a number or date make a **keyed list**
   (`- **About €33M:** …`, `- **17 Dec 2026:** …`). The key is at most 4 words.
4. **Plain names.** No acronym, agency, programme or Act number unless it is
   explained where it appears; prefer the plain name alone. ✗ "NÚKIB counts
   delay against the unregistered" ✓ "The national cyber-security agency treats
   a long delay as a reason for a bigger fine." ✗ "Act No. 264/2025 Coll." ✓
   "the new cybersecurity law". ✗ "IROP 120" ✓ "the EU grant for towns,
   regions and hospitals".
5. **Numbers:** round them and say what they mean. Write "about", never "~".
   Keep a number only if it changes a decision.
6. **No fluff:** cut "demonstrably", "compelled by law, not persuaded",
   "consultancies are no longer alone", "Existing non-solutions" phrasing,
   market-size sentences that aren't about Czech buyers (the $70bn Europe
   figure), and "Know who else is in the room".
7. **Say it once (§4):** no company names in prose or moves; no receipt price
   or dated event restated outside its home. Link instead.
8. **In-page links** use only anchors that exist on BOTH the modern and gazette
   pages: `#problem`, `#proven-abroad`, `#local-competition`, `#how-big`,
   `#why-now`, `#difficulty-to-enter`, `#first-moves`.
9. **`Existing non-solutions:` and `Solved elsewhere:` are ONE sentence each**,
   with no names (the rows carry them).
10. **Moves:** 3 to 5. The first sentence is an imperative of at most 12 words;
    at most one more sentence; at least one in-page link; no `[Sn]`, amounts,
    percentages or full dates. **Move 1 builds or contacts** (Build, Make, Call,
    Email, Meet, Visit, Interview, Ask, Shadow, Write). No move 1 sells. Keep the
    body heading `## First moves` (it is a parse key; the page prints
    "Suggested first moves").
11. **Process step text:** actor in plain words ("A consultant who checks what
    the law requires", not "A scope-analysis seller"); one sentence per cell;
    `summary.today` ≤ 25 words.

**Target shape (illustrative. Verify every claim against its source before writing):**
```markdown
The new cybersecurity law makes each covered organisation register with the national cyber-security agency, then put security measures in place within a year [S1].

- **About 6,000:** firms, towns and hospitals the law covers, across energy, manufacturing, food, logistics and digital services [S1,S2].
- **4,825:** had registered by February 2026, so over a thousand had not [S13].
- **1 university:** had to re-tender for the outside security manager the law requires [S19].

Why now: The first one-year deadlines run out in late 2026 [S1].
- **1 Nov 2025:** the new cybersecurity law took effect [S1].
- **17 Jul 2026:** the state began naming organisations under a second law that adds physical-security duties [S5].
- **15 Sep 2026:** EU money for building security tools closes [S10].
- **Late 2026:** the first deadlines for security measures run out [S1].
- **17 Dec 2026:** the EU grant for towns, regions and hospitals stops taking applications [S9].

Who pays: The covered organisations pay, and towns and hospitals can get half back from an EU grant [S1,S9].
- **About €33M:** public cyber-security contracts in June–August 2026 [S7].
- **About 121,000 CZK:** what one town paid a consultant just to write its grant application [S8].
- **€500–6,000 a year:** what compliance software costs per firm abroad [S14].

Existing non-solutions: Four small Czech products sell the paperwork the law requires, and none does the security work itself [S16].

Solved elsewhere: Two funded European companies sell security-compliance software to small firms [S11,S12].

## First moves

1. Build a fixed-price readiness check for one town. It shows what the town owes under [the new law](#why-now) and by when.
2. Call the care homes and small towns already buying help. Their contracts are listed under [Who pays](#how-big).
3. Write one town's EU grant application, then do the work it pays for. The grant [closes in December](#why-now).
4. Sell the security work, not the documents. [The Czech sellers](#local-competition) only sell the paperwork.
5. Offer the second law's duties to the same customers. See [Why now](#why-now).
```

---

## 8. Data vs page, and gazette safety

- **Page-only (WP1, WP2, WP3):** everything in §3 and §5. **No new record field,
  no schema, db or zod change in the pilot.**
- **Content (p-0008 only):** body prose and `process` text, rewritten.
- **The gazette reads the same file.** Once deployed, p-0008's live page will
  show the new prose. Checks:
  - `#anchor` links need WP3's `md.ts` change, or they print as raw markdown.
  - The gazette dek (first sentence of Who pays) needs WP3's `sections.ts` fix,
    or the dek swallows the list.
  - Keyed bullets render as bold-key bullets: fine.
  - All allowed anchors exist on the gazette record page.
  - Removing names from the p-0008 prose is fine, because the gazette's comps
    and locals ledgers still list them.
  - Sources that are no longer cited in prose (e.g. the Mordor market size)
    show as "on file, not cited" in the drawer, which is acceptable. They are
    not deleted.
  - Parity is unaffected (both loaders read the same body).

---

## 9. Codify after approval (NOT part of the pilot. Run only once the owner approves p-0008)

| Where | What gets written |
|---|---|
| `skills/design-language/SKILL.md` §7, §10 | The record head has no category drawing (D10). Facts column on the right: Category · Entry · Verified, no Locality, no Window (D11). The section list and order (D1). The section anatomy and the answer-line style (D2, §3.2). The keyed-list device, and that it is not an inline label. Who already sells this: strip + rows + dot glyph, Czechia first (D4). The process step table replaces the process cards (D5). The Who pays table and fold, no MoneyScale (D6). Why now keyed dates with the warm dot (D7). Difficulty is 2 lines (D8). "Suggested first moves" (D9). Section gap 120/72 (D12). NEVER list: a figure that needs a caption paragraph; a company named outside its row. |
| `web/app/lab/modern/DESIGN.md` | The same record-page values: facts column, answer line 17/26/500, keyed list 148px key column, section gap 120, strip and dot sizes, step table grid. |
| `data/RECORD-TEMPLATE.md` | A new "Writing rules for the body", from §7 rules 1–11 with p-0008's ✗/✓ pairs. The say-it-once table (§4). The allowed in-page anchors. The keyed-list grammar. The Why now keyed-date forms (`D Mon YYYY`, `Mon YYYY`, `YYYY`, `Early/Mid/Late YYYY`, `Q1–Q4 YYYY`, `H1/H2 YYYY`). The moves contract. "Where each slice lands" updated (the merged section; "Dates on file" is gone). The Figures section: map, timeline and money scale are no longer on the record page. |
| `pipeline/MATCH.md` | One short law: "Write the record for someone who has never heard of the agency or the law. Every fact has one home on the page (RECORD-TEMPLATE, say it once)." |
| `scripts/check-records.py` | New invariants, ERROR for records in a `PLAIN_PROSE_RECORDS = {"p-0008", …}` worklist and WARNING for the rest; the set is deleted once every record is rewritten: **(a)** no `comps[]`/`locals[]` name (whole word, case-sensitive, all names, minus a small common-word set such as Better, Enter, Figures, Florence) in body prose or moves; **(b)** no Act or decree numbers (`\d+/\d{4}\s*(Coll|Sb)`, `Act No.`, `vyhlášk`, `zákon č.`); **(c)** `ungloss_terms` becomes an error; **(d)** in-page link targets ∈ the allowed anchor set, and `#local-competition` requires `locals[]`; **(e)** section shape: first block is one sentence ≤25 words, other paragraphs ≤2 sentences, sentences ≤25 words, ≤1 list per section with 2–5 items, keyed keys ≤4 words, non-solutions and solved elsewhere are exactly one sentence; **(f)** Why now list is keyed, keys parse as the date forms, oldest first, every item carries a marker; **(g)** moves: 3–5 items, item 1 opener ∈ the build/contact verbs, no move opens "Sell/Pitch/Market", lead ≤12 words, ≤2 sentences, ≥1 in-page link, no `[Sn]`/amount/percent/full date; **(h)** no amount equal to a `type: price` `amount_czk` (normalised: `3,000`/`3 000`/`3k`/`about 91,000`/`9M`) in body prose; **(i)** fluff and typography: banned words (demonstrably, notably, crucially, essentially, robust, leverage, landscape, ecosystem, seamless, compelled), no `~`, ≤1 parenthesis and ≤1 dash pair per sentence, ≤2 markers per sentence; **(j)** `comps[].maturity` (below) equals `established()`. |
| `web/lib/data.ts`, `scripts/db.py` | Add `comps[].maturity` (`established`/`early`), a nullable column in `problem_comps`, mapped on the DB read path, parity green. Fill all records mechanically from `established()`: 45 of 78 comps pass today. `FieldStrip` then draws abroad maturity like Czechia's. |
| Other 28 live records | Rewrite each to the codified rules, adding it to `PLAIN_PROSE_RECORDS` as it lands (Q3). |

---

## 10. Owner questions (at most 3, each with a recommendation)

1. **In "Who already sells this", should Czechia come before Abroad?**
   *Recommend yes.* A builder asks "who would I fight here?" before "did it
   work elsewhere?", and the local row carries the teal "nobody established"
   answer.
2. **Should moves carry no receipts or figures, only links to the section that
   holds them?** *Recommend yes.* It is what removes the repetition (today move 1
   restates Lexnova, 91k CZK and Český Brod, and move 6 restates every
   competitor). The evidence is one click away.
3. **Rolling out to the other 28 records: batch right after you approve p-0008,
   or one record at a time?** *Recommend a batch right after approval*, with the
   §9 checks landing first so every rewrite is held to them by the build.
