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


# SWEEP — VeKLEP problem statements, 2026-09-28 (owner decision 15)

## SWEEP — VeKLEP RIA backfill (2026-09-28, owner-approved)

**Topic:** read the state's own problem statements ("Definice problému", RIA, důvodová zpráva) in the VeKLEP drafts that no pass had ever read. Operating files: `pipeline/SWEEP.md`, the reg-scan item 4 duty in `pipeline/SCANS.md`, and the dropped-log duty in `pipeline/INGEST.md` 3c. This sweep does NOT advance any rotation or checklist, and it touched no problem file. It wrote ONLY `data/raw/2026-09-28/sweep-veklep/`, which holds `pages/` (the documents), `staged.jsonl` and this file. Nothing under `data/signals/**` changed, and `git status data/signals` is clean after the dry run. There was no real `--complete`, no `db.py` call and no git operation.

### Scope, measured

- **Ledger:** `data/signals/regulation/*.jsonl` holds 256 veklep lines: 198 in `2026-08-25.jsonl`, 21 in 09-02, 4 in 09-08, 26 in 09-19 and 7 in 09-28. Every id was grepped against every committed manifest (`data/raw/*/manifest.md`) and every `docs/weekly/*.md`.
  - All veklep lines after 2026-08-25 had their documents read before: on 09-03 (the 09-02 table), 09-18, 09-19, 09-21 and 09-28.
  - The unread set is **the 198 lines of the 2026-08-25 backfill.** Ten of those ids appear in some manifest, but only as coverage mentions or "card already in corpus", never as a RIA read.
- **Dropped log:** `data/signals/dropped-log.jsonl` has 11 veklep lines. All 11 had their documents read on 2026-09-21 or 2026-09-28, per those days' manifests. **0 re-staged by hand**: no dropped document says more than what those passes already turned into records.
- **Status-changed:** the 13 materials the reg-scan pass listed as changed since 19 Sep were re-checked against the live ODok material pages. See part G.

### Counts

| | |
|---|---|
| backfill lines triaged by title | **198 / 198** (full table in the appendix) |
| selected for reading (buyer impact first) | 64 backfill materials, plus the 13 status-changed materials checked |
| **materials actually read** | **69**: 64 backfill + 5 status-changed with a new DZ or material. 4 status-changed had no new document; 1 (KORNDXWQDTHG) was already read on 09-28; 3 overlap with the backfill reading set |
| documents downloaded and converted | 82 DZ/RIA/material documents across those materials (`pages/*.docx|doc|pdf` + `.txt`), plus 9 live material pages and 1 psp.cz history page |
| verdict STAGE by the reading agents | 31 |
| **staged** | **18** (13 held back under the coordinator rulings, see below) |
| quotes verified (literal substring of the whitespace-collapsed saved page, ≤300 chars) | 31 / 31 candidates; 18 / 18 staged |
| e-mail/phone regex on `staged.jsonl` | 0 matches |

### How it ran

1. **Metadata:** the newest copy of each material came from the scripted feed's committed-era payloads (`data/raw/*/veklep-p*.json` in the main checkout, read-only; 324 materials, latest 2026-09-21). The 2026-09-28 payload is **not on disk** in either checkout; only `manifest.md` exists under `data/raw/2026-09-28/`.
2. **Documents:** for each material the newest `Závěrečná zpráva RIA` and the newest `Důvodová zpráva` were fetched. For MPs' bills, which have neither, the newest `Materiál`/`Předkládací zpráva` was fetched instead. URLs are the `odok.cz/portal/services/download/attachment/<ID>/` form, fetched with `curl -L --http1.1` and a descriptive UA carrying no personal data. ODok's "Empty reply from server" happened repeatedly; every file succeeded on retry (up to 6×). Some batches re-fetched downloads that had arrived truncated. **Re-checked:** every document has a non-empty `.txt`. The one sub-3 kB text is `zp_ALBSDS9BKZY8.txt`, a genuinely one-page předkládací zpráva whose content was verified. Conversion used `textutil` for doc/docx and `pdftotext -layout` for PDF.
3. **Reading** ran in 7 thematic batches (A cyber/digital, B health/social, C energy/environment, D labour/business, E towns/building/transport, F education/misc, G misc + status-changed). The per-material findings JSON (problem, numbers, duty-bearer, dates, corpus dedup, verdict) was kept in the session scratchpad and summarised in the table below.
4. **Coordinator rulings applied:**
   - (1) One record per instrument: where a reg- signal already holds the same Czech instrument, no new signal was minted and the new numbers are listed here for MATCH.
   - (2) The 270 staff / 244M CZK counselling figure is counted once, on `reg-spz-normativy-170-2026`.
   - (3) The withdrawn ZZVZ review draft is listed as a finding, not staged. CONVENTIONS has no rule admitting a skartováno draft as a regulation trigger, and its proposed effect date (2026-07-01) has lapsed.
   - (4) Urgency follows the INGEST rubric, with urgency 0 for drafts whose proposed effect date has lapsed.

### Staged: 18 records (`staged.jsonl`)

All records share these fields and properties:
- `source: reg-scan`, `evidence_type: regulation`, `extraction: manual`, `geo_origin: CZ`, `_needs: []`, `money_eur: null`.
- `url` = the ODok attachment URL of the document the quote was taken from.
- `notes` open with `SWEEP 2026-09-28 … card veklep-<PID>` and a `STATUS:` line.
- None of the ids is in `seen.txt`.

| id | veklep | date | sc/m/u/r | why it clears the bar |
|---|---|---|---|---|
| `reg-cra-cz-notifikovane-osoby-2027` | ALBSDVJAZ93T | 2027-12-11 | 2/0/2/3 | **0 notified CRA conformity bodies in CZ or the EU**; 1–2 applicants expected; ČOI supervises ~98 % of products |
| `reg-eidas2-cz-prijimani-penezenky-2026` | ALBSDHZA32NV | 2026-12-24 | 2/0/2/3 | wallet acceptance by public bodies 24 Dec 2026 and by AML-obliged firms 24 Dec 2027. Integration costs 100–300k CZK per town office, 250–500k CZK per kraj; central build 97–155M CZK |
| `reg-tisnova-linka-rtt-2027` | KORNDSNGW4RC | 2027-06-28 | 0/1/2/2 | 112/150 must take real-time text by 28 Jun 2027; ~19.5M CZK a year requested (one buyer, HZS) |
| `reg-gdpr-stiznosti-uoou-2027` | KORNDUBE2G4D | 2027-04-03 | 2/0/2/3 | GDPR complaints **680 → 2,500+ (+270 %) in a year**, many AI-generated; abusive for-profit DSARs hit SMEs |
| `reg-ezadanka-elektronicka-dokumentace-2027` | ALBSDVLDLD32 | 2027-07-01 | 3/0/2/3 | eŽádanka compulsory for every provider 1 Jul 2027 (labs 2028); electronic health documentation compulsory 1 Jan 2029; 100m requests a year; state cost 2.4bn CZK to 2031 |
| `reg-sujb-rentgeny-vymena-2028` | KORNDN5BG3OC | 2028-01-01 | 2/0/**0**/1 | obsolete medical X-ray sources banned: the worst by 1 Jan 2028, the rest by 2030. Urgency 0 under ruling 4 (the draft's effect date of 2026-02-01 has lapsed; Sbírka not verified) |
| `reg-jmhz-rizikove-prace-2027` | ALBSDRVH64TT | 2027-01-01 | 2/0/2/3 | every employer with category-3/4 risk work reports shifts monthly via JMHZ; fine up to 100k CZK |
| `reg-prispevek-na-peci-prevod-ussz-2028` | ALBSDS9BKZY8 | 2028-06-01 | 2/0/1/1 | **enacted as 92/2026 Sb.** (psp.cz tisk 125, saved). The care-allowance handover moves to June 2028 because the MPSV IT was not ready |
| `reg-eru-vyuctovani-pristupne-2028` | KORNDSYHSVS2 | 2028-01-01 | 2/0/**0**/3 | energy bills must be tagged PDF/UA with a QR code from 1 Jan 2028; the DZ says no accessibility standard for bills exists today (urgency 0 under ruling 4) |
| `reg-zaruky-puvodu-mesicni-2027` | KORNDVKEAY33 | 2027-01-01 | 1/0/2/3 | monthly guarantee-of-origin matching from 1 Jan 2027; renewable credits for charge-point operators need OTE registration within 60 days |
| `reg-ied2-cz-chovy-povoleni-2029` | KORNDQQFC3B1 | 2029-01-01 | 2/1/1/3 | **lower hundreds** of pig and poultry farms newly need integrated permits; e-permitting from 2029; EMS by 1 Jul 2030 |
| `reg-platformova-prace-cz-2027` | KORNDSJJKRYG | 2027-01-01 | 1/0/2/3 | the standalone CZ act (reg-platform-work holds only the EU directive date); up to **546,000** platform workers, 80–90 % OSVČ; 55–118k CZK year-1 admin cost per platform |
| `reg-chraneny-trh-prispevky-2027` | KORNDW3FR25W | 2027-01-01 | 1/0/2/2 | **3,912 employers and 79,922 disabled staff** file ~3,900 claims a quarter against 13.5bn CZK; sworn declarations and ex-post audits from 2027 |
| `reg-registrace-vozidel-online-2027` | KORNDQLEC77O | 2027-07-01 | 2/0/2/3 | **~2m registration visits a year** at 206 ORP offices; burden 2.4bn CZK a year; online registration from 1 Jul 2027 |
| `reg-bim-verejni-stavebnici-2027` | KORNDR6J5588 | 2027-01-01 | 2/0/2/3 | public builders (kraje etc.) must keep IFC models in a compliant CDE from 1 Jan 2027 (the DZ gives no figures) |
| `reg-dobijeci-body-parkoviste-2027` | ALBSDJ5DKVKK | 2027-01-01 | 2/0/**0**/2 | 1 charging point per 10 car spaces in existing non-residential buildings with more than 20 spaces by 1 Jan 2027. Urgency 0 under ruling 4, but **the duty date sits in § 167 of the enacted building act**, so MATCH should re-read that |
| `reg-registry-ve-vzdelavani-2028` | KORNDADEAZ7K | 2028-09-01 | 2/1/1/3 | **8,530 school directorates** must automate individual pupil/teacher data feeds; 170.6M CZK budgeted to founders; 1,394 private/church schools 27.9M CZK |
| `reg-spz-normativy-170-2026` | KORNDS3SSYSD | 2027-01-01 | 2/1/**3**/3 | **enacted as 170/2026 Sb.**, in force 1 Jan 2027: per-client national normatives for counselling centres; 1.24bn CZK in 2025; **+270 staff ≈ 244M CZK** (counted here only) |

### Dry run (validation only)

```
cp -R data/signals $TMPDIR/sweep-veklep-sim/
python3 scripts/normalize.py --raw data/raw/2026-09-28/sweep-veklep --complete --dry-run --today 2026-09-28 \
    --out-dir $TMPDIR/sweep-veklep-sim/signals --seen $TMPDIR/sweep-veklep-sim/signals/seen.txt \
    --dropped-log $TMPDIR/sweep-veklep-sim/signals/dropped-log.jsonl
normalize --complete --dry-run: would append 18 records across 1 file(s); 0 dropped by materiality; 0 incomplete; 0 refused by AC-GDPR1.
  .../sweep-veklep-sim/signals/regulation/2026-09-28.jsonl: +18
  dedup by identity key (append): 0 skipped
  AC-GDPR1 allowlist: dropped 36 non-allowlisted field(s) across 18 record(s): _needs, evidence_type
```
**Owed to the coordinator:** the real `python3 scripts/normalize.py --raw data/raw/2026-09-28/sweep-veklep --complete` and the `db.py upsert` line it prints.

### Held back: STAGE-grade findings not minted (coordinator rulings)

| veklep | why not staged | what the document adds (for MATCH / for the existing record) |
|---|---|---|
| KORNDRFM95MG (EET 2.0 RIA) | ruling 1: already `reg-eet2-2027` + `reg-mf-eet2-2027`; no third EET signal | **~600,000 businesses** in scope (RIA calls it a very rough estimate, assuming ~40 % take in-person payments); +14.4bn CZK a year of revenue; Finanční správa ~500M CZK set-up |
| KORNDUVFCEIZ (teaching assistants) | ruling 1: `reg-skolsky-asistenti` is the same instrument. The veklep card is in `seen.txt`, so re-staging it is impossible | AP FTE 5,946 (2016) → 17,096 (2025), +13.1 % a year; SEN pupils in mainstream 61,042 → 157,311; 18,514.66 AP FTE funded costing 9.826bn CZK; PHAmax cuts ~3,000 FTE; effect **1 Sep 2027**. The 270/244M counselling figure is not repeated here (ruling 2) |
| KORNDLSJSEUC (CZ AI act) | ruling 1: `reg-ai-act-cz-dozor` is the same bill (from an MPO press release) | 207,056,767 CZK state build-out 2026–28 (ČTÚ 112.4M); 41 FTE; authority designation deadline of 2 Aug 2025 missed |
| KORNDVXD6FLN (e-gov internal administration) | ruling 1: `reg-vnitrni-sprava-egov` | up to 17 % of adults digitally excluded; assisted filing 12 min / 90 CZK per filing; effect 1 Jul 2027 |
| KORNDTFAAQBP (air-quality recast) | ruling 1: `reg-ovzdusi-aaqd-2026` | 163 mil. EUR extra investment to 2030; **no municipality has ever issued a smog regulation order**; household heating is the main source |
| KORNDSJHRRGS (pay transparency) | ruling 1: `reg-pay-transparency-cz` | 15 % of firms track gender pay gaps; employer cost 197.9M–2,256.5M CZK; **first report for 150+ employers "do 31. března 2028"** (DZ line 855) — see p-0018 |
| KORNDQ6FEQB9 (Foreigners Act) | ruling 1: `reg-cizinecky-zakon-2029` | ~634,000 residence applications a year; **up to a third decided late**; up to 40 % of applications filed abroad incomplete; effect 2029 |
| KORNDDVFVG8B (CCD2) | ruling 1: `reg-ccd2-bnpl-2026` (the MF transposition) | statutory **cost cap** (coefficient 4 × (REPO + 8 pp), floor 48 %); ~380bn CZK book; RIA effect "11/2026" against the MF press release's 1 Feb 2027 |
| KORNDQ2H6JVT (CI resilience decree 122/2026) | ruling 1: adds only the state's cost figure to `reg-cer-zakon-266` | new measures cost "jednotky či nižší desítky milionů korun" per entity; plans due 9 months, incident reporting 10 months after designation |
| ALBSD65EF6FP (ZZVZ review, **skartováno**) | ruling 3: withdrawn draft with a lapsed effect date; CONVENTIONS has no rule admitting it as a trigger | the best-quantified procurement problem in the set: ÚOHS review takes ~5 months (+~50 % with appeal); 45 % of first-instance decisions appealed; ~200 decisions a year on live tenders; **~80bn CZK of contracts a year frozen in review**. **Finding / new-problem candidate** (contracting-authority review risk) |
| KORNDK9DFTG2 (ITS / bus-stop data) | ruling 4: proposed effect 1 Jul 2026 lapsed and enactment not verified → urgency 0; with scale 1 / money 0 it would drop on materiality, so not staged | road owners in 10 urban nodes supply stop and accessibility data from 31 Dec 2026, nationwide 31 Dec 2028 (EU-fixed dates) |
| KORNDHLAQEDY (metering decree) | ruling 4: draft effect 2026-08-01 lapsed → urgency 0 → drops at scale 1 | the **1 Jul 2027 smart-meter roll-out** for sites above 6 MWh a year; the DSO reading centres are not yet working, so a stop-gap estimate is allowed to 30 Jun 2027. The roll-out date is in the decree in force, so a later pass could stage it on that |
| ALBSDUUFQ5OR (pharmacy vaccination) | no date: the DZ says "as soon as possible" (a regulation record needs a date) | 659,286 reimbursed flu vaccinations in 2025 (398M CZK); pharmacists, dentists and other doctors may vaccinate adults |

### Findings per existing problem (for MATCH; nothing was edited)

- **p-0004** (family caregiver benefit): `reg-prispevek-na-peci-prevod-ussz-2028`. The care-allowance administration handover is postponed to 1 Jun 2028 (92/2026 Sb.) because the IT was not ready.
- **p-0008** (NIS2 / CI capacity), four items:
  - KORNDQ2H6JVT (122/2026 Sb.): per-entity cost "jednotky či nižší desítky milionů Kč"; 9- and 10-month clocks from designation.
  - KORNDHKBKWJY: significance thresholds, e.g. 1,500 district-heating offtake points.
  - KORNDTUBDJRM: the new DZ of 23 Sep adds a 6M CZK MV portal.
  - KORNDW7JRL1U: CI entities may stop drones, unquantified.
  - Not staged: overlap with `reg-cer-zakon-266`.
- **p-0009** (employment card automation): new Foreigners Act (KORNDQ6FEQB9). ~634k applications a year; up to 1/3 decided late; up to 40 % of applications filed abroad incomplete, often for missing employer ("garant") documents; effect 2029. Held on `reg-cizinecky-zakon-2029`.
- **p-0016** (CRA, rejected): `reg-cra-cz-notifikovane-osoby-2027` reopens a different angle: 0 notified conformity bodies and 1–2 expected applicants.
- **p-0017** (EUDI wallet): `reg-eidas2-cz-prijimani-penezenky-2026`. Acceptance by public bodies 24 Dec 2026 and by AML-obliged firms (banks, lenders, insurers, notaries, estate agents) 24 Dec 2027. Private costs 5–15k CZK per verification point; municipal integration 100–300k CZK per office.
- **p-0018** (pay transparency):
  - **Date conflict:** p-0018 (brief, S1 and the `reg-pay-transparency-cz` notes) says the first reports for 150+ employers are due **30 Apr 2028**, from a law-firm reading. The ministry's own DZ (KORNDSJHRRGS, `zd_KORNDVYHMQIC.txt` line 855) says "Pro zaměstnavatele se 150 a více zaměstnanci je první vypracování zpráv stanoveno do 31. března 2028". Line 843 speaks of "do 31. března, potažmo 30. dubna": 31 March for preparing the report, and 30 April is the date for security forces sending their reports to MPSV (line 672).
  - The primary source therefore supports **31 Mar 2028** for employers, and p-0018 should cite it.
  - Also from the same DZ: 15 % of firms track the gap; employer cost 197.9M–2,256.5M CZK; 100–149 employers first report by 31 Mar 2031.
  - KORNDWGLMTLV (NV to JMHZ) is the vehicle that carries the pay-transparency data fields, so p-0018's "a different obligation" wording is inaccurate.
- **p-0020** (accessibility enforcement): `reg-eru-vyuctovani-pristupne-2028` (energy bills PDF/UA + QR) and `reg-tisnova-linka-rtt-2027` (112 real-time text) are two dated accessibility duties outside e-shops.
- **p-0022 / p-0036** (hospital eHealth, clinical documentation): `reg-ezadanka-elektronicka-dokumentace-2027`. The national mandates are eŽádanka on 1 Jul 2027 and all electronic documentation on 1 Jan 2029. The DZ admits provider costs "cannot be quantified" and a heavier burden on small ambulatory providers.
- **p-0024 / p-0025** (EPBD retrofit):
  - `reg-dobijeci-body-parkoviste-2027`: EV charging retrofit, statutory 1 Jan 2027.
  - KORNDTFAAQBP: 163 mil. EUR to meet the 2030 air limits, aimed at household boilers. Held on `reg-ovzdusi-aaqd-2026`.
- **p-0027 / p-0044** (consumer credit):
  - CCD2 (KORNDDVFVG8B): a national cost cap (coefficient = 4 × (REPO + 8 pp), never below 48 %); a book of ~380bn CZK; the RIA says no statistics exist on how many retailers come into scope.
  - **Effect-date conflict:** RIA "11/2026" against the 2027-02-01 cited in p-0044.
  - Not staged: held on `reg-ccd2-bnpl-2026`.
- **p-0034** (AI Act): the CZ adaptation bill costs the state build-out at 207M CZK for 2026–28; the designation deadline of 2 Aug 2025 was missed. Held on `reg-ai-act-cz-dozor`.
- **p-0042** (special-needs assessment backlog):
  - `reg-spz-normativy-170-2026` (enacted: centre funding by per-client normatives from 1 Jan 2027, +270 staff ≈ 244M CZK).
  - KORNDUVFCEIZ: teaching assistants move to PHAmax on **1 Sep 2027**, ending the ŠPZ recommendation as the route to an AP. p-0042's "no dated rule forces action" is contradicted. Held on `reg-skolsky-asistenti`.
  - `reg-registry-ve-vzdelavani-2028`: pupil registers are meant to target SEN support.
- **p-0050** (grant-recipient clawbacks):
  - `reg-chraneny-trh-prispevky-2027`: sheltered-employment subsidies move to sworn declarations checked ex post. 3,912 employers, 13.5bn CZK a year; 179 inspections in Q1 2026 with findings mostly ex post.
  - KORNDT7CHVOE (housing-support annual statements with repayment by 31 May): weak.
- **p-0001** (energy community billing):
  - KORNDSYHQEBY is already held as `reg-eru-sdileni-132-2026`. Its 1 Jan 2027 tariff change (reserved input + max demand) could be added there.
  - KORNDSQHZCUW's DZ notes widespread resale of electricity to end users causing disputes, unquantified.
- **p-0011** (home care agency ops): KORNDSFK3SWC (505/2006) defines the new optional health-care tasks. Already p-0011's S5; no numbers.
- **p-0006** (weak): ALBSDNCJXJV7. The beneficial-owner register becomes non-public by law; 45M CZK ESM rewrite, already contracted (`hlidac-36765458`).
- **Existing records whose notes the new DZs would enrich** (append-only, so this is for MATCH/errata, not edits):
  - `reg-lex-kratom-2027` (KORNDVEC8EF8 DZ of 7 Sep: the KORUND inspection found 63 % of ~1,000 outlets in breach; 129 new outlet permits in H1 2026).
  - `reg-katastr-omezeni-dat` (80M CZK IS; geometric-plan fee 100 → 500 CZK).
  - `reg-omnibus-i-2026-470` (KORNDTDKSPAP: the CZ sustainability-report duty falls from ~2,000 to ~96 entities; only ~25 reported for 2024).
  - `reg-platform-work` (its note says transposition via a zákoník práce amendment; it is a standalone act).
  - `reg-rud-bytova-vystavba-2028` (KORNDXQH9BRI): the government's draft opinion (for 5 Oct 2026) is NEGATIVE, citing 8.1–9.9bn CZK a year.

### New-problem candidates (for MATCH; a sweep creates none)

1. **Procurement-review delay**: ALBSD65EF6FP (withdrawn) RIA. ~80bn CZK of contracts a year frozen in ÚOHS review, ~5 months per case. Buyers: contracting authorities, towns, hospitals. It is a finding only, so it needs a second stream (e.g. ÚOHS statistics as a demand record) before MATCH.
2. **GDPR complaint and abusive-DSAR flood**: `reg-gdpr-stiznosti-uoou-2027` (+270 %, AI-generated complaints, for-profit access/erasure claims against SMEs).
3. **Vehicle registration without a visit**: `reg-registrace-vozidel-online-2027` (~2m visits a year; fleets, dealers and leasing firms are the private buyers).
4. **School information systems → state registers**: `reg-registry-ve-vzdelavani-2028` (8,530 directorates, 20k CZK each, budgeted).
5. **CRA conformity-assessment bottleneck**: `reg-cra-cz-notifikovane-osoby-2027`.
6. **Livestock IPPC permit wave**: `reg-ied2-cz-chovy-povoleni-2029`.
7. **Public-client BIM/CDE**: `reg-bim-verejni-stavebnici-2027`. The corpus already holds CDE market consultations (TSK Praha, Dukovany II) and kraj CDE tenders, so the demand leg exists.
8. **Platform-work compliance**: `reg-platformova-prace-cz-2027`.
9. **Weaker candidates:**
   - energy-bill accessibility, `reg-eru-vyuctovani-pristupne-2028`;
   - GoO monthly matching / charge-point credits, `reg-zaruky-puvodu-mesicni-2027`;
   - JMHZ risk-work reporting, `reg-jmhz-rizikove-prace-2027`, a payroll-software field;
   - radiology source replacement, `reg-sujb-rentgeny-vymena-2028`;
   - pharmacy vaccination service (ALBSDUUFQ5OR, undated).

### What is still unread (named coverage gaps)

- **51 MPs' and Senate bills** in the backfill (54 minus the 3 read). VeKLEP holds only the government's opinion for them; their DZ lives in the sněmovní tisk on psp.cz, which this sweep did not walk. A future pass owes at least the tax, social-insurance and education ones: tisky 244, 109, 112, 133 and the two ZZVZ/ÚOHS reform bills.
- **80 government materials set aside by title** (reasons in the appendix). The **deferred** ones are worth a later read:
  - pension-savings DPS KORNDUPEVPB2 (R3);
  - capital market KORNDMUGLUEK (R3);
  - insurance KORNDW8JASV8 (R2);
  - ČT/ČRo funding KORNDT4HPGKS (R2);
  - chemicals KORNDLS9CWIW;
  - IMERA ALBSDMJFC24N;
  - budget-reporting KORNDUGC5X4Q;
  - statistical survey programme KORNDW8FR8J1;
  - toy safety KORNDUVBWQN4;
  - distance-contract model form KORNDP3EGBS2;
  - railway code KORNDP9GS5QY;
  - vet flexibility KORNDL7GA5X3;
  - the fuel-price regulation act KORNDT4CKC7A;
  - public-budgets package KORNDQGFVQKI;
  - civil procedure ALBSDLNEPCL2;
  - state social support ALBSDRZHK5X1;
  - competition office ALBSDSKF7WP8;
  - FDI screening KORNDTDJHSJC;
  - maturita/admissions KORNDRSLZN5H.
- **Enactment not verified** for several drafts whose status is "B - signováno" (EET 2.0, ITS, vehicle registration, eIDAS 2, platform work, pay transparency). Only 92/2026 (tisk 125) and 170/2026 were confirmed today.
- **ALBSDXRFYLM6** has no entry in the pre-09-21 payloads, so its attachment list could not be diffed. No attachment is dated after 9 Sep.
- **The 2026-09-28 raw payloads are missing on disk** (`veklep-p*.json`, top-level `staged.jsonl`, `regulation/pages`), so this sweep's metadata stops at the 2026-09-21 payload.

### 5-line sweep summary

```
topic:              VeKLEP RIA backfill — the state's own problem statements in 198 never-read drafts (+11 dropped-log lines, +13 status-changed)
records staged:     regulation 18 (reg-scan); funded 0 / tenders 0 / demand 0 — out of scope for this sweep by design
appended after mat.: dry run +18, 0 dropped, 0 incomplete, 0 refused (real --complete owed to the coordinator)
absence checks:     none claimed (no arb records); dedup greps per record in notes
coverage gaps:      51 MPs'/Senate bills (psp.cz tisk not walked); 80 title-set-aside incl. 19 deferred; enactment unverified for 6 signed bills; 09-28 payloads missing on disk
```

### Documents read (every material, in batch order)

| # | veklep id | material (DZ/RIA read) | the state's own problem statement | numbers | verdict |
|---|---|---|---|---|---|
| 1 | `KORNDHKBKWJY` | NV o základních službách a kritériích významnosti (zákon o KI) — zd_KORNDVYHQ364.docx | Implements § 10(2) of CER Act 266/2025: lists essential services and parametric significance thresholds so providers can self-assess whether they are critical-infrastructure entities; replaces NV 432/2010. | district heating threshold: 1,500 offtake points (aimed at outages hitting 50,000+ inhabitants) | NO RECORD: parametric decree; DZ states no economic/financial impact and no costs, only thresholds |
| 2 | `KORNDQ2H6JVT` | Vyhláška o plánu odolnosti, posouzení rizik a hlášení incidentu (subjekty KI) — zd_KORNDVCCU4OP.docx | Act 266/2025 (in force 19 Aug 2025) cannot be applied without this decree setting the content of CI entities' resilience plans, risk assessments, resilience measures and incident reporting (incident = 35% significance threshold). | average cost of new resilience measures per CI entity: 'jednotky či nižší desítky milionů korun' (single to low tens of millions CZK); incident threshold: 35% significance-of-impact level; planning documentation due within 9 months, incident reporting within 1 | Not staged (coordinator ruling, see "Held back") |
| 3 | `ALBSDVJAZ93T` | Zákon o kybernetické bezpečnosti výrobků s digitálními prvky (adaptace CRA) — zd_ALBSDVJAZ93T.docx | CRA (Reg. 2024/2847) needs national market-surveillance and notifying authorities; the state has never supervised product cybersecurity, does not know how many CZ manufacturers or products are in scope, and no conformity-assessment body is yet notified in CZ o | notified conformity-assessment bodies in CZ: 0 (none notified at EU level either); realistic estimate 1–2 applicants; ~98% of products with digital elements fall under ČOI supervision; NÚKIB +5 staff, 8,500,000 CZK/yr; ČOI +10 staff, 12,500,000 CZK/yr; ČBÚ +1  | **STAGED `reg-cra-cz-notifikovane-osoby-2027`** |
| 4 | `KORNDLSJSEUC` | Zákon o umělé inteligenci (adaptace AI aktu) — zd_KORNDVDSBF5O.docx | Czechia missed the AI Act's 2 Aug 2025 deadline to designate authorities; the bill names ČTÚ (main market surveillance), ÚOOÚ, ČNB, ÚNMZ, ČAS and a notified body, and MPO costs the enforcement build-out at 207M CZK for 2026–2028; risk of EU infringement if del | state funding need 2026–2028: 207,056,767 CZK (2026: 61,097,649; 2027: 55,916,559; 2028: 90,042,559); ČTÚ 112,362,000 CZK over 2026–2028; ≥24 FTE needed for supervision; 41 FTE total across bodies; notified body 20,350,000 CZK; conformity verification per AI a | Not staged (coordinator ruling, see "Held back") |
| 5 | `ALBSDHZA32NV` | Novela zákonů 297/2016 a 250/2017 (eIDAS 2 / EUDI peněženka) — zd_ALBSDNLEMC53.docx | eIDAS 2 obliges Czechia to provide an EU Digital Identity Wallet from 24 Dec 2026 and public bodies plus AML-obliged private entities to accept it; DIA's EY-based estimate costs the central build and every ministry, kraj and town's integration. | central state investment first 2 years: 97–155M CZK; operations 5 years: 110–220M CZK; one-off integration: central bodies 200–300k CZK each (31 ministries/offices ≈ 7.8M CZK), krajské úřady 250–500k CZK each (14 ≈ 4.2M CZK), obecní úřady 100–300k CZK each; 66 | **STAGED `reg-eidas2-cz-prijimani-penezenky-2026`** |
| 6 | `KORNDVXD6FLN` | Zákon o další elektronizaci postupů na úseku vnitřní správy — ria_KORNDVXD6FLN.docx, zd_KORNDVXD6FLN.doc | Czech law has no general basis for automated administrative acts without an official, for video hearings, or for assisted digital filing; up to 17% of adults are digitally excluded (PAQ 2024) and have no legal alternative to help them file digitally. | up to 17% of Czech adults digitally excluded (PAQ Research 2024, cited by RIA); assisted filing in MPSV agendas: avg 12 minutes, 90 CZK excl. VAT per filing; video-hearing kit per authority: tens of thousands to hundreds of thousands CZK/yr (not quantified ove | Not staged (coordinator ruling, see "Held back") |
| 7 | `KORNDW7JRL1U` | Zákon o odolnosti subjektů KI proti bezpilotním systémům — zd_KORNDW7JRL1U.docx | Repeated drone overflights of Czech critical-infrastructure sites go unanswered: police reaction time is too slow and CI entities lack legal authority to intervene; the bill lets CI entities stop drones in designated zones under documented procedures. | none | NO RECORD: no numbers (incident counts and costs unquantified; state budget impact 'minimal', CI costs private and not prescribed); an enabling power, not a dated duty |
| 8 | `KORNDSNGW4RC` | Vyhláška o požadavcích na formu a způsob tísňové komunikace (112/150/158) — zd_KORNDWDJR72A.docx | The European Accessibility Act requires emergency number 112 to accept real-time text (synchronised voice and text) by 28 Jun 2027; Czech emergency centres (HZS ČR runs one system for 112 and 150) must add it, costing ~19.5M CZK/yr more. | operating cost increase ~1.6M CZK/month ≈ 19.5M CZK/yr (market survey); no investment costs assumed yet (depends on government choice: shared platform vs 112-only) | **STAGED `reg-tisnova-linka-rtt-2027`** |
| 9 | `KORNDUBE2G4D` | Novela zákona 110/2019 o zpracování osobních údajů (adaptace GDPR procesního nařízení 2025 — zd_KORNDUBE2G4D.docx | GDPR complaints to ÚOOÚ jumped ~270% from 680 (2024) to 2,500+ (2025), increasingly AI-generated and without evidence, which cannot be decided in the 30/60-day deadlines courts impose; abusive data-subject requests for profit also hit SMEs. The bill adapts EU  | GDPR art. 77 complaints to ÚOOÚ: 680 in 2024 → 2,500+ in 2025 (~+270%); current court-derived decision deadline: 30 / 60 days | **STAGED `reg-gdpr-stiznosti-uoou-2027`** |
| 10 | `ALBSDVLDLD32` | Novela zákona 325/2021 o elektronizaci zdravotnictví (EHDS 1. etapa, povinná eŽádanka, pov — zd_ALBSDVLDLD32.docx | Czechia must stand up EHDS bodies by 26 Mar 2027 and deliver patient-summary/eRecept exchange by 2029; the bill also makes eŽádanka (electronic referral) and electronic health documentation compulsory for every healthcare provider, whose IT, process-migration  | 2,400 mil. CZK: state cost of EHDS implementation to 2031 (table 1: bodies, 450 mil digital-service projects, 470 mil infrastructure, 250 mil interoperability, 300 mil cybersecurity, 100 mil education); 100 mil.: eŽádanky issued per year (excluding internal in | **STAGED `reg-ezadanka-elektronicka-dokumentace-2027`** |
| 11 | `KORNDN5BG3OC` | Vyhláška měnící 422/2016 o radiační ochraně — zd_KORNDQKCK2Y7.docx | Some medical X-ray/ionising-radiation sources still in service now give intolerable patient doses or poor image quality (e.g. film radiography); the decree bans them, with deferred effect so providers can run procurement tenders to replace them. | 'nezanedbatelné procento' (non-negligible share, not quantified) of registered sources in operation fail the new requirements (SÚJB source register); no cost figures; DZ claims no impact on business or budgets | **STAGED `reg-sujb-rentgeny-vymena-2028`** |
| 12 | `KORNDUAER3CU` | Vyhláška měnící 377/2022 (zdravotnické prostředky – hlášení výpadků dodávek) — zd_KORNDVJB4SL2.docx | Implements EU 2024/1860: specifies what manufacturers must tell SÚKL about expected interruptions of medical-device supply (MDCG 2024-16 form fields). | none | NO RECORD: pure EU tidy-up (data fields for an EU duty already in force), no numbers, DZ claims costs covered by existing capacity |
| 13 | `KORNDVL9Q4OE` | Vyhláška měnící 134/1998 (seznam zdravotních výkonů) — zd_KORNDVL9Q4OE.doc | Annual update of the point-value list of reimbursable procedures: 65 new codes, 225 updated, 18 cancelled. | 65 new procedures (19 inpatient); 225 updated procedures; 18 cancelled procedures (-21 to -23 mil. CZK); 249-266 mil. CZK impact on public health insurance in 2027; 88 mil. CZK for TRACP5b lab test at 208,000 tests/yr; overhead minute rates indexed by 2.50 % i | NO RECORD: parametric fee table (annual procedure-list update); numbers are reimbursement cost, not a buyer problem |
| 14 | `KORNDSFK3SWC` | Vyhláška měnící 505/2006 (sociální služby – pomoc při běžných úkonech péče o zdraví, speci — zd_KORNDV48NNPG.docx | Implements act 38/2025: defines the new optional 'help with routine health-care tasks' (oral/topical medicines, stoma/urine bag emptying and changing) for home-care (pečovatelská služba) and personal assistance, and the specialised course (incl. 24 h practical | 24 hours: practical part of the specialised course (half in home nursing care); no cost or headcount figures; DZ: no budget impact | NO RECORD: no numbers; activity is optional, and the substance (new health-care tasks for care services) is already held as p-0011 S5 |
| 15 | `ALBSDUUFQ5OR` | Novela zákona 258/2000 – očkování dospělých farmaceuty, zubními lékaři a lékaři — zd_ALBSDWN9TWGG.docx | Adults can only be vaccinated by a narrow set of clinicians; the bill lets pharmacists, dentists and other licensed doctors indicate and give selected vaccinations (flu, COVID-19) to over-18s after a 5-year-valid course, with mandatory pre-vaccination consulta | 642,172 reimbursed flu vaccinations in 2024 (354.9 mil. CZK); 659,286 reimbursed flu vaccinations in 2025 (398.0 mil. CZK); +10 % scenario: +65,929 vaccinations/yr, +39.8 mil. CZK/yr to 437.8 mil. CZK; 630-780 thousand flu doses/yr; 116 adverse-reaction report | Not staged (coordinator ruling, see "Held back") |
| 16 | `KORNDVAHEWJL` | Novela zákona 373/2011 o specifických zdravotních službách (asistovaná reprodukce, pracovn — zd_KORNDVAHEWJL.docx | Opens assisted reproduction to women without a male partner, aligns gender-change rules with Pl. ÚS 52/23, and relaxes occupational-medicine contracting (category-1/2 work can use the registering GP; merged request/report form). | ART births 3.4 % (2013), 5.5 % (2023), ~6.3 % (2024) of all births; 77.6 thousand births in 2025 vs 111.8 thousand in 2021 (-31 %); TFR 1.28 | NO RECORD: rights/deregulation bill; numbers are demographic context, no cost or duty on a buyer |
| 17 | `ALBSDRVH64TT` | Novela zákona 258/2000 a 323/2025 (výrobky ve styku s pitnou vodou; hlášení rizikových pra — zd_ALBSDTKBEYAT.docx, ma_ALBSDW3H5H6G.docx | Transposes EU drinking-water-contact materials rules (positive lists applicable 31 Dec 2026) and, added at MPSV's request, makes employers report per-employee shifts worked in category-3 and category-4 risk work monthly through JMHZ to the Health Ministry and  | fine up to 100,000 CZK for failing to report risk-work data via JMHZ; fine up to 3,000,000 CZK (user of agency workers failing §40a duties); 2 test labs interested in notification (drinking-water materials); cost to manufacturers 'cannot be estimated' | **STAGED `reg-jmhz-rizikove-prace-2027`** |
| 18 | `ALBSDS9BKZY8` | Poslanecký návrh – odklad převodu příspěvku na péči a dávek OZP z ÚP ČR na ÚSSZ (novela 10 — ma_ALBSDS9BKZY8.pdf, zp_ALBSDS9BKZY8.docx | Moving administration of the care allowance (příspěvek na péči), disability benefits and disability cards from the Labour Office to the social-security offices (ÚSSZ) on 1 Jul 2026 is 'unrealistic': the ministry's information systems are not ready, risking IS  | ~1,353 mobility-allowance payments/month at 2,900 CZK in 2025 (home oxygen/ventilation users); 3,923,700 CZK/month; 47,209,100 CZK/yr (2025); 53,677,500 CZK (2026) and 60,485,100 CZK (2027) projected at +1 %/month recipient growth | **STAGED `reg-prispevek-na-peci-prevod-ussz-2028`** |
| 19 | `KORNDNQKQT1K` | Vyhláška o energetickém auditu a systému hospodaření s energií — zd_KORNDXYLMHGR.docx | Implementing decree replacing vyhláška 140/2021 after Act 406/2000 was amended by 87/2025: audit/EnMS duty now tied to final energy consumption rather than firm size. The DZ states no quantified problem and says the decree imposes no new duties. | 23 611 MWh (85 TJ) per year: threshold for mandatory certified energy management system; 2 778 MWh (10 TJ) per year: threshold for mandatory energy audit | NO RECORD: already held as reg-eed-energy-audits (same 10/85 TJ thresholds and dates); DZ adds no count of affected firms and no costs, and says it creates no new duties |
| 20 | `KORNDHLAQEDY` | Novela vyhlášky 359/2020 Sb., o měření elektřiny — zd_KORNDNQGCCB0.docx | Metering decree amended for Lex OZE III (storage, flexibility, aggregation): sets sub-metering requirements for flexibility providers, and gives DSOs a stop-gap way to estimate substitute data because their smart-meter reading centres are not yet fully working | 6 MWh/year: consumption above which sites must get interval (type C1-C3) smart metering; 2027-07-01: statutory roll-out deadline for those sites; 2027-06-30: end of the temporary substitute-data method for DSOs | Not staged (coordinator ruling, see "Held back") |
| 21 | `KORNDSYHQEBY` | Novela vyhlášky 408/2015 Sb., o Pravidlech trhu s elektřinou — zd_KORNDVKESNBV.docx | ERÚ implements Lex OZE III: the data centre (EDC) takes over accounting for flexibility and storage; sharing groups using iterative allocation grow from 50 to 100 EAN; community groups stay capped at 1000 EAN because EDC still runs as a temporary solution; bal | 50 -> 100 EAN: sharing-group size eligible for the iterative allocation; 1000 EAN: cap on a sharing group (kept after 30.6.2026); 5 iteration rounds allowed for groups with at least 2 consumption EANs; EDC cost increase: ERÚ says it cannot quantify it | NO RECORD: already held as reg-eru-sdileni-132-2026 (same 100-EAN, territorial limits and 2026-08-01 / 2027-01-01 / 2027-07-01 waves); DZ counts no participants and gives |
| 22 | `KORNDSYHSVS2` | Novela vyhlášky 207/2021 Sb., o vyúčtování dodávek energií — zd_KORNDVS9L2SR.docx | Energy bills are not accessible: the state says there is no accessibility standard at all and electronic bills are plain PDFs that screen readers cannot read. The decree requires consumer electricity and gas bills to be tagged PDFs (expected to follow EN 301 5 | 2028-01-01: tagged-PDF and QR-code duty starts; no count of suppliers and no cost figure; DZ only says suppliers will need IT changes | **STAGED `reg-eru-vyuctovani-pristupne-2028`** |
| 23 | `KORNDVKEAY33` | Vyhláška o zárukách původu energie, kreditech pro dobíjecí stanice, emisích SZTE a zbytkov — zd_KORNDVKEAY33.docx | New decree under the POZE act and the Energy Act (87/2025): sets rules for guarantees of origin (GoO), credits for charging-station operators for renewable electricity used in EV charging, district-heating GHG intensity and the residual mix. From 1 January 202 | 270 000 CZK: state cost of sponsored access to ČSN EN 16325 (up to 1000 accesses); 60 days after effect: registration window for charging-station operators to claim credits for Jan 2026 onward; 2027-01-01: monthly GoO matching starts | **STAGED `reg-zaruky-puvodu-mesicni-2027`** |
| 24 | `KORNDSQHZCUW` | Novela energetického zákona 458/2000 Sb. (Lex vodík, transpozice 2024/1788) — zd_KORNDWUBZZX8.docx | Last stage of transposing the gas/hydrogen directive 2024/1788: hydrogen networks regulated, optional state guarantee for hydrogen grid investment (§19ab), gas DSOs must plan decommissioning of network parts 5 years ahead, automatic compensation for missed qua | 12.87 CZK per consumption point per month: 2026 non-network infrastructure charge (fee base being moved); 5 years: advance notice for a gas DSO decommissioning plan; 1 000 000 CZK: maximum fine for the new alternative-fuel offence | NO RECORD: no RIA; DZ explicitly says impacts cannot be quantified; the duties fall on a few network operators, and the only number is the existing 12.87 CZK/month fee. W |
| 25 | `KORNDN3AZ79Q` | Novela zákona o odpadech 541/2020 Sb. (adaptace na nařízení 2024/1157 o přepravě odpadů) — zd_KORNDT6DHXUQ.docx | Adapts the Waste Act to the new EU Waste Shipment Regulation 2024/1157: competences, sanctions, electronic filing through the EU central system (Art. 27). It also scraps regional waste management plans (POH kraje) as needless admin. No RIA. | 30 applications over 10 years: prior-consent facility permits; 81 600 CZK over 10 years: total cost to businesses; 89 040 CZK over 10 years: cost to regional authorities; 755 776 CZK over 10 years (75 578 CZK/yr): MŽP costs removed; ~1.7 mil. CZK per region 20 | NO RECORD: pure EU adaptation; quantified effects are tiny (30 firms and 81,600 CZK over 10 years); the only real change is removing a regional planning duty |
| 26 | `KORNDQQFC3B1` | Novela zákona o integrované prevenci 76/2002 Sb. (transpozice IED 2024/1785) — zd_KORNDWLB3EJF.docx | Transposes IED 2.0 into CZ law (no RIA, pure transposition). Emission limits are to be set at the lowest achievable level rather than the top of the BAT range. Scope widens to mining, batteries and smaller pig/poultry farms (lower hundreds of new farm permits) | lower hundreds of livestock operations (pigs, poultry, mixed): newly subject to integrated permits; tens of installations: newly covered industrial activities; tens to low hundreds of permitting proceedings per year: extra regional workload in transition; tens | **STAGED `reg-ied2-cz-chovy-povoleni-2029`** |
| 27 | `KORNDTFAAQBP` | Novela zákona o ochraně ovzduší 201/2012 Sb. (transpozice AAQD 2024/2881) — zd_ALBSDWLFGBCP.docx | Transposes the recast Ambient Air Quality Directive: stricter limit values bind authorities and permitting from 1 January 2030, with health-damage compensation also from 2030. The DZ names household heating as the largest source of pollution, followed by road  | 163 mil. EUR: one-off additional investment for CZ to meet the stricter limits by 2030 (EC GAINS model, upper estimate); 1.14-3.36 bn EUR per year: net health benefit for CZ; 7-21 EUR of health benefit per 1 EUR invested; tens to hundreds of bn CZK per year: c | Not staged (coordinator ruling, see "Held back") |
| 28 | `KORNDSJJKRYG` | Návrh zákona o platformové práci — ria_ALBSDXJFF29J.docx, zd_ALBSDVYJETRV.docx | Platform work in CZ is unmapped; many platform workers are misclassified as self-employed (OSVČ) and lack minimum wage, sick pay and OSH, while algorithmic management is opaque and SÚIP enforcement capacity is thin. | up to 546,000 people do platform work in CZ (EC 2021 estimate): 139,000 >20 h/week or >half of income, 257,000 regularly but less, 150,000 occasionally; tens to low hundreds of digital labour platforms operate in CZ (Eurostat 2025); ~100 analysed in detail; OS | **STAGED `reg-platformova-prace-cz-2027`** |
| 29 | `KORNDSJHRRGS` | Novela zákoníku práce – transparentnost odměňování (směrnice 2023/970) — zd_KORNDVYHMQIC.docx | Equal-pay rules are hard to enforce because pay systems are opaque; only 15% of Czech firms monitor gender pay gaps on comparable positions and pay-discrimination lawsuits are rare. | 15% of Czech firms track gender pay gaps on comparable positions (MPSV representative survey 2025); employer cost of building/formalising pay systems: 197.9M-2,256.5M CZK total (30/60/90% of employers needing to act x low/mid/high effort); per employer year 1: | Not staged (coordinator ruling, see "Held back") |
| 30 | `KORNDWGLMTLV` | Novela NV 417/2025 Sb. k JMHZ — zd_KORNDWGLMTLV.docx | Parametric update of the JMHZ data sets: adds fields for pay-transparency and platform-work reporting and new data users (SÚIP/OIP, MZd/KHS, MSp). | none | NO RECORD: parametric decree; the DZ says no impact on the state budget or businesses, no numbers. Note for p-0018: this decree is the vehicle that carries the pay-transp |
| 31 | `KORNDQ6FEQB9` | Návrh zákona o vstupu a pobytu cizinců (cizinecký zákon) — zd_KORNDRTGXRRU.docx | Residence-permit handling is paper-based and understaffed: up to a third of in-country applications are decided late, appointment waits run weeks to a month, and up to 40% of applications filed abroad are incomplete, often because employer ('garant') documents | foreign population >1 million, >10% of CZ residents (since 2022); 660,000 with >90-day stay at end of 2021; ~634,000 residence applications a year; 630,000+ further proceedings a year (address/passport changes etc.), ~223,000 of them temporary protection; ~400 | Not staged (coordinator ruling, see "Held back") |
| 32 | `KORNDW3FR25W` | Novela zákona o zaměstnanosti a zákona o integračním sociálním podniku — ria_KORNDW3FR25W.docx, zd_KORNDW3FR25W.docx | The subsidy for employing disabled people on the sheltered labour market (CHTP) is administratively heavy and unpredictable: employers document every extra cost item, regional labour-office branches decide identical costs differently, and payment lags 2-3 mont | 3,912 sheltered-market employers and ~79,922 disabled employees (Q1 2026); ~3,900 subsidy applications a quarter processed by Úřad práce; 13.5bn CZK allocated in 2025, 13.0bn CZK drawn; 179 inspections completed in Q1 2026, key findings mostly ex-post; ~4% of  | **STAGED `reg-chraneny-trh-prispevky-2027`** |
| 33 | `KORNDDVFVG8B` | Novela zákona o spotřebitelském úvěru 257/2016 (CCD2) — ria_KORNDSGAT6IS.docx, zd_KORNDJ9CVTMB.docx | CCD2 pulls interest-free credit, loans under EUR 200, short loans and BNPL into full consumer-credit regulation; the RIA adds a national cost cap and refuses a licensing exemption for retailers who offer their own deferred payment. | outstanding consumer-credit principal ~380bn CZK; banks ~87%, non-banks ~13%; cost cap, loan A (<=6 months and <=20,000 CZK): total cost <= 2,000 CZK flat + amount x coefficient x term; cost cap, loan B: contractual APR <= coefficient; coefficient = 4 x (REPO  | Not staged (coordinator ruling, see "Held back") |
| 34 | `KORNDTDKSPAP` | Novela zákona o účetnictví, o auditorech a zák. 317/2025 (Omnibus I / ESAP) — zd_KORNDV3BD81B.docx | Transposes Omnibus I (Directive 2026/470): sustainability reporting shrinks to entities with >1,000 staff and >EUR 450M (11bn CZK) turnover; opt-out for 2025-2026; third-country reports; asset materiality threshold raised to 100k CZK. | sustainability-report duty falls from ~2,000 estimated entities to ~96; ~25 entities produced a 2024 sustainability report; about half expected to opt out for 2025-2026; threshold 450M EUR = 11,000,000,000 CZK turnover and >1,000 staff; long-term asset thresho | NO RECORD: an EU deregulation tidy-up that removes duties. Useful numbers (duty falls from ~2,000 to ~96 entities; only ~25 reported for 2024) belong as a note on reg-omn |
| 35 | `KORNDPLHESJU` | Novela občanského zákoníku – odpovědnost za vadné výrobky (směrnice 2024/2853) — zd_KORNDWNCB531.docx | Transposes the new Product Liability Directive into §§ 2939-2943 of the Civil Code: software and AI systems become products under strict liability, and the burden of proof is eased. | none | NO RECORD: pure transposition with no RIA and no numbers; the DZ only says impact on business is possible. The 9 Dec 2026 date is already held in reg-pld-software-liabili |
| 36 | `ALBSDDEJ5C5N` | Návrh zákona o ekodesignu výrobků — zd_ALBSDM9A62N9.docx | National adaptation law for ESPR (2024/1781): names market-surveillance bodies, the notifying authority and penalties. | fine up to 10,000,000 CZK for failing to publish data on discarded unsold goods | NO RECORD: adaptation and enforcement law; the DZ says business impact is 'only marginal' and gives no counts or costs. The duties are already held in reg-espr-unsold-goo |
| 37 | `ALBSD65EF6FP` | Novela ZZVZ 134/2016 – zrychlení přezkumu zakázek u ÚOHS — ria_ALBSDDYMQREV.docx, zd_ALBSDDYMQREV.docx | Review of public-procurement decisions before ÚOHS is slow and unpredictable (a rare two-stage administrative review plus courts, up to five steps), so contracting authorities pick the least challengeable method (lowest price) rather than best value, and proje | ~990 bn CZK/yr public purchasing (~15 % of GDP, per national procurement strategy); ~200 ÚOHS decisions/yr on bids against live tender procedures; 45 % of first-instance decisions appealed (rozklad) in 2022; 12 % of proposals returned to first instance (ping-p | Not staged (coordinator ruling, see "Held back") |
| 38 | `KORNDS9FFBNF` | Novela zákona 13/1997 – zrušení valorizace dálniční známky a osvobození EV — ria_KORNDVHHKSNX.docx, zd_KORNDU8E6WS2.docx | Automatic CPI/network-length indexation raises the e-vignette price every year regardless of road quality; the bill freezes rates and ends EV exemption and hybrid/CNG discounts. | -488 m CZK SFDI revenue in 2027, -739 m CZK in 2028; ~9.2 bn CZK expected vignette revenue 2026 (DZ: ~8.7 bn); +140 CZK (2025) and +130 CZK (2026) annual vignette increases from indexation | NO RECORD: fee-rate policy (vignette indexation repeal); no duty on buyers; already held as reg-dalnicni-znamka-valorizace |
| 39 | `KORNDQLEC77O` | Novela zákona 56/2001 – digitalizace registrace vozidel, Euro 7, nesilniční stroje — ria_KORNDX9FJCDB.docx, zd_KORNDTY8XVWJ.docx | Vehicle registration still needs an in-person visit to one of 206 ORP registration offices (paying fees, returning plates/certificates, collecting documents) even when filed online; the bill moves it to Portál dopravy with pickup-box delivery and automated der | ~2 million registration transactions/yr at registration offices (2025); 1 223 130 vehicle sales/transfers, 278 581 data changes, 154 668 deregistrations, 197 689 end-of-life records, 97 689 lost/stolen plates (2025); 206 registration offices (ORP); ~2.4 bn CZK | **STAGED `reg-registrace-vozidel-online-2027`** |
| 40 | `KORNDR6J5588` | Vyhláška k zákonu 330/2025 – informační model stavby a CDE — zd_KORNDXKDYPLV.docx | Implements Act 330/2025: obliged public builders must create a building information model (IFC-based, per ÚNMZ data standard) and keep it in a common data environment with API export, tamper-proof transaction logs and role-based access, from 1 Jan 2027. | No figures; DZ says all impacts were assessed in the act's RIA and the decree adds none | **STAGED `reg-bim-verejni-stavebnici-2027`** |
| 41 | `ALBSDJ5DKVKK` | Novela vyhlášky 146/2024 o požadavcích na výstavbu – EPBD: nabíjení a kola — zd_ALBSDNQDEFM9.docx | Transposes EPBD 2024/1275 art. 14: new and renovated buildings need bike parking and EV charging points/ducting, and existing non-residential heated/cooled buildings with >20 car spaces must have at least 1 charging point per 10 spaces or ducting for 50 % of s | ~110 000 CZK per dwelling for two bike spaces incl. one with charger cabling (strictest variant); 1 charging point per 10 car spaces or ducting for 50 % of spaces; threshold: non-residential buildings with >20 car spaces | **STAGED `reg-dobijeci-body-parkoviste-2027`** |
| 42 | `KORNDX5MJKKB` | Novela vyhlášky 130/2024 o stanovení obecních stavebních úřadů — zd_KORNDX5MJKKB.docx | Redraws building-office districts at towns' request (third amendment): 40 municipalities move between offices; some small offices are abolished. | 40 municipalities move between building-office districts; 594 municipal building offices remain | NO RECORD: reorganisation of building-office districts; no costs, no duty on buyers |
| 43 | `ALBSDPLDDVNJ` | Novela zákona o podpoře bydlení 175/2025 – odklad účinnosti — zd_ALBSDPLDDVNJ.docx | Technical deferral: postpones part three of the housing-support act by 2 months and suspends kraj/ORP administrative proceedings and mandatory contributions until 31 Aug 2026, pending a substantive rewrite. | RIA cost of the act: 0.79 bn CZK year 1 (refined to 605 m), 1.07 bn year 2, 1.45 bn CZK from year 3; ~600 m CZK of 2026 state spending deferred; 2026 costs: 348 m CZK ORP housing contact points, 52 m CZK kraje, 12 m CZK ministry staff; 208 pages of methodology | NO RECORD: technical deferral whose transition ended 2026-08-31; no new duty |
| 44 | `KORNDT7CHVOE` | Vyhláška o náležitostech vyúčtování příspěvků podle zákona o podpoře bydlení — zd_KORNDWGBJKPE.docx | Sets the form of the annual statement that housing-support providers file with the kraj (or MMR/MPSV) for five contribution types, with separate accounting and repayment of unused amounts. | No counts of providers or amounts | NO RECORD: reporting-form decree; the duty comes from act 175/2025 §99; no numbers; the scheme is under political rewrite |
| 45 | `KORNDK9DFTG2` | Novela zákona o silničním provozu 361/2000 – transpozice směrnice ITS 2023/2661 — zd_KORNDMYFEGS5.docx | Transposes the revised ITS directive: road owners, car-park owners, urban-rail, port and airport operators must feed ŘSD/MD machine-readable data (traffic signs, parking, stops and their accessibility) for a national access point, phased over 27 data categorie | 27 data categories due by 31 Dec 2025/2026/2027/2028; 10 urban nodes first (Brno, České Budějovice, Hradec Králové, Liberec, Olomouc, Ostrava, Pardubice, Plzeň, Praha, Ústí nad Labem); ~150 m CZK/yr NDIC operating cost, up to 30 m CZK/yr upgrades; ~25 m CZK in | Not staged (coordinator ruling, see "Held back") |
| 46 | `KORNDADEAZ7K` | Zákon o registrech ve vzdělávání — ria_KORNDUXEDCPC.docx, zd_KORNDTTLELGM.docx | MŠMT says it lacks individual, current data on pupils and teachers (no unique IDs, only aggregated returns hand-checked at obec/kraj/ministry level), so it cannot target SEN support, model teacher shortages or meet EU statistical duties; the bill creates pupil | 8,530 school directorates (ředitelství) run by obce/kraje/svazky obcí must automate data transfer to the registers — 170.6M CZK at ~20,000 CZK each, paid from municipal/regional budgets; 1,394 private and church school legal entities — 27.88M CZK (20,000 CZK e | **STAGED `reg-registry-ve-vzdelavani-2028`** |
| 47 | `KORNDUVFCEIZ` | Novela školského zákona 561/2004 — institucionalizace asistentů pedagoga (PHAmax) — ria_KORNDXGEUQVB.docx, zd_KORNDXGEUQVB.docx | Teaching assistants are granted per pupil only on a counselling-centre (ŠPZ) recommendation, so AP posts grow 13.1%/yr, are unstable and unevenly spread, schools are pushed to 'label' pupils with diagnoses, and schools and ŠPZ are buried in paperwork; the bill | AP posts in mainstream primary schools: 5,946 FTE (2016) -> 17,096 FTE (2025); +13.1%/yr average; pupils with special educational needs in mainstream primary classes: 61,042 (2016) -> 157,311 (2025), +19.7% in 2025 alone; 18,514.66 AP FTE funded as support mea | Not staged (coordinator ruling, see "Held back") |
| 48 | `KORNDS3SSYSD` | Novela vyhlášky 72/2005 — poradenské služby, financování ŠPZ (vyhl. 170/2026 Sb.) — zd_KORNDXJDYQKE.docx | Kraje set counselling-centre (PPP/SPC) budgets by inconsistent regional normatives, producing large gaps in clients per specialist between regions; from 1 Jan 2027 the state funds centres by national per-client normatives split by difficulty (with/without a re | 1.24bn CZK paid to kraj/obec-run ŠPZ for pedagogical work in 2025; average ŠPZ pedagogical salary 53,247 CZK/month (2025); +270 ŠPZ pedagogical staff funded in 2027 vs 2025 = ~244M CZK; private ŠPZ received ~105M CZK and church ŠPZ ~26M CZK in 2025; ~20% of ŠP | **STAGED `reg-spz-normativy-170-2026`** |
| 49 | `KORNDVYSHWKK` | NV o standardech pro akreditace ve vysokém školství — zd_KORNDVYSHWKK.docx | Replaces NV 274/2016 accreditation standards for universities and study programmes at the request of the National Accreditation Bureau; RIA exempted (18 May 2026). | none | NO RECORD: standards rewrite with RIA exemption; DZ states no budget or business impact and gives no numbers |
| 50 | `KORNDSNHG8PC` | Novela vyhlášky 377/2013 o skladování a používání hnojiv — zd_KORNDVXAXRAZ.docx | Aligns the decree with the amended fertiliser act, adds stability criteria and application rules for stable compost (may be left unincorporated in standing crops), updates fertiliser-use record fields. | none | NO RECORD: parametric decree; DZ states no budget or business impact and gives no numbers |
| 51 | `KORNDM2F6FC0` | Novela katastrálního zákona 256/2013 — zd_KORNDVCF7SWJ.docx | Cadastre data (names, rights, prices) are mined and misused in bulk; the bill releases non-personal data as open data, restricts personal/price data to identified requesters with a logged purpose, forces e-filing of vklad via data box/portal, and raises fines. | 80M CZK cadastre IS changes; ~25M CZK/yr saved on mailing 'zaplombování' notices; ~60M CZK/yr extra fee revenue (geometric-plan confirmation fee 100 -> 500 CZK); fines raised to 100,000 CZK (natural persons) and 1,000,000 CZK (businesses) for the graver offenc | NO RECORD: already held as reg-katastr-omezeni-dat with the same date; DZ numbers are state-side (80M IS, fee revenue), no count of affected users or filings — could enri |
| 52 | `KORNDR9CY314` | Novela zákona o regulaci reklamy 40/1995 (léčiva, zdravotnické prostředky) — ria_KORNDS99N8WT.doc, zd_KORNDR9CY314.docx | The broad definition of advertising stops anyone but the treating doctor giving patients information on medicines and medical devices, and over-regulates advertising of prescription-only devices; the bill loosens rules and allows electronic mandatory informati | none | NO RECORD: deregulation; the RIA contains no numbers at all (no budget impact, no counts) |
| 53 | `KORNDRFM95MG` | Zákon o evidenci tržeb (EET 2.0) — ria_KORNDTTHXQ5R.docx, zd_KORNDT5HZ4QQ.docx | Concealed revenues, including new cashless channels (digital wallets, payment gateways, private Revolut/PayPal accounts), escape taxation and disadvantage honest firms; EET 2.0 obliges businesses taking in-person payments to register sales online from 1 Jan 20 | ~600,000 businesses expected to fall under registration (assumes ~40% take in-person payments; RIA calls it a very rough estimate); ~5,000 CZK tax credit per self-employed person registering sales; +14.4bn CZK/yr tax revenue at full run (4.3bn CZK to municipal | Not staged (coordinator ruling, see "Held back") |
| 54 | `ALBSDVJCUTRW` | Poslanecký návrh — prodejní doba v maloobchodě 223/2016 (tisk 243) — zp_ALBSDW98VEBE.docx, ma_ALBSDW98VEBE.pdf | MPs want the holiday sales ban for shops over 200 m2 to cover all public holidays and listed other holidays, since the current split confuses consumers, staff and retailers; MF, MPO, MZV, MMR and ÚOHS recommend the government oppose it. | applies to shops with sales area over 200 m2; EU: 12 member states have fully free opening hours (MPO) | NO RECORD: no quantified impacts (MZe notes the DZ does not quantify them); ministries recommend opposing it; not a problem statement |
| 55 | `ALBSDU4DJ2KS` | Poslanecký návrh — zákon o obalech 477/2001 (tisk 193) — zp_ALBSDUMCAZQR.docx, ma_ALBSDUMCAZQR.pdf | Defines the authorised packaging company's take-back service as a service of general economic interest and requires its independence from waste firms: shareholder caps of 3% (up to 33% under conditions), at least 34 shareholders, share capital 2M CZK. | shareholder cap 3% (max 33% under conditions); share capital 2,000,000 CZK; 12/18-month compliance windows after effect | NO RECORD: governance/ownership rules for a single organisation; the bill says it has no budget impact and gives no problem numbers |
| 56 | `KORNDVEC8EF8` | Novela zákona o návykových látkách (lex kratom) — zd_KORNDXPB6GFX.docx | Kratom and other psychomodulatory substances are sold widely with poor compliance; the KORUND inspection found violations at 63% of about 1,000 outlets checked, and toxicology centres logged about 350 synthetic-cannabinoid intoxications in H1 2026. | ~1,000 outlets and distribution points inspected in action KORUND; violations at 63% of them; ~900 unlawful acts documented, 373 suspected crimes; ~0.5 million products seized; 17,000+ ordered destroyed; 169 risky internet domains identified; 25 e-shops blocke | NO RECORD: already held as reg-lex-kratom-2027 (same instrument, same dates). The newest DZ (7 Sep) adds numbers the record lacks: KORUND inspection (~1,000 outlets, 63%  |
| 57 | `KORNDX6AEXUS` | NV všeobecný vyměřovací základ 2025 / valorizace důchodů 2027 — zd_KORNDY2HV3SJ.docx | Annual parametric decree setting pension-calculation values for 2027 and the January 2027 pension increase. | VVZ 2025: 48,900 CZK; coefficient 1.0565; reduction thresholds 22,732 / 206,652 CZK; base pension 5,170 CZK; average old-age pension +304 CZK to 22,196 CZK (+1.4%); extra state spend 1.1 bn CZK above the statutory minimum | NO RECORD: parametric annual decree; no buyer or duty |
| 58 | `KORNDWVGVS5J` | Novela NV 55/2024 o nepřijatelnosti žádostí občanů RU/BY na ZÚ — zd_KORNDWVGVS5J.docx | Adds an exception to the inadmissibility of visa applications by Russian and Belarusian citizens: direct relatives of Czech citizens and of Belarusians living long-term in Czechia may apply. | none | NO RECORD: narrow policy exception, no application counts or backlog figures in the DZ |
| 59 | `KORNDS2HT779` | Novela zákona o DPH (ViDA, čl. 2) — zd_KORNDTLAP48E.docx | Transposes article 2 of the EU VAT in the Digital Age directive: OSS clarifications, the platform deemed-supplier rule extended to some B2B buyers, call-off stock abolished from 1 Jul 2028. | no fiscal impact expected (DZ) | NO RECORD: EU transposition tidy-up with no numbers; the substantive ViDA duties (e-reporting 2030, platforms 2028) are deferred to a later amendment |
| 60 | `KORNDQBKNV61` | Ochrana obchodního tajemství (novela několika zákonů) — zd_KORNDVCCH595.docx | Completes transposition of the Trade Secrets Directive: new procedural tools to keep trade secrets confidential in civil proceedings. | none | NO RECORD: procedural EU tidy-up; no numbers, no public-budget or business costs |
| 61 | `ALBSDN3D48DW` | Novela zákona 22/1997 (adaptace CPR-2024 stavební výrobky) — zd_ALBSDU3G7SKT.docx | Removes Construction Products Regulation 305/2011 adaptation provisions from Act 22/1997 as CPR 2024/3110 applies (adaptation moves to Act 90/2016). | no budget impact | NO RECORD: pure adaptation to an EU regulation, no numbers |
| 62 | `KORNDUGFTG75` | Novela občanského zákoníku (MSp) – zájem dítěte, domácí násilí, péče — zd_ALBSDXWCTYQ4.docx | Family-law amendment: defines the child's best interest, requires courts to consider removing parental responsibility after domestic violence, and lets courts leave one parent's share of care unset. | 'zájem dítěte' appears in 32 Civil Code provisions, 6 ZŘS and 11 ZSPOD provisions; no fiscal or business impact | NO RECORD: substantive family law with no numbers and no buyer |
| 63 | `ALBSDNCJXJV7` | Novela zákona 37/2021 o evidenci skutečných majitelů (6. AML směrnice) — zd_KORNDTDAMZP5.docx | The beneficial-ownership register becomes non-public by law (public access only after proving legitimate interest in a new administrative procedure), codifying the de facto closure of 17 Dec 2025; Justice Ministry must rewrite the ESM system. | 45 mil. CZK preliminary cost to rewrite the ESM information system; 3-5 posts for the new legitimate-interest access agenda; BO check of direct shareholders limited to stakes of 5% or more; EU transposition deadline 10 Jul 2026 (legitimate-interest verificatio | NO RECORD: the only hard number (45 mil. CZK ESM rewrite) is already contracted and held as hlidac-36765458 (Asseco ISVR/ESM upgrade, 49.6 mil. CZK, Aug 2026); the privat |
| 64 | `KORNDEBHMA6M` | Zákon o rámci opatření pro výrobu technologií pro nulové čisté emise (NZIA) — zd_KORNDM8H3BQU.docx | Adapts the NZIA regulation: regional authorities (krajské úřady) and DESÚ become single contact points for net-zero manufacturing permits, and MPO approves strategic projects. | 2 DESÚ posts 1,958,072 CZK/yr; 2 MPO posts 1,958,072 CZK/yr; 1 CzechInvest post 840,117 CZK/yr; comparison: 101 contact points in FR, 16 in DE, 9 in AT | NO RECORD: EU adaptation; the only numbers are ~4.8 mil. CZK/yr of state staffing, with no dated duty and no buyer spend |
| 65 | `KORNDXCGU8JB` | Novela zákona 416/2023 o dorovnávacích daních — no new doc | — | none | NO RECORD: no new document, status now 3 - připomínkové řízení ukončeno (attachments identical to 21 Sep; DZ+RIA still 27 Aug) |
| 66 | `KORNDTUBDJRM` | Vyhláška o portálu kritické infrastruktury — zd_KORNDY7BGPAR.docx | — | 6,000,000 CZK portal set-up incl. hardware, 90% EU ISF-funded | NO RECORD: new DZ (23 Sep) read. It quantifies only the state build: 6 mil. CZK for the MV portal and hardware, 90% from the EU Internal Security Fund. The decree takes e |
| 67 | `KORNDXQH9BRI` | Poslanecký návrh – RUD, podíl DPH za dokončené byty (ST 298) — (new) ma_ALBSDY9BAMHA.pdf, up_ALBSDY9BAMHA.docx | — | none | NO RECORD: no new DZ (MPs' bill). The new material is a DRAFT government opinion, NEGATIVE ("nesouhlasné stanovisko"), drafted for the government meeting of 5 Oct 2026. M |
| 68 | `KORNDVTBZKV2` | Vyhláška 254/2015 paušální náhrada nákladů řízení — zd_KORNDY7BMNUK.docx | — | none | NO RECORD: new DZ (23 Sep) read; fee-table decree raising the flat cost refund from 300 to 450 CZK per act from 2027-01-01 (1,701 proceedings under Act 82/1998 in 2024);  |
| 69 | `ALBSDW3HDEWG` | Novela zákona 115/2001 o podpoře sportu — (new) ma_ALBSDY8LNGGS.docx, pd/ob/pz_ALBSDY8LNGGS | — | none | NO RECORD: amended version approved (AS). The Materiál carrying the DZ was read: the Sport Agency's anti-doping body is widened to match-fixing, safeguarding and spectato |
| 70 | `KORNDVYGNA4F` | Vyhláška 418/2003 fondy zdravotních pojišťoven — zd_KORNDY8JKKXS.docx | — | none | NO RECORD: new DZ (24 Sep) read, and its numbers are unchanged: a 0.52 pp cut to the cost limit, about 3 bn CZK saved in 2027, a state transfer of about +21 bn CZK, effec |
| 71 | `ALBSDXRFYLM6` | Úhradová vyhláška 2027 — no new doc | — | none | NO RECORD: no new document, status now 3 - připomínkové řízení ukončeno. All attachments are dated 9 Sep 2026, before 19 Sep. meta.json holds no entry for this PID, so th |
| 72 | `KORNDXAMWBJD` | Novela zákona 18/2004 o uznávání odborné kvalifikace — no new doc | — | none | NO RECORD: no new document, status now 3 - připomínkové řízení ukončeno (attachments identical, 25 Aug) |
| 73 | `KORNDXBH65S3` | Novela vodního zákona (UWWTD) — no new doc | — | none | NO RECORD: no new document, status now 3 - připomínkové řízení ukončeno (attachments identical; DZ+RIA still 27 Aug) |

### Appendix — title triage of all 198 backfill lines

| veklep id | type | title (abridged) | triage |
|---|---|---|---|
| `ALBSDMMJQW2S` | bill | Návrh zákona, kterým se mění zákon č. 159/1999 Sb., o některých podmínkách podnikání a o výkonu některých činn | set aside: tourism act (eTurista) older skartováno version — superseded by ALBSDXWJ7VQX, RIA read 2026-09-28 and held as reg-eturista-registr-ubytovani-2028 |
| `ALBSDPVEP9GE` | MPs' bill | Návrh poslanců Radka Vondráčka, Renaty Vesecké, Libora Vondráčka a Zuzany Ožanové na vydání zákona, kterým se  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDPVEF33B` | MPs' bill | Návrh poslanců Radka Vondráčka, Renaty Vesecké, Libora Vondráčka a Zuzany Ožanové na vydání zákona o právních  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDP9GS5QY` | decree | Vyhláška, kterou se mění vyhláška č. 177/1995 Sb., kterou se vydává stavební a technický řád drah, ve znění po | set aside: railway construction/technical code — niche (SŽ); deferred |
| `ALBSD65EF6FP` | bill | Návrh zákona, kterým se mění zákon č. 134/2016 Sb. o zadávání veřejných zakázek, ve znění pozdějších předpisů, | READ (batch E) → no record |
| `KORNDEBHMA6M` | bill | Návrh zákona o stanovení rámce opatření pro posílení evropského systému výroby technologií pro nulové čisté em | READ (batch G) → no record |
| `ALBSDPHMFNE2` | MPs' bill | Návrh poslanců Olgy Richterové, Ivana Bartoše, Hany Ančincové, Barbory Pipášové, Lenky Martínkové Španihelové, | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDPLDDVNJ` | bill | Návrh zákona, kterým se mění zákon č. 175/2025 Sb., o poskytování některých opatření v podpoře bydlení (zákon  | READ (batch E) → no record |
| `KORNDN5BG3OC` | decree | Vyhláška, kterou se mění vyhláška č. 422/2016 Sb., o radiační ochraně a zabezpečení radionuklidového zdroje  | READ (batch B) → staged `reg-sujb-rentgeny-vymena-2028` |
| `ALBSDQG99B8P` | MPs' bill | Návrh poslance Andreje Babiše na vydání zákona, kterým se mění zákon č. 245/2000 Sb., o státních svátcích, o o | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDPUA7225` | MPs' bill | Návrh poslanců Petra Hladíka, Václava Pláteníka a Gabriely Svárovské na vydání zákona, kterým se mění zákon č. | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDLYCP480` | decree | Vyhláška,  kterou se mění vyhláška č. 518/2004 Sb., kterou se provádí zákon č. 435/2004 Sb., o zaměstnanosti,  | set aside: employment-act implementing decree — technical forms |
| `KORNDHLAQEDY` | decree | Návrh vyhlášky, kterou se mění vyhláška č. 359/2020 Sb., o měření elektřiny, ve znění pozdějších předpisů  | READ (batch C) → no record |
| `KORNDK9DFTG2` | bill | Návrh zákona, kterým se mění zákon č. 361/2000 Sb., o provozu na pozemních komunikacích a o změnách některých  | READ (batch E) → no record |
| `KORNDQGFVQKI` | bill | Návrh zákona, kterým se mění některé zákony v oblasti veřejných rozpočtů | set aside: public-budgets package — deferred (fiscal rules) |
| `KORNDQXBYLEV` | bill | Vládní návrh zákona o státním rozpočtu České republiky na rok 2026 | set aside: 2026 state budget act — budget, not a problem statement |
| `ALBSDQSHVJ5B` | MPs' bill | Návrh poslance Aleše Juchelky na vydání zákona, kterým se mění zákon č. 151/2025 Sb., o dávce státní sociální  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDQSAFLS2` | MPs' bill | Návrh poslance Aleše Juchelky na vydání zákona, kterým se mění zákon č. 110/2006 Sb., o životním a existenčním | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDQLG8UT0` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 304/2014 Sb., o platových poměrech státních zaměstnanců, ve z | set aside: public-sector pay tables — parametric |
| `ALBSDVXBREUW` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 187/2006 Sb., o nemocenském pojištění, ve znění pozdějších předp | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDVYNC777` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 222/2010 Sb., o katalogu prací ve veřejných službách a správě | set aside: public-service work catalogue — parametric job classification |
| `ALBSDVZJCC47` | MPs' bill | Návrh poslanců Jana Bureše, Petra Bendla, Karla Haase, Marka Bendy, Ivana Adamce, Jakuba Jandy, Jana Bauera a  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDVJCXEIV` | MPs' bill | Návrh poslanců Pavly Pivoňka Vaňkové, Věry Kovářové, Jana Papajanovského a Lucie Sedmihradské na vydání zákona | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDVJCUTRW` | MPs' bill | Návrh poslanců Marka Výborného, Petra Hladíka a Františka Talíře na vydání zákona, kterým se mění zákon č. 223 | READ (batch F) → no record |
| `ALBSDVLHFD24` | MPs' bill | Návrh poslankyně Pavly Pivoňka Vaňkové na vydání zákona, kterým se mění zákon č. 586/1992 Sb., o daních z příj | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDVM9NT3Q` | MPs' bill | Návrh poslanců Drahoslava Ryby a Jiřího Bartáka na vydání zákona o standardizaci a o změně některých zákonů (z | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDUVBWQN4` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 86/2011 Sb., o technických požadavcích na hračky, ve znění po | set aside: toy safety NV — EU tidy-up (new Toy Safety Reg. applies directly); deferred |
| `KORNDUGC6N75` | decree | Vyhláška o procentním podílu jednotlivých obcí a krajů na částech celostátního hrubého výnosu daně z přidané h | set aside: municipal/regional tax-share percentages — parametric |
| `KORNDT7CHVOE` | decree | Vyhláška o náležitostech vyúčtování příspěvků podle zákona o podpoře bydlení  | READ (batch E) → no record |
| `KORNDT9BVT1C` | decree | Vyhláška, kterou se mění některé vyhlášky v souvislosti s novelou zákona o investičních společnostech a invest | set aside: decrees following investment-companies act — niche |
| `ALBSDVJAZ93T` | bill | Návrh zákona o požadavcích na kybernetickou bezpečnost výrobků s digitálními prvky a o změně některých souvise | READ (batch A) → staged `reg-cra-cz-notifikovane-osoby-2027` |
| `KORNDSNHG8PC` | decree | Vyhláška, kterou se mění vyhláška č. 377/2013 Sb., o skladování a způsobu používání hnojiv, ve znění pozdějšíc | READ (batch F) → no record |
| `KORNDN3AZ79Q` | bill | Návrh zákona, kterým se mění zákon č. 541/2020 Sb., o odpadech, ve znění pozdějších předpisů, a zákon č. 634/2 | READ (batch C) → no record |
| `KORNDVUF2EMJ` | gov. order | Nařízení vlády o zavedení letního času v letech 2027 až 2031  | set aside: summer time 2027–2031 — parametric |
| `KORNDUAER3CU` | decree | Vyhláška, kterou se mění vyhláška č. 377/2022 Sb., o provedení některých ustanovení zákona o zdravotnických pr | READ (batch B) → no record |
| `KORNDNQKQT1K` | decree | Vyhláška o energetickém auditu a systému hospodaření s energií  | READ (batch C) → no record |
| `KORNDQQFC3B1` | bill | Návrh zákona, kterým se mění zákon č. 76/2002 Sb., o integrované prevenci a omezování znečištění, o integrovan | READ (batch C) → staged `reg-ied2-cz-chovy-povoleni-2029` |
| `ALBSDVLDLD32` | bill | Návrh zákona, kterým se mění zákon č. 325/2021 Sb., o elektronizaci zdravotnictví, ve znění pozdějších předpis | READ (batch B) → staged `reg-ezadanka-elektronicka-dokumentace-2027` |
| `KORNDRGAL6PM` | bill | Návrh zákona, kterým se mění zákon č. 49/1997 Sb., o civilním letectví, ve znění pozdějších předpisů, a zákon  | set aside: civil aviation act — niche; deferred |
| `KORNDTFAAQBP` | bill | Návrh zákona, kterým se mění zákon č. 201/2012 Sb., o ochraně ovzduší, ve znění pozdějších předpisů, a zákon č | READ (batch C) → no record |
| `KORNDS3SSYSD` | decree | Vyhláška, kterou se mění vyhláška č. 72/2005 Sb., o poskytování poradenských služeb ve školách a školských por | READ (batch F) → staged `reg-spz-normativy-170-2026` |
| `KORNDWP9BJGT` | bill | Návrh zákona, kterým se mění zákon č. 367/2021 Sb., o opatřeních k přechodu České republiky k nízkouhlíkové en | set aside: low-carbon transition act (Dukovany II support) — single project |
| `KORNDWTGSB79` | decree | Vyhláška, kterou se mění vyhláška č. 156/2005 Sb., o technických a provozních podmínkách amatérské radiokomuni | set aside: amateur radio conditions — niche |
| `KORNDVYSHWKK` | gov. order | Nařízení vlády o standardech pro akreditace ve vysokém školství  | READ (batch F) → no record |
| `KORNDWUFBTR9` | gov. order | Nařízení vlády o stanovení některých podmínek poskytnutí mimořádné finanční podpory pro zemědělce postižené zv | set aside: one-off farm crisis aid (Middle East) — subsidy condition, one-off |
| `KORNDWVGVS5J` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 55/2024 Sb., o nepřijatelnosti žádostí občanů třetích zemí o  | READ (batch G) → no record |
| `KORNDVXD6FLN` | bill | Návrh zákona, kterým se mění některé zákony v souvislosti s další elektronizací postupů na úseku vnitřní správ | READ (batch A) → no record |
| `ALBSDUUFQ5OR` | bill | Návrh zákona, kterým se mění zákon č. 258/2000 Sb., o ochraně veřejného zdraví a o změně některých související | READ (batch B) → no record |
| `KORNDPLHESJU` | bill | Návrh zákona, kterým se mění zákon č. 89/2012 Sb., občanský zákoník, ve znění pozdějších předpisů. | READ (batch D) → no record |
| `KORNDUGC5X4Q` | decree | Vyhláška, kterou se mění vyhláška č. 5/2014 Sb., o způsobu, termínech a rozsahu údajů předkládaných pro hodnoc | set aside: budget-reporting data for state/municipal budgets — technical reporting format; deferred |
| `KORNDU4FMHER` | decree | Vyhláška, kterou se mění vyhláška č. 522/2006 Sb., o státním odborném dozoru a kontrolách v silniční dopravě,  | set aside: roadside-check risk categories — enacted 168/2026 Sb., read 2026-09-28 via e-Sbírka: re-grades enforcement, no new duty |
| `KORNDTDKSPAP` | bill | Návrh zákona, kterým se mění zákon č. 563/1991 Sb., o účetnictví, ve znění pozdějších předpisů, zákon č. 93/20 | READ (batch D) → no record |
| `KORNDSNGW4RC` | decree | Vyhláška o požadavcích na formu a způsob tísňové komunikace | READ (batch A) → staged `reg-tisnova-linka-rtt-2027` |
| `KORNDW3FR25W` | bill | Návrh zákona, kterým se mění zákon č. 435/2004 Sb., o zaměstnanosti, ve znění pozdějších předpisů, a zákon č.  | READ (batch D) → staged `reg-chraneny-trh-prispevky-2027` |
| `KORNDW8FR8J1` | decree | Vyhláška o Programu statistických zjišťování na rok 2027  | set aside: statistical survey programme 2027 — annual parametric (ČSÚ reporting duty list); deferred |
| `KORNDSQHZCUW` | bill | Návrh zákona, kterým se mění zákon č. 458/2000 Sb., o podmínkách podnikání a o výkonu státní správy v energeti | READ (batch C) → no record |
| `KORNDX4E2C5I` | bill | Návrh zákona, kterým se mění zákon č. 61/2000 Sb., o námořní plavbě, ve znění pozdějších předpisů, a zákon č.  | set aside: maritime navigation act — niche |
| `KORNDX4KBHOV` | bill | Návrh zákona, kterým se mění zákon č. 207/2000 Sb., o ochraně průmyslových vzorů a o změně zákona č. 527/1990  | set aside: industrial designs act (EU design reform) — niche IP |
| `KORNDUPEVPB2` | bill | Návrh zákona, kterým se mění zákon č. 427/2011 Sb., o doplňkovém penzijním spoření, ve znění pozdějších předpi | set aside: pension-savings product rules (DPS); fund managers only, low buyer impact — deferred |
| `KORNDVADGSS4` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 83/2023 Sb., o stanovení podmínek poskytování přímých plateb  | set aside: CAP direct-payment conditions — farm subsidy parameters |
| `KORNDWGLMTLV` | gov. order | Nařízení,  kterým se mění nařízení vlády č. 417/2025 Sb., k provedení zákona o jednotném měsíčním hlášení zamě | READ (batch D) → no record |
| `KORNDW7JRL1U` | bill | Návrh zákona, kterým se mění některé zákony s cílem posílit odolnost subjektů kritické infrastruktury proti be | READ (batch A) → no record |
| `ALBSDX59B8YE` | MPs' bill | Návrh poslanců Karla Havlíčka a Romana Kubíčka na vydání zákona, kterým se mění zákon č. 328/2025 Sb., o výzku | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDX6AEXUS` | gov. order | Nařízení o výši všeobecného vyměřovacího základu za rok 2025, přepočítacího koeficientu pro úpravu všeobecného | READ (batch G) → no record |
| `KORNDX6ALKHS` | gov. order | Nařízení vlády o pravidlech pro organizaci správního úřadu  | set aside: rules for organising a state administrative office — internal |
| `KORNDX5MJKKB` | decree | Vyhláška, kterou se mění vyhláška č. 130/2024 Sb., o stanovení obecních stavebních úřadů, ve znění pozdějších  | READ (batch E) → no record |
| `KORNDSQEFNQH` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 278/2008 Sb., o obsahových náplních jednotlivých živností, ve | set aside: trade-licence content descriptions — parametric list |
| `KORNDQBKNV61` | bill | Návrh zákona, kterým se mění některé zákony v oblasti ochrany obchodního tajemství  | READ (batch G) → no record |
| `KORNDW8JASV8` | bill | Návrh zákona, kterým se mění zákon č. 277/2009 Sb., o pojišťovnictví, ve znění pozdějších předpisů, a další so | set aside: insurance act transposition — insurers only, deferred |
| `KORNDWFEFC5X` | gov. order | Nařízení vlády o výši vyměřovacího základu pro pojistné na veřejné zdravotní pojištění hrazené státem pro rok  | set aside: state-paid health-insurance base 2027 — parametric |
| `ALBSDQDACPI1` | MPs' bill | Návrh poslanců Petra Hladíka, Bohuslava Niemiece, Václava Pláteníka, Moniky Brzeskové, Jany Filipovičové, Mari | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDN6KDHNG` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 140/2023 Sb., o stanovení podmínek provádění opatření agroles | set aside: agroforestry subsidy conditions — farm subsidy parameters |
| `KORNDJUJEVVC` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 73/2023 Sb., o stanovení pravidel podmíněnosti plateb zeměděl | set aside: CAP conditionality — farm subsidy parameters |
| `ALBSDDEJ5C5N` | bill | Návrh zákona o ekodesignu výrobků a o výkonu státní správy v této oblasti, a o změně souvisejících zákonů | READ (batch D) → no record |
| `ALBSDQK9WKJD` | MPs' bill | Návrh poslanců Mariana Jurečky, Moniky Brzeskové, Toma Philippa, Marka Výborného a dalších na vydání zákona, k | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDQKA3C4N` | MPs' bill | Návrh poslanců Petra Hladíka, Bohuslava Niemiece, Václava Pláteníka, Moniky Brzeskové, Jany Filipovičové, Mari | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDRDGW9D3` | MPs' bill | Návrh poslanců Mariana Jurečky, Moniky Brzeskové, Toma Philippa, Benjamina Činčily a dalších na vydání zákona, | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDRFJN7UG` | MPs' bill | Návrh poslankyně Pavly Pivoňka Vaňkové na vydání zákona, kterým se mění zákon č. 117/1995 Sb., o státní sociál | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDQTF86PL` | MPs' bill | Návrh poslanců Benjamina Činčily, Mariana Jurečky, Toma Philippa, Marka Výborného a dalších na vydání zákona,  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDJZJHQ1E` | bill | Návrh zákona, kterým se mění zákon č. 40/2009 Sb., trestní zákoník, ve znění pozdějších předpisů, a další souv | set aside: criminal code — justice, no buyer duty |
| `KORNDNQDXTF0` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 83/2023 Sb., o stanovení podmínek poskytování přímých plateb  | set aside: CAP direct payments — farm subsidy parameters |
| `KORNDRFM95MG` | bill | Návrh zákona o evidenci tržeb a o změně některých dalších zákonů | READ (batch F) → no record |
| `ALBSDRDBL9NP` | MPs' bill | Návrh poslanců Elišky Olšákové, Karla Dvořáka, Lucie Sedmihradské, Julie Smejkalové, Michala Zuny, Jiřího Horá | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDQKJ5MIH` | bill | Návrh zákona, kterým se mění zákon č. 141/1961 Sb., o trestním řízení soudním (trestní řád), ve znění pozdější | set aside: criminal procedure — justice |
| `KORNDR9CY314` | bill | Návrh zákona, kterým se mění zákon č. 40/1995 Sb., o regulaci reklamy a o změně a doplnění zákona č. 468/1991  | READ (batch F) → no record |
| `KORNDS5JEWJO` | MPs' bill | Návrh poslance Aleše Juchelky na vydání zákona, kterým se mění zákon č. 117/1995 Sb., o státní sociální podpoř | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDSB9VZPH` | MPs' bill | Návrh poslanců Martina Kupky, Jana Skopečka, Jiřího Havránka a Vojtěcha Munzara na vydání zákona, kterým se mě | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDPMD76PZ` | bill | Vládní návrh zákona, kterým se mění zákon č. 104/2013 Sb., o mezinárodní justiční spolupráci ve věcech trestní | set aside: international judicial cooperation — justice |
| `ALBSDQCC9S8Z` | bill | návrh zákona, kterým se mění zákon č. 141/1961 Sb., o trestním řízení soudním (trestní řád), ve znění pozdější | set aside: criminal procedure (skartováno) — justice |
| `KORNDSABR468` | decree | Vyhláška o způsobu a termínu oceňování nákladů na zdravotní služby v roce 2026 pro účely přerozdělování pojist | set aside: health-insurance redistribution costing 2026 — parametric |
| `KORNDSNDXQ8B` | gov. order | Nařízení vlády,  kterým se mění nařízení vlády č. 361/2025 Sb., o stanovení částek životního minima a existenč | set aside: subsistence minimum amounts — parametric |
| `ALBSDHZA32NV` | bill | Návrh zákona, kterým se mění zákon č. 297/2016 Sb., o službách vytvářejících důvěru pro elektronické transakce | READ (batch A) → staged `reg-eidas2-cz-prijimani-penezenky-2026` |
| `ALBSDSKF7WP8` | bill | Návrh zákona, kterým se mění některé zákony v oblasti působnosti Úřadu pro ochranu hospodářské soutěže | set aside: competition-office powers — deferred |
| `KORNDRVG2A1L` | decree | Vyhláška o nastavitelných parametrech přerozdělování pojistného na veřejné zdravotní pojištění pro rok 2027 a  | set aside: health-insurance redistribution parameters 2027 — parametric |
| `ALBSDRZHK5X1` | bill | Návrh zákona, kterým se mění zákon č. 117/1995 Sb., o státní sociální podpoře, ve znění pozdějších předpisů | set aside: state social support act — benefit parameters; deferred |
| `KORNDL7GA5X3` | decree | Vyhláška, kterou se mění vyhláška č. 128/2009 Sb., o přizpůsobení veterinárních a hygienických požadavků pro n | set aside: veterinary flexibility for small food businesses — niche; deferred |
| `ALBSDRVHV79Q` | MPs' bill | Návrh poslanců Lucie Sedmihradské, Jana Papajanovského, Věry Kovářové, Matěje Hlavatého, Jakuba Krainera, Pavl | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDLNEPCL2` | bill | Návrh zákona, kterým se mění zákon č. 99/1963 Sb., občanský soudní řád, ve znění pozdějších předpisů, zákon č. | set aside: civil procedure/court fees — justice; deferred |
| `KORNDRVB6L2L` | bill | Návrh zákona, kterým se mění zákon č. 329/1999 Sb., o cestovních dokladech, ve znění pozdějších předpisů, záko | set aside: travel documents / ID cards — state issuance |
| `ALBSDS9BKZY8` | MPs' bill | Návrh poslanců Aleše Juchelky a Jany Pastuchové na vydání zákona, kterým se mění zákon č. 108/2006 Sb., o soci | READ (batch B) → staged `reg-prispevek-na-peci-prevod-ussz-2028` |
| `ALBSDQRAN8WQ` | MPs' bill | Návrh poslanců Olgy Richterové, Ivana Bartoše, Hany Ančincové, Barbory Pipášové, Lenky Martínkové Španihelové, | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDRDGYVNR` | MPs' bill | Návrh poslanců Mariana Jurečky, Moniky Brzeskové, Toma Philippa, Marka Výborného a dalších na vydání zákona, k | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDR99RFB1` | MPs' bill | Návrh poslanců Jana Bureše, Karla Haase, Renáty Zajíčkové, Štěpána Slováka, Petra Sokola, Jany Černochové, Lib | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDR79R7BR` | MPs' bill | Návrh poslance Karla Dvořáka na vydání zákona, kterým se mění zákon č. 340/2015 Sb., o zvláštních podmínkách ú | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDS5AS75T` | MPs' bill | Návrh poslanců Jana Bureše, Martina Baxy, Karla Haase, Renáty Zajíčkové, Štěpána Slováka, Petra Sokola, Jany Č | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDNEF9MK8` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 80/2023 Sb., o stanovení podmínek provádění agroenvironmentál | set aside: agri-environment-climate measures — farm subsidy parameters |
| `KORNDMUGLUEK` | bill | Návrh zákona, kterým se mění zákon č. 256/2004 Sb., o podnikání na kapitálovém trhu, ve znění pozdějších předp | set aside: capital-market act transposition; niche (investment firms), p-0006 adjacent — deferred |
| `KORNDS5FLZJK` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 491/2001 Sb., o volbách do zastupitelstev obcí a o změně některý | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDS8KFDG1` | MPs' bill | Návrh poslance Matěje Ondřeje Havla na vydání ústavního zákona, kterým se mění ústavní zákon č. 1/1993 Sb., Ús | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDS5AUEX1` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 256/2004 Sb., o podnikání na kapitálovém trhu, ve znění pozdější | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDT4CKC7A` | bill | Návrh zákona o regulaci cen pohonných hmot vládou a o změně zákona č. 526/1990 Sb., o cenách, ve znění pozdějš | set aside: act on government fuel-price regulation — the enabling law of the cap series; deferred |
| `ALBSDT7A6K64` | MPs' bill | Návrh poslankyně Zuzany Mrázové na vydání zákona, kterým se mění zákon č. 283/2021 Sb., stavební zákon, ve zně | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDP3EGBS2` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 29/2023 Sb., o vzorovém poučení o právu na odstoupení od smlu | set aside: model withdrawal form for distance contracts — EU tidy-up (p-0028 adjacent, but a template change); deferred |
| `ALBSDSZGD2I7` | MPs' bill | Návrh poslanců Petra Hladíka, Moniky Brzeskové, Jany Filipovičové, Zdeny Kašparové, Marie Krškové, Jany Kruták | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDT8EKD5A` | MPs' bill | Návrh poslanců Olgy Richterové, Ivana Bartoše, Zdeňka Hřiba, Gabriely Svárovské, Venduly Svobodové, Ireny Ferč | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDTDAY5XA` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 13/1997 Sb., o pozemních komunikacích, ve znění pozdějších předp | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDTDHWVRP` | bill | Zákon o Finančním analytickém úřadu  | set aside: Financial Analytical Office act — state organisation |
| `KORNDTDKGHLE` | bill | Návrh zákona, kterým se v souvislosti s přijetím zákona o ekonomické ochraně státu a zákona o Finančním analyt | set aside: companion amendments for FAÚ / economic protection — technical |
| `KORNDMPDBE54` | bill | Návrh zákona, kterým se mění zákon č. 218/2000 Sb., o rozpočtových pravidlech a o změně některých souvisejícíc | set aside: budgetary rules (skartováno) — fiscal |
| `KORNDQ6FEQB9` | bill | Návrh zákona o vstupu a pobytu cizinců (cizinecký zákon) | READ (batch D) → no record |
| `KORNDLS9CWIW` | bill | Návrh zákona, kterým se mění zákon č. 350/2011 Sb., o chemických látkách a chemických směsích a o změně někter | set aside: chemicals act — deferred |
| `ALBSDRMDTWS7` | MPs' bill | Návrh poslanců Andreje Babiše, Taťány Malé, Radka Vondráčka, Heleny Válkové, Borise Šťastného a Radima Fialy n | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDR6J5588` | decree | Vyhláška o provedení některých ustanovení zákona č. 330/2025 Sb. týkajících se správy informací o stavbě | READ (batch E) → staged `reg-bim-verejni-stavebnici-2027` |
| `KORNDNM876XL` | gov. order | Nařízení vlády,  kterým se mění nařízení vlády č. 458/2013 Sb., o seznamu výchozích a pomocných látek a jejich | set aside: lists of addictive substances/precursors — parametric |
| `KORNDS5FFX14` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 95/2004 Sb., o podmínkách získávání a uznávání odborné způsobilo | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDR99UHLJ` | MPs' bill | Návrh poslanců Václava Pláteníka, Jiřího Vojáčka, Mariana Jurečky, Benjamina Činčily, Marie Krškové, Jiřího Ho | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDRUD7WIN` | MPs' bill | Návrh poslanců Aleny Schillerové, Patrika Nachera, Borise Šťastného, Tomia Okamury a Taťány Malé na vydání zák | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDRV9DCVC` | MPs' bill | Návrh poslanců Mariana Jurečky, Moniky Brzeskové, Toma Philippa, Marka Výborného a dalších na vydání zákona, k | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDRV99BCD` | MPs' bill | Návrh poslanců Elišky Olšákové, Karla Dvořáka, Lucie Sedmihradské, Julie Smejkalové, Michala Zuny, Jiřího Horá | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDDVFVG8B` | bill | Návrh zákona, kterým se mění zákon č. 257/2016 Sb., o spotřebitelském úvěru, ve znění pozdějších předpisů, a d | READ (batch D) → no record |
| `KORNDTDJHSJC` | bill | Zákon o ekonomické ochraně státu  | set aside: economic protection of the state (FDI screening) — state organisation; deferred |
| `ALBSDTLBDM98` | MPs' bill | Návrh poslanců Andreje Babiše, Tomia Okamury, Lucie Šafránkové, Petra Macinky, Borise Šťastného, Taťány Malé,  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDTLGYDBL` | bill | Návrh zákona, kterým se mění zákon č. 141/1961 Sb., o trestním řízení soudním (trestní řád), ve znění pozdější | set aside: criminal procedure — justice |
| `KORNDTSAMQVA` | decree | Vyhláška,  kterou se mění vyhláška č. 573/2025 Sb., o změně sazby základní náhrady za používání silničních mot | set aside: travel-allowance fuel prices — parametric (successor KORNDXWQDTHG read 2026-09-28) |
| `KORNDU3AQW1C` | gov. order | Nařízení vlády o cenovém výměru pro regulované pohonné hmoty pro období od 20. května 2026 do 31. května 2026  | set aside: fuel price cap 20–31 May 2026 — expired; cap series held as reg-pohonne-hmoty-strop-2026-10 |
| `ALBSDTUDB51A` | MPs' bill | Návrh poslanců Huberta Langa, Igora Hendrycha, Jiřího Maška a Drahoslava Ryby na vydání zákona, kterým se mění | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDTZDW2VM` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 88/2024 Sb., o správě voleb, ve znění pozdějších předpisů, a něk | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDLMBS4FB` | bill | Vládní návrh zákona, kterým se mění zákon č. 40/2009 Sb., trestní zákoník, ve znění pozdějších předpisů, a dal | set aside: criminal code — justice |
| `KORNDUEE4451` | gov. order | Nařízení vlády, kterým se vydává cenový výměr regulující ceny některých pohonných hmot pro období od 1. června | set aside: fuel price cap June 2026 — expired; cap series held |
| `ALBSDTYB922F` | regional bill | Návrh zastupitelstva hlavního města Prahy na vydání zákona, kterým se mění zákon č. 458/2000 Sb., o podmínkách | set aside: Prague assembly energy-act bill — political proposal, no RIA |
| `KORNDU3EM7M1` | decree | Vyhláška, kterou se mění vyhláška č. 571/2020 Sb., kterou se stanoví poplatky za poskytování a přístup k český | set aside: ČSN standards access fees — fee table |
| `KORNDU7AL36H` | bill | Vládní návrh zákona, kterým se s cílem dále posílit bezpečnost České republiky mění zákony upravující opatření | set aside: Ukraine-conflict security measures — state |
| `ALBSDJ5DKVKK` | decree | Návrh vyhlášky, kterou se mění vyhláška č. 146/2024 Sb., o požadavcích na výstavbu | READ (batch E) → staged `reg-dobijeci-body-parkoviste-2027` |
| `KORNDS2HT779` | bill | Návrh zákona, kterým se mění zákon č. 235/2004 Sb., o dani z přidané hodnoty, ve znění pozdějších předpisů  | READ (batch G) → no record |
| `KORNDRFC4KF4` | gov. order | Návrh nařízení vlády, kterým se mění nařízení vlády č. 481/2012 Sb., o omezení používání některých nebezpečnýc | set aside: RoHS exemptions NV — EU tidy-up |
| `ALBSDTFLRBGA` | bill | Návrh zákona, kterým se mění zákon č. 40/2009 Sb., trestní zákoník, ve znění pozdějších předpisů, a zákon č. 1 | set aside: criminal code/procedure — justice |
| `KORNDTZBUH5R` | bill | Návrh zákona, kterým se mění zákon č. 90/2024 Sb., o zbraních a střelivu, ve znění pozdějších předpisů, zákon  | set aside: weapons and ammunition acts — niche (gun holders/dealers) |
| `KORNDRSLZN5H` | decree | Vyhláška,  kterou se mění vyhláška č. 177/2009 Sb., o bližších podmínkách ukončování vzdělávání ve středních š | set aside: maturita / admissions decrees — exam logistics; deferred |
| `ALBSDMJFC24N` | bill | Vládní návrh zákona o působnosti orgánů státu při řešení mimořádných situací na vnitřním trhu a o změně zákona | set aside: internal-market emergency act (IMERA) — deferred |
| `ALBSDU4DJ2KS` | MPs' bill | Návrh poslankyně Bereniky Peštové na vydání zákona, kterým se mění zákon č. 477/2001 Sb., o obalech a o změně  | READ (batch F) → no record |
| `KORNDSFK3SWC` | decree | Vyhláška,  kterou se mění vyhláška č. 505/2006 Sb., kterou se provádějí některá ustanovení zákona o sociálních | READ (batch B) → no record |
| `KORNDLSJSEUC` | bill | Návrh zákona o umělé inteligenci a o změně některých souvisejících zákonů | READ (batch A) → no record |
| `KORNDUGFTG75` | bill | Návrh zákona, kterým se mění zákon č. 89/2012 Sb., občanský zákoník, ve znění pozdějších předpisů, a některé d | READ (batch G) → no record |
| `KORNDUPSXN21` | decree | Vyhláška, kterou se mění některé vyhlášky o předávání údajů ve vysokém školství  | set aside: higher-education data transfers — technical |
| `KORNDM2F6FC0` | bill | Návrh zákona, kterým se mění zákon č. 256/2013 Sb., o katastru nemovitostí (katastrální zákon), ve znění pozdě | READ (batch F) → no record |
| `KORNDS9FFBNF` | bill | Návrh zákona, kterým se mění zákon č. 13/1997 Sb., o pozemních komunikacích, ve znění pozdějších předpisů | READ (batch E) → no record |
| `KORNDKVG689M` | gov. order | Nařízení vlády,  kterým se mění nařízení vlády č. 462/2000 Sb., k provedení § 27 odst. 8 a § 28 odst. 5 zákona | set aside: crisis-management NV — internal state |
| `KORNDVHE5272` | gov. order | Nařízení vlády,  kterým se vydává cenový výměr regulující ceny některých pohonných hmot pro období od 1. červe | set aside: fuel price cap 1–19 July 2026 — expired; cap series held |
| `ALBSDURFV5B3` | MPs' bill | Návrh poslanců Víta Rakušana, Karla Dvořáka, Pavly Pivoňka Vaňkové, Lukáše Vlčka a Ester Weimerové na vydání ú | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDUAA6SOP` | decree | Vyhláška, kterou se mění vyhláška č. 376/2011 Sb., kterou se provádějí některá ustanovení zákona o veřejném zd | set aside: health-insurance implementing decree — technical |
| `KORNDUNBD4JJ` | bill | Návrh ústavního zákona o celostátním referendu | set aside: constitutional referendum act — political |
| `KORNDQ2H6JVT` | decree | Vyhláška o plánu odolnosti, posouzení rizik, opatřeních k zajištění odolnosti subjektů kritické infrastruktury | READ (batch A) → no record |
| `ALBSDUMBLGK4` | MPs' bill | Návrh poslanců Víta Rakušana, Karla Dvořáka a Lukáše Vlčka na vydání zákona, kterým se mění zákon č. 134/2016  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `ALBSDUF86JWB` | MPs' bill | Návrh poslanců Patrika Nachera, Tomia Okamury, Taťány Malé, Radima Fialy, Filipa Turka, Barbory Rázgy a Martin | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDADEAZ7K` | bill | Návrh zákona o registrech ve vzdělávání a o změně některých souvisejících zákonů | READ (batch F) → staged `reg-registry-ve-vzdelavani-2028` |
| `ALBSDURFRZ8D` | MPs' bill | Návrh poslanců Taťány Malé, Andreje Babiše, Borise Šťastného a Tomia Okamury na vydání zákona, kterým se mění  | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDSJH9NLM` | gov. order | Nařízení vlády, kterým se mění nařízení vlády č. 243/2013 Sb., o investování investičních fondů a o technikách | set aside: investment-fund investing rules — niche (fund managers) |
| `KORNDT4HPGKS` | bill | Návrh zákona, kterým se mění zákon č. 483/1991 Sb., o České televizi, ve znění pozdějších předpisů, a zákon č. | set aside: public-broadcaster funding reform — political, no buyer duty on businesses beyond fee collection; deferred |
| `KORNDUBE2G4D` | bill | Návrh zákona, kterým se mění zákon č. 110/2019 Sb., o zpracování osobních údajů | READ (batch A) → staged `reg-gdpr-stiznosti-uoou-2027` |
| `KORNDV49P63X` | decree | Vyhláška, kterou se mění vyhláška č. 388/2011 Sb., o provedení některých ustanovení zákona o poskytování dávek | set aside: disability-benefit implementing decree — technical |
| `KORNDUMG5472` | decree | Vyhláška, kterou se mění vyhláška č. 117/2025 Sb., kterou se mění vyhláška č. 72/2022 Sb., o zajištění přiměře | set aside: adequacy of RES operating support — niche (supported generators) |
| `ALBSDUA9YZOL` | bill | Vládní návrh zákona, kterým se mění zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní pojištění, ve zněn | set aside: health-insurance premiums act — parametric |
| `ALBSDUMB6SCH` | MPs' bill | Návrh poslanců Štěpána Slováka, Martina Kupky, Karla Haase, Renáty Zajíčkové, Zdenky Crkvenjaš Němečkové, Petr | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDSYHQEBY` | decree | Vyhláška, kterou se mění vyhláška č. 408/2015 Sb., o Pravidlech trhu s elektřinou, ve znění pozdějších předpis | READ (batch C) → no record |
| `KORNDSYHSVS2` | decree | Vyhláška,  kterou se mění vyhláška č. 207/2021 Sb., o vyúčtování dodávek a souvisejících služeb v energetickýc | READ (batch C) → staged `reg-eru-vyuctovani-pristupne-2028` |
| `KORNDTYJFZ0I` | decree | Vyhláška,  kterou se mění vyhláška č. 412/2021 Sb., o rozpočtové skladbě, ve znění pozdějších předpisů | set aside: budget classification — technical |
| `KORNDUVFCEIZ` | bill | Návrh zákona, kterým se mění zákon č. 561/2004 Sb., o předškolním, základním, středním, vyšším odborném a jiné | READ (batch F) → no record |
| `KORNDV4MNCNT` | gov. order | Nařízení vlády o koeficientu pro výpočet minimální mzdy v roce 2027 a 2028  | set aside: minimum-wage coefficient — already held as reg-min-mzda-koeficient-2027-2028 |
| `KORNDSJHRRGS` | bill | Návrh zákona, kterým se mění zákon č. 262/2006 Sb., zákoník práce, ve znění pozdějších předpisů, a některé dal | READ (batch D) → no record |
| `KORNDHKBKWJY` | gov. order | Nařízení vlády o základních službách a kritériích významnosti | READ (batch A) → no record |
| `KORNDSJJKRYG` | bill | Návrh zákona o platformové práci | READ (batch D) → staged `reg-platformova-prace-cz-2027` |
| `ALBSDNCJXJV7` | bill | Návrh zákona, kterým se mění zákon č. 37/2021 Sb., o evidenci skutečných majitelů, ve znění pozdějších předpis | READ (batch G) → no record |
| `KORNDV6G82YO` | bill | Návrh zákona o ozdravných postupech a řešení krize v pojišťovnictví a o změně souvisejících zákonů (zákon o oz | set aside: insurance recovery/resolution (IRRD) — insurers + ČNB, niche |
| `KORNDVEC8EF8` | bill | Návrh zákona, kterým se mění zákon č. 167/1998 Sb., o návykových látkách a o změně některých dalších zákonů, v | READ (batch G) → no record |
| `ALBSDVB9VVIG` | MPs' bill | Návrh poslanců Andreje Babiše a Roberta Plagy na vydání zákona, kterým se mění zákon č. 561/2004 Sb., o předšk | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDVL9Q4OE` | decree | Návrh vyhlášky, kterou se mění vyhláška č. 134/1998 Sb., kterou se vydává seznam zdravotních výkonů s bodovými | READ (batch B) → no record |
| `KORNDVKEAY33` | decree | Vyhláška o zárukách původu energie, kreditech pro dobíjecí stanice, způsobu stanovení emisí skleníkových plynů | READ (batch C) → staged `reg-zaruky-puvodu-mesicni-2027` |
| `ALBSDVDFXP4J` | Senate bill | Senátní návrh zákona, kterým se mění zákon č. 245/2000 Sb., o státních svátcích, o ostatních svátcích, o význa | set aside: MPs'/Senate bill — VeKLEP holds only the government's opinion, no RIA; DZ lives in the sněmovní tisk |
| `KORNDVLDAK4V` | decree | Vyhláška, kterou se mění některé vyhlášky v oblasti účetního výkaznictví státu  | set aside: state accounting reports — technical |
| `KORNDVTGXD9X` | bill | Návrh zákona o evropských průkazech pro osoby se zdravotním postižením a o změně zákona č. 329/2011 Sb., o pos | set aside: EU disability/parking cards — benefit administration, niche |
| `KORNDVTH9H6F` | bill | Návrh zákona, kterým se mění některé zákony v souvislosti s přijetím zákona o evropských průkazech pro osoby s | set aside: companion amendments to EU disability-card act — technical |
| `ALBSDN3D48DW` | bill | Návrh zákona, kterým se mění zákon č. 22/1997 Sb., o technických požadavcích na výrobky a o změně a doplnění n | READ (batch G) → no record |
| `ALBSDRVH64TT` | bill | Návrh zákona, kterým se mění zákon č. 258/2000 Sb., o ochraně veřejného zdraví a o změně některých související | READ (batch B) → staged `reg-jmhz-rizikove-prace-2027` |
| `KORNDVAHEWJL` | bill | Návrh zákona, kterým se mění zákon č. 373/2011 Sb., o specifických zdravotních službách, ve znění pozdějších p | READ (batch B) → no record |
| `KORNDR6DHQT0` | bill | Návrh zákona, kterým se mění zákon č. 359/1992 Sb., o zeměměřických a katastrálních orgánech, ve znění pozdějš | set aside: survey and cadastral authorities act — state organisation |
| `KORNDSZH7EOD` | bill | Návrh zákona, kterým se mění zákon č. 155/1995 Sb., o důchodovém pojištění, ve znění pozdějších předpisů, a da | set aside: pension insurance parameters — state benefit, no buyer duty |
| `KORNDSNE78UH` | decree | Vyhláška, kterou se mění vyhláška č. 275/1998 Sb., o agrochemickém zkoušení zemědělských půd a zjišťování půdn | set aside: agrochemical soil testing — niche |
| `KORNDQLEC77O` | bill | Návrh zákona, kterým se mění zákon č. 56/2001 Sb., o podmínkách provozu vozidel na pozemních komunikacích, ve  | READ (batch E) → staged `reg-registrace-vozidel-online-2027` |
