# MATCH — the region agent

You turn region-blind evidence into region problem records. Work autonomously; do
not ask questions. Read `SPEC.md` §MATCH for the mechanics, `SCORING.md` for the
ladders, `data/RECORD-TEMPLATE.md` for the shape. **This file is the judgment.**

Every law below exists because the register already made that exact mistake and
shipped it to the public site. Each one carries its scar deliberately: a rule
stated without its failure gets "simplified" away by the next agent who finds it
verbose. If you are about to relax one of these, you are about to reintroduce a
bug someone already paid for.

---

## 0. The failure this register keeps making: ONE FIELD, TWO MEANINGS

Four separate times, a single field was made to carry two different questions,
and every time the register ended up publicly contradicting itself:

| Field | Meaning A | Meaning B | What shipped |
|---|---|---|---|
| `gap: 0` | "not checked yet" | "checked — it's taken" | a page printing *"local competitors not yet checked"* directly above a list of competitors |
| `proof: 2` | "proven abroad" | "…and no CZ player found" | 13 of 26 records scoring proof ≤1 above their own funded comparables |
| de-rank rule | "a local player exists" | "a local player owns this" | a one-person operator de-ranked the register's 11/12 record to `watching` |
| `locals.status` | "young company" | "sells something adjacent" | two agents hit it, solved it two different ways, register encoded the same fact twice |

**When a field's value would be set for two different reasons, it is two fields.**
Split it before you write, not after someone reads the contradiction on the site.

---

## 1. Existence decides nothing. Maturity does.

Half the signal corpus (yc + round + arb-scan) exists to say *"a funded foreign
company exists."* So ~81% of records are BORN passing that test. A question
everything passes carries no information.

Apply the ESTABLISHED test in `SCORING.md` to every player, foreign and local.
**The axis is the same on both sides; only the sign flips:**

- **Abroad**, established is GOOD NEWS — the model is proven, someone already paid
  the tuition. Early is weaker validation but not nothing: the market is being
  proven right now, and that is a good moment to join.
- **Locally**, the sign flips. Established means the space is taken. **An early
  local player does NOT close a space.** It is evidence the market is being made.

> Owner, 2026-08-25: *"if it's just funded two guys who have a prototype that's a
> signal that it's a good time to join. Established well maintained product?
> probably not a good space to enter."*

Check dates before you score. p-0006 stood down for an incumbent that ARES dates
to 2025-10-01 — younger than the record that de-ranked for it. p-0008's locals
are younger than the obligation they sell against.

---

## 2. Never exclude. Inform the builder.

> Owner, 2026-08-25: *"Never 'exclude' — the goal is to inform the builder properly."*

Every local player you find goes in `locals[]`. A mature vendor selling something
adjacent is **intelligence a builder needs**, not noise to be filtered. Label it
`competes: adjacent` and write, in `evidence`, what it actually sells and why that
is not this. That sentence is the value.

Never drop a player to make a score come out right. Never mislabel one to dodge an
invariant. If the schema cannot express what you found, say so in your report —
that is a schema bug, and it gets fixed. Both of those workarounds have already
been tried here, and they produced a register that encoded the same situation two
contradictory ways.

---

## 3. Receipts over plausibility

Never invent a URL, a founding year, a headcount or a figure to satisfy a schema.
`since` is optional for early players precisely so you are never forced to guess;
`url` is optional when `ico` is present precisely so a real company with no
website still gets recorded. A plausible-sounding fact with no receipt is the
exact failure this register exists to avoid.

If you cannot source it, write down that you could not, and why.

---

## 4. A negative is only evidence if the method produces positives

Before trusting any "we found nothing", run a **positive control**: search for
something you already know exists and confirm the method surfaces it. Record the
control in the gap-check note.

An absence check with no control is worth nothing, and the register has shipped
several. The 2026-08-13 checks cited a Y Combinator page for a London company as
the receipt for a *Czech* absence — which proves nothing about Czechia.

---

## 5. Gap authority is asymmetric

Evidence of a named established direct competitor **lowers** gap. Failure to find
one **never raises** it. Only a check with recorded `queries[]`, `checked[]` and a
passing positive control can move gap to 2.

---

## 6. Search in the language of the market

The corpus is **structurally blind** to bootstrapped Czech SMB vendors: they raise
no capital and sell through no tender, so a capital-and-tender-shaped ledger
cannot see them. Ten such vendors were found by search and return ZERO hits across
all 11,330 signals.

An English-language query returned no Czech vendor at all where the Czech query
returned four. **Always search in Czech**, with descriptive product language a
customer would use — not the register's own vocabulary. Run several query shapes:
one shape returning nothing is not evidence of absence.

---

## 7. "Not done" is never a score

An unrun check is a **missing receipt**, caught by `scripts/check-records.py` and
blocked at the build gate. It is never expressed as a number, and it never appears
in rendered prose. There are no "not yet", "to be confirmed" or "pending" states
on a published record — either the work is done, or the record does not ship.

---

## 8. A rule enforced by prose is not enforced

`SPEC.md` forbade the proof-vs-comps contradiction from the beginning. Nothing
checked it, so 13 records carried it for weeks. If you introduce a rule, add the
invariant to `scripts/check-records.py` in the same change — it runs inside
`prebuild`, so a contradiction fails the build and blocks the deploy.

And keep the checker honest: 8 of its 11 errors were once phantoms from rejected
records, which is how a real error becomes invisible. **A check that cries wolf
gets ignored, and an ignored check is the same as no check.**

---

## 9. Write for a builder, not an analyst

The reader is deciding what to build this quarter. Write for them:

- **Headline**: short, concrete, urgent, a number where there is one, never abstract;
  no acronym where a word exists. Detail goes in the dek.
- **`brief:`** (optional): the situation told as a short story, at most 2 sentences
  and 40 words. Say who is stuck, doing what, and what forces it now. Cite every
  number or date, and write only what the sources say ("most have nobody" needs a
  source that counts them). **`good_for:`** (optional): one line naming the real
  entry requirement, or the space when anyone can enter. No numbers, no markers.
  Both are gated in `check-records.py`.
- **The card under a headline is exactly three items: story, Suggested, Good for.**
  Write it by the framing rules, each with a rejected and an approved example, in
  `data/RECORD-TEMPLATE.md` → "The headline block" → "The framing rules".
- **Dek**: explain every acronym and Czech term in plain English on first use.
- **`solution:`**: one sentence stating what would likely solve the problem —
  REQUIRED on every record, and always shown as "Likely solution", so describe the
  product and never claim the outcome ("will solve", "the only", "guarantees" fail
  the build). Where an incumbent already sells the answer, describe that product
  neutrally; whether the field is open is the gap score's job, not this line's.
- Never write about the register itself. No "this record", "de-rank", "gap check",
  "receipted", "urgency and rank". The reader does not know or care that a pipeline
  exists.
- Every numeric claim carries an `[Sn]`.
- **"Who pays and how much" is answered by a price receipt** — a `type: price`
  source naming the Czech buyer, the crown figure, the unit and the basis — or
  it is not answered. MONEY alone never claims it: that ladder measures
  proximity to a public budget, and "public money moving near this problem" is
  not "this buyer pays this much for this" (owner, 2026-09-03).

---

## 9a. Difficulty to enter is judged, not predicted (owner, 2026-09-15)

`entry:` replaced the `build:` scorecard. The capital ladder, the team band and
the time-to-first-revenue guess are gone — owner: *"get rid of the team
predictions"*; *"CAPITAL €10–100k / TEAM 2–5 people is pretty arbitrary, more
abstract categories will be more truthful"*. What the record states instead is
the doors an entrant has to get through, which the evidence on the record can
actually answer: **who buys · what permission · who is already here · what it
must plug into · money**.

- **Two of the seven keys are DERIVED and you do not get a vote.**
  `incumbents` is read off `locals[]` (direct + established ⇒ `direct`; else
  adjacent + established ⇒ `adjacent`; else `open`), and `level` is read off
  the gate weights. `scripts/check-records.py --strict` fails the build on
  either disagreement, so fix the ledger, never the value.
- **`incumbents` does not move the level.** GAP already prices established
  competition; weighing it here too is one fact in two places — §0, again.
- **Reading the buyer's own ERP is `software`.** Pohoda, Helios, ABRA, Cygnus,
  a hospital's own system: that is what every business tool does.
  `national-system` means a STATE, national or EU system the product cannot
  work without, or hardware and crews in the field.
- **`permission: licence` is an authorisation to SELL THE PRODUCT**, or a
  regulated profession's monopoly over its core act. Hiring a lawyer or a tax
  adviser as an ingredient is a product choice, not a gate.
- **`why` names the gates, in the same plain voice as `solution:`** — one or
  two sentences, ≤ 320 chars, no certainty words (the same OVERCLAIM regex).
  Where the level is `easy`, say why the door is open.

Full definitions: `data/CONVENTIONS.md`, "difficulty to enter".

---

## 9b. Draw the process only where a process exists (owner, 2026-09-15)

`process:` is the one figure on a record page an author writes. Everything else
drawn there — the field timeline, the who's-in-the-room grid, the comp map, the
money scale — is derived from `comps[]`, `locals[]` and the price receipts, and
you author none of it.

- **Author `process:` when the problem is a WORKFLOW somebody performs today.**
  Skip it for a new obligation or a one-off decision: about twelve of the 29
  live records have no process to draw, and no block is the honest answer.
- **NEVER FILL A GAP WITH A PLAUSIBLE GUESS.** A diagram reads as settled fact
  whatever the prose beside it says. Owner: *"be SUPER CLEAR about where we're
  not sure how the process looks, put question marks if you don't know."* So
  every step carries `known`: `documented` (cited), `inferred` (our reading of
  the record's own prose) or `unknown` (we do not know, and the page prints a
  "?"). `inferred` costs a dashed line; a guess dressed as `documented` costs
  the register the only thing it has. §3, drawn.
- **The after half is ours, and it is never evidence.** No `[Sn]` in a step's
  `after` or in `summary.after`, and no certainty words in the summary — it
  renders inside a box labelled SUGGESTED (§9).
- **Money and competitors are not in it.** A crown figure is a `type: price`
  receipt; a named seller is `comps[]` or `locals[]`. Both are refused inside
  the figure, and a step names the ROLE instead. §0, again.

Full contract, page order and a worked example: `data/RECORD-TEMPLATE.md`,
"Figures". Enforced in `scripts/check-records.py`.

---

## 10. Scores and prose are one artifact

A score and the paragraph under it are read together, so they must be authored
together. Most factual errors this register shipped were not wrong facts — they
were a number and a sentence written by different passes with nothing comparing
them. After you move any score, re-read the prose beneath it and fix the words to
match the evidence. **Never the reverse.**

---

## 11. A direct ask is demand, never money

An `ask` source — a signal from the `asks` ledger: a TA ČR research need, an
owner-set hackathon challenge — is a receipt that a named institution HAS the
problem. It cites **demand** and nothing else: rung 1 on its own, rung 2 when it
recurs or joins other documented demand. It never cites **money** — a prize is
not a budget, and a research need's budget arrives later, through the tender,
which lands in `tenders` and cites money there. And it says nothing about
**gap**: that the owner wants it solved is not evidence that no vendor sells it.
Gap still needs its check (§4, §5). `TYPE_TO_DIM` in `web/lib/scorecard.ts` and
`scripts/db.py` encodes the first half; the checker still owns the second.
