# Scoring v2: what the evidence on file can actually score

*Lens: evidence feasibility. Written 2026-09-17 against the owner's direction of the
same day. **Nothing here is built.** No record, score, rulebook or script was edited.*

**Corpus.** 29 live records (37 in `data/problems/cz/`, minus 8 `status: rejected`),
318 sources. The register date is **2026-09-04**, the newest `updated`. That is the
date `extractDate()` and `check-records.py` measure against, so every "recent" or
"within 18 months" below is measured from it. Signals: 17,121 lines in
`data/signals/**`. Lookups: `cz-contract-parties` (14,918 party rows, 7,649 contracts),
`cityvizor-invoices` (80,286 lines, 25 bodies, Jul 2025 to Aug 2026),
`ms21-public-projects` (26,048), `cz-eshop-addons` (609) and `cz-eshop-vendors` (181).

**How the numbers were made.** Counts of fields, source types, dates and derived
levels come from scripts and can be repeated. Anything that needs someone to read a
source (whether a contract buys *this* product, whether a tender is an award, whether
a deadline is enacted) is **judged**, and says so. Scripts: a PyYAML loader over the
frontmatter, plus `established()` imported from `scripts/check-records.py`.

---

## 0. The numbers in one screen

| | Today | Under the owner's direction |
|---|---|---|
| Source types on live records | gap-check 62 · arbitrage 51 · regulation 46 · tender 41 · contract 23 · complaint 22 · subsidy 16 · price 16 · news 16 · statistic 12 · round 5 · hiring 5 · ask 3 | same, since no new data is assumed |
| Sources with a `dims:` tag | 61 of 318 (34 of them `[]`); **none tagged `urgency`** | every scored point needs a pinned source |
| Dimensions a script checks against a ledger | 2 of 5 (`proof` rungs 0/1/2+, `gap`) | 3 of 6 at most without new fields (abroad, competition, difficulty) |
| Freshness point | held by 29 of 29 | removed: **every record loses 1 point, 13 drop to Why now 0** |
| Money: public budget nearby | total 26 points; 8 records at 2 | **Willingness to pay** (judged): total 22; **6 at rung 2, all six with public buyers**; 13 at 0 |
| Dated deadline, enacted, in the future | (not stored) | 6 of 16 deadline records; 3 more already in force; **6 rest on an unpassed law or an untransposed directive** |
| Execution difficulty | easy 11 · moderate 4 · hard 7 · very-hard 7, outside the total | summed as ease (0 to 3), **3 of today's top 10 drop out** |
| Register total (my simulation, §5.4) | 197 points, mean 6.79 | 178, mean 6.14; 9 of today's top 10 stay in the top 10 |

---

## 1. One table per dimension

"Enough evidence" means a source on the record that a reader could check the score
against. It does not mean the score is right.

### 1.1 The opportunity (and the demand signal) — today `demand` 0 to 2

| | |
|---|---|
| **Scored from today** | `complaint`, `ask`, `hiring`, `news`, and `statistic` when tagged `dims: [demand]`. `web/lib/scorecard.ts` `TYPE_TO_DIM` also counts a `gap-check` whose note contains "Demand point", and anything tagged `[demand]`, arbitrage included. |
| **Distribution** | 0: 11 · 1: 7 · 2: 11 |
| **Records with enough evidence** | **13 of 18** records with demand ≥1 cite a complaint, ask or hiring source. Two rest on `news` only: **p-0009** (at 1) and **p-0037** (at 2, on news dated 2006, 2020 and 2026). Three rest on something that is not a demand receipt: **p-0006** and **p-0010** (a `gap-check` "Demand point" only), and **p-0002** (an `arbitrage` source tagged demand, which means a foreign company is standing in as evidence of Czech pain). **p-0001** and **p-0008** are at 2 on a single complaint each. |
| **Checked by script** | **No.** `check-records.py` has no demand invariant. `SCORING.md`'s "Tier-3 sources can never lift proof or demand above 1" can't be enforced, because **no source carries a tier field** (the word appears once, in `CONVENTIONS.md`). |
| **Would change under the natural reading** | If "the opportunity" also counts buyers visibly acting (buying, re-tendering, failing to buy), four demand-0 records are underscored: **p-0026** (7 utilities buying smart metering), **p-0029** (~28 records-management tenders, several re-published), **p-0031** (towns re-tendering solar 3 to 4 times), and **p-0024** (15 energy-performance-contract awards). Each would gain +1, maybe +2. But that same evidence is the Willingness-to-pay receipt (§2), so counting it here too counts one fact twice. The three records resting on a non-demand source (p-0002, p-0006, p-0010) would drop to 0 under a strict reading: −1 each. |
| **New data or fields needed** | A `tier` (or `kind: petition \| association \| regulator-count \| press \| forum`) on demand sources, so the tier-3 rule becomes a check. A rule that `gap-check` and `arbitrage` never back demand. And a decision on whether "buyers acting" belongs to the opportunity or to Willingness to pay. It can't be both. |

### 1.2 Why now, without freshness — today `urgency` 0 to 3 = deadline 0 to 2 + freshness 0 to 1

| | |
|---|---|
| **Scored from today** | `regulation` sources (46), by type mapping only. **Zero** sources carry `dims: [urgency]`. The deadline part is not stored anywhere: `urgencySplit()` re-derives it at render time. |
| **Records with enough evidence** | Deadline ≥1 on **16** records. A named, enacted, future date that binds the buyer: **6** (§3). |
| **Records that lose a point** | **All 29** lose the freshness point, since every live record has a source under 90 days old. **13 go to 0:** p-0001, 0002, 0003, 0004, 0005, 0007, 0009, 0011, 0026, 0027, 0031, 0032, 0033. **6 change band:** p-0036 10→9 (PRIME→STRONG), p-0022, p-0032 and p-0033 8→7 (STRONG→FAIR), p-0025 and p-0034 5→4 (FAIR→FAINT). |
| **Would also change under "how real is the deadline"** | Capping a deadline that rests on an unpassed Czech law at 1: **p-0018** and **p-0023**, −1 each. Three records score 2 on a date already behind the register date (**p-0030** 1 Jul 2026, **p-0034** 2 Aug 2026, **p-0035** 1 Jan 2026). They keep 2 only if the rule says "in force now" counts. |
| **"Demand now" point** | Mechanically, 19 of 29 have ≥1 tender, contract, complaint, ask, hiring or signed-price source dated in the six months up to the register date. Judged (the buyer's own action, not an annual report or adjacent state spend): **16** (list in §3). |
| **New data or fields needed** | `deadline` stored (0 to 2), `deadline_on` (the date), `deadline_ref` (the S-number), and `deadline_status: enacted \| in-force \| draft \| directive-untransposed`. For the demand-now point, **an event date separate from `date`** (see red flag R3). |

### 1.3 Willingness to pay — replaces `money` 0 to 2

| | |
|---|---|
| **Scored from today** | `type: price` (16 receipts on 13 records; basis: list-price 9 · signed-contract 5 · manual-equivalent 2), `contract` (23 sources on 9 records), `tender` (41 on 13 records), `subsidy` (16 on 10). Only **1** price receipt is tagged `dims: [money]`. |
| **Records with enough evidence (judged)** | Rung 2, a named Czech buyer has paid for this or its manual equivalent: **6**. Rung 1, a price someone asks, or public money that pays this buyer to buy this: **10**. Rung 0: **13**. Per-record list in §2. |
| **Would change (judged, vs today's money)** | +1: p-0006, 0010, 0018, 0023, 0028, 0037 · −1: p-0004, 0011, 0024, 0032, 0035, 0036 · **−2: p-0017, p-0031** · 15 unchanged. Total 26 → 22. |
| **Checked by script** | Price-receipt *shape* only (five fields, url, vocabulary). Nothing checks that the payer is this record's buyer, that the thing bought is this product, or that a tender was awarded. |
| **New data or fields needed** | See §2.3. On `price`: `buys: this \| manual-equivalent \| adjacent` and `payer_kind` matching `entry.buyer`. An `invoice` basis. TED award status persisted on signals. Private-buyer price evidence, of which there is almost none. |

### 1.4 Validated abroad — `proof` 0 to 3, unchanged

| | |
|---|---|
| **Scored from today** | `comps[]`: 78 entries, all with `geo`, `since`, `traction`; 12 carry `markets`. Plus `arbitrage` and `round` sources. |
| **Distribution** | 0: 2 (p-0026, p-0030) · 1: 3 · 2: 13 · 3: 11 |
| **Records with enough evidence** | **29 of 29.** The established test runs in `check-records.py` on every comp. |
| **Would change** | Nothing under a rename. One gap: **the checker separates 0, 1 and 2+ but never checks rung 3 against rung 2** ("established in 2+ markets, one CEE-adjacent"). A rough parse (established comps, their `geo` plus `markets`, CEE list from `SCORING.md`) disagrees with 3 records: **p-0032** at 3 with one established comp, in GB; **p-0010** and **p-0031** at 2 where the parse reads 3. The parse is rough, since it reads `markets` generously, so treat these as a worklist. |
| **New data or fields needed** | None. Add a rung-3 invariant. |

### 1.5 Competition, low = good — `gap` 0 to 2, inverted for display

| | |
|---|---|
| **Scored from today** | `locals[]` (`competes` × `maturity`, `ico`, `since`) plus a `gap-check` with `queries[]` and a positive control. 62 gap-checks on 29 records. |
| **Distribution** | gap 0 (taken): 12 · 1 (early sellers only): 10 · 2 (checked, none): 7. As Competition: 2 on 12 · 1 on 10 · 0 on 7. |
| **Records with enough evidence** | **29 of 29**, checked by script. `entry.incumbents` is also checked against the same ledger. |
| **Would change** | No score changes. A display map, `competition = 2 − gap`. |
| **Caution** | **All 7 records at Competition 0 list adjacent local firms, 53 between them** (p-0033 lists 11, p-0027 lists 10, p-0007 lists 9). A row reading "Competition 0/2" above eleven named Czech companies is the "not checked above a list of competitors" contradiction again, in a new place (R5). The label has to say "nobody sells *this*". |
| **New data or fields needed** | None. |

### 1.6 Execution difficulty, low = good — `entry.level`, today outside the total

| | |
|---|---|
| **Scored from today** | `entry.buyer`, `permission`, `integration`, `money`. The level is derived and checked by script. `incumbents` carries no weight. |
| **Distribution** | easy 11 · moderate 4 · hard 7 · very-hard 7. Gates: buyer small-firms 15 / large-firms 4 / public 10 · permission none 25 / registration 2 / licence 2 · integration software 18 / national-system 10 / certified 1 · money bootstrap 20 / outside-money 9. |
| **Records with enough evidence** | **29 of 29.** The level is a derivation, not a claim about evidence. The gates themselves are judged, and only `why` names them. |
| **Would change** | As a display, nothing. Summed into a total, ranks move (§4). |
| **New data or fields needed** | None to display it. To sum it, a `SCORING.md` amendment ("never enters the 12 points" is written there) and a decision on the scale (4 levels → 0 to 3). |

---

## 2. Willingness to pay

### 2.1 What is on file, record by record (judged)

The ladder used to judge, as a candidate and not a proposal: **2** = a named Czech
buyer of this record's buyer type has *paid* (a signed contract, an awarded tender, an
invoice) for this product or its manual equivalent · **1** = a price someone asks
(list price, a published fee), or public money that pays *this buyer* to buy *this* ·
**0** = nothing, or public money that only sits near the problem.

| Evidence on file | Records | Count |
|---|---|---|
| **Signed contract or awarded tender for this product or its manual equivalent** | p-0008 (Lexnova NIS2 package, 91k CZK, repeat order; Český Brod 9M; TED awards) · p-0022 (hospital-system awards to STAPRO and OR-CZ; KNTB 2.8M price rises) · p-0026 (VaK Židlochovicko 8.4M; Kroměříž 21.4M) · p-0029 (~28 records-management procurements, awards on the e-spis and GINIS stacks) · p-0001 (care home and hospital sharing contracts, with the admin fee bundled into the electricity) · p-0037 (Kolín paid 1.45M for a surface register, **in 2019**) | **6** |
| **Paid consultant** (the manual equivalent, bought) | p-0008 (Boskovice paid 121k CZK for a grant application), plus p-0037 above | 2, both already in the row above |
| **Price asked, no transaction** (list price or published fee) | p-0002 (Wue 650/seat) · p-0003 (Průvodka 12,900/project; permit engineering 16,000/project) · p-0006 (AML Proof 25/case) · p-0018 (TREXIMA 79k/yr) · p-0023 (Účtárna.ai 5k/mo) · p-0025 (subsidy desk 10k fee) · p-0028 (two add-ons, 19 and 200 CZK/mo) · p-0033 (nurse wage bill as manual equivalent) | **8** |
| **Public money that pays this buyer for this** (open grant) | p-0010 (OP TAK 50% for SME software; its only price is a US list price) · p-0036 (IROP call 79 to 2 Dec 2026; the vendor's AI coding pilot was **free**) | **2** |
| **Only public money near the problem** (adjacent or state-side) | p-0004 (ministry IT framework) · p-0011 (state data-layer contract; autism-services call) · p-0017 (the state building its own wallet; the buyer is regulated firms) · p-0024 (retrofit works, not analytics) · p-0031 (solar panels, not the pooled tender) · p-0032 (care-home construction concessions) · p-0035 (hospitals buying medicines, not procurement tooling) | **7** |
| **Nothing** | p-0005 · p-0007 · p-0009 · p-0027 · p-0030 · p-0034 | **6** |

**So: 6 records show people paying now, 10 show a price or a grant for this buyer, and
13 show only public money nearby, or nothing.**

**Every one of the 6 rung-2 records has a public buyer.** Crossed with `entry.buyer`:
public 6 at rung 2, 1 at rung 1, 3 at rung 0 · small-firms **0 at rung 2**, 7 at
rung 1, 8 at rung 0 · large-firms 0 / 2 / 2. That is not because Czech small firms
don't pay. Payment receipts are mandatory *only* for public bodies (registr smluv,
TED), and the register has no feed for private spend (R1).

### 2.2 What Money → Willingness to pay does to totals (money swapped, nothing else changed)

| Record | Money → WTP | Total |
|---|---|---|
| p-0017 EUDI wallet | 2 → 0 | 6 → 4 |
| p-0031 municipal PV | 2 → 0 | 7 → 5 |
| p-0036 clinical documentation | 2 → 1 | **10 → 9** (leaves PRIME) |
| p-0035 hospital drugs | 1 → 0 | 9 → 8 |
| p-0032 care placement | 1 → 0 | 8 → 7 (leaves STRONG) |
| p-0004 · p-0011 · p-0024 | 1 → 0 | −1 each |
| p-0028 e-shop compliance | 0 → 1 | **9 → 10** (to PRIME) |
| p-0037 stormwater | 1 → 2 | 9 → 10 (to PRIME, on one 2019 contract) |
| p-0006 · p-0010 · p-0018 · p-0023 | 0 → 1 | +1 each |
| the other 15 | unchanged | |

Money points go from 26 to 22. The two records that fall furthest (p-0017, p-0031)
are the ones `docs/who-pays-audit-2026-09-03.md` already flagged as money spent by a
party that isn't their buyer. That is the correction working.

### 2.3 Which sources could supply "people pay now" at scale

| Source | State today | What it can prove | Limit |
|---|---|---|---|
| **Registr smluv** (`smlouvy` bulk dump) | Feed **parked** (per-item, needs `smlouvy_reduce.py`). The lookup `cz-contract-parties.jsonl` holds 7,649 contracts with payer and recipient IČO. | Payment by a named public buyer to a named vendor, **below every tender threshold**. The only source that can show p-0008's 91k CZK package orders at scale. | Public payers only. Contract subject is free text, so "is it *this* product" stays a reading. The lookup covers about a week of dumps (some party dates are junk: `0001-01-01`, `2206-07-20`). |
| **Hlídač státu** (`hlidac`) | LIVE, 2,210 contract signals, payer and recipient in `notes` | The same register through an API, used by query (large contracts, topic searches). | The same public-only limit. Per-query, so coverage is whatever was searched. |
| **TED** (`ted`) | LIVE, 8,169 signals | Awards over the EU threshold. | **Award status isn't persisted.** The fetcher requests `form-type`, `winner-name` and `winner-identifier`, but no committed TED signal carries a winner (0 of 8,169; 4,959 carry the buyer only). "Awarded tender" can't be read off the ledger today, so every award claim on a record was judged by reading the notice. |
| **NEN** `/vysledek` pages | Feed `planned` (PENDING) | Actual price plus supplier for below-threshold procedures. | Not built. |
| **CityVizor invoices** (lookup) | 80,286 purchase lines, 25 bodies, Jul 2025 to Aug 2026, 99.4% counterparty IČO | *Executed* payment (an invoice), including a monthly software fee (Axians, 48,352 CZK/month for hosted records management). The only invoice-grade source. | 25 of about 6,250 municipalities; Prague unreachable. |
| **MS2021+** (lookup) | 26,048 approved public projects | A signed grant agreement, with the beneficiary's own problem statement. | **This is public money, not willingness to pay.** A grant approved *for* a buyer is rung 1 at most, unless the project line shows the thing bought. The catalog's `basis: signed-contract` for these rows would score rung 2 by construction (R2). |
| **Shoptet / Upgates add-on lookups** | 609 add-ons with `price_note` and `rating_count` | The one **private-buyer** proxy on file: a paid add-on with 145 ratings is many shops paying monthly. Relevant to p-0028. | A rating count is not a paying-install count. E-shops only. |
| **ARES** | Enrichment | Confirms a vendor exists and its age. | Says nothing about payment. |
| **Price lists by hand** | 9 list-price receipts | What a seller asks. | Not proof that anyone pays (rung 1). |

**Private willingness to pay has no ingest at all.** 15 of 29 records sell to small
firms, and the only receipts that can reach them are hand-read price lists, and
add-on ratings for e-shops.

---

## 3. Why now

### 3.1 Deadlines on the 16 records with deadline ≥1 (judged from the regulation sources and the Why now prose)

| Kind | Records | Count |
|---|---|---|
| **Enacted, dated, in the future, binds the buyer, <18 months** | p-0006 (AMLR, 10 Jul 2027) · p-0008 (Act 264/2025, one year from each entity's registration, so the date varies per entity) · p-0029 (attested records system by 1 Jan 2027) · p-0017 (relying-party acceptance, stated only as "within 36 months of the implementing acts", about late 2027) | **4** |
| **Enacted and dated, but >18 months** | p-0022 (EHDS 2029) · p-0036 (EHDS 2031) | **2** |
| **Enacted, but binds someone other than the buyer** | p-0010 (eFTI obliges *authorities* to accept e-documents on 9 Jul 2027; hauliers are not obliged) | **1** |
| **Already in force, date behind the register date** | p-0030 (1 Jul 2026) · p-0034 (AI Act Art. 50, 2 Aug 2026) · p-0035 (1 Jan 2026) | **3** |
| **EU directive date, Czech law not passed** | p-0028 (EmpCo applies 27 Sep 2026; tisk 53 awaits third reading; **no draft-law badge**) · p-0024 (EPBD, Czech dates "unset"; has the badge) · p-0025 (EPBD 2030/2033; **no badge**, same source as p-0024) | **3** |
| **Unpassed Czech law** (`draft_law` set) | p-0018 (pay transparency) · p-0023 (accounting act, 2028) · p-0037 (water-utilities draft, Jul 2027, which is <18 months but scored deadline 1) | **3** |

**Enacted and dated in the future: 6 (4 under 18 months). Resting on draft law or an
untransposed directive: 6. Already in force: 3. Binding someone else: 1.**

Two inconsistencies turned up. **p-0024 and p-0025 cite the same EPBD source, and only
one carries the draft-law badge.** **p-0028's deadline 2 depends on a Czech bill**
that hasn't passed, while its pain (today's ČOI fines) doesn't. That fits the badge's
rules, but not a "how real is the deadline" reading.

**An open question the owner's wording raises:** is a **grant closing date** a
deadline? p-0036's approved headline *is* one ("closes in December"), and so is
p-0008's IROP 120 (17 Dec 2026). If it counts, p-0002 (NPO call to 30 Nov 2026),
p-0001 (KOMUNERG to 31 Dec 2027), p-0010, p-0028 (OP TAK to Sep 2027) and p-0023
(vouchers to Apr 2027) gain a deadline too. Today `SCORING.md` counts regulatory
triggers only.

### 3.2 "Demand now": buyers acting in the six months to 2026-09-04

| | Records |
|---|---|
| **Yes (judged)**, the buyer's own buying, re-tendering, asking, complaining or hiring | p-0001 (sharing contracts) · p-0003 (Q2 ombudsman building complaints) · p-0008 (awards, package orders) · p-0011 (nurse hiring) · p-0022 (hospital awards) · p-0023 (back-office hiring) · p-0024 (EPC awards) · p-0026 (utility contracts) · p-0027 (8,200 arbiter filings by May 2026) · p-0028 (ČOI Q2 fines) · p-0029 (records tenders) · p-0031 (solar re-tenders) · p-0032 (illegal care homes, Jun 2026) · p-0033 (nurse hiring) · p-0035 (hospital medicine notices) · p-0036 (three hospital asks, Sep 2026) — **16** |
| **Mechanical hit, judged no** | p-0004 (a Commission country report and ministry IT) · p-0007 (trades hiring, adjacent) · p-0017 (the state's own wallet tender) — 3 |
| **None on file** | p-0002 · 0005 · 0006 · 0009 · 0010 · 0018 · 0025 · 0030 · 0034 · 0037 — **10** |

With deadline realness capped for draft law, plus this point, Why now totals go from
56 to 41. The changes are in §0 and §5.4.

---

## 4. Execution difficulty as a score

**Distribution:** easy 11 · moderate 4 · hard 7 · very-hard 7. Mapping used: ease =
easy 3 · moderate 2 · hard 1 · very-hard 0, added to today's score (0 to 15). Tie-break
as today (deadline, then money).

| # | Today (0 to 12) | level | With ease (0 to 15) | level | was |
|---|---|---|---|---|---|
| 1 | p-0008 · 11 | hard | p-0008 · 12 | hard | 11 |
| 2 | p-0036 · 10 | very-hard | **p-0028 · 12** | easy | 9 |
| 3 | p-0035 · 9 | very-hard | **p-0032 · 11** | easy | 8 |
| 4 | p-0028 · 9 | easy | p-0036 · 10 | very-hard | 10 |
| 5 | p-0037 · 9 | hard | p-0037 · 10 | hard | 9 |
| 6 | p-0001 · 9 | hard | p-0001 · 10 | hard | 9 |
| 7 | p-0022 · 8 | very-hard | **p-0004 · 10** | easy | 7 |
| 8 | p-0032 · 8 | easy | **p-0009 · 10** | easy | 7 |
| 9 | p-0033 · 8 | hard | p-0035 · 9 | very-hard | 9 |
| 10 | p-0029 · 7 | very-hard | **p-0006 · 9** | moderate | 7 |

**Out:** p-0022, p-0029, p-0033. **In:** p-0004, p-0006, p-0009. Spearman ρ between the
two full rankings is **0.73**. So yes, scoring difficulty moves the ranking a lot.

Why it moves so much: **ease and today's score are negatively correlated (r = −0.27).**
Hard records carry *more* evidence, because public buyers (a weight-2 gate) leave
public receipts. Summing ease therefore promotes records with thin evidence: p-0004
(no price, no deadline, demand 1) and p-0009 (money 0, no deadline) reach the top 10
on ease alone. Keeping difficulty as a separate row avoids this. The owner's "low =
good" can be shown as a word without adding it to the total.

---

## 5. Migration cost and order

### 5.1 What each dimension costs

| Dimension | Kind of change | Records touched | Blocks on |
|---|---|---|---|
| Validated abroad | **Display rename only** | 0 | Nothing. Add the rung-3 invariant, which opens a 3-record worklist. |
| Competition (low = good) | **Display map** `2 − gap` | 0 | A label that says "sells *this*" (R5). Keep `gap` stored, so the total can't flip sign. |
| Execution difficulty (low = good) | **Display only** if kept outside the total. If summed: a `SCORING.md` amendment, and bands move | 0 | The owner's call on summing (§4) |
| The opportunity / demand | **Rescoring pass** (worklist of about 7: p-0002, 0006, 0010 down; p-0024, 0026, 0029, 0031 up if buying counts), plus a new `tier`/`kind` field on demand sources | ~7 changed, all 29 re-read | Where "buyers acting" lives (here or in WTP) |
| Why now | **Mechanical** −1 freshness on 29 · **fill** `deadline_on`/`deadline_ref`/`deadline_status` on 16 · **rescoring** of the draft cap (2) and in-force dates (3) · **new field** for demand-now (event date) and a judged pass on 29 | 29 | An event-date field; the grant-deadline ruling |
| Willingness to pay | **New ladder, all 29 rescored**, new `price` fields (`buys`, `payer_kind`, basis `invoice`), and for more than the 6 public-buyer records, **new ingest** | 29 | TED award persistence, `smlouvy_reduce.py`, NEN `/vysledek`, some private-spend source |

### 5.2 Order

1. **Display-only, now:** Validated abroad, Competition (with the "sells this" label),
   and Execution difficulty as a row outside the total.
2. **Mechanical Why now:** store `deadline = urgency − 1` and drop freshness. Label it
   only after `deadline_on`/`deadline_ref` are filled on the 16 records and the
   invariants below pass.
3. **Demand rescoring pass** (small, about 7 records), with the `kind` field.
4. **Willingness to pay** last. Score it on what is on file (6 / 10 / 13), and say on
   the page that rung 2 is reachable only through public registers today.
5. **Ingest** in parallel with 4: persist TED `form-type`/winner, un-park `smlouvy`
   with a reducer, build NEN `/vysledek`, and look for a private-spend source.

### 5.3 Invariants `check-records.py` would need (each in the same change as its field, per CLAUDE.md rule 2)

**Why now**
1. `0 ≤ why_now.deadline ≤ 2`; the stored sum equals `deadline + demand_now`.
2. `deadline ≥ 1` ⇒ `deadline_on` (ISO date) and `deadline_ref` resolving to a source
   of `type: regulation` (or `subsidy`, if grant deadlines are ruled in).
3. `deadline = 2` ⇔ `deadline_status ∈ {enacted, in-force}` AND (`deadline_on` ≤
   register date + 18 months, or `in-force`). `deadline = 1` ⇔ enacted and >18 months,
   or `draft`/`directive-untransposed`.
4. `draft_law` present ⇒ `deadline ≤ 1`, and `deadline_status = draft` ⇒ `draft_law`
   present. That closes the p-0024/p-0025 split.
5. `demand_now = 1` ⇒ ≥1 cited source of type tender/contract/complaint/ask/hiring, or
   a signed price, with an **event date** within N days before the register date and
   not after it.

**Willingness to pay**

6. `wtp = 2` ⇒ ≥1 `price` with basis ∈ {signed-contract, tender-line, invoice},
   `buys ∈ {this, manual-equivalent}`, dated within M months (24 would flag p-0037's
   2019 contract).
7. `wtp = 1` ⇒ a `price` of any basis, or a `subsidy` tagged `pays: buyer`.
8. `subsidy`, `tender` and `contract` alone never reach `wtp = 2`. A price citing an
   MS2021+ approved project caps at 1.
9. `price.payer_kind` must equal `entry.buyer`.
10. Retired key: `scores.money` present ⇒ ERROR (the `LOCAL_RETIRED_KEYS` pattern).

**The opportunity / demand**

11. `demand ≥ 1` ⇒ ≥1 cited complaint/ask/hiring source, or a statistic tagged demand.
    `gap-check` and `arbitrage` never count.
12. `demand = 2` ⇒ ≥2 distinct demand sources, or one of `kind ∈ {petition,
    association, regulator-count}`.
13. Every source with `kind: press \| forum` alone ⇒ `demand ≤ 1` (the tier-3 rule,
    finally checked).

**Validated abroad, Competition, Difficulty**

14. `proof = 3` ⇒ established comps covering ≥2 markets, ≥1 CEE-adjacent.
15. The Competition display must equal `2 − gap`, asserted in the web build next to
    `assertScoringVocabulary()`.
16. If difficulty is summed: `score == proof + gap + demand + wtp + why_now + ease(level)`.
    If not summed: assert that the level never reaches the total.

**Register order:** `registerRows()` tie-breaks on `urgencySplit(...).deadline` and
`money`. It must move to the stored deadline and to `wtp`.

### 5.4 The simulation behind §0 (all judged inputs, for sizing only)

Assumed: proof, gap and demand as stored · WTP as §2.1 · Why now = deadline (draft cap
on p-0018, p-0023) + demand-now as §3.2 · no ease. **Total 197 → 178.** 16 records
fall (p-0017 −3; p-0004 and p-0031 −2; 13 records −1), 12 are unchanged, and 1 rises
(p-0028 +1). Bands: PRIME 2→2 (p-0036 out, p-0028 in), STRONG 7→6, FAIR 16→14, FAINT
4→7. Top 10 overlap 9 of 10 (p-0032 out, p-0006 in); ρ = 0.94. **Without ease, the
proposal barely moves the ranking. The difficulty sum is what reorders it.**

---

## 6. Red flags

**R1. Willingness to pay can only be proven for public buyers.** All 6 rung-2 records
are public-buyer records, and 0 of 15 small-firm records reach rung 2. The public
registers are the only payment receipts the pipeline can read. A WTP score would reward
records that are *hard to enter* (a public buyer is a weight-2 gate) and penalise the
owner's own canonical easy case, the trucking app. That is a data-access bias, and it
would read as a finding about the market. The page needs to say "paid by a public
buyer" vs "priced", or the ladder needs a private rung it can actually reach.

**R2. "Public money might raise willingness to pay" brings the old field back.**
Letting an open grant lift WTP puts `money`'s old meaning (a public budget near the
problem) back inside the new field, which breaks rule 1 again. Worse, the MS2021+
citation rule already writes grants as `basis: signed-contract`, so a grant would pass
a naive rung-2 check. The grant must cap at rung 1 and be labelled as a grant.

**R3. `date` has two meanings.** 27 of 318 live sources are dated *after* the register
date: regulation 16 (effective dates), subsidy 9 (call close dates), and also a
*complaint* (p-0008's SME UNION, dated 2026-12-31) and a *tender* (p-0037's loan call,
2027-03-31). Annual reports are dated at publication, not at the events they count.
"Demand now" and "not recently checked" both need an event date the register doesn't
store. Scoring demand-now off `date` would give points for future deadlines and for
report publication.

**R4. Why now loses its only point on 13 records.** Nothing is wrong with that, since
freshness separated nothing (29 of 29 held it). But it shows how much the current "Why
now" row rests on a check every record passes. Of the 16 real deadlines, **6 rest on
law that doesn't bind anyone yet**, 3 are already behind us, and 1 binds the
authorities rather than the buyer. None of this is pinned to a source (0 `dims:
[urgency]` tags). "How real is the deadline" is currently unscoreable, not just
unscored.

**R5. "Competition 0" above a list of companies.** All 7 records at Competition 0 carry
adjacent local firms, 53 in all. The inverted display turns "checked: nobody sells
this" into a number that reads as "no competition", printed above up to eleven Czech
firms. That is the `gap: 0` "not checked above a list of competitors" defect again,
with the sign flipped.

**R6. Summing difficulty promotes thin records.** §4: p-0004 and p-0009 reach the top 10
on ease alone. Adding a derived feasibility level to an evidence total mixes a fact
about the market with a count of receipts, which is the reason `SCORING.md` kept
`entry` out.

**R7. "Buyers acting" gets counted twice.** The same tender or contract is the natural
receipt for *the opportunity* (demand signal), for *Why now* (demand now) and for
*Willingness to pay* (people pay). p-0008, p-0022, p-0026 and p-0029 would score all
three off the same notices. Pick one home for "a buyer spent money" (WTP), and let the
other two cite complaints, asks and deadlines only.

**R8. Checks that exist in prose only.** Several dimensions have no invariant today:
demand (none), the tier-3 rule (no field), proof rung 3 (unchecked, 3-record
disagreement), `dims` pinning (61 of 318 tagged, 34 of those empty), and TED award
status (fetched, never persisted). A v2 that adds judgment words ("reasonable",
"real") on these rows without the §5.3 invariants would be *less* checkable than the
current numbers, whose rungs are at least written down.

**R9. Judgment in this document.** The WTP ladder (§2.1), the demand-now set (§3.2)
and the deadline classes (§3.1) are one reader's judgment on 29 records. They size the
work. They are not a rescoring and must not be copied into records as one.
