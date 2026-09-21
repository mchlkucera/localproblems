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

Since 2026-09-04 it also holds `ms21-public-projects.jsonl` (26,048 rows,
22.9 MB, from the MMR open-data export of approved EU-fund projects, CC BY
4.0): every PUBLIC-BODY beneficiary with its IČO, region, the money committed,
and — where the applicant wrote one rather than a placeholder — the problem
that project was funded to solve. **It is a lookup and not a feed, and the
reason is the `smlouvy` reason**: 40,988 projects carrying real money would
pass materiality and bury a 16,000-record ledger, so this tree holds it and
`scripts/ms21_query.py` searches it. Its consumers are the `price` receipt
(what a named Czech public buyer actually paid) and the `gap` check (who has
already been funded to build this). Only 10,834 of the 26,048 rows carry a
real `<PROBLEM>` statement — 7,885 say `-` and 7,329 say `nerelevantní` — and
the placeholders are OMITTED rather than written into a field called
`problem`, because an empty string in a problem field is the shape that looks
present and says nothing.

Since 2026-09-05 it also holds `cityvizor-invoices.jsonl` (80,286 rows,
30,149,595 bytes = 28.75 MiB, from CityVizor's public invoice API — the
accounting ledgers 26 municipalities and regions publish voluntarily): one
line per PURCHASE invoice line — rozpočtová položka 504x/51xx/61xx only;
transfers, payroll, income lines and credit notes are counted and dropped —
with the paying body, the counterparty's IČO (on 99.4% of rows), the amount,
the booking date, the ledger's free-text description and the budget
paragraph/item. It is the executed-spend counterpart of the ms21 file: what a
named body ACTUALLY PAID a named counterparty for a thing, below every tender
threshold. **It is a lookup and not a feed, for the ms21 reason squared**:
the same 26 bodies book ~150,000 purchase lines in two years, every one
carrying real money. It is also SHORTER than two years by measurement — two
years is ~54 MB and the 30 MB ceiling is the stop rule for a committed,
never-pruned tree — so `scripts/cityvizor_index.py` keeps whole months,
newest first, and trims the oldest month across ALL bodies until the file
fits: 2025-07-01 … 2026-08-31 today, ten months trimmed, the kept window
printed by `scripts/fetch_cityvizor.sh` and written into its receipt. Its
consumer is the `price` receipt, searched by `scripts/cityvizor_query.py`;
the url a citation gets is the body's per-MONTH invoice page
(`cityvizor.cz/<slug>/faktury;rok=Y;mesic=M`), shared by every line of that
month because the public view exposes no invoice id — the constant-url shape
again, with the row `id` in `note` as the identifying key.

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
  mpsv (MPSV/ÚP `volna-mista` open data). Live since 2026-08-24.
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
- `asks` — direct asks from problem owners: a named institution states a
  problem it wants solved before money is attached: tacr (TA ČR research
  needs, scripts/fetch_tacr.sh) and hackathon (owner-set challenge statements
  from six organizer sites, scripts/fetch_hackathons.sh) and nen-ptk (the
  state procurement portal's PRE-TENDER MARKET CONSULTATIONS — a public buyer
  describing a need before it writes a specification, which is the earliest
  point at which a buyer with budget says what it cannot do today,
  scripts/fetch_nen_ptk.sh). NOT student-picked
  hackathon topics, NOT petitions. Registered and first records landed
  2026-09-03. The first cut (32 rows) was REWRITTEN the same night under
  the owner's admission rules and is recorded in data/raw/2026-09-03/
  manifest.md: an owner must be named by the page (no organizer fallback),
  a row must state a problem (no bare topic lines), the `stated_need` bar
  admits only a concrete need a builder could start on, and an event date
  is not urgency. 39 staged -> 16 landed (11 challenges, 5 needs); 19
  refused by the stated-need bar (themes, open calls, a vendor pitch,
  ministries' own priority studies), 4 dropped at scale 0.
  The record is the statement and who made it — `owner`, required on this
  ledger and on no other; prizes, team counts and winners are never
  recorded, for the engagement-is-not-pain reason above.
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
            · tacr- (the TA ČR need id, the TT code, lowercased)
            · nenptk- (the NEN contract code, e.g. nenptk-n006-26-p00000122)
            · hack- (sha1-8 of site + "|" + challenge title — the six pages
            are re-read every run, so the id must come from the statement,
            not from the run)
source      fetch provenance: ted | hlidac | yc | round | reg-scan | arb-scan |
            demand-scan | suggest | reddit | feed | mpsv | coi | sukl | nen |
            smlouvy | dotace (dotace-scan agent harvests of grant/subsidy
            calls, prefix dotace-; a grant record fetched via the Hlídač
            dotace API stays `hlidac` — provenance, not topic) | veklep
            (the legislative e-library via the Hlídač dataset mirror — a new
            PUBLISHER, the ODok portal, not merely a new script, which is
            what earns it a value where ec-hys and nku did not take one) |
            tacr (TA ČR's own needs feed — a new PUBLISHER, the agency that
            runs the BETA programmes) | hackathon (the organizers' own event
            pages — a new PUBLISHER, the hospital, city or ministry that set
            the challenge; the ledger is `asks`, and the owner is the
            record's `owner` field, never the source value. For one day
            (2026-09-03) it rode on `notes: owner: …`, because
            `entity_native` is a staging field the append allowlist drops —
            and that day proved the point: a fact inside free text reached
            no validator and no page, so it is a first-class field now)
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
geo_origin  where the signal comes FROM: an ISO2 country code, `EU`, or `XX`
            when the source names no country. `XX` is ISO 3166-1 USER-ASSIGNED,
            so it collides with no real country now or ever.
money_eur   number | null (best-effort EUR value) + money_note (how derived)
summary     max 2 sentences, EN
scores      objective, mechanical — see rubric below
notes       optional free text: transfer logic, quotes, and anything not
            carried by a field of its own
cz_check    optional — THE CZECH ABSENCE VERDICT, structured. Written by
            `arb-scan` and absent elsewhere. See "The Czech absence check"
            below; the schema and its invariant are in web/lib/data.ts
            (CzCheckSchema), which is where they run
owner       who stated the problem: the institution named as the setter of an
            ask. REQUIRED on every `asks` record, absent elsewhere. Its own
            field, never a `notes: owner: …` prefix — one field, one meaning:
            `notes` is free text, and a fact riding inside it was read by no
            validator and rendered on no page. Gated in scripts/db.py
            check_owner() on both write paths, so an `asks` line without it,
            or any other line with it, red-builds the site. Rendered in the
            ledger's Source cell as `{source label} · {owner}`.
quote       optional — a VERBATIM snippet of the fetched payload (see below)
http_status optional — integer; liveness of `url` at its last check
fetched_at  optional — ISO timestamp of the payload this record came from
extraction  optional — structured | llm-fallback | manual
```

`geo_origin: XX` — **THE EXPLICIT UNKNOWN (added 2026-09-21).** There was no
spelling for "the source names no country", so agents wrote `US`, and `US` then
meant both *American* and *unknown* — one field, two meanings, the defect
`pipeline/MATCH.md` §0 exists to prevent. It was flagged on 2026-09-19,
recurred on 2026-09-21, and was reported independently by three scoring agents.
Write `XX` when the payload names no origin; never guess a country to fill the
field (§3: receipts over plausibility). Note that the regex always matched `XX`
letter for letter — nothing was blocked, the VALUE WAS SIMPLY NEVER DECLARED,
which is why it was never used. It renders as "Not stated", never as a country
code (`web/lib/format.ts`). **Existing ledger lines are NOT retro-edited**: the
ledgers are append-only and we cannot now recover which `US` meant unknown; an
errata class covers that cleanup.

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
`money <= 1 AND scale <= 1 AND urgency == 0`; for `asks` the scale bar is
`scale <= 0` — an owner-set ask at niche scale is material, one body's own
internal need is not (owner, 2026-09-03). The asks extractors stage no
`urgency_date`: a hackathon's event date or a consultation date is not a
deadline on the problem, and letting it score urgency was one field carrying
two meanings. No region judgment at normalize.

## Region layer — data/problems/<region>/

One markdown file per problem: `p-NNNN-<slug>.md`. A problem is uniquely
`<region>/<id>`; each region has its own p-NNNN namespace. Frontmatter:
```
id, region, title, brief? (one cited sentence: the situation), solution (one plain
sentence: the likely solution), good_for? (one line: who it suits), draft_law? (one
cited line: the unpassed law the main pain depends on), category
(sector list above), geo, score (0-12),
scores {proof 0-3, money 0-2, urgency 0-3, demand 0-2, gap 0-2},
status: candidate | active | watching | stale | claimed | solved | rejected,
entry {level, buyer, permission, incumbents, integration, money, why},
comps [{name, url, geo, since, traction, signal?: <evidence id>, markets?: [ISO2..]}],
locals? [{name, url?, ico?, since, competes: direct|adjacent,
          maturity: established|early, evidence}],   (url? — one of url/ico)
process? {summary {today, after?},
          steps [{who, today, known, cites, reenters?, change, after}]},
sources [{type, url, note, date, name?, gist?, why?, signal?: <evidence id>,
          dims?: [dimension..],
          payer?, amount_czk?, unit?, basis?}],   (all four REQUIRED on type: price,
                                                   forbidden on every other type)
created, updated
```

An UNPRICED record says where to look. `price_search:` on a problem record is
one sentence naming the surfaces and the keyword — never an amount; the
checker refuses a crown figure in it (owner, 2026-09-04: "we can give an
estimate of where we think we should search for it"). The page prints it
beside the absence line, and the line disappears the day a `type: price`
receipt lands.

`sources[].name` / `gist` / `why` — the public face of a source (`note` is the
internal receipt and never renders). `name` is the display name the ledger row
links. `gist` is the clerk's few-word label on the ledger row — 2–6 words,
optional (owner, 2026-08-25: "even the link explanations are too long"). `why`
is the full plain sentence saying what the source is and why it is cited — with
a `gist` present it moves behind the row's native "more" toggle; without one it
renders in the open, exactly as before.

`sources[].type: price` — the PRICE RECEIPT: what a named Czech buyer actually
pays for THIS product or its manual equivalent (owner ruling, 2026-09-03;
docs/who-pays-audit-2026-09-03.md). It was added because the old MONEY ladder
asked "is public budget nearby?" and never whose pocket the money leaves or
whether it buys this — six of the eight rung-1 records wrote "adjacent" in their
own notes, and every one of the corpus's fourteen Czech price points sat inside
a gap-check, backing `gap`. Since 2026-09-19 it is what MONEY is scored from
(SCORING.md, "is someone paying for this job now?"): a price receipt tagged
`dims: [money]` is the ONLY source that earns a Willing to pay point. Basis
`list-price`, `buyer-interview` or `manual-equivalent` is an ASKING receipt
(rung 1); `signed-contract` or `tender-line` dated within 24 months of
`updated` is a PAID receipt (rung 2). A registr smluv contract or an awarded
tender line that buys THIS job is restated as a price receipt with its payer,
amount, unit and date; a consultant paid to do the job by hand is a
`signed-contract` receipt. No new dimension: the 12-point card stands. A price source carries five REQUIRED fields — `payer` (a
named buyer or a sized segment), `amount_czk` (an unquoted, non-negative number
of crowns; `0` is a real receipt where a free incumbent sets the price), `unit`
(`per-seat-month` · `per-case` · `per-year` · `per-project` · `one-off` ·
`per-hour`), `basis` (`list-price` · `signed-contract` · `tender-line` ·
`buyer-interview` · `manual-equivalent`) and `date` — and a price source
missing any of them FAILS the build (`scripts/check-records.py`, and zod in
`web/lib/data.ts`); the same fields on any other type fail too, because they
would render nothing. It renders under **Willing to pay** as one mono ledger line,
`<payer> pays <amount> CZK <unit> · <basis> · <date>`, linked to the source; a
record scoring ≥ 7 with no price receipt prints the house line `No Czech buyer
has priced this yet.` A price receipt cites **money** only when tagged
`dims: [money]` — a signed public contract can be both — and never proof, gap,
urgency or demand; untagged it backs no score at all. On a record rescored to
the 2026-09-19 ladders (`SCORING_V2_ENFORCED`), money >= 1 without a tagged price
receipt FAILS the build: public money nearby never claims "who pays and how
much". `basis: manual-equivalent` is how an
OPEN field gets priced at all — there is no incumbent page to read a price
from, so the receipt is what the same job costs done by hand.

`solution` — REQUIRED (was the optional `fix`, renamed 2026-09-10), one plain
sentence stating what would likely solve the problem, ALWAYS rendered as `LIKELY
SOLUTION` — never as a known answer. Compression of `## First moves`,
`entry.why` and the solved-elsewhere paragraph, never invention; no Czech/EU
acronym goes in ungloss; no certainty words (check-records.py `OVERCLAIM`).
Where a local incumbent already sells the answer, the sentence describes that
product neutrally — whether the field is open is the gap score's job.

`brief` / `good_for` — THE HEADLINE LINES (OPTIONAL; owner, 2026-09-16). `brief` is ONE
sentence (≤ 25 words) of fact on what is happening and why it is urgent now, every
number or date `[Sn]`-cited and resolving, no proposal, ledger name or certainty word;
`good_for` is one line (≤ 15 words) naming who the opportunity suits by skills and
interests — no numbers, no markers, no market claims. ERRORs in check-records.py
`check_headline`; both ride `problems.extra_json`. Full rules and the headline rule:
`data/RECORD-TEMPLATE.md`, "The headline block".

`draft_law` — THE "DRAFT LAW" BADGE (OPTIONAL; owner, 2026-09-16). Present ONLY when the
record's main pain depends on a law not yet passed or published (a bill, a government
draft, a planned law, or an untransposed EU directive where the pain needs the Czech law);
never for a law in force, a published EU regulation, or a pain that exists today anyway.
One line (≤ 12 words) naming the law and its status, `[Sn]`-cited to a `type: regulation`
source, no certainty words. ERRORs in check-records.py `check_draft_law`; rides
`problems.extra_json`. Full rules: `data/RECORD-TEMPLATE.md`, "`draft_law:`".

`entry` — DIFFICULTY TO ENTER (REQUIRED on every record, rejected ones
included; owner, 2026-09-15). It REPLACES `build` — the stánek→továrna capital
ladder, the `first_revenue` guess and the `builder` team band are retired.
Owner's words: *"get rid of the team predictions"*; *"CAPITAL €10–100k / TEAM
2–5 people is pretty arbitrary, more abstract categories will be more
truthful"*; *"include a clear difficulty to enter — e.g. app for truck people
is easy, entering government healthcare is tough — should be in the index
view"*. A euro band and a headcount were a prediction about a team nobody has
met; these five gates are facts about the market the record already carries
evidence for. Judged from the record's own evidence, never aspirationally:

- `buyer` — who signs the FIRST contract. `small-firms`: SMEs, sole traders,
  households, associations, small installers, privately run care homes.
  `large-firms`: corporates, utilities, banks, insurers, lenders, private
  hospital chains, big distributors. `public`: the state, ministries, agencies,
  municipalities, public hospitals, VaK water utilities owned by towns —
  anything bought under procurement law.
- `permission` — what an entrant must be ALLOWED before selling. `none`: a
  trade licence and nothing else. `registration`: a notification, registration
  or certification obtainable in weeks and rarely refused (a data-protection
  registration, ISO, a supplier qualification). `licence`: an authorisation
  the law requires to SELL THE PRODUCT ITSELF, or a regulated profession's
  monopoly covering the product's core act — placing agency workers under
  zákon 435/2004, giving investment advice under a ČNB licence, the state
  attest a records system must hold before a public body may buy it. **Hiring
  or partnering with a lawyer, accountant or tax adviser as an ingredient of
  the service is a product choice, not a gate — that is `none`** (owner
  amendment, 2026-09-15; applied one way across every record).
- `incumbents` — DERIVED from the `locals[]` ledger, no judgment: any local at
  `competes: direct` AND `maturity: established` ⇒ `direct`; else any at
  `competes: adjacent` AND `maturity: established` ⇒ `adjacent`; else (no
  locals, only early players, or only `competes: non-seller` rows) ⇒ `open`.
  A `non-seller` row carries no `maturity`, so it satisfies neither limb and
  derives `open` exactly as an empty ledger does — recording ČOI costs a record
  nothing, which is what makes the no-exclude rule affordable. The same three
  lines are stated in `SCORING.md` and implemented in `scripts/check-records.py`
  `entry_incumbents`, which asserts the stored value: change all three together
  or the build fails. **It does not move the level** — see the level rule below.
- `integration` — what the product must plug into to work at all. `software`: a
  standalone app, SaaS or marketplace — **including one that reads or writes
  the BUYER'S OWN accounting, ERP, dispatch, HR, records or clinical software**
  (Pohoda, Helios, ABRA, Cygnus, a hospital's own system, a dispatcher's
  planning tool). That is what every business tool does and it is not a gate.
  `national-system`: the product cannot work without connecting to a STATE,
  national or EU system (EDC — the national electricity data hub, the state
  eHealth gateway, the EU deforestation information system, the cadastre and
  its orthophoto, datová schránka filings, ISIR — the insolvency register,
  eRecept) or without hardware or crews in the field (meters, radio readers,
  insulation crews). `certified`: the product ITSELF must pass a certification
  or audit before use (a medical device, a payment institution, e-ID wallet
  acceptance, safety-critical or cybersecurity certification).
- `money` — `bootstrap`: a solo builder or small team can reach the first
  paying customer on their own money. `outside-money`: liquidity, hardware,
  regulatory capital or a long public sales cycle means outside money before
  the first sale. Override the default only with a reason in `why`.
- `level` — DERIVED, and the checker asserts it (see below).
- `why` — one or two plain sentences, house voice, ≤ 320 chars, naming the
  gate(s) that set the level and, where the record's evidence gives one, the
  concrete thing behind it. No certainty words (`check-records.py` `OVERCLAIM`,
  the same regex `solution` is held to). For an `easy` record it says why the
  door is open. It may mention an established player in one clause — that is
  true and useful — but never as the reason for the level.

**THE LEVEL RULE (mechanical, checker-enforced; amended 2026-09-15).** Weights:
buyer `small-firms` 0 / `large-firms` 1 / `public` 2 · permission `none` 0 /
`registration` 1 / `licence` 2 · integration `software` 0 / `national-system` 1
/ `certified` 2 · money `bootstrap` 0 / `outside-money` 2.

- max weight 0 → `easy` · max weight 1 → `moderate` · exactly one gate at 2 →
  `hard` · two or more gates at 2 → `very-hard`

**`incumbents` carries no weight, and that is the rule, not an omission: the
`gap` score already prices established competition, and counting it here too
priced one fact twice** (one field, one meaning — CLAUDE.md rule 1). The first
pass under the unamended rule put 20 of 37 records at hard or very-hard and
turned the owner's own canonical easy example, an app for trucking firms, into
`hard`. Difficulty to enter means the DOORS: who buys, what permission, what
you must plug into, and money.

`level` must equal the derived value and `incumbents` must equal the value
derived from `locals[]`. Both are ERRORs in
`python3 scripts/check-records.py --strict`, which runs inside `npm run build`.
The site never re-derives either: `web/` reads the stored value.

`process` — THE PROCESS FIGURE (OPTIONAL; owner, 2026-09-15). How the work runs
TODAY and what the suggested solution does to each step: a `summary.today`
sentence plus at least two ordered `steps`. **Authored only where the record's
problem is a workflow somebody performs today** — roughly a dozen of the live
records describe a new obligation or a one-off decision instead, have no
process to draw, and carry no block; drawing one for them would mean inventing
it. **Uncertainty is a value here, never a silence** (owner: *"be SUPER CLEAR
about where we're not sure how the process looks, put question marks if you
don't know"*): every step's `known` is `documented` (stated in cited evidence,
`cites` required), `inferred` (our reading of the record's own prose, drawn
dashed) or `unknown` (we do not know, `cites` forbidden, the page draws a "?").
`today` is null exactly on a `change: new` step and `after` exactly on a
`change: goes` one; `after` is the proposal and carries NO citation anywhere,
including `summary.after`, which is optional and written only where it says
what the `solution:` sentence does not. A crown figure or a `comps[]`/`locals[]`
name inside the block is refused — money is a `type: price` receipt and
competition is the ledgers' question (one field, one meaning). Every rule is an
ERROR in `scripts/check-records.py --strict`; the full contract, the page order
and a worked example are in `data/RECORD-TEMPLATE.md`, "Figures". Not a column
in `scripts/db.py`: it rides `problems.extra_json` verbatim.

`comps` — foreign comparables (REQUIRED; the "where it works" ledger): companies
running the model elsewhere, with public verifiable traction. 2–4 entries per
record with foreign proof; `comps: []` is legitimate ONLY where `proof` is 0 and
no comparable exists (build-enforced: proof >= 1 requires >= 1 comp):
- `name`, `url` — the company and its site
- `geo` — HQ country, ISO2 (UK -> GB)
- `since` — founding year, unquoted integer. The schema floor is 1800, not
  1980: the floor's only job is catching a slipped digit, and a floor set at
  the age of the software industry rejects real comparables. Deutsche Leasing
  (founded 1962) finances 85 electric buses and their chargers in Lübeck and
  is the closest comparable p-0046 has; the old floor kept it out of `comps[]`
  and that record scored `proof: 2` instead of 3. The ways round a false floor
  are a false year (§3 forbids it) or a dropped company (§2 forbids it), both
  worse than the bug. Moved 2026-09-21; `locals[].since` moved with it
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
opposite things. Rendered as a ledger under **Market gap** (the reader-facing
name of `gap` since 2026-09-19; anchor `#competition`) — in two
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
- `competes` — `direct` | `adjacent` | `non-seller`. **Does it sell THIS?**
  `direct` = this record's product to this record's buyer. `adjacent` = a real
  player in the neighbourhood selling something else. `non-seller` = a body IN
  THE ROOM that sells nothing at all — a regulator, an inspectorate, a
  ministry, a chamber, a state registry, a university output with no vendor
  behind it. The ONLY field `gap` reads for eligibility, and only `direct`
  counts there.
- `maturity` — `established` | `early`. The established test (below),
  unchanged. It sets the RUNG, once `competes` has decided the entry counts at
  all. **REQUIRED on every row that sells something and FORBIDDEN at
  `competes: non-seller`** — a body that sells nothing has no years selling and
  no customers, so `established` would claim it is in a market it is not in and
  `early` would claim it is young. Neither is true, so the key is absent;
  writing one is an ERROR in `scripts/check-records.py`.
- `evidence` — at `direct`, which limb(s) of the established test this player
  passes, stated so a reader can check it. At `adjacent`, WHAT IT ACTUALLY
  SELLS and why that is not this. At `non-seller`, what the body DOES and why a
  builder needs to know it is in the room — the row moves no score, so that
  sentence is the entire value of the row.
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
point of the split. **Neither does a `non-seller`**, by the same mechanism: the
ladder counts `competes: direct` and nothing else.

`non-seller` was added on 2026-09-21 because the split was still one value
short. The Czech trade inspectorate (ČOI) belongs on p-0048's ledger — a
builder needs to know it is in the room — but it sells nothing, so `maturity`
had no honest value for it and its author left it in prose. That is the
FALSE-ABSENCE half of the defect above, recurring: the same wall, one value
further along. It is not called `enforcer` because `enforcer` names one species
of the class (a state registry enforces nothing, a chamber enforces nothing)
and because it answers a different question from its siblings — `direct` and
`adjacent` say what a player SELLS, `enforcer` would say what kind of BODY it
is, which is a second axis inside one field.

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
- a `locals[]` entry at `competes: non-seller` carrying a `maturity`, or any
  other entry missing one
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
resolvable source ref degrades the rendered scorecard. Under the 2026-09-19
ladders a tender, contract or subsidy that maps to money is PUBLIC MONEY
NEARBY: it renders under Willing to pay and can lift a priced record one rung,
but the point itself needs a `type: price` receipt tagged `dims: [money]`, and
every urgency point needs a `regulation` source (SCORING.md). On a record not
yet rescored, the retired freshness component of urgency still refs the newest
source dated <90 days before the extract; on a rescored one it refs nothing.

`hiring`→demand, and money only as a `type: price` receipt (basis
`manual-equivalent`: the posted wage for doing the job by hand) — **NEVER proof.** A posting at a VC-funded startup is
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

## The Czech absence check — `cz_check` on an `arb-scan` signal

`arb-scan`'s entire job is answering one question: **does a Czech player
already sell this?** Until 2026-09-21 the answer was PROSE inside `notes`, so
nothing validated it — the `owner` defect again, in the field whose whole
purpose is to be read by a machine. It cost two of five verdicts in one week:
`gb-academyai` said *contested* with an established direct seller named in its
own note, and `lt-enforceshield` said *absent* where a direct seller exists.

```
cz_check:
  verdict:  absent | contested | taken
  queries:  [ … ]            the Czech query SHAPES actually run
  surfaces: [ … ]            where it looked: google-cz, ares, own ledgers, …
  control:  { query, found, passed }      the positive control (MATCH.md §4)
  players:  [ { name, ico?, url?, competes, maturity?, evidence } ]
```

`players[]` uses **the same `competes` / `maturity` vocabulary as
`locals[]`** — deliberately, so the evidence layer and the record layer cannot
describe one market on two different axes, and so the verdict can be checked
against the players on the ladder `SCORING.md`'s GAP actually reads.

**OPTIONAL, AND PERMANENTLY SO.** Some 6,000 `funded` lines were appended before
it existed and the ledgers are append-only, so a required field here would
red-build the site forever. An absent `cz_check` means no check was recorded —
the honest state, and never a score.

**The invariant, and where it runs.** `SignalSchema` in `web/lib/data.ts`
(`CzCheckSchema`), which both loaders parse every ledger line through, so a
contradiction fails `npm run build`. NOT `scripts/check-records.py`: that file
reads records, not signals, and a rule filed where it cannot run is the prose
this register does not count as enforcement. It fails a line on:

| rule | why |
|---|---|
| `taken` requires ≥ 1 player at `direct` + `established` | TAKEN is GAP rung 0 and needs the player that closed the space |
| `contested` requires ≥ 1 `direct` and NONE at `direct` + `established` | contested is "sellers, all early"; an established seller is `taken` |
| `absent` requires ZERO `direct` players | a seller found makes it contested or taken; adjacent and non-seller rows move nothing |
| `control.passed` must be `true` | a negative with no passing control is worth nothing (MATCH.md §4) |
| `absent` / `contested` need ≥ 2 `queries` | one query shape returning nothing is not evidence of absence (§6). `taken` asserts a positive and is finished when the seller is named |

**WHAT IT CATCHES AND WHAT IT CANNOT — stated because an overclaimed gate is
how a register stops checking.** It catches a verdict that contradicts **the
players the check itself recorded**: `gb-academyai` fails it. It does NOT and
cannot catch **a player the search never found** — `lt-enforceshield` recorded
no seller because it saw none, and no schema knows about a company nobody
looked at. That is what actually killed both of this week's verdicts, and no
checker will ever fix it; only the search will. The existing defence against
that real risk is elsewhere and **it held this week**: `SCORING.md`'s GAP
ladder makes rung 2 cost its own `type: gap-check` source ON THE RECORD, with
`queries[]`, `checked[]` and a passing positive control, so an arb-scan verdict
never becomes a score by itself.

On a failed control, write the miss in `notes` beside the method that broke and
omit `cz_check` entirely — "it has not found an absence; it has found a broken
method. Say so and write nothing." A recorded control MISS is worth more than a
clean negative, but it is not a verdict.

**Before the first `cz_check` line is appended**, the key must also be added to
`LEDGER_ALLOWLIST` in `scripts/normalize.py` — that allowlist drops every field
it does not name, which is exactly how the `asks` `owner` fact ended up riding
inside `notes` for a day. Schema first, allowlist second, record third.

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


---

## Correcting a judgment of ours — `data/errata.jsonl`, class `our-judgment`

The signal ledgers are append-only and public, so nothing in `data/signals/**`
is ever edited. A wrong VALUE is corrected on read by a line in
`data/errata.jsonl`; from 2026-09-21 a wrong JUDGMENT OF OURS is recorded the
same way, under the fourth class, `our-judgment`. The loader is
`load_errata()` in `scripts/db.py` and its docstring is the contract.

**When it applies.** A conclusion we wrote into a signal's prose is wrong: a
CZ-market verdict in `notes`, or a reading of a source that verdict rests on.
Nobody published the claim but us. **When it does not.** Anything a publisher
asserted — those are the three older classes (`our-attribution`,
`disputed-source-value`, `source-updated`). An `our-judgment` entry moves no
money and touches no aggregate.

**Shape**, one line per id, like `source-updated` and for the same reason (a
second line for an id silently replaces the first, and one signal can be wrong
about two things):

```
{"id", "class": "our-judgment", "recorded", "action": "annotate-only",
 "verified_against", "corrections": [{field, kind, claim, ledger_reading,
 our_reading, basis}], "evidence", "impact", "note"}
```

- `kind` is **`verdict`** when the CZ-check conclusion itself is replaced —
  `ledger_reading` and `our_reading` are both one of `taken` / `contested` /
  `absent`, and **any gap score taken from those notes is void** — or
  **`reading`** when a supporting reading is wrong and the verdict survives.
- `claim` locates the assertion inside the notes; `basis` says why the new
  reading is right, in the vocabulary of the ESTABLISHED test where a verdict
  turns on it.
- **No `value_is_correct`, no `field`/`source_value` at the top level.** The
  key is ABSENT, not null: `true` would affirm a publisher's figure this entry
  never checked, and `null` would record a dispute we do not hold. Absent is
  the third state and the loader enforces it.
- `action` is `annotate-only` and nothing applies it on read. Signal `notes`
  are not rendered on any public page (`web/lib/site/ledger.tsx` prints title,
  summary and quote), so the entry exists for the register's own memory and for
  the next agent who reads the signal — never write an `impact` line claiming a
  reader saw the wrong judgment.

**The loader raises, naming the line.** Unknown class, missing
`evidence` / `impact` / `verified_against`, an empty `corrections`, a missing
correction key, a `kind` outside the two, a verdict outside the three words, a
correction that changes nothing, or any `action` other than `annotate-only`
(an `exclude…` action would move money aggregates on the strength of a market
verdict). Read it back with `python3 scripts/db.py errata`.

---

## `data/signals/dropped-log.jsonl` — the materiality-drop memory

data/signals/dropped-log.jsonl — THE MATERIALITY-DROP MEMORY. Committed,
beside `seen.txt`, and the pipeline's second cross-run memory. One JSON line
per DISTINCT dropped signal id, folded: a re-drop costs no new line, it moves
`last_seen` and increments `times_dropped`. Written only by
`normalize.py --complete` (INGEST.md 3c). Key order is fixed and is the write
order:
  id · feed · evidence_type · title (<=140 chars) · url ·
  scores {money, scale, urgency} · first_seen · last_seen · times_dropped
`scores` carries the THREE the materiality filter actually reads and not
`recurrence`, which it ignores — one field, one meaning.
A dropped id is deliberately NOT in `seen.txt`: a drop must stay re-mintable,
because a later run may legitimately find the record material. This file is a
memory of the drop, never a suppression of the record.
It is NOT a ledger and no loader reads it as one: `db.py` globs
`data/signals/*/*.jsonl` and `web/lib/data.ts` walks EVIDENCE_TYPES
subdirectories, so a top-level file here is invisible to both. Verified
2026-09-21 — db-gate green with the file present.
