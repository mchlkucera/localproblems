# The record content contract

**One file, one job: what a problem record must contain so the page renders itself.**

The site is a template, not a set of hand-built pages. `web/lib/sections.ts` splits a
record's body by **literal lead-ins**, and `web/app/problem/[region]/[id]/page.tsx`
renders those slices into fixed sections. So a record that follows this contract gets
the current design for free — and a future design change is one edit to the template,
never a regeneration of 23 pages.

**This is why the lead-ins are load-bearing.** Change `Why now:` to `Why it's urgent:`
in a record and that paragraph silently falls into the previous section. There is no
error; the page just renders wrong. Do not improvise them.

---

## The body, in order

```markdown
<lead paragraph — the problem, in plain words, with [Sn] markers>

Why now: <the dated trigger and why the window is open now>

Who pays: <who the buyer is; the FIRST SENTENCE becomes the page's dek, so
make it a standalone sentence that reads well directly under the title>

Existing non-solutions: <who is already in this market locally, plainly —
"nobody, and here is what a search returns" is a valid answer>

Solved elsewhere: <the funded comparables abroad, what each proves>

## First moves        ← records scoring ≥ 7 only
1. <numbered, concrete, each tied to evidence on the record>

## Revisions          ← audit trail; kept in the file, NOT rendered publicly
2026-08-24 · <tag> — <what changed and why>
```

### Where each slice lands on the page

| lead-in | section | notes |
|---|---|---|
| *(no lead-in — the opener)* | **The problem** | anchors `#problem` |
| `Why now:` | **Why now** | `#why-now`; also feeds the dated Window fact |
| `Who pays:` | **dek** + **How big** | first sentence → dek, remainder → `#how-big` |
| `Existing non-solutions:` | **Local competition** | `#local-competition`, **below** the `locals[]` ledger |
| `Solved elsewhere:` | **Proven abroad** | `#proven-abroad`, above the comps ledger |
| `## First moves` | **First moves** | score ≥ 7 only |
| `## Revisions` | *(not rendered)* | stays auditable in git |

Everything else on the page is generated from **frontmatter**, not prose: the
scorecard from `scores`, the comps ledger from `comps[]`, the local-competition
ledger from `locals[]`, "What you need" from `build` + a comp's team size,
Sources from `sources[]`.

---

## Frontmatter that drives the page

```yaml
fix: '<one plain sentence: the product a builder would actually build>'   # OPTIONAL
score: 7                      # MUST equal the sum of the five below
scores:
  proof: 2                    # → "Validated abroad"   (0-3)
  gap: 1                      # → "Local opportunity"  (0-2) high = field open
  demand: 1                   # → "Demand signal"      (0-2)
  money: 0                    # → "Money available"    (0-2)
  urgency: 3                  # → "Why now"            (0-3)
build:
  capital: garage             # kiosk <€10k · garage €10–100k · funded €100k–1M · industrial >€1M
  first_revenue: months       # weeks · months · year-plus
  builder: small-team         # solo · small-team (2–5) · funded-team
  note: '<one sentence: the skills this actually demands>'
comps:
  - name: Hemut
    url: https://hemut.com/
    geo: US
    since: 2024
    traction: '…3-person team…'   # a "N-person team" here is cited in "What you need"
locals:                         # OPTIONAL — omit the key entirely, NEVER `locals: []`
  - name: GORDIC
    url: https://www.gordic.cz/
    ico: '47903783'             # optional, strongly preferred — QUOTED (leading zeros)
    since: 1993                 # year it started selling THIS product, else founded
    status: established         # established | early  ← this IS the gap score
    evidence: 'GINIS holds atest 1/2025 for eSSL; 3 distinct public buyers in registr smluv'
sources:
  - type: arbitrage
    url: https://…
    name: 'Hemut'                 # ← what the READER sees
    why: 'AI back office for small hauliers — the closest template.'   # ← one plain line
    note: '<internal receipt — NEVER rendered, NEVER edited once written>'
    date: '2026-08-13'
    signal: yc-hemut
```

`name`/`why` are the public face of a source; `note` is the internal receipt.
Without `name`/`why` the page falls back to the signal's title/summary — readable,
but write them.

### `fix:` — the proposed product, in one sentence (optional)

Rendered directly under the dek, labelled `WHAT TO BUILD`. It exists because a
builder used to have to read three sections down to First moves before learning
what the product actually is. Rules:

- **One sentence, plainest words available.** Not a plan, not a pitch, no
  adjectives. "A marketplace where vetted nurses and carers pick up open shifts
  at care homes, and the home pays a fee for every shift filled."
- **Compression, not invention.** The material is already in `## First moves`
  and in `build.note` — say what those say, shorter.
- **No jargon.** It is the second thing read after the dek, so the same rule
  applies: a Czech or EU acronym gets replaced or glossed inline (`NZÚ` → "the
  state renovation subsidy").
- **OMIT IT where the record has no clear product answer** — typically where the
  argument closes with a named local incumbent and does not say what an entrant
  would build that the incumbent does not already sell. The page renders nothing
  when the key is absent, and an absent line is better than a vague one. Four
  live records are deliberately without it.

### `locals:` — who already sells this HERE (optional, but required at `gap: 0`)

The mirror of `comps[]`, and it exists because the asymmetry between the two let
a bug ship: 69 foreign comparables carried structured `since` + `traction` while
every local player lived as prose inside a gap-check `note:`. A machine could
read the foreign half of the register and not the local half, so `gap` could not
be audited, and `gap: 0` silently meant two opposite things.

It renders as a ledger under **Local competition**, in the same grammar as
"Proven abroad": linked name · IČO · since · the `established`/`early` band, with
`evidence` as the note line. The `Existing non-solutions:` paragraph keeps
rendering **underneath** it — the ledger says *who*, the prose says *what that
means for an entrant*.

| key | |
|---|---|
| `name`, `url` | the company and its site |
| `ico` | optional, **strongly preferred** — 8 digits, **quoted** (`'04903783'`; unquoted YAML eats the leading zero). It is what makes the claim checkable without a human: the checker counts distinct public buyers for it in `data/lookup/cz-contract-parties.jsonl`. |
| `since` | the year it started selling **this product**, else its founding year. Unquoted integer, exactly like `comps[].since`. **Required at `status: established`** (the test's first limb is "≥ 3 years selling"); optional at `early`, where a small Czech vendor often publishes no year — state what is verifiable, **never invent a year to fill the field**. |
| `status` | `established` \| `early` — **this is the gap score** |
| `evidence` | which limb(s) of the established test it passes, stated so a reader can check it |

**THE ESTABLISHED TEST** (`SCORING.md`; enforced by `scripts/check-records.py`):

> A player is **ESTABLISHED** when it has been selling for **≥ 3 years** AND shows
> at least one of: named customers or a public customer count · ≥ 2 distinct
> public buyers in `data/lookup/cz-contract-parties.jsonl` · funding at Series A
> or later · a state certification, attest or framework listing.
> Otherwise it is **EARLY** — funded-but-prototype, solo-operator, pre-customer.

The same test scores both ledgers **with the sign flipped**, and that is the
whole point of the field:

- **Abroad**, established is good news — the model is proven and someone else
  paid the tuition. `comps[]` maturity is what moves `proof` up the ladder.
- **Locally**, established is bad news — the space is taken, and `gap` is 0.
  **An EARLY local player does NOT close the space and must never de-rank a
  record on its own**; that is `gap: 1`, contested and still enterable.

Rules the build enforces (each one fails `npm run build`):

- `status: established` must **cite a limb** in `evidence` and have a `since`
  implying ≥ 3 years. A claim without a receipt is not a score.
- `gap: 0` requires at least one `locals[]` entry with `status: established`.
  "Not checked" is not a score on this ladder — an absent check is a missing
  receipt, caught here, never rendered as a number.
- `gap` at **any** value requires a `type: gap-check` source carrying
  `queries[]`. Every gap score is a claim about the local field.
- `gap ≥ 1` while `locals[]` names an established player is a contradiction.
- Omit the key when there is no named local player. **Never write `locals: []`** —
  `problem_locals` is a child table and cannot tell an empty list from an absent
  key, so the two loaders would disagree about the record.

---

## House rules for the prose

- **Plain.** A board member reading for the first time must not meet jargon. Banned
  from rendered prose: *de-rank, gap-check, absence check, incumbent re-check,
  receipted, materiality, verdict words* (UNPROVEN/FAINT/SCATTERED…), and any
  sentence about our own process ("the audit found…", "re-judgment required").
  That story belongs in `## Revisions`.
- **One claim per sentence, one or two `[Sn]` markers per sentence.** Chaining four
  markers into a clause is what made p-0008 read denser than p-0010 at the same
  length. If a sentence needs five receipts, it is five sentences — or the
  enumeration belongs in the money-receipts list, which renders automatically.
- **≤ 300 words of argument** (the five paragraphs above, excluding First moves and
  Revisions). p-0010 is the reference at ~511 including everything.
- **"How big" states a real number.** Market size, population of buyers, and a
  bottom-up estimate with its assumptions shown — never a vibe. If no figure is on
  file, say so plainly; `money: 0` is honest.
- **Every figure carries a source.** No source, no number.

## Rules that are not style

- **Never** change `score`, `scores` or `status` in a content pass — that is a MATCH
  judgment (SPEC §4).
- **Never** modify an existing `sources[].note`. Add `name`/`why` beside it.
- **Never** orphan or renumber an `[Sn]` marker. Markers resolve by position in
  `sources[]`; move a marker with its claim, never alone.
- A correction is announced, never silent: it goes in `## Revisions`, dated, merged
  into that date's entry rather than appended as a new block.

## Checking your work

```bash
node web/scripts/lint-citations.mjs     # reads output, ALWAYS exits 0 — read the WARNs
python3 scripts/check-records.py        # this contract, reported (exits 0; read the ERRORs)
npm --prefix web run build              # zod-validated; a bad record fails the build
npm --prefix web run parity             # both loaders must emit byte-identical HTML
```

**`check-records.py` is now a build gate.** `npm run build` runs it as
`--strict` in `prebuild`, so any **ERROR** stops the build. Run it bare while you
work — it exits 0 and prints everything, warnings included — and treat the ERROR
lines as the list of things that must be gone before the record ships.
