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
ledger from `locals[]`, "Difficulty to enter" from `entry`, Sources from
`sources[]`.

---

## Frontmatter that drives the page

```yaml
title: '<plain, urgent headline — digits for numbers, ≤ 2 short sentences>'   # REQUIRED
brief: '<OPTIONAL — the story, ≤ 2 sentences and ≤ 40 words: who is stuck, doing what, what forces it NOW; every number/date cited [Sn]>'
solution: '<one plain sentence: what would likely solve the problem; starts "Build " when brief is set>'   # REQUIRED
good_for: '<one line, ≤ 15 words: the real entry requirement, or the space if anyone can enter>'   # OPTIONAL
score: 7                      # MUST equal the sum of the five below
scores:
  proof: 2                    # → "Validated abroad"   (0-3)
  gap: 1                      # → "Local opportunity"  (0-2) high = field open
  demand: 1                   # → "Demand signal"      (0-2)
  money: 0                    # → "Money nearby"       (0-2) public budget near this — NOT who pays
  urgency: 3                  # → "Why now"            (0-3)
entry:                        # DIFFICULTY TO ENTER — required on EVERY record
  level: hard                 # easy | moderate | hard | very-hard   (DERIVED, see below)
  buyer: public               # small-firms | large-firms | public
  permission: licence         # none | registration | licence
  incumbents: adjacent        # open | adjacent | direct   (DERIVED from locals[])
  integration: software       # software | national-system | certified
  money: bootstrap            # bootstrap | outside-money
  why: '<one or two plain sentences naming the gate(s) that set the level>'
comps:
  - name: Hemut
    url: https://hemut.com/
    geo: US
    since: 2024
    traction: '…$10M Series A, 50+ utility customers…'   # PUBLIC and verifiable
locals:                         # OPTIONAL — omit the key entirely, NEVER `locals: []`
  - name: GORDIC
    url: https://www.gordic.cz/ # optional IF `ico` is present (see below)
    ico: '47903783'             # optional, strongly preferred — QUOTED (leading zeros)
    since: 1993                 # year it started selling THIS product, else founded
    competes: direct            # direct | adjacent  ← does it sell THIS?
    maturity: established       # established | early  ← the established test
    evidence: 'GINIS holds atest 1/2025 for eSSL; 3 distinct public buyers in registr smluv'
  - name: Efektivia
    url: https://efektivia.eu/
    since: 2022
    competes: adjacent          # a real player nearby, selling something else
    maturity: established       # …and mature. Adjacent NEVER moves gap.
    evidence: 'sells AI triage to the building authority — the other side of the counter
      from the applicant this record serves'
sources:
  - type: arbitrage
    url: https://…
    name: 'Hemut'                 # ← what the READER sees
    gist: 'US trucking back office'   # ← 2–6 words, the label on the ledger row
    why: 'AI back office for small hauliers — the closest template.'   # ← one plain line
    note: '<internal receipt — NEVER rendered, NEVER edited once written>'
    date: '2026-08-13'
    signal: yc-hemut
```

`name`/`gist`/`why` are the public face of a source; `note` is the internal
receipt. `gist` is the few-word label printed on the ledger row (NAME · gist ·
date); `why` is the full sentence — behind the row's "more" toggle when a `gist`
is present, in the open otherwise. Without `name`/`why` the page falls back to
the signal's title/summary — readable, but write them.

### `type: price` — the price receipt (who pays, and how much)

`money` scores how near a **public budget** is; it never says who pays for this
product or what they pay (owner ruling, 2026-09-03). That answer is a `price`
source: what a named Czech buyer pays for THIS product or its manual
equivalent. Five fields are REQUIRED and the build fails without any of them —
`payer` (a named buyer or a sized segment), `amount_czk` (unquoted number; `0`
is real where a free incumbent sets the price), `unit` (`per-seat-month` ·
`per-case` · `per-year` · `per-project` · `one-off` · `per-hour`), `basis`
(`list-price` · `signed-contract` · `tender-line` · `buyer-interview` ·
`manual-equivalent`), `date`. The same fields on any other type also fail. It
renders under **How big** as one ledger line, `<payer> pays <amount> CZK <unit>
· <basis> · <date>`; a record scoring ≥ 7 without one prints `No Czech buyer
has priced this yet.` It cites `money` only when tagged `dims: [money]`, never
another dimension — untagged, it backs no score, which is the point.

```yaml
  - type: price
    url: https://www.wue.cz/cenik
    name: 'Wue'
    gist: 'installer SaaS list price'
    why: 'What a Czech installer pays today for the back office this record proposes.'
    note: 'ceník read 2026-08-13; 650 Kč/seat/mo, heat-pump module +200 Kč'
    date: '2026-08-13'
    payer: 'Czech PV/heat-pump installers (2–20 seats)'
    amount_czk: 650
    unit: per-seat-month
    basis: list-price
```

### `price_search:` — where to look for the price (optional, one sentence)

For a record that scores 7 or more and carries no `type: price` source: the
surfaces and the keyword a builder should search — a registr smluv full-text
query, an MS2021+ index keyword (`scripts/ms21_query.py`), a named vendor's
price list, a named ROLE at a named institution to ask. It is an estimate of
WHERE, never of HOW MUCH: a crown figure in it fails the build (owner,
2026-09-04). Renders beside "No Czech buyer has priced this yet."

### `solution:` — the likely solution, in one sentence (required)

Rendered directly under the dek, ALWAYS labelled `LIKELY SOLUTION` — on the
record page and on every other surface that shows it. The register says what
would probably solve the problem, never that it knows (owner, 2026-09-10: "don't
try to make it like we know everything"). It exists because a builder used to
have to read three sections down to First moves before learning what the product
actually is. Renamed from `fix:` and made required on 2026-09-10. Rules:

- **One sentence, plainest words available.** Not a plan, not a pitch, no
  adjectives. "A marketplace where vetted nurses and carers pick up open shifts
  at care homes, and the home pays a fee for every shift filled."
- **Compression, not invention.** The material is already in `## First moves`
  and in `entry.why` — say what those say, shorter.
- **No jargon.** It is the second thing read after the dek, so the same rule
  applies: a Czech or EU acronym gets replaced or glossed inline (`NZÚ` → "the
  state renovation subsidy").
- **Describe the product, never the outcome.** No certainty the label disowns:
  "will solve/fix/eliminate", "guarantees", "the only", "the answer", "best",
  "clearly". `scripts/check-records.py` fails the build on these (`OVERCLAIM`).
- **REQUIRED on every record, rejected ones included** — the build fails without
  it. It answers "what would likely solve this problem?", which every record can
  answer, even one whose argument closes with a named local incumbent: there the
  likely solution is what that incumbent sells, stated neutrally. Whether the
  answer is still open to an entrant is the gap score's question, never this
  field's (one field, one meaning). The old rule — omit the key where an
  incumbent holds the field — is retired with the rename.

### The headline block — `title`, `brief:`, `solution:`, `good_for:` (owner, 2026-09-16)

A general builder reads the top of a record in this order: a **headline**, then a
card of **exactly three items**: the story (`brief`), **Suggested** (`solution`)
and **Good for** (`good_for`). `brief` and `good_for` are OPTIONAL; a record that
carries a `brief` gets the card, and every rule below applies to it. The copy the
owner approved after many rounds, and the reference for everything that follows:

```yaml
# p-0008
title: '6,000 Czech towns and firms have months left to meet a new cybersecurity law'
brief: 'Many small firms don''t even know the law covers them, and the first deadlines hit in late 2026 [S1,S2]. A firm that misses its deadline can be fined up to 2% of its turnover (which is A LOT of money) [S1].'
solution: 'Build a small security agency that writes their EU grant applications and does the security work.'
good_for: 'Cybersecurity people interested in grants and public-sector sales.'
# p-0036
title: 'Czech hospitals pay twice for every medical report. A 1.14bn CZK grant to change that closes in December.'
brief: 'Doctors type reports as free text, then other staff re-read them by hand [S1,S3]. The state pays hospitals to upgrade, but only until December [S8].'
solution: 'Build report templates inside the hospital''s own software that pre-fill codes for staff to check, as companies already do abroad.'
good_for: 'Health-tech builders patient with hospital tenders.'
```

#### The framing rules

**The aim is really simple language and a clear motivation.** Each rule below
came from an owner correction. Rules marked **(gate)** fail the build in
`scripts/check-records.py --strict` (`check_headline`). The rest are judged:
no regex can tell abstract from concrete, so none is attempted.

**The card is exactly three items:** story, Suggested, Good for.
- ✗ Four or five items. The brief was a list of 1 to 3 bullets for a few hours
  on 2026-09-16, which made the card that long. **(gate)** A list now fails.
- ✓ One `brief` string, one `solution`, one `good_for`.

**Headline (`title`)**

**The first test: every headline names a clear pain point.** Owner, 2026-09-16:
*"Each heading should have a clear pain point."* Say WHO is hurting and HOW,
in plain words: wasted time, lost money, fines, stuck cases, overpaying, a
deadline they may miss. A volume ("82,000 cases") or a missing product ("no
Czech software does X") is NOT a pain point on its own; it can sit beside the
pain, never replace it. The pain must be real and sourced, like any other
claim (rule 5): where a record's sources show nobody hurting, keep the most
honest headline and flag the record, never invent a pain to pass this test.
Judged, not gated: no regex can tell a pain from a fact.
   - ✗ "Czechia handled 82,000 work-permit cases in 2024, and no Czech software tracks them" ("Why is that a problem? I don't see the pain point there.")
   - ✓ "Czech work permits for foreign staff get stuck, and agencies still do every file by hand"
   - ✓ "Czech hospitals are overpaying for medicine"
   - ✓ "6,000 Czech towns and firms have months left to meet a new cybersecurity law"

1. **Say plainly what is going on and why it matters now, in simple words.**
   - ✗ "6,000 Czech organisations. One cyber deadline." ("sounds like a novel title, too abstract")
   - ✗ "…and since September they can grow much bigger" ("very abstract", "wtf")
   - ✓ "Czech hospitals are overpaying for medicine"
2. **Use digits for numbers.** **(gate)** On a record with a brief, a spelled-out
   cardinal (two to ninety, hundred, thousand, million, billion) fails. "one",
   "hundreds", "thousands" and "twice" pass because they are ordinary prose or
   vague amounts.
   - ✗ "Six thousand Czech firms must meet new security rules, and most are not ready"
   - ✓ "6,000 Czech towns and firms have months left to meet a new cybersecurity law"
3. **Keep it short.** At most two short sentences. Use the second only when it
   carries the urgency.
   - ✗ "Czech hospitals write reports as free text, then pay people to read them again" (the second half repeats the problem, and no urgency is given)
   - ✓ "Czech hospitals pay twice for every medical report. A 1.14bn CZK grant to change that closes in December."
4. **Frame dates relative to today, honestly.** If most deadlines are 3 to 9 months
   away, say "months left".
   - ✗ "…have one year to meet a new cybersecurity law"
   - ✓ "…have months left to meet a new cybersecurity law"
5. **Make no claim a source doesn't back.** A headline carries no marker, so
   check its figure against the body's cited sentence before it ships.
   - ✗ "…and most are not ready" (no source counts who is ready)
   - ✓ "6,000 Czech towns and firms" (the regulator's own count)

**Story (`brief`)**

6. **Tell it like a story:** who is stuck, doing what, and what forces it now.
   Use simple language and no abstraction.
   - ✗ "Most deadlines fall between late 2026 and mid-2027, fines reach 2% of turnover, and a university has re-tendered for a security manager" (a list of facts)
   - ✗ "Grant: up to 28M CZK per hospital" ("abstract")
   - ✓ "Doctors type reports as free text, then other staff re-read them by hand."
7. **Say who a rule hits, and make the number felt in human terms.** A fine on a
   percentage of turnover applies to firms, not to towns.
   - ✗ "fines reach 2% of turnover" ("what fines, for whom?")
   - ✓ "A firm that misses its deadline can be fined up to 2% of its turnover (which is A LOT of money)"
8. **Don't be oddly specific.** Don't name a single town or institution, and
   don't tell a one-off anecdote unless it IS the story. Cutting specifics is
   the way to make a brief shorter.
   - ✗ "The town of Týn nad Vltavou paid a consultant…" (too specific)
   - ✗ "one small town paid…" ("how is it relevant?")
   - ✓ "The state pays hospitals to upgrade, but only until December."
9. **Use "most" or "many" only when a source says so.** No regex checks this.
   The author has to find the receipt.
   - ✗ "…and most have nobody who can do it" (no source counts them, so it was cut)
   - ✓ "Many small firms don't even know the law covers them" (the business association's own words)
10. **Don't assert a cause the evidence doesn't prove.** Put the two facts side
    by side and let the reader join them.
    - ✗ "Most of the 6,000 have nobody to do the work — Mendel University re-tendered…" (one re-tender offered as proof of the whole)
    - ✓ "Doctors type reports as free text, then other staff re-read them by hand."
11. **At most 2 sentences and 40 words.** **(gate)** A line break also fails.
    - ✗ "…by hand [S1,S3]. Coders lose hours to it [S3]. The state pays…" (three sentences; the checker's positive control)
    - ✓ the p-0008 brief above: two sentences, 39 words
12. **Receipts and one meaning.** Every number, date or month carries `[Sn]` at
    the end of the sentence it backs. **(gate)** A brief with a number and no
    marker at all fails, and so does a marker that doesn't resolve. Where each
    marker sits is judged. Don't talk about solutions ("suggest",
    "opportunity", "build a": that is `solution:`). Don't name anyone from
    `comps[]`/`locals[]` (the ledgers answer that question). No certainty
    words (`OVERCLAIM`).
    - ✗ "…the first deadlines hit in late 2026." (a date with no marker)
    - ✓ "…the first deadlines hit in late 2026 [S1,S2]."

**Suggested (`solution`)**

13. **Start with "Build".** **(gate)** On a record with a brief, the check reads
    only the opener. Then name the plain business form (an agency, software, a
    marketplace, a service), WHERE it lives or plugs in, and what it does.
    - ✗ "build report templates" ("WHERE? missing explanation")
    - ✓ "Build report templates inside the hospital's own software that pre-fill codes for staff to check"
14. **Point abroad in the plural.** Write "as companies already do abroad", not
    the name of one foreign company. The names belong in the Proven abroad
    ledger.
    - ✗ "…, as Tiplu does in Germany" (illustrative; the owner asked of the plural form, "isn't better?")
    - ✓ "…, as companies already do abroad."
15. **No certainty words.** **(gate)** `OVERCLAIM`: "will solve", "the only",
    "guarantees", "best" and similar.
    - ✗ "…software that will solve the double reading" (illustrative)
    - ✓ "Build a small security agency that writes their EU grant applications and does the security work."
16. **Never a block of text that says almost nothing.**
    - ✗ "A fixed-price service for the towns and care homes covered by the new Czech cybersecurity law: check what each one owes before its deadline, write the EU subsidy application where one applies, then do the security work itself rather than only the documents." ("a block of text saying almost nothing")
    - ✓ "Build a small security agency that writes their EU grant applications and does the security work."

**Good for (`good_for`)**

17. **Name the real entry requirement plainly** when the evidence shows one:
    the specific knowledge, interests, network or skills a builder must have to
    enter.
    - ✗ "procurement insiders patient with public hospitals" (a requirement stated as jargon: "this isn't simple language")
    - ✓ "Someone with cybersecurity skills who's interested in grants and public-sector sales."
18. **Never invent a requirement. When anyone could enter, name the space
    instead**, so the reader knows what they are walking into.
    - ✗ "people who know how hospitals buy medicines" (a requirement that isn't real: "the builder really must know this?")
    - ✓ "Someone who'd like to work with hospitals."
19. **Plain words, short, no numbers.** **(gate)** At most 15 words, one line, no
    digits or spelled magnitudes, no `[Sn]`, and no market claims ("lucrative",
    "growing", "underserved") or certainty words. A line that needs a citation
    has turned into a second brief without its receipt.
    - ✗ "Builders chasing a growing 1.14bn CZK market" (illustrative; it fails on the number and on "growing")
20. **Start with the person.** **(gate)** The card prints "Good for" straight before
    this line, so its first word names WHO: Someone, People, Engineers, Developers…
    (`GOOD_FOR_PERSON_OPENERS` in `scripts/check-records.py`).
    - ✗ "Mapping and aerial-photo people who'd like to work with sewer operators." (reads "Good for mapping…" — owner: "Good for should always start with a person")
    - ✓ "Someone who can map from aerial photos and would like to work with sewer operators."
    - ✓ "Health-tech builders patient with hospital tenders."

**Honesty is non-negotiable.** Check every claim on the card against the
record's sources before it ships, and never let wording the owner approved stand
in for a receipt. The first approved draft of the p-0008 brief read "Most must
comply by 31 Dec 2026 … and most have nobody who can do it". The Act starts each
one-year clock when the registration decision is delivered, and no source on file
counts who lacks the people, so both claims were corrected before they shipped
(p-0008 `## Revisions`, 2026-09-16).

`web/lib/data.ts` types `brief` and `good_for` and resolves the brief's markers.
Neither is a column in `scripts/db.py`; both ride `problems.extra_json`, like
`process`.

### `entry:` — difficulty to enter (required, owner 2026-09-15)

It REPLACES `build:`. The capital ladder, the team band and the time-to-first-
revenue guess are retired — owner: *"get rid of the team predictions"*, and
*"CAPITAL €10–100k / TEAM 2–5 people is pretty arbitrary, more abstract
categories will be more truthful"*. Every key is required, on every record,
rejected ones included; `data/CONVENTIONS.md` carries the full gate
definitions. What an author has to get right:

- **Judge from the record's own evidence, never aspirationally.** The gates are
  facts about the market, not a plan.
- **`incumbents` is not a judgment.** It is read off `locals[]`: any local at
  `competes: direct` AND `maturity: established` ⇒ `direct`; else any at
  `competes: adjacent` AND `maturity: established` ⇒ `adjacent`; else `open`.
  Change the ledger, not the value.
- **`level` is not a judgment either.** Weights: buyer 0/1/2 · permission
  0/1/2 · integration 0/1/2 · money 0/2. Max 0 → `easy` · max 1 → `moderate` ·
  exactly one gate at 2 → `hard` · two or more at 2 → `very-hard`.
  **`incumbents` carries no weight** — the `gap` score already prices
  established competition, and counting it twice is one fact in two places
  (amended 2026-09-15, after the first pass put 20 of 37 records at hard or
  very-hard and made the owner's canonical easy example, an app for trucking
  firms, come out `hard`).
- **Reading the buyer's OWN software is `software`.** Pohoda, Helios, ABRA,
  Cygnus, a hospital's own system, a dispatcher's planning tool — that is what
  every business tool does. `national-system` is for a STATE, national or EU
  system the product cannot work without (EDC, the state eHealth gateway,
  ISIR, the cadastre, datová schránka, eRecept) or for hardware and crews in
  the field.
- **`permission: licence` is an authorisation to SELL THE PRODUCT**, or a
  regulated profession's monopoly over its core act. Hiring a lawyer or an
  accountant as an ingredient is a product choice → `none`.
- **`why` names the gates, not an outcome.** One or two sentences, ≤ 320 chars,
  plain words, every Czech/EU acronym glossed at first use, no certainty words
  (the same `OVERCLAIM` regex `solution:` is held to). Both derivations and
  every rule above are ERRORs in `scripts/check-records.py --strict`, which
  runs inside `npm run build`.

### `locals:` — who already sells this HERE (optional, but required at `gap: 0`)

The mirror of `comps[]`, and it exists because the asymmetry between the two let
a bug ship: 69 foreign comparables carried structured `since` + `traction` while
every local player lived as prose inside a gap-check `note:`. A machine could
read the foreign half of the register and not the local half, so `gap` could not
be audited, and `gap: 0` silently meant two opposite things.

It renders as a ledger under **Local competition**, in the same grammar as
"Proven abroad": linked name · IČO · since · the `established`/`early` maturity
band, with `evidence` as the note line — **split into two labelled groups**, the
ones that sell this first ("3 sell this") and the ones nearby that do not ("4
nearby, selling something else"). The `Existing non-solutions:` paragraph keeps
rendering **underneath** — the ledger says *who*, the prose says *what that
means for an entrant*.

| key | |
|---|---|
| `name` | the company |
| `url` | its site. **Optional IF `ico` is present** — see the ARES fallback below. At least one of `url` / `ico` is required. |
| `ico` | optional, **strongly preferred** — 8 digits, **quoted** (`'04903783'`; unquoted YAML eats the leading zero). It is what makes the claim checkable without a human: the checker counts distinct public buyers for it in `data/lookup/cz-contract-parties.jsonl`. |
| `since` | the year it started selling **this product**, else its founding year. Unquoted integer, exactly like `comps[].since`. **Required at `maturity: established`** (the test's first limb is "≥ 3 years selling"); optional at `early`, where a small Czech vendor often publishes no year — state what is verifiable, **never invent a year to fill the field**. |
| `competes` | `direct` \| `adjacent` — **does it sell THIS?** The only field `gap` reads for eligibility. |
| `maturity` | `established` \| `early` — the established test, unchanged. It sets the **rung**. |
| `evidence` | at `direct`: which limb(s) of the established test it passes, stated so a reader can check it. At `adjacent`: **what it actually sells, and why that is not this.** |

### `competes` vs `maturity` — one field per question

`status: established | early` shipped for exactly one commit and both content
agents broke on it the same way. A **mature** Czech firm that sells something
**adjacent** — the other side of the counter, a different segment, a service firm
rather than a product vendor — is not `early`; but writing `established` forced
`gap: 0` and stood a record down over a company that does not sell this. One
agent wrote those firms down as `early` (a false maturity claim), the other left
them out of the ledger (a false absence), so the two halves of the register
encoded the same situation two different ways. It is the same one-field-two-
meanings defect this line of work has already fixed three times.

- **`competes: direct`** — sells THIS record's product to THIS record's buyer.
- **`competes: adjacent`** — a real player in the neighbourhood that does NOT
  sell this: different segment, different side of the counter, legacy/partial, or
  a service firm rather than a product vendor. **`evidence` must say plainly what
  it does sell and why that is not this** — without that sentence the entry reads
  as a competitor the record failed to score against, which is worse than the
  exclusion it replaced.
- **An `adjacent` player NEVER moves `gap`, at any maturity.** That is the entire
  point of the split.

### NEVER EXCLUDE a local player

Owner, 2026-08-25: *"Never exclude — the goal is to inform the builder
properly."* Every local player found goes in the ledger. A builder needs to see
who else is in the room, who the buyer already pays, and who could turn and
compete next quarter; the adjacent half of the ledger is **intelligence, not
noise**. Dropping a real firm to protect a score is the register lying by
omission, and the labelled groups exist precisely so that recording one costs
nothing.

### The ARES fallback — when there is no product URL

`url` is optional **against an `ico`**, and that exists because the no-exclude
rule needs it. AML solutions s.r.o. (IČO `10691766`) is a real player on p-0006
with no product URL anywhere in the corpus, and the choice was to drop a real
firm or invent a link. Both are forbidden, so there is a third option: record
the IČO and let the page link the company's public state-register record,

```
https://ares.gov.cz/ekonomicke-subjekty?ico=<ico>
```

which is verifiable and real. `web/lib/data.ts` `localHref()` picks `url` when
present and this otherwise. **Never invent a URL to fill the field.**

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

---

## Figures — the diagrams on a record page

A record page draws a handful of diagrams. **Four of them are DERIVED: they are
read off ledgers you have already written, and you author nothing for them.**
One is AUTHORED, and it is the only one this section asks anything of you.

### Derived — nothing to write, and nothing to fix in the figure

| Figure | Read from | Drawn when |
|---|---|---|
| **The field timeline** | `comps[].since` and `locals[].since` | two or more players carry a `since` |
| **Who's in the room** | `locals[]`, gridded `competes` × `maturity` | the record has a `locals[]` ledger |
| **The comp map** | `comps[].geo` and `comps[].markets` | the comps ledger names a country |
| **The money scale** | `amount_czk` on every `type: price` source | **two or more** price receipts are on file |

The money scale is the one with a threshold, and the threshold is the point: a
scale drawn through a single point is a picture of one number pretending to be
a distribution. One receipt renders as the ledger line it already is.

**If a derived figure draws wrong, the ledger is wrong.** There is no figure to
correct — change `since`, `competes`, `geo` or the price receipt, and the
drawing follows. That is the whole reason these four are derived: a diagram
hand-tuned to look right is a diagram that stops agreeing with the record
underneath it the first time the ledger moves.

### Authored — `process:`, the work as it runs today

`process:` is OPTIONAL and the option is the point.

- **Author it when the record's problem is a WORKFLOW somebody performs today** —
  a report written and then read twice, a back office re-typing paperwork, a
  duty bought in pieces from three different sellers. The figure shows those
  steps and what the suggested solution does to each.
- **SKIP it for a new obligation or a one-off decision with no current process.**
  A hand classification of all 29 live records (2026-09-15) found about twelve
  with nothing to draw: the problem is that a law starts applying, or that a
  buyer has a choice to make, and there is no repeated sequence of steps to
  put in a left-hand column. **Drawing one anyway means inventing it**, which is
  the exact failure the register exists to avoid (MATCH.md §3). No block is the
  honest answer and it costs the page nothing.

### The uncertainty rule — say the quiet part in the data

> Owner, 2026-09-15: *"be SUPER CLEAR about where we're not sure how the
> process looks, put question marks if you don't know."*

**NEVER FILL A GAP WITH A PLAUSIBLE GUESS.** A diagram reads as settled fact
whatever the prose beside it says, so a step drawn confidently because nobody
wrote down that it was a guess is the worst thing this figure can do. Every
step therefore states how its TODAY column is known, in one field:

| `known` | means | `cites` |
|---|---|---|
| `documented` | the step is stated in evidence cited on this record | REQUIRED, non-empty |
| `inferred` | OUR READING of the record's own prose — not stated anywhere | optional: name where the reading comes from |
| `unknown` | we do not know how this step happens; the page draws a **"?"** | FORBIDDEN — a source describing it would make it one of the two above |

`inferred` costs the figure nothing but a dashed line, and `unknown` is a
legitimate, publishable value: "who files the claim is not documented" is a
fact about the evidence, and writing it down is how a reader learns which parts
of the picture are receipts. What is forbidden is the fourth option — writing
the guess as if it were the first.

### The contract

```yaml
process:
  summary:
    today: '<ONE plain sentence: how the work runs today. REQUIRED.
             May carry [Sn] markers, which must resolve.>'
    after:  '<ONE plain sentence on the process with the solution applied.
             OPTIONAL — write it only when it says something the `solution:`
             sentence does not. NO citations, no certainty words.>'
  steps:                       # at least 2; one step is a sentence, not a process
  - who: Coder                 # who does it today, in plain words; '?' when unknown
    today: 'Reads the report again to produce the codes the insurer pays on'
    known: documented          # documented | inferred | unknown
    cites: [3]                 # S-numbers into sources[]; [] when none, never absent
    reenters: true             # OPTIONAL — this step re-types or re-reads what
                               # someone already wrote. Forbidden on a `new` step.
    change: changes            # stays | changes | goes | new
    after: 'Confirms the insurer codes proposed from the report''s own data'
```

- **`today` is null EXACTLY when `change: new`** — a step the solution adds has
  no today, and every other step has one.
- **`after` is null EXACTLY when `change: goes`** — a step the solution removes
  has no after, and every other step survives into the box.
- **`after` is the proposal and carries NO citation, ever.** Not in a step, not
  in `summary.after`. The record holds evidence for the problem; it holds none
  for our answer to it, and an `[Sn]` there dresses a proposal as a finding.
- **On a `new` step, `who` is who would do it with the solution** — there is
  nobody doing it now, and `known` says how sure we are of that (usually
  `inferred`).
- **One field, one meaning (CLAUDE.md rule 1).** The block describes the
  workflow and nothing else. A crown figure belongs on a `type: price` receipt,
  which carries the payer, the unit and the basis that make a number checkable;
  a competitor belongs on `comps[]` or `locals[]`, which carry the maturity
  test. `scripts/check-records.py` refuses both inside the figure — name the
  ROLE instead ("the dispatch software", "a compliance-documents seller").
- Every rule above is an ERROR in `python3 scripts/check-records.py --strict`,
  which runs inside `npm run build`. `web/lib/data.ts` types the same shape in
  zod.

### Where it lands on the page

The page reads the record in this order, and the figure is split across two of
the three:

1. **The problem** — the full argument, unchanged: the lead paragraphs, Why
   now, Who pays, Existing non-solutions, Solved elsewhere.
2. **The process today** — `summary.today`, then the steps' TODAY column. This
   is still the problem section's job: it is what the reader is being shown is
   wrong.
3. **The Suggested solution box** — the `solution:` sentence, and inside the
   same box the steps with the solution applied (the AFTER column), plus
   `summary.after` where one is written.

So the same list of steps is drawn twice, once on each side of the box. Write
each pair so it reads across: the `after` answers its own `today`, in the same
grammar, at the same length.

### A worked example (p-0010, trucking back office)

```yaml
process:
  summary:
    today: 'A dispatcher arranges each load by phone, and someone in the office re-types the delivery note and the CMR consignment note and chases the invoice and the factoring by hand [S2].'
  steps:
  - who: Dispatcher
    today: 'Arranges each load by phone'
    known: documented
    cites: [2]
    change: stays
    after: 'Unchanged — the suggested solution reads the paperwork, it does not take the call'
  - who: '?'
    today: 'How the signed delivery note and CMR get from the delivery point back to the office is not known'
    known: unknown
    cites: []
    change: changes
    after: 'The driver captures the delivery note and the CMR where the load is delivered'
  - who: The office
    today: 'Someone re-types the delivery note and the CMR consignment note'
    known: documented
    cites: [2]
    reenters: true
    change: changes
    after: 'The delivered load''s own delivery note and CMR are read instead of re-typed'
  - who: The office
    today: 'Invoices and the factoring paperwork are chased by hand'
    known: documented
    cites: [2]
    change: changes
    after: 'Those same two documents become the invoice'
  - who: The back office
    today: null
    known: inferred
    cites: [11]
    change: new
    after: 'The delivery note and the CMR are kept in the electronic form authorities must accept from 9 July 2027'
```

Read what that example does NOT do. It does not claim the office re-types the
invoice as well — the record says the invoicing is "chased by hand" and nothing
more, so no `reenters` is set on that step. It does not guess how the signed
paperwork travels back from the delivery point, a step every haulier plainly
performs and no source on the record describes: that step is `unknown`, carries
no cites, and the page prints a "?". And the last step is `inferred` rather than
`documented`, because the source behind it says only that the named incumbent
does not do this — which is our reading that nobody does, not a finding that
nobody does.

**`summary.after` is absent from that example on purpose.** p-0010's `solution:`
sentence already says the documents become the invoice and go onto the
electronic footing; a summary repeating it would be the same sentence printed
twice in the same box. Write `summary.after` only where it adds what `solution:`
does not — p-0008 writes one because the shape of its answer (three sellers
collapsing into one) is not in its solution sentence.

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
