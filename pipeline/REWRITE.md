# Rewriting a record's body

**How to remake an old record to the owner-approved writing rules, one record at a
time, without losing a fact.**

- **The rules:** `data/RECORD-TEMPLATE.md`, "Writing the body" (the 14 rules, what the
  page shows, the say-it-once table).
- **The reference:** `data/problems/cz/p-0008-nis2-implementation-capacity.md`.
  Read its body and its 2026-09-16 and 2026-09-17 Revisions entries before you start.
  It passes every body rule with no waiver (fixed 2026-09-17), so it can be copied as
  the pattern.
- **The gate:** `python3 scripts/check-records.py --strict --enforce <id>` must print
  `errors: 0`.

A rewrite changes **body prose, `entry.why`, and rendered text that breaks a rule**
(`process` text, `sources[].why`/`gist`, `comps[].traction`, `locals[].evidence`).
It never changes `score`, `scores`, `status`, `entry` gate values, `sources[]` order,
any `note:`, or `title`/`brief`/`solution`/`good_for` (the owner approved those
separately; if one of them trips a gate, stop and report it rather than rewording it).

---

## Order of operations

1. **Read the sources.** Read the whole record, including every `sources[].note`
   (the internal receipts) and the Revisions. List every fact in the body with its
   `[Sn]`. That list is what "never remove content" is checked against in step 4.
2. **Restructure.** Sort the facts into sections by the question each answers
   (template, "The body, in order"). Move each company to its `comps[]`/`locals[]` row
   and each price to its `type: price` receipt; where the body used them, link
   instead. Choose each section's 3 most important items.
3. **Rewrite.** Answer sentence first, then the 3 items, then the detail as short
   paragraphs or plain bullets. Why now as pain. Willing to pay as money actually
   spent. `entry.why` as `Easier: … Harder: …`. Moves as 3–5 one-line stories whose
   first sentence stands alone.
4. **Verify against the sources.** For every rewritten sentence, open its `[Sn]`
   source (the `note:` and, if the claim changed shape, the URL) and confirm it says
   that. Tick off the fact list from step 1: every fact is either still in the body or
   now lives in its ledger row or receipt. A claim no source supports is corrected, and
   the correction goes in Revisions. An inference is written as one and flagged there.
5. **Gates.** `python3 scripts/check-records.py --strict --enforce <id>` → `errors: 0`,
   and read the advice warnings (long page items, long move leads).
   `node web/scripts/lint-citations.mjs` → no new WARN for your record.
6. **Revisions.** Add one entry under today's date (merge into an existing entry for
   that date): what moved where, what was corrected and against which source, which
   inferences were flagged, and "no score, status, source or note changed".
7. **Screenshot check** (the coordinator, once per batch, after the build; see
   "Batching"). Open `/problem/cz/<id>` at 1440 px and at 375 px. Read only the headings
   and the first lines: do they tell the whole story? Open each Read more: is everything
   there, in order?

## The checklist

Tick every line before calling a record done.

**Page view**
- [ ] Each of the 5 body sections opens with ONE answer sentence of about 20 words
      (max 25) that answers its question.
- [ ] Headings plus answer sentences alone tell the whole story.
- [ ] Each section's first list has its 3 most important items first, each about 14
      words or fewer.
- [ ] Why now: the first 3 items are who loses what time or money, and when. Law dates
      come after them.
- [ ] Willing to pay: the answer says whether people pay now; the items are prices,
      contracts or paid consultants, not only public money.

- [ ] Process steps (if any): each drawn `today` / `after` is a phrase of about 4–8
      words (max 10); detail moved to `process.summary` or the body; the record joins
      `PROCESS_PHRASE_ENFORCED` in `scripts/check-records.py`.

**Language**
- [ ] Every acronym, agency and law is explained where it first appears, or left out.
- [ ] Short sentences; no fluff words; at most one aside per sentence.
- [ ] Lists are plain bullet sentences that start with the number or the subject. No
      `- **Key:**` rows.
- [ ] No "the record" / "this record" anywhere a reader sees.

**Say it once**
- [ ] No company from `comps[]`/`locals[]` named in the body or the moves.
- [ ] No price receipt restated or cited in the body or the moves; link
      `[Willing to pay](#willing-to-pay)`.
- [ ] In-page links use the canonical anchors: `#opportunity`, `#solution`, `#why-now`,
      `#willing-to-pay`, `#validated-abroad`, `#competition`, `#execution-difficulty`,
      `#first-moves`, `#sources`.

**Moves** (only where the record has `## First moves`; don't add moves to a record
that has none)
- [ ] 3 to 5 moves, each on one line.
- [ ] Move 1 builds something or contacts someone specific. It never sells.
- [ ] Each first sentence stands alone ("a check of what?" has an answer in it).
- [ ] Then a story in simple words: who, what you give them, why they say yes, what
      comes next.
- [ ] No `[Sn]` markers and no figures; links to the evidence sections instead.

**Execution difficulty**
- [ ] `entry.why` is `Easier: a, b, and c. Harder: x, and y.`, ≤ 320 characters.
- [ ] An item with its own comma list means semicolons between that half's items.

**Honesty**
- [ ] Every fact from step 1 is still on the page somewhere.
- [ ] Every kept claim keeps its `[Sn]`; every rewritten sentence was checked against
      its source.
- [ ] Corrections and inferences are written in a dated Revisions entry.
- [ ] No score, status, source, `note:` or headline field changed.

## What "done" means

A record is done when all of these are true:

1. The checklist is ticked.
2. `python3 scripts/check-records.py --strict --enforce <id>` prints `errors: 0`.
3. The coordinator has added the id to `BODY_V2_ENFORCED` in
   `scripts/check-records.py`. **This is what makes the rules binding on that record:**
   from then on a regression fails `npm run build`. A record not in the set is not
   done, however good it reads.
4. `npm --prefix web run build` and `npm --prefix web run parity` pass.
5. The page was looked at (step 7) and the owner has seen it, or the batch was
   explicitly delegated.

Never add a waiver to reach done. `BODY_V2_WAIVERS` holds reported debt the owner has
seen; a new entry needs the owner's say-so, recorded in that record's Revisions.

## Batching

- **3–5 records per agent, one agent per batch, batches in parallel.** Each agent owns
  its record files and nothing else.
- **No shared files.** Agents do NOT edit `scripts/check-records.py`, the template,
  this file, page code or another record. They verify with `--enforce <ids>`, which
  changes nothing on disk.
- **Agents don't build.** Parallel `next build` runs fight over `web/.next` and
  `data/register.db`. The coordinator, after all agents in a round report:
  1. reviews each diff (`git diff -- data/problems/cz/<file>`), spot-checking a few
     rewritten sentences against their sources;
  2. adds the finished ids to `BODY_V2_ENFORCED` in one edit;
  3. runs `npm --prefix web run build`, then `npm --prefix web run parity`;
  4. screenshots each page (`npm --prefix web run start`, then `agent-browser`
     headless at `http://localhost:3000/problem/cz/<id>`, 1440 px and 375 px, with one
     Read more sheet open);
  5. commits only when the owner asks.
- **One review round** per batch: collect every finding, send each agent one message.

### Suggested batches (highest score first)

The remaining live records, every non-rejected one except p-0008:

| Batch | Records (score) | Has moves |
|---|---|---|
| 1 | p-0036 (10) · p-0001 (9) · p-0028 (9) · p-0037 (9) | all |
| 2 | p-0035 (9) · p-0022 (8) · p-0032 (8) · p-0033 (8) | all |
| 3 | p-0003 (7) · p-0004 (7) · p-0006 (7) · p-0009 (7) | all |
| 4 | p-0024 (7) · p-0027 (7) · p-0029 (7) · p-0031 (7) | all |
| 5 | p-0002 (6) · p-0007 (6) · p-0010 (6) · p-0011 (6) | p-0002, p-0010 |
| 6 | p-0017 (6) · p-0018 (6) · p-0025 (5) · p-0034 (5) | none |
| 7 | p-0023 (4) · p-0030 (4) · p-0005 (3) · p-0026 (3) | p-0023 |

Rejected records (p-0012–p-0016, p-0019–p-0021) have no page and are not rewritten.
`python3 scripts/check-records.py` prints one "body v2: not rewritten yet" line per
remaining record; `--body-v2` lists each finding. When that line is gone from every
record, delete `BODY_V2_ENFORCED` and make the gates unconditional.

## Agent prompt template

Paste, filling the `<…>`:

```text
Rewrite the body of these localproblems.org problem records to the owner-approved
writing rules: <p-00XX>, <p-00YY>, <p-00ZZ>. Repo:
/Users/michalkucera/Documents/CODE/localproblems. Don't commit.

Read first, in this order:
1. CLAUDE.md
2. pipeline/REWRITE.md (this procedure: follow its order of operations and checklist)
3. data/RECORD-TEMPLATE.md, "Writing the body" (the rules, what the page shows, say it once)
4. The reference record data/problems/cz/p-0008-nis2-implementation-capacity.md,
   including its 2026-09-16 and 2026-09-17 Revisions entries. Its waived gaps
   (REWRITE.md, top) are not examples.

You own ONLY these files: <data/problems/cz/p-00XX-….md>, <…>. Don't edit any other
file: not scripts/check-records.py, not the template, not page code, not another record.
Don't run `npm run build` (the coordinator does).

For each record:
- Keep every sourced fact (owner: "Dont remove content just make it scannable and
  readable"). Correct only what the sources don't support, and record it.
- Check every rewritten sentence against its [Sn] source's note and, if needed, its URL.
- Don't change score, scores, status, entry gate values, sources order, any note:,
  title, brief, solution or good_for.
- Add a dated Revisions entry (today's date).
- Gate: python3 scripts/check-records.py --strict --enforce <p-00XX>,<p-00YY>,<p-00ZZ>
  must print errors: 0. Read the advice warnings too and fix what you can.

Report back (≤150 words per record): what moved where, every correction with its
source, every inference you flagged, any fact you could not place, and the checker's
final line.
```
