# How the register shows its scores: options and a recommendation

*Proposal, 2026-09-17. Answers the owner's request to name the sections and the scores
the same way, taking ideabrowser.com as the model, and to consider a 1–10 scale.
**Nothing here is built.** No code, data or rulebook was edited. Already decided and
taken as given: the rail's Opportunity card becomes a **table of contents with
scores**. It lists the sections in page order, scored sections show their score, and
CSS alone highlights the current section while the reader scrolls.*

Evidence used: `SCORING.md`, `pipeline/MATCH.md` §0–1, `CLAUDE.md`, the evidence
doctrine (memory), `skills/design-language/SKILL.md` §6, §7 and §10,
`docs/record-page-redesign.md`, `web/lib/scorecard.ts`, `web/lib/data.ts`
(`urgencySplit`), `scripts/check-records.py`, the live page `/problem/cz/p-0008`
(read 2026-09-17), ideabrowser.com's idea of the day for 2026-09-17 (*Recovery Desk*,
read in full), and its previous-ideas list. Older idea pages are paywalled, so the
full ideabrowser label ladder could not be sampled. Every corpus figure below was
measured over the 29 live records (37 in total, minus 8 rejected).

---

## 0. Decision in one screen

| | A. Section scores | B. Out of 10 | C. Opportunity + Business fit |
|---|---|---|---|
| Score names | the section names | the section names | section names, in two groups |
| Scale | the rubric's own points (n/3, n/2), total n/12 | 0–10 per score, mapped from the rungs; total n/10 | as A, plus new fit rows |
| Label word | a plain phrase taken from the rung text | same as A | same as A |
| Rescoring? | **no**. Labels only, plus one mechanical field | **no**. A display mapping | **yes**, for revenue and go-to-market |
| Invents precision? | no | **yes**: 11 values drawn for 3–4 rungs, and the total loses bands | on the new rows, yes |
| Cost | small | medium, and the bands break | large, and needs evidence the register lacks |

**Recommendation: A**, with ideabrowser's three-part row (number, plain word, one-line
reason) and a front-page meter grouped by section. The exact specification is in §5.

---

## 1. What ideabrowser does, read as a reader

Its idea page (checked on 2026-09-17) shows two blocks under the pitch:

```
Opportunity 9 Exceptional    Problem 8 High Pain    Feasibility 6 Challenging    Why Now 9 Perfect Timing

Business Fit
  💰 Revenue Potential      $1M-$10M ARR potential through subscription-based ...   $$$
  🛠️ Execution Difficulty   Moderate build with wearable integrations, 2-4 week ...  5/10
  🚀 Go-To-Market           Exceptional potential with strong demand and clear ...   9/10
```

Further down the same page there are more scores: a Value Equation "9 Excellent",
A.C.P. "8/10, 9/10, 8/10", a market matrix, and keyword volume.

### What works for a reader

1. **One number per question.** No sub-scores and no fractions to read. The eye
   gets the answer from the number alone.
2. **A word next to every number.** "8" alone means little. "8 High Pain" says which
   end of the scale is good and roughly where the idea sits.
3. **A one-line reason** on the Business Fit rows. The reason ties the number to
   something about this idea ("2-4 week MVP timeline").
4. **Few questions, named the way a builder asks them.** Is the problem real? Why
   now? Can I build it? Will it make money? Can I sell it? No rubric jargon.
5. **The same four names come back** as page sections ("Why Now?", "Proof & Signals",
   "The Market Gap", "Execution Plan"), so a score leads to its explanation.

### Where it is weaker, measured against this register's rules

1. **The labels are hype.** "Exceptional", "Perfect Timing", "10x Better" and
   "Unfair Advantage" judge the idea. They do not describe evidence, and the page
   sells "Perfect Timing" twice: as a tag in the header and as the Why Now label.
   `SKILL.md` §10 rule 11 exists to keep exactly this off our pages.
2. **The numbers are not tied to evidence.** Nothing on the page says what a 9 would
   need, or what would make it an 8. The site says so itself. Its footer calls the
   scores "educational and based on assumptions" and the revenue figures
   illustrative. The register's one claim to be better than a chatbot is that every
   point has a receipt (`SCORING.md`: no source, no point).
3. **One field, two meanings, on their own page.** Feasibility 6 "Challenging" and
   Execution Difficulty 5/10 "Moderate" both answer "how hard is it to build?", with
   different numbers, different words and no stated polarity. Go-To-Market 9/10
   restates demand ("strong demand") that Problem already scored. This is the defect
   `MATCH.md` §0 records four times.
4. **Scales are mixed.** A number with a word, n/10, and "$$$" all sit in one block.
5. **Score inflation.** A 1–10 scale with no written rungs drifts to 6–9, because
   nothing stops it. The rest of that page reads 9, 8, 9, 8, 9, 9.

**What to take from it:** the row shape (name, number, word, reason), names that are
builder questions, and names that match the sections. **What to leave:** judgment
adjectives, unanchored 1–10 numbers, and several numbers for one question.

---

## 2. The constraints any option must meet

These come from this repo, not from taste. Each one rules something out.

**C1. "Who already sells this" holds two scores with opposite signs.** Validated
abroad (`proof`) and Local opportunity (`gap`) both apply the established test, but an
established player is good news abroad and bad news in Czechia (`SCORING.md`,
`MATCH.md` §1). **Merging them into one "Competition" number would put two meanings in
one field.** A merged number can't say whether a 1 means "nothing proven abroad" or
"taken at home". So the section keeps **two scored lines, Abroad and In Czechia**.
"One score per section" is therefore true for four sections and false for this one.

**C2. "Who pays" is not what `money` measures.** The rung measures how close a
*public budget* is, and never who pays (owner ruling, 2026-09-03). A bare "Who pays
2/2" would bring back the over-claim the owner removed. **The label under it must
always say public money and "nearby".** This is the one place where matching the
names leaks meaning, and the label word is what stops the leak.

**C3. "Why now" is one stored number with two meanings.** `scores.urgency` (0–3) is
the sum of `deadline` (0–2, a forcing date) and `freshness` (0–1, the newest source is
under 90 days old). Only the sum is stored. `urgencySplit()` in `web/lib/data.ts`
re-derives the parts at render time from source dates. Measured today:

- **Freshness is 1 on all 29 live records.** A check that every record passes carries
  no information, the same argument `SCORING.md` makes against "a company exists".
- **13 of 29 live records score urgency 1 on freshness alone**, with no dated trigger
  (p-0001, 0002, 0003, 0004, 0005, 0007, 0009, 0011, 0026, 0027, 0031, 0032, 0033).
  Their "Why now 1/3" means "we looked recently", not "the timing is right".
- Freshness is measured against the register's newest `updated` date and decays,
  while the stored sum does not change. After 90 days without new sources,
  `urgencySplit` gives the point to `deadline`. A label read from `deadline` would
  then print "Deadline over 18 months out" on a record that has no deadline.

So **no option may put a timing word on Why now until the deadline part is stored and
checked.** §5.4 gives the fix: a mechanical field, plus the deadline date and its
source named on 16 records.

**C4. Only two of the five rungs are checked by script today.** `check-records.py`
compares `proof` with `comps[]` (the established test) and `gap` with `locals[]` plus
the gap-check. `money` and `demand` have no invariant against their ledgers, and
`urgency` has none apart from the sum. A label word therefore carries the checker's
authority on Abroad and In Czechia, and only MATCH's judgment on the other three. That
is no worse than the number shown today, but a label reads as a claim, so §5.4 adds
the Why now check. Money and demand stay as they are, recorded as a known gap.

**C5. Say it once.** `record-page-redesign.md` §4 gives a score or rung one home: the
rail. A score repeated inside every section heading breaks that rule, except where the
rail isn't beside the heading (≤1080px, where the rail drops below main).

**C6. `SKILL.md` §10 rule 16.** Never restate `SCORING.md` vocabulary in different
words. **Any label word must therefore be written into `SCORING.md` first**, and the
build must check it word for word, as `assertScoringVocabulary()` already does for the
verdict words.

---

## 3. The options

In all options the page order is the same, and so is the TOC:
The problem · Suggested solution · Who already sells this (Abroad, In Czechia) ·
Who pays · Why now · Difficulty to enter · Suggested first moves.
The mockups use p-0008's real scores (proof 3, gap 1, demand 2, money 2, urgency 3 =
deadline 2 + freshness 1, entry Hard). The reason lines are built the way
`scoreRead()` builds them today, from p-0008's ledgers.

### Option A: Section scores, rubric points, plain rung labels

**Names**, one to one with the sections:

| Section | Scored line | Field | Scale |
|---|---|---|---|
| The problem | The problem | `demand` | /2 |
| Who already sells this | Abroad | `proof` | /3 |
| Who already sells this | In Czechia | `gap` | /2 |
| Who pays | Who pays | `money` | /2 |
| Why now | Why now | `urgency` | /3 |
| Difficulty to enter | level word, no number | `entry.level` | Easy · Moderate · Hard · Very hard |

**Scale:** the rubric's points, unchanged (n/max), and the total n/12. Bars stay as
segments, one per point, so a /3 visibly has three steps.

**Label words:** one short phrase per rung, taken from the rung's own text (§5.2).
They describe what is on file, never how good it is. No "Exceptional", no
"Perfect".

**Reason line:** one line under the label, built from the ledger (counts, never
company names, per C5 and the say-it-once table), plus the number of sources behind
it. Example: "2 companies abroad, established across several markets · 3 sources".

**Total:** "Opportunity 11/12" with no adjective, and under it a line that can be
counted: "4 of 5 checks full". Bands stay number ranges ("10–12") on the front page.

**Rail (TOC) mockup, desktop:**

```
┌──────────────────────────────────────────┐
│ Opportunity                        11/12 │
│ 4 of 5 checks full                       │
│──────────────────────────────────────────│
│ The problem                  ▮▮     2/2  │
│   Documented, recurring                  │
│ Suggested solution                       │
│▌Who already sells this                   │  ◀ current section: bar + text-1
│▌  Abroad                     ▮▮▮    3/3  │
│▌  Established in 2+ markets              │
│▌  In Czechia                 ▮▯     1/2  │
│▌  Early sellers only                     │
│ Who pays                     ▮▮     2/2  │
│   Open or recurring public money nearby  │
│ Why now                      ▮▮▮    3/3  │
│   Deadline within 18 months              │
│ Difficulty to enter           ● Hard     │
│ Suggested first moves                    │
└──────────────────────────────────────────┘
  reason lines live in each row's ladder tooltip (hover/focus), as today
```

**Section heading, desktop (rail beside it): unchanged, no score** (C5):

```
Why now
Small towns, care homes and firms covered by the new cybersecurity law start
running out of time in late 2026, and ...
```

**Section heading, ≤1080px (rail below main): one quiet chip**, in the meta style,
linking down to the rail:

```
Why now                                        3/3 · Deadline within 18 months
```

**Front-page row meter:** still 12 segments, now **grouped in page order** with a 4px
gap between groups, so the reader can see which checks are full, not only how many:

```
now:     ▮▮▮▮▮▮▮▮▮▮▮▯  11/12
A:       ▮▮ ▮▮▮ ▮▯ ▮▮ ▮▮▮  11/12
         │  │   │  │  └ Why now
         │  │   │  └ Who pays
         │  │   └ In Czechia
         │  └ Abroad
         └ The problem
```

The row's hover card lists the same rows as the rail in page order, with label words.

---

### Option B: A 0–10 display per score, mapped from the rungs

**Names:** as in A. **Label words and reason lines:** as in A.

**Scale:** each rung maps mechanically to a number out of 10:
`display = round(10 × rung ÷ max)`, rounding halves up.

| Ladder | Rung → display |
|---|---|
| /3 (Abroad, Why now) | 0 → 0 · 1 → 3 · 2 → 7 · 3 → 10 |
| /2 (The problem, In Czechia, Who pays) | 0 → 0 · 1 → 5 · 2 → 10 |
| Total /12 | 12→10 · 11→9 · **10→8 · 9→8** · 8→7 · 7→6 · 6→5 · 5→4 · **4→3 · 3→3** · 2→2 · 1→1 · 0→0 |

It has to be **0–10, not 1–10.** A 1–10 scale would show rung 0 ("nothing on file")
as 1. That is a point with no source, which `SCORING.md` forbids.

**Rail mockup:**

```
┌──────────────────────────────────────────┐
│ Opportunity                       9 / 10 │
│──────────────────────────────────────────│
│ The problem                          10  │
│   Documented, recurring                  │
│ Suggested solution                       │
│▌Who already sells this                   │
│▌  Abroad                             10  │
│▌  Established in 2+ markets              │
│▌  In Czechia                          5  │
│▌  Early sellers only                     │
│ Who pays                             10  │
│   Open or recurring public money nearby  │
│ Why now                              10  │
│   Deadline within 18 months              │
│ Difficulty to enter           ● Hard     │
│ Suggested first moves                    │
└──────────────────────────────────────────┘
```

**Heading chip (≤1080px):** `Why now      10 · Deadline within 18 months`

**Front-page meter:** 10 segments, `▮▮▮▮▮▮▮▮▮▯  9/10`.

---

### Option C: "Opportunity" and "Business fit"

**Opportunity** (the five scored lines of A, total n/12) sits above **Business fit**,
which copies ideabrowser's second block. What the register has evidence for today:

| Ideabrowser row | Register equivalent | Evidence today |
|---|---|---|
| Execution Difficulty | **Difficulty to enter** (`entry.level`) | **Yes, on all records.** Derived from gates and checked by script. It is feasibility, not opportunity, so it already sits outside the 12 points (`SCORING.md`). |
| Revenue Potential | **What one buyer pays** (`type: price` receipts) | **Partly.** 13 of 29 live records have a price receipt and 16 have none. A receipt is one buyer's price, not a market size. A "$$$" or ARR band would need a count of buyers × price, and only **2 of 29** live records hold both a `statistic` and a `price` source. It would also be a new ladder, a new judgment and new invariants. |
| Go-To-Market | nothing | **No.** No field, source type or ingest records how a builder reaches buyers. Scoring it today would be the plausible-without-receipt claim the register exists to avoid (evidence doctrine). |

**Rail mockup** (fit rows shown only where evidence exists):

```
┌──────────────────────────────────────────┐
│ Opportunity                        11/12 │
│   The problem                ▮▮     2/2  │
│   Who already sells this                 │
│     Abroad                   ▮▮▮    3/3  │
│     In Czechia               ▮▯     1/2  │
│   Who pays                   ▮▮     2/2  │
│   Why now                    ▮▮▮    3/3  │
│ Business fit                             │
│   Difficulty to enter         ● Hard     │
│   One buyer pays         121,000 CZK     │  ← absent on 16 of 29 records
│   (no go-to-market row: nothing on file) │
│ Suggested solution · Suggested first moves│
└──────────────────────────────────────────┘
```

This **breaks the TOC decision**: grouping by kind takes the rows out of page order,
and "One buyer pays" belongs to the Who pays section, so the price would appear twice.

**Heading chip:** as in A. **Front-page meter:** A's grouped meter, plus the entry dot
and word after it (`▮▮ ▮▮▮ ▮▯ ▮▮ ▮▮▮ 11/12 · ● Hard`).

---

## 4. Integrity check and migration cost

### 4.1 Integrity

| Question | A | B | C |
|---|---|---|---|
| **One field, one meaning?** | Holds, **if** Who already sells this keeps two lines (C1), the Who pays label says public money nearby (C2), and Why now words read the stored deadline part only (C3). | Same as A. It also adds a quieter problem: the page implies that "Abroad 10" and "Who pays 10" can be compared, but they sit on 4-rung and 3-rung ladders. | Rows as in A. Revenue potential and go-to-market would each need a new field with its own meaning. That is legitimate only once receipts exist. |
| **Invented precision?** | None. The number *is* the rung. | **Yes.** It shows 0–10, but a score can only take 3 or 4 of those values. A reader takes "7" to mean 70% and "5 vs 7" as a real gap. The total is worse: **9 and 10 both show 8, and 3 and 4 both show 3.** The band edge 10–12 / 8–9 therefore can't be drawn on the /10 scale at all. The two displayed totals also disagree: on **9 of 29** live records, averaging the five /10 numbers gives a different total from rescaling the sum (p-0028: 9/12 → 8, but the five displays average to 7). The mapping makes no new judgment, but it prints more precision than the rungs have. | Revenue and go-to-market numbers would be new, unreceipted judgments today. |
| **Do labels become verdict words?** | No, if the rules in §5.2 hold. The words are taken from the rung text, written into `SCORING.md`, checked word for word, and describe what is on file ("Early sellers only"), not quality ("Challenging"). No adjective on the total. | Same as A. The bigger risk in B is that a bare 10 reads as "perfect" anyway. | A label like "$$$" is a verdict with no rung behind it. |
| **Difficulty to enter** | Stays a level word with its dot, in the TOC, with no number and outside the total, as `SCORING.md` requires. | Same. Resist "Difficulty 5/10": the level is derived from gates and has four values, not ten. | It becomes the anchor of Business fit, which is correct, but the fit group is one row plus a partial ledger today. |

### 4.2 Migration cost

| Item | A | B | C |
|---|---|---|---|
| Record scores | **No rescoring of the 12 points.** One mechanical field (`scores_detail.deadline`, equal to `urgency − 1` on every live record today), plus a short MATCH pass naming the deadline date and source on the 16 records with deadline ≥ 1 (§5.4). That pass may correct some deadline rungs. | No rescoring. The same deadline work. | New fields on all 29 records (buyer count, go-to-market receipts). That is new MATCH research, i.e. rescoring. |
| `SCORING.md` | Add a `labels` line under each ladder (replacing the `verdicts` line), plus one paragraph: public names are the section names. Bands stay. | A, plus the mapping table, and a ruling on bands. The /10 total can't separate 9 from 10, so the thresholds must move (a rubric change) or bands stay on /12 (two scales on one site). | A, plus two new ladders with rungs and receipts. |
| `check-records.py` | Deadline invariant (§5.4), WARNING first. Label checks run in the web build. | A, plus an assertion that display = mapping (trivial). | A, plus invariants for each new field, in the same change (CLAUDE.md rule 2). |
| `web/lib/scorecard.ts` | `SCORE_ROWS` → TOC rows in page order with anchors. `READS`/`VERDICTS` → `LABELS` read from `SCORING.md`. `scoreRead` stops naming companies. `criterion()` for urgency reads the stored deadline, not `urgencySplit`. | A, plus the mapping function. | A, plus fit rows. |
| Record page rail | TOC (already decided) with label lines, and a heading chip at ≤1080px. | Same, /10 numbers. | Two groups, out of page order. |
| Front-page meter (`web/lib/site/front.tsx`, `DESIGN.md` "Opportunity meter") | Group the 12 pips into 5 groups in page order. The hover card goes in page order. | 10 pips, and the grouping rail's bands ("Opportunity 10–12 …") need new ranges. | A, plus the entry word. |
| `SKILL.md` §6 | Meter: grouped by check, page order. The hover card goes in page order, not most-filled first. | Meter: 10 segments, bands on /10. | A, plus the entry dot on the row. |
| `SKILL.md` §7 | The rail becomes the TOC in page order, and "sorted most-filled first" is deleted. Add the ≤1080px heading chip. | Same. | Same, plus the fit group. |
| `SKILL.md` §10 rule 11 | Reword: "NEVER a band verdict word (PRIME, STRONG, …) or a judgment adjective (Exceptional, Perfect, Strong). A rung label from `SCORING.md` `labels`, verbatim, is allowed." | Same. | Same, and the fit rows fall under it too. |
| `SKILL.md` §10 rule 16 | Unchanged. It now covers the labels, which is the point. | Same. | Same. |
| Other | `record-page-redesign.md` §4 (a score's home: rail, plus the chip at ≤1080px). The `RECORD-TEMPLATE.md` comments on `scores:`. The string lists in `web/lib/site/sources.ts`, `web/lib/figures/field.tsx` and `web/lib/figures/money.tsx`. How it works copy. `npm --prefix web run parity`. | A, and How it works has to explain the mapping. | A, plus `MATCH.md` laws and new ingest for go-to-market evidence. |
| **Size** | **About one work package**, plus the deadline-date pass on 16 records. | One and a half, plus a band decision. | Several, and blocked on research. |

---

## 5. Recommendation: Option A, specified

### 5.1 Names and order (TOC = page order)

| # | TOC row (section) | Scored line | Field | Max | Anchor |
|---|---|---|---|---|---|
| 1 | The problem | The problem | `demand` | 2 | `#the-problem` |
| 2 | Suggested solution | none | | | `#suggested-solution` |
| 3 | Who already sells this | **Abroad** | `proof` | 3 | `#who-already-sells-this` |
| 3 | (same) | **In Czechia** | `gap` | 2 | `#who-already-sells-this` |
| 4 | Who pays | Who pays | `money` | 2 | `#who-pays` |
| 5 | Why now | Why now | `urgency` | 3 | `#why-now` |
| 6 | Difficulty to enter | level dot + word | `entry.level` | none | `#difficulty-to-enter` |
| 7 | Suggested first moves | none | | | `#first-moves` |

Use whichever anchors the page already renders. Check `page.tsx` before building,
because the legacy aliases (`#proven-abroad`, `#local-competition`) are still linked
from prose.

Top of the card: **"Opportunity n/12"**, then **"k of 5 checks full"**, where k counts
scores at their maximum. No band word and no adjective.

### 5.2 Label words: the rung table to write into `SCORING.md`

Rules for any future edit: **(1)** the phrase is taken from the rung's own words, not
from a judgment of the idea. **(2)** At most 5 words. **(3)** No quality adjective
(exceptional, strong, perfect, high, great, promising). **(4)** Rung 2 of In Czechia
says "checked", because that rung costs a gap-check with a positive control.
**(5)** It renders verbatim, sentence case, never uppercase.

| Line | Rung 0 | Rung 1 | Rung 2 | Rung 3 | Taken from (`SCORING.md`) |
|---|---|---|---|---|---|
| The problem (`demand`) | Pain assumed | Scattered complaints | Documented, recurring | | "assumed · scattered complaints · recurring documented complaints, petition, or industry pressure" |
| Abroad (`proof`) | None on file | Early players only | One established player | Established in 2+ markets | "no foreign solution on file · EARLY foreign players only · one ESTABLISHED foreign player · ESTABLISHED in 2+ markets" |
| In Czechia (`gap`) | Established seller here | Early sellers only | Checked: nobody sells this | | "at least one … direct AND established · … all are EARLY · checked, and NO local sells this" |
| Who pays (`money`) | No public money on file | Tender or grant nearby | Open or recurring public money nearby | | "none · relevant tender/grant exists · OPEN tender or grant ≥ ~5M CZK, or recurring annual spend" plus the 2026-09-03 "nearby" ruling |
| Why now (`urgency`), **read from `deadline` only** | No dated trigger | Deadline over 18 months out | Deadline within 18 months | | "no regulatory trigger · compliance date >18mo out · compliance date <18mo" |

The brief's example "Deadline within a year" is **not** the rung. The rung is 18
months, and rule 16 forbids rewording it. Freshness gets no word of its own. Its point
is stated in the Why now tooltip, "+1: a source dated in the 90 days before this
record was verified", until owner question 3 is settled.

**Difficulty to enter** keeps Easy · Moderate · Hard · Very hard (CONVENTIONS.md) and
no number.

### 5.3 Reason line (tooltip body and ≤1080px fold)

This is today's `scoreRead()`, with three changes: **(a)** no company names; say "4
local players sell this, all still early", not "Lexnova …" (say-it-once). **(b)** It
ends with the number of sources behind the line, from `dimRefs()`: "· 3 sources".
**(c)** The Why now line reads the stored deadline (§5.4), never `urgencySplit`. The
existing ladder tooltip stays: what the check asks, the rungs with this record's rung
highlighted, then "This record: … n of max."

### 5.4 The one data change: store the deadline part

```yaml
scores:
  urgency: 3
scores_detail:
  deadline: 2              # 0 no regulatory trigger · 1 >18mo · 2 <18mo  (SCORING.md URGENCY)
  deadline_on: 2026-12-31  # REQUIRED when deadline ≥ 1: the compliance date the rung reads
  deadline_ref: 4          # REQUIRED when deadline ≥ 1: the S-number that states that date
```

- **Fill, part 1 (mechanical):** `deadline = urgency − 1` on every live record today
  (freshness is 1 on all 29, and `urgencySplit` agrees on every record). For the 8
  rejected records, use `urgencySplit`'s value.
- **Fill, part 2 (not mechanical, a short MATCH pass):** `deadline_on` and
  `deadline_ref` for the 16 live records with deadline ≥ 1. **The deadline isn't
  receipted in a checkable form today.** A rough census on 2026-09-17 looked for a
  `type: regulation` or `dims: [urgency]` source dated after `updated`, at the
  distance the rung needs. It found none on **12 of those 16** (p-0006, 0010, 0022,
  0023, 0024, 0025, 0028, 0030, 0034, 0035, 0036, 0037). On p-0037, a deadline-1
  record, it found dates within 18 months, which would point to rung 2. The parse was
  rough (the date may sit in a `news` source or in prose), so treat the list as the
  worklist, not as findings. The point stands anyway: until the date is named, "Deadline
  within 18 months" is a label no script can hold to its receipt. If a record can't
  name its date, its deadline rung is wrong. That's a MATCH correction, not a display
  problem.
- **Invariants** (`check-records.py`, **WARNING first**; they become ERROR once the
  census is clean, so the check isn't crying wolf):
  1. `0 ≤ urgency − deadline ≤ 1`. The freshness point cannot exceed 1.
  2. `deadline ≥ 1` requires `deadline_on` and `deadline_ref`, and `deadline_ref`
     must be an existing source.
  3. The rung must match the date: `deadline = 2` ⇔ `deadline_on` is after `updated`
     and within 18 months of it; `deadline = 1` ⇔ more than 18 months out.
  4. Plant one violation of each and watch it fail before merging (doctrine: a check
     never shown to fail is not evidence).
- **Web:** `criterion()` and the Why now label read `scores_detail.deadline`, and
  `urgencySplit` is retired from the display. `registerRows()` tie-breaks on the
  stored deadline.

Scores, totals, bands and ordering stay the same, except where the MATCH pass finds a
deadline rung its own date doesn't support. Such a fix is a correction, published as
one.

**Build order:** the Abroad, In Czechia, The problem and Who pays labels can ship as
soon as `SCORING.md` carries them. The Why now label ships only after the deadline
invariants are clean. Until then, the Why now line shows "n/3" with no label word.

### 5.5 Front page

- The meter keeps 12 pips at 4×8px, **grouped 2 · 3 · 2 · 2 · 3 in page order** (The
  problem, Abroad, In Czechia, Who pays, Why now), with a 4px gap between groups and
  the usual 1px gap inside a group. Each group fills from its left edge. Then "n/12".
- The hover card reads "Opportunity n of 12", then the five lines **in page order**,
  each with mini bar, n/max and label word.
- The grouping rail stays numeric ("Opportunity 10–12").

### 5.6 Rulebook edits, for the implementation agent

`SCORING.md` (labels, and the deadline field paragraph) · `data/RECORD-TEMPLATE.md`
(`scores:` comments → the new public names; `scores_detail`) · `SKILL.md` §6
(meter), §7 (rail = TOC, heading chip), §10 rule 11 (wording in §4.2) ·
`web/app/(site)/DESIGN.md` (meter grouping, rail rows) ·
`docs/record-page-redesign.md` §4 (a score's home) · `scripts/check-records.py`
(§5.4) · `web/lib/scorecard.ts` (build-time assertion extended to `LABELS`). Gates:
`npm --prefix web run build`, then `npm --prefix web run parity`.

---

## 6. Owner questions (at most 3, each with a recommendation)

1. **Out of 10, or the rubric's own points?** *Recommend the rubric's points (n/3,
   n/2, total n/12).* The clarity you liked on ideabrowser comes from the word and the
   reason next to each number, and A has both. A 0–10 display prints values the rungs
   can't produce. It shows 9/12 and 10/12 both as 8, so it can't draw the 10–12 / 8–9
   band edge. On 9 of 29 records it also gives two different totals, depending on
   whether a reader averages the rows or rescales the sum.

2. **Should the total carry a word, like ideabrowser's "Opportunity 9 Exceptional"?**
   *Recommend no adjective.* Use a line that can be counted instead: "Opportunity
   11/12 · 4 of 5 checks full". The total adds up five different questions, so any
   single word claims more than the sum can back, and verdict words were removed from
   public pages for that reason.

3. **Should freshness stay inside Why now?** *Recommend: this change stores the
   deadline part and labels Why now from it alone; freshness leaves the 12 points in
   a separate rubric change.* Every live record scores the freshness point today, so it
   separates nothing. On 13 records it is the *only* Why now point, which makes "Why
   now 1/3" mean "we looked recently". The Verified date in the facts column already
   says that. Removing it makes the total /11 and moves the bands, so it deserves its
   own decision.
