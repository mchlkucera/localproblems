# Scoring v2: rubric design

*Proposal, 2026-09-17. One of three independent takes on the core scoring model. This
one is the **rubric lens**: what each scored dimension asks, where it stops, what
evidence earns each rung, and how an author could game it. **Nothing here is built.**
No code, data or rulebook was edited.*

Read before writing: `SCORING.md`, `CLAUDE.md`, `pipeline/MATCH.md` §0–1 and §9–11,
`data/RECORD-TEMPLATE.md`, `data/CONVENTIONS.md` (price receipt, difficulty to enter),
`docs/scoring-presentation-options.md`, `docs/who-pays-audit-2026-09-03.md`,
`scripts/check-records.py` (skimmed), and the records p-0005 (3/12), p-0008 (11/12),
p-0010 (7/12), p-0030 (4/12) and p-0036 (10/12).

The owner's direction (2026-09-17) is taken as given: **keep points; reasonable
judgement words; six scored dimensions** (The opportunity, Why now, Willingness to
pay, Validated abroad, Competition, Execution difficulty); Suggested solution and
Suggested first moves are unscored sections; money is rethought as willingness to
pay; freshness leaves Why now; each row shows **one number, one word, one reason
line**, as on ideabrowser.

---

## 0. The model on one screen

| # | Dimension | The builder's question | Pts | Words, 0 → 3 | Reads |
|---|---|---|---|---|---|
| 1 | **The opportunity** | Is there a real, documented pain, and how many Czech buyers share it? | 0–3 | Assumed · Reported · Documented · Widespread | sufferer-side sources: complaints, asks, associations, failed tenders, counts |
| 2 | **Why now** | Is a real deadline forcing this buyer, and are buyers visibly moving now? | 0–3 | None · Mild · Building · Forcing | `why_now` block: one binding instrument, one demand-now receipt |
| 3 | **Willingness to pay** | Do buyers like this one pay money for this job today? | 0–3 | Unproven · Indicated · Evidenced · Strong | `type: price` receipts, plus one public-money modifier |
| 4 | **Validated abroad** | Has someone already made this business work elsewhere? | 0–3 | None found · Early · Established · Validated | `comps[]`, established test (unchanged) |
| 5 | **Competition** (fewer = more points) | Who already sells this in Czechia, and are they entrenched? | 0–3 | Taken · Crowded · Light · None | `locals[]` + gap-check (competes, then maturity) |
| 6 | **Execution difficulty** (easier = more points) | How many hard doors stand between a builder and the first sale? | 0–3 | Very hard · Hard · Moderate · Easy | `entry.level`, derived (unchanged rule) |

**Total: 18.** No multipliers. **One gate:** a record whose opportunity is 0
(pain assumed) cannot rise above the lowest band, whatever it sums to (§7).

Three rules hold across all six rows, and most of this document is how each row obeys
them:

1. **One source, one scored dimension.** A source's `dims` may name at most one of
   the six. The same registr smluv contract can't be a pain receipt, a demand-now
   receipt *and* a payment receipt. Each dimension reads a different kind of fact
   (a sufferer's voice, a date, an amount, a foreign ledger, a local ledger, a gate),
   so the routing table in §8 sends each source type to exactly one. This is rule #1
   (one field, one meaning) applied to evidence: one fact, one column.
2. **Every rung is a test a script can at least partly check.** Where a rung needs
   judgement (is this "the same job"?), the judgement is written into a stored field
   with a closed vocabulary (`competes`, `binds`, `payer_type`), and the checker
   holds the number to the field. This is rule #2.
3. **Evidence that lowers a score needs a receipt. Absence that raises one needs a
   positive control.** This already governs Competition. It now also governs one
   rung of Why now and one of Willingness to pay (§2, §3).

**"This job" is defined once, by `solution:`.** Willingness to pay, Validated abroad
and Competition all ask about *this* product for *this* buyer (`entry.buyer`). Change
the solution sentence and three scores may move. So a `solution:` edit needs a
Revisions line that re-reads those three.

---

## 1. The opportunity (0–3)

### The question

*Is there a real pain, told from the buyer's side, and does it reach a countable
group of Czech buyers?* It also carries **the demand signal**: who complains, who
asks, who fails to buy. Owner: "This should also explain the demand signal."

### What it must NOT mean

| Not this | Because that is | The line between them |
|---|---|---|
| "A law now requires X" | **Why now** | A duty is not a pain. A new obligation is a date and a sanction. It becomes pain only when the obligated say it hurts: they can't find help, can't afford it, don't know they're covered. **A `regulation` source can never back The opportunity.** A fine *ceiling* is a Why now consequence. A fine actually *levied* on a named party is a loss, so it is opportunity. |
| "Buyers pay for it" | **Willingness to pay** | Payment implies pain, but reading it twice doubles one fact. **A `price` receipt or an awarded `contract`/`tender` never backs The opportunity.** A *failed* or *re-run* procurement (nobody bid, the role stays unfilled) is pain: the buyer tried and could not buy. That is a different fact about the same register. |
| "Buyers are moving now" | **Why now** | The opportunity is a *level*: the pain exists. Why now's demand limb is a *change*: more of it, recently, for a named reason. A count of the affected (6,000 covered entities) is opportunity. The same series rising between two dated windows is Why now. |
| "Someone abroad built this" | **Validated abroad** | A funded foreign company proves a model, not a Czech pain. `round`, `arbitrage` and `yc` sources never back The opportunity. |
| "The market is big" | nothing scored | A market-size report (Mordor, $70B) is context. It counts no Czech sufferer and backs no rung. |

### Rungs

| Pts | Word | Evidence test (all must hold) | Example source types |
|---|---|---|---|
| **0** | **Assumed** | No Czech source from or about the people who have the problem. The pain is inferred from a law, a foreign company or the author's reasoning. p-0005's own words: "the demand case is structural, not evidenced." | none that qualify |
| **1** | **Reported** | At least one Czech source in which a sufferer, or someone speaking for them, states the pain, or a third party documents a named case. | `complaint`, `ask` (MATCH §11), `news` naming a case, `hiring` for the manual role, a failed or re-run `tender` |
| **2** | **Documented** | (a) **Two or more independent sources**: different publishers, not one press release republished; at least one tier 1–2. **And** (b) **a named loss or a named inability**, sourced: money lost or overpaid, time lost, fines actually levied, or a buyer that tried and could not get the job done (a re-run tender, an unfilled mandated role, a waiting list). | association statement + re-run tender; ombudsman report + news case; ČOI fines levied + consumer complaints |
| **3** | **Widespread** | Rung 2, **plus** (c) **a sourced count of the Czech population that has the problem** (an official statistic or register count, not an estimate), **and** (d) **recurrence across that population**: an aggregate (complaint counts, a regulator's or association's statement about the group, several independent cases), not one anecdote. | NÚKIB registration tally; ČSÚ count; ČOI inspection statistics; SME Union statement about its members |

**One line of reason:** who hurts · what they lose · how many. Example (p-0008):
*"Covered towns and firms can't find people to do the work · about 6,000 covered ·
4 sources."*

### Anti-gaming and controls

- **Independence is counted by origin, not by URL.** Three articles quoting one ČTK
  story are one source. Two vendors' blog posts about "the pain" are tier 3 and
  interested parties. **Tier-3 or vendor-authored sources can't lift this row above
  1** (today's rule for demand, kept).
- **The loss must be the buyer's, stated from the buyer's side** (MATCH §9 framing
  rule 5). "Inspection rates rose" is the regulator's side. "Shops paid 13.0M CZK in
  fines" is the buyer's.
- **A count is not an estimate.** "~40,000 transport firms" needs a register or
  statistic behind it. The author's multiplication does not qualify for rung 3.
- **Look for the counter-signal.** Before rung 2, search for evidence the pain is
  already absorbed: a free state tool, a free counselling service (p-0004), an
  insurer's free calculator. That fact does not lower this row. It belongs to
  Willingness to pay (§3, free substitute), but finding it is part of doing this row
  honestly.
- **Checkable:** rung ≥ 1 needs a source tagged `dims: [opportunity]` whose type is on
  the allowed list. Rung ≥ 2 needs two such sources with distinct hosts and one
  `loss:` line. Rung 3 needs a `statistic` tagged opportunity. The checker can hold
  all of this, but not whether the loss is real. That stays MATCH's judgement,
  written into the `loss:` line so a reviewer can read it.

---

## 2. Why now (0–3), redesigned

### The question

*Is there a real deadline that forces **this buyer** to act, how real is it, and is
there dated evidence that buyers are moving **now**?* Owner: "there is a deadline,
how real is the deadline, and if theres anything supporting that theres demand NOW
and why (not recently checked)."

### What it must NOT mean

| Not this | Because | The line |
|---|---|---|
| "We looked recently" | retired | **Freshness is gone.** It scored 1 on all 29 live records (`scoring-presentation-options.md` C3), so it separated nothing, and on 13 records it was the only Why now point. The Verified date already says when we looked. |
| "The pain exists" | **The opportunity** | Why now reads a date and a change. It never reads a complaint. |
| "Public money is open until 17 Dec" | **Willingness to pay** | A grant window's closing date looks like a deadline, but its consequence is a lost subsidy, which is money. It is WTP's public-money modifier (§3). **A `subsidy` source never backs Why now.** One fact, one column. |
| "Buyers pay" | **Willingness to pay** | WTP reads *amounts* (a buyer paid X). Why now reads *change* (more buyers acted in this window than before, for a named reason). A single contract is WTP. A series observed twice is Why now. |
| "The technology matured" | nothing | "AI extraction is commodity" (p-0005), "AI phone agents have matured" (p-0010) are the author's reading, never a dated instrument. They earn no point. |

### Stored parts, derived rung

Why now is the one row that combines two facts, so both are **stored** and the rung
is **derived**, the way `entry.level` is. The earlier failure was storing only the
sum. Sketch (shape only, not a schema decision):

```yaml
why_now:
  deadline: hard            # none | soft | hard  (derived from the four facts below)
  instrument_ref: 1         # the S-number of the regulation that sets the date
  status: enacted           # enacted | draft   (draft ⇔ the record carries draft_law:)
  binds: buyer              # buyer | other     (does the duty fall on entry.buyer?)
  deadline_on: 2026-11-01   # the date the instrument sets, or computes (e.g. 1 yr from registration)
  sanction_ref: 1           # S-number naming the fine, ban or licence loss; enforcement_ref if the date has passed
  demand_now: first         # none | trend | first | backlog
  demand_now_ref: 6         # the S-number of that receipt
```

**Deadline part (0–2).**

| Part | Test |
|---|---|
| **hard = 2** | All four: **enacted** (published in the Sbírka zákonů or the EU Official Journal, not a bill or a draft decree); **binds the buyer** (the instrument's scope names the record's `entry.buyer` population, not the authority that must *accept* something and not the vendor); **dated**: `deadline_on` is in the instrument, is ≤ 18 months after `updated`, or has passed; **has teeth**: a named sanction in the instrument (fine ceiling, trading ban, licence loss). **A passed deadline stays hard only with an enforcement receipt dated within 12 months of `updated`**: fines levied, an inspection campaign, proceedings opened. An old date nobody enforces isn't real. |
| **soft = 1** | A dated trigger exists but fails one test: a draft (the record carries `draft_law:`); more than 18 months out; binds someone other than the buyer, but forces the buyer indirectly; no sanction; or passed with no enforcement receipt. |
| **none = 0** | No dated instrument touches this buyer. |

**Demand-now part (0–1).** One receipt that buyers are acting on this job *now*,
and why. It must show **change**, not level, so it can't double-count WTP's
contracts or the opportunity's counts. Three shapes qualify:

| Shape | Test | Example |
|---|---|---|
| `trend` | The same series observed in two dated windows of equal length, the later one higher. Both counts are sourced with the query that produced them. | registr smluv full-text "NIS2", Jun–Aug 2025 vs Jun–Aug 2026 |
| `first` | The same query returns nothing before the trigger and something after it, within 12 months of `updated`. **Positive control required**: the query must return a known pre-trigger document of a neighbouring kind, or the "nothing before" proves nothing (MATCH §4). | first tenders ever for a MiCA wind-down; first "NIS 2 balíček" contracts |
| `backlog` | An authority or association states, with a date inside the last 12 months, that demand exceeds supply: a queue, applications over capacity, repeated failed procurements. | ČNB: 251 applications assessed, 11 granted; three re-run tenders for the mandated security manager |

The `why` is part of the test: the receipt's note must name the cause (the
instrument, a price change, a newly opened data hub). A rise with no stated cause is
still a rise, but the note says "cause not stated" and the reason line shows it.

### Rungs

| Pts | Word | = deadline + demand-now | Reads as |
|---|---|---|---|
| **0** | **None** | none + none | nothing dated forces or shows movement |
| **1** | **Mild** | soft + none, **or** none + demand-now | a date on the horizon, or buyers moving without a legal push |
| **2** | **Building** | hard + none, **or** soft + demand-now | a real deadline not yet visibly biting, or a softer one that already is |
| **3** | **Forcing** | hard + demand-now | an enacted, dated, sanctioned duty on this buyer, and buyers visibly moving |

The word describes timing strength, which is true for either route to 1 and 2. The
**reason line names the parts**, so the route is never hidden. Examples:
*"Law in force, deadlines from Nov 2026, fines to 2% of turnover · contracts citing
it first appear in 2026"* or *"No deadline · hospital AI coding went from 0 to 23
sites in a year"*.

(The words reuse `SCORING.md`'s existing urgency verdicts in sentence case, so no new
vocabulary enters. Rule 16 of `SKILL.md` §10 then only needs its verdict-word ban
relaxed for rung words.)

### Anti-gaming and controls

- **"Binds the buyer" is the check that bites.** p-0010 scores urgency 3 today on
  eFTI (9 July 2027), but its own text says the regulation "obliges authorities
  EU-wide to *accept* electronic freight documents". The duty falls on authorities,
  not hauliers, so the deadline part is **soft**. That is exactly the over-claim a
  stored `binds:` field forces an author to confront.
- **The date comes from the instrument, not the press.** `instrument_ref` must be a
  `type: regulation` source, and `deadline_on` must be stated or computable from it.
  A computed date (one year from registration) needs a `deadline_basis` line.
- **Draft ⇔ `draft_law:`.** The checker can assert that `status: draft` iff the
  record carries the draft-law badge, and that a draft never makes `hard`. That
  links two fields that already exist.
- **Stale by the calendar.** The 18-month and 12-month windows are measured from
  `updated`, so the stored rung doesn't drift between builds. The checker also
  **warns** when, measured from the build date, the rung would differ, which
  surfaces records whose "now" has passed (open question 4).
- **Demand-now can't be a single transaction**, and it can't reuse the source that
  sets WTP's rung (the one-source-one-dimension rule).

---

## 3. Willingness to pay (0–3), redesigned

### The question

*Do buyers of this record's type pay money for this job, or for its bought-in manual
equivalent, today? How solid is the receipt?* Owner: "are people willing to pay right
now? (public money might make their willingness to pay go up)".

### What it must NOT mean

| Not this | Because | The line |
|---|---|---|
| "Public money moves near the problem" | the retired `money` ladder | The who-pays audit found 6 of 8 rung-1 records calling their own money "adjacent", and p-0017 and p-0031 at rung 2 on spend by someone who is not their buyer (the state building the wallet; €60M of solar panels bought for a pooling-operator record). **Public money counts only through the modifier below, and never alone.** |
| "The pain is real" | **The opportunity** | Payment is read here only. A price or contract never backs opportunity. |
| "A local vendor exists" | **Competition** | One source, two facts, opposite signs: the vendor's existence and maturity go in `locals[]` and lower Competition, while its **price** and its **named paying customers** are WTP receipts. A proven, occupied market scores high here and low there. That isn't double counting. It is the true picture. |
| "The market is large" | nothing scored | A market total or a bottom-up multiplication (6,000 × €3,000) is context under How big. It is never a receipt. |
| "It will be cheap to sell" | **Execution difficulty** | `entry.money` (bootstrap vs outside money) is the builder's capital. WTP is the buyer's. |

### What counts as evidence that buyers pay now

The existing `type: price` receipt (payer · amount_czk · unit · basis · date) is the
right shape. It gains **one closed field**, `payer_type: small-firms | large-firms |
public | households`, so the checker can require that a receipt's payer matches
`entry.buyer`. That is the "is this our buyer?" judgement, written down.

| Evidence | Basis | Strength | Why |
|---|---|---|---|
| a vendor's published list price for this job | `list-price` | **asking**: rung 1 | an offer to sell, not proof anyone bought |
| a consultant's published rate card for doing this job by hand | `list-price` | asking: rung 1 | same |
| in-house cost of doing the job by hand (sourced wage × sourced hours) | `manual-equivalent` | asking: rung 1, **never higher** | the job is *done*, not *bought*; it anchors a price, not a purchase |
| a buyer states a figure in an interview | `buyer-interview` | asking: rung 1 | stated preference |
| a signed contract in registr smluv for this job | `signed-contract` | **paid**: rung 2 | money moved |
| an awarded tender line for this job | `tender-line` | paid: rung 2 | money committed after competition |
| a bought-in manual equivalent that was actually paid (a town paid a consultant 121k CZK to write the application) | `signed-contract` | paid: rung 2 | the job was bought, by hand |
| a vendor's **named** paying customer at a stated price | `signed-contract` or `list-price` + `customer_ref` | paid: rung 2 | a name plus a price, not a logo wall |
| a vendor's revenue figure for this product line (annual report, Sbírka listin) | `revenue` (**new basis value**) | **paid widely**: rung 3 | sustained payment across buyers |
| **free substitute** on file (state tool, free counselling, insurer's free calculator) | `list-price`, `amount_czk: 0` | **caps** the row (below) | affirmative evidence against paying, not merely absence (who-pays audit §4) |

**Budgets are not receipts.** A line in a municipal budget (CityVizor) or a ministry
allocation says money is *available*, not that it buys this. It enters only as the
public-money modifier, and only when it names the job.

### Rungs

| Pts | Word | Evidence test | p-type example |
|---|---|---|---|
| **0** | **Unproven** | No price for this job on file, after a recorded price search (`price_search:` names where one was looked for). Or only a free substitute. | p-0030: "No Czech firm publishes a price for either job" |
| **1** | **Indicated** | At least one **asking** receipt: a list price, rate card, buyer-interview figure or sourced in-house cost, with `payer_type` matching `entry.buyer`. | a Czech SaaS ceník; a permit engineer's 16–42k CZK |
| **2** | **Evidenced** | At least one **paid** receipt (`signed-contract` or `tender-line`) dated within 24 months of `updated`, `payer_type` matching. | one care home's ~91k CZK NIS2 package |
| **3** | **Strong** | **Three or more distinct payers** (distinct IČO, or distinct named households or firms) with paid receipts inside 24 months; **or** a recurring payment (a renewal, or a subscription with a sourced paying-customer count); **or** a `revenue` receipt. | Lexnova's repeat orders + Český Brod + Týn nad Vltavou |

**Public money: a modifier, never the whole score.** An open public programme lifts
the row by **+1, capped at 3**, only when **all** of these hold:

1. **the base is already ≥ 1**, so public money can't create the first point (the
   owner's "never the whole score");
2. the programme **names the record's buyer type** as eligible;
3. it **names this job, or its cost category**, as eligible spend: IROP 120 names
   cyber-security measures under Act 264/2025, but a solar-panel procurement does not
   name a pooling operator's fee;
4. it is **open on `updated`**, or awarded to named buyers of this type within the
   last 12 months;
5. it **pays under 100%**, so the buyer still co-pays. A fully funded purchase shows
   the state's willingness, not the buyer's.

Stored as `wtp_public_ref: <S-number>` on a `type: subsidy` source tagged
`dims: [wtp]`. The reason line always names it: *"Paid by 3 public buyers in 2026 ·
EU grant covers 50%"*. That's why the words are evidence-strength words
(Indicated, Evidenced, Strong) rather than route words (Priced, Paid): a lifted 2 is
real evidence of willingness, but nobody has "Paid".

A **public buyer's own tender for this job is not the modifier.** When the buyer is
public, its award *is* the payment (rung 2), and the only question is whether it
bought this job.

**Free-substitute cap.** If a `price` receipt at `amount_czk: 0` is on file for this
job and this buyer type, the row **caps at 1**, unless a **paid** receipt shows
someone paying anyway (the free option doesn't serve that segment). Then the cap
lifts, and the reason line says so. p-0018 (free Logib tool, 79,000 CZK/yr list
price, no paid receipt) caps at 1. p-0029 (free OSS Alliance, ~€17M paid in ten
weeks) keeps its rung.

### Anti-gaming and controls

- **The structural bias, named.** Public buyers publish their contracts. Small
  private buyers don't. Left alone, this row rewards public-sector records and
  punishes SMB ones (the audit: *"the register can only learn what a Czech buyer pays
  in markets it has just discovered are occupied"*). Two counterweights: rung 1
  accepts manual-equivalent and list prices, which any SMB market has; and Execution
  difficulty already takes points from public buyers (§6). The rows lean opposite
  ways on purpose. Neither is adjusted to cancel the other.
- **"This job" drift.** Český Brod's ~9M CZK buys municipal security implementation,
  and the Lexnova package buys paperwork. Both are p-0008's job only because p-0008's
  `solution:` says "does the security work". A record whose solution is software
  can't cite SIEM implementation awards. The payer-type field is checkable. The job
  match is judgement, so each paid receipt's `why` must say in one clause what was
  bought.
- **Rung 0 is a score, "not searched" is not.** A 0 needs `price_search:` filled.
  With no search, the checker fails the record as a missing receipt (MATCH §7). So
  "unpriced" is never mistaken for "unlooked".
- **One source, one dimension.** A price receipt tagged `wtp` can't also be
  Competition's gap-check evidence *as a tagged dim*. The gap-check's `checked[]` may
  still point at the vendor page, because ledgers aren't `dims`. That is how
  the audit's "fourteen prices filed in the wrong column" get into the right one
  without being counted twice.

---

## 4. Validated abroad (0–3)

### The question

*Has anyone made this business work somewhere else, and how solid is the proof?*
("goes to who already sells this abroad".)

### What it must NOT mean

- **Nothing local.** No rung may mention Czechia (the v1 proof-rung-2 scar,
  `SCORING.md`).
- **Not demand or payment in Czechia.** A foreign customer count proves the model,
  not a Czech buyer.
- **Not "a company exists".** Existence carries no information: 81% of records were
  born passing it (MATCH §1).

### Rungs (the current ladder, kept; one field added)

| Pts | Word | Evidence test | Sources |
|---|---|---|---|
| **0** | **None found** | No foreign player on file selling this job. | none |
| **1** | **Early** | Only EARLY foreign players: under 3 years, or no established limb. | `round` (seed), `yc`, company page |
| **2** | **Established** | One foreign player passes the ESTABLISHED test (≥ 3 years selling + a limb: named customers or count · Series A+ · certification or framework · ≥ 2 public buyers). | `round`, `arbitrage`, customer page, annual report |
| **3** | **Validated** | ESTABLISHED in 2+ markets, at least one CEE-adjacent (DE/AT/PL/Nordics/Baltics/SI/SK/HU). | as above |

**Added: `comps[].fit: same | adjacent`**, the foreign twin of `locals[].competes`.
p-0010's Cargofy and Nexcade "both sell to freight forwarders, one buyer over" (its
own words), yet today they count toward proof. An `adjacent` comp is recorded and
rendered, and **moves nothing**. Same scar, other side of the border.

**One line of reason:** *"Sold in Germany since 2014 and in 90 countries · 2
companies."*

### Anti-gaming and controls

- **Funding is a limb, not a verdict.** Series A plus under 3 years is still Early.
  The checker already computes this from `since` and `traction`. Keep it.
- **Dead comparables count against nothing, but must be recorded** (`status: closed`)
  when found. A graveyard is information, and dropping it to protect a 2 is the
  "never exclude" violation (MATCH §2).
- **Rung 0 needs no control to score**: finding nothing *lowers* the row, and the
  authority is asymmetric in the safe direction. But **prose that claims "nobody
  anywhere sells this"** (p-0030) is a positive claim. It needs a recorded search
  (queries in English, German and Polish) or it is cut. The score is safe. The
  sentence isn't.

---

## 5. Competition (0–3; fewer and younger sellers = more points)

### The question

*Who already sells this job to this buyer in Czechia, and are they entrenched?*
("goes to who sells locally".)

### What it must NOT mean

- **Not adjacent players.** An `adjacent` local, however mature, moves nothing
  (`SCORING.md`, kept). It is intelligence for the builder, rendered in its own group.
- **Not difficulty.** `entry.incumbents` still carries no weight in Execution
  difficulty. That row prices doors, this row prices rivals (§6).
- **Not "unchecked".** "Not checked" is a missing receipt that fails the build,
  never a score (MATCH §7).
- **Not abroad.** A foreign player selling into Czechia with a Czech entity or Czech
  customers is a local, since it sells here. A foreign player without either is a comp.

### Rungs

The current gap ladder has three rungs. The owner's "3/3" framing and the corpus
both support a fourth, and it sits **between early and none**, where the builder's
situation really differs: being the second entrant against one prototype is not
being the fifth against four paperwork shops.

| Pts | Word | Evidence test (competes first, then maturity) |
|---|---|---|
| **0** | **Taken** | ≥ 1 local at `competes: direct` + `maturity: established`. |
| **1** | **Crowded** | No established direct seller, but **≥ 3 distinct early direct sellers** (distinct IČO, or distinct URL where no IČO exists). |
| **2** | **Light** | 1–2 early direct sellers. |
| **3** | **None** | **Checked** (a `gap-check` with Czech-language `queries[]`, `checked[]` and a passing positive control), and no local sells this. Adjacent players may be on file. |

**One line of reason:** *"4 Czech sellers of the paperwork, all under 2 years old ·
none does the security work."* Counts, no company names (the say-it-once rule).

### Anti-gaming and controls

- **Asymmetric authority, unchanged.** Finding a direct seller lowers the row, and
  failing to find one never raises it. Rung 3 costs the control-backed check.
- **The count rung is safe in the same direction.** More early sellers found means
  fewer points, so an author can't gain by finding more. The risk runs the other
  way: *not recording* a third early seller to keep a 2. The defence is the one MATCH
  §2 already states, plus a checker warning when a gap-check's `checked[]` names a
  host that appears in no `locals[]` entry.
- **Direct vs adjacent is where the judgement sits**, so each `evidence` line must
  say what the player sells and, for `adjacent`, why that is not this job (kept).
- **Established is script-checked**, from `since`, `ico` and `evidence` (kept).
- **"Well maintained" is not a rung.** The owner said an established, *well
  maintained* product closes the space. A rung for "established but abandoned" would
  raise a score on the absence of maintenance evidence, which breaks asymmetric
  authority. An abandoned incumbent stays Taken, and its `evidence` line says "last
  release 2019". That is the builder's intelligence, not a point.

---

## 6. Execution difficulty as a score (0–3; easier = more points)

### The question

*How many hard doors stand between a builder and the first paying customer?* ("goes
to Difficulty to enter".)

### Mapping: no new judgement

The `entry` block and its **level rule are kept exactly** (`data/CONVENTIONS.md`,
amended 2026-09-15): buyer small-firms 0 / large-firms 1 / public 2 · permission none
0 / registration 1 / licence 2 · integration software 0 / national-system 1 /
certified 2 · money bootstrap 0 / outside-money 2. The score is read straight off
the derived level:

| `entry.level` | Rule | Pts | Word |
|---|---|---|---|
| `easy` | max gate weight 0 | **3** | **Easy** |
| `moderate` | max gate weight 1 | **2** | **Moderate** |
| `hard` | exactly one gate at 2 | **1** | **Hard** |
| `very-hard` | two or more gates at 2 | **0** | **Very hard** |

The checker already asserts the level. It adds `scores.difficulty == 3 − rank(level)`.
The row shows the **level word**, not "Ease", so polarity is stated once in the row
label: *"Execution difficulty (easier = more points)"*.

**One line of reason:** the gate(s) that set the level, from `entry.why`. *"Public
buyers, so each sale goes through a tender."*

### What it must NOT mean

- **Not competition.** `entry.incumbents` stays derived and **weightless** (the
  2026-09-15 amendment). Counting rivals here too would price one fact twice.
- **Not willingness to pay.** `entry.money` is whether the *builder* needs outside
  capital before the first sale, not whether the buyer has money.
- **Not the team.** Team size and time to revenue stay retired.

### Anti-gaming: the incentive flips, so the gates need receipts

While difficulty sat outside the total, nobody gained from understating a gate. **Now
`permission: none` instead of `licence` is worth one or two points**, so the gates
move from "judged from the record's evidence" to **cited**:

- `permission: registration | licence` and `integration: national-system |
  certified` each carry an `_ref` to the source naming the requirement.
- **The downward claim needs a receipt too.** On records in regulated categories
  (fintech, health, care, staffing, legal-compliance), `permission: none` needs a
  `permission_ref` or a one-clause reason in `entry.why` saying why no authorisation
  applies. Otherwise the checker warns. This is where the owner's own amendment
  lives: *"hiring a lawyer … is a product choice, not a gate"*.
- `money: bootstrap` on a record whose buyer is `public` and whose only paid
  receipts are tenders gets a checker warning. The long public sales cycle is exactly
  the reason `outside-money` exists.

### Why it may join the total at all

`SCORING.md` kept difficulty out because it is feasibility, not opportunity. The owner
now scores it. The honest way to do that is to keep it **one row of six, unweighted**:
a builder chooses between ideas on both "is it worth it?" and "can I get in?", and
one sixth of the total is enough to separate p-0005 (easy) from p-0026 (very hard)
without letting an easy door lift a record with no pain. That is the gate's job
(§7).

---

## 7. Total, weighting, gate and bands

### Total

```
total = opportunity + why_now + wtp + abroad + competition + difficulty     (0–18)
```

**Equal weights, no multipliers.** Weighting The opportunity ×2 was considered and
rejected. A doubled row makes the total impossible to read off the six rows ("why is
it 21?"), and the case it guards against (a deadline with no pain) is handled more
plainly by a gate.

### The gate: no documented pain, no top band

**If `opportunity == 0`, the band is capped at Faint**, whatever the total.

- **Why this dimension, and only this one.** Every other row can be high for a
  record nobody wants: a sanctioned deadline (Why now 3), funded Germans (Abroad 3),
  an empty local field (Competition 3) and an easy door (Difficulty 3) sum to 12 with
  no Czech sufferer on file. That isn't hypothetical: it is the shape of the eight
  regulation-first rejected records (p-0012–p-0021: urgency 2–3, demand 0 or 1).
  Assumed pain is the one failure a builder can't recover from.
- **Cap the band, not the number.** The total stays the honest sum, so a reader can
  add the six rows and get it. The band word and the front-page sort use the capped
  band, and the reason line says *"Capped: pain not documented"*. One field, one
  meaning: `total` is arithmetic, `band` is the verdict.
- **No second gate.** Competition 0 (Taken) already moves `status` to `watching`
  (SPEC). A score gate as well would enforce one fact twice.

### Bands (/18)

Placed at the same proportions as today's /12 bands (≥ 83%, ≥ 67%, ≥ 42%):

| Total | Band |
|---|---|
| 15–18 | Prime |
| 12–14 | Strong |
| 8–11 | Fair |
| 0–7 | Faint |

Newsletter-lead material stays "Strong and up" (≥ 12). **Tie-break:** opportunity,
then willingness to pay, then why now. The first two answer "is this worth building?"

### Indicative re-scores (a sanity check of the rungs, not findings)

Read from each record's current text only. A real re-score is a MATCH pass.

| Record | Opp. | Why now | WTP | Abroad | Comp. | Diff. | Total | Band | Today |
|---|---|---|---|---|---|---|---|---|---|
| **p-0008** NIS2 | 3 Widespread: SME Union + re-run Mendel tender; NÚKIB count | 3 Forcing *if* the "first" query is run (else 2): Act 264 enacted, binds, dated, sanctioned | 3 Strong: ≥ 3 public payers in 2026 (the IROP 120 lift is not needed) | 3 Validated: Secfix DE, Copla LT | 1 Crowded: 4 early direct | 1 Hard: public buyer | **14** (13) | Strong | 11/12 Prime |
| **p-0010** trucking | 1–2 | **1 Mild**: eFTI binds authorities, not hauliers | 0–1 | 1–2 (Cargofy and Nexcade, which sell to forwarders, become `fit: adjacent`) | 0 Taken: TruckManager since 2007 | 3 Easy | **6–9** | Faint–Fair | 7/12 Fair |
| **p-0030** MiCA exit | 0 Assumed | 2 Building: passed 1 July 2026, ČNB enforcement live; no change receipt for *exits* | 0 Unproven | 0 None found | 2 Light | 3 Easy | **7**, gate applies | Faint | 4/12 Faint |
| **p-0005** order entry | 0 Assumed ("not evidenced") | 0 None ("AI is commodity" is no trigger) | 0–1 | 2 Established (Workist) | 0 Taken | 3 Easy | **5–6**, gate applies | Faint | 3/12 Faint |

What the table shows: the easy-door points no longer hide weak records (the gate
holds p-0005 and p-0030), p-0008 drops a band for being crowded and hard to enter,
and p-0010's urgency 3 doesn't survive the `binds:` test.

---

## 8. Evidence routing and invariants

### One source type → one dimension

| Source type | May tag | Never tags |
|---|---|---|
| `complaint`, `ask`, `hiring` | opportunity | the other five |
| `tender` / `contract`, **failed or re-run** (`outcome: failed`) | opportunity | wtp |
| `tender` / `contract`, **awarded**; `price` | wtp | opportunity, why_now |
| `statistic`: a **count** of sufferers | opportunity | why_now |
| `statistic`: a **dated series in two windows**, or a backlog | why_now (demand-now) | opportunity, wtp |
| `regulation` | why_now (instrument, sanction); difficulty (`permission_ref`, `integration_ref`) | opportunity, wtp |
| `news` | opportunity (a named case) **or** why_now (an enforcement receipt), one per source | wtp |
| `subsidy` | wtp (public modifier only) | why_now, opportunity |
| `round`, `arbitrage`, `yc` | none: they feed `comps[]` | all six |
| `gap-check` | none: it feeds `locals[]` and Competition rung 3 | all six |

### Invariants for `scripts/check-records.py` (same change as the rubric, WARNING first)

1. Every `scores.*` is in 0–3, and `total` equals the sum.
2. A source's `dims` names at most one of the six. Its type is allowed for that dim
   (the table above).
3. **Opportunity:** rung ≥ 1 ⇒ an allowed source tagged opportunity. Rung ≥ 2 ⇒ two
   such, distinct hosts, and a `loss:` line. Rung 3 ⇒ a `statistic` tagged
   opportunity. Tier-3-only ⇒ ≤ 1.
4. **Why now:** the rung equals the table in §2 from stored parts. `hard` ⇒ status
   `enacted`, `binds: buyer`, `instrument_ref` → a `regulation`, `sanction_ref`
   present, `deadline_on` ≤ `updated` + 18 months (or past, with an enforcement ref
   dated within 12 months). `status: draft` ⇔ `draft_law` present. `first` ⇒ a
   recorded positive control.
5. **WTP:** the rung follows from price receipts (basis, `payer_type == entry.buyer`,
   date ≤ 24 months, distinct payers). The modifier needs base ≥ 1 and a `subsidy`
   source tagged wtp. A `0 CZK` receipt with no paid receipt ⇒ ≤ 1. Rung 0 ⇒
   `price_search:` present.
6. **Abroad:** as today, counting only `fit: same`.
7. **Competition:** as today's gap, plus rung 1 ⇔ ≥ 3 distinct early direct and rung
   2 ⇔ 1–2.
8. **Difficulty:** `scores.difficulty == {easy:3, moderate:2, hard:1, very-hard:0}[level]`.
   Gate refs as in §6.
9. **Gate:** `opportunity == 0` ⇒ `band == faint`.
10. **Plant one violation of each and watch it fail** before merging (evidence
    doctrine).

---

## 9. Remaining open questions (5, each with a recommendation)

1. **What is the total called?** The owner's first dimension is "The opportunity", and
   the earlier proposal called the total "Opportunity n/12". One word, two meanings,
   on the same card. **Recommend:** the total is **"Score 14/18"** (or "Overall"), and
   "The opportunity" names only the pain row.

2. **Six rows at /3, or keep Competition at /2?** Keeping /2 avoids inventing the
   Crowded rung but breaks the uniform "n/3" the owner likes, and it weights local
   competition below the other five. **Recommend /3 everywhere**, with Crowded defined
   as ≥ 3 distinct early direct sellers. It is a count, checkable, and it only ever
   lowers a score when more players are found.

3. **Does the gate cap the band or the number?** **Recommend the band.** The total
   stays the honest sum a reader can check, and the band, the sort and a printed
   *"Capped: pain not documented"* carry the verdict.

4. **Is Why now measured from `updated` or from today?** From `updated`, a stored
   rung never drifts between builds, but a record untouched for a year still says
   "Forcing" about a passed date. From today, builds fail on the calendar.
   **Recommend `updated` for the ERROR, the build date for a WARNING**, and a
   re-verification worklist from the warnings. Staleness becomes visible without
   builds breaking at midnight.

5. **How strict is the demand-now limb at launch?** The trend, first and backlog
   shapes need queries most records haven't run, so many Why now scores drop one
   point on day one (p-0008 included, until its "first" query is recorded).
   **Recommend accepting the drop.** Ship as WARNING, publish corrections as
   corrections, and don't admit "a dated count with no baseline" as a fourth shape. That
   shape is how freshness passed on every record.
