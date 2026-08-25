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

- **Headline**: short, plain, no acronym where a word exists. Detail goes in the dek.
- **Dek**: explain every acronym and Czech term in plain English on first use.
- **`fix:`**: one sentence naming what you would actually build. **Omit it entirely**
  when the argument closes with an incumbent and names nothing an entrant would
  build that the incumbent does not already sell — the page renders nothing, which
  is honest. A vague fix reads worse than none.
- Never write about the register itself. No "this record", "de-rank", "gap check",
  "receipted", "urgency and rank". The reader does not know or care that a pipeline
  exists.
- Every numeric claim carries an `[Sn]`.

---

## 10. Scores and prose are one artifact

A score and the paragraph under it are read together, so they must be authored
together. Most factual errors this register shipped were not wrong facts — they
were a number and a sentence written by different passes with nothing comparing
them. After you move any score, re-read the prose beneath it and fix the words to
match the evidence. **Never the reverse.**
