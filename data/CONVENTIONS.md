# Conventions (v2)

## Sectors (exactly one per signal and per problem)
fintech, health, housing, energy, mobility, govtech, retail-services, b2b,
legal-compliance, education, environment, other

## Evidence layer — data/signals/

One JSONL file per evidence type per run date: `data/signals/<type>/<run-date>.jsonl`,
append-only, committed to git. `data/signals/seen.txt` = one canonical id per
line, sorted — the dedup index.

**`seen.txt` IS ID-KEYED AND THAT IS NOT THE ONLY WAY A RECORD DUPLICATES.** The
same resource harvested twice under two id conventions is invisible to it, and
that is not hypothetical: on 2026-08-21 a staged run held 20 `echys-<id>`
records naming the identical Commission page as an existing `consult-<slug>`
record, and 30 `nku-k<code>` records naming the same NKÚ audit conclusion as an
existing `nku-<topic>` record. So `scripts/normalize.py` runs a SECOND dedup
axis, on identity keys, at both staging and `--complete`. Two things about it
are binding:

- **A key is identifying only where it is unique.** A key value carried by more
  than one record — on either side — is a listing page, a dataset landing page
  or a round-up, and is EXEMPTED rather than merged. This is measured, not
  assumed: 67 urls in the committed corpus are shared by 571 records (6.1%),
  one Vestbee round-up being the cited url of 32 distinct funding rounds, and
  `coi` / `sukl` / `mpsv` emit whole aggregate families under one constant
  dataset url BY DESIGN. Merging on url alone would delete 504 real records.
- **Nothing is dropped quietly.** Every skip names both ids and the url, on the
  console and in the run manifest; every exemption names its reason. A silent
  drop and a silent duplicate are equally invisible.

## Lookup layer — data/lookup/

A THIRD tree, and deliberately not a variant of the other two. `data/raw/` is
gitignored and pruned at 28 days; `data/signals/` is the canonical append-only
ledger and every id prefix in it must be claimed by a registry row (AC-F3).
An enrichment corpus is neither: it is a rebuildable-but-expensive lookup table
that has no evidence type, no date, no score, and no business being in a signal
ledger — filing `shoptet-partner-104` under `data/signals/` would create an
orphan id prefix and fail the build for everyone.

So: `data/lookup/<name>.jsonl`, COMMITTED, never pruned, never walked by
`scripts/db.py`, `web/lib/data.ts` or the build gate (verified 2026-08-21 —
all three walk only `data/signals/`, `data/problems/` and `data/raw/`).
Rewritten in place by its fetcher rather than appended to, because it describes
a CURRENT population and not a sequence of events. Today it holds
`cz-eshop-addons.jsonl` (606 add-ons) and `cz-eshop-vendors.jsonl` (179
vendors), written by `scripts/fetch_shoptet.sh` and `scripts/fetch_upgates.sh`,
and its consumer is the `gap` check — it is what makes
`checked: [eshop-addon-marketplaces]` a claim we can back.

**Which date is `<run-date>`:** the date naming the `data/raw/<run-date>/` directory the
records were completed from — never the wall clock. An attended completion routinely
happens a day or more after the fetch, and naming the ledger from the clock would file one
staged batch under two different names on two different days. `SPEC.md` §3 is authoritative
here and uses `<run-date>` throughout; `pipeline/INGEST.md` step 4 states the same rule
operationally.

Evidence types and their feeds:
- `funded` — companies founded/financed: yc, round, arb-scan (foreign-market scans)
- `regulation` — regulatory triggers with dates: reg-scan; plus the fetched
  feed veklep (the government's legislative e-library via the Hlídač dataset
  mirror, scripts/fetch_veklep.sh — every draft carries a mandatory RIA whose
  first section is a state-authored problem definition; the script stages
  metadata + links, the RIA reading is the model half's / reg-scan's job)
- `tenders` — tenders, grants, public contracts: ted, hlidac, smlouvy (the
  state's OWN daily bulk dump of registr smluv, scripts/fetch_smlouvy.sh) and
  nen (below-threshold contracts via ISVZ open data — REGISTERED and PARKED,
  see data/feeds.json). `smlouvy` reads the same register `hlidac` reads, and
  keeps its own `smlouvy-` prefix rather than reusing `hlidac-`, because
  `source` is FETCH PROVENANCE: a record pulled from data.smlouvy.gov.cz that
  says `hlidac` is a false receipt. The overlap that creates is handled at
  ingest by the identity-key dedup in scripts/normalize.py, not by pretending
  the two feeds are one.
- `demand` — bottom-up documented complaints and unmet needs (NKÚ audit
  findings, ombudsman reports, civic complaint data, chamber/NGO surveys,
  consultations): demand-scan research harvests; plus fetched feeds: suggest
  (Google Suggest pain completions, scripts/fetch_suggest.sh) and reddit
  (CZ-subreddit pain search, scripts/fetch_reddit.sh). Suggest/reddit items
  need PAIN LANGUAGE (complaints, failures, workarounds) — engagement metrics
  never justify a record, and no single feed may dominate the ledger.
- `hiring` — employers committing their own budget to a dated, specific need:
  mpsv (MPSV/ÚP `volna-mista` open data). REGISTERED, no records yet.
  Recorded as AGGREGATES (by theme, or by theme × IČO), never one row per
  vacancy: a single posting scores `money` 1 and is filtered out of
  existence by materiality, so a per-posting feed would fetch thousands of
  items a week and write approximately none of them while looking like it
  ran correctly. AGGREGATE BEFORE THE MATERIALITY FILTER. An individual
  posting is recorded only when the posting itself is the evidence — a
  named employer staffing a specific compliance wave.
  `hiring` is a separate type rather than part of `demand` for the same
  reason stated above: it is high-volume, and folding it in would let one
  feed dominate that ledger.
- `bootstrapped` — RESERVED (indie-hacker/revenue signals); create only when a
  fetchable source exists

Record schema (one JSON object per line):
```
id          canonical <prefix>-<nativeid>; v1 ids grandfathered unchanged.
            Prefixes: ted- · hlidac- · yc- · round- · reg- · feed- (sha1-8 of
            URL) · arb-scan uses the ISO2 of the origin country (de-, dk-, pl-)
            · demand-scan uses the reporting body (nku-, ombud-, civic-,
            chamber-, uni-, ngo-, consult-) · suggest- (sha1-8 of the query)
            · reddit- (post id) · mpsv- (the aggregate key, NOT a url or
            content hash: mpsv-<YYYY-MM>-<theme> or
            mpsv-<YYYY-MM>-<ico>-<theme>. Reposting is the whole problem —
            the same vacancy reappears for months, so any id derived from
            the posting itself defeats the dedup index)
            · smlouvy- (the registr-smluv idVerze) · nen- (the NEN code)
            · coi- (coi-<YYYY-Hn>-<act slug>) and sukl- (sukl-<YYYY-MM>-<ATC
            group>) — both AGGREGATE keys, for the `hiring` reason above
            · echys- (the Commission initiative id) · roundup- (a Vestbee
            round-up article awaiting a split into per-round records)
            · dotace- (dotace-scan: the programme + call number or a stable
            slug of the call, e.g. dotace-npo-31-24-138-pobytove-sluzby)
            · veklep- (the ODok material PID, e.g. veklep-KORNDVKKWEK9 —
            native id, case preserved)
source      fetch provenance: ted | hlidac | yc | round | reg-scan | arb-scan |
            demand-scan | suggest | reddit | feed | mpsv | coi | sukl | nen |
            smlouvy | dotace (dotace-scan agent harvests of grant/subsidy
            calls, prefix dotace-; a grant record fetched via the Hlídač
            dotace API stays `hlidac` — provenance, not topic) | veklep
            (the legislative e-library via the Hlídač dataset mirror — a new
            PUBLISHER, the ODok portal, not merely a new script, which is
            what earns it a value where ec-hys and nku did not take one)
            THIS LIST IS AN ENUM IN web/lib/data.ts (SignalSchema.source) AND
            A LEDGER LINE CARRYING AN UNLISTED VALUE RED-BUILDS THE SITE.
            Widen the enum in a commit BEFORE the first record lands, never in
            the same one and never after: the ledgers are append-only, so a
            record written against a schema that does not accept it blocks
            every deploy until someone edits a file that must not be edited.
            NOT EVERY FEED NEEDS A NEW VALUE, and most should not take one.
            ec-hys writes `reg-scan`, nku writes `demand-scan` and vestbee
            writes `round`, because each is a new FETCHER for a provenance the
            corpus already has. A new value is for a new publisher, not a new
            script.
url         primary source URL
date        native ISO date of the signal
title       short English display name, "Thing — what it is"
sector      one of the sectors above
geo_origin  where the signal comes FROM: ISO2 or EU
money_eur   number | null (best-effort EUR value) + money_note (how derived)
summary     max 2 sentences, EN
scores      objective, mechanical — see rubric below
notes       optional free text: absence checks, transfer logic, quotes
quote       optional — a VERBATIM snippet of the fetched payload (see below)
http_status optional — integer; liveness of `url` at its last check
fetched_at  optional — ISO timestamp of the payload this record came from
extraction  optional — structured | llm-fallback | manual
```

The last four are **receipts**: they let a record be checked mechanically instead of
trusted. **Any optional field written here must be added to `SignalSchema`
(`web/lib/data.ts`) in the same change** — the schema is a `z.strictObject` (top level and
the nested `scores`), so an unknown key is a **build failure**, loudly, rather than a key
silently dropped on its way to the site. Omit a receipt key entirely when you have no
value for it: an empty `quote` is not a quote, it is the shape that looks present and says
nothing, and the schema rejects it.

`quote` — **a flat string, and its shape is a contract, not an internal choice.** The
inline-source-citations program consumes it (see the reveal seam under Citations below)
and will not block on us, so it has to be right the first time. The required shape is a
verbatim snippet plus the source it came from, retrievable by signal id — and a flat
string on the signal record satisfies all three with no added structure: the record's own
`id` supplies retrievability, its `url` supplies attribution, and the snippet travels with
both on one JSONL line. **No nested object, no quote array, no separate quote store.**
Anything richer is structure the consumer did not ask for and cannot rely on; anything
flatter loses the attribution. Multiple quotes per signal would be a schema change
negotiated with them, never a unilateral one.

Format law: ≤300 chars, **verbatim**, native language preserved, whitespace collapsed, no
ellipsis inside a number. Capturable **only at ingest**, because `data/raw/` is gitignored
and pruned at 28 days — by the time anyone wants to verify a claim, the source text is
gone. For scripted feeds, ingest REFUSES to append a record whose `quote` is not a literal
substring of the fetched payload after whitespace collapse; for agent harvests the payload
is prose an agent read, so it degrades to a manifest warning. That asymmetry is stated
rather than hidden.

`extraction` — how the record was produced. `structured` = a parser (jq / regex / CSV /
RSS) read declared fields. `llm-fallback` = the structured parse violated its contract and
a model recovered records from the raw payload; these are counted in the run summary and
marked on the ledger, because a recovered record is weaker evidence than a parsed one.
`manual` = an agent harvest.

Objective scores (0–3 integers, set at normalize time, region-blind):
- `scale` — entities the underlying need touches: 0 one org · 1 niche segment ·
  2 a sector · 3 economy-wide/cross-sector
- `money` — attached EUR: 0 none/unknown · 1 <200k · 2 200k–2M · 3 >2M
- `urgency` — 0 none · 1 dated event >18mo out · 2 <18mo · 3 <6mo or already
  in force with active enforcement
- `recurrence` — 0 one-off event · 1 probably repeatable · 2 recurring need
  (annual/continuous) · 3 structural (mandated forever)

Materiality filter (the ONLY normalize-time filter): drop only if
`money <= 1 AND scale <= 1 AND urgency == 0`. No region judgment at normalize.

## Region layer — data/problems/<region>/

One markdown file per problem: `p-NNNN-<slug>.md`. A problem is uniquely
`<region>/<id>`; each region has its own p-NNNN namespace. Frontmatter:
```
id, region, title, fix? (one plain sentence: the proposed product), category
(sector list above), geo, score (0-12),
scores {proof 0-3, money 0-2, urgency 0-3, demand 0-2, gap 0-2},
status: candidate | active | watching | stale | claimed | solved | rejected,
build {capital, first_revenue, builder, note},
comps [{name, url, geo, since, traction, signal?: <evidence id>, markets?: [ISO2..]}],
locals? [{name, url?, ico?, since, competes: direct|adjacent,
          maturity: established|early, evidence}],   (url? — one of url/ico)
sources [{type, url, note, date, name?, gist?, why?, signal?: <evidence id>,
          dims?: [dimension..]}],
created, updated
```

`sources[].name` / `gist` / `why` — the public face of a source (`note` is the
internal receipt and never renders). `name` is the display name the ledger row
links. `gist` is the clerk's few-word label on the ledger row — 2–6 words,
optional (owner, 2026-08-25: "even the link explanations are too long"). `why`
is the full plain sentence saying what the source is and why it is cited — with
a `gist` present it moves behind the row's native "more" toggle; without one it
renders in the open, exactly as before.

`fix` — OPTIONAL, one plain sentence naming the product a builder would build,
rendered under the dek as `WHAT TO BUILD`. Compression of `## First moves` and
`build.note`, never invention; no Czech/EU acronym goes in ungloss. Where a
record has no clear product answer — the argument closes with a named local
incumbent and never says what an entrant would build instead — OMIT the key.
The template renders nothing when it is absent, which is honest; a vague fix is
worse than none.

`build` — the buildability scorecard (REQUIRED on every record): who can build
this, with what, how fast. Judged honestly from the record's own evidence, never
aspirationally:
- `capital` — the stánek→továrna ladder: `kiosk` <€10k · `garage` €10–100k ·
  `funded` €100k–1M · `industrial` >€1M
- `first_revenue` — time to first paying customer: `weeks` · `months` · `year-plus`
- `builder` — who it takes: `solo` · `small-team` (2–5) · `funded-team`
- `note` — one sentence justifying the three calls

`comps` — foreign comparables (REQUIRED; the "where it works" ledger): companies
running the model elsewhere, with public verifiable traction. 2–4 entries per
record with foreign proof; `comps: []` is legitimate ONLY where `proof` is 0 and
no comparable exists (build-enforced: proof >= 1 requires >= 1 comp):
- `name`, `url` — the company and its site
- `geo` — HQ country, ISO2 (UK -> GB)
- `since` — founding year, unquoted integer
- `traction` — funding stage/amount, customers, pricing, revenue — whatever is
  PUBLIC and verifiable, with the source named compactly (e.g. "(Sifted, 2026)").
  Never fabricated; a comp without verifiable numbers records what IS verifiable.
- `signal` — optional ref to an evidence-layer id (reuse `data/signals/funded/`
  first); must resolve (build-enforced)
- `markets?: [ISO2…]` — countries the comparable verifiably operates/sells in
  beyond its HQ; recorded only when sourced (never repeats `geo`; vague claims
  like "15+ countries" get no list)

`locals` — local incumbents (OPTIONAL; the "who already sells this HERE" ledger,
added 2026-08-25). The mirror of `comps`, and it exists because the asymmetry
between the two is what let a bug ship: 69 foreign comparables carried
structured `since` + `traction` while every local player lived as PROSE inside a
gap-check `note:`. A machine could read the foreign half of the register and not
the local half, so `gap` could not be audited and `gap: 0` silently meant two
opposite things. Rendered as a ledger under **Local competition** — in two
labelled groups, `direct` first — with the `Existing non-solutions:` paragraph
underneath it:
- `name` — the company
- `url` — its site. OPTIONAL **if `ico` is present**; at least one of the two is
  required (see "The ARES fallback" below).
- `ico` — optional but STRONGLY PREFERRED, 8 digits as a QUOTED string
  (`'04903783'` — unquoted YAML eats the leading zero). It is what makes the
  claim checkable without a human: `scripts/check-records.py` counts distinct
  public buyers for it in `data/lookup/cz-contract-parties.jsonl`.
- `since` — the year it started selling THIS product, else its founding year;
  unquoted integer, exactly like `comps[].since`. REQUIRED at
  `maturity: established` — the test's first limb is ">= 3 years selling" and
  cannot be evaluated without it. OPTIONAL at `early`, where a small Czech
  vendor often publishes no year at all: state what is verifiable and NEVER
  invent a year to fill the field, exactly as with a comp's headcount.
- `competes` — `direct` | `adjacent`. **Does it sell THIS?** `direct` = this
  record's product to this record's buyer. `adjacent` = a real player in the
  neighbourhood selling something else. The ONLY field `gap` reads for
  eligibility.
- `maturity` — `established` | `early`. The established test (below), unchanged.
  It sets the RUNG, once `competes` has decided the entry counts at all.
- `evidence` — at `direct`, which limb(s) of the established test this player
  passes, stated so a reader can check it. At `adjacent`, WHAT IT ACTUALLY
  SELLS and why that is not this.
- **Omit the key when there is no named local player. NEVER write `locals: []`** —
  `problem_locals` is a child table and cannot tell an empty list from an absent
  key, so the two loaders would disagree about the record. `scripts/db.py`
  refuses the empty form outright.

### `competes` + `maturity`: one field per question (2026-08-25)

`status: established | early` lasted one commit. Both content agents hit the
same wall independently: a MATURE Czech firm selling something ADJACENT — the
other side of the counter, a different segment, a service firm rather than a
product vendor — is not `early`, but writing `established` forced `gap: 0` and
stood a record down over a company that does not sell this. One agent wrote
those firms down as `early` (a false maturity claim); the other left them out of
the ledger (a false absence). Two halves of the register encoding the same
situation two different ways — the same one-field-two-meanings defect already
fixed at PROOF rung 2, GAP rung 0 and the SPEC de-rank rule.

**An `adjacent` player NEVER moves `gap`, at any maturity.** That is the entire
point of the split.

### NEVER EXCLUDE a local player

Owner, 2026-08-25: *"Never exclude — the goal is to inform the builder
properly."* Every local player found goes in `locals[]`. A builder needs to see
who else is in the room, who the buyer already pays, and who could turn and
compete next quarter: the adjacent half of the ledger is INTELLIGENCE, not
noise. Dropping a real firm to keep a score is the register lying by omission.
The page renders the two groups separately and counts them ("3 sell this · 4
nearby"), so recording an adjacent player costs a record nothing.

### The ARES fallback — a real player with no product URL

`url` went optional (against an `ico`) because the no-exclude rule needs it:
AML solutions s.r.o., IČO `10691766`, is a real player on p-0006 with no product
URL anywhere in the corpus, and the choice was to drop a real firm or invent a
link. Both are forbidden, so there is a third option — record the IČO, and the
page links the company's public state-register record instead:

    https://ares.gov.cz/ekonomicke-subjekty?ico=<ico>

verifiable, real, and one click for the reader. `web/lib/data.ts` `localHref()`
picks `url` when present and this otherwise. **NEVER invent a URL to fill the
field**; a row with neither `url` nor `ico` fails the build.

### THE ESTABLISHED TEST (SCORING.md, owner 2026-08-25)

> A player is ESTABLISHED when it has been selling for **>= 3 years** AND shows
> at least one of: named customers or a public customer count · **>= 2 distinct
> public buyers** in `data/lookup/cz-contract-parties.jsonl` · funding at
> **Series A or later** · a **state certification, attest or framework listing**.
> Otherwise it is EARLY — funded-but-prototype, solo-operator, pre-customer.

It replaced the v1 "does a company exist?" test, which could not discriminate:
half the signal corpus is "a funded foreign company exists", so 81% of records
were born passing it. Existence is not information; maturity is.

**The same test scores both ledgers, WITH THE SIGN FLIPPED.** Abroad, an
established player is good news — the model is proven and someone already paid
the tuition, and that is what lifts `proof`. Locally, the sign flips: an
established, well-maintained local product **that sells this** means the space is
taken and `gap` is 0. **An EARLY local player does NOT close the space and must
never de-rank a record on its own** — that is `gap: 1`, contested and still
enterable. **An ADJACENT player closes nothing at any maturity**, which is what
`competes` is for.

Every field the test reads is on the record already (`comps[].since`,
`comps[].traction`, `locals[].since`, `locals[].ico`, `locals[].evidence`), so
it is CHECKED BY SCRIPT, not judged — a dimension a machine cannot audit is a
dimension that silently rots. `scripts/check-records.py --strict` runs inside
`npm run build` and fails it on:
- a `maturity: established` entry that cites no limb, or whose `since` is under
  3 years — asked of ADJACENT entries too: "this firm is established" is the
  same claim whichever side of the counter it sells on
- a `locals[]` entry still carrying the RETIRED `status` key, or any other
  unknown key (`LocalSchema` is `z.strictObject`; `scripts/db.py` refuses it as
  well, so a record cannot be half-migrated silently)
- a `locals[]` entry with neither `url` nor `ico`
- `gap: 0` with no `locals[]` entry at `competes: direct` AND
  `maturity: established` — "not checked" is not a score on this ladder; an
  absent check is a missing receipt
- `gap >= 1` while `locals[]` names an established player that sells this
- `gap: 2` while `locals[]` names anyone at `competes: direct`. Adjacent entries
  at rung 2 are FINE — they do not affect the score, and printing them under
  "the field is open" is the point of the split, not a contradiction.
- `gap` at any value with no `type: gap-check` source carrying `queries[]`
- a `proof` score that contradicts the maturity of its own `comps` ledger

The established test runs against the register's own newest `updated`, never the
wall clock — the same reproducibility law `extractDate()` enforces on the site.

## Body shape and length (binding)

A reader arrives at a record with two questions — **what is the problem, and
could I build it** — and must be able to answer both without reading an audit
trail. The body is written to be answerable in one screen, and it is written
that way at creation: trimming 31 records by hand is a one-off, the shape is
what lasts.

**Section order, exactly this, nothing else:**

```
<lead paragraph(s)>            the problem
Why now: …                     the window
Who pays: …                    how big (first sentence becomes the page dek)
Existing non-solutions: …      closes the problem section
Solved elsewhere: …            where it works
## First moves                 score >= 7 only — 4–6 numbered steps
## Revisions                   the record's own audit trail, at the foot
```

**The lead-ins are LITERAL.** `web/lib/sections.ts` splits the body by matching
`Why now:`, `Who pays:`, `Existing non-solutions`, `Solved elsewhere`,
`## First moves` and `## Revisions` at the start of a paragraph. A paragraph
with no recognised lead-in stays with whichever bucket is open, so a renamed or
dropped lead-in does not error — it silently files prose under the wrong
heading, which has broken a record before. Read that file before touching one.
Never invent a seventh section.

**Length targets** (targets, not build gates — the gate is the evidence):

| Part | Target |
|---|---|
| Argument paragraph | ≤ 60 words |
| Argument prose, whole record | ≤ 300 words |
| Revision entry | ≤ 80 words |
| First moves | 4–6 numbered steps |

Over target, cut connective tissue, restated framing and adjectives.
**Never cut a sentence that carries an `[Sn]` marker** — the markers are the
receipts, and a record that loses them stops being a register entry.

**The gloss law.** The first use of a trade term in rendered prose carries a
plain-language appositive — an em-dash or parenthetical gloss in the same
sentence (`NZÚ — the state renovation subsidy`; `RIA (the mandatory impact
assessment)`). The allowlist in `scripts/check-records.py` (`GLOSS_ALLOWLIST`)
names what a builder is assumed to know — EU, VAT, API and the like — and the
checker flags every other ALL-CAPS token whose first use goes ungloss'd,
WARNING-ONLY: the warnings are the retrofit worklist, never a build failure.

**The argument states the picture as it stands now.** "The 2026-08-13 absence
check found no vendor; the 2026-08-20 re-check overturned it" is revision
prose. In the body write what is true and cite it, then let the revision list
carry who checked what, when, and why they were wrong.

### Revisions (replaces the appended CORRECTION block, 2026-08-21)

The register prints its corrections — that is the whole claim it has over an
LLM guess — but printing them is not the same as leading with them. Until
2026-08-20 each correction was appended as its own `**CORRECTION (date,
tag):**` block after a `---` rule and rendered with a 4px ink left rule; 40 of
them had accumulated across 31 records, and on p-0026 the trail outweighed the
argument it corrected 441 words to 181. **Visible is not the same as dominant.**

```
## Revisions

2026-08-13 · de-rank — The gap check found the position occupied … [S6].
2026-08-20 · evidence audit — Two blocks from this date, merged … [S1,S3].
```

- **ONE ENTRY PER DATE.** A new correction **merges into that date's existing
  entry**; it never appends a second block. Where two corrections assert the
  same thing, fold them into one statement and say in the entry that it is a
  merge ("Two blocks recorded on this date, merged here").
- **Oldest first**, appended at the end — the same append discipline
  `sources[]` uses. No sort step, so no sort to get wrong.
- **Head:** `<ISO date> · <tag> — `. The tag is short (≤ 40 chars), contains
  no em dash, and names the kind of change: `evidence audit` · `gap re-check`
  · `de-rank` · `title sweep` · `fact check` · `money receipted` ·
  `regulation added`. Everything after the first em dash is the entry prose.
- **Cite like the argument.** A revision carries `[Sn]` markers exactly as
  body prose does; they resolve against the same `sources[]` list.
- **Plain prose only.** `web/lib/md.ts` supports `**strong**`, links and
  lists — nothing else. Backticks and single-asterisk italics ship to the
  reader as literal punctuation, and the quiet register the revision list is
  set in does not want bold anyway.
- **NEVER DELETE OR SILENTLY SHRINK A REVISION.** Merging and compressing are
  allowed. Dropping a fact one of them asserts is not: a silent deletion is
  the same sin as the invention it corrected. If a claim is withdrawn, the
  withdrawal is written down.
- **Never hidden.** The list renders on the page, in the reading order, in the
  photocopy — quieter than the argument (`ol.revisions`, design-language
  v1.9), never behind a disclosure.
- Legacy `**CORRECTION (…)` blocks and `Updated <date>` tails still route into
  this list from anywhere in the body, so a stray old-format block lands in
  the revisions ledger rather than leaking into the argument. Do not write new
  ones.

## Citations in the body (binding)

Every factual claim in a record body names the source it came from. The
marker is `[Sn]`, where `n` is the 1-based position of the entry in that
record's `sources:` list — the same number the rendered Sources ledger prints
as row `Sn`. Two sources behind one claim: `[S3,S5]`.

```
…communities lose up to half the value of shared electricity [S2].
The portal launched in July 2024 [S3], and a year on trade press still
reports complications [S4].
```

- The marker sits at the END of the sentence or clause it supports, BEFORE
  the period. Uppercase `S`. `[S3](…)` is a markdown link, never a citation.
- A marker asserts "this source backs this claim". NEVER write one the source
  does not actually support — an invented citation is worse than none.
- A claim with no source on file gets a real `sources[]` entry or stays
  uncited. **APPEND new entries at the end of the list**: S-numbers are
  positional, so inserting in the middle silently renumbers every marker
  after it.
- Prose that links a url already on the ledger gets its marker automatically
  from the url match — no `[Sn]` needed after such a link.
- An `[Sn]` that resolves to nothing renders as literal `[Sn]` text on the
  page and `web/scripts/lint-citations.mjs` prints a `citations: WARN` line
  naming record and marker at build time. **Warning only** — a citation
  defect never blocks a deploy; bad data does.
- Markers are annotation, not re-judgment: adding one never changes `score`,
  `scores` or `status`. It does bump `updated`.

The reveal: hovering, focusing or long-pressing a marker shows the source's
display name, its date, and the record's note on it — a native `title`, no
JavaScript, no new visual device. **Seam (reserved):** when the evidence layer
records a verbatim `quote` on a signal, the reveal prints that quote in place
of the note. Purely additive — the syntax, the ledger and the record files do
not change; only the ingest schema and the composer in `web/lib/md.ts` do.

Scoring: per SCORING.md — every point justified by a sources[] entry; a
tier-3-grade signal alone never creates a problem.

Source `type` → scorecard dimension (rendered by the web app):
arbitrage→proof · tender/contract/subsidy→money · regulation→urgency ·
complaint/news→demand · gap-check→gap. A gap-check note containing the literal
marker "Demand point" also backs demand. When evidence justifies a different
dimension, set an explicit `dims: [..]` list — a scored dimension without a
resolvable source ref degrades the rendered scorecard. The freshness component
of urgency always refs the newest source dated <90 days before the extract.

`hiring`→demand, money — **NEVER proof.** A posting at a VC-funded startup is
downstream of that company's round, so counting both would double-count one
capital event. Hiring evidence is a named local employer committing their own
budget to a dated need — the same evidential class as a tender, which is why it
is not barred by the hierarchy law that keeps capital signals to confirmation
only. Compliance detection from hiring is CORROBORATING evidence, never a
discovery engine: a handful of postings can confirm a problem already evidenced
by a tender and a regulation, and can never find one.

## Gap-check sources

A `type: gap-check` source may carry three optional sibling keys:

```yaml
sources:
  - type: gap-check
    url: https://www.ares.gov.cz/ekonomicke-subjekty?obor=35.14
    note: "No CZ vendor offering settlement/billing for energy communities."
    date: 2026-08-19
    queries:
      - "komunitní energetika zúčtování software"
      - "energy community billing settlement CZ"
    checked: [ares, google-cz, cz-saas-directories]
    expires: 2026-11-17          # date + 90 days, computed once when written
```

`checked` vocabulary — the surfaces actually searched, so an absence claim
states its own coverage instead of asserting a bare negative:

| token | means |
|---|---|
| `ares` | ARES business register searched by NACE/obor |
| `app-stores` | Apple/Google store search for a consumer app |
| `cz-saas-directories` | CZ SaaS/vendor directories |
| `eshop-addon-marketplaces` | the CZ e-commerce add-on marketplaces — `data/lookup/cz-eshop-addons.jsonl`, built by scripts/fetch_shoptet.sh and scripts/fetch_upgates.sh |
| `google-cz` | Czech-language web search, `hl=cs` |
| `startupjobs` | StartupJobs.cz / hiring signals for a CZ player |
| `own-funded-ledger` | our own `data/signals/funded/` searched for a CZ entrant |

**A NEW TOKEN, NOT A WIDENED `app-stores`.** The add-on marketplaces raised a
real question: `app-stores` is defined as "Apple/Google store search for a
consumer app", which does not literally cover a platform add-on marketplace, and
the token has been used 0 times. Stretching the definition to cover both was the
cheap fix and is the wrong one. THE WHOLE POINT OF THIS VOCABULARY is that an
absence claim states its own coverage; "I searched the app stores" and "I
searched the Shoptet and Upgates add-on catalogues" are claims about two
different populations, and a reader who cannot tell which was searched has been
told nothing. One token per surface, and `app-stores` keeps its literal meaning.
Adding a token is a SAME-CHANGE EDIT IN TWO FILES: this table and the
`GAP_CHECKED` enum in web/lib/data.ts, which is closed on purpose so a typo
fails the build loudly instead of quietly reading as a surface nobody searched.

**THE LAW — expiry is display-only.** An expired gap-check flags staleness on
the rendered page and never changes `scores.gap`, never changes `score`, and
never changes `status`. The de-rank rule in SPEC §4 remains the ONLY mechanism
that moves `gap`, and **`SCORING.md` is untouched by any of this.** Decay
compares against the register's own newest `updated`, never the wall clock — a
commit must build identically on any day it is built.

**QUERIES ARE NOW MANDATORY, AT EVERY GAP VALUE.** Since 2026-08-25 every record
needs a `type: gap-check` source carrying `queries[]`, and
`scripts/check-records.py --strict` fails the build without one. The reason is
the rung-0 fix: `gap: 0` used to mean "check not done", so an unchecked record
and a de-ranked one landed on the same number. Rung 0 now means TAKEN and only
TAKEN, which leaves the missing check with nowhere to hide as a score — so it is
caught as the missing receipt it is.

**A retrofit is not a de-rank.** Adding these keys to an existing gap-check is a
metadata addition. If you find yourself researching incumbents while doing it,
you have stopped retrofitting and started de-ranking: stop, leave the record
alone, and hand it to the MATCH agent. The trap is that the intuitive fix IS the
violation — writing the queries you would have run, rather than the ones you did,
makes the higher score *look* justified, and prose review cannot catch it.
**Verify a retrofit by diffing `score` and `scores.gap` numerically, never by
reading.**

**DO NOT TOUCH `note:`. AT ALL.** Not to normalize it, not to reformat it, not
to fix a typo or a plural. The three keys above are added as siblings and
nothing else changes. There is no canonical `note:` prefix — a full census of
all 22 gap-check entries across 20 records finds four families and five distinct
literal strings (`Absence check` 9, `Absence checks` 1, `Gap check` 7, `Quick
check` 3, `Incumbent re-check` 2), none authoritative, several containing
escaped quotes. This is written as a **prohibition rather than a list of shapes
to preserve**, deliberately: a prohibition still holds for the variant nobody
has sampled yet, whereas "preserve prefix X" invites normalizing everything that
is not X. Re-derive the census rather than trusting this paragraph:

```
grep -h -A6 'type: gap-check' data/problems/cz/*.md | grep -o 'note: .*' \
  | awk '{print $1, $2}' | sort | uniq -c | sort -rn
```

## Proving a negative

A gap score is the register's only claim of the form "nobody local does this,"
and it is the claim most likely to be wrong in the way that embarrasses us: a
reader who knows the market names the incumbent in one reply. On 2026-08-20 a
re-check of all sixteen absence claims found **half of them false**, including
four of the five records carrying `gap: 2`. These rules come out of that run.

**THE CORPUS CANNOT SEE THE COMPETITION.** This is first because it invalidates
the intuitive method. The nine vendors found occupying p-0001 and p-0002 —
Enerio, Softlink CEM, EnerCA, ENERGOMETR, CANCOM, Wue, RAYNET, AutoERP, Infina —
return **zero hits across all 6,181 signals**, and so do Průvodka, Apertia and
Bildix. They are bootstrapped SMB software vendors: they never raised, so no
funding feed carries them; they sell to private buyers, so no tender names them.
Our discovery pipeline is aimed at funded startups and public procurement and is
therefore blind to exactly the companies a gap claim is about. **A gap check run
against `data/signals/` alone is not a gap check** — `own-funded-ledger` can
never on its own justify a gap. Only live Czech-language search finds these.

Corollary from the same run: the register held the disproof of its own claim —
**Softlink was named as an incumbent on p-0026 while p-0001 asserted that niche
was empty.** Before asserting an absence, grep the other problem records.

**Search in Czech.** For p-0002 the English query returned no Czech vendor and
the Czech queries returned four. Czech SMB vendors do not describe themselves in
English, and a register that searches in English will keep finding empty markets
that are not empty.

**A negative result is only evidence when the method is known to produce
positives.** Before writing an absence, run the same method at a company known to
exist. The register supplies its own controls — checks that DID find incumbents:
Wultra (p-0017), Softlink (p-0026), Ringil (p-0010). If the method cannot surface
one of those, it has not found an absence; it has found a broken method. Say so
and write nothing. A recorded control MISS is worth more than a clean negative.

**Never receipt a Czech absence with a foreign URL.** Both records de-ranked from
`gap: 2` had cited a foreign company's funding page — `exnaton.com`,
`ycombinator.com/companies/autarc` — as proof no Czech vendor existed. A foreign
company's existence is evidence about that company and nothing else.

**Gap authority is asymmetric.**

| direction | who decides | why |
|---|---|---|
| down (**ESTABLISHED** player that **SELLS THIS** found → `gap: 0`) | any check, immediately | SPEC §4 de-rank rule: name it in `locals[]` at `competes: direct` + `maturity: established`, record `status: watching` |
| down (player that sells this found, all **EARLY** → `gap: 1`) | any check, immediately | it is a contested field, not a closed one — see the established test |
| sideways (**ADJACENT** player found → no change) | any check, immediately | record it in `locals[]` at `competes: adjacent` and say what it sells; it is intelligence, not a competitor |
| up (found nothing → raise) | **nobody** | not-finding-it and not-existing are indistinguishable from where the searcher sits |

**A local player found is not automatically a de-rank to 0.** Since 2026-08-25
the de-rank lands on the rung the two fields put the player on. First ask
`competes`: if it does not sell this, NOTHING MOVES — record it and go on. If it
does, `maturity` decides: an established one takes the space (`gap: 0`), an early
one contests it (`gap: 1`) and closes nothing on its own. Record it in every
case; the ledger is what a builder reads to see who is already in the room.

Not a matter of confidence. A searcher who looked hard and found nothing holds
exactly the evidence of one who searched badly; only the positive control
separates them, and even a passed control proves the method works for the
*control's* market, not this one. Record the coverage, leave the number, hand it
to MATCH. p-0001 and p-0002 are the standing proof: both looked like clean
absences until the queries were run in the right language.

**The title is a claim too.** Ten titles survived a body rewrite still asserting
absences their own records had retracted. A retraction that leaves the claim
standing in the most-read line on the page is not a retraction. When a de-rank
lands, re-read the title before closing the record.

## Adding a new evidence type

Eight steps. **Three are enforced by the build rather than by memory** — which is
the point: the checklist polices itself where it can.

1. `data/CONVENTIONS.md` — add the type to the evidence-type list above, name
   its feeds, and add its id-prefix rule to the record schema.
2. `data/feeds.json` — add the feed(s) with `evidence_type: <new>`, an `access`
   (ToS) verdict and a `contract`. **BUILD-ENFORCED:** every `source` value
   present in `data/signals/**` must be claimed by a registry entry, or the
   build fails and `/sources` would otherwise under-explain the corpus.
3. `data/signals/<type>/` — nothing to do; created on first append.
4. `web/lib/data.ts` — add the type to `EVIDENCE_TYPES`. This one line lights up
   the route via `generateStaticParams`.
5. `web/app/signals/[type]/page.tsx` — add the `TITLES` and `DESCRIPTIONS`
   entries. **BUILD-ENFORCED:** both are `Record<EvidenceType, string>`, so
   step 4 without step 5 is a TypeScript error.
6. `web/lib/data.ts` — add the new `source` key(s) to `SignalSchema`'s `source`
   enum. **BUILD-ENFORCED and loudly:** it is a `z.enum`, so an unknown value
   fails validation immediately. Contrast the optional receipt fields above,
   where forgetting the schema edit produces silence instead — same file, two
   opposite failure modes.
7. `SPEC.md` §3 layout, §5 route table, §5 nav line; and the design skill, which
   is binding and states the ledger list explicitly.
8. `data/feed_health.json` — nothing to do; the feed appears as `PENDING` on its
   first health export, so a registered-but-silent type is visible from day one
   rather than forgotten.

**Steps 1–8 may all land before a single record exists, and `hiring` did exactly
that.** A registered-but-empty type renders its ledger, appears in the nav and
shows as `PENDING` on `/sources` — which is the honest state, not a defect: a
feed that has never produced is then visible from day one instead of forgotten.

**What must NOT run ahead of the rules is the fetcher.** For any source that
carries personal data, the field allowlist and its checker ship BEFORE the first
record can be written, never alongside it. A late fetcher costs nothing; a
rushed one writing personal data into an append-only public log costs
everything, because those ledgers are public and there is no quiet cleanup.
