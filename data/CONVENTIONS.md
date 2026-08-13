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
  consultations): demand-scan research harvests
- `bootstrapped` — RESERVED (indie-hacker/revenue signals); create only when a
  fetchable source exists

Record schema (one JSON object per line):
```
id          canonical <prefix>-<nativeid>; v1 ids grandfathered unchanged.
            Prefixes: ted- · hlidac- · yc- · round- · reg- · feed- (sha1-8 of
            URL) · arb-scan uses the ISO2 of the origin country (de-, dk-, pl-)
            · demand-scan uses the reporting body (nku-, ombud-, civic-,
            chamber-, uni-, ngo-, consult-)
source      fetch provenance: ted | hlidac | yc | round | reg-scan | arb-scan |
            demand-scan | feed
url         primary source URL
date        native ISO date of the signal
title       short English display name, "Thing — what it is"
sector      one of the sectors above
geo_origin  where the signal comes FROM: ISO2 or EU
money_eur   number | null (best-effort EUR value) + money_note (how derived)
summary     max 2 sentences, EN
scores      objective, mechanical — see rubric below
notes       optional free text: absence checks, transfer logic, quotes
```

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
sources [{type, url, note, date, signal?: <evidence id>, dims?: [dimension..]}],
created, updated
```
Body: 3–6 paragraphs — problem · why-now · who-pays · existing non-solutions ·
foreign comparables. Corrections are appended after a `---` line, opening with
`**CORRECTION (<date>...):**`.

Scoring: per SCORING.md — every point justified by a sources[] entry; a
tier-3-grade signal alone never creates a problem.

Source `type` → scorecard dimension (rendered by the web app):
arbitrage→proof · tender/contract/subsidy→money · regulation→urgency ·
complaint/news→demand · gap-check→gap. A gap-check note containing the literal
marker "Demand point" also backs demand. When evidence justifies a different
dimension, set an explicit `dims: [..]` list — a scored dimension without a
resolvable source ref degrades the rendered scorecard. The freshness component
of urgency always refs the newest source dated <90 days before the extract.
