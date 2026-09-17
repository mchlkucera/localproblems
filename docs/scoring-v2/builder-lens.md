# Scoring v2, the builder and reader lens

*Written 2026-09-17. This is one of three independent takes on the owner's scoring direction
of the same day. It asks two questions: do the scores answer what a founder, indie hacker or
small agency asks when choosing a problem, and can a reader take them in at a glance?
**Nothing here is built.** No code, data or rulebook was edited.*

Read for this: `SCORING.md`, `docs/scoring-presentation-options.md` (the earlier Option A
proposal), `docs/record-page-redesign.md` (since deleted; its rules now live in
`skills/design-language/SKILL.md` §7), the live page `/problem/cz/p-0008` (read
2026-09-17), and `data/problems/cz/p-0008-*.md`. Outside sources are listed in §7.

---

## 0. Recommendations on one screen

| # | Recommendation |
|---|---|
| R1 | **Keep five summed scores, all pointing the same way, still out of 12.** The problem (pain) /2 · Who pays /2 · Why now /3 · Proven abroad /3 · Market gap /2. |
| R2 | **Execution difficulty gets a scored rung (a level word) but stays out of the total.** It is the effort side of the decision, and it depends on who the reader is. It sits next to the total instead: "11/12 · Hard to enter". |
| R3 | **Separate the three demand questions by the kind of evidence each accepts.** People *say* it hurts (pain). People *pay* for it or for a workaround (who pays). A *dated* event forces the purchase now (why now). One piece of evidence earns one point. |
| R4 | **Money becomes "Who pays: is anyone paying today?"** Public money is the *reason* a buyer can pay. It goes in the reason line and never earns a point by itself. A public tender that buys this product *is* a payment, so it counts. |
| R5 | **"Competition" is renamed "Market gap"** so that more always means better on every summed row. Difficulty needs no renaming, because its word ("Hard") already shows which way is good. |
| R6 | **Short judgment words, taken from `SCORING.md`'s own verdict ladder where one exists**, in sentence case, plus a reason line. There is no word like "Exceptional" or "Perfect". |
| R7 | **The total carries a plain band word and "the catch"**, meaning the weakest summed score in words. |
| R8 | **Section order: swap Why now and Who pays.** Keep Proven abroad and Market gap next to each other, because together they tell the arbitrage story. |

---

## 1. Coverage: do these scores answer the builder's questions?

### 1.1 What a builder asks, and where each framework asks it

| Builder's question | YC (Friedman's 10 / PG) | Mom Test | Lean Canvas | ideabrowser | Owner's v2 | Verdict |
|---|---|---|---|---|---|---|
| Is the pain real and sharp? | "How acute is this problem?" | past behaviour, not opinions | Problem | Problem "8 High Pain" | The opportunity | **Covered** |
| Will anyone pay? | proxies | **commitment: time, reputation, money** | Revenue streams | Revenue Potential "$$$" | Money available (to rethink) | **Covered once redefined (R4)** |
| Why now? | "recently become possible or necessary?" | | | Why Now "9 Perfect Timing" | Why now | **Covered** |
| Has someone proven the model? | "good proxies for this business" | | | Proof & Signals | Validated abroad | **Covered** |
| Who's already here? | "Do you have competition?" | | Existing alternatives | The Market Gap | Competition | **Covered** |
| Can I get in? | "hard to get started" (a *good* sign) | | Unfair advantage | Feasibility, Execution Difficulty | Execution difficulty | **Covered** |
| How big is it? | "How big is the market?" | | Customer segments | Revenue Potential, keyword volume | none | **Missing: show as a fact, don't score it** |
| Who is my first customer, and can I reach them? | "who wants this right now?" (PG) | "who to talk to first" | Early adopters, Channels | Go-To-Market 9/10 | Suggested first moves | **Partly: make it required in the moves** |
| Is this for me? | founder–market fit | | | "Right for You?" | "Good for" (head) | **Covered, and not scored (owner: not business fit)** |

### 1.2 What's missing, and what to do about each

1. **Size (how many buyers).** Builders always ask it, but it should not be a score here.
   There are three reasons. The register can't back it: 2 of 29 live records hold both a
   `statistic` and a `price` source (`scoring-presentation-options.md` §3C). It also
   favours big and shallow over narrow and deep, and Paul Graham argues for the opposite:
   "something a small number of people want a large amount". And an indie hacker and an
   agency want different sizes. **Recommendation: one required, sourced fact line at the
   top of The problem, "Buyers: about 6,000 covered organisations [S]".** p-0008 already
   has it in prose. It gets no points and no word.
2. **A reachable first customer.** This is the most practical question, and today it is
   implicit. **Recommendation: no score. Suggested first move 1 or 2 must name a buyer type
   that can be found in a public list** (the contract register, the business register, a
   sector association) and link to where the evidence is. p-0008's move 2, "Call the
   directors of care homes and small towns that are already paying…", already does this.
   The `entry.buyer` gate already prices how hard that buyer is to sell to.
3. **Price per buyer.** This matters because it decides whether the problem suits an indie
   or an agency. It already has a home, the "What one buyer pays" table under Who pays.
   Keep it there as a fact. It is not a separate score.

Deliberately **left out**: revenue potential (ARR bands), a go-to-market score, and
scalability. None of them has receipts, and the owner said "not business fit".

### 1.3 What overlaps, and how to separate the pairs that are "related but not the same"

**The demand triangle.** The owner's text puts demand in three places. The opportunity
"should also explain the demand signal". Why now asks "if there's anything supporting that
there's demand NOW". Money asks "are people willing to pay right now". Without a rule, one
wave of tenders would earn three points. The Mom Test gives the dividing line: *what people
say* is weak evidence, and *what they give up* (time, reputation, money) is strong. So the
three scores are split by **what kind of evidence each one accepts**:

| Score | The question, as shown to the reader | Accepts | Never accepts |
|---|---|---|---|
| **The problem** (pain) | *Do the people who have it say it hurts?* | complaints, petitions, association alarms, surveys, press | payments; dates |
| **Who pays** | *Is anyone paying today, for this or for a workaround?* | price receipts, contracts, tenders **for this product or its manual equivalent** | grants on their own, budgets, complaints |
| **Why now** | *Is there a real deadline, and are buyers moving because of it?* | a dated trigger (law in force, grant close, ban date) plus a **dated rise** in buying since that trigger | a single purchase (that belongs to Who pays); "we checked recently" |

**The rule, which the checker enforces:** a source earns a point on at most one of these
three rows. A contract proves payment. A *count of contracts over time, measured since the
trigger*, proves timing, and it needs its own statistic or query source.

**Freshness goes away.** The owner said "not recently checked". It is 1 on all 29 live
records today, so it separates nothing. On 13 records it is the only Why now point. The
Verified date in the facts column already says when the record was checked.

**Abroad and here.** Both use the established test with opposite signs. The names separate
them by **place and by direction**: *Proven abroad* (someone established sells it there,
which is good) sits right above *Market gap* (nobody established sells it here, which is
good). Read one after the other, they are the register's core pitch: it works there, and
it's open here.

**Market gap and Difficulty.** These are already separate, because `entry.incumbents` carries
no weight in the difficulty level (`SCORING.md`). Keep it that way.

**Public money and Who pays.** A grant is a subsidy. It makes a purchase more likely but is
not a purchase. It goes in the reason line ("an EU grant pays half for towns"). A tender
that buys this product is a buyer paying, so it counts toward Who pays.

---

## 2. Naming

### 2.1 Names, questions and judgment words

Rules for the words: at most 3 words, sentence case, no quality adjective about the *idea*
("Exceptional", "Perfect", "Great"). Words about the *evidence* are allowed ("Documented",
"Firm"). Where `SCORING.md` already has a verdict for a rung, reuse it in sentence case
(its rule 16: never restate the vocabulary in different words). New rungs get new words,
and those words go into `SCORING.md` first.

| Row (TOC and section name) | Max | Rung 0 | Rung 1 | Rung 2 | Rung 3 | ideabrowser equivalent |
|---|---|---|---|---|---|---|
| **The problem**, scored as pain | 2 | Assumed | Scattered | Documented | | Problem "8 High Pain" |
| **Who pays** | 2 | No payer found | Pays workarounds | Paying now | | Revenue Potential "$$$" |
| **Why now** | 3 | No deadline | Soft deadline | Firm deadline | Pressing | Why Now "9 Perfect Timing" |
| **Proven abroad** | 3 | None | Early | Established | Validated | Proof & Signals (not scored) |
| **Market gap** | 2 | Taken | Contested | Open | | The Market Gap (not scored) |
| **Difficulty to enter** (not summed) | | Easy | Moderate | Hard | Very hard | Feasibility "6 Challenging", Execution Difficulty "5/10" |

What the new or changed rungs mean:

- **Who pays.** 0: no receipt shows anyone paying. 1: buyers pay for a workaround (a
  consultant, a manual service, staff time with a price) or for an adjacent product, with a
  `type: price` or contract receipt. 2: a named buyer paid for **this product or its direct
  equivalent**, with a price receipt, contract or awarded tender dated within 24 months.
  *Why workarounds get a point:* "they already pay a consultant 121,000 CZK to do this by
  hand" is the strongest demand evidence a builder can get, and it is rung 1, not rung 0.
- **Why now** (freshness removed). 0: no dated trigger. 1 *Soft*: a trigger exists but isn't
  binding yet (a draft law, a date more than 18 months away, or no named penalty). 2 *Firm*:
  a binding date in force, within 18 months, with a named penalty or cutoff. 3 *Pressing*:
  Firm, plus a dated rise in buying since the trigger (for example, tenders citing the law
  in the last 6 months). "Soft / Firm" answers the owner's "how real is the deadline".
  "Pressing" answers "demand NOW".
- **Proven abroad** keeps the current rungs. "Validated" is `SCORING.md`'s existing rung-3
  verdict, and it matches the owner's own word.
- **Market gap** keeps the current rungs and reuses `SCORING.md`'s verdicts verbatim.

### 2.2 Low = good: invert the name, or keep it?

What goes wrong in practice: a reader sees **"Competition 2/2"** and a full bar next to
four rows where full means good, and reads it as "heavy competition". The row actually
means "nobody sells this, checked". ideabrowser shows the same risk on its own page, with
"Feasibility 6 Challenging" next to "Execution Difficulty 5/10" and neither saying which
way is good.

The fix depends on whether the number is added into the total:

- **Market gap (summed): invert the name.** Any summed row whose full bar means "bad" will be
  misread. "Market gap" is the builder's own term, ideabrowser uses it as a section heading,
  it matches the stored field (`gap`), and more always means better. The section still
  answers the owner's competition question. Its answer line names who sells locally, and its
  tooltip says: *"Is an established Czech company already selling this? Fewer is better,
  so the score counts the gap."* Don't use the live label "Local opportunity": it clashes
  with the total's name.
- **Difficulty to enter (not summed): keep the name, show a word, not n/max.** "Hard" can't
  be misread. The problem only appears when a number is involved. Show it with the existing
  dot, not the teal pips (in `DESIGN.md`, teal means "in the builder's favour"), and never
  as "2/3". If the owner does want it added into the total, invert it to **"Ease of entry"**
  (very hard 0 · hard 1 · moderate 2 · easy 3) with the words unchanged. That makes the
  total /15 and moves the bands. See Q2.

---

## 3. The total

**Keep one total, over the five summed rows only, out of 12.** Builders expect a single
number to sort by, and the front page already sorts on it. Difficulty stays out because it
is the other axis. Prioritisation frameworks such as RICE put effort in the *denominator*,
not in the sum. It also depends on the reader: p-0008 is Hard for a solo founder, but
closer to Moderate for an agency with public-sector references. If difficulty were summed,
a hard, strong problem would look average and an easy, weak one would look fine.

**How it reads** (the record rail and the row hover card):

```
Opportunity 11/12 · Strong
Hard to enter · The catch: early local sellers
```

- **Bands**, keeping today's edges: 10–12 **Strong** · 8–9 **Good** · 5–7 **Mixed** · 0–4
  **Weak**. These are plain words, not PRIME or STRONG in capitals. This goes against
  `SKILL.md` §10 rule 11 ("never a verdict word"), so the owner's "judgement words but
  reasonable" needs to amend that rule explicitly.
- **The catch** is the summed row with the lowest share of its maximum (ties go to page
  order), in its own judgment word. If every row is full, the line is left out. This gives
  the weakest link without a second number. A builder reads a total to find out what's
  wrong with the idea, and this line tells them.
- **Alternative considered: weakest link only, with no total.** It's more honest about
  adding up different questions. But it breaks sorting, and it makes a 0 on one row look
  like a 0 overall. Rejected, although the catch line keeps the useful part of it.

---

## 4. Glance test, p-0008 under this naming

p-0008 rescored with the v2 ladders, reading its own sources:
- **Pain 2.** An SME association alarm and documented unawareness.
- **Who pays 2.** Český Brod paid about 9M CZK for municipal security work. A care home paid
  about 91,000 CZK for a package.
- **Why now 3.** Act 264/2025 has been in force since 1 Nov 2025, the one-year deadlines
  run out in late 2026, and there is a fine. That is Firm. About €33M of security tenders
  landed in June–August 2026, which makes it Pressing.
- **Abroad 3.** Secfix (DE) and Copla (LT).
- **Gap 1.** Four early Czech sellers.

The total is unchanged at **11/12**.

### 4.1 Rail (table of contents), desktop

```
┌───────────────────────────────────────────────┐
│ Opportunity                    11/12 · Strong │
│ Hard to enter · The catch: early local sellers│
│───────────────────────────────────────────────│
│ The problem        ▮▮   2/2   Documented      │
│ Suggested solution                            │
│ Who pays           ▮▮   2/2   Paying now      │
│ Why now            ▮▮▮  3/3   Pressing        │
│ Proven abroad      ▮▮▮  3/3   Validated       │
│▌Market gap         ▮▯   1/2   Contested       │  ◀ current section
│ Difficulty to enter      ● Hard               │
│ Suggested first moves                         │
└───────────────────────────────────────────────┘
tooltip on a row = its question (§1.3) + the rungs + a reason line, e.g.
  Market gap: "4 Czech sellers, all under 2 years old; none established · 2 sources"
```

### 4.2 Front-page row meter

The pips are grouped in page order: problem 2 · pays 2 · now 3 · abroad 3 · gap 2.

```
▮▮ ▮▮ ▮▮▮ ▮▮▮ ▮▯  11/12 · Hard to enter
```

Hover card: "Opportunity 11 of 12 · Strong", then the five rows in page order (mini bar,
n/max, word), then "Difficulty to enter: Hard", then "The catch: early local sellers".

### 4.3 The 5-second test

A reader who sees only the rail would conclude:

> "Strong one. People are already paying, a real deadline is pressing, and it's proven in
> two countries abroad. The catch is that a few new Czech sellers are already in, and it's
> hard to enter. Probably public buyers."

Every one of those claims can be traced to a row. **One thing a reader would stumble on:**
the section's answer line says "none sells the security work itself", yet the row says
*Contested*. Either the four locals sell the paperwork, which would make them `adjacent`
and the gap 2 (Open), or they sell this, which would make that answer line wrong. That is a
MATCH decision about the record, not a naming problem, but a glance reader will notice the
mismatch. Flagged for the p-0008 content owner.

---

## 5. Order of sections on the page

Owner's order: The opportunity → Suggested solution → Why now → Money → Validated abroad →
Competition → Execution difficulty → Suggested first moves.

It already reads as a story: what's wrong, what to build, why it can't wait, whether it
pays, whether it's proven, who's here, what it costs to get in, what to do on Monday. It is
also close to how YC asks: problem, why now, market, competition.

**One swap is worth making: Who pays before Why now.**
- After the solution, the builder's next question is "will anyone pay for that?" Timing
  only matters once payment is plausible (the Mom Test's point, and the one that sinks most
  ideas).
- The head already carries the timing hook on deadline records. p-0008's title reads
  "…have months left…". Putting Why now straight after the solution repeats it.
- It also puts the three demand rows in order of evidence strength: says it hurts → pays →
  is forced now.

**Keep Proven abroad directly above Market gap.** It's the same test with opposite signs,
and it reads as one argument.

Recommended order: **The problem → Suggested solution → Who pays → Why now → Proven abroad →
Market gap → Difficulty to enter → Suggested first moves.** "How it works", the process
table, stays inside or right after Suggested solution, as it is now.

---

## 6. Open questions (with recommendations)

1. **Name of the first section: "The opportunity" or "The problem"?** *Recommend "The
   problem".* "Opportunity" is already the name of the total, so a row called "The
   opportunity 2/2" under "Opportunity 11/12" is two things with one name. "The problem" is
   also what the section describes, the skim test already uses it, and it reads less like a
   pitch.
2. **Should Difficulty to enter be added into the total?** *Recommend no.* It stays a scored
   rung (a level word), sits next to the total as "Hard to enter", and is used as a sort or
   filter. If yes, rename it "Ease of entry" (0–3, easy = 3). The total then becomes /15 and
   every band edge moves.
3. **Who pays at /2, with workarounds at rung 1?** *Recommend yes.* It keeps the total at 12
   and the bands unchanged, and it counts manual spend, the strongest signal an indie can
   act on. Cost: 16 of 29 live records have no price receipt today, so expect money scores
   to drop and a receipt-hunting pass. Plan it as a correction, not a quiet re-rank.
4. **Band words on the total (Strong · Good · Mixed · Weak)?** *Recommend yes, together with
   the catch line.* This needs an explicit amendment to `SKILL.md` §10 rule 11. The words
   must be written into `SCORING.md` and checked word for word, the way verdicts are today.
5. **Can one source earn points on more than one of pain, pay and now?** *Recommend no, with
   an invariant in `check-records.py` in the same change* (CLAUDE.md rule 2). A "Pressing"
   rung needs its own dated-rise source, not the contracts already counted under Who pays.

---

## 7. Sources

- ideabrowser, idea of the day for 2026-09-17, read in full: <https://www.ideabrowser.com/idea-of-the-day>.
  The page shows "Opportunity 9 Exceptional · Problem 8 High Pain · Feasibility 6
  Challenging · Why Now 9 Perfect Timing" and a Business Fit block (Revenue Potential
  "$$$", Execution Difficulty "5/10", Go-To-Market "9/10", "Right for You?"). Its sections
  are Why Now?, Proof & Signals, The Market Gap and Execution Plan, and its footer calls
  the scores "educational and based on assumptions".
- ideabrowser output fields (scores 1–10 with labels such as "Severe Pain" and "Great
  Timing"): <https://apify.com/marielise.dev/ideabrowser-scraper>
- Jared Friedman (YC), "How to Get and Evaluate Startup Ideas", with his 10 questions
  summarised: <https://gist.github.com/crkrenn/3ab4024df9da10c0b9dc7379c36358e2>. YC
  library: <https://www.ycombinator.com/library/8g-how-to-get-startup-ideas>
- Paul Graham, "How to Get Startup Ideas" (narrow and deep; "who wants this right now?"):
  <https://www.paulgraham.com/startupideas.html>
- Rob Fitzpatrick, *The Mom Test*, on commitment and advancement (time, reputation, money):
  <https://readingraphics.com/book-summary-the-mom-test/>,
  <https://www.campelolabs.com/books/the-mom-test>
- Ash Maurya, Lean Canvas (Problem with existing alternatives; Customer segments with early
  adopters): <https://www.leanfoundry.com/articles/what-is-lean-canvas>
- Tony Ulwick, Outcome-Driven Innovation opportunity score (importance + (importance −
  satisfaction); underserved = high importance and low satisfaction):
  <https://en.wikipedia.org/wiki/Outcome-Driven_Innovation>,
  <https://www.productplan.com/glossary/opportunity-scoring>
- RICE prioritisation (effort as the denominator): <https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/>
