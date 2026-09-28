# run manifest — 2026-09-28

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-09-28`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-28T0440 | ted | ok | 200 | 65954940 | 8001 | 42970 | 2026-09-28T04:40:50Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | hlidac | ok | 200 | 1965254 | 821 | 24652 | 2026-09-28T04:41:40Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | veklep | ok | 200 | 1760317 | 143 | 6527 | 2026-09-28T04:43:50Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | tacr | ok | 200 | 264246 | 14 | 2163 | 2026-09-28T04:44:12Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | hackathon | ok | 200 | 5470389 | 14 | 15792 | 2026-09-28T04:44:15Z | data/raw/2026-09-28 | partial: hackjakbrno:mode-a upol:yield-zero |
| 2026-09-28T0440 | nen-ptk | ok | 200 | 45587124 | 139 | 342956 | 2026-09-28T04:44:32Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | edesky | skipped | 000 | 0 | 0 | 0 | 2026-09-28T06:51:29Z |  | registry status=planned |
| 2026-09-28T0440 | cc-cz | ok | 200 | 17692 |  | 978 | 2026-09-28T06:51:33Z | data/raw/2026-09-28/feed-czechcrunch.xml |  |
| 2026-09-28T0440 | yc-oss | ok | 200 | 10513933 |  | 6578 | 2026-09-28T06:51:34Z | data/raw/2026-09-28/yc-all.json |  |
| 2026-09-28T0440 | vestbee | ok | 200 | 1065432 | 29 | 2650 | 2026-09-28T06:51:41Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | suggest | ok | 200 | 11895 | 42 | 98494 | 2026-09-28T06:52:44Z | data/raw/2026-09-28/suggest-pain.jsonl |  |
| 2026-09-28T0440 | reddit-new | ok | 200 | 188700 | 100 | 2642 | 2026-09-28T06:58:05Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | reddit-search | ok | 200 | 330188 | 100 | 1948 | 2026-09-28T06:58:05Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | nku | ok | 200 | 77587 | 128 | 1526 | 2026-09-28T06:59:07Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | sukl | ok | 200 | 1626823 | 15 | 4848 | 2026-09-28T06:59:09Z | data/raw/2026-09-28 | validity=2026-09-28 rows_in_file=83428 aggregates=15 |
| 2026-09-28T0440 | ec-hys | ok | 200 | 128160 | 34 | 5494 | 2026-09-28T06:59:15Z | data/raw/2026-09-28 |  |
| 2026-09-28T0440 | nen | skipped | 000 | 0 | 0 | 0 | 2026-09-28T06:59:48Z |  | registry status=planned |
| 2026-09-28T0440 | mpsv | skipped | 000 | 0 | 0 | 0 | 2026-09-28T06:59:49Z | data/raw/2026-09-28 | month 2026-08 already present in seen.txt |
| 2026-09-28T0440 | coi | skipped | 200 | 39676640 | 0 | 42709 | 2026-09-28T06:59:49Z | data/raw/2026-09-28 | no completed half-year to emit: None |
| 2026-09-28T0440 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-09-28T07:00:33Z |  | registry status=planned |

---

# Ingest run 2026-09-28T0900
Run date: 2026-09-28  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 17692 | 10 | 10 | — | structured | yes |  |
| `coi` | 200 | 39676640 | 0 | 0 | — | none | yes | no completed half-year to emit: None |
| `ec-hys` | 200 | 128160 | 34 | 13 | — | structured | yes |  |
| `hackathon` | 200 | 5470389 | 14 | 11 | below-range | structured | yes | partial: hackjakbrno:mode-a upol:yield-zero |
| `hlidac` | 200 | 1965254 | 821 | 80 | — | structured | yes |  |
| `mpsv` | — | 0 | 0 | 0 | — | none | yes | month 2026-08 already present in seen.txt |
| `nen-ptk` | 200 | 45587124 | 139 | 64 | above-range | structured | yes |  |
| `nku` | 200 | 77587 | 128 | 126 | — | structured | yes |  |
| `reddit-new` | 200 | 188700 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 330188 | 100 | 74 | — | structured | yes |  |
| `suggest` | 200 | 11895 | 42 | 27 | — | structured | yes |  |
| `sukl` | 200 | 1626823 | 15 | 0 | — | structured | yes | validity=2026-09-28 rows_in_file=83428 aggregates=15 |
| `tacr` | 200 | 264246 | 14 | 6 | — | structured | yes |  |
| `ted` | 200 | 65954940 | 8001 | 3005 | — | structured | yes |  |
| `veklep` | 200 | 1760317 | 143 | 11 | — | structured | yes |  |
| `vestbee` | 200 | 1065432 | 29 | 6 | — | structured | yes |  |
| `yc-oss` | 200 | 10513933 | 6253 | 920 | — | structured | yes |  |

## Staged records — PENDING, not appended

4404 records carry their mechanical fields and are waiting on a model. 11390 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 4404 |
| `scores.recurrence` | 4404 |
| `sector` | 4404 |
| `geo_origin` | 4404 |
| `title` | 3486 |
| `summary` | 3486 |
| `pain` | 201 |
| `stated_need` | 80 |
| `scores.urgency` | 74 |

**Transport status UNKNOWN for 1 feed(s):** `mpsv`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 4404 staged record(s) passed the field allowlist and the email/phone content scan.

## Republication candidates — same quote and value, new notice id

**225 staged tender record(s) repeat the verbatim quote and the value of a record already on file.** TED re-notifies the same procurement under a new number and neither dedup axis can see it. They are KEPT — a re-issued tender can be evidence (p-0031) — each carries the earlier id in `notes`, and MATCH decides dup or distinct.

| staged id | repeats | seen in |
|---|---|---|
| `hlidac-37273929` | `hlidac-37272177` | batch |
| `ted-536808-2026` | `ted-547009-2026` | ledger |
| `ted-536828-2026` | `ted-560207-2026` | ledger |
| `ted-541036-2026` | `ted-557909-2026` | ledger |
| `ted-543982-2026` | `ted-527994-2026` | batch |
| `ted-545908-2026` | `ted-532795-2026` | batch |
| `ted-552739-2026` | `ted-528999-2026` | batch |
| `ted-555462-2026` | `ted-554061-2026` | batch |
| `ted-556897-2026` | `ted-545152-2026` | batch |
| `ted-556949-2026` | `ted-554061-2026` | batch |
| `ted-557720-2026` | `ted-599397-2026` | ledger |
| `ted-565027-2026` | `ted-553142-2026` | batch |
| `ted-566552-2026` | `ted-533014-2026` | batch |
| `ted-571334-2026` | `ted-570329-2026` | batch |
| `ted-573735-2026` | `ted-596228-2026` | ledger |
| `ted-580531-2026` | `ted-585863-2026` | ledger |
| `ted-584625-2026` | `ted-553308-2026` | batch |
| `ted-602172-2026` | `ted-600285-2026` | batch |
| `ted-602795-2026` | `ted-599397-2026` | ledger |
| `ted-603768-2026` | `ted-545152-2026` | batch |
| `ted-605581-2026` | `ted-596494-2026` | batch |
| `ted-606337-2026` | `ted-533174-2026` | batch |
| `ted-609008-2026` | `ted-588567-2026` | ledger |
| `ted-611301-2026` | `ted-610027-2026` | batch |
| `ted-611847-2026` | `ted-608668-2026` | batch |
| `ted-612086-2026` | `ted-610856-2026` | batch |
| `ted-612438-2026` | `ted-540209-2026` | ledger |
| `ted-614696-2026` | `ted-535070-2026` | ledger |
| `ted-614985-2026` | `ted-545152-2026` | batch |
| `ted-615079-2026` | `ted-612286-2026` | batch |
| `ted-615618-2026` | `ted-544133-2026` | ledger |
| `ted-620340-2026` | `ted-533142-2026`, `ted-593389-2026` | ledger |
| `ted-621151-2026` | `ted-582057-2026` | batch |
| `ted-621196-2026` | `ted-550596-2026` | ledger |
| `ted-621214-2026` | `ted-622067-2026` | ledger |
| `ted-621287-2026` | `ted-619553-2026` | batch |
| `ted-621987-2026` | `ted-528464-2026` | ledger |
| `ted-622336-2026` | `ted-564208-2026`, `ted-575552-2026`, `ted-579550-2026`, `ted-604354-2026`, `ted-610001-2026` | ledger |
| `ted-623347-2026` | `ted-622944-2026` | batch |
| `ted-625487-2026` | `ted-528024-2026` | ledger |
| `ted-625493-2026` | `ted-547014-2026` | ledger |
| `ted-631802-2026` | `ted-534000-2026` | batch |
| `ted-633463-2026` | `ted-609630-2026` | ledger |
| `ted-640693-2026` | `ted-471282-2026`, `ted-615443-2026` | ledger |
| `ted-642898-2026` | `ted-637714-2026` | batch |
| `ted-645157-2026` | `ted-607500-2026` | batch |
| `ted-650322-2026` | `ted-477412-2026`, `ted-493185-2026`, `ted-562526-2026`, `ted-590645-2026` | ledger |
| `ted-650393-2026` | `ted-626906-2026` | ledger |
| `ted-650585-2026` | `ted-596203-2026` | ledger |
| `ted-650707-2026` | `ted-585683-2026` | ledger |
| `ted-650826-2026` | `ted-642047-2026` | batch |
| `ted-650832-2026` | `ted-609007-2026` | ledger |
| `ted-650940-2026` | `ted-650271-2026` | batch |
| `ted-651059-2026` | `ted-520111-2026` | ledger |
| `ted-651764-2026` | `ted-613467-2026` | ledger |
| `ted-651823-2026` | `ted-504975-2026`, `ted-506356-2026` | ledger |
| `ted-651913-2026` | `ted-627506-2026` | ledger |
| `ted-652071-2026` | `ted-625755-2026` | ledger |
| `ted-652142-2026` | `ted-625943-2026` | ledger |
| `ted-652163-2026` | `ted-651064-2026` | batch |
| `ted-652279-2026` | `ted-593070-2026` | ledger |
| `ted-652282-2026` | `ted-596358-2026` | ledger |
| `ted-652327-2026` | `ted-594233-2026` | ledger |
| `ted-652434-2026` | `ted-630617-2026` | ledger |
| `ted-652490-2026` | `ted-461180-2026`, `ted-477824-2026`, `ted-522836-2026`, `ted-560780-2026`, `ted-568558-2026`, `ted-617274-2026`, `ted-633374-2026` | ledger |
| `ted-652559-2026` | `ted-591418-2026`, `ted-640810-2026`, `ted-643165-2026`, `ted-646553-2026` | ledger |
| `ted-652642-2026` | `ted-502499-2026`, `ted-583423-2026`, `ted-621507-2026` | ledger |
| `ted-652719-2026` | `ted-597696-2026` | ledger |
| `ted-652786-2026` | `ted-637023-2026` | ledger |
| `ted-652823-2026` | `ted-585063-2026` | ledger |
| `ted-652925-2026` | `ted-564353-2026` | ledger |
| `ted-652930-2026` | `ted-652500-2026` | batch |
| `ted-652934-2026` | `ted-563956-2026`, `ted-644697-2026` | ledger |
| `ted-652950-2026` | `ted-513956-2026`, `ted-601492-2026` | ledger |
| `ted-653057-2026` | `ted-621842-2026` | batch |
| `ted-653186-2026` | `ted-589830-2026`, `ted-610006-2026`, `ted-628111-2026` | ledger |
| `ted-653578-2026` | `ted-570930-2026`, `ted-605404-2026` | ledger |
| `ted-653745-2026` | `ted-588762-2026`, `ted-609303-2026`, `ted-625251-2026`, `ted-629623-2026`, `ted-644325-2026` | ledger |
| `ted-653863-2026` | `ted-637037-2026`, `ted-641532-2026` | ledger |
| `ted-653974-2026` | `ted-577270-2026` | batch |
| `ted-654067-2026` | `ted-594786-2026` | ledger |
| `ted-654086-2026` | `ted-549308-2026`, `ted-594098-2026`, `ted-604569-2026`, `ted-620705-2026` | ledger |
| `ted-654453-2026` | `ted-586011-2026` | ledger |
| `ted-654549-2026` | `ted-602131-2026`, `ted-606455-2026`, `ted-623961-2026`, `ted-641424-2026` | ledger |
| `ted-654557-2026` | `ted-581636-2026`, `ted-620085-2026` | ledger |
| `ted-654559-2026` | `ted-617576-2026` | batch |
| `ted-654677-2026` | `ted-576762-2026` | ledger |
| `ted-654684-2026` | `ted-651967-2026` | batch |
| `ted-654727-2026` | `ted-590210-2026` | ledger |
| `ted-654818-2026` | `ted-636901-2026` | ledger |
| `ted-654845-2026` | `ted-540691-2026` | ledger |
| `ted-654888-2026` | `ted-590480-2026`, `ted-620380-2026`, `ted-641475-2026` | ledger |
| `ted-654914-2026` | `ted-580642-2026`, `ted-614675-2026`, `ted-621080-2026`, `ted-626448-2026`, `ted-634522-2026`, `ted-638649-2026` | ledger |
| `ted-655064-2026` | `ted-579015-2026` | ledger |
| `ted-655135-2026` | `ted-587413-2026`, `ted-615564-2026` | ledger |
| `ted-655612-2026` | `ted-640483-2026` | ledger |
| `ted-655677-2026` | `ted-591378-2026` | ledger |
| `ted-655812-2026` | `ted-536135-2026`, `ted-584748-2026`, `ted-585419-2026` | ledger |
| `ted-656002-2026` | `ted-574737-2026`, `ted-638862-2026`, `ted-642266-2026`, `ted-645625-2026` | ledger |
| `ted-656013-2026` | `ted-530681-2026` | batch |
| `ted-656020-2026` | `ted-567576-2026`, `ted-629638-2026` | ledger |
| `ted-656137-2026` | `ted-650579-2026` | batch |
| `ted-656322-2026` | `ted-569202-2026`, `ted-599255-2026`, `ted-610739-2026` | ledger |
| `ted-656431-2026` | `ted-471761-2026`, `ted-479736-2026`, `ted-490749-2026`, `ted-505800-2026`, `ted-532517-2026`, `ted-555812-2026`, `ted-565673-2026`, `ted-576774-2026`, `ted-585277-2026`, `ted-596315-2026`, `ted-611059-2026`, `ted-625848-2026`, `ted-632248-2026`, `ted-637497-2026` | ledger |
| `ted-656444-2026` | `ted-615983-2026` | ledger |
| `ted-656546-2026` | `ted-599842-2026`, `ted-628247-2026` | ledger |
| `ted-657107-2026` | `ted-604530-2026` | ledger |
| `ted-657336-2026` | `ted-620298-2026`, `ted-640251-2026` | ledger |
| `ted-657383-2026` | `ted-635766-2026` | ledger |
| `ted-657420-2026` | `ted-530859-2026`, `ted-551198-2026`, `ted-566641-2026` | ledger |
| `ted-657457-2026` | `ted-581077-2026`, `ted-619596-2026` | ledger |
| `ted-657504-2026` | `ted-625066-2026`, `ted-635334-2026` | ledger |
| `ted-657622-2026` | `ted-487388-2026`, `ted-567182-2026`, `ted-605248-2026` | ledger |
| `ted-657663-2026` | `ted-595964-2026`, `ted-638058-2026` | ledger |
| `ted-657795-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-657799-2026` | `ted-604757-2026` | ledger |
| `ted-657894-2026` | `ted-488911-2026`, `ted-533408-2026`, `ted-540928-2026`, `ted-550874-2026`, `ted-555408-2026`, `ted-568835-2026`, `ted-590021-2026`, `ted-593753-2026`, `ted-600559-2026`, `ted-618373-2026`, `ted-628024-2026`, `ted-643610-2026` | ledger |
| `ted-657918-2026` | `ted-521305-2026` | ledger |
| `ted-657930-2026` | `ted-527994-2026` | batch |
| `ted-657970-2026` | `ted-609844-2026`, `ted-634994-2026` | ledger |
| `ted-658092-2026` | `ted-563059-2026`, `ted-625529-2026`, `ted-640568-2026` | ledger |
| `ted-658104-2026` | `ted-657364-2026` | batch |
| `ted-658135-2026` | `ted-629659-2026` | ledger |
| `ted-658331-2026` | `ted-476510-2026`, `ted-523188-2026`, `ted-611853-2026` | ledger |
| `ted-658424-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-658753-2026` | `ted-578250-2026`, `ted-609713-2026`, `ted-623589-2026`, `ted-629262-2026` | ledger |
| `ted-658756-2026` | `ted-654707-2026` | batch |
| `ted-658806-2026` | `ted-652999-2026` | batch |
| `ted-659029-2026` | `ted-584813-2026` | ledger |
| `ted-659130-2026` | `ted-635057-2026` | ledger |
| `ted-659171-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-659176-2026` | `ted-612350-2026`, `ted-634932-2026` | ledger |
| `ted-659192-2026` | `ted-659191-2026` | batch |
| `ted-659209-2026` | `ted-610209-2026` | ledger |
| `ted-659253-2026` | `ted-657199-2026` | batch |
| `ted-659258-2026` | `ted-568539-2026`, `ted-622763-2026` | ledger |
| `ted-659394-2026` | `ted-547596-2026`, `ted-603014-2026` | ledger |
| `ted-659435-2026` | `ted-477579-2026`, `ted-507989-2026`, `ted-519602-2026`, `ted-538178-2026`, `ted-558024-2026`, `ted-581728-2026`, `ted-603543-2026`, `ted-606067-2026`, `ted-628817-2026`, `ted-645808-2026` | ledger |
| `ted-659558-2026` | `ted-581960-2026` | ledger |
| `ted-659625-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-659634-2026` | `ted-531621-2026` | ledger |
| `ted-659665-2026` | `ted-549644-2026`, `ted-622847-2026`, `ted-640013-2026` | ledger |
| `ted-659682-2026` | `ted-657371-2026` | batch |
| `ted-659687-2026` | `ted-469306-2026`, `ted-505445-2026`, `ted-536637-2026` | ledger |
| `ted-659703-2026` | `ted-579752-2026`, `ted-620801-2026` | ledger |
| `ted-659751-2026` | `ted-651128-2026` | batch |
| `ted-659987-2026` | `ted-591481-2026` | ledger |
| `ted-660010-2026` | `ted-612494-2026` | ledger |
| `ted-660055-2026` | `ted-642228-2026` | ledger |
| `ted-660103-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-660243-2026` | `ted-554275-2026`, `ted-589691-2026`, `ted-626435-2026`, `ted-636746-2026` | ledger |
| `ted-660258-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-660371-2026` | `ted-617782-2026` | ledger |
| `ted-660384-2026` | `ted-626041-2026` | ledger |
| `ted-660421-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-660475-2026` | `ted-599397-2026` | ledger |
| `ted-660556-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-660812-2026` | `ted-484442-2026` | ledger |
| `ted-660836-2026` | `ted-531756-2026`, `ted-560017-2026`, `ted-580549-2026`, `ted-631877-2026` | ledger |
| `ted-660848-2026` | `ted-660769-2026` | batch |
| `ted-660928-2026` | `ted-660769-2026` | batch |
| `ted-661057-2026` | `ted-594514-2026` | ledger |
| `ted-661079-2026` | `ted-484442-2026` | ledger |
| `ted-661370-2026` | `ted-509527-2026` | ledger |
| `ted-661379-2026` | `ted-536424-2026`, `ted-551970-2026`, `ted-573041-2026` | ledger |
| `ted-661396-2026` | `ted-595586-2026` | ledger |
| `ted-661716-2026` | `ted-487706-2026`, `ted-558632-2026`, `ted-624737-2026` | ledger |
| `ted-662110-2026` | `ted-495725-2026`, `ted-500012-2026`, `ted-502986-2026`, `ted-522774-2026`, `ted-561946-2026`, `ted-575418-2026`, `ted-590261-2026` | ledger |
| `ted-662151-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026`, `ted-620795-2026`, `ted-626356-2026`, `ted-633846-2026` | ledger |
| `ted-662183-2026` | `ted-595961-2026`, `ted-610436-2026` | ledger |
| `ted-662204-2026` | `ted-528227-2026`, `ted-555065-2026`, `ted-624244-2026`, `ted-640580-2026` | ledger |
| `ted-662233-2026` | `ted-590898-2026` | ledger |
| `ted-662266-2026` | `ted-602907-2026` | ledger |
| `ted-662334-2026` | `ted-614665-2026` | ledger |
| `ted-662404-2026` | `ted-659191-2026` | batch |
| `ted-662424-2026` | `ted-660769-2026` | batch |
| `ted-662426-2026` | `ted-598992-2026` | ledger |
| `ted-662675-2026` | `ted-536370-2026`, `ted-622187-2026`, `ted-635634-2026` | ledger |
| `ted-662676-2026` | `ted-574737-2026`, `ted-638862-2026`, `ted-642266-2026`, `ted-645625-2026` | ledger |
| `ted-662741-2026` | `ted-590281-2026` | ledger |
| `ted-662926-2026` | `ted-605206-2026`, `ted-648765-2026` | ledger |
| `ted-662943-2026` | `ted-593885-2026` | ledger |
| `ted-662974-2026` | `ted-565066-2026` | ledger |
| `ted-663066-2026` | `ted-567340-2026`, `ted-644708-2026` | ledger |
| `ted-663095-2026` | `ted-586672-2026` | ledger |
| `ted-663109-2026` | `ted-580642-2026`, `ted-614675-2026`, `ted-621080-2026`, `ted-626448-2026`, `ted-634522-2026`, `ted-638649-2026` | ledger |
| `ted-663163-2026` | `ted-554184-2026`, `ted-576756-2026`, `ted-641354-2026` | ledger |
| `ted-663171-2026` | `ted-661790-2026` | batch |
| `ted-663222-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-663475-2026` | `ted-545018-2026`, `ted-545288-2026`, `ted-545893-2026`, `ted-546347-2026`, `ted-578596-2026`, `ted-609735-2026`, `ted-611559-2026`, `ted-612495-2026` | ledger |
| `ted-663478-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026` | ledger |
| `ted-663773-2026` | `ted-579988-2026`, `ted-604859-2026` | ledger |
| `ted-663965-2026` | `ted-615301-2026` | ledger |
| `ted-663972-2026` | `ted-490911-2026`, `ted-531770-2026`, `ted-558714-2026`, `ted-634730-2026` | ledger |
| `ted-664228-2026` | `ted-650245-2026` | batch |
| `ted-664315-2026` | `ted-561823-2026` | ledger |
| `ted-664347-2026` | `ted-566954-2026` | ledger |
| `ted-664483-2026` | `ted-490911-2026`, `ted-531770-2026`, `ted-558714-2026`, `ted-634730-2026` | ledger |
| `ted-664854-2026` | `ted-591590-2026`, `ted-641320-2026` | ledger |
| `ted-664960-2026` | `ted-488033-2026`, `ted-516010-2026`, `ted-547691-2026`, `ted-565387-2026`, `ted-576952-2026`, `ted-579054-2026`, `ted-583339-2026`, `ted-609049-2026`, `ted-646805-2026` | ledger |
| `ted-665110-2026` | `ted-488911-2026`, `ted-533408-2026`, `ted-540928-2026`, `ted-550874-2026`, `ted-555408-2026`, `ted-568835-2026`, `ted-590021-2026`, `ted-593753-2026`, `ted-600559-2026`, `ted-618373-2026`, `ted-628024-2026`, `ted-643610-2026` | ledger |
| `ted-665295-2026` | `ted-594537-2026` | ledger |
| `ted-665642-2026` | `ted-566557-2026` | ledger |
| `ted-665679-2026` | `ted-544821-2026`, `ted-632625-2026` | ledger |
| `ted-665888-2026` | `ted-606988-2026`, `ted-640381-2026` | ledger |
| `ted-665982-2026` | `ted-610869-2026` | ledger |
| `ted-666083-2026` | `ted-620247-2026` | ledger |
| `ted-666087-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026`, `ted-620795-2026`, `ted-626356-2026`, `ted-633846-2026` | ledger |
| `ted-666245-2026` | `ted-610132-2026` | ledger |
| `ted-666326-2026` | `ted-596347-2026`, `ted-628548-2026`, `ted-629778-2026`, `ted-639270-2026`, `ted-646352-2026` | ledger |
| `ted-666340-2026` | `ted-550596-2026` | ledger |
| `ted-666422-2026` | `ted-626770-2026`, `ted-649987-2026` | ledger |
| `ted-666480-2026` | `ted-585863-2026` | ledger |
| `ted-666498-2026` | `ted-626790-2026` | ledger |
| `ted-666529-2026` | `ted-631491-2026` | ledger |
| `ted-666531-2026` | `ted-487594-2026`, `ted-488105-2026` | ledger |
| `ted-666669-2026` | `ted-590664-2026` | ledger |
| `ted-666770-2026` | `ted-578619-2026` | ledger |
| `ted-666988-2026` | `ted-485208-2026` | ledger |
| `ted-667020-2026` | `ted-466905-2026`, `ted-548527-2026`, `ted-573412-2026`, `ted-606562-2026`, `ted-638301-2026` | ledger |
| `ted-667096-2026` | `ted-651788-2026` | batch |
| `ted-667133-2026` | `ted-593496-2026` | ledger |
| `ted-667145-2026` | `ted-574737-2026`, `ted-638862-2026`, `ted-642266-2026`, `ted-645625-2026` | ledger |
| `ted-667162-2026` | `ted-618216-2026` | ledger |
| `ted-667178-2026` | `ted-487594-2026`, `ted-488105-2026` | ledger |

## Dedup by identity key — same resource, different id

**49 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
| `echys-14628` | `consult-cloud-ai-act` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14628 |
| `echys-14638` | `consult-europol-mandate` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14638 |
| `echys-15252` | `consult-territorial-supply-constraints` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15252 |
| `echys-16413` | `consult-horizon-partnerships` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16413 |
| `echys-17172` | `consult-dual-use-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17172 |
| `echys-17912` | `consult-mica-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17912 |
| `echys-18194` | `consult-victims-rights-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18194 |
| `echys-18658` | `consult-housing-simplification` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18658 |
| `hack-ebca5de0` | `hack-c5c10e91` | `url` | `hackathon` | https://www.aimtechackathon.cz/hackathon/ |
| `nku-k24032` | `nku-urad-prace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24032.pdf |
| `nku-k24008` | `nku-rsc-sport` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24008.pdf |
| `nku-k25001` | `nku-dph-ecommerce` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25001.pdf |
| `nku-k24018` | `nku-odpocivky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24018.pdf |
| `nku-k24025` | `nku-erecept-sms` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24025.pdf |
| `nku-k24016` | `nku-lesnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24016.pdf |
| `nku-k24009` | `nku-fakultni-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24009.pdf |
| `nku-k24014` | `nku-nelegalni-prace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24014.pdf |
| `nku-k24017` | `nku-gacr-tacr` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24017.pdf |
| `nku-k24007` | `nku-dtm` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24007.pdf |
| `nku-k24006` | `nku-modernizacni-fond` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24006.pdf |
| `nku-k24012` | `nku-vycvik-acr` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24012.pdf |
| `nku-k24004` | `nku-esbirka` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24004.pdf |
| `nku-k24001` | `nku-pesi-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24001.pdf |
| `nku-k23031` | `nku-pozemkove-upravy` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K23031.pdf |
| `nku-k25018` | `nku-zemedelsky-vyzkum` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25018.pdf |
| `nku-k25014` | `nku-ikem-hospodareni` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25014.pdf |
| `nku-k25013` | `nku-zdravotnicky-vyzkum` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25013.pdf |
| `nku-k25021` | `nku-up-ucetni-zaverka-2025` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25021.pdf |
| `nku-k25017` | `nku-dia-ucetnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25017.pdf |
| `nku-k24024` | `nku-uspory-energie` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24024.pdf |
| `nku-k25012` | `nku-letecka-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25012.pdf |
| `nku-k25011` | `nku-cista-mobilita` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25011.pdf |
| `nku-k25005` | `nku-etcs` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25005.pdf |
| `nku-k25008` | `nku-srazkove-vody` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25008.pdf |
| `nku-k25007` | `nku-react-eu-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25007.pdf |
| `nku-k25009` | `nku-vrt` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25009.pdf |
| `nku-k25003` | `nku-majetkove-ucasti` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25003.pdf |
| `nku-k25004` | `nku-mistni-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25004.pdf |
| `nku-k25006` | `nku-protipovodnova-ochrana` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25006.pdf |
| `nku-k24028` | `nku-statni-sluzba` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24028.pdf |
| `nku-k24029` | `nku-msmt-horizont-kontroly` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24029.pdf |
| `nku-k25002` | `nku-rizeni-skolstvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25002.pdf |
| `nku-k24031` | `nku-justicni-pohledavky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24031.pdf |
| `nku-k24030` | `nku-doprava2020` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24030.pdf |
| `nku-k24026` | `nku-viza-it` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24026.pdf |
| `veklep-KORNDW7HRLI7` | `reg-veznice-ubytovaci-plocha-2030` | `url` | `veklep` | https://odok.gov.cz/portal/veklep/material/KORNDW7HRLI7/ |
| `veklep-KORNDUAFXG1S` | `reg-pozemkove-upravy-vykupy-2027` | `url` | `veklep` | https://odok.gov.cz/portal/veklep/material/KORNDUAFXG1S/ |
| `yc-d-model` | `yc-d_model` | `url` | `yc-oss` | https://www.ycombinator.com/companies/d_model |
| `yc-galactic-resource-utilization-space-inc-gru-spac` | `yc-galactic-resource-utilization-space-inc-gru-space` | `url` | `yc-oss` | https://www.ycombinator.com/companies/galactic-resource-utilization-space-inc-gru-space |

**2 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:idea13.cz/` | carried by 4 records in THIS batch — undecidable, so no merge |
| `url:nakopniprahu.cz/` | carried by 6 records in THIS batch — undecidable, so no merge |


# Attended scan passes — 2026-09-28

Four attended feeds ran in parallel as subagents, each staging only into its own
`data/raw/2026-09-28/<feed>/` directory. The coordinator ran `normalize.py --complete --today 2026-09-28`
once per feed, sequentially, and those runs appended to `seen.txt`; `sort -c` confirmed it sorted.
Every staged record carried `evidence_type` explicitly, so none was mis-routed.

| feed | records appended | ledger |
|---|---|---|
| demand-scan | 1 | `data/signals/demand/2026-09-28.jsonl` |
| reg-scan | 6 | `data/signals/regulation/2026-09-28.jsonl` |
| dotace-scan | 0 | — (MS2021+ diff +2/−0, both planned 2027 calls; the two newly opened calls already in the ledger) |
| arb-scan | 5 | `data/signals/funded/2026-09-28.jsonl` |

Coordinator registry change: `se` added to arb-scan `id_prefixes` (Tandem Health, a Swedish round, could not be staged without it).

## demand-scan pass — 2026-09-28 (weekly delta)

This is the weekly delta pass of feed `demand-scan` (evidence_type `demand`), run seven days
after the pass of 2026-09-21 (`data/raw/2026-09-21/manifest.md`, demand section). It follows
pipeline/SCANS.md and walked every checklist source. The window was **items published or newly
surfaced since 2026-09-21**, plus everything the 2026-09-21 pass said it owed. It also followed
up the 2026-09-21 weekly report's candidate *"Czech research recipients lose grant money to
reporting they got wrong"* by looking for evidence from the recipient side.

Worktree `localproblems-weekly-2026-09-28`. This pass wrote to its own paths only: payloads
under `data/raw/2026-09-28/demand/pages/`, `data/raw/2026-09-28/demand/staged.jsonl` and this
file. It made no ledger write, no seen.txt write, no dropped-log write, no DB write, no
feeds.json edit and no git state change.

### Hand-off

- `data/raw/2026-09-28/demand/staged.jsonl` holds **1 record**:
  `civic-mf-odvody-rozpoctova-kazen-2025`. It carries `"evidence_type": "demand"` and
  `"_needs": []`, and every REQUIRED_OUT field is filled.
- A dry run against a SCRATCH COPY of `data/signals` (`$TMPDIR/demand-sim-0928/signals`,
  seen.txt 18,697 ids) printed:
  `normalize --complete --dry-run: would append 1 records across 1 file(s); 0 dropped by
  materiality; 0 incomplete; 0 refused by AC-GDPR1.` →
  `signals/demand/2026-09-28.jsonl: +1`; `dedup by identity key (append): 0 skipped`;
  `AC-GDPR1 allowlist: dropped 2 non-allowlisted field(s) across 1 record(s): _needs,
  evidence_type` (this is expected: both are routing-only fields).
  `git status --porcelain data/signals` was empty afterwards.
- The coordinator therefore owes this feed one `--complete` over
  `data/raw/2026-09-28/demand` and one `db.py upsert data/signals/demand/2026-09-28.jsonl`.

### Dropped-log duty (INGEST.md 3c) — opened first

`data/signals/dropped-log.jsonl` has 3,984 lines. The feeds in this remit account for
**89 `nku` lines and 0 `demand-scan` lines**. Sorted by `times_dropped`, **every one of the 89 is
at 1**, with first_seen = last_seen = 2026-09-19. So there is **no repeat offender** in this
remit this week. The lines break down as follows:
- ~60 are Věstník "Změna plánu kontrolní činnosti", Kolegium agendas, "Kontroly zahajované"
  and "Ukončení … (nepublikovaná)" notices. These are procedural cards, and none has a
  document behind it that says more than the card.
- 19 are old conclusion PDFs (`nku-k22032 … nku-k25020`) that the scripted feed back-filled.
  The corpus was checked for each: k25015/16/20 are cited inside
  `nku-majetkove-ucasti` / `nku-up-ucetni-zaverka-2025`, and the 2026-09-03 pass judged them
  against the pain bar. The other 16 (e.g. 22/32, 23/10, 23/14, 23/28, 24/03, 24/05, 24/10,
  24/11, 24/13, 24/15, 24/19–24/23, 24/33) are cited by no demand record. Their cards scored
  0/0/0 on metadata alone. **Owed, not done this pass:** a future monthly broad pass should
  read those 16 PDFs for the quantified failure. A weekly delta has no budget for 16
  conclusions, and SCANS.md item 1 is exactly the "read the PDF, not the card" duty.
- Press-release twins of records already held: `nku-15872` (→ `nku-zdravotnicky-vyzkum`),
  `nku-15897` (→ `nku-ikem-hospodareni`), and the accounting-audit releases 15787 / 15796 /
  15799 / 15809 / 15814 (→ `nku-dia-ucetnictvi`, `nku-up-ucetni-zaverka-2025` and others).
  Their documents are already held at their conclusion-PDF urls, so nothing was re-staged.

### Checklist source 1 — NKÚ kontrolní závěry (parse the PDFs)

**Visited. No new conclusion was published. Nothing minted.**

- RSS `https://nku.cz/cz/rss.xml`: **200**, 13,843 B (`pages/nku-rss.xml`), against 13,475 B
  on 09-21. There are two new items since 21 Sep:
  - **id15934, 25 Sep 2026**, *"Problémy s výběrem DPH řešili odborníci z evropských kontrolních
    institucí na konferenci v Praze"*. The item page answered **200** (24,779 B,
    `pages/nku-15934.html`; browser UA, after a 301 from http). It is a press release about the
    EU Contact Committee VAT network meeting of 23–24 Sep. It names no audit, gives no figure
    and reports no failure. **Not minted**: it fails the pain-language/quantified-failure bar,
    and cross-border e-commerce VAT is already held as `nku-dph-ecommerce` (k25001).
  - id15932, 24 Sep 2026, *"Nabídka nepotřebného majetku – AV technika"*: an asset-disposal
    notice. Not a signal.
  - Nothing else is new. The newest audit item is still id15918 (25/18, held as
    `nku-zemedelsky-vyzkum`).
- Conclusion-PDF existence probe `https://www.nku.cz/assets/kon-zavery/kNNNNN.pdf` (HEAD):
  - 200: k25018 only (Last-Modified unchanged, Mon 21 Sep 2026 04:26:37 GMT).
  - 404: k25019, k25022, k25023, **k25024**, k25025, k25026, k25027, k25028, k25029, k25030,
    k26001, k26002, k26003.
  - **k25024 variants also 404**: `K25024.pdf` on www.nku.cz, and both `K25024.pdf` and
    `k25024.pdf` on bare nku.cz.
- Věstník index `https://www.nku.cz/cz/publikace-a-dokumenty/vestnik/`: **200**, 41,328 B
  (`pages/nku-vestnik.html`). This is byte-identical in size to the 09-19 and 09-21 captures.
  The částky listed are 1/2026, 2/2026 and 3/2026. **There is no 4/2026.**
- Re-read for the MATCH follow-up (below): k24017.pdf (604,629 B), k25013.pdf (703,711 B) and
  k25018.pdf (657,286 B), all **200** and saved with `pdftotext -layout` output.

### Checklist source 2 — European Semester CZ package

**Visited. Nothing new.**

- `https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages-including-country-reports/country-report-czechia_en`:
  **200**, 74,808 B (`pages/ecsem-landing.html`), against 74,780 B earlier. The 28-byte delta
  is page chrome. The stripped text still shows the **3 June 2026** Country Report as the
  newest item, then 2025, 2024 and 2023, all unchanged. Both halves of the 2026 cycle are held
  (`ecsem-cz2026-*`, `ecsem-cz2026-csr`). **Nothing minted.**
- CELLAR SPARQL was not re-queried: the landing page has not moved, and 09-19 closed the CSR
  OJ reference. It stays owed to the next MONTHLY broad pass (carried from 09-21).

### Checklist source 3 — MPSV Statistická ročenka, chapter 5

**Visited. EXPECTED ABSENCE (not yet published). This is not a coverage gap.**

- `https://mpsv.gov.cz/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci-archiv`:
  **200**, 1,332,921 B (`pages/mpsv-rocenka-archiv.html`), against 1,325,956 B on 09-21. The
  size moved but the content did not:
  - The newest edition is still **"Statistická ročenka z oblasti práce a soc. věcí v roce
    2024"** (`.7z`, section dated 14. května 2026), followed by the 2023 `.zip`.
  - `v roce 2024` appears 4×, which is the positive control. `v roce 2025` appears 0×, and no
    2025 file link exists.
- Two guessed non-archive slugs (`/statisticka-rocenka-z-oblasti-prace-a-socialnich-veci`,
  `/statisticke-rocenky-…`) returned **404**. They are not real pages and their payloads were
  discarded.
- **Owed:** re-check next pass. When the 2025 edition lands, diff tab 5.9 against
  `civic-mpsv-rocenka-neuspokojene-2024` and file it under `civic-`.

### Checklist source 4 — Ombudsman ESO (HTML walk, no RSS)

**Visited. One new ESO item, not minted (single case, scale 0). The positive control passed.**

- `https://www.ochrance.cz/eso/zpravy/`: **200**, 14,674 B (`pages/ombud-eso-zpravy.html`).
  This is the taxonomy explainer.
- ESO app `https://eso.ochrance.cz/`: **200**, 83,474 B (`pages/eso-home.html`). It was walked
  with the session method: cookie jar → `POST /Vyhledavani/Search` →
  `POST /Nalezene/GetPocetVysledku --data ""` → `POST /Nalezene/GetTableContent`. Paging
  uses `page=N&rows=10&sidx=&sord=`, which is the site's own `fnNextPage()` params.
  - **Positive control** `FormaZjisteni=22`: **41 hits**, unchanged since 09-18.
  - `DatumVydaniOd=01.06.2026`: **45 hits**, against 44 on 09-21. All 5 pages were read
    (`pages/eso-table-since0601-p{1..5}.html`): 45 distinct item ids, which is the 09-21 set
    plus exactly **ESO 15088**.
  - `DatumVydaniOd=19.09.2026`: **2 hits**. These are the future-dated 6160/2025/VOP and
    4474/2025/VOP (items 14702, 14744), both already seen and both single cases.
  - Item-id frontier `/Nalezene/Edit/15083 … 15130`: only **15088** answered 200. All the
    others were non-200.
- **ESO 15088**: sp. zn. 115/2025/DO, Zpráva o šetření § 18, datum vydání 25.08.2026,
  children's ombudsman. It is one grandmother's foster-care allowance overpayment wrongly
  demanded back by ÚP Tišnov, and the office corrected it. Saved as `pages/eso-edit-15088.html`.
  **Not minted**: it is a single case (scale 0, money 0, urgency 0) and would be dropped by
  materiality. Prior passes did not mint single § 18 reports either.
- Aktuálně `https://www.ochrance.cz/aktualne/`: **200**, 47,734 B. There are two items newer
  than 15 Sep, and both were read:
  - 23 Sep 2026: the ombudsman publishes Kamil Fousek's *"Manifest o ústavní péči"*
    (`pages/ombud-ustav-neni-domov.html`). It says deinstitutionalisation "stále vázne" but
    gives no figure. The shape is already held as `ombud-deinstitucionalizace`. Not minted.
  - 22 Sep 2026: International Day of Sign Languages (`pages/ombud-znakovy-jazyk.html`). This is
    awareness content with no finding. Not minted.
- The Q3 2026 quarterly report is not due until after 30 Sep 2026. This is an expected
  absence, and `ombud-q2-2026` is still the newest.

### MATCH follow-up — recipient side of "research recipients lose grant money"

The pass looked for demand evidence that grant **recipients** pay odvody for breaching budget
discipline:
- **Found, with receipts, and staged:** the MF Central Harmonisation Unit's *Zpráva o
  výsledcích finančních kontrol ve veřejné správě za rok 2025*.
  - Payloads: `pages/mf-fk-2025.pdf`, 719,434 B, Last-Modified 2026-05-18; landing page
    `pages/mf-fk-2025.html`.
  - Corroborated by the Financial Administration's *Výroční zpráva 2025* ch. 5.3
    (`pages/fs-vz-2025.pdf`, 12,701,559 B, Last-Modified 2026-06-30).
  - Every figure below was checked as a literal substring of the pdftotext output:
    - 1,816 tax audits of subsidies over 8,090m CZK
    - 1,769 payment assessments, 639.1m CZK, **365.3m CZK of that being levies for breach of
      budget discipline**
    - FS: 977 levy assessments, 860 referrals, 22 criminal complaints
    - 193 waiver requests seeking 395.6m CZK, of which almost 118.0m CZK was waived
    - 98 appeals, 35 lawsuits + 14 cassation complaints
  - Recipient failures named, most frequent first: procurement run against Act 134/2016;
    distorted or false unit reporting under simplified-cost grants; missed deadlines,
    indicators and sustainability conditions; ineligible or duplicate costs.
  - Both documents predate the window (May/June 2026). They are staged because the
    coordinator's brief asked for exactly this evidence and the corpus did not hold it: no
    ledger record cites either url, and no `mf-`/`fs-` id exists.
- **Not found, stated honestly:** there is no research-specific recipient-side count beyond
  what the corpus already holds.
  - k25018 (25/18) is the only one of the three audits with a budget-discipline figure: 8 of
    14 projects breached the support contract, 4 with facts suggesting a budget-discipline
    breach, and 1,113 duplicate results (12.91 %) in IS VaVaI.
  - k24017 (24/17) and k25013 (25/13) were re-read in full. **Neither contains
    "rozpočtové kázně"**. 25/13 says outright that the audit found no breach of the rules in
    drawing the IPO support (line 836 of `pages/nku-k25013.txt`).
  - Web searches for TA ČR / GA ČR annual-report counts of referrals to finanční úřady and
    for NSS 2026 research-grant odvod judgments returned nothing usable.
  - The research-specific recipient case therefore rests on one audit plus the system-wide MF
    and FS figures. MATCH should weigh it as such.

### Records

| id | source doc | sector | scores (sc/mo/ur/re) | money |
|---|---|---|---|---|
| `civic-mf-odvody-rozpoctova-kazen-2025` | MF CHJ, Zpráva o výsledcích finančních kontrol za rok 2025, ch. 5, PDF of 2026-05-18 | legal-compliance | 3/3/3/3 | €14,910,204 (365.3m CZK @ 24.5) |

Scoring notes:
- **Scale 3**: every class of subsidy recipient is audited (89 state units, 366 municipalities,
  495 companies, 858 other bodies).
- **Money 3**: the levy alone is 365.3m CZK; the penále is excluded.
- **Urgency 3**: this is the "already in force AND actively enforced" branch. Act 218/2000
  § 44/44a is live, and 977 levy assessments were issued in 2025.
- **Recurrence 3**: statutory and continuous.
- **Sector**: `legal-compliance`, not `education` (the nku-gacr-tacr precedent). The record is
  about recipients' compliance with grant conditions across all programmes, not about
  research funding outcomes.
- **Prefix**: `civic-`, following `civic-mpsv-*` for a ministry's own report. No `mf-` prefix
  exists in the feed's id_prefixes.

**Quote**: 205 chars, verbatim from `pages/mf-fk-2025.txt` after `\s+` collapse, checked
mechanically.

### Dedup

- seen.txt (18,697 ids): `civic-mf-odvody-rozpoctova-kazen-2025` → 0 matches.
- Neither url (the MF PDF or the FS annual report) appears anywhere under `data/signals/`. The
  identity-key pass in the scratch dry run skipped 0.
- Near-misses were checked. No held signal is about the budget-discipline levy: the only
  demand hits for "rozpočtov" are `nku-zemedelsky-vyzkum` and `nku-ikem-hospodareni`, which
  are different documents. The regulation ledger holds budgetary-rules bills
  (`veklep-ALBSDQTF86PL`, `veklep-KORNDMPDBE54`), which are law changes, not demand.

### Candidates for MATCH

- **NEW-problem candidate, strengthened: "Czech grant recipients lose money to compliance they
  got wrong".** No problem in `data/problems/cz/` (p-0001 … p-0049) covers grant-recipient
  compliance. The grep for dotační / budget discipline found only incidental mentions, in
  p-0002 and p-0041.
  - Evidence set: `civic-mf-odvody-rozpoctova-kazen-2025` (this pass, system-wide: 365.3m CZK
    of levies a year, 977 assessments, 193 waiver requests, procurement and unit-reporting
    errors first), plus `nku-zemedelsky-vyzkum` (research-specific: 8 of 14 contract breaches,
    4 suspected budget-discipline breaches, 12.91 % IS VaVaI error), `nku-gacr-tacr` and
    `nku-zdravotnicky-vyzkum` (the provider-side outcome-blindness).
  - Recommendation to MATCH: frame the problem on the **recipient** side and across grants
    generally, with research as one segment rather than the whole. The system-wide receipts
    are much stronger than the research-only ones. The buyer pays to avoid an odvod: the
    193 waiver requests seeking 395.6m CZK are recipients already paying for the mistake.
  - Adjacent: `p-0031-municipal-pv-procurement` (towns running subsidised procurement), since
    procurement breaches are the #1 levy cause.
- Carried from 2026-09-21, still open for MATCH: `ombud-spravni-rad-praxe` (the authorities
  want an external methodology); the delegated-agenda burden in small municipalities
  (`ombud-male-obce-statni-sprava` with `reg-verejne-opatrovnictvi-prenos-2027`, near
  `p-0038-village-public-guardianship`); healthcare complaint handling
  (`ombud-stiznosti-zdravotnictvi`).

### Coverage gaps

- **Carried, still open: NKÚ 25/24 (revitalisation of public spaces).** k25024.pdf is 404 for
  the **fourth** consecutive pass, including the upper-case and bare-domain variants. It was
  approved by the 13th Kolegium on 7 Sep 2026. Owed: a re-probe next pass. If it is still
  missing at the monthly pass, read the Kolegium id15884 page and the Věstník for a publication
  note instead of probing blind.
- **Carried: Věstník 4/2026** has not appeared (index unchanged). It is owed when it lands and
  should list 25/18.
- **New, owed to the next monthly broad pass:** 16 old NKÚ conclusion PDFs sit in the dropped
  log at 0/0/0 and are cited by no record (list above). Their documents have not been read.
- **Expected absences, not gaps:** MPSV ročenka 2025 is not published (positive control
  passed). The ombudsman Q3 2026 report is not due until after 30 Sep. The Semester cycle is
  complete for 2026.
- **Deliberate non-visit:** CELLAR SPARQL. It is owed to the monthly pass (carried).
- **For the coordinator, outside this remit:**
  - The scripted `nku` feed has still not landed its headline twins: `nku-15872`, `nku-15897`
    and id15918 are not in seen.txt (15872 and 15897 sit in the dropped log at scale 0–1).
  - id15934 (the VAT conference) will arrive through that feed and should drop.

### Pass summary

```
feed:                     demand-scan (weekly delta, evidence_type demand, 7 days after the 2026-09-21 pass)
checklist sources:        4 of 4 visited (NKU / European Semester / MPSV rocenka / ombudsman ESO); ESO control 41 passed, MPSV control (2024 edition) passed
records staged:           1  (civic-mf-odvody-rozpoctova-kazen-2025; scratch dry run: +1, 0 dropped, 0 incomplete, 0 refusals, 0 identity-key skips)
coverage gaps named:      2 carried (NKU 25/24 k25024.pdf 404 x4; Vestnik 4/2026) · 1 new owed (16 unread NKU PDFs in dropped log) · 3 expected absences · 1 deliberate non-visit (CELLAR)
rotation state:           n/a — category rotation is arb-scan's duty
```


## reg-scan pass — 2026-09-28 (weekly delta)

Weekly delta pass of `reg-scan` (feed row: `evidence_type` regulation, `source` reg-scan,
`id_prefixes` ["reg"], runner attended). Operating file: `pipeline/SCANS.md` reg-scan
checklist items 1–4 under THE CHECKLIST LAW; evidence bar `pipeline/SWEEP.md` step 4. Window:
enacted or published since the 2026-09-21 passes, plus the carried debts both 2026-09-21
reg-scan sections named.

Run alongside the scripted ingest on the same raw date. This pass wrote ONLY
`data/raw/2026-09-28/regulation/` (`staged.jsonl`, `manifest-section.md`, `pages/`). It READ
the top-level `veklep-p1..p6.json` payload read-only, to get attachment lists without
re-fetching what the script fetched (the same method the 2026-09-21 RIA follow-up used). It did
not touch any other top-level file. **Nothing was written to `data/signals/**`, `seen.txt`,
`register.db`, `data/problems/**`, `feeds.json` or the shared `manifest.md`.** No `db.py` call,
no real `--complete`, no git operation.

**Records staged: 6**, all `reg-` prefixed, `source: reg-scan`, `evidence_type: regulation`,
`extraction: manual`, none in `seen.txt`. Each quote is ≤300 chars and was checked in a script
as a literal substring of the whitespace-collapsed saved page.

| id | instrument | status | date | payload |
|---|---|---|---|---|
| `reg-pohonne-hmoty-strop-2026-10` | NV 172/2026 Sb., fuel price cap for Oct 2026 | **ENACTED** (in force 1 Oct 2026, expires 31 Oct) | 2026-10-01 | `esbirka/sb-2026-172.txt`, `veklep/zd_KORNDY6KW2UP.txt` |
| `reg-min-mzda-2027-171-2026` | MPSV notice 171/2026 Sb., 2027 minimum wage 24,900 CZK | **ENACTED** | 2027-01-01 | `esbirka/sb-2026-171.txt` |
| `reg-aifmd2-130-2026` | Act 130/2026 Sb., AIFMD II transposition | **ENACTED** (in force 1 Sep 2026; phase 16 Apr 2027) | 2027-03-01 | `esbirka/sb-2026-130-excerpt.txt` |
| `reg-ehds-identifikace-myhealth-2027` | Impl. Reg. (EU) 2026/2099, MyHealth@EU identification | **ENACTED** (OJ L 22 Sep 2026) | 2027-03-26 | `eu/32026R2099-en.txt` |
| `reg-omnibus-i-2026-470` | Directive (EU) 2026/470 (Omnibus I: CSRD/CSDDD) | **ENACTED** (OJ L 26 Feb 2026) | 2027-03-19 | `eu/32026L0470-en.txt` |
| `reg-uvery-osvc-ochrana-2028` | MF bill on business loans to sole traders (VeKLEP KORNDY9BQZVI) | **DRAFT** | 2028-01-01 | `veklep/ria_KORNDY9BQZVI.txt` |

### Access notes (measured today)

- **vlada.gov.cz**: both checklist pages return HTTP 200 with the descriptive UA. The RSS feed
  (`/cs/urad/RSS/rss.xml`) returns HTTP 200 but now carries only **2 items**, dated 24 and 25 Sep.
  `/cz/ppov/lrv/dokumenty/` returns 200 with an empty document list (it is rendered by JS). The
  site search URL `/cz/vyhledavani/?searchtext=` returns **404**.
- **ODok**: the redirect from odok.cz to odok.gov.cz still holds. **Four "Empty reply from
  server" / truncated-transfer failures** happened today, on 2 of 15 attachments and 2 of 7
  agenda pages. Each succeeded on an identical retry. This is the same intermittency class
  recorded on 2026-09-19 and 2026-09-21.
- **e-Sbírka ELI open data** worked on every probe. **New today: the e-Sbírka `sbr-cache` JSON
  API** (`https://e-sbirka.gov.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2026%2F<n>%2F0000-00-00`)
  returns the title and dates of an act **whose text is not yet digitised**. That is how 166/2026
  was identified below. It returns HTTP 400 for numbers not yet promulgated (173, 174). The
  `www.e-sbirka.cz` host of the same path timed out.
- **EUR-Lex**: not fetched directly. The CELLAR SPARQL endpoint and CELEX content negotiation
  (`http://publications.europa.eu/resource/celex/<CELEX>`) both returned HTTP 200. Neither
  needed the headless browser.
- **psp.cz**: served as windows-1250 and decoded with iconv before reading.
- 28 Sep 2026 is a public holiday (St Wenceslas), so no cabinet sitting took place today.

---

### Checklist source 1: Programové prohlášení vlády + semi-annual fulfilment evaluations

**Visited. Nothing new.**
`https://vlada.gov.cz/cz/vlada/programove-prohlaseni/programove-prohlaseni-vlady-224629/` returns
**HTTP 200, 181,238 bytes**, byte-length identical to 2026-09-21. It still has one attachment
(`programove-prohlaseni-vlady.pdf`, page dated 5. 1. 2026) and **no fulfilment evaluation**.

Cabinet business since 2026-09-21, read through ODok `zvlady/jednani-detail/<date>` for
22–30 Sep (`pages/vlada/odok-jednani-*.html`). The only sitting with content is **25 Sep 2026**,
which had one item: 732/26, the update of the Italy–Czechia action plan, resolution 619/2026. The
other dates return the 33,376-byte empty template. The RSS carries two items: EU committee
resolution no. 12, and the PM laying the foundation stone of the Karlovy Vary integrated rescue
centre. **No record from source 1.** Carried gap unchanged: no machine-readable fulfilment
evaluation. The next one is expected around January 2027.

### Checklist source 2: Plán legislativních prací vlády (2026; is 2027 published?)

**Visited. Unchanged. The 2027 plan is NOT published.**
`https://vlada.gov.cz/cz/ppov/lrv/dokumenty/plan-legislativnich-praci-vlady-na-rok-2026-226017/`
returns **HTTP 200, 43,059 bytes**. The page carries the same two annexes
(`1234_2026_priloha_c-_1.pdf`, `_2.pdf`), dated 20. 3. / 23. 3. 2026. It is 11 bytes shorter than
on 2026-09-21, and the attachment and date diff shows no content change.

For the 2027 plan: none of this week's **143 VeKLEP materials** is titled "Plán legislativních
prací" (grep of the payload titles). No cabinet agenda since 21 Sep carries it. The LRV documents
index renders empty without JS. This is an **expected absence**: the annual plan is usually
approved around the turn of the year. **No record from source 2.**

### Checklist source 3: e-Sbírka and EUR-Lex (enacted since 2026-09-21)

**e-Sbírka: visited.** Probed ELI 2026/166 through 2026/190 (`pages/esbirka/eli-2026-*.ttl`).
**Five new acts, 168–172, now have text.** 173–190 all return the 768-byte empty stub.

| Sb. | what it is (from its own prefix fragments) | in force | outcome |
|---|---|---|---|
| 166/2026 | **CARRIED DEBT CLEARED (title):** "Zákon, kterým se mění zákon č. 375/2022 Sb., o zdravotnických prostředcích a diagnostických zdravotnických prostředcích in vitro" (sbr-cache JSON) | 16 Sep 2026 | The text is still "právě digitalizujeme", so its subject beyond the title is unknown. **Not recorded** (a title is not a duty). The gap narrows to "content" |
| 168/2026 | MD decree amending 522/2006 Sb.: new Annex 4 ADR risk categories for roadside checks | 23 Sep 2026 | Not recorded. It re-grades enforcement and adds no new duty. Card `veklep-KORNDU4FMHER` already in corpus |
| 169/2026 | MPSV notice: normative rent for the state social-assistance benefit, 1 Oct–31 Dec 2026 | 1 Oct 2026 | Not recorded. It is a benefit parameter for the Labour Office, not a business duty |
| 170/2026 | MŠMT decree amending 72/2005 Sb. on school counselling services | 1 Jan 2027 | Not recorded this pass. Card `veklep-KORNDS3SSYSD` already in corpus. Full text saved (`sb-2026-170.txt`, 47 kB) for a later read |
| 171/2026 | MPSV notice: **2027 minimum wage 24,900 CZK/month, 148.30 CZK/h**, guaranteed-pay table, hardship allowance 1,245–3,735 CZK | 1 Jan 2027 | **RECORDED: `reg-min-mzda-2027-171-2026`** |
| 172/2026 | NV: **fuel price cap 1–31 Oct 2026** (formula + 2.50 CZK/l margin + 21 % VAT) | 1 Oct 2026 | **RECORDED: `reg-pohonne-hmoty-strop-2026-10`** |

Carried e-Sbírka and psp.cz debts:
- **EET 2.0 Sbírka number: NOT CLEARED, re-measured.** `psp.cz historie t=189` (HTTP 200,
  49,770 bytes, "Stav projednávání ke dni: 28. září 2026", `pages/psp/psp-tisk189.html`) still
  ends at "Prezident zákon podepsal 17. 9. 2026" with no promulgation line. The newest Sbírka
  number is 172/2026, and 173+ are empty stubs. That makes 11 days since signature.
  `reg-eet2-2027` and `reg-mf-eet2-2027` still owe their number and in-force date.
- **Act 130/2026: CARRIED DEBT CLEARED.** The transitional provisions (Čl. II) and effect clause
  (Čl. VIII) were re-fetched from ELI and read. **RECORDED: `reg-aifmd2-130-2026`.**
- **166/2026 empty fragments:** narrowed to "title known, text undigitised" (above).
- **Sněmovní tisk 48 (plant-protection act, carrier for the Impl. Reg. 2023/564 spray-record
  duty): NOT CLEARED.** `historie t=48` (HTTP 200, 37,983 bytes, state as of 28 Sep 2026) is
  unchanged. It is still returned to the general debate of the second reading, and no vote has
  been held since. Related: the pesticide-equipment decree draft `veklep-KORNDXYA34EY` (read
  today) says outright that it implements a new power from tisk 48, so it cannot be issued
  until that bill passes.
- **2027 motorway-vignette rates: NOT CLEARED.** No Sbírka act 168–172 and no VeKLEP material
  this week sets them. The sections decree (`veklep-KORNDY2BWJMB`) is the only 2027 vignette
  instrument in view.

**EUR-Lex: visited via CELLAR.** Every `32026[RLD]` act with an OJ publication date of
**2026-09-22 .. 2026-09-28** was enumerated. **41 CELEX** are listed in
`pages/eu/ojL-pub-2026-09-22_28.rq` and `.csv`. No OJ items were dated 26–28 Sep. **No directive
(`32026L…`) was published in the window.**
- **RECORDED: `reg-ehds-identifikace-myhealth-2027`** (32026R2099). It puts identification and
  authentication duties on healthcare providers and professionals using MyHealth@EU, from
  26 Mar 2027.
- **Read, not recorded:** **32026R1753** (Euro 7 / Euro VI entries added to Annex II of
  2018/858). The type-approval list is amended and in force the day after publication, but the
  duties sit in Reg. 2024/1257 and the UN regulations it cites, so this act is a reference update
  for manufacturers. **32026R2111** (ATCO licensing). It corrects an application date for tasks
  of national aviation authorities, so it creates no market duty.
- **Not recorded, by class:** CFSP and sanctions acts (2161, 2160, 2136, 2137, 2138, 2147, 2156,
  2157, 2159, 2164, 2165); trade defence (2107 GFR countervailing duty, 2101 pea protein
  anti-dumping, 2118 Pekin duck registration); animal-disease emergency measures in Greece (2123,
  2148); feed-additive authorisations (2110, 2113, 2115, 2120, 2129); GMO authorisations (2112,
  2117, 2121); biocide approval-expiry postponements (2119, 2124, 2131) and one Union biocidal
  authorisation (2116); third-country animal-entry lists (2149); a Lithuanian LNG State-aid
  decision (2114); Council agreement signatures and positions (2126, 2144, 2145); management-board
  appointments (05009, 05011–05013); and an expert-group decision (04900).
- **Directive (EU) 2026/470: CARRIED DEBT CLEARED.** It was published before the window, but the
  2026-09-21 pass named it as gap 8. Read in full. **RECORDED: `reg-omnibus-i-2026-470`.**

### Checklist source 4: VeKLEP RIA "Definice problému", ledger items AND dropped-log repeat offenders

**Sequencing state:** `data/raw/2026-09-28/staged.jsonl` **did not exist** at any check this
pass (the last check was just before this section was written). The scripted `veklep` fetch
completed at 04:44:12Z: `ok=1`, HTTP 200, 1,760,317 bytes, **143 items**
(`.fetch/receipts.jsonl`). Rather than wait, this pass took the same id set normalize will
stage: every payload `Id` whose `veklep-<Id>` is not in `seen.txt`. There are **11**. It then read
their documents.

**THE TWO COUNTS SCANS.md item 4 REQUIRES:**
- **RIA sections read from the ledger: 7 materials (8 documents).**
- **RIA sections read from the dropped log: 11 of 11 veklep lines opened. 2 documents newly
  read**, the other 9 having been read in full on 2026-09-21 with their attachments unchanged.
  **0 re-staged by hand.**

Plus **3 genuinely new materials this week** (not yet in either ledger or log, because staging
has not run). All 3 were read, and 2 produced records.

**(a) Ledger half.** `data/signals/regulation/2026-09-21.jsonl` holds **0 veklep lines**. The
2026-09-21 scripted run appended none. That leaves nothing new in the ledger since the last pass.
**Seven veklep ledger lines in `2026-09-19.jsonl` had never had their documents read**, because
the 09-19 scripted ingest appended them after that day's reg-scan pass. No manifest mentions six
of them, and `KORNDXY8B5OY` is mentioned only as a duplicate card. All seven were read today.
Attachment lists came from `data/raw/2026-09-19/veklep-p*.json` in the main checkout, read-only.

| veklep id | material | what the DZ / RIA states | outcome |
|---|---|---|---|
| `KORNDXYKKS1I` | security-forces medical fitness, vyhl. 226/2019 | restores the milder classification for purely laboratory glucose-regulation findings (removed 1 Jan 2025), mainly at HZS's request, plus 16 classification changes. No count of people affected; in force 1 Jan 2027 | No record. Nothing quantified |
| `KORNDXYA34EY` | professional pesticide application equipment, vyhl. 207/2012 | photo-documentation at control testing (new power from **tisk 48**), updated EN standards, drones and non-spray kit | No record. Blocked on tisk 48 |
| `KORNDXYAVAYV` | truck and bus licence oral-exam questions, vyhl. 167/2002 | 45 → 40 questions, 8 new ones on driver-assistance systems, alternative drives and AdBlue, partly for Directive (EU) 2025/2205; one-off material costs for driving schools | No record |
| `KORNDXTH7F1K` | verification offices list, vyhl. 36/2006 | adds 11 municipal offices, removes 2. Start-up costs ≈ 8,600 CZK per office (up to +35,000 IT, +30,000 furniture); fee income 2,000–15,000 CZK a year | No record. One-body administrative list |
| `ALBSDXWJ7VQX` | tourism act 159/1999 (eTurista, STR Reg. 2024/1028) | RIA "Definice problému" read in full: duplicate reporting by accommodation providers; in the Berounsko VŠE study, 105 of 187 establishments (56.1 %) were absent from ČSÚ's register; 10,012 HUZ with 562,467 beds (2025); ~8m platform nights (2024); ORP cost 44,709,620 CZK; effective 1 Jan 2028 | No new record. Already held as **`reg-eturista-registr-ubytovani-2028`** (same RIA URL) and matched to **p-0040** |
| `KORNDXWQDTHG` | 2026 travel-allowance rates, vyhl. 573/2025 | August 2026 petrol price 41.80 CZK/l, **+20.46 %** over the decree value, which triggers an extraordinary revision from 1 Oct 2026. RIA waived as parametric | No record. The price rise is cited inside `reg-pohonne-hmoty-strop-2026-10` |
| `KORNDXY8B5OY` | startup act (second card), RIA | "Definice problému": 972 VC-backed startups since 2015 (89.2 per million; Estonia 681), VC 25 USD per capita | No new record. Already held as **`reg-startup-evidence-odpocet-2027`** |

**The rest of the ledger half is a standing gap, not a clean bill.** 13 veklep materials already
in `seen.txt` changed state in the payload since 2026-09-19. These are
KORNDXBH65S3 (water act), KORNDVEC8EF8 (addictive substances), KORNDXQH9BRI,
KORNDXCGU8JB (top-up taxes), KORNDVTBZKV2, ALBSDW3HDEWG, KORNDXWQDTHG, KORNDVYGNA4F,
ALBSDXRFYLM6, KORNDTUBDJRM (critical-infrastructure portal), KORNDXAMWBJD, KORNDX6AEXUS and
KORNDWVGVS5J. Several come from the **198-line 2026-08-25 backfill**, whose RIAs no pass has read.
Named below as a coverage gap.

**(b) Dropped-log half.** `data/signals/dropped-log.jsonl` has **11 veklep lines** (3,984 lines
in total). Sorted by `times_dropped`, all 11 tie at **1**, with `last_seen 2026-09-19`. Each was
checked against today's payload:
- **7 re-stage today**, being in the payload and not in `seen.txt`: KORNDV4EB4WE, KORNDY2HHS8D,
  KORNDUAFXG1S, KORNDUEGPUWG, KORNDNSF3ZQ5, KORNDW7HRLI7 and KORNDSAKSLEQ. All 7 were read in full
  on 2026-09-21. Two recorded problems came from them: `reg-veznice-ubytovaci-plocha-2030`
  (KORNDW7HRLI7) and `reg-pozemkove-upravy-vykupy-2027` (KORNDUAFXG1S). **New attachments since
  09-21:** KORNDY2HHS8D has a final DZ (`zd_KORNDY7BM2FW`, 23 Sep). It was **read today and is
  unchanged**: the pension supplement rises 0.2 % from January 2027, parametric. KORNDV4EB4WE has
  only a signed PDF material, with no new DZ. The other five have no attachments dated after
  09-20.
- **4 have aged out of the feed**, being absent from today's 143: KORNDVKKWEK9, KORNDV7FMSPN,
  KORNDV37RXI3 and KORNDXRHWVVT. All were read on 2026-09-21, and none states a quantified
  problem.
- **KORNDVACDSIC** (firearms medical fitness, *skartováno*) is not in the dropped log, although
  the 2026-09-19 manifest records it as dropped. It **re-appears in today's payload** as an
  unseen id. **CARRIED DEBT CLEARED: its DZ was opened today for the first time**
  (`zd_KORNDVACDSIC.docx`, from the material page `pages/veklep/material-KORNDVACDSIC.html`). It
  drops the duty to certify having viewed the new **emergency health record** (§ 34a Act
  325/2021) in firearms medical reports. The stated reason is low practical value against the
  time and access costs, and the "complications with launching and using this institution". The
  DZ gives no numbers. It is a qualitative signal of eHealth usability trouble, with no record.
- **Re-staged by hand: 0.** No dropped document says more than its card beyond what 2026-09-21
  already turned into records.
- **Observation for the coordinator:** 9 of these 11 ids re-staged on 2026-09-21 (per that day's
  RIA follow-up). Yet every line still reads `times_dropped 1 / last_seen 2026-09-19`. The log
  was committed in 124b2e3 (21 Sep, 21:01), after the 09-21 scripted ingest commit 3b9dd29
  (11:29). The likely explanation is that the log was built after the 09-21 run and never folded
  that run's drops. Either way,
  `times_dropped` currently undercounts those repeat offenders by one.

**(c) New this week (the 3 non-re-stager unseen ids):**

| veklep id | material | what the DZ / RIA states | outcome |
|---|---|---|---|
| `KORNDY9BQZVI` | MF bill: business loans to sole traders + notarial code (RIA) | "Definice problému": regulatory arbitrage between the consumer-credit act and civil-code loans exposes OSVČ to predatory lending, including acceleration after 3 days, notarial deeds with consent to enforcement, and fake "IČO" loans. Worked case: 300,000 CZK paid out → 1,402,800 CZK enforced within 75 days. 1,996,027 natural-person entrepreneurs; **~60bn CZK outstanding** (ČNB ARAD, 7/2026). Effective 1/2028 | **RECORDED: `reg-uvery-osvc-ochrana-2028`** |
| `KORNDY5KT835` | NV fuel price cap Oct 2026 (two DZ versions, byte-identical text) | extraordinary market situation after the 10 and 18 Sep Saudi supply shocks; retail tracks Brent at one week (r > 0.91); Q1 daily reporting failed | Enacted as **172/2026 Sb.**, **RECORDED: `reg-pohonne-hmoty-strop-2026-10`** |
| `ALBSDY9ERHUU` | deputies' bill: merge the Czech Breeding Inspection (ČPI) into SVS, and SVS becomes founder of the 3 state veterinary institutes | administrative reorganisation, effective 1 Jan 2027. SVS administers 298 EU base acts (1,082 with amendments). No external problem is quantified | No record |

All 15 documents downloaded this pass are saved in `pages/veklep/` as `.docx`/`.pdf`, with `.txt`
extractions (docx via an inline zip reader, pdf via `pdftotext -layout`).

---

### Evidence-bar compliance

- **Enacted vs draft:** `notes` opens with `STATUS:` on every record. 5 are ENACTED, each with
  its Sbírka or OJ date and in-force date. 1 is DRAFT (`reg-uvery-osvc-ochrana-2028`), and its
  notes say nothing in it is in force.
- **Dates:** each `date` is the day the duty bites: 2026-10-01, 2027-01-01, 2027-03-01 (6 months
  after 1 Sep 2026 under Čl. II(1) and (10) of 130/2026), 2027-03-26, 2027-03-19 (transposition)
  and 2028-01-01 (proposed effect). Secondary dates are quoted in `notes`.
- **Urgency:** 3 on the five enacted records, since each bites within 6 months of 2026-09-28.
  The 26 Mar 2027 EHDS date is 179 days out, and 172/2026 is in force in 3 days. 2 on the draft
  (Jan 2028 is about 15 months out). None relies on the "in force and enforced" branch alone.
- **Money:** `money_eur` is null on all 6, each with a `money_note`. The 60bn CZK loan book and
  the ORP and IT budgets are market or budget context, not money attached to the need. Nothing
  was estimated.
- **Quotes:** 6 of 6 verified mechanically as literal substrings of the whitespace-collapsed
  saved page. Lengths are 142, 124, 277, 247, 151 and 157. One first draft of the EHDS quote
  failed the check ("the" vs "that") and was replaced by the exact text, which is why the check
  exists.
- **Absence claims:** every "not in the corpus" names its search terms (listed in each record's
  DEDUP clause).
- **Personal data:** a regex check of `staged.jsonl` for e-mail and phone patterns returns 0
  matches. No natural person is named except ministers' signatures, which were not copied into
  any record.

### Dry run (validation only, nothing written to the ledgers)

```
cp -R data/signals $TMPDIR/reg-sim-0928/
python3 scripts/normalize.py --raw data/raw/2026-09-28/regulation --complete --dry-run --today 2026-09-28 \
    --out-dir $TMPDIR/reg-sim-0928/signals --seen $TMPDIR/reg-sim-0928/signals/seen.txt \
    --dropped-log $TMPDIR/reg-sim-0928/signals/dropped-log.jsonl
  -> normalize --complete --dry-run: would append 6 records across 1 file(s); 0 dropped by
     materiality; 0 incomplete; 0 refused by AC-GDPR1.
     $TMPDIR/reg-sim-0928/signals/regulation/2026-09-28.jsonl: +6
     dedup by identity key (append): 0 skipped
     AC-GDPR1 allowlist: dropped 6 non-allowlisted field(s) across 6 record(s): evidence_type
```

**Owed to the coordinator:** the real
`python3 scripts/normalize.py --raw data/raw/2026-09-28/regulation --complete` and the `db.py
upsert` line it prints. Nothing was committed.

### Facts in existing records this pass found stale (for MATCH/PROCESS; nothing was edited)

- **`reg-csrd-post-omnibus`** still reads "Final Omnibus I text pending formal adoption — treat
  scope/dates as agreed but not yet in OJ". Directive (EU) 2026/470 has been in the OJ since
  26 Feb 2026. It is now recorded as `reg-omnibus-i-2026-470`, with transposition due
  19 Mar 2027.
- **`reg-min-mzda-2027-164-2026`** gives the 2027 minimum as "24,809.64 CZK before the labour
  code's rounding". The published figure is **24,900 CZK / 148.30 CZK/h** (171/2026 Sb.).
- **`reg-eet2-2027` / `reg-mf-eet2-2027`**: still no Sbírka number (unchanged, re-measured).
- **`reg-ehds`** says "implementing acts due Mar 2027". A third implementing act (2026/2099) is
  now out, after 2026/2083 and 2026/2098.
- **`veklep-KORNDXWQDTHG`** card says "2026 travel allowance rates". The underlying trigger is a
  20.46 % petrol price rise and an extraordinary mid-year revision from 1 Oct 2026. The card is
  not wrong, but it hides the fact.

### MATCH candidates

| record | matches | why |
|---|---|---|
| `reg-ehds-identifikace-myhealth-2027` | **p-0022** (hospital eHealth interoperability) | same EHDS obligation chain (p-0022 already cites `reg-ehds`); adds provider-side identification duties and the 2027 date |
| `reg-omnibus-i-2026-470` | **no live problem**. Evidence for the value-chain-supplier candidate raised on 2026-09-21 (with `reg-esrs-value-chain-cap-2027`) | defines the "protected undertakings" (≤1,000 staff) and self-declaration that a supplier-side tool is built against |
| `reg-min-mzda-2027-171-2026` | **p-0018** (pay transparency / pay setting), secondary **p-0033** (care-workforce wages) | January pay-band reset for every employer; guaranteed-pay table for public employers |
| `reg-uvery-osvc-ochrana-2028` | **NEW-PROBLEM CANDIDATE**, adjacent to **p-0027** (consumer-credit dispute flood) | Sole-trader borrowers fall outside the consumer-credit act. The RIA documents 3-day acceleration and notarial enforcement, with a worked case of 300k CZK → 1.4m CZK enforced in 75 days, a ~60bn CZK loan book and up to 2m natural-person entrepreneurs. Builders' angle: contract-review / "is this really a consumer loan" triage for OSVČ and debt advisers, or lender-side compliance once the rules land in 2028. The corpus has nothing on it (searched: úvěry pro podnikatele, nespotřebitel, predátor, na IČO, notářský zápis) |
| `reg-pohonne-hmoty-strop-2026-10` | **no live problem**. Weak new candidate: daily max-price computation and compliance evidence for independent filling stations under a recurring cap (4 caps in 2026) | Formula inputs are public (MF Cenový věstník daily). Duty on every public station, enforced by SFÚ. Recurrence is the open question: the cap is monthly and ad hoc |
| `reg-aifmd2-130-2026` | **no live problem** | niche (Czech fund managers and FKI); liquidity-management tooling by 16 Apr 2027. Record only |

### Coverage gaps named

1. **No machine-readable fulfilment evaluation of the programme** (carried, recheck about Jan 2027).
2. **The 2027 Plán legislativních prací is not published** (expected absence; carried). The LRV
   document index renders empty without JS, so a future pass should check the cabinet agendas
   from December.
3. **EET 2.0 still has no Sbírka number** (carried, re-measured today: 11 days after signature,
   173+ empty).
4. **166/2026 Sb. is identified by title but its text is still undigitised** (narrowed from
   "unknown"). A future pass owes the content of this amendment to Act 375/2022 on medical
   devices. Its sněmovní tisk was not looked up this pass.
5. **Sněmovní tisk 48 is stalled** (carried). It now blocks two instruments: the 2023/564 spray
   records and the pesticide-equipment decree `veklep-KORNDXYA34EY`.
6. **The 2027 motorway-vignette rates are unrecorded** (carried). No instrument has appeared.
7. **`data/raw/2026-09-28/staged.jsonl` did not exist during this pass** (sequencing). The 11
   unseen veklep ids were derived from the payload instead. If normalize mints any id other than
   `veklep-<Id>`, or stages anything beyond those 11, the difference is unread.
8. **Backfill RIAs never read (standing).** The 198 veklep lines in
   `data/signals/regulation/2026-08-25.jsonl` have never had a RIA pass. 13 seen materials changed
   state since 09-19 without their documents being re-read. A SWEEP-sized job, not a weekly delta.
9. **170/2026 Sb. (school counselling decree, 1 Jan 2027)** was saved in full but not read for a
   record.
10. **The `times_dropped` undercount** described under source 4(b). This is a data-quality note
    on `dropped-log.jsonl`, not a source failure.

### 5-line pass summary

```
feed:                reg-scan (evidence_type regulation, prefix reg-, weekly delta pass 2026-09-28)
checklist sources:   4 of 4 visited (programme: HTTP 200, unchanged, no evaluation · plan 2026 unchanged, 2027 not published · e-Sbírka 166-190 (168-172 new, 166 titled via sbr-cache) + EUR-Lex CELLAR 09-22..28, 41 CELEX · VeKLEP: RIA read ledger 7 materials / dropped-log 11 of 11 lines, 2 new docs, 0 re-staged + 3 new materials read)
records staged:      6 (5 ENACTED: 172/2026 fuel cap, 171/2026 minimum wage, 130/2026 AIFMD II, EU 2026/2099 EHDS identification, Dir. 2026/470 Omnibus I; 1 DRAFT: OSVČ business-loan protection), dry-run +6, 0 dropped, 0 refused
coverage gaps named: 10 (4 carried unchanged, 2 carried and narrowed, 4 new); carried debts cleared: Act 130/2026, Dir. 2026/470, KORNDVACDSIC, 166/2026 title
rotation state:      n/a (arb-scan duty)
```


## dotace-scan pass — 2026-09-28 (weekly delta)

Weekly delta for the `dotace-scan` feed (`data/feeds.json` key `dotace-scan`, `signal_source: dotace`,
`evidence_type: tenders`, `id_prefixes: ["dotace"]`), run under `pipeline/SCANS.md` (THE CHECKLIST LAW).
Worktree: `localproblems-weekly-2026-09-28`. Left-hand side: the 2026-09-21 pass.

Raw captures: `data/raw/2026-09-28/dotace/pages/` (MS2021+ XML snapshot, today's sorted call-id list, the
per-call field diff, two ČNB lists, 2 OPD call-text PDFs + text, 2 OPJAK schedule PDFs + text, 20 portal pages).
Staged: `data/raw/2026-09-28/dotace/staged.jsonl` — **zero lines**.
This pass wrote nothing else: no ledgers, `seen.txt`, `register.db`, `feeds.json`, `errata.jsonl` or shared
`manifest.md`; no `--complete` without `--dry-run`, no `db.py`, no git state change.

### Exchange rate

**24.350 CZK/EUR**, ČNB list **#186 of 25.09.2026**. Requests for `date=25.09.2026` and `date=28.09.2026`
(fetched 2026-09-28 ~04:45Z, before today's 14:30 fixing) both returned HTTP 200 and the same payload, first line
`25.09.2026 #186`, containing `EMU|euro|1|EUR|24,350`. Saved as `pages/cnb-denni_kurz-25.09.2026.txt`,
`pages/cnb-denni_kurz-28.09.2026.txt`. No record this pass needed a conversion.

### Checklist source 1: MS2021+ open-data call list

- **Fetch.** `https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml` → **HTTP 200, 1,676,671 bytes**, fetched
  2026-09-28T04:42:45Z (sandbox proxy denied the host first; re-run with the host allowed). Payload
  `DATE="2026-09-27T20:45:00.000+02:00"` (Sunday night's export). Saved as `pages/ms21-SeznamVyzev_21_27.xml`,
  sha256 `d43f51025d4e44c970583c86682261996ba9e8a0d26b27e27739d8989e436200`.
- **Left-hand side, code level.** The 817-code list printed in the 2026-09-21 manifest section. Re-extracted from
  that manifest and verified: 817 codes, sha256 of the newline-terminated sorted list =
  `ac83c80814d4f9414369f044e0f939fc1c672c01981bb71f6f4bef41206e13aa`, **exactly the hash 2026-09-21 recorded**.
  So the manifest-as-left-side mechanism worked as designed.
- **Left-hand side, field level.** The 2026-09-21 XML payload is gone (it lived in a removed worktree). The
  2026-09-19 XML survives at `localproblems/data/raw/2026-09-19/dotace/ms21-SeznamVyzev_21_27.xml` (main
  checkout), and the 2026-09-21 section documents the full 09-19→09-21 field delta as exactly one change
  (`06_22_070` Pozastavená → Otevřená). So the per-call field diff was run **09-19 → 09-28** and that one known
  change subtracted; everything else below happened between 09-21 and 09-28. Output:
  `pages/ms21-diff-2026-09-19-vs-28.txt` (namespace-aware, every leaf field of every `<VYZVA>`, keyed by `KOD`).

**Code diff: 817 → 819. +2 / −0.**

| Added KOD | Call | State | Window | Allocation | Outcome |
|---|---|---|---|---|---|
| `02_27_049` | OP JAK — *Desegregace* (zřizovatelé segregovaných škol, PO OSS MŠMT) | Plánovaná | 2027-02-22 → 2027-08-31 | 150,000,000 CZK | not minted: planned |
| `02_27_050` | OP JAK — *PRO-ROMA II* (Romani and pro-Romani NGOs) | Plánovaná | 2027-02-28 → 2027-08-31 | 50,000,000 CZK | not minted: planned |

Both come from the new **OP JAK schedule 2027 v1** (approved 18 Sep 2026; `pages/opjak-harmonogram-2027_v1.pdf`
and `.txt`). Planned calls are not minted, which is how every earlier pass treated `02_25_044/045` and
`02_26_046`. They are carried as gap 4.

**Newly OPENED calls (state → Otevřená): `04_26_044`, `04_26_045`, and both are already in the ledger.**

| KOD | Change | Ledger | Outcome |
|---|---|---|---|
| `04_26_044` OPD 44 fast charging, priority areas | Rozpracovaná → **Otevřená**; zpřístupnění 2026-08-31 → 2026-09-25; open 2026-09-14 → 2026-10-09; close 2026-11-30 → **2026-12-07** | `dotace-opd-44-rychlodobijeci-prioritni` (date 2026-11-30) | **errata candidate**, not re-minted |
| `04_26_045` OPD 45 normal charging in towns and villages | same date moves | `dotace-opd-45-bezne-dobijeci-mesta` (date 2026-11-30) | **errata candidate**, not re-minted |

Receipt: both call texts were re-issued on 25 Sep (`pages/opd-44-text-vyzvy.pdf`, `pages/opd-45-text-vyzvy.pdf`,
from `opd.cz/UploadFiles/Vyzva_44_…_2026-09-25.pdf` and `Vyzva_45_…_2026-09-25.pdf`). Both read
`Datum vyhlášení výzvy 25. 9. 2026` and `Datum ukončení příjmu žádostí o podporu 7. 12. 2026, 14:00 hod.`, with
`Alokace výzvy 100 000 000 Kč` (44) and `150 000 000 Kč` (45). The opd3.opd.cz news box says
"ŘO OPD3 vyhlásil v pátek 25. září výzvu č. 44 a č. 45". Allocations are unchanged.

**Other state/field changes (09-21 → 09-28), none mintable:**
- *Pipeline moves, not yet open:* `04_26_046` OPD 46 fast charging for cars, whole ČR, 315,000,000 CZK:
  Plánovaná → **Finalizovaná**, zpřístupnění 2026-10-01, open 2026-10-14, close 2027-01-06. `04_26_047` OPD 47
  fast charging for **trucks**, 500,000,000 CZK: Plánovaná → **Rozpracovaná**, zpřístupnění 2026-10-31, open
  2026-11-16, close 2027-01-29. Their pages `opd3.opd.cz/stranka/vyzva-46/` and `/vyzva-47/` return HTTP 200 but are
  empty stubs with no call content (saved). `05_26_107` OPŽP 107: Rozpracovaná → **Schválená**, open 2026-10-14,
  close 2026-11-25 (already in the ledger as `dotace-opzp-107-environmentalni-centra`). `10_26_117` / `10_26_118`
  OP ST *Zavádění nástrojů*, 58,823,529.41 and 211,764,705.88 CZK: Plánovaná → Rozpracovaná, open 2026-10-14.
  `02_25_044` OPJAK: open moved to 2026-11-24, close to 2027-04-30, and it changed from round-based to rolling.
- *Closures (Otevřená → Uzavřená):* `01_26_087`, `03_26_111`, `05_24_073`, `05_26_101`…`05_26_104`,
  `06_23_103`, `06_23_104`, `12_26_046` (OP AMIF, closed 2026-09-23; a backlog item never minted), `12_26_049`.
- *Deadline extensions:* `03_23_058` OP Z+ social-partner dialogue (400 M CZK), close 2026-09-30 → **2026-11-30**.
  `10_25_089` OP ST circular economy Ústecký kraj (166.7 M CZK), close 2026-09-30 → **2026-11-04**. Neither is in
  the ledger; both are open-call backlog items (gap 2).
- *Allocation changes:* `01_24_043` OP TAK Inovační vouchery IV, 250 M → **350 M CZK**. IROP `06_22_039`,
  `06_22_053`, `06_22_066`, `06_22_067`, `06_23_074`, `06_23_108` were re-costed. None of these is in the ledger.
- State counts today: Otevřená 132, Plánovaná 25, Rozpracovaná 5, Vyhlášená 4, Finalizovaná 1, Schválená 1,
  Pozastavená 5, Uzavřená 622, Zrušená 19, Ukončená 5.

**Today's full MS2021+ call-id list, which is the next pass's left-hand side.** 819 codes, sorted. sha256 of the
newline-terminated list: `2cbbd8ab807b3c8a0f792ecb973eeec785749a059368838576fb96e5e57a9026` (same convention
as the 09-21 hash, which verified). Also at `pages/ms21-kody-2026-09-28.txt`, but that copy is pruned at 28 days
and the list below is the durable one.

```
01_22_001 01_22_002 01_22_003 01_22_004 01_22_005 01_22_006 01_22_007 01_22_008
01_23_009 01_23_010 01_23_011 01_23_012 01_23_013 01_23_014 01_23_015 01_23_016
01_23_017 01_23_018 01_23_019 01_23_020 01_23_021 01_23_022 01_23_023 01_23_024
01_23_025 01_23_026 01_23_027 01_23_028 01_23_029 01_23_030 01_23_031 01_23_032
01_23_033 01_23_034 01_23_035 01_23_036 01_23_037 01_23_039 01_23_040 01_23_041
01_24_038 01_24_042 01_24_043 01_24_044 01_24_045 01_24_046 01_24_047 01_24_048
01_24_049 01_24_050 01_24_051 01_24_052 01_24_053 01_24_054 01_24_055 01_24_056
01_24_059 01_24_060 01_24_061 01_24_062 01_24_063 01_24_065 01_24_073 01_25_057
01_25_058 01_25_064 01_25_066 01_25_067 01_25_068 01_25_069 01_25_070 01_25_071
01_25_072 01_25_074 01_25_075 01_25_076 01_25_077 01_25_078 01_25_079 01_25_080
01_25_081 01_25_082 01_25_083 01_26_084 01_26_085 01_26_086 01_26_087 01_26_088
01_26_089 01_26_090 01_26_091 01_26_092 01_26_093 01_26_094 01_26_095 01_26_096
02_22_001 02_22_002 02_22_003 02_22_004 02_22_005 02_22_006 02_22_007 02_22_008
02_22_009 02_22_010 02_22_011 02_22_012 02_23_013 02_23_014 02_23_015 02_23_016
02_23_017 02_23_018 02_23_019 02_23_020 02_23_021 02_23_022 02_23_023 02_23_024
02_23_025 02_23_026 02_23_027 02_23_028 02_23_029 02_24_030 02_24_031 02_24_032
02_24_033 02_24_034 02_24_035 02_24_036 02_24_037 02_24_038 02_25_039 02_25_040
02_25_041 02_25_042 02_25_043 02_25_044 02_25_045 02_26_046 02_26_047 02_26_048
02_27_049 02_27_050 03_00_094 03_00_095 03_22_001 03_22_002 03_22_003 03_22_004
03_22_005 03_22_006 03_22_007 03_22_008 03_22_009 03_22_010 03_22_011 03_22_012
03_22_013 03_22_014 03_22_015 03_22_016 03_22_017 03_22_018 03_22_019 03_22_020
03_22_021 03_22_022 03_22_023 03_22_024 03_22_025 03_22_026 03_22_027 03_22_028
03_22_029 03_22_030 03_22_031 03_22_032 03_22_033 03_22_034 03_22_035 03_22_036
03_22_037 03_22_038 03_22_039 03_22_040 03_22_041 03_22_042 03_22_043 03_22_044
03_22_045 03_22_046 03_22_099 03_22_100 03_22_101 03_23_047 03_23_048 03_23_049
03_23_050 03_23_051 03_23_052 03_23_053 03_23_054 03_23_055 03_23_056 03_23_057
03_23_058 03_23_093 03_23_096 03_24_059 03_24_060 03_24_061 03_24_062 03_24_063
03_24_064 03_24_065 03_24_066 03_24_067 03_24_068 03_24_069 03_24_070 03_24_071
03_24_072 03_24_073 03_24_074 03_24_075 03_24_076 03_24_077 03_24_078 03_24_079
03_25_080 03_25_081 03_25_082 03_25_083 03_25_084 03_25_085 03_25_086 03_25_087
03_25_088 03_25_089 03_25_097 03_25_102 03_25_103 03_25_104 03_25_105 03_25_106
03_25_108 03_25_109 03_25_110 03_26_090 03_26_091 03_26_107 03_26_111 03_26_112
03_27_092 03_27_098 04_22_001 04_22_002 04_22_003 04_22_004 04_22_005 04_22_006
04_22_007 04_22_008 04_22_009 04_22_010 04_23_011 04_23_012 04_23_013 04_23_014
04_23_015 04_23_016 04_23_017 04_23_018 04_23_019 04_23_020 04_23_021 04_23_022
04_23_023 04_24_024 04_24_025 04_24_026 04_24_027 04_24_028 04_24_029 04_24_030
04_24_031 04_24_032 04_24_033 04_24_034 04_24_035 04_25_036 04_25_037 04_25_038
04_25_039 04_25_040 04_25_041 04_25_042 04_25_043 04_26_044 04_26_045 04_26_046
04_26_047 04_26_048 05_22_001 05_22_002 05_22_003 05_22_004 05_22_005 05_22_006
05_22_007 05_22_008 05_22_009 05_22_010 05_22_011 05_22_012 05_22_013 05_22_014
05_22_015 05_22_016 05_22_017 05_22_018 05_22_019 05_22_020 05_22_021 05_22_022
05_22_023 05_22_024 05_22_025 05_22_026 05_22_027 05_22_028 05_22_029 05_22_030
05_22_031 05_23_032 05_23_033 05_23_034 05_23_035 05_23_036 05_23_037 05_23_038
05_23_039 05_23_040 05_23_041 05_23_042 05_23_043 05_23_044 05_23_045 05_23_046
05_23_047 05_23_048 05_23_049 05_23_050 05_23_051 05_23_052 05_23_053 05_23_054
05_23_055 05_23_056 05_23_057 05_23_058 05_23_059 05_23_060 05_23_061 05_23_062
05_24_063 05_24_064 05_24_065 05_24_066 05_24_067 05_24_068 05_24_069 05_24_070
05_24_071 05_24_072 05_24_073 05_24_074 05_24_075 05_24_076 05_24_077 05_24_078
05_24_080 05_24_083 05_25_079 05_25_081 05_25_082 05_25_084 05_25_085 05_25_086
05_25_087 05_25_088 05_25_089 05_25_090 05_25_091 05_25_092 05_25_093 05_25_094
05_25_095 05_25_096 05_25_097 05_25_098 05_25_099 05_25_100 05_26_101 05_26_102
05_26_103 05_26_104 05_26_105 05_26_106 05_26_107 05_26_108 05_26_109 06_22_001
06_22_002 06_22_003 06_22_004 06_22_005 06_22_006 06_22_007 06_22_008 06_22_009
06_22_010 06_22_011 06_22_012 06_22_013 06_22_014 06_22_015 06_22_016 06_22_017
06_22_018 06_22_019 06_22_020 06_22_021 06_22_022 06_22_023 06_22_024 06_22_025
06_22_026 06_22_027 06_22_028 06_22_029 06_22_030 06_22_031 06_22_032 06_22_033
06_22_034 06_22_035 06_22_036 06_22_037 06_22_038 06_22_039 06_22_040 06_22_041
06_22_042 06_22_043 06_22_044 06_22_045 06_22_046 06_22_047 06_22_048 06_22_049
06_22_050 06_22_051 06_22_052 06_22_053 06_22_054 06_22_055 06_22_056 06_22_057
06_22_058 06_22_059 06_22_060 06_22_061 06_22_062 06_22_063 06_22_064 06_22_065
06_22_066 06_22_067 06_22_068 06_22_069 06_22_070 06_22_111 06_22_112 06_23_071
06_23_072 06_23_073 06_23_074 06_23_075 06_23_076 06_23_077 06_23_078 06_23_079
06_23_080 06_23_081 06_23_082 06_23_083 06_23_084 06_23_085 06_23_086 06_23_087
06_23_088 06_23_089 06_23_090 06_23_091 06_23_092 06_23_093 06_23_094 06_23_095
06_23_096 06_23_097 06_23_098 06_23_099 06_23_100 06_23_101 06_23_102 06_23_103
06_23_104 06_23_105 06_23_106 06_23_107 06_23_108 06_23_109 06_23_110 06_23_113
06_23_114 06_24_115 06_24_116 06_25_117 06_25_118 06_26_119 06_26_120 06_26_121
06_26_122 07_22_001 07_22_002 07_22_003 07_22_004 07_22_005 08_22_001 08_22_002
08_22_003 08_23_004 08_23_005 08_23_006 08_23_007 08_23_008 08_23_009 08_23_010
08_23_011 08_23_012 08_23_013 08_23_014 08_24_015 08_24_016 08_24_017 08_24_018
08_24_019 08_24_020 08_24_021 08_24_022 08_24_023 08_25_024 08_25_025 08_25_026
08_25_027 08_25_028 08_25_029 08_25_030 08_26_031 08_26_032 08_26_033 08_26_034
08_26_035 08_26_036 08_26_037 08_26_038 08_26_039 10_22_001 10_22_002 10_22_003
10_22_004 10_23_005 10_23_006 10_23_007 10_23_008 10_23_009 10_23_010 10_23_011
10_23_012 10_23_013 10_23_014 10_23_015 10_23_016 10_23_017 10_23_018 10_23_019
10_23_020 10_23_021 10_23_022 10_23_023 10_23_024 10_23_025 10_23_026 10_23_027
10_23_028 10_23_029 10_23_030 10_23_031 10_23_032 10_23_033 10_23_034 10_23_035
10_23_036 10_23_037 10_23_038 10_23_039 10_23_040 10_23_041 10_23_042 10_23_043
10_23_044 10_23_045 10_23_046 10_24_047 10_24_048 10_24_049 10_24_050 10_24_051
10_24_052 10_24_053 10_24_054 10_24_055 10_24_056 10_24_057 10_24_058 10_24_059
10_24_060 10_24_061 10_24_062 10_24_063 10_24_064 10_24_065 10_24_066 10_24_067
10_24_068 10_24_069 10_24_070 10_24_071 10_24_072 10_25_073 10_25_074 10_25_075
10_25_076 10_25_077 10_25_078 10_25_079 10_25_080 10_25_081 10_25_082 10_25_083
10_25_084 10_25_085 10_25_086 10_25_087 10_25_088 10_25_089 10_25_090 10_25_091
10_25_092 10_25_093 10_25_094 10_25_095 10_25_096 10_25_097 10_25_098 10_25_099
10_25_100 10_25_101 10_25_102 10_25_103 10_25_104 10_26_105 10_26_106 10_26_107
10_26_108 10_26_109 10_26_110 10_26_111 10_26_112 10_26_113 10_26_114 10_26_115
10_26_116 10_26_117 10_26_118 11_22_001 11_22_002 11_23_003 11_23_004 11_23_005
11_23_006 11_23_007 11_23_008 11_23_009 11_23_010 11_23_011 11_24_012 11_24_013
11_24_014 11_24_015 11_24_016 11_24_017 11_25_018 11_25_019 11_25_020 11_25_021
11_26_022 12_22_001 12_22_002 12_22_003 12_22_004 12_23_005 12_23_006 12_23_007
12_23_008 12_23_009 12_23_010 12_23_011 12_23_012 12_23_013 12_23_014 12_23_015
12_23_016 12_23_017 12_24_018 12_24_019 12_24_020 12_24_021 12_24_022 12_24_023
12_24_024 12_25_025 12_25_026 12_25_027 12_25_028 12_25_029 12_25_030 12_25_031
12_25_032 12_25_033 12_25_034 12_25_035 12_25_036 12_25_037 12_25_038 12_26_039
12_26_040 12_26_041 12_26_042 12_26_043 12_26_044 12_26_045 12_26_046 12_26_047
12_26_048 12_26_049 12_26_050 12_26_051 12_26_052 12_26_053 12_26_054 12_26_055
12_26_056 13_22_001 13_23_002 13_23_003 13_23_004 13_23_005 13_23_006 13_23_007
13_23_008 13_24_009 13_24_010 13_24_011 13_24_012 13_25_013 13_25_014 13_26_015
13_26_016 13_26_017 13_26_018 13_26_019 13_26_020 14_22_001 14_22_002 14_23_003
14_23_004 14_23_005 14_23_006 14_23_007 14_23_008 14_24_009 14_24_010 14_24_011
14_25_012 14_25_013 14_25_014 14_25_015 14_25_016 14_26_017 14_26_018 14_26_019
14_26_020 14_26_021 14_26_022
```

### Checklist source 2: the portals the `feeds.json` row names

Each page was fetched on 2026-09-28 and diffed against its 2026-09-19 capture in
`localproblems/data/raw/2026-09-19/dotace/pages/` (visible text only: tags, scripts, styles and comments stripped).
The 2026-09-21 captures are gone with their worktree. The 09-21 section lists every 09-19→09-21 change, so any
change below that it does not list happened after 09-21.

- **IROP.** `https://irop.gov.cz/cs/vyzvy-2021-2027` returned **HTTP 200**. Two rows went *Otevřená → Uzavřená*,
  the portal side of `06_23_103` / `06_23_104` closing in the XML. No row was added.
  `…/Vyzvy-2021-2027/Vyzvy/70vyzvaIROP` returned HTTP 200 and is still *Otevřená*. The only change is the statistics
  box (`27. 9. 2026`: 639,509,514 Kč requested, 365 applications, 73.8 %), which is project traffic.
  **Nothing new.** The deep AJAX walk (recipe in the 09-21 section) was not repeated: the XML shows no new `06_*` code
  and no IROP code moving into Vyhlášená or Otevřená.
- **OPŽP.** `https://opzp.cz/nabidka-dotaci/` returned **HTTP 200**. Calls 101, 102, 103, 104 and 73 left the
  listing after closing on 25. 9. 2026. One card is newly visible: *Výzva č. 2/2026 FN – Půjčky na intenzifikaci
  čistíren odpadních vod* (window 2. 7. 2026 – 31. 3. 2027; the card shows `Alokace 0 Kč`). **It is already in
  the ledger** as `dotace-sfzp-2-2026-fn-cov`, so nothing to mint. `https://opzp.cz/dotace/107-vyzva/` returned
  HTTP 200 and is text-identical. **Nothing new.**
- **OPJAK.** `https://opjak.cz/vyzvy/` returned **HTTP 200**. The only changes are the schedule link text
  (2022–2027) and the dashboard percentage. No call row was added. `https://opjak.cz/harmonogram-vyzev/` returned
  **HTTP 200 and CHANGED**: it now links a new *Harmonogram výzev 2027 verze 1* and *2026 verze 3*, both approved
  18 Sep 2026. Both PDFs were fetched (HTTP 200) and converted to text. That is the source of `02_27_049` and
  `02_27_050`, both still planned. **No new open call.**
- **SFŽP.** `…/dotace-a-pujcky/` and `…/financni-nastroje-a-pujcky/` returned **HTTP 200** and are text-identical.
  `…/modernizacni-fond/vyzvy/` returned **HTTP 200 with one change**: *Výzva TRANSGov č. 2/2025 – Elektrizace
  železničních tratí* went from `Alokace: 7 175 000 000 Kč` to `Alokace: 10 175 000 000 Kč`. It is in the ledger as
  `dotace-mf-transgov-2-elektrizace-trati` (money_eur 292,900,000), which makes it an **errata candidate**.
  **No new call.**
- **NPO.** `https://planobnovy.gov.cz/vyhlasene-vyzvy/` returned **HTTP 200** and is text-identical. **Nothing new.**
- **TAČR.** `https://tacr.gov.cz/` returned **HTTP 200**. The "Aktuální možnosti podpory" box dropped RAMP, which
  closed 2026-09-22. It still lists FOREST, SIGMA 18 DC1, Biodiversa, Water4All, DUT 2026, THÉTA 2 4th competition
  and CET, **all nine TAČR calls are in the ledger** (`dotace-tacr-*`). The news items are results (DUT 2025,
  SIGMA 16 DC4 formal check), not calls. `https://tacr.gov.cz/programy-a-souteze/` returned **HTTP 200**: FOREST and
  others changed status label, and the calendar rotated. **No new competition.**
- **CINEA / HaDEA.** `https://cinea.ec.europa.eu/funding-opportunities/calls-proposals_en` returned **HTTP 200**.
  The listing shrank from **25 to 10** "Upcoming and open" calls, because the LIFE-2026 SAP family closed on
  2026-09-22. All 10 remaining calls fit on page 0 and **every one was already on the 09-19 capture** (checked title
  by title). Those 10 are: CEF Transport 2026, HE fair transition €45 M, Cities Mission €85.5 M, batteries and
  mobility €263 M, energy supply €23.5 M, NEB Facility €101.1 M, HE energy €131.5 M, PSLF, LIFE SNaP, LIFE SIP CLIMA.
  Pages 1–3 no longer exist at this count and were not fetched. `https://hadea.ec.europa.eu/calls-proposals_en`
  returned **HTTP 200** and is text-identical. **Nothing new.** No 429s this pass.

**Checklist: 8 of 8 sources visited** (MS2021+ XML plus IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA), each
named above with its URL and HTTP status.

### Records staged: 0

`staged.jsonl` has zero lines, and that is the correct result for this pass. The diff adds two codes, and both are
2027 *planned* calls. The two calls that newly opened (OPD 44/45) are already held, and only their dates moved. No
portal shows a call the ledger lacks. Dry run against a scratch copy of `data/signals`:
`normalize --complete --dry-run: would append 0 records across 0 file(s); 0 dropped by materiality; 0 incomplete;
0 refused by AC-GDPR1.` / `dedup by identity key (append): 0 skipped`.

### MATCH candidates

No records were staged, so none are new. The items this pass touched map to problems as follows:
- OPD 44/45 (errata) and OPD 46/47 (pipeline; call 47 is truck charging, 500 M CZK) sit next to
  **p-0046-electric-bus-fleet-finance** (depot chargers). That is adjacent, not a direct hit: these are public-access
  car and truck charging calls, not bus depots. Call 47 would also bear on **p-0010-trucking-back-office** only
  through the fleet-electrification angle, which is weak.
- TRANSGov 2 (rail electrification, sole applicant Správa železnic): no problem.
- OP JAK Desegregace / PRO-ROMA II: at most weakly **p-0042-special-needs-assessment-backlog** (school inclusion),
  and only once they are declared.

### Errata candidates (for the coordinator; this pass did not write `data/errata.jsonl`)

1. `dotace-opd-44-rychlodobijeci-prioritni`: date 2026-11-30 → **2026-12-07** (call re-declared 25. 9. 2026,
   opens 9. 10. 2026). Its notes also say "opens 2026-09-14", which is now wrong. Receipt `pages/opd-44-text-vyzvy.txt`.
2. `dotace-opd-45-bezne-dobijeci-mesta`: the same date change. Receipt `pages/opd-45-text-vyzvy.txt`.
3. `dotace-mf-transgov-2-elektrizace-trati`: allocation 7,175,000,000 → **10,175,000,000 CZK** (≈417.9 M EUR at
   24.350). Receipt `pages/sfzp-mf-vyzvy.html`.

### Coverage gaps (named, not silent)

1. **EU topic conditions are still owed**, carried from 09-21 gap 1: funding rates for `HORIZON-CL5-2026-11` and
   `SMP-FOOD` (call-document PDFs), the CEF-DIG budget, `HORIZON-CID/MISS-CANCER/CL4-2026-03`, and the LIFE TA/PLP
   identifiers. **LIFE-2026 SAP family closed 2026-09-22 unminted.** Its budgets (319 M EUR) are on record in the
   09-21 section only. The 09-21 pass's warning ("lost to the ledger the same way LIFE-CET was") has now come true,
   and whether to mint closed calls retroactively is the coordinator's decision. `ec.europa.eu` was not accessed this
   pass, because there was no delta to chase there.
2. **Open-call backlog is still owed** (from 09-18/09-21). Updated against today's XML: `12_26_046` OP AMIF
   **closed 2026-09-23 unminted**. `03_24_059`, `10_25_089` and `14_26_018` were due 2026-09-30: `10_25_089` is now
   extended to 2026-11-04, and the other two have not moved. `03_23_058` (not on the old list) is extended to
   2026-11-30. The IROP, OPD `04_25_038`, OP Z+ `03_24_062/03_22_012`, OP ST `10_25_095/10_26_110` and OP NSHV
   `14_26_019` items were not re-examined this pass. Also not in the ledger: `01_24_043` Inovační vouchery IV
   (allocation just raised to 350 M CZK). OP TAK is not on this feed's portal list, but the call is in the XML.
3. **OPD 46 / 47 are not yet declared.** 46 becomes accessible on 2026-10-01 (Finalizovaná, 315 M CZK) and 47 on
   2026-10-31 (500 M CZK, trucks). Their pages are empty stubs today. The next pass mints them once the call texts
   exist.
4. **OP JAK planned calls:** `02_25_044` (open 2026-11-24, now rolling), `02_25_045` and `02_26_046`, plus the new
   `02_27_049` Desegregace and `02_27_050` PRO-ROMA II. The 2026 v3 and 2027 v1 schedules are saved as text but were
   not read line by line for other re-timed calls.
5. **OPŽP 107** is Schválená in the XML, with receipt opening 2026-10-14. It is already minted with a status caveat;
   the next pass confirms the declaration and removes the caveat via errata if warranted.
6. **Field-level left side reconstructed.** The 09-21 XML is gone, so the diff ran against 09-19 and subtracted the
   one change the 09-21 section documented. The code-level left side verified by hash. Next pass: the 2026-09-28 XML is
   in `pages/`, so use it directly while it survives the 28-day prune.
7. **Not repeated this pass:** the IROP deep AJAX walk, the OPŽP POST API and the IROP status filters. In each case
   the XML shows no delta that would need them.

### Pass summary (5 lines)

```
feed:              dotace-scan (weekly delta, 2026-09-28; left-hand side = 09-21 call-id list, 817 codes, hash-verified)
checklist sources: 8 of 8 visited — MS2021+ XML (200, 817→819, +2/−0: 02_27_049, 02_27_050, both Plánovaná 2027) + IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA
records:           0 staged — newly opened 04_26_044/045 (OPD 44/45) already in the ledger; portals show no call the ledger lacks; dry run clean (0/0/0/0)
coverage gaps:     7 named — EU topic conditions (LIFE SAP closed unminted); open-call backlog (AMIF 12_26_046 closed unminted); OPD 46/47 pending; OPJAK planned (+2); OPŽP 107 Schválená; field-level left side reconstructed; deep walks not repeated
errata candidates: 3 — OPD 44 and 45 close 2026-11-30 → 2026-12-07; TRANSGov 2 allocation 7.175 → 10.175 bn CZK
```


## arb-scan pass — 2026-09-28 (weekly delta)

Attended pass, worktree `localproblems-weekly-2026-09-28`. Staging only: nothing was appended to
`data/signals/**`, `seen.txt`, `dropped-log.jsonl` or `data/register.db`, `feeds.json` and the shared
`manifest.md` were not touched, and git state was not touched. Output:

- `data/raw/2026-09-28/funded/staged.jsonl` — 5 records, each `"evidence_type": "funded"`, `"_needs": []`,
  a structured `cz_check`, a verified verbatim `quote`
- `data/raw/2026-09-28/funded/manifest-section.md` — this file
- `data/raw/2026-09-28/funded/pages/` — 64 payloads: every page quoted or cited below, including the 403 bodies

**Window.** Previous pass 2026-09-21. The strict window (rounds announced 2026-09-21 to 09-28) produced
three of the five records (`de-mika`, `nl-duqu`, `is-50skills`, all 2026-09-24). The other two come from
the category sweep: `de-galvany` (2026-06-08), which no pass had captured, and `fi-klinik` (2018-05-18),
the health debt carried since 2026-09-18. Every record states its round date in `date` and its
provenance in `money_note`.

### The checklist source for this feed: THE CATEGORY-ROTATION DUTY

Walked: 1 of 1. All 12 categories are named below. Rotation state at the start was read from the
`## arb-scan` section of `data/raw/2026-09-21/manifest.md`. Arb-record counts are `source: arb-scan`
lines in `data/signals/funded/*.jsonl` before this pass (228 in total).

This pass covered the four owed categories, the longest-unswept (last swept 2026-09-18), and stopped there.

| category | last swept BEFORE | arb records before | covered this pass | records staged | last swept AFTER |
|---|---|---|---|---|---|
| energy | 2026-09-18 | 18 | **YES** (owed) | 1 (`de-galvany`) | 2026-09-28 |
| fintech | 2026-09-18 | 21 | **YES** (owed) | 2 (`de-mika`, `nl-duqu`) | 2026-09-28 |
| health | 2026-09-18 | 29 | **YES** (owed, and the **Klinik debt is paid**) | 1 (`fi-klinik`) | 2026-09-28 |
| b2b | 2026-09-18 | 65 | **YES** (owed) | 1 (`is-50skills`) | 2026-09-28 |
| other | 2026-09-19 | 7 | no | 0 | 2026-09-19 |
| mobility | 2026-09-19 | 10 | no | 0 | 2026-09-19 |
| housing | 2026-09-19 | 13 | no | 0 | 2026-09-19 |
| environment | 2026-09-19 | 18 | no | 0 | 2026-09-19 |
| govtech | 2026-09-21 | 7 | no | 0 | 2026-09-21 |
| education | 2026-09-21 | 10 | no | 0 | 2026-09-21 |
| legal-compliance | 2026-09-21 | 13 | no | 0 | 2026-09-21 |
| retail-services | 2026-09-21 | 17 | no | 0 | 2026-09-21 |

**The next pass starts from the four at 2026-09-19, thinnest first: `other` (7), `mobility` (10),
`housing` (13), `environment` (18).** Then the four at 2026-09-21, thinnest first: `govtech` (7),
`education` (10), `legal-compliance` (13), `retail-services` (17). The four swept today go last.

### Sources walked, each named with what it gave

| source | result |
|---|---|
| **tech.eu RSS** `https://tech.eu/feed/` | HTTP 200, 137 KB, 20 items, 2026-09-23 to 09-27. Saved `pages/listing-tech_eu_feed_`. Gave Duqu, 50skills, Crux Analytics, Kontext and Reply Next. |
| **tech.eu weekly recap** | **Not published yet.** The Monday recap for 2026-09-21 to 09-25 was not on tech.eu's homepage at fetch time (saved `pages/listing-tech_eu_home.html`; newest item 2026-09-27), and `/tag/weekly-recap/` and `/2026/09/` return 404. The Friday round-up that stands in for it, *"TEKEVER raises $580M Series D, DTCP closes €455M defence fund…"* (2026-09-25, HTTP 200, saved as `pages/cand-tech_eu_2026_09_25_tekever...html`), was read in full: 65+ deals with outbound links, and it confirmed Duqu, Palma.ai, Gamindo and Reply Next. See COVERAGE GAP 1. |
| **tech.eu article pages** | HTTP 200 on all seven requested (Crux, Duqu, 50skills, Kontext, Reply Next, the TEKEVER round-up, and Tandem Health from 2026-09-14). |
| **EU-Startups RSS** `https://www.eu-startups.com/feed/` | HTTP 200, 86 KB, 10 items back to 2026-09-23. Saved. Gave the week's round-up link and Duqu, 50skills (its title carries the EUR figure used on `is-50skills`), Clastix and Metycle (`de-metycle` is already in the ledger). |
| **EU-Startups article pages** | **403 on every attempt this pass**, desktop UA with and without Accept headers. The body is a Cloudflare "Just a moment..." challenge (saved as `pages/search-eustartups-cloudflare-403-duqu.html` and the `cand-www_eu_startups_*` files). **This reverses the 2026-09-21 note that article pages were reachable.** The round-up (Sept 21 – Sept 25) also 403s now rather than showing the CLUB paywall. See COVERAGE GAP 2. |
| **Sifted RSS** `https://sifted.eu/feed` | HTTP 200, 24 items back to 2026-09-23. Saved. In-category items: Humanos (Lisbon, insurance for AI agents, fintech) — the article is **403** (saved `pages/cand-sifted_eu_articles_humanos_seed_raise_.html`), so no amount could be receipted; the rest are commentary, defence, deeptech or `other` (Magic AI's fitness mirror). |
| **Vestbee** | `sitemap_index.xml` 200 and `__sitemap__/posts.xml` 200 (1.06 MB) **but still generated 2026-09-09**, newest `lastmod` 2026-09-09 — **stale for the third week**. The category-page retry this pass owed was done: `/insights/articles`, `/insights/news`, `/insights/category/funding` all 404, **but `https://vestbee.com/insights` returns 200 and lists current posts** (saved `pages/probe-vestbee_com_insights.html`), including mika (2026-09-24), Duqu (2026-09-24), StandardX (2026-09-23) and Clastix. `de-mika` was found and receipted here. **Vestbee's route is `/insights`, not the sitemap.** Ten article pages fetched, all 200; Cargofy, Paymove and Wultra are already in the ledger. |
| **brutkasten** (for signteq) | `brutkasten.com/?s=signteq` still **403**. The other route worked: trendingtopics.eu search → two signteq articles (EN and DE), both 200, saved as `pages/cand-signteq-*.html`, dated 2026-09-16. The amount is still not receipted, so the round is not staged (below). |
| **ARES** (`ekonomicke-subjekty/vyhledat`, POST) | HTTP 200 on every query. 16 name searches run, IČO and datumVzniku recorded for every Czech player named in a `cz_check`. |
| **Own ledgers** | `data/signals/funded/*.jsonl` (6,127 lines), `data/signals/seen.txt` (18,697 ids) and `data/lookup/cz-contract-parties.jsonl` checked per candidate and per Czech IČO; `data/problems/cz/*.md` grepped for each Czech player. |
| **Web search** | 17 searches: 4 English (energy sweep, health sweep, the tech.eu recap, a Klinik profile search), 2 receipt hunts (Klinik 2018, GALVANY), and **11 Czech gap-check queries**, recorded verbatim in each record's `notes` and `cz_check.queries`. |

### COVERAGE GAPS (named, with what a future pass owes them)

1. **The tech.eu Monday recap for 2026-09-21 to 09-25 was not published at fetch time.** It was the most
   productive source two weeks running. The Friday round-up covered the notable deals, but not the full
   list of 70 or so. **Owed:** the next pass reads the 2026-09-28 recap first for the category it owns;
   rounds in energy, fintech, health or b2b that it lists and this pass missed are fair game in any
   category's sweep.
2. **EU-Startups is now fully behind a Cloudflare challenge**: article pages, not only search and tag pages,
   return 403 with the "Just a moment..." body. The RSS still works (titles and summaries only). **Owed:**
   reach EU-Startups stories through tech.eu, Vestbee or the company's own release, or run a real browser
   session (`agent-browser`) if a specific article is the only receipt.
3. **The Vestbee sitemap is stale for the third week** (generated 2026-09-09). This is no longer a
   coverage hole, because `/insights` lists current posts. **Owed:** use `/insights` as the standing route
   and drop the sitemap.
4. **Sifted articles return 403** (Humanos). The RSS works. **Owed:** the Humanos round (Lisbon, insurance
   for AI agents, `fintech`) needs another receipt, from the company's release or Portuguese press.
5. **`se` is not in arb-scan's `id_prefixes`**, so **Tandem Health** (Stockholm, USD 100M Series B on
   2026-09-14, an AI co-pilot that writes clinicians' notes, used by 10,000 care organisations in 14 markets;
   saved as `pages/cand-tech_eu_2026_09_14_swedish_healthtech_tandem...html`) **could not be staged**. The
   prefix list is `feeds.json`'s to widen, and this pass may not write `feeds.json`. **Owed:** add `se` to
   arb-scan's `id_prefixes`, then stage `se-tandemhealth` with a Czech check. It is the natural foreign
   comparable for **p-0036** (hospital clinical documentation).
6. **Schema validation was mechanical, not zod.** `web/node_modules` has zod but no `tsx`, so
   `SignalSchema` was not run directly on the staged lines. The `CzCheckSchema` invariants (taken ⇒ ≥1
   direct + established; control.passed; ≥2 queries for absent/contested; 8-digit IČO) were checked in
   Python on the lines `--complete` wrote to a scratch copy, and all five pass. The build will run the
   real check.
7. **Maturity limbs for large Czech incumbents were not receipted.** E.ON Energie, KS - program,
   AC Heating, Nano Energies, Sloneek and HCH Consulting are over 3 years old in ARES, but this pass did
   not receipt a second limb for any of them, so each is recorded as `early` *on the test*, with that
   stated in `evidence`. No verdict rests on any of them. **Owed:** nothing, unless one of them ever
   becomes the deciding player.

### Dedup suppressions — found, NOT staged because already in the ledger

- **Cargofy** (UA, USD 11M Series A, 2026-06-18) — `round-cargofy`.
- **Paymove** (PL, EUR 2.1M, 2026-06-10) — `round-paymove`.
- **Metycle** (DE, EUR 131.7M credit facility, 2026-09-24) — `de-metycle`. Debt facility, no new model.
- **Axle Energy** (GB, energy flexibility) — `round-axle-energy`, surfaced by the energy sweep.
- **Aisel Health** (DK, EUR 1.7M pre-seed, psychiatry records) — `round-aisel`, surfaced by the health sweep.
- **Verda** (FI, USD 189M AI cloud) — `round-verda`.
- **Wultra** (CZ) — Czech, and the register's own positive control; not an arb candidate.

### Candidates examined and rejected (so the selection is not silent)

- **signteq** (AT, Vienna; KYC/KYB, PEP and sanctions screening, qualified e-signatures, plus a new
  "Know Your Agent" line; round dated 2026-09-16 on trendingtopics.eu). **Not staged, again, now for one
  reason instead of two:** the date is receipted, but the amount is still not. The source says only that
  the size was undisclosed and runs into the millions ("siebenstellige"). The rule is amount AND date.
  **Owed:** a figure from the company, Compass-Verlag or the Austrian commercial register (Firmenbuch
  capital increase). It stays a live `legal-compliance` candidate.
- **Crux Analytics** (US-based, EUR 1.9M seed, 2026-09-24): software for small banks and credit unions to
  win and keep small-business clients. The buyer is the US community-bank and credit-union segment, which
  has no Czech counterpart at that density. It is a US story, not a transferable model.
- **Kontext** (DE, USD 4M, 2026-09-24): runtime security for AI agents. It is `b2b`, but not checked this
  pass. It is a horizontal security product, and no Czech gap check was run, so it is recorded here and
  not staged half-checked. **Owed:** a b2b pass can take it.
- **Reply Next** (ES, EUR 400k pre-seed, 2026-09-24): reviews and local-presence management for brands
  with hundreds of locations. Money 1 and not checked in Czech; held for a `retail-services` pass.
- **Clastix** (IT, EUR 2.9M, Kubernetes) and **Palma.ai** (DE, USD 1.8M, governed AI agents): developer
  and enterprise infrastructure with no buyer-side problem the register tracks.
- **Companion.energy** (BE, EUR 7.8M, 2026-06): an EU-Startups article, now 403, so it could not be
  receipted beyond the search snippet. **Owed** to the next energy pass.
- **Gamindo** (IT, EUR 1.4M): corporate training, which is `education` and not owned this pass.

### Records — 5 staged in `data/raw/2026-09-28/funded/staged.jsonl`

Verdict vocabulary is unchanged: **absent** means no Czech seller was found, with ≥2 query shapes and a
passing control. **contested** means sellers exist but none is established. **taken** means an
established direct seller exists. All five came back **taken**: this week's funded models are already sold
in Czechia. This is the outcome the Aibility lesson predicted. Each check was run in Czech with
customer-language query shapes, and each named player was resolved in ARES.

| id | category | what | money | maturity abroad | CZ verdict |
|---|---|---|---|---|---|
| `de-galvany` | energy | heat pumps sold, installed and then run against dynamic power prices, as one package | EUR 10M seed (2026-06-08) | established (late-2022 founding; 2,500+ systems; EUR 20.1M 2025 revenue) | **taken** — Woltair s.r.o. (IČO 06770525, since 2018; Series A, own ledger `round-woltair`) sells install + subsidy end-to-end; E.ON sells the same. Not found: a Czech seller of the *operating* layer (household heat pump + battery run against the spot price as a service). That is a sub-niche observation, not a verdict. |
| `fi-klinik` | health | sorts incoming patient requests by condition and urgency before a clinician sees them | EUR 2.25M Series A (2018-05-18) | established (since 2013; named UK practices; Aalto study, -14% cost per patient) | **taken** — Medevio s.r.o. (IČO 09675400, since 2020) auto-sorts GP requests by type and urgency and flags acute states; "více než 4 000 lékařů a sester". |
| `de-mika` | fintech | AI bookkeeping, VAT, annual accounts and tax for small companies, reviewed by accountants | EUR 6M seed (2026-09-24) | early (founded 2024; 750+ companies, EUR 1M+ ARR) | **taken** — iÚčto / Direct Accounting s.r.o. (IČO 28499638, since 2008) sells online accounting with AI plus accounting services to "přes 40 000 podnikatelů"; HCH Consulting also sells it (early on the test). |
| `nl-duqu` | fintech | cash advances against unpaid B2B invoices within 24 hours, invoice not sold | EUR 1.5M pre-seed (2026-09-24) | early (founded 2025) | **taken** — Cashbot / Red Stone Now s.r.o. (IČO 06790887, since 2018; 25,000+ financings, 1.75bn CZK) and Platební instituce Roger a.s. (IČO 01729462, since 2013, ČNB-licensed). |
| `is-50skills` | b2b | HR processes run as workflows, AI agents on the judgment steps | USD 6M ≈ EUR 5.3M (2026-09-24) | traction limb met (Icelandair, Eimskip, City of Reykjavík); years limb not receipted | **taken** — ALVENO s.r.o. (IČO 26288613, since 2002; named customers FlixBus, Heureka) sells digital onboarding and HR approvals; Sloneek (IČO 08684332) sells "AI HR Workflows". |

**Positive control (MATCH §4), run 2026-09-28 by this pass, two limbs on every record:** (a) ARES name
search `Wultra` → Wultra s.r.o., IČO 03643174, datumVzniku 2014-12-15. The ARES method surfaces a
known small Czech software vendor. (b) In each record's own domain, the same Czech descriptive query
surfaced a known Czech vendor in an adjacent space: AC Heating (heat pumps), KPK software's Dr. HELP and
B&G's 3L Manažer (ambulatory software), iÚčto, MyÚčto and Ježek software (accounting), Bibby Financial
Services (factoring), and KS - program (HR/payroll). **PASSED on all five.**

**Mechanical checks run before writing, all passing:**
- Every `quote` is a literal substring of its saved payload after whitespace collapse, and ≤300 chars.
- Every `id` prefix is the lowercase ISO2 of its `geo_origin`, and is in arb-scan's `id_prefixes` (de, fi, nl, is).
- No `id` is in `seen.txt` or any funded ledger.
- `scores.money` matches the ladder against `money_eur`.
- No record trips the materiality filter.

**Dry run** (scratch copy of `data/signals`):
`normalize.py --raw data/raw/2026-09-28/funded --complete --dry-run --today 2026-09-28 --out-dir <scratch> --seen <scratch>/seen.txt --dropped-log <scratch>/dropped-log.jsonl`
→ `would append 5 records across 1 file(s); 0 dropped by materiality; 0 incomplete; 0 refused by
AC-GDPR1`, identity-key dedup 0 skipped, and the allowlist dropped only `_needs` and `evidence_type`, as
designed. A non-dry `--complete` into the same scratch copy confirmed that `cz_check` survives the
allowlist on all five lines.

### Which existing problem each record could be a comparable for

| record | existing problem in `data/problems/cz/` |
|---|---|
| `de-galvany` | **p-0002** (installer back office): GALVANY is the vertically integrated alternative to selling software to installers, and Woltair is already named there. Also **p-0025** (insulation and retrofit patchwork). |
| `de-mika` | **p-0023** (AI accounting capacity): the foreign proof that an AI ledger with accountant review runs a small company's full annual cycle. |
| `fi-klinik` | none directly. The nearest are **p-0036** and **p-0022**, both hospital-side; Klinik is primary-care intake. |
| `nl-duqu` | none. No record covers SME working capital. |
| `is-50skills` | none directly. **p-0009** (employment-card agencies) is the nearest people-paperwork record, with a different buyer. |
| *(not staged)* Tandem Health | **p-0036** (hospital clinical documentation). Blocked on the `se` prefix, COVERAGE GAP 5. |

### New problem candidates for the register

**None recommended from this pass.** All five checks came back *taken*, and a taken check is the opposite
of a new problem. Two leads are recorded so they are not lost:

1. **The operating layer for household heat pumps**, from the `de-galvany` check. Czech installers sell the
   box and the subsidy paperwork (Woltair, E.ON, AC Heating's NZÚ service), and Nano Energies sells the
   spot tariff. No Czech seller turned up that *runs* a household heat pump and battery against the spot
   price as a service. **Gap check so far:** the three Czech queries on `de-galvany`, plus the ARES
   searches for Woltair, AC Heating, Nano Energies and E.ON. **Positive control:** the same query method
   surfaced AC Heating s.r.o. (IČO 29156203), and ARES `Wultra` passed. **Why it is not a candidate yet:**
   no query was aimed at the operating layer alone, and the loss is a household's power bill, not a
   documented Czech pain. It needs a dedicated query set (e.g. "řízení tepelného čerpadla podle spotové
   ceny služba", "chytré řízení TČ a baterie dynamický tarif domácnost") and a sourced Czech cost before it
   could carry a record.
2. **Know-Your-Agent verification** (signteq). This has no Czech check yet, because the round is not
   receipted and was not staged. It is a `legal-compliance` lead for a later pass.

### PASS SUMMARY

```
feed:               arb-scan (evidence_type funded), attended, 2026-09-28 (weekly delta)
checklist sources:  1 of 1 walked (THE CATEGORY-ROTATION DUTY); 12 of 12 categories named; 4 of 4 owed
                    categories swept (energy, fintech, health incl. the Klinik debt, b2b); 7 funding
                    listings visited and named (tech.eu RSS + round-up, EU-Startups RSS, Sifted RSS,
                    Vestbee /insights + sitemap, trendingtopics for signteq)
records staged:     5 — de-galvany (energy), fi-klinik (health), de-mika + nl-duqu (fintech),
                    is-50skills (b2b); all CZ verdicts 'taken', controls passed; dry run +5, 0 refused
coverage gaps:      7 named — tech.eu Monday recap not yet out; EU-Startups articles now Cloudflare-403;
                    Vestbee sitemap stale (use /insights); Sifted articles 403 (Humanos); no 'se' prefix
                    (Tandem Health unstaged); zod not run directly; incumbents' 2nd limb unreceipted
rotation state:     energy, fintech, health, b2b now 2026-09-28; next: other, mobility, housing,
                    environment (2026-09-19), then govtech, education, legal-compliance, retail (2026-09-21)
```



# Model passes and append — 2026-09-28 (scripted feeds)

`ingest.sh` exited **0** (every feed met its contract, run fully audited). It staged 4,404 records
after `seen.txt` dedup (11,390 already known) and planned 90 pass-A batches for the subagent driver.

- **Pass A** (scale, recurrence, sector, geo_origin; plus pain / stated_need / urgency where asked):
  90 batches graded by 10 coordinating subagents (Sonnet), several of which fanned out to their own
  per-batch subagents. `apply A`: **4,230 filled, 174 refused by the pain bar, 0 rejected**.
  Grader notes worth keeping: TED single-buyer tenders graded scale 0 by rule; YC cards with no
  `all_locations` were given geo `US` (an inference from YC's base, not a card fact — flagged);
  the hackathon theme posts were graded `stated_need: false` (open topics) and NEN-PTK
  consultations mostly `true`; every `event_date_in_past` TED deadline graded urgency 0, one
  signed VeKLEP decree graded 3.
- **Materiality**: 3,335 dropped (338 new to `dropped-log.jsonl`, 2,997 re-drops).
- **Pass B** (title, summary) on 829 survivors: 17 batches, 4 subagents. `apply B`: 788 filled,
  **41 rejected** (summaries over the 2-sentence cap — abbreviations like "s.r.o. " split
  sentences). One retry batch of 41, one sentence each: 41 filled, 0 rejected.
- **Appended** (`--complete --allow-incomplete`, run date 2026-09-28): **895** records —
  tenders 802, funded 69, regulation 12, asks 9, demand 3. **174 remain staged** (pain bar refused,
  by design; not appended, not in seen.txt). Identity-key dedup on the second append skipped the
  854 already-appended rows correctly; no ledger line was duplicated (tenders file: 762 + 40 = 802).
- `db.py upsert` run on all five ledgers; `db.py fetchlog` +17 rows.

Health (`data/feed_health.json`): **LIVE 21 · PENDING 6 · STALE 1 · BROKEN 0**. STALE is `sukl`
(15 aggregates fetched, 0 kept — the snapshot's aggregates were already known). No
`ok=1 items_kept=0` silence on a signal feed. Partial: `hackathon` (hackjakbrno failed its
section guard; upol returned 5 bare titles, kept 0). `coi` skipped (no completed half-year),
`mpsv` skipped (2026-08 already ingested, and no transport receipt — status left blank on purpose).
The scripted `nku` feed ran for the first time since 2026-09-08: 128 fetched, 126 kept for scoring.
