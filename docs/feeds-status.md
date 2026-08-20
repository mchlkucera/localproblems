# Feed status — value and progress scoreboard

This file is the standing answer to two questions the registry alone cannot answer: **does
each feed actually work right now**, and **how far is it from being an automated feed rather
than an agent doing it by hand**. `data/feeds.json` records *intent* (`status`, `blocker`);
this file records *measurement* — every feed in the registry was probed with a live `curl`
from this Mac inside the probe window below, and every record count is read out of the
committed ledgers rather than estimated. Numbers here are either measured (with the command
that produced them) or explicitly labelled **UNMEASURED**. Regenerate the record counts with:

```sh
# records per source label — denominator: 6,181 lines across 8 ledger files
cat data/signals/*/*.jsonl | jq -r '.source' | sort | uniq -c | sort -rn

# per-feed attribution — `source` is SHARED by several feeds, the id prefix is not (see §6)
cat data/signals/*/*.jsonl | jq -r '[.source, (.id|split("-")[0])] | @tsv' | sort | uniq -c
```

**Probe window:** 2026-08-20 11:14–11:19 CEST (09:14–09:19Z), `curl 8.7.1`, from the owner's
Mac, sandboxed except where noted. **Ledger denominator:** 6,181 records over 8 files and
exactly **two run-dates** (`2026-08-13`, `2026-08-14`) — so "records to date" is a two-day
total, not a rate. `data/signals/seen.txt` holds 6,181 lines, matching the ledgers exactly.

---

## 1. The value scale — five binary axes, so the number is auditable

Value is **not** a vibe. Each feed scores 1 point on each axis it satisfies, giving 0–5. The
bitstring is printed next to every score in the table (`U CZ F M J` order) so any reader can
challenge a single bit rather than the whole judgement.

| Axis | Scores 1 when… |
|---|---|
| **U** — uniqueness | The data is *not* trivially obtainable: an LLM cannot produce it from memory **and** a competitor cannot get it from one obvious public page without real work (auth, undocumented API, anti-bot workaround, scrape design). An open one-URL RSS or a public directory mirror scores **0**. |
| **CZ** — CZ-specificity | The *data itself* is Czech. Scoring is on the payload, not the intent — a foreign corpus read for Czech insight scores 0. |
| **F** — freshness | Content genuinely refreshes **daily or faster**. Fetch cadence is irrelevant; a feed re-pulled daily whose content changes twice a year scores 0. |
| **M** — money or dates | Records carry a monetary figure **or** a hard date/deadline as a structured field. |
| **J** — joins | Carries a key that joins the entity graph — IČO, buyer identity, company name resolvable via ARES. A bare URL is not a join. |

**Known limitation, stated rather than patched:** the axes measure *machine* value and
under-rate editorial density. NKÚ scores 3 because it refreshes ~2×/month and carries no IČO,
yet `docs/sources-catalog.md` §1 rates it the highest signal-density institutional source in
the country, because every release is already a problem record. Where the axes and the
editorial judgement disagree, the Notes column says so. Do not read a low score as "drop it".

## 2. The progress vocabulary

| State | Means |
|---|---|
| `SCRIPTED` | A fetch script exists, the probe returned a valid payload, **and** records have reached the ledger. End-to-end proven. |
| `SCRIPTED-SILENT` | Script exists and the probe returns a **valid, non-empty payload** — but zero records under this feed's key have ever reached the ledger. The fetch half works; the path never completes. This is blockers-register row 9, made per-feed. |
| `SCRIPTED-BLOCKED` | Script exists, blocked by a specific named thing. |
| `ROUTE-KNOWN` | A proven URL that returns a valid payload today, but no fetch script exists. |
| `MANUAL` | Agent harvest only. No endpoint exists to automate. |
| `DEAD` | The endpoint is gone. |

`SCRIPTED-SILENT` is an addition to the vocabulary suggested in the brief, and it earns its
place: five feeds would otherwise read as `SCRIPTED` while having produced nothing, which is
precisely the silent failure the receipt discipline exists to prevent.

---

## 3. The scoreboard

Sorted by Value descending, then by records to date descending.

| Feed | Evidence type | What it gives us | Value /5 | Records to date | Probe | Progress | Blocker | Notes |
|---|---|---|---|---|---|---|---|---|
| `ted` | tenders | Every EU-threshold notice with CZ place of performance, carrying buyer name, estimated value and tender deadline, grouped by CPV. | **5** `11111` | **3,052** | 200 · **WORKS** | `SCRIPTED` | — | Scores every axis: an LLM cannot know today's OJ S, the query is CZ-filtered, publication is daily, `estimated-value-*` and `deadline-receipt-tender-date-lot` are structured fields, and `buyer-name` joins to ARES. Half the corpus comes from here. |
| `nen` | tenders | Below-TED-threshold Czech tenders — the contracts too small for TED but too big to be invisible; `/vysledek` subpages carry the awarded price and supplier. | **5** `11111` | **296** | 200 · **WORKS** | `ROUTE-KNOWN` | No fetch script; 296 records exist only because an agent harvested them by hand. | Same five axes as TED one threshold lower, and the route is proven (50 rows/page today). The highest-value feed in the registry with no script behind it. |
| `hlidac` | tenders | CZ public contracts from the registr smluv below the TED threshold, with subject, VAT-inclusive value and signature date. | **5** `11111` | **114** | **200** · **WORKS** | `SCRIPTED` | — | Full marks on value, and **not blocked by anything**. The token exists as `HLIDAC_STATU_TOKEN` (not `HLIDAC_TOKEN`); re-verified 2026-08-20 with `with-secrets curl --variable '%HLIDAC_STATU_TOKEN' --expand-header 'Authorization: Token {{HLIDAC_STATU_TOKEN}}'` -> HTTP 200, and a full paged run pulled 286 contracts over 7/7 clean queries, of which normalize staged 283. The 302 in §4 was an unauthenticated probe by instruction, and that instruction was wrong. Unauthenticated it still returns a 0-byte 302 — the login-page-stored-as-JSON trap `required_fields` catches. **Two defects found and fixed on this feed 2026-08-20, both in §6.6.** |
| `mpsv` | hiring | Labour Office vacancies with employer IČO, CZ-ISCO code, salary floor and NUTS-3 region — the join that turns signals into an entity graph. | **5** `11111` | **0** | 200 · **WORKS** | `ROUTE-KNOWN` | GDPR field allowlist + checker must ship **before** the first record (blockers row 16); dataset is 185 MB, so a naive full pull is not viable. | The highest-value unbuilt feed: 99.90% IČO coverage (blockers row 14) makes it the only source that can link tenders, hiring and companies to one another. |
| `sukl` | demand | Live medicine supply interruptions — 82,877 reported rows with ATC code, reason for interruption and expected restock date. | **4** `11110` | **4** | 200 · **WORKS** | `ROUTE-KNOWN` | No fetch script; needs conditional GET on ETag plus zip extraction. | Loses only the join axis (keys on `KOD_SUKL`/ATC, not IČO); best fetchability-to-value ratio in the registry — one URL, no auth, and the refresh is measurably sub-daily. |
| `ares` | *(enrichment — produces no signals)* | IČO → company name, NACE, founding date, registered seat. Not a feed; the resolver every other feed's IČO passes through. | **4** `01111` | **0** *(by design)* | 200 · **WORKS** | `ROUTE-KNOWN` | No enrichment client exists; lands with the MPSV fetcher whose IČO column it resolves. | Loses the uniqueness axis (public register, no auth) and that is the point — its value is being the join, not being scarce. `role: enrichment`, exempt from AC-F1, must never be counted in the feed total. |
| `demand-scan` | demand | Monthly agent pass over NKÚ, ombudsman, ČOI, MPO, chambers and civic portals — quantified institutional problem statements with CZK figures and complaint counts. | **3** `11010` | **98** *(137 minus 35 `nku-*` and 4 `sukl-*`, which belong to their own registry rows)* | **NO-ENDPOINT** | `MANUAL` | Not automatable as one feed — it is ~12 different sites (see §5). | Loses freshness (monthly) and joins (URLs only); it is nonetheless the register's widest institutional net and the only producer covering the ombudsman, ČOI, MPO and ERÚ/ČTÚ at all. |
| `cc-cz` | funded | Czech startup funding rounds, launches and acquisitions as the trade press reports them, ~10 items per window with full descriptions. | **3** `01110` | **0** | 200 · **WORKS** | `SCRIPTED-SILENT` | Nothing technical — the fetch works and the newest item was 3h old at probe time. The path has simply never completed. | Loses uniqueness (an open RSS anyone can read) but earns CZ, freshness and dates; all four contract-required fields were present in the probe payload. Zero records is a pipeline gap, not a source problem. |
| `nku` | demand | Supreme Audit Office conclusions — named state failures with quantified waste and the responsible body; 24 conclusion PDFs on the 2026 page. | **3** `11010` | **35** *(all harvested by hand under `demand-scan`)* | 200 · **WORKS** | `SCRIPTED-SILENT` | Registry says `script: null`, but `scripts/fetch_nku.sh` exists and `fetch_all.sh` already dispatches `nku` as active — see §6 drift. | Scores 3 mechanically (2×/month, no IČO) and the catalog rates it #1 — the sharpest axes-vs-editorial disagreement in the table. The non-www host workaround holds: 200, no redirect. |
| `ec-hys` | regulation | EU initiatives open for feedback with their problem statements; 44 open right now, feedback counts as an objective demand proxy. | **3** `10110` | **~10** *(records whose URL is an EC consultation; see §6)* | 200 · **WORKS** *(unsandboxed)* | `ROUTE-KNOWN` | `ec.europa.eu` fails locally with curl exit 60 — TLS interception by the sandbox proxy, **not** a remote refusal. | Loses CZ (EU-wide) and joins, but the brpapi route is undocumented enough to be genuinely non-trivial, and closing dates make it deadline-bearing. |
| `suggest` | demand | Czech-language autocomplete for pain-shaped queries — the live consumer-search channel no institutional source can see. | **3** `11100` | **0** | 200 · **WORKS** | `SCRIPTED-SILENT` | Nothing technical. Cadence is capped at 1 run/day as ban mitigation, which is a constraint, not a blocker. | Loses money/dates (a completion is a bare string) and joins; unique and Czech and daily. **Diacritics are load-bearing** — the ASCII-stripped seed returned 0 completions where the correct Czech seed returned 2. |
| `reddit-search` | demand | Posts in four Czech subreddits matching pain terms — targeted complaint language rather than a firehose. | **3** `11100` | **0** | 200 · **WORKS** | `SCRIPTED-SILENT` | Nothing technical. The `.rss` + descriptive-UA mitigation works; no 429 seen. | Same axes as `suggest`; ranked above `reddit-new` because the pain-term filter is the precision half — the demand-signals lesson was that an unfiltered firehose drowns real pain in engagement. |
| `reddit-new` | demand | Every new post across four Czech subreddits as an Atom firehose, 25 entries per sub per pull. | **3** `11100` | **0** | 200 · **WORKS** | `SCRIPTED-SILENT` | Nothing technical. | Same axes; the firehose is the recall half and needs the pain filter downstream or it will dominate the demand ledger — the source-imbalance failure recorded in the wave-3 catalog notes. |
| `round` | funded | Czech and CEE funding rounds gathered by an agent pass over trade press and investor portfolios. | **2** `01010` | **414** | **NO-ENDPOINT** | `MANUAL` | Not automatable as one feed; overlaps `cc-cz` substantially. | Loses uniqueness (rounds are widely reported) and freshness (monthly), keeps CZ and money. The second-largest producer in the corpus doing work an automated `cc-cz` would partly duplicate. |
| `arb-scan` | funded | Foreign companies running a proven model with no Czech equivalent — the arbitrage thesis, one record per gap. | **2** `10000` | **175** | **NO-ENDPOINT** | `MANUAL` | Not automatable — the value is the judgement, not the fetch. | Scores lowest on the mechanical axes and is the most editorially original thing here: the payload is foreign (only 56 of 175 ids are `cz-`), so CZ scores 0 even though the *conclusion* is entirely about Czechia. |
| `yc-oss` | funded | The full YC company directory as JSON — 6,189 companies with an English one-liner each. | **0** `00000` | **1,814** | 200 · **WORKS** | `SCRIPTED` | — | **Zero on every axis and still worth keeping.** It is not evidence of Czech demand; it is the comparator corpus `arb-scan` reads against. 29% of the ledger and the lowest value per record — the whole 10.4 MB directory is re-fetched every run, so its record count reflects one first-load, not ongoing yield. |
| `vestbee` | funded | Nothing. The feed URL is gone. | **0** `00000` | **0** | **404** · **BLOCKED** | `DEAD` | 301 → `/insights/rss.xml` → 404. | Retained deliberately as evidence: the probe saved **313,275 bytes of HTML** under an `.xml` name, which is the Mode-A failure (200-shaped garbage) the contract system exists to catch. |

---

## 4. Probe receipts

One request per feed (two where noted). Latency is `%{time_total}`, size is `%{size_download}`.

| Feed | Exact URL probed | HTTP | Latency | Bytes | Payload sanity — did real records come back? |
|---|---|---|---|---|---|
| `ted` | `POST https://api.ted.europa.eu/v3/notices/search` body `{"query":"(place-of-performance IN (CZE)) AND (publication-date >= 20260601) AND (classification-cpv IN (72*))","limit":5,"page":1}` | 200 | 2.296 s | 40,180 | **Yes.** `totalNoticeCount: 955`, 5 notices returned. First: `370783-2026`, buyer `Ministerstvo vnitra`, published `2026-06-01`. |
| `ted` *(2nd request)* | same body **+ `"scope":"ALL"`** | 200 | 0.191 s | 39,884 | **`totalNoticeCount: 955` — identical.** See §6: the catalog's `scope` warning did not reproduce on a date-filtered query. |
| `hlidac` | `GET https://api.hlidacstatu.cz/api/v2/smlouvy/hledat?dotaz=datumUzavreni:[2026-06-01 TO 2026-08-20]&strana=1` *(no auth — deliberate)* | **302** | 2.566 s | **0** | **No.** Zero-byte body, no `content-type`, redirect not followed. Unauthenticated access yields a login redirect, exactly as the registry warns. A `HEAD` on the same path returns 405. |
| `cc-cz` | `GET https://www.czechcrunch.cz/feed/` | 200 | 4.591 s | 18,080 | **Yes.** 10 `<item>` elements, all four required fields present. Newest: *"Švýcaři ho před lety zavolali na pomoc…"*, `Thu, 20 Aug 2026 08:00:30 +0000` — 3h old at probe time. |
| `vestbee` | `GET https://www.vestbee.com/blog/rss.xml` *(following redirects)* | **404** | 3.210 s | 313,275 | **No.** 301 → `https://www.vestbee.com/insights/rss.xml` → 404. Body is `<!DOCTYPE html>` — a marketing page, not a feed. |
| `yc-oss` | `GET https://yc-oss.github.io/api/companies/all.json` | 200 | 1.180 s | **10,402,545** | **Yes.** 6,189 companies. First: `CircuitHub` — *"On-Demand Electronics Manufacturing"*. Both required fields present. |
| `suggest` | `GET https://suggestqueries.google.com/complete/search?client=firefox&hl=cs&ie=utf-8&oe=utf-8&q=datová%20schránka%20nefunguje` | 200 | 0.156 s | 145 | **Yes.** 2 completions: `datová schránka nefunguje`, `datová schránka nefunguje heslo`. *(First attempt used an ASCII-stripped seed and returned 0 completions in 26 bytes — a probe artefact, not a source failure.)* |
| `reddit-new` | `GET https://www.reddit.com/r/czech/new.rss` (UA `localproblems-register/1.0 …`) | 200 | 0.954 s | 43,673 | **Yes.** 25 `<entry>` elements. First: *"Zkušenosti s Rohlíkem"*, link `…/comments/1vte3hl/…`. No 429. |
| `reddit-search` | `GET https://www.reddit.com/r/czech/search.rss?q=nefunguje&restrict_sr=1&sort=new` (same UA) | 200 | 0.742 s | 69,438 | **Yes.** 25 entries. First: *"Filtrování reklam a videa na webu"*. No 429 despite following `reddit-new` by 40 s. |
| `nku` | `GET https://nku.cz/scripts/rka/vestnik.asp?rok=2026` *(non-www)* | 200 | 2.925 s | 28,795 | **Yes.** Title `Věstník NKÚ \| NKÚ`, **24 PDF links**, 86 `NN/NN` conclusion codes. Sample: `/assets/kon-zavery/K25021.pdf`. No redirect — the non-www workaround holds. |
| `sukl` | `HEAD` then `GET https://opendata.sukl.cz/soubory/MR/mr.zip` | 200 | 3.401 s / 2.880 s | 1,614,842 | **Yes.** `ETag: "18a3fa-6596e1588b8af"`, `Last-Modified: Wed, 19 Aug 2026 22:40:02 GMT` — **content changed ~10.6 h before the probe**, confirming sub-daily refresh. Zip holds `mr_hlaseni.csv` (**82,877 data rows**, 12.6 MB) + `mr_hlaseni_platnost.csv` (1 row). First record: `ACYLCOFFIN`, ATC `N02BA51`, `TYP_OZNAMENI: zahajeni`. |
| `ec-hys` | `GET https://ec.europa.eu/info/law/better-regulation/brpapi/searchInitiatives?size=5&language=EN&feedbackStatus=OPEN` | **curl 60** sandboxed → **200** unsandboxed | 0.966 s | 17,743 | **Yes** (unsandboxed). `totalElements: 44` open-feedback initiatives, 9 pages. First: *"Green-listing certain waste for the purposes of shipments to recovery between Member States"*, ref `Ares(2025)4387521`, topic `Environment`. Sandboxed attempt failed with `SSL certificate problem: unable to get local issuer certificate` — local TLS interception, **not** a remote refusal. |
| `nen` | `GET https://nen.nipez.cz/en/verejne-zakazky/p:vz:typVZ=Maly_rozsah,Zjednoduseny,Podlimitni,Podlimitni_mimo_ZVZ&datumPrvniUver=2026-06-01,2026-08-20&page=1` | 200 | 5.741 s | 282,398 | **Yes.** 51 `<tr>`, **50 unique detail codes** — exactly the catalog's 50 rows/page. First: `N006/26/V00026141` — *"Chemikálie pro elektroforézy"*, buyer `Ministerstvo obrany`, `24. 08. 2026 09:00`. |
| `mpsv` | `GET https://data.mpsv.cz/od/soubory/volna-mista` then `HEAD …/volna-mista.json` | 200 | 2.707 s / 0.369 s | 827 | **Partly.** The registry URL is an **Apache directory index**, not data — it lists 9 files. The dataset is `volna-mista.json`: `content-length: 185,271,163` (**185 MB**), `last-modified: Wed, 19 Aug 2026 20:08:48 GMT`. The metadata JSON-LD (10,488 B) confirms the `osobní údaje` declaration first-hand. |
| `ares` | `GET https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/27074358` | 200 | 2.593 s | 5,091 | **Yes.** Resolved IČO `27074358` → `Asseco Central Europe, a.s.`, `datumVzniku: 2003-08-06`, `czNace: ["55900","68200","47","69200",…]`, plus `sidlo`, `pravniForma`, `dic`. Every enrichment field the registry promises is present. |
| `demand-scan` · `arb-scan` · `round` | — | — | — | — | **NO-ENDPOINT.** These are agent research harvests, not HTTP feeds: `url: null`, `script: null`, `runner: attended`, `parse: manual`. There is nothing to probe, and their absence from this table is correct rather than a gap. They are scored on the other four axes above. |

---

## 5. What to build next — ranked by value per unit of effort

1. **`nen` fetcher — highest value-per-effort in the repo.** Value 5, route measured working
   today (200, 50 rows/page, buyer + subject + deadline in the table), 296 records already
   proven by hand, and the only missing piece is a script. One SSR `GET` plus a table parse
   against a URL shape that is already written down. Nothing is blocked; nobody has built it.
   *Caveat measured today:* the listing renders dates as `24. 08. 2026`, **not** ISO — the
   contract's `required_fields: ["datumPrvniUver"]` names a URL matrix parameter, not a
   column that appears in the HTML, so a naive field check will fail on a healthy payload.
2. **Close the `SCRIPTED-SILENT` gap — five feeds, near-zero fetch engineering.** `cc-cz`,
   `suggest`, `reddit-new`, `reddit-search` and `nku` all returned valid non-empty payloads in
   this probe run, and all five have produced **zero** records under their own key. That is
   4 of 17 feeds (24%) whose scripts run and whose output goes nowhere, plus `nku` whose
   script landed today. This is not a fetch problem — it is the normalize/ingest half never
   completing. **DIAGNOSED 2026-08-20, and it was never about the feeds** (§6.7): five
   defects in `scripts/normalize.py` sat between the fetchers and the ledger. Fixed; a
   crafted seven-feed run then staged 4,788 records with zero contract failures, and a
   118-record slice spanning all seven feeds completed and appended into three evidence
   ledgers. `nku` is the exception and stays scriptless-in-effect: its
   contract is `parse: html-table`, for which there is no structured parser by design, so
   its first records must come from an attended LLM-fallback pass.
3. **`sukl` fetcher.** Value 4, one URL, no auth, and the probe just removed the last unknown:
   the CSV columns are now measured (`KOD_SUKL`, `NAZEV`, `ATC`, `TYP_OZNAMENI`,
   `PLATNOST_OD`, `DATUM_HLASENI`, `DUVOD_PRERUSENI_UKONCENI`, `TERMIN_OBNOVENI`), so the
   registry's deliberately-empty `required_fields` can be filled with facts instead of
   guesses. ETag + `Last-Modified` are both served, so a conditional GET is trivial, and
   82,877 rows diff cleanly for outage trends.

**Deliberately ranked 4th, not 1st: `mpsv`.** It is the highest-value single build in the
registry (the only IČO join, value 5) but it is the *worst* value-per-effort right now,
because two hard prerequisites sit in front of it: the GDPR field allowlist and its checker
must exist before the first record is written, and the full dataset measured **185 MB**, so
the changelog/increment path (`typZmenyOpenData`) is mandatory rather than an optimisation.
Build it — just not before the three above, each of which is a day's work at most.

**Retracted, and worth reading as a lesson rather than deleted:** this section used to end
"`hlidac` cannot be fixed by feed work at all — the secrets path exports zero variables, so
adding `HLIDAC_TOKEN` to the vault fixes nothing. It is an owner action, not an engineering
one." Every clause of that is wrong. The secrets path works (`with-secrets` + curl
`--variable`/`--expand-header`); the token was already in the vault under a different name;
and the two things actually stopping the feed were both engineering defects in this repo
(§6.6). The claim survived because nobody re-ran the probe with the other name — a negative
recorded once and then quoted forever. **Re-measure before you repeat a blocker.**

---

## 6. Delta and integrity findings

### 6.1 Catalog sources with no registry row

`docs/sources-catalog.md` carries 19 numbered candidates plus 8 wave-2 routes and 2 wave-3
routes. Of the 19 numbered, **3 are in the registry** (#1 NKÚ → `nku`, #3 Have Your Say →
`ec-hys`, #4 SÚKL → `sukl`). **16 are not** — and the interesting part is that most are
*already producing records*, hidden inside the `demand-scan` harvest where no feed-health
check can see them. Counts are by id prefix across all 8 ledgers:

| Catalog # | Source | Tier | Records already in ledger | In registry? |
|---|---|---|---|---|
| 2 | Veřejný ochránce práv (ombudsman) | 1 | **14** (`ombud-*`) | **No** |
| 5 | ČOI | 1 | **3** (`coi-*`) | **No** |
| 6 | Finanční arbitr | 2 | **1** (`fa-*`) | **No** |
| 7 | MPO consumer policy | 2 | **3** (`mpo-*`) | **No** |
| 8 | Hospodářská komora ČR | 2 | **4** (`chamber-*` 3, `spcr-*` 1) | **No** |
| 9 | ČŠI | 2 | 0 — 403s generic fetchers | **No** |
| 10 | Mapa zadlužení / IPŘP / PAQ | 2 | 0 | **No** |
| 11 | NÚKIB | 2 | 0 | **No** |
| 12 | Svaz měst a obcí ČR | 2 | **1** (`smo-*`) | **No** |
| 13 | ČKAIT / ČLK / ČAK | 2 | 0 | **No** |
| 14 | ERÚ + ČTÚ | 3 | **3** (`eru-*` 1, `ctu-*` 2) | **No** |
| 15 | Participatory budgets (Brno) | 3 | within **32** `civic-*` | **No** |
| 16 | NGO service-gap reports | 3 | **2** (`ngo-*`) | **No** |
| 17 | Munipolis | 3 | 0 — catalog says do not build against it | **No** *(correctly)* |
| 18 | CVVM / STEM / Eurobarometer | 3 | 0 | **No** |
| 19 | University tech-transfer offices | 3 | 0 — catalog's honest negative | **No** *(correctly)* |
| w2 | EIC Accelerator winner lists | — | 0 | **No** |
| w2 | Plán legislativních prací vlády + psp.cz | — | within `reg-scan` (3 `psp.cz`, 15 `vlada.gov.cz`) | **No** |

Two of these absences are *correct* and should stay: #17 Munipolis (no public API, catalog
says watchlist only) and #19 TTOs (a recorded honest negative). The other 16 are the real
delta — the ombudsman in particular is the catalog's #2 source, is already contributing 14
records, and has predictable quarterly PDF URLs on file, yet has no registry row and
therefore no contract, no health check and no blocker of its own.

### 6.2 The `source` label collides — three different feeds share one key

`source: "hlidac"` holds **463** records, but they come from **three unrelated provenances**:

| id prefix | Count | What it actually is |
|---|---|---|
| `nen-*` | **296** | NEN below-threshold portal (`nen.nipez.cz`) — the `nen` feed, not Hlídač |
| `hlidac-*` | **114** | Genuine registr smluv (`smlouvy.gov.cz`) |
| `dotace-*` | **53** | **EU funding calls** (`cinea.ec.europa.eu`, `hadea.ec.europa.eu`) — e.g. *"CEF Transport 2026 — 1.1bn EUR for TEN-T"*. Not Czech contracts at all, and matching no registry feed or catalog entry. |

Anything counting per-feed yield off `.source` will over-credit Hlídač by **4×** and make the
one genuinely auth-blocked feed look like the healthiest tenders source in the repo. Per-feed
attribution in this file is by **id prefix** for that reason. The `dotace-*` 53 are an
unregistered producer that should either get a registry row or be relabelled.

### 6.3 `reg-scan` produces 126 records and has no registry row

`reg-scan` is the `signal_source` of `ec-hys`, but the two are not the same thing. By URL
host, the 126 `reg-scan` records are `eur-lex.europa.eu` (42), `e-sbirka.gov.cz` (18),
`vlada.gov.cz` (15), `zakonyprolidi.cz` (5), `psp.cz` (3) — a **legislative-tracking harvest**.
Only **10** touch an EC consultation URL. So `ec-hys` is credited with ~10 records here, not
126, and the remaining ~116 belong to a producer with **no feed key, no contract and no
health check** — the largest single hole in AC-F1 totality that this probe found.

### 6.4 Registry drift observed during the probe — RESOLVED

At **2026-08-20 11:12** the repo state and `data/feeds.json` (mtime 11:03) disagreed:
`feeds.json` said `nku`: `"script": null`, while `scripts/fetch_nku.sh` existed (untracked)
and `scripts/fetch_all.sh` already dispatched `nku` with that script path. The reading at
the time was "work in flight rather than a defect", and that reading was right.

**Re-checked 2026-08-20 15:20 and the drift is closed.** `git show HEAD:data/feeds.json`
carries `"script": "scripts/fetch_nku.sh"`, and `git ls-files scripts/` lists the fetcher as
tracked. The registry now describes the filesystem. `status` stays `planned`, and that is
not residual drift: `status` is INTENT and the intent is deliberate — the feed's contract is
`parse: html-table`, `fetch_all.sh` skips any non-`active` row with a `skipped` receipt, and
the first NKÚ records are meant to come from an attended LLM-fallback pass rather than an
unattended run that would only log a parse violation forever.

This entry is kept rather than deleted because the *shape* recurs: a doc that records a
disagreement between two files is only true at its timestamp, and the way to retire it is to
re-run the check and say so, never to assume it aged out.

### 6.5 The TED `scope=ALL` catalog claim did not reproduce

`docs/sources-catalog.md` (wave-2) states `scope` **MUST** be `"ALL"` because the default
`LATEST` "silently returns only today's OJ S edition". Measured today, an identical
date-filtered CZ query returned **`totalNoticeCount: 955` both with and without
`"scope":"ALL"`**. `scripts/fetch_ted.sh` sends no `scope` parameter and is evidently getting
the full range regardless. Two readings are possible and this probe cannot separate them: the
warning may only apply to queries carrying no `publication-date` filter, or the API default
may have changed. **Do not delete the catalog note** — but it should be narrowed to the query
shape it was actually observed on, and `fetch_ted.sh` is not currently at risk from it.

### 6.6 The Hlídač contract named a field the API does not return

Two defects, both measured against three authenticated 200s (75 items) on 2026-08-20, both
fixed the same day.

**(a) `required_fields` demanded `cenaSDph`, which appears on 0 of 75 items.** The FIELDS
check declares a feed BROKEN when a required key is missing from *every* item, so the
contract guaranteed a BROKEN verdict on a perfectly healthy payload — and `items_kept` 0
with it. `cenaSDph` is a real name, which is why it survived review: it is a **query-DSL**
field (the registry's own `it-large` query filters on `cenaSDph:>10000000` and returns 37
hits), not a response field. The response carries `hodnotaVcetneDph` (key on 25/25,
non-null 14/25), `hodnotaBezDph` (25/25, non-null 17/25) and `calculatedPriceWithVATinCZK`
(non-null 25/25 — the API's own CZK-including-VAT normalisation, which also resolves the
foreign-currency contracts `ciziMena` marks). Contract now requires `identifikator`,
`predmet`, `datumUzavreni`, `hodnotaVcetneDph`; the extractor reads the money fields in the
order above and treats a `0.0` price as *unpublished* rather than as a free contract.
PROVEN BOTH WAYS: the committed contract over the real payloads gives
`ok: 0 · "fields: cenaSDph missing from every item" · items_kept 0`; the corrected one gives
`ok: 1 · items_kept 283`.

**(b) `items_fetched` reported the API's `total`, not what landed on disk.** The fetcher
requested `strana=1` only, wrote 25 contracts per query, and then logged `total` — 477 for
the `nis2` query alone. The manifest, `fetch_log` and `/sources` therefore showed the feed
fetching roughly **4x more than it did**, and the ~92% of each result set nobody was paging
through was invisible *because* the over-count filled the hole. This is the failure mode the
whole receipt discipline exists for: a wrong number that reads like a healthy one. Fixed by
counting `len(results)` per page and paging to `HLIDAC_PAGES` (default 4) pages of 25, with
the shortfall carried on the manifest row as an `ok` result with a coverage note
(`coverage: 286 of 1076 available`) rather than as a failure. Measured after the fix at
`HLIDAC_PAGES=2`: **286 on disk, 286 reported, 1,076 available** — the under-fetch is now a
number you can read instead of one you cannot see.

### 6.7 Why five scripted feeds never landed a record — it was normalize, not the feeds

`docs/feeds-status.md` §5 has ranked "close the SCRIPTED-SILENT gap" second since this file
was written, on the theory that the normalize half "never completed". Measured 2026-08-20,
that was right about the location and understated the cause: **five separate defects in
`scripts/normalize.py`, three of them fatal to every record on every feed.**

| # | Defect | Measured blast radius |
|---|---|---|
| 1 | `--complete` required `geo_origin`; the `_needs` list an agent is told to fill never named it; no extractor set it | 4,397 of 4,397 staged records. A three-record `--complete` filled to exactly `_needs` exited 1 printing `geo_origin`. **Every feed**, not just reddit/suggest |
| 2 | Every extractor derived `date` by `str(value)[:10]`, which is a truncation and not a parse | cc-cz RSS `pubDate` -> `Thu, 20 Au`; yc-oss `launched_at` is UNIX epoch seconds -> `1322045523`. 4,397 of 4,397 records unusable, and the ledger FILE was named after it |
| 3 | `--complete` named the ledger file after the *record's* date instead of the run date | One run would have scattered across dozens of files (`funded/2011-11-23.jsonl`), contradicting SPEC §3 and breaking the run-date-from-filename rule `db.py` depends on |
| 4 | The payload-filename table matched `reddit-search` on tokens `scripts/fetch_reddit.sh` never writes — its search payloads are `reddit-<sub>-q-<term>.rss` | All four subs' search results filed under `reddit-new`. 0 of 4 correctly attributed before, 4 of 4 after, no other feed's filenames affected |
| 5 | Empty/absent optional receipts were written as `""` / `null` instead of being omitted | `SignalSchema` declares them `.optional()` (zod: undefined only) and `quote` adds `.min(1)`, so `quote: ""` — which normalize itself produces and counts as a `quote_failure` — or `http_status: null` from a feed with no fetch receipt is a **red build**, permanently, in an append-only ledger |

Defect 1 masked 2, 3 and 5: the refusal happened one step before any of them was reached, so
nobody had ever seen a completed run to find them in. Defect 5 has never fired only because
0 of 4,788 staged records currently carry an empty quote — luck about this corpus, not a
property of the code.

All five are fixed. `_needs` is now DERIVED from the same predicate `--complete` refuses on,
so that pair cannot drift apart again. Verified after the fix: a crafted seven-feed run
staged **4,788 records with 0 contract failures**, and a **118-record slice spanning all
seven feeds** completed into `demand` (48), `funded` (30) and `tenders` (40) — all three
files named for the run date — with **0 violations** against a field-for-field port of
`SignalSchema`. The port was then shown able to fail by planting each of the four traps
above, because a check that has never gone red is not evidence.

### 6.8 What the review found after §6.7 — three more, and one closed gap

§6.7's five defects reproduce exactly as written; every measurement in it was re-run
against the same payloads and the same HEAD. Three further defects were found in the
same file, and they matter because §6.7's own fix is what makes them reachable: nothing
could reach a ledger while `geo_origin` refused every record, so these had never had the
chance to write anything wrong.

| # | Defect | Measured blast radius |
|---|---|---|
| 6 | The payload key was recomputed inside the extraction loop and `break`-ed on the FIRST filename, so every item of a multi-file feed took the first file's key | `CPV_SECTOR` is the only thing that gives a TED record its `sector`. Measured on five synthetic CPV payloads (10 notices each): **all 50 records came out `sector: b2b`** — `ted-bizserv` sorts first. Silent twice over, because a wrongly-filled sector is non-empty and therefore never appears in `_needs`. Fixed by recording one payload key per item as the items are read |
| 7 | `--complete` named the ledger file from `date.today()` | §6.7 defect 3 fixed "named after the record's date"; the replacement reads the WALL CLOCK. `--complete --raw data/raw/2026-08-05` run on 2026-08-20 wrote `funded/2026-08-20.jsonl`. The attended half runs a session after the fetch by design, so the same staged file completes into two different filenames on two different days — and `ingest.sh`'s own printed hand-off (`db.py upsert …/$TODAY.jsonl`, `$TODAY` = the FETCH day) then names a path that does not exist. Fixed: the run date comes from the `data/raw/<date>/` being completed; `--today` still overrides |
| 8 | `fetched_at` was stamped with normalize's clock | CONVENTIONS.md defines it as "ISO timestamp of the payload this record came from". Measured on the committed 2026-08-20 payloads: receipt `started_at` 09:19:56Z, record `fetched_at` 14:08:15Z — **4h48m of drift on a same-day re-normalize**, days for an attended completion. This is the same fabricated-receipt defect §6.7 fixed for `http_status`, two lines below it in the same loop. Fixed: `fetched_at` is the receipt's `started_at`, shape-checked against `SignalSchema`'s `isoTimestamp`, and OMITTED when there is no receipt |

**And the gap §6.7 left open is now closed.** §6.7 verified its records against "a
field-for-field port of `SignalSchema`", which cannot catch a rule mis-transcribed. Run
end to end instead, on real data: `fetch_hlidac.sh` authenticated (7/7 HTTP 200, 135
contracts on disk of 443 available at `HLIDAC_PAGES=1`) → `normalize --mechanical-only`
(134 staged, 0 malformed ids, 0 non-ISO dates) → `--complete` (134 appended to
`tenders/2026-08-20.jsonl`) → **`npm --prefix web run build` GREEN against real zod.**
Both latent build-breakers from §6.7 defect 5 were also planted and watched fail:
`quote: ""` → `quote: Too small: expected string to have >=1 characters`;
`http_status: null` → `http_status: Invalid input: expected number, received null`.

**Still not measured:** a real all-feeds run has never been green — `fetch_all.sh`,
`fetch_ted.sh`, `fetch_reddit.sh`, `fetch_suggest.sh` and `fetch_nku.sh` were not
executed by this review either, so defect 6's fix is proven on synthetic TED payloads
and on real Hlídač ones, not on a real TED fetch. `HLIDAC_PAGES=4` (the default) remains
untested; the runs behind this file are at 1 and 2 pages.

---

## 7. Counts

**By probe verdict (denominator 17):** WORKS 13 · BLOCKED 1 (`vestbee`) ·
NO-ENDPOINT 3 (`demand-scan`, `arb-scan`, `round`). *(Was "AUTH 1 (`hlidac`)" — retired
2026-08-20: `hlidac` authenticates. See §6.6 and the retraction in §5.)*

**By progress state (denominator 17):**

| State | Count | Feeds |
|---|---|---|
| `SCRIPTED` | **3** | `ted`, `yc-oss`, `hlidac` |
| `SCRIPTED-SILENT` | **5** | `cc-cz`, `suggest`, `reddit-new`, `reddit-search`, `nku` |
| `SCRIPTED-BLOCKED` | **0** | — |
| `ROUTE-KNOWN` | **5** | `nen`, `mpsv`, `sukl`, `ec-hys`, `ares` |
| `MANUAL` | **3** | `demand-scan`, `arb-scan`, `round` |
| `DEAD` | **1** | `vestbee` |

**The headline:** 13 of 17 feeds return a healthy payload from this machine today, and
**3** are proven end-to-end. Nothing in this registry is blocked by a remote refusal —
`ec-hys` is blocked by a local TLS proxy and `vestbee` is simply gone.

**The five `SCRIPTED-SILENT` rows stay silent in this table on purpose.** The defects that
kept them silent are fixed and a crafted run proved the path (§6.7), but `SCRIPTED` in §2
means *records have reached the ledger*, and none have — the completing step is an attended
model pass that has not been run since the fix. Promoting them here on the strength of a
fixed bug would be exactly the "looks healthy, produced nothing" claim this file exists to
prevent. The next attended ingest run is what moves them, and nothing else.
