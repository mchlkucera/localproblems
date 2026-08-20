# Conventions (v2)

## Sectors (exactly one per signal and per problem)
fintech, health, housing, energy, mobility, govtech, retail-services, b2b,
legal-compliance, education, environment, other

## Evidence layer — data/signals/

One JSONL file per evidence type per run date: `data/signals/<type>/<date>.jsonl`,
append-only, committed to git. `data/signals/seen.txt` = one canonical id per
line, sorted — the dedup index.

Evidence types and their feeds:
- `funded` — companies founded/financed: yc, round, arb-scan (foreign-market scans)
- `regulation` — regulatory triggers with dates: reg-scan
- `tenders` — tenders, grants, public contracts: ted, hlidac
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
source      fetch provenance: ted | hlidac | yc | round | reg-scan | arb-scan |
            demand-scan | suggest | reddit | feed | mpsv
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
id, region, title, category (sector list above), geo, score (0-12),
scores {proof 0-3, money 0-2, urgency 0-3, demand 0-2, gap 0-2},
status: candidate | active | watching | stale | claimed | solved | rejected,
build {capital, first_revenue, builder, note},
comps [{name, url, geo, since, traction, signal?: <evidence id>, markets?: [ISO2..]}],
sources [{type, url, note, date, signal?: <evidence id>, dims?: [dimension..]}],
created, updated
```

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
Body: 3–6 paragraphs — problem · why-now · who-pays · existing non-solutions ·
foreign comparables. Corrections are appended after a `---` line, opening with
`**CORRECTION (<date>...):**`.

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
| `google-cz` | Czech-language web search, `hl=cs` |
| `startupjobs` | StartupJobs.cz / hiring signals for a CZ player |
| `own-funded-ledger` | our own `data/signals/funded/` searched for a CZ entrant |

**THE LAW — expiry is display-only.** An expired gap-check flags staleness on
the rendered page and never changes `scores.gap`, never changes `score`, and
never changes `status`. The de-rank rule in SPEC §4 remains the ONLY mechanism
that moves `gap`, and **`SCORING.md` is untouched by any of this.** Decay
compares against the register's own newest `updated`, never the wall clock — a
commit must build identically on any day it is built.

**A retrofit is not a de-rank.** Adding these keys to an existing gap-check is a
metadata addition. If you find yourself researching incumbents while doing it,
you have stopped retrofitting and started de-ranking: stop, leave the record
alone, and hand it to the MATCH agent. The trap is that the intuitive fix IS the
violation — a record scoring `gap: 0` ("CZ incumbent check not done") correctly
has no gap-check source to extend, and "helpfully" creating one requires the
research that moves `gap` upward. Freshly added `queries` would then *look* like
justification for the higher score, so prose review cannot catch it. **Verify a
retrofit by diffing `score` and `scores.gap` numerically, never by reading.**

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
| down (incumbent found → `gap: 0`) | any check, immediately | SPEC §4 de-rank rule: name the incumbent, `status: watching` |
| up (found nothing → raise) | **nobody** | not-finding-it and not-existing are indistinguishable from where the searcher sits |

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
