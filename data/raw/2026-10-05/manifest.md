# run manifest — 2026-10-05

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-10-05`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-05T0703 | ted | ok | 200 | 62730086 | 7625 | 56876 | 2026-10-05T07:03:23Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | hlidac | ok | 200 | 2119066 | 822 | 13161 | 2026-10-05T07:04:28Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | veklep | ok | 200 | 1946918 | 151 | 4470 | 2026-10-05T07:06:26Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | tacr | ok | 200 | 264246 | 14 | 1352 | 2026-10-05T07:06:50Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | hackathon | ok | 200 | 4962051 | 14 | 10288 | 2026-10-05T07:06:53Z | data/raw/2026-10-05 | partial: hackjakbrno:mode-a upol:yield-zero |
| 2026-10-05T0703 | nen-ptk | ok | 200 | 48307792 | 142 | 331996 | 2026-10-05T07:07:04Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | edesky | skipped | 000 | 0 | 0 | 0 | 2026-10-05T08:09:58Z |  | registry status=planned |
| 2026-10-05T0703 | cc-cz | ok | 200 | 18599 |  | 478 | 2026-10-05T08:09:58Z | data/raw/2026-10-05/feed-czechcrunch.xml |  |
| 2026-10-05T0703 | yc-oss | ok | 200 | 10542143 |  | 3191 | 2026-10-05T08:09:59Z | data/raw/2026-10-05/yc-all.json |  |
| 2026-10-05T0703 | vestbee | ok | 200 | 1089240 | 61 | 1232 | 2026-10-05T08:10:02Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | suggest | ok | 200 | 11897 | 42 | 24487 | 2026-10-05T08:11:14Z | data/raw/2026-10-05/suggest-pain.jsonl |  |
| 2026-10-05T0703 | reddit-new | ok | 200 | 185628 | 100 | 1401 | 2026-10-05T08:15:23Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | reddit-search | ok | 200 | 329839 | 100 | 1694 | 2026-10-05T08:15:23Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | nku | ok | 200 | 78251 | 131 | 876 | 2026-10-05T08:16:06Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | sukl | ok | 200 | 1628761 | 15 | 967 | 2026-10-05T08:16:07Z | data/raw/2026-10-05 | validity=2026-10-05 rows_in_file=83509 aggregates=15 |
| 2026-10-05T0703 | ec-hys | ok | 200 | 123518 | 34 | 4971 | 2026-10-05T08:16:09Z | data/raw/2026-10-05 |  |
| 2026-10-05T0703 | nen | skipped | 000 | 0 | 0 | 0 | 2026-10-05T08:16:34Z |  | registry status=planned |
| 2026-10-05T0703 | mpsv | ok | 200 | 36240297 | 21 | 22754 | 2026-10-05T08:16:35Z | data/raw/2026-10-05/mpsv-hiring-2026-09.json | coverage: 23 of 30 days (7 absent); 75543 rows -> 6967 novy -> 21 aggregates written, of which 11 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| 2026-10-05T0703 | coi | skipped | 200 | 39676640 | 0 | 6479 | 2026-10-05T08:17:05Z | data/raw/2026-10-05 | no completed half-year to emit: None |
| 2026-10-05T0703 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-10-05T08:17:13Z |  | registry status=planned |

---

# Ingest run 2026-10-05T1017
Run date: 2026-10-05  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 18599 | 10 | 10 | — | structured | yes |  |
| `coi` | 200 | 39676640 | 0 | 0 | — | none | yes | no completed half-year to emit: None |
| `ec-hys` | 200 | 123518 | 34 | 14 | — | structured | yes |  |
| `hackathon` | 200 | 4962051 | 14 | 11 | below-range | structured | yes | partial: hackjakbrno:mode-a upol:yield-zero |
| `hlidac` | 200 | 2119066 | 822 | 84 | — | structured | yes |  |
| `mpsv` | 200 | 36240297 | 21 | 21 | — | structured | yes | coverage: 23 of 30 days (7 absent); 75543 rows -> 6967 novy -> 21 aggregates written, of which 11 are employer CANDIDATES pending scripts/fetch_ares.sh clearance |
| `nen-ptk` | 200 | 48307792 | 142 | 58 | above-range | structured | yes |  |
| `nku` | 200 | 78251 | 131 | 128 | — | structured | yes |  |
| `reddit-new` | 200 | 185628 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 329839 | 100 | 76 | — | structured | yes |  |
| `suggest` | 200 | 11897 | 42 | 27 | — | structured | yes |  |
| `sukl` | 200 | 1628761 | 15 | 15 | — | structured | yes | validity=2026-10-05 rows_in_file=83509 aggregates=15 |
| `tacr` | 200 | 264246 | 14 | 6 | — | structured | yes |  |
| `ted` | 200 | 62730086 | 7625 | 2690 | — | structured | yes |  |
| `veklep` | 200 | 1946918 | 151 | 19 | — | structured | yes |  |
| `vestbee` | 200 | 1089240 | 61 | 58 | — | structured | yes |  |
| `yc-oss` | 200 | 10542143 | 6269 | 884 | — | structured | yes |  |

## Staged records — PENDING, not appended

4145 records carry their mechanical fields and are waiting on a model. 11350 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 4145 |
| `scores.recurrence` | 4145 |
| `geo_origin` | 4145 |
| `sector` | 4109 |
| `title` | 3263 |
| `summary` | 3263 |
| `pain` | 203 |
| `stated_need` | 74 |
| `scores.urgency` | 61 |

## AC-GDPR1 — contact-field gate

No personal data detected. 4145 staged record(s) passed the field allowlist and the email/phone content scan.

## Republication candidates — same quote and value, new notice id

**200 staged tender record(s) repeat the verbatim quote and the value of a record already on file.** TED re-notifies the same procurement under a new number and neither dedup axis can see it. They are KEPT — a re-issued tender can be evidence (p-0031) — each carries the earlier id in `notes`, and MATCH decides dup or distinct.

| staged id | repeats | seen in |
|---|---|---|
| `hlidac-37393001` | `hlidac-37348449` | batch |
| `ted-555462-2026` | `ted-554061-2026` | batch |
| `ted-556897-2026` | `ted-545152-2026` | batch |
| `ted-556949-2026` | `ted-554061-2026` | batch |
| `ted-557720-2026` | `ted-599397-2026` | ledger |
| `ted-565027-2026` | `ted-553142-2026` | batch |
| `ted-571334-2026` | `ted-570329-2026` | batch |
| `ted-573735-2026` | `ted-596228-2026` | ledger |
| `ted-580531-2026` | `ted-585863-2026`, `ted-666480-2026` | ledger |
| `ted-584625-2026` | `ted-553308-2026` | batch |
| `ted-602172-2026` | `ted-600285-2026` | batch |
| `ted-602795-2026` | `ted-599397-2026` | ledger |
| `ted-603768-2026` | `ted-545152-2026` | batch |
| `ted-605581-2026` | `ted-596494-2026` | batch |
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
| `ted-621196-2026` | `ted-550596-2026`, `ted-666340-2026` | ledger |
| `ted-621214-2026` | `ted-622067-2026` | ledger |
| `ted-621287-2026` | `ted-619553-2026` | batch |
| `ted-621987-2026` | `ted-528464-2026` | ledger |
| `ted-622336-2026` | `ted-564208-2026`, `ted-575552-2026`, `ted-579550-2026`, `ted-604354-2026`, `ted-610001-2026` | ledger |
| `ted-623347-2026` | `ted-622944-2026` | batch |
| `ted-625487-2026` | `ted-528024-2026` | ledger |
| `ted-625493-2026` | `ted-547014-2026` | ledger |
| `ted-633463-2026` | `ted-609630-2026` | ledger |
| `ted-642898-2026` | `ted-637714-2026` | batch |
| `ted-645157-2026` | `ted-607500-2026` | batch |
| `ted-650826-2026` | `ted-642047-2026` | batch |
| `ted-653057-2026` | `ted-621842-2026` | batch |
| `ted-653974-2026` | `ted-577270-2026` | batch |
| `ted-654559-2026` | `ted-617576-2026` | batch |
| `ted-655064-2026` | `ted-579015-2026` | ledger |
| `ted-657918-2026` | `ted-521305-2026` | ledger |
| `ted-657930-2026` | `ted-543982-2026` | batch |
| `ted-659558-2026` | `ted-581960-2026` | ledger |
| `ted-660475-2026` | `ted-599397-2026` | ledger |
| `ted-667393-2026` | `ted-461180-2026`, `ted-477824-2026`, `ted-522836-2026`, `ted-560780-2026`, `ted-568558-2026`, `ted-617274-2026`, `ted-633374-2026`, `ted-652490-2026` | ledger |
| `ted-667870-2026` | `ted-593949-2026` | ledger |
| `ted-668664-2026` | `ted-625446-2026` | ledger |
| `ted-669515-2026` | `ted-553426-2026`, `ted-638764-2026` | ledger |
| `ted-669861-2026` | `ted-651730-2026` | ledger |
| `ted-670055-2026` | `ted-588762-2026`, `ted-609303-2026`, `ted-625251-2026`, `ted-629623-2026`, `ted-644325-2026`, `ted-653745-2026` | ledger |
| `ted-670085-2026` | `ted-599058-2026` | ledger |
| `ted-670290-2026` | `ted-631483-2026` | ledger |
| `ted-670743-2026` | `ted-603562-2026`, `ted-649043-2026` | ledger |
| `ted-671185-2026` | `ted-604584-2026` | ledger |
| `ted-671293-2026` | `ted-538010-2026` | ledger |
| `ted-671478-2026` | `ted-554275-2026`, `ted-589691-2026`, `ted-626435-2026`, `ted-636746-2026`, `ted-660243-2026` | ledger |
| `ted-671568-2026` | `ted-508506-2026` | ledger |
| `ted-671705-2026` | `ted-650891-2026` | ledger |
| `ted-671923-2026` | `ted-590615-2026` | ledger |
| `ted-672247-2026` | `ted-480786-2026`, `ted-547298-2026`, `ted-549130-2026` | ledger |
| `ted-672319-2026` | `ted-581754-2026`, `ted-645471-2026` | ledger |
| `ted-672553-2026` | `ted-597111-2026` | ledger |
| `ted-672641-2026` | `ted-600341-2026` | ledger |
| `ted-672659-2026` | `ted-565622-2026`, `ted-579413-2026` | ledger |
| `ted-672892-2026` | `ted-307565-2026`, `ted-646698-2026` | ledger |
| `ted-672974-2026` | `ted-536370-2026`, `ted-622187-2026`, `ted-635634-2026`, `ted-662675-2026` | ledger |
| `ted-673178-2026` | `ted-591347-2026` | ledger |
| `ted-673193-2026` | `ted-585518-2026` | ledger |
| `ted-673308-2026` | `ted-671062-2026` | batch |
| `ted-673475-2026` | `ted-672079-2026` | batch |
| `ted-673528-2026` | `ted-471761-2026`, `ted-479736-2026`, `ted-490749-2026`, `ted-505800-2026`, `ted-532517-2026`, `ted-555812-2026`, `ted-565673-2026`, `ted-576774-2026`, `ted-585277-2026`, `ted-596315-2026`, `ted-611059-2026`, `ted-625848-2026`, `ted-632248-2026`, `ted-637497-2026`, `ted-656431-2026` | ledger |
| `ted-673661-2026` | `ted-535830-2026` | ledger |
| `ted-673812-2026` | `ted-491490-2026` | ledger |
| `ted-673928-2026` | `ted-652583-2026` | ledger |
| `ted-674056-2026` | `ted-487634-2026`, `ted-503215-2026`, `ted-543649-2026`, `ted-595167-2026`, `ted-636353-2026` | ledger |
| `ted-674231-2026` | `ted-657981-2026` | ledger |
| `ted-674511-2026` | `ted-564353-2026`, `ted-652925-2026` | ledger |
| `ted-674571-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026`, `ted-620795-2026`, `ted-626356-2026`, `ted-633846-2026`, `ted-662151-2026`, `ted-666087-2026` | ledger |
| `ted-674619-2026` | `ted-597605-2026`, `ted-631428-2026` | ledger |
| `ted-674807-2026` | `ted-658199-2026` | ledger |
| `ted-674925-2026` | `ted-662522-2026` | ledger |
| `ted-674938-2026` | `ted-616996-2026` | ledger |
| `ted-675048-2026` | `ted-662569-2026` | ledger |
| `ted-675142-2026` | `ted-654412-2026` | ledger |
| `ted-675156-2026` | `ted-641459-2026` | ledger |
| `ted-675244-2026` | `ted-589902-2026`, `ted-609023-2026` | ledger |
| `ted-675287-2026` | `ted-675185-2026` | batch |
| `ted-675370-2026` | `ted-596617-2026`, `ted-630247-2026`, `ted-644804-2026` | ledger |
| `ted-675442-2026` | `ted-594786-2026`, `ted-654067-2026` | ledger |
| `ted-675550-2026` | `ted-627652-2026` | ledger |
| `ted-675816-2026` | `ted-646876-2026` | ledger |
| `ted-675922-2026` | `ted-602131-2026`, `ted-606455-2026`, `ted-623961-2026`, `ted-641424-2026`, `ted-654549-2026` | ledger |
| `ted-675973-2026` | `ted-609697-2026` | ledger |
| `ted-675981-2026` | `ted-588738-2026`, `ted-615753-2026`, `ted-620746-2026`, `ted-646826-2026` | ledger |
| `ted-676042-2026` | `ted-622050-2026` | ledger |
| `ted-676525-2026` | `ted-614025-2026` | ledger |
| `ted-676634-2026` | `ted-642002-2026` | ledger |
| `ted-676783-2026` | `ted-526780-2026`, `ted-527415-2026`, `ted-527946-2026`, `ted-529184-2026`, `ted-560693-2026`, `ted-561677-2026`, `ted-562280-2026`, `ted-563055-2026`, `ted-619295-2026`, `ted-619410-2026`, `ted-620333-2026`, `ted-621211-2026`, `ted-621320-2026`, `ted-622002-2026`, `ted-622650-2026` | ledger |
| `ted-676914-2026` | `ted-477579-2026`, `ted-507989-2026`, `ted-519602-2026`, `ted-538178-2026`, `ted-558024-2026`, `ted-581728-2026`, `ted-603543-2026`, `ted-606067-2026`, `ted-628817-2026`, `ted-645808-2026`, `ted-659435-2026` | ledger |
| `ted-676963-2026` | `ted-586011-2026`, `ted-654453-2026` | ledger |
| `ted-676993-2026` | `ted-468892-2026`, `ted-553646-2026`, `ted-578104-2026`, `ted-594889-2026`, `ted-612005-2026` | ledger |
| `ted-677144-2026` | `ted-551210-2026`, `ted-585220-2026` | ledger |
| `ted-677165-2026` | `ted-470646-2026`, `ted-552097-2026`, `ted-577271-2026`, `ted-595383-2026`, `ted-611044-2026` | ledger |
| `ted-677196-2026` | `ted-628601-2026` | ledger |
| `ted-677684-2026` | `ted-608224-2026` | ledger |
| `ted-677688-2026` | `ted-602026-2026`, `ted-614156-2026` | ledger |
| `ted-677764-2026` | `ted-477968-2026`, `ted-481331-2026`, `ted-612124-2026` | ledger |
| `ted-677884-2026` | `ted-594537-2026`, `ted-665295-2026` | ledger |
| `ted-678179-2026` | `ted-674719-2026` | batch |
| `ted-678195-2026` | `ted-606820-2026` | ledger |
| `ted-678279-2026` | `ted-610856-2026` | batch |
| `ted-678381-2026` | `ted-610856-2026` | batch |
| `ted-678440-2026` | `ted-655567-2026` | ledger |
| `ted-678450-2026` | `ted-566980-2026` | ledger |
| `ted-678474-2026` | `ted-513926-2026`, `ted-550988-2026` | ledger |
| `ted-678491-2026` | `ted-620253-2026` | ledger |
| `ted-678547-2026` | `ted-610856-2026` | batch |
| `ted-678571-2026` | `ted-613418-2026` | ledger |
| `ted-678944-2026` | `ted-570436-2026`, `ted-619843-2026` | ledger |
| `ted-678961-2026` | `ted-677702-2026` | batch |
| `ted-679178-2026` | `ted-614025-2026` | ledger |
| `ted-679188-2026` | `ted-537364-2026`, `ted-583837-2026`, `ted-618982-2026` | ledger |
| `ted-679202-2026` | `ted-496157-2026` | ledger |
| `ted-679337-2026` | `ted-574899-2026` | ledger |
| `ted-679530-2026` | `ted-651014-2026` | ledger |
| `ted-679554-2026` | `ted-589378-2026` | ledger |
| `ted-679879-2026` | `ted-464869-2026`, `ted-537758-2026`, `ted-553141-2026` | ledger |
| `ted-679934-2026` | `ted-657295-2026` | ledger |
| `ted-680041-2026` | `ted-573039-2026`, `ted-585749-2026` | ledger |
| `ted-680065-2026` | `ted-661629-2026` | ledger |
| `ted-680075-2026` | `ted-600362-2026` | ledger |
| `ted-680231-2026` | `ted-615301-2026`, `ted-663965-2026` | ledger |
| `ted-680319-2026` | `ted-610856-2026` | batch |
| `ted-680499-2026` | `ted-627304-2026`, `ted-646586-2026` | ledger |
| `ted-680530-2026` | `ted-502655-2026`, `ted-569629-2026`, `ted-612317-2026` | ledger |
| `ted-680728-2026` | `ted-594680-2026`, `ted-626765-2026` | ledger |
| `ted-680883-2026` | `ted-626770-2026`, `ted-649987-2026`, `ted-666422-2026` | ledger |
| `ted-680921-2026` | `ted-625427-2026` | ledger |
| `ted-680971-2026` | `ted-680647-2026` | batch |
| `ted-681013-2026` | `ted-638367-2026` | ledger |
| `ted-681028-2026` | `ted-476872-2026`, `ted-557258-2026`, `ted-619912-2026` | ledger |
| `ted-681035-2026` | `ted-610856-2026` | batch |
| `ted-681138-2026` | `ted-589830-2026`, `ted-610006-2026`, `ted-628111-2026`, `ted-653186-2026` | ledger |
| `ted-681152-2026` | `ted-620510-2026` | ledger |
| `ted-681377-2026` | `ted-593033-2026`, `ted-609059-2026` | ledger |
| `ted-681523-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-681757-2026` | `ted-652999-2026`, `ted-658806-2026` | ledger |
| `ted-681793-2026` | `ted-608969-2026` | ledger |
| `ted-681864-2026` | `ted-535984-2026` | ledger |
| `ted-681960-2026` | `ted-618592-2026` | ledger |
| `ted-681978-2026` | `ted-616410-2026` | ledger |
| `ted-682023-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-682229-2026` | `ted-607460-2026` | ledger |
| `ted-682287-2026` | `ted-653459-2026` | ledger |
| `ted-682337-2026` | `ted-613532-2026` | ledger |
| `ted-682473-2026` | `ted-568522-2026`, `ted-592294-2026` | ledger |
| `ted-682522-2026` | `ted-515998-2026`, `ted-625543-2026`, `ted-644284-2026` | ledger |
| `ted-682655-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-683164-2026` | `ted-667500-2026` | batch |
| `ted-683204-2026` | `ted-638367-2026` | ledger |
| `ted-683235-2026` | `ted-518662-2026`, `ted-597134-2026` | ledger |
| `ted-683311-2026` | `ted-614677-2026` | ledger |
| `ted-683421-2026` | `ted-627652-2026` | ledger |
| `ted-683443-2026` | `ted-613424-2026` | ledger |
| `ted-683528-2026` | `ted-591590-2026`, `ted-641320-2026`, `ted-664854-2026` | ledger |
| `ted-683537-2026` | `ted-463450-2026` | ledger |
| `ted-683553-2026` | `ted-667054-2026` | ledger |
| `ted-683689-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-683736-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-683777-2026` | `ted-542879-2026`, `ted-612734-2026`, `ted-624348-2026` | ledger |
| `ted-684005-2026` | `ted-674260-2026` | batch |
| `ted-684098-2026` | `ted-490850-2026`, `ted-494021-2026` | ledger |
| `ted-684146-2026` | `ted-490911-2026`, `ted-531770-2026`, `ted-558714-2026`, `ted-634730-2026`, `ted-663972-2026`, `ted-664483-2026` | ledger |
| `ted-684267-2026` | `ted-535984-2026` | ledger |
| `ted-684291-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026`, `ted-607320-2026`, `ted-615022-2026`, `ted-620795-2026`, `ted-626356-2026`, `ted-633846-2026`, `ted-662151-2026`, `ted-666087-2026` | ledger |
| `ted-684415-2026` | `ted-654645-2026` | ledger |
| `ted-684441-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-684444-2026` | `ted-664684-2026` | ledger |
| `ted-684548-2026` | `ted-536370-2026`, `ted-622187-2026`, `ted-635634-2026`, `ted-662675-2026` | ledger |
| `ted-684572-2026` | `ted-615943-2026` | ledger |
| `ted-684690-2026` | `ted-514922-2026` | ledger |
| `ted-684698-2026` | `ted-664758-2026` | ledger |
| `ted-684736-2026` | `ted-671678-2026` | batch |
| `ted-684758-2026` | `ted-557044-2026`, `ted-557593-2026`, `ted-558393-2026`, `ted-558450-2026`, `ted-559522-2026`, `ted-560048-2026`, `ted-657795-2026`, `ted-658424-2026`, `ted-659171-2026`, `ted-659625-2026`, `ted-660103-2026`, `ted-660258-2026`, `ted-660421-2026`, `ted-660556-2026`, `ted-663222-2026`, `ted-663478-2026` | ledger |
| `ted-684821-2026` | `ted-679860-2026` | batch |
| `ted-684850-2026` | `ted-619071-2026` | ledger |
| `ted-684897-2026` | `ted-547853-2026`, `ted-586137-2026` | ledger |
| `ted-684984-2026` | `ted-616256-2026` | ledger |
| `ted-685044-2026` | `ted-588762-2026`, `ted-609303-2026`, `ted-625251-2026`, `ted-629623-2026`, `ted-644325-2026`, `ted-653745-2026` | ledger |
| `ted-685098-2026` | `ted-602907-2026`, `ted-662266-2026` | ledger |
| `ted-685118-2026` | `ted-596674-2026`, `ted-635589-2026` | ledger |
| `ted-685173-2026` | `ted-653458-2026` | ledger |
| `ted-685188-2026` | `ted-477579-2026`, `ted-507989-2026`, `ted-519602-2026`, `ted-538178-2026`, `ted-558024-2026`, `ted-581728-2026`, `ted-603543-2026`, `ted-606067-2026`, `ted-628817-2026`, `ted-645808-2026`, `ted-659435-2026` | ledger |
| `ted-685253-2026` | `ted-613616-2026` | ledger |
| `ted-685255-2026` | `ted-557644-2026` | ledger |
| `ted-685330-2026` | `ted-579988-2026`, `ted-604859-2026`, `ted-663773-2026` | ledger |
| `ted-685385-2026` | `ted-529597-2026` | ledger |
| `ted-685562-2026` | `ted-604003-2026`, `ted-613260-2026` | ledger |
| `ted-685604-2026` | `ted-626906-2026`, `ted-650393-2026` | ledger |

## Dedup by identity key — same resource, different id

**56 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
| `echys-14628` | `consult-cloud-ai-act` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14628 |
| `echys-14638` | `consult-europol-mandate` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14638 |
| `echys-15252` | `consult-territorial-supply-constraints` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15252 |
| `echys-16413` | `consult-horizon-partnerships` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16413 |
| `echys-17172` | `consult-dual-use-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17172 |
| `echys-18194` | `consult-victims-rights-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18194 |
| `hack-ebca5de0` | `hack-c5c10e91` | `url` | `hackathon` | https://www.aimtechackathon.cz/hackathon/ |
| `nku-k24032` | `nku-urad-prace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24032.pdf |
| `nku-k24008` | `nku-rsc-sport` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24008.pdf |
| `nku-k25001` | `nku-dph-ecommerce` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25001.pdf |
| `nku-k24018` | `nku-odpocivky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24018.pdf |
| `nku-k24025` | `nku-erecept-sms` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24025.pdf |
| `nku-k24016` | `nku-lesnictvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24016.pdf |
| `nku-k24009` | `nku-fakultni-nemocnice` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24009.pdf |
| `nku-k24023` | `nku-ctu-ucetni-zaverka-2024` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24023.pdf |
| `nku-k24019` | `nku-mpsv-ucetni-zaverka-2024` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24019.pdf |
| `nku-k24014` | `nku-nelegalni-prace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24014.pdf |
| `nku-k24017` | `nku-gacr-tacr` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24017.pdf |
| `nku-k24020` | `nku-mk-ucetni-zaverka-2024` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24020.pdf |
| `nku-k24007` | `nku-dtm` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24007.pdf |
| `nku-k24006` | `nku-modernizacni-fond` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24006.pdf |
| `nku-k24012` | `nku-vycvik-acr` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24012.pdf |
| `nku-k24010` | `nku-socialni-sluzby-infrastruktura` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24010.pdf |
| `nku-k24004` | `nku-esbirka` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24004.pdf |
| `nku-k24003` | `nku-knihovny-digitalizace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24003.pdf |
| `nku-k23014` | `nku-brownfieldy` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K23014.pdf |
| `nku-k24001` | `nku-pesi-komunikace` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24001.pdf |
| `nku-k23010` | `nku-vystroj-policie` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K23010.pdf |
| `nku-k23031` | `nku-pozemkove-upravy` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K23031.pdf |
| `nku-k25022` | `nku-podpora-startupu` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25022.pdf |
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
| `nku-k24022` | `nku-nsa-ucetni-zaverka-2024` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24022.pdf |
| `nku-k24029` | `nku-msmt-horizont-kontroly` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24029.pdf |
| `nku-k25002` | `nku-rizeni-skolstvi` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K25002.pdf |
| `nku-k24031` | `nku-justicni-pohledavky` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24031.pdf |
| `nku-k24030` | `nku-doprava2020` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24030.pdf |
| `nku-k24026` | `nku-viza-it` | `nku-kzaver` | `nku` | https://nku.cz/assets/kon-zavery/K24026.pdf |
| `veklep-KORNDW7HRLI7` | `reg-veznice-ubytovaci-plocha-2030` | `url` | `veklep` | https://odok.gov.cz/portal/veklep/material/KORNDW7HRLI7/ |
| `round-mika` | `de-mika` | `url` | `vestbee` | https://www.vestbee.com/insights/articles/mika-raises-6-m |
| `yc-d-model` | `yc-d_model` | `url` | `yc-oss` | https://www.ycombinator.com/companies/d_model |
| `yc-galactic-resource-utilization-space-inc-gru-spac` | `yc-galactic-resource-utilization-space-inc-gru-space` | `url` | `yc-oss` | https://www.ycombinator.com/companies/galactic-resource-utilization-space-inc-gru-space |

**2 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:idea13.cz/` | carried by 4 records in THIS batch — undecidable, so no merge |
| `url:nakopniprahu.cz/` | carried by 6 records in THIS batch — undecidable, so no merge |
| 2026-10-05T0818 | ares | ok | 200 | 47924 | 11 | 2690 | 2026-10-05T08:18:38Z | data/raw/2026-10-05/ares-lookups-2026-09.json | resolved 11 of 11 (404 0, bad-checksum 0); named 6 employer record(s) |

---

# Coordinator notes — 2026-10-05

- `ingest.sh` exited **1**: `fetch_all` reported `mpsv(rc=1)`. mpsv itself fetched 23/30 day files and wrote 21 aggregates, 11 of them employer candidates pending ARES. The coordinator then ran `fetch_all.sh data/raw/2026-10-05 ares` (11 resolved, 6 named, 5 dropped below the employer-record cap) and re-ran `normalize.py --mechanical-only` BEFORE any grading so staging reflects the fold (4,145 -> 4,140 staged). That second mechanical run appended a duplicate ingest section to this manifest; it was reverted to the pre-run copy, so the ingest section above is the original run.
- **Pass A** (86 batches, 9 Sonnet graders; one grader took all 74 asks so ask grading is consistent, owner decision 13 of 2026-09-28): 3,976 filled, 149 refused by the pain bar, 15 asks graded `stated_need: false` (59 true). Grader notes: every TED/veklep `event_date_in_past` item graded urgency 0; 14 current SÚKL supply interruptions graded 3.
- **Materiality**: 3,240 dropped (327 new to `dropped-log.jsonl`, 2,913 re-drops).
- **Pass B** (15 batches, 3 Sonnet writers): 730 filled, 0 rejected.
- **Appended** (`--complete --allow-incomplete`): **736** — tenders 610, funded 47, demand 38, regulation 21, hiring 16, asks 4. 164 remain staged by design.
- **Attended scans** appended earlier by the coordinator, one `--complete --today 2026-10-05` per feed directory: demand 9, regulation 5, dotace 4, funded 13, plus 1 demand record staged by the new-candidate judge (`civic-uohs-prezkum-vz-2025`). Run total **768**.
- demand-scan used `nku-<topic>` ids (45 earlier demand-scan records do the same) because only the `nku` prefix gets the `nku-kzaver` identity key that stops the scripted card for the same audit re-staging. `nku` is not in the demand-scan `id_prefixes` list in feeds.json; see the weekly report.
- Health after: LIVE 22, PENDING 6, STALE 0, BROKEN 0.


## demand-scan pass — 2026-10-05 (weekly delta)

This is the weekly delta pass of feed `demand-scan` (evidence_type `demand`), seven days after the
2026-09-28 pass (`data/raw/2026-09-28/manifest.md`, demand section). It follows pipeline/SCANS.md
and walked every checklist source. The window was **items published or newly surfaced since
2026-09-28**, plus everything the 09-28 pass said it owed. That included the **16 old NKÚ
conclusion PDFs in the dropped log that nobody had read**. All 16 were read this pass.

Worktree `localproblems-weekly-2026-10-05`. This pass wrote only to
`data/raw/2026-10-05/demand/`: payloads under `pages/`, `staged.jsonl` and this file. It made no
ledger, seen.txt, dropped-log, register.db or feeds.json write, and no git state change.

### Hand-off

- `data/raw/2026-10-05/demand/staged.jsonl` holds **9 records**. Each carries
  `"evidence_type": "demand"`, `"_needs": []`, `extraction: manual`, a verbatim quote, and every
  REQUIRED_OUT field.
  - Every quote was asserted mechanically as a literal substring of the `pdftotext -layout`
    output after `\s+` collapse. The outputs are saved as `pages/nku-kNNNNN.txt`.
- **Dry run** against a SCRATCH COPY (`$TMPDIR/demand-sim-1005/signals`, with `--out-dir`,
  `--seen` and `--dropped-log` all pointed at the copy, `--today 2026-10-05`). It printed:
  `would append 9 records across 1 file(s); 0 dropped by materiality; 0 incomplete; 0 refused by
  AC-GDPR1` → `signals/demand/2026-10-05.jsonl: +9`; `dedup by identity key (append): 0 skipped`.
  The allowlist dropped only `_needs` and `evidence_type`, as expected.
  `git status --porcelain data/signals` was **empty** afterwards.
- The coordinator owes this feed one `--complete` over `data/raw/2026-10-05/demand` and the
  `db.py upsert` line it prints.
- **ID-prefix note: these records use `nku-<topic>`, not one of the 14 demand-scan prefixes.**
  This is deliberate. `scripts/normalize.py` `record_keys()` forms the `nku-kzaver:<code>`
  identity key **only for prefix `nku`**. That key is what dedups the scripted `nku` feed's
  `nku-kNNNNN` cards against a hand-read conclusion. Under `civic-` the key would not form, and
  the scripted card for the same audit would be re-staged or re-dropped every run. The corpus
  already holds 45 hand-written `nku-<topic>` records with `source: demand-scan` (e.g.
  `nku-zemedelsky-vyzkum`, `nku-up-ucetni-zaverka-2025`), so this follows established practice.
  The `nku` registry row's `signal_source` is also `demand-scan`.
  - The coordinator may still prefer a re-prefix. If so, the alternative is `civic-nku-<topic>`
    (precedent: `civic-nku-1719-nakup-leciv`), at the cost of the kzaver dedup.

### Dropped-log duty (INGEST.md 3c) — opened first

- `data/signals/dropped-log.jsonl` now has 4,322 lines. Of these, **90 are `nku` and 0 are
  `demand-scan`**.
- Sorted by `times_dropped`, every `nku` line is at **2** (first_seen 2026-09-19, last_seen
  2026-09-28). Each one is a repeat offender, re-dropped by the 09-28 scripted run.
- Card classes:
  - ~60 Věstník procedural notices ("Změna plánu…", "Ukončení … (nepublikovaná)", Kolegium
    agendas, "Kontroly zahajované"). None has a document that says more than its card.
  - 7 press-release twins (`nku-15787/15796/15799/15809/15814/15872/15897`). These are already
    held at their conclusion-PDF URLs, as the 09-28 pass recorded.
  - **19 conclusion PDFs** (`nku-k22032 … nku-k25020`). k25015/16/20 were judged by the 09-03 /
    08-10 passes. **The other 16 were read in full this pass** (summary section "Shrnutí a
    vyhodnocení" plus findings). Verdicts are in the table below.

| audit | subject · body | quantified failure found | verdict |
|---|---|---|---|
| 22/32 | Presidential Office, Správa Pražského hradu, Lesní správa Lány | 149k CZK legal fees, 83k CZK double payment, 1,195,500 CZK paid with no legal basis | **not re-staged**: one body, money 1, scale 0, urgency 0. The drop was correct |
| 23/10 | Police uniforms · MV | 2,373.9m CZK spent 2018–22; no systemisation (0 of 7 goals); penalties unclaimed in 8 of 12 contracts | **re-staged** `nku-vystroj-policie` |
| 23/14 | Brownfield grants · MMR, SFPI | ~255m CZK audited; budget-discipline breach indications in 7 of 19 projects; no record of land regenerated | **re-staged** `nku-brownfieldy` |
| 23/28 | Test institutes EZÚ / TZÚS · MPO as founder | 17.9m CZK wasted on a halted EZÚ building project; ≥31.2m CZK retaining wall needed | **not re-staged**: a single state enterprise's project failure (scale 0) with no buyer-facing need. Money 2 would pass the filter, so this is a judgment and is stated as one |
| 24/03 | Library digitisation · MK | 446.7m CZK; 12.7m CZK paid over the legal cap; 24 unlawful projects; 1 inspection in 7 years | **re-staged** `nku-knihovny-digitalizace` |
| 24/05 | Publicity of 2014–20 OPs · MMR, MPO | 648m CZK publicity spend; impact never measured; no loss figure | **not re-staged**: outcome-blindness with no quantified failure or loss |
| 24/10 | Social-services infrastructure (IROP) · MMR | 5,970m CZK, 664 projects; up to 19.1m CZK suspected budget-discipline breaches; cars bought beyond need | **re-staged** `nku-socialni-sluzby-infrastruktura` |
| 24/11 | HGV weigh-in-motion · MD, SFDI, ŘSD | 2.61% of offences prosecuted | **already held** as `nku-vazeni-kamiony` (press-release URL id14742, same audit, 9 Jun 2025) |
| 24/13 | University infrastructure · MŠMT | — | **already held** as `nku-vysoke-skoly` (id14757, 16 Jun 2025) |
| 24/15 | ERÚ asset management | "no significant shortcomings"; Prague office rent 39m vs Ostrava 7m CZK | **not re-staged**: no failure, one body |
| 24/19 | MPSV 2024 accounts | 7.6bn CZK bookkeeping defects corrected mid-audit | **re-staged** `nku-mpsv-ucetni-zaverka-2024` |
| 24/20 | MK 2024 accounts | 6.6bn CZK corrected mid-audit | **re-staged** `nku-mk-ucetni-zaverka-2024` |
| 24/21 | State enterprises in liquidation · MPO, MZe | liquidations lasting 8–23 years; 160.6k CZK impact | **not re-staged**: money 1, scale 1, urgency 0 (would drop) |
| 24/22 | National Sports Agency 2024 accounts | 911.8m CZK corrected + 1,431.1m CZK misclassified | **re-staged** `nku-nsa-ucetni-zaverka-2024`. The `nku-up-ucetni-zaverka-2025` notes call it "clean", but the text shows the same failure class as 25/21 |
| 24/23 | ČTÚ 2024 accounts | 6,457.3m CZK corrected mid-audit | **re-staged** `nku-ctu-ucetni-zaverka-2024` |
| 24/33 | Soft-target protection | — | **already held** as `nku-mekke-cile` (id15411, 9 Feb 2026) |

- **Result: 8 of 16 re-staged, 3 already held under press-release URLs, 5 not re-staged with
  reasons.**
- Publication dates come from the NKÚ Věstník year tables (`pages/nku-vestnik-{2025,2026}.html`,
  "Datum zveřejnění"). They are not taken from PDF Last-Modified headers, which are re-upload
  dates for some files: k23010 was approved 29 Apr 2024 and published 20 Jan 2025.
- **For the coordinator:** the three "already held" audits are held under press-release URLs
  with no `kNNNNN` in url or title. So the kzaver key does not form for them, and the scripted
  cards `nku-k24011/k24013/k24033` will keep re-dropping (harmless, but they will keep counting
  up `times_dropped`). The cards for the 8 re-staged audits will dedup from now on.

### Checklist source 1 — NKÚ kontrolní závěry (parse the PDFs)

**Visited. One new conclusion was published (25/22), and it is staged.**

- RSS `https://nku.cz/cz/rss.xml`: **200**, 14,259 B (`pages/nku-rss.xml`), against 13,843 B on
  09-28. Items newer than 25 Sep:
  - **id15950, 5 Oct 2026**: *"Do podpory startupů vložil stát téměř miliardu korun…"*. This is
    the press release to audit **25/22**. The page answered 200 and was saved as
    `pages/nku-15950.html`. → staged as `nku-podpora-startupu` from the conclusion PDF.
  - id15926 (1 Oct): "Kontroly zahajované v říjnu 2026". Procedural, saved, not a signal.
  - id15938 / id15939 (29 Sep): NKÚ job adverts. Not signals.
- Conclusion-PDF probe (HEAD, `www.nku.cz/assets/kon-zavery/`):
  - **200**: k25018, **k25021** (Last-Modified 10 Aug 2026, already held as
    `nku-up-ucetni-zaverka-2025`), **k25022** (**new**, Last-Modified 5 Oct 2026 04:32 GMT,
    453,105 B).
  - **404**: k25019, k25023, **k25024**, k25025–k25030, k26001–k26003. Upper-case `K…pdf` on
    www and on bare nku.cz also returned 404 (or 301 for files that exist).
- **25/24 (revitalisation of public spaces): 404 for the fifth consecutive pass.** As the 09-28
  pass advised, the Kolegium page id15884 was read instead of probing blind
  (`pages/nku-15884.html`, 200). It confirms that the 13th Kolegium on 7 Sep 2026 **approved**
  "Kontrolní závěr z kontrolní akce č. 25/24 – Peněžní prostředky určené na podporu
  revitalizace veřejných prostranství měst a obcí".
  - The 2026 Věstník year table lists no publication for 25/24.
  - Approval-to-publication lag measured this pass: **25/22 took 77 days** (20 Jul → 5 Oct). On
    that lag, 25/24 would land around **late November 2026**. This is not a fetch failure.
- **Věstník 4/2026.** The issue index `pages/nku-vestnik.html` (200, 41,328 B) is byte-identical
  and still lists only částky 1–3/2026.
  - But the year table `https://nku.cz/scripts/rka/vestnik.asp?rok=2026` (200,
    `pages/nku-vestnik-2026.html`) already assigns items to **částka 4/2026**: 25/13 (7.9),
    25/14 (14.9), 25/18 (21.9), **25/22 (5.10)** and three plan changes of 11.9.
  - So 4/2026 is being filled but not yet issued as a document. Every conclusion in it is either
    held or staged.
- Payloads: `pages/nku-k25021.pdf`, `pages/nku-k25022.pdf`, the 16 dropped-log PDFs
  (`pages/nku-k{22032,…,24033}.pdf`), each with a `.txt` beside it, and
  `pages/nku-vestnik-{2024,2025,2026}.html`.

### Checklist source 2 — European Semester CZ package

**Visited. Nothing new.**

- `…/country-pages-including-country-reports/country-report-czechia_en`: **200**, 76,131 B
  (`pages/ecsem-landing.html`), against 74,808 B on 09-28.
  - The size delta is page chrome. The newest item is still the **3 June 2026** Country Report,
    then 4 June 2025.
  - Both halves of the 2026 cycle are held (`ecsem-cz2026-*`, `ecsem-cz2026-csr`).
  - The next cycle opens with the Autumn Package (Nov 2026) and the 2027 Country Report
    (~May/June 2027).
- CELLAR SPARQL was **deliberately not visited**. It stays owed to the next MONTHLY broad pass
  (carried since 09-21).

### Checklist source 3 — MPSV Statistická ročenka, chapter 5

**Visited. EXPECTED ABSENCE (not yet published). This is not a coverage gap.**

- The archive page returned **200**, 1,335,986 B (`pages/mpsv-rocenka-archiv.html`).
- The newest edition is still "… v roce 2024" (`.7z`).
- **Positive control:** "v roce 2024" ×4. "v roce 2025" ×0.
- Owed: re-check next pass. When the 2025 edition lands, diff tab 5.9 against
  `civic-mpsv-rocenka-neuspokojene-2024` and file it under `civic-` (the mpsv- trap).

### Checklist source 4 — Ombudsman ESO (HTML walk, no RSS)

**Visited. 5 newly visible ESO items, none minted (single cases, or systemic with no figure).
The positive control passed. The Q3 report is not yet published.**

- `https://www.ochrance.cz/eso/zpravy/`: **200**, 14,674 B. This is the taxonomy explainer,
  same size as before.
- ESO app `https://eso.ochrance.cz/`: **200**, 83,474 B.
  - Session method: cookie jar → `POST /Vyhledavani/Search` → `POST /Nalezene/GetPocetVysledku
    --data ""` → `POST /Nalezene/GetTableContent` with `page=N&rows=10&sidx=&sord=`.
  - **Positive control** `FormaZjisteni=22`: **41**, unchanged.
  - `DatumVydaniOd=01.06.2026`: **49 hits**, against 45 on 09-28. All 5 pages were read
    (`pages/eso-table-since0601-p{1..5}.html`).
  - The ids were diffed against the 09-18 capture in the main checkout
    (`data/raw/2026-09-18/demand/eso-table-recent-p*.html`, 43 ids) plus 15082 (09-21) and
    15088 (09-28). The **4 additions** are older item ids published late:
    - **14866**: 8167/2025/VOP, § 18, 27.07.2026. ČSSZ delays in an EU-coordinated invalidity
      pension. Single case.
    - **15018**: 3667/2026/VOP, § 18, 13.08.2026. ČSSZ left a terminally ill man with no income
      from Jan 2026 over EU-coordination pension periods. Single case.
    - **15020**: 1983/2026/VOP, § 18, 17.08.2026. ČSSZ erred on sickness benefit after the
      support period. Single case.
    - **14998**: 4096/2024/VOP, § 18 follow-up, 18.06.2026. **Systemic.** KACPU centres do not
      consistently identify unaccompanied Ukrainian minors at risk of exploitation, and OSPOD
      offices are described as "dlouhodobě velmi náročná" in workload. The only figures are
      "3 až 4 případy měsíčně" (KACPU calls to OSPOD). **Not minted**: scale 1, money 0,
      urgency 0, so it would drop. It is noted as supporting colour for `p-0041` below.
  - Item-id frontier: probed `/Nalezene/Edit/15089 … 15130`. Only **15090** answered 200.
    - It is 4371/2025/VOP, a § 18 report of 10.10.2025 with a § 19 final statement of
      3.3.2026: a housing allowance wrongly refused after a returned early pension. Single
      case, not minted.
    - The two ČSSZ EU-coordination cases (14866, 15018) share a shape. Two cases are not a
      scale claim, so this is watch only.
- Aktuálně `https://www.ochrance.cz/aktualne/`: **200**, 47,577 B. Two items newer than the
  09-28 read:
  - "Hlas společnosti uvnitř Kanceláře ombudsmana: Sestavili jsme poradní orgány"
    (`pages/ombud-poradni-organy.html`). Advisory-body candidates, with a public consultation
    to 14.10.2026. Organisational news, not minted.
  - "Prázdninový Zpravodaj ombudsmana…" (`pages/ombud-zpravodaj-prazdniny.html`). A newsletter
    of single cases, not minted.
- **Q3 2026 quarterly report: NOT YET PUBLISHED.**
  - `…/dokument/zpravy_pro_poslaneckou_snemovnu_2026/2026-iii-q.pdf` returned **404** (the
    upper-case variant also 404).
  - Positive control `2026-ii-q.pdf` returned **200** (held as `ombud-q2-2026`). The Q2 report
    appeared in ESO on 30.07.2026 (items 14988/14992), about a month after quarter end.
  - Q3 is therefore expected around **late October 2026**. This is an expected absence, owed
    next pass.

### Records

| id | source doc (published) | sector | sc/mo/ur/re | money_eur | key number |
|---|---|---|---|---|---|
| `nku-podpora-startupu` | KZ 25/22, 5 Oct 2026 | govtech | 2/3/0/2 | 37,306,122 | 914m CZK; impact untracked on most projects; 21m CZK agency-staff cost uneconomical |
| `nku-vystroj-policie` | KZ 23/10, 20 Jan 2025 | other | 1/3/0/2 | 96,893,878 | 2,373.9m CZK; penalties unclaimed in 8 of 12 contracts |
| `nku-brownfieldy` | KZ 23/14, 17 Feb 2025 | environment | 2/3/0/2 | 10,408,163 | 7 of 19 projects with budget-discipline breach indications |
| `nku-knihovny-digitalizace` | KZ 24/03, 3 Mar 2025 | education | 2/3/0/2 | 18,232,653 | 12.7m CZK over cap, 24 unlawful projects, 1 inspection in 7 years |
| `nku-socialni-sluzby-infrastruktura` | KZ 24/10, 19 May 2025 | health | 2/3/0/2 | 243,673,469 | up to 19.1m CZK suspected budget-discipline breaches |
| `nku-mpsv-ucetni-zaverka-2024` | KZ 24/19, 11 Aug 2025 | govtech | 1/3/0/2 | 310,204,082 | 7.6bn CZK bookkeeping defects corrected |
| `nku-mk-ucetni-zaverka-2024` | KZ 24/20, 21 Jul 2025 | govtech | 1/3/0/2 | 269,387,755 | 6.6bn CZK corrected |
| `nku-nsa-ucetni-zaverka-2024` | KZ 24/22, 16 Feb 2026 | govtech | 1/3/0/2 | 37,216,327 | 911.8m CZK corrected + 1,431.1m CZK misclassified |
| `nku-ctu-ucetni-zaverka-2024` | KZ 24/23, 11 Aug 2025 | govtech | 1/3/0/2 | 263,563,265 | 6,457.3m CZK corrected |

- All amounts are converted at 24.5 CZK/EUR, the rate used by nku-gacr-tacr and
  nku-up-ucetni-zaverka-2025. Each `money_note` states which figure was converted.
- For the four accounting audits, the money is a **misstatement corrected**, not money lost.
  Their `money_note` says so.
- **Urgency 0 throughout.** These are closed audits with no dated obligation. Precedent
  (`nku-up-ucetni-zaverka-2025`) scored 1, but rung 1 means "a dated event >18 months out" and
  none exists (one field, one meaning). This does not affect materiality: every record is
  money 3.

### Dedup

- seen.txt: none of the 9 ids appears.
- Corpus: no ledger record cites any of the 9 conclusion PDFs, in either `k`/`K` spelling or
  either host.
- The scratch dry run skipped 0 on identity keys. Each record forms `url:` + `nku-kzaver:<code>`
  keys (checked with `normalize.record_keys`).
- **Possible same-run twin:** the scripted `nku` feed may land the press release
  `nku-15950` (25/22) in today's ingest. That card's title carries no k-code, so it will not
  dedup against `nku-podpora-startupu`. If it scores material it is a second record for the
  same audit, and should be judged at `--complete` (it scored 0/0/0 in every comparable
  precedent and would drop).

### Candidates for MATCH

- **`p-0050-grant-recipient-clawbacks`** (grant recipients made to repay over procurement or
  condition breaches) gains **recipient-side, programme-level receipts**:
  - `nku-brownfieldy`: budget-discipline breach indications at **7 of 19** brownfield projects,
    with towns and regions as recipients.
  - `nku-socialni-sluzby-infrastruktura`: **up to 19.1m CZK** of suspected breaches at NGO and
    municipal social-service providers.
  - Provider-side context: `nku-knihovny-digitalizace` (grants paid against the rules, almost
    no inspection, so breaches surface late).
- **Outcome-blind state support programmes:** `nku-podpora-startupu` joins `nku-gacr-tacr`,
  `nku-zdravotnicky-vyzkum` and `nku-zemedelsky-vyzkum`. These are providers that cannot show
  what their money achieved. No problem record in `data/problems/cz/` covers this.
  - **New-problem candidate (weak, provider-side):** "Czech grant providers cannot show what
    their programmes achieved, because recipients do not report outcomes".
  - Evidence: <50% of supported startups reported data and sanctions were never used (25/22);
    research audits 24/17, 25/13, 25/18; 24/05 (648m CZK of publicity with no impact
    measurement, read but not staged).
  - The buyer would be a ministry or agency (MPO/CzechInvest, TA ČR, MZe). It is adjacent to
    p-0050 from the other side.
- **State accounting quality:** the 4 accounting records plus `nku-up-ucetni-zaverka-2025` and
  `nku-dia-ucetnictvi` give **six state accounting units whose books carried 0.1–7.6bn CZK of
  defects** that were caught only by the auditor.
  - No problem covers public-sector bookkeeping. `p-0023-ai-accounting-capacity` is about
    accountant retraining under a planned law, not this, so it is at most adjacent.
  - Possible new-problem candidate. It is weak as a market: each unit is one buyer, there are
    many of them, and the money is a misstatement rather than a loss.
- **`p-0041-social-work-case-notes`** (child-protection offices short-staffed): ESO 14998 states
  OSPOD workload is "dlouhodobě velmi náročná" and recommends MPSV relieve OSPOD overload.
  This is qualitative colour only, not minted, with no figure.
- `nku-vystroj-policie` has no problem match. It is a single-ministry kit-logistics failure, kept
  as evidence only.
- Carried from 09-28 and still open:
  - `ombud-spravni-rad-praxe`
  - the small-municipality delegated-agenda burden (`ombud-male-obce-statni-sprava`, near
    `p-0038-village-public-guardianship`)
  - `ombud-stiznosti-zdravotnictvi`

### Coverage gaps

- **Carried: NKÚ 25/24 `k25024.pdf`, 404 ×5.** Approval on 7 Sep 2026 is confirmed via
  Kolegium id15884. On the measured 77-day lag it is expected around late November. Owed: a
  re-probe each pass.
- **Carried (changed shape): Věstník 4/2026.** Items are assigned to it in the year table, but
  the issue document is not in the index. Owed when it is issued. It should contain
  25/13, 25/14, 25/18 and 25/22, all held or staged.
- **Expected absences, not gaps:** MPSV ročenka 2025 (control passed); ombudsman Q3 2026 report
  (control `2026-ii-q.pdf` 200, expected ~late Oct); Semester cycle complete for 2026.
- **Deliberate non-visit:** CELLAR SPARQL, owed to the monthly broad pass (carried).
- **Closed this pass:** the 16 unread NKÚ PDFs in the dropped log. All were read: 8 re-staged,
  3 already held, 5 judged and not re-staged.

### Pass summary

```
feed:                     demand-scan (weekly delta, evidence_type demand, 7 days after the 2026-09-28 pass)
checklist sources:        4 of 4 visited (NKU / European Semester / MPSV rocenka / ombudsman ESO); ESO control 41 passed, MPSV control passed, ombud Q-report control passed
records staged:           9  (1 new NKU 25/22 + 8 re-staged from the dropped log; scratch dry run: +9, 0 dropped, 0 incomplete, 0 refusals, 0 identity-key skips)
coverage gaps named:      2 carried (NKU 25/24 404 x5; Vestnik 4/2026 not issued) · 1 closed (16 dropped-log PDFs read) · 3 expected absences · 1 deliberate non-visit (CELLAR)
rotation state:           n/a — category rotation is arb-scan's duty
```


## reg-scan pass — 2026-10-05 (weekly delta)

Weekly delta pass of `reg-scan` (`evidence_type` regulation, `source` reg-scan, prefix `reg-`,
attended). Operating file: `pipeline/SCANS.md` reg-scan checklist 1–4 under THE CHECKLIST LAW;
evidence bar `pipeline/SWEEP.md` step 4; dropped-log duty `pipeline/INGEST.md` 3c. Window:
published or enacted since the 2026-09-28 passes, plus the debts the 2026-09-28 reg-scan section
and the 2026-09-28 VeKLEP SWEEP named.

Ran alongside the scripted ingest on the same raw date. This pass wrote ONLY
`data/raw/2026-10-05/regulation/` (`staged.jsonl`, this file, `pages/`). It READ the top-level
`veklep-p1..p7.json` payload read-only (151 items, fetched 07:06Z, `ok`) to get attachment lists
without re-fetching what the script fetched. **Nothing was written to `data/signals/**`,
`seen.txt`, `dropped-log.jsonl`, `register.db`, `feeds.json`, `data/problems/**` or the shared
`manifest.md`.** No real `--complete`, no `db.py` call, no git operation.

**Records staged: 5** — all `reg-`, `source: reg-scan`, `evidence_type: regulation`,
`extraction: manual`, `_needs: []`, none in `seen.txt`. Every quote is ≤300 chars and was checked
in a script as a literal substring of the whitespace-collapsed saved page (lengths 98, 269, 277,
65, 189).

| id | instrument | status | date | payload |
|---|---|---|---|---|
| `reg-ki-portal-178-2026` | vyhl. 178/2026 Sb., critical-infrastructure portal | **ENACTED**, in force 1 Oct 2026 | 2026-10-01 | `esbirka/sb-2026-178.txt` |
| `reg-cestovni-nahrady-175-2026` | vyhl. 175/2026 Sb., travel-allowance petrol price 34.70 → 41.80 CZK/l | **ENACTED**, in force 1 Oct 2026 | 2026-10-01 | `esbirka/sb-2026-175.txt` |
| `reg-cz-drg-2027-174-2026` | ČSÚ sdělení 174/2026 Sb., CZ-DRG version 2027 | **ENACTED**, effective 1 Jan 2027 | 2027-01-01 | `esbirka/sb-2026-174.txt` |
| `reg-eu261-revize-2027` | Regulation (EU) 2026/2202, EU261 air-passenger-rights reform | **ENACTED** (OJ L 2 Oct 2026), applies 23 Oct 2027 | 2027-10-23 | `eu/32026R2202-en.txt` |
| `reg-preshranicni-vymahani-pokut-2027` | MD bill transposing Dir. (EU) 2024/3237 (VeKLEP KORNDY2GNBC7) | **DRAFT** (comment procedure) | 2027-07-20 | `veklep/zd_KORNDY2GNBC7.txt` |

### Access notes (measured today)

- **vlada.gov.cz**: both checklist pages HTTP 200, **byte-identical in length to 2026-09-28**
  (181,238 and 43,059 bytes). RSS 200, 8 items (1–5 Oct).
- **ODok**: `odok.cz` → `odok.gov.cz` / `www.odok.gov.cz` redirects. **Five downloads arrived
  truncated** (16,021 / 77,987 / 229,012 / 392,822-byte stubs, not valid zip/pdf); every one
  succeeded on retry, validated with `unzip -t` / `pdfinfo`. Same intermittency class as 09-19,
  09-21 and 09-28. `textutil` failed inside the sandbox; docx converted with an inline zip reader,
  pdf with `pdftotext -layout`.
- **e-Sbírka**: `sbr-cache/dokumenty-sbirky/<staleUrl>` works for metadata (HTTP 400 for numbers
  not yet promulgated). **New today: the full text is available from
  `sbr-cache/dokumenty-sbirky/<staleUrl>/fragmenty?cisloStranky=N` when sent with
  `Accept: application/json`** (HTTP 406 without it). The ELI HTML route is a JS shell.
- **EUR-Lex**: CELLAR SPARQL on `official-journal-act_date_publication`; CELEX content
  negotiation for the full text. No browser needed.
- **psp.cz**: windows-1250, decoded with iconv.

---

### Checklist source 1: Programové prohlášení vlády + semi-annual fulfilment evaluations

**Visited. Nothing new.** Page HTTP 200, 181,238 bytes, same single attachment
(`programove-prohlaseni-vlady.pdf`), **no fulfilment evaluation**. Cabinet business since 09-28
read via ODok `zvlady/jednani-detail/<date>` (`pages/vlada/odok-jednani-*.html`): 29 Sep–2 Oct are
the empty 33,376-byte template; **5 Oct 2026** has an agenda (22 items + addendum), undecided at
read time. Agenda items relevant to the register, for a later pass: 670/26 school act (teaching
assistants, `KORNDUVFCEIZ`, held on `reg-skolsky-asistenti`), 728/26 MPs' RUD bill
(`KORNDXQH9BRI`, tisk 298), 706/26 NV extraordinary support for farmers hit by the Middle-East
crisis, 741/26 *Zpráva o stavu snižování zátěže podnikatelů v ČR v roce 2025* (a state-authored
business-burden report — a demand-scan lead), 738/26 H1 2026 budget execution. **No record from
source 1.** Carried gap: no fulfilment evaluation (next expected ~January 2027).

### Checklist source 2: Plán legislativních prací vlády (2026; is 2027 published?)

**Visited. Unchanged; the 2027 plan is NOT published.** 2026 page HTTP 200, 43,059 bytes, same two
annexes (`1234_2026_priloha_c-_1.pdf`, `_2.pdf`). None of today's 151 VeKLEP materials is titled
"Plán legislativních prací" (title grep), and the 5 Oct cabinet agenda does not carry it. Expected
absence (the plan is approved around the turn of the year). Several drafts read today cite the
"Plán legislativních prací vlády na zbývající část roku 2026" — a mid-year supplementary plan
this checklist URL does not point at; a future pass should locate it. **No record from source 2.**

### Checklist source 3: e-Sbírka and EUR-Lex (enacted since 2026-09-28)

**e-Sbírka: visited.** sbr-cache probed 2026/166–200 (`pages/esbirka/sbr-2026-*.json`):
**173–179 are new**, 180–200 return HTTP 400 (not promulgated). Texts fetched for 166, 167,
173–179 (`sb-2026-*.txt`).

| Sb. | what it is | in force | outcome |
|---|---|---|---|
| 166/2026 | amends 375/2022 Sb. on medical devices | 16 Sep 2026 | **Still undigitised** ("právě digitalizujeme", 19 days after promulgation). Carried |
| 167/2026 | NV amending 83/2023 Sb., direct payments to farmers | 1 Oct 2026 | Not recorded: payment conditions, held as cards `veklep-KORNDVADGSS4`/`KORNDNQDXTF0` |
| 173/2026 | MD decree, inland-navigation medical fitness (card `KORNDV37RXI3`, dropped-log) | 14 Oct 2026 | Not recorded: reference update to Reg. (EU) 2026/118, DZ says no new duty |
| 174/2026 | ČSÚ notice: **CZ-DRG version 2027** | 1 Jan 2027 | **RECORDED `reg-cz-drg-2027-174-2026`** |
| 175/2026 | MPSV decree: travel-allowance petrol price **34.70 → 41.80 CZK/l** | 1 Oct 2026 | **RECORDED `reg-cestovni-nahrady-175-2026`** (card `KORNDXWQDTHG`) |
| 176/2026 | NV: pension supplements 2027 (card `KORNDY2HHS8D`) | 1 Jan 2027 | Not recorded: benefit parameter |
| 177/2026 | NV: 2027 pension parameters — VVZ 2025 48,900 CZK, coefficient 1.0565, basic amount 5,170 CZK, +270 CZK + 0.2 % | 1 Jan 2027 | Not recorded: benefit parameters; any OSVČ minimum-advance figure would have to be derived, and nothing is derived |
| 178/2026 | MV decree: **critical-infrastructure portal** (card `KORNDTUBDJRM`) | 1 Oct 2026 | **RECORDED `reg-ki-portal-178-2026`** |
| 179/2026 | NV: folk-architecture heritage reserves (card `KORNDV4EB4WE`) | 1 Jan 2027 | Not recorded: niche |

Carried debts:
- **EET 2.0 Sbírka number: NOT CLEARED, moved.** `psp.cz historie t=189` (HTTP 200,
  `pages/psp/psp-tisk189.html`) now adds "Schválený zákon odeslán k publikaci ve Sbírce zákonů
  1. 10. 2026". Highest promulgated number is 179/2026 and none is the EET act. `reg-eet2-2027` /
  `reg-mf-eet2-2027` still owe their number and in-force date — expect it in the 180s next week.
- **166/2026 content: NOT CLEARED** (still undigitised in e-Sbírka; the PDF "Stáhnout" route was
  not tried). Its sněmovní tisk was not looked up.
- **Tisk 48: MOVED.** `historie t=48` (state as of 5 Oct 2026) now reads "Projednávání tisku
  navrženo na pořad 34. schůze (od 13. října 2026)". Still in the general debate of the second
  reading; still blocks the 2023/564 spray-record duty and the pesticide-equipment decree
  `veklep-KORNDXYA34EY`.
- **2027 motorway-vignette rates: NARROWED, not cleared.** No Sbírka act or VeKLEP material sets
  them. Press only (secondary, not a receipt): a bill abolishing automatic indexation and keeping
  the annual vignette at 2,570 CZK in 2027 passed the Chamber around 29–30 Sep 2026 and goes to the
  Senate (novinykraje.cz 30 Sep 2026; e15.cz; denik.cz). Its tisk number was not identified at
  psp.cz this pass. Consumer price, not a business duty, so it would not be staged even when
  enacted unless a duty attaches.
- **170/2026 Sb. ("saved but unread"): CLEARED by the 2026-09-28 SWEEP**, which staged
  `reg-spz-normativy-170-2026` from it (now in the 09-28 ledger). Nothing further owed.
- **Act 166/2026 vs the 09-28 list**: 167/2026 had no line in the 09-28 table; named above.

**EUR-Lex: visited via CELLAR.** Every `32026[RLD]` act with OJ publication date
**2026-09-29 .. 2026-10-05**: **71 CELEX** (`pages/eu/ojL-pub-2026-09-29_10-05.rq` / `.csv`).
**No directive (`32026L…`) in the window.**
- **RECORDED `reg-eu261-revize-2027`** (32026R2202, OJ L 2 Oct 2026; applies 23 Oct 2027). Read in
  full.
- Read by title, not recorded: 32026D2211 (harmonised standards for refrigerating systems and heat
  pumps — reference list); 32026D2209 (Euratom standard document for radioactive-waste shipments —
  niche); 32026R2162 (anti-dumping, Chinese glass beads); 32026D2194 (Spanish excise derogation);
  32026D2221 (European defence projects of common interest).
- Not recorded, by class: CFSP / EPF / missions (2172, 2176, 2179, 2190, 2195–2198, 2206, 2213,
  2231, 2191); CoR / EESC / Cedefop / Court of Auditors appointments (2173–2175, 2177, 2178, 2180–
  2183, 2222, 2225, 05025–05027); animal-disease emergency measures and third-country entry lists
  (2186, 2207, 2215, 2216, 2220, 2188, 2227, 2238); biocide national derogations and Union
  authorisations (2140–2142, 2150, 2153, 2199, 2201, 2203); railway Directive 2016/797 requests
  (2139, 2189); feed additives (2158); GIs (2167, 2168, 2224); molasses prices (2212); port list
  (2155); ESS-ERIC (2166); EEA / Morocco / UK-withdrawal positions (2217, 2219, 2223, 2232, 2233,
  2234, 2237, 2239); Ukraine Facility instalment (2230); Norway contribution (2229); ETS registry
  allocation-table decisions (05089, 05128); two corrigenda (R1744R(01), R1738R(01)).

### Checklist source 4: VeKLEP RIA "Definice problému" — ledger items AND dropped-log repeat offenders

**Sequencing state:** the scripted `veklep` fetch completed (`ok`, HTTP 200, 1,946,918 bytes,
**151 items**). `data/raw/2026-10-05/staged.jsonl` and
`data/signals/regulation/2026-10-05.jsonl` **did not exist** at any check this pass. As on 09-28,
the pass took the set normalize will stage — every payload `Id` whose `veklep-<Id>` is not in
`seen.txt`: **20 materials**.

**THE TWO COUNTS SCANS.md item 4 REQUIRES:**
- **RIA / DZ sections read from the ledger: 2 materials (2 new DZs + 2 cover reports).** The
  7 veklep lines appended to `regulation/2026-09-28.jsonl` were all read on 09-21/09-28 and none
  has an attachment dated after 2026-09-25 (checked against today's payload), so nothing new
  there. Of the 109 already-seen materials in today's payload, **2 gained documents since 26 Sep**
  and both were read: `ALBSDVLDLD32` (eHealth act, final DZ + bill of 30 Sep) and `KORNDVL9Q4OE`
  (procedure-point list, předkládací zpráva of 2 Oct).
- **RIA / DZ sections read from the dropped log: 5 of the 11 veklep lines opened (the 5 that are
  back in today's payload), 4 documents read, 0 re-staged by hand.**

**(a) Dropped-log half — opened FIRST.** `data/signals/dropped-log.jsonl` (4,322 lines) holds
**11 veklep lines**. Sorted by `times_dropped`: **KORNDNSF3ZQ5** (Zlatý potok NPP decree) and
**KORNDSAKSLEQ** (MV schools decree) at **2** (first 09-19, last 09-28; per the 3c known hole, both
may really be 3); the other nine at 1 (first 09-19, read as possibly 2).
- **KORNDNSF3ZQ5** (×2, re-stages today → a third drop): newest DZ `zd_KORNDX9EERH3` (24 Aug)
  re-read. Nature reserve of 429.27 ha + 271.85 ha buffer for the freshwater pearl mussel; 12 people
  and 5 legal persons objected; "mírnou administrativní zátěž" for owners. Nothing quantified that
  the card lacks. **Not re-staged.**
- **KORNDSAKSLEQ** (×2, re-stages today → a third drop): newest DZ `zd_KORNDWDKMAN3` (27 Jul)
  re-read. New MV decree for its own schools; the DZ says no budget, business or third-party
  impact; proposed effect 1 Jul 2026 has lapsed. **Not re-staged.**
- **KORNDW7HRLI7** (prison cell space, ×1; already recorded as `reg-veznice-ubytovaci-plocha-2030`
  on 09-21): **new final DZ and comment settlement of 29 Sep** read (`zd_/vp_KORNDYDJ3W9A`).
  Figures unchanged (19,850 normed places, −2,798, 17,052; 95.47 % → 111.14 %); still asks for
  effect "nejpozději však 31. prosince 2026". Stage moved to **8PK (Legislative Council
  committee)**. The Ombudsman's office and the government's human-rights commissioner objected;
  answered by reference to the *Koncepce rozvoje vězeňství do roku 2035* (resolution 832 of
  29 Oct 2025). Status update only; no new record.
- **KORNDVKKWEK9** (ÚZSVM act, ×1, aged out on 09-28, back today): **new DZ + settlement of
  1 Oct** read (`zd_/vp_KORNDYFJ89C3`). Lets ÚZSVM represent state organisations and kraje
  (free of charge for kraje), lets ministries found state organisations with MF consent, and moves
  state-owned bridges over motorways/class-I roads to ŘSD because many are "v havarijním stavu".
  No count, no money, no business impact. **Not re-staged.**
- **KORNDV37RXI3** (×1, back today): DZ of 17 Sep read; now **enacted as 173/2026 Sb.** — a
  reference update to Reg. (EU) 2026/118, no new duty. **Not re-staged.**
- The other 6 lines (KORNDUAFXG1S, KORNDUEGPUWG, KORNDV4EB4WE, KORNDV7FMSPN, KORNDXRHWVVT,
  KORNDY2HHS8D) are not among today's unseen ids (three are now in the ledger, the others aged
  out); all were read on 09-21/09-28.

**(b) Ledger half.** As counted above. `ALBSDVLDLD32` (eHealth act, held as
`reg-ezadanka-elektronicka-dokumentace-2027`): material moved to **stage 7, submitted to the
government on 30 Sep 2026**, with **three unresolved disputes with ÚOOÚ** (who keeps the patient
summary; breadth of access to the shared health record; the electronic pregnancy record). The
effect clauses are unchanged: 1 Jul 2027, 1 Jan 2028, 1 Jan 2029 (bill text line 837–842).
`KORNDVL9Q4OE` (procedure-point list 134/1998 Sb. for 2027): 386 procedures touched — 112 new,
19 removed, 256 updated; 2027 cost to public insurance estimated 627–644M CZK; substantive
comments from 11 bodies incl. ČLK, HK ČR and the MF; stage 6PK. Used as context in
`reg-cz-drg-2027-174-2026`, not staged on its own.

**(c) The 15 genuinely new materials** (unseen, not in the dropped log):

| veklep id | material | what the document states | outcome |
|---|---|---|---|
| `KORNDY2GNBC7` | MD bill: road-traffic act, Dir. 2024/3237 + 2025/2205 | 12,144 information forms sent 2024–25; ~96 % speeding; "významné dopady" on ORP offices; driver tracing for offences abroad; 3M CZK MD IT; effect 1 Jul / **20 Jul** / 26 Nov 2027 | **RECORDED `reg-preshranicni-vymahani-pokut-2027`** |
| `KORNDYDBGPRF` | NV: extraordinary work visa, agriculture/food/forestry | renews NV 437/2023 (expires 31 Dec 2026) unchanged to 31 Dec 2028: 2,500 applications a year (UA 1,500; BA, GE, MD, MK 250 each); "trvající akutní nedostatek pracovníků"; RIA waived; full exemption from comment procedure | No record: renewal of the status quo, no new duty, no quantified shortage. MATCH note for p-0009 |
| `KORNDYFAKWLD` | ČNB decree: crypto-asset reporting (MiCA) | reporting duties for CASPs from 1 Jan 2027; "cca 11 poskytovatelů" at 1 Jul 2026; annual or quarterly by class | No record: 11 firms. MATCH note for p-0030 (the "11" agrees) |
| `KORNDYDEQE13` | MZ decree 432/2003 Sb.: new category 4 for psychological load | real-time safety-critical decisions + shifts crossing ≥2 time zones; effect 1 Jan 2027; RIA waived | No record: aviation-crew niche. Note for `reg-mpsv-narocne-profese` / `reg-jmhz-rizikove-prace-2027` |
| `KORNDYDA4WEV` | MZe: ÚKZÚZ fee schedule | fee revision for costs, new EU-required proficiency tests | No record: parametric |
| `KORNDYDABALM` | MZe: NLI inspector ID card (EUDR timber) | competence moved from kraje to NLI by 251/2025 Sb. | No record |
| `ALBSDY9FGH6L` | MV: election laws (Dir. 2025/1788, 2026/1194) | mobile-EU-voter information and accessibility duties; 2.5M CZK per election for double envelopes in Prague and statutory cities | No record: no external duty-bearer market |
| `ALBSDYECP6DO` | MO: Military Police act | competence over MoD organisations' property; informants | No record |
| `KORNDYEB2WYW` | NV: civil-service fields and exam equivalence | merges two MV fields | No record |
| `KORNDYDBN5D6` | State budget act 2027 | budget bill (signed) | Title and law-text annex skimmed; no record (no dated duty on business) |
| `KORNDYDBN6FO` | Medium-term budget outlook 2028–29 | — | Title only; no record |
| `KORNDYGGP5U9` | MPs' bill (tisk 327): OSVČ caring for a child up to 7 counted as secondary activity | opposition bill; government opinion pending | No record |
| `KORNDYGGQQUU` | Senate bill (tisk 329): criminal code, limitation periods | — | No record |
| `ALBSDYEFULHG` | MPs' constitutional bill (tisk 320) | PDF text-layer garbled | No record (scanned/garbled; title only) |
| `KORNDV37RXI3`, `KORNDVKKWEK9`, `KORNDW7HRLI7`, `KORNDNSF3ZQ5`, `KORNDSAKSLEQ` | — | counted in (a) | — |

All documents read are saved in `pages/veklep/` as `.docx`/`.doc`/`.pdf` with `.txt` extractions.

---

### Evidence-bar compliance

- **Enacted vs draft:** every `notes` opens with `STATUS:`. 4 ENACTED (Sbírka or OJ dates and
  in-force dates cited), 1 DRAFT (`reg-preshranicni-vymahani-pokut-2027`, nothing in force).
- **Dates** are the day the duty bites: 2026-10-01 (178, 175), 2027-01-01 (174), 2027-07-20 (the
  bill's cross-border provisions, Čl. VI(a)), 2027-10-23 (EU 2026/2202 "shall apply from").
- **Urgency:** 3 for 178 and 175 (in force), 3 for 174 (88 days), 2 for EU261 (383 days) and for
  the draft (≈9.5 months). Scale 3 only for 175 (every employer reimbursing car travel).
- **Money:** `money_eur` null on all 5, each with a `money_note`. The 3M CZK MD IT cost and the
  627–644M CZK procedure-list cost are named in notes and not scored (state or payer cost, not money
  attached to the need — same convention as the 09-28 sweep). Nothing estimated or converted.
- **Quotes:** 5 of 5 verified mechanically as literal substrings (native language: Czech for the
  four CZ instruments, English for the EU regulation, read in its EN expression).
- **Absence claims:** none made; every DEDUP clause names its search terms.
- **Personal data:** e-mail/phone regex on `staged.jsonl`: 0 matches. Decree 178 lists the
  personal fields a CI entity must submit; none were copied as values.

### Dry run (validation only, nothing written to the ledgers)

```
mkdir -p $TMPDIR/reg-sim-1005b && cp -R data/signals $TMPDIR/reg-sim-1005b/
python3 scripts/normalize.py --raw data/raw/2026-10-05/regulation --complete --dry-run --today 2026-10-05 \
    --out-dir $TMPDIR/reg-sim-1005b/signals --seen $TMPDIR/reg-sim-1005b/signals/seen.txt \
    --dropped-log $TMPDIR/reg-sim-1005b/signals/dropped-log.jsonl
  -> normalize --complete --dry-run: would append 5 records across 1 file(s); 0 dropped by
     materiality; 0 incomplete; 0 refused by AC-GDPR1.
     .../reg-sim-1005b/signals/regulation/2026-10-05.jsonl: +5
     dedup by identity key (append): 0 skipped
     AC-GDPR1 allowlist: dropped 10 non-allowlisted field(s) across 5 record(s): _needs, evidence_type
git status --porcelain data/signals   -> (empty)
```
**Owed to the coordinator:** the real
`python3 scripts/normalize.py --raw data/raw/2026-10-05/regulation --complete` and the `db.py
upsert` line it prints.

### Facts in existing records this pass found stale (report only; nothing was edited)

- **`reg-ezadanka-elektronicka-dokumentace-2027`** notes say "VeKLEP stage 3 (comment period closed
  2026-08-03)". The bill was **submitted to the government on 30 Sep 2026 (stage 7)** with three
  unresolved ÚOOÚ disputes. Dates unchanged.
- **`reg-veznice-ubytovaci-plocha-2030`** notes describe the draft "in the VeKLEP comment
  procedure". It is now at **stage 8PK** (settlement of comments dated 29 Sep 2026). Figures unchanged.
- **`reg-eet2-2027` / `reg-mf-eet2-2027`**: still no Sbírka number; psp.cz now records dispatch for
  publication on **1 Oct 2026**.
- **`reg-pohonne-hmoty-strop-2026-10`** treats the travel-allowance revision as a draft knock-on
  (`KORNDXWQDTHG`); it is **enacted as 175/2026 Sb.**, in force 1 Oct 2026.
- **p-0036**, regulation entry for the 2027 reimbursement decree, says "CZ-DRG is the status quo
  rather than a new dated duty". CZ-DRG **version 2027** is now formally issued by **174/2026 Sb.**
  with effect 1 Jan 2027 — new grouper, coding rules and weights every hospital must adopt. Not a
  contradiction of the decree reading, but the "no dated duty" clause should be re-read against it.
- Metadata cards now enacted (cards are not wrong, they are behind): `veklep-KORNDTUBDJRM` →
  178/2026; `veklep-KORNDXWQDTHG` → 175/2026; `veklep-KORNDY2HHS8D` → 176/2026;
  `veklep-KORNDV4EB4WE` → 179/2026; `KORNDV37RXI3` (dropped) → 173/2026.

### MATCH candidates

| record | matches | why |
|---|---|---|
| `reg-ki-portal-178-2026` | **p-0008** (NIS2 / CI capacity) | the enacted channel for CI incident reports and named-user management under 266/2025 Sb., in force now; p-0008 already cites `reg-cer-zakon-266` |
| `reg-cz-drg-2027-174-2026` | **p-0036** (clinical documentation / coding), secondary **p-0022** | annual coding and grouper change on 1 Jan 2027; p-0036's queries already target CZ-DRG grouper and coding modules |
| `reg-eu261-revize-2027` | **no live problem** — new candidate below | |
| `reg-preshranicni-vymahani-pokut-2027` | **no live problem** | municipal-office casework + fleet-operator driver identification |
| `reg-cestovni-nahrady-175-2026` | **no live problem** | payroll/expense parameter; context for the fuel-cap record |
| (finding) `KORNDYFAKWLD` | **p-0030** (MiCA CASP wind-down) | ČNB counts "cca 11" CASPs at 1 Jul 2026, agreeing with p-0030's "all but 11"; survivors get ČNB reporting from 1 Jan 2027 |
| (finding) `KORNDYDBGPRF` | **p-0009** (employment-card automation) | the farm/food/forestry work-visa quota (2,500 a year) is renewed to end-2028, pending the new foreigners act (tisk 144) from 2029 |
| (finding) `ALBSDVLDLD32` | **p-0022 / p-0036** | eHealth bill now before the government; ÚOOÚ disputes over patient-summary ownership and shared-record access |

### New-problem candidates (for MATCH; a scan creates none)

1. **EU261 claim handling after the reform** (`reg-eu261-revize-2027`): every carrier and
   intermediary must run a complaint mechanism with 7-working-day / 1-month / 2-month clocks, send
   compensation information within 96 hours, and keep proof of every notice. Buyers: Czech
   carriers, OTAs and travel agencies selling flights, airports (rights notice). Date-certain
   (23 Oct 2027). Needs a demand leg (ČOI / ÚCL complaint statistics) before MATCH.
2. **Municipal cross-border offence casework** (`reg-preshranicni-vymahani-pokut-2027`):
   translated notices and decisions, driver tracing and fine hand-off at ~206 ORP offices; the DZ
   expects machine translation (eTranslation) and promises no money to towns. Weak: draft, no RIA.

### Coverage gaps named

1. **No fulfilment evaluation of the programme** (carried; recheck ~January 2027).
2. **2027 Plán legislativních prací not published** (expected absence; carried). New: the
   **"Plán legislativních prací vlády na zbývající část roku 2026"** cited by today's drafts is not
   the checklist URL and was not located.
3. **EET 2.0 Sbírka number** (carried; sent for publication 1 Oct, 180+ not yet promulgated).
4. **166/2026 Sb. content** (carried; e-Sbírka text still undigitised, PDF route untried).
5. **Tisk 48** (carried; on the 34th-session agenda from 13 Oct 2026).
6. **2027 vignette rates** (narrowed to press reports of a Chamber-passed freeze at 2,570 CZK;
   primary tisk not identified).
7. **Sequencing:** `data/raw/2026-10-05/staged.jsonl` did not exist during the pass; the 20 unseen
   veklep ids were derived from the payload. If normalize stages anything else, the difference is
   unread.
8. **Not read beyond title/annex:** state budget 2027 (`KORNDYDBN5D6`, 24 attachments incl. a
   15 MB annex), medium-term outlook (`KORNDYDBN6FO`), constitutional bill tisk 320 (PDF text layer
   garbled).
9. **5 Oct cabinet outcomes** not yet published at read time (agenda only).
10. **Standing (from the 09-28 sweep):** 51 MPs'/Senate bills in the backfill whose DZ lives on
    psp.cz; 80 title-set-aside backfill materials incl. 19 deferred. Not a weekly-delta job.

### 5-line pass summary

```
feed:                reg-scan (evidence_type regulation, prefix reg-, weekly delta pass 2026-10-05)
checklist sources:   4 of 4 visited (programme 200 unchanged, no evaluation · plan 2026 unchanged, 2027 not published · e-Sbírka 166–200 (173–179 new) + EUR-Lex CELLAR 09-29..10-05, 71 CELEX, 0 directives · VeKLEP: RIA/DZ read ledger 2 materials / dropped log 5 of 11 lines opened, 4 docs, 0 re-staged + 15 new materials triaged, 9 DZs read)
records staged:      5 (4 ENACTED: 178/2026 CI portal, 175/2026 travel allowance, 174/2026 CZ-DRG 2027, EU 2026/2202 EU261 reform; 1 DRAFT: cross-border fine enforcement), dry-run +5, 0 dropped, 0 refused
coverage gaps named: 10 (5 carried, of which 3 moved/narrowed; 5 new); debts cleared: 170/2026 (by the 09-28 sweep); moved: EET 2.0 (sent for publication 1 Oct), tisk 48 (on agenda 13 Oct), vignette (press only)
rotation state:      n/a (arb-scan duty)
```


## dotace-scan pass — 2026-10-05 (weekly delta)

Weekly delta for the `dotace-scan` feed (`data/feeds.json` key `dotace-scan`, `signal_source: dotace`,
`evidence_type: tenders`, `id_prefixes: ["dotace"]`), run under `pipeline/SCANS.md` (THE CHECKLIST LAW).
Worktree `localproblems-weekly-2026-10-05`. Left-hand side: the 2026-09-28 pass.

Raw captures: `data/raw/2026-10-05/dotace/pages/`. That folder holds the MS2021+ XML snapshot, today's sorted call-id
list, the per-call field diff, two ČNB lists, 5 call-text PDFs with their text (OPD 46, OP FVB 18, OP ST 117 and 118,
OPŽP 107) and 21 portal or call pages.
Staged: `data/raw/2026-10-05/dotace/staged.jsonl` has **4 lines**.
This pass wrote nothing else. It did not touch the ledgers, `seen.txt`, `dropped-log.jsonl`, `register.db`,
`feeds.json`, `errata.jsonl` or the shared `manifest.md`. It ran no `--complete` without `--dry-run`, no `db.py` and
changed no git state.

### Exchange rate

**24.465 CZK/EUR**, from ČNB list **#190 of 02.10.2026**. Requests for `date=02.10.2026` and `date=05.10.2026` were
fetched 2026-10-05 ~07:07Z, before today's 14:30 fixing. Both returned HTTP 200 with the same payload: first line
`02.10.2026 #190`, containing `EMU|euro|1|EUR|24,465`. Both are saved as `pages/cnb-denni_kurz-*.txt`. The opd3.opd.cz
page prints the same "Aktuální kurz eura: 24,465". All 4 records use this rate.

### Checklist source 1: MS2021+ open-data call list

- **Fetch.** `https://ms21opendata.mssf.cz/SeznamVyzev_21_27.xml` returned **HTTP 200, 1,678,175 bytes**, fetched
  2026-10-05T07:05:13Z. The payload reads `DATE="2026-10-04T20:45:00.000+02:00"` (Sunday night's export). Saved as
  `pages/ms21-SeznamVyzev_21_27.xml`, sha256 `b8638ab3a35aef4e6509d58ef1605c66eb661898f36a9a2fad8dab9859a76a2e`.
- **Left-hand side, code level.** This is the 819-code list printed in the 2026-09-28 manifest section. Re-extracted from
  that manifest and verified: 819 codes, and the sha256 of the newline-terminated sorted list is
  `2cbbd8ab807b3c8a0f792ecb973eeec785749a059368838576fb96e5e57a9026`, **exactly the hash 2026-09-28 recorded**.
- **Left-hand side, field level.** The 2026-09-28 XML is gone with its worktree. The 2026-09-19 XML survives at
  `localproblems/data/raw/2026-09-19/dotace/ms21-SeznamVyzev_21_27.xml` in the main checkout. The per-call diff
  therefore ran **09-19 → 10-05**, and every delta the 09-21 and 09-28 sections already documented was subtracted. What
  remains happened between 09-28 and 10-05. Output is in `pages/ms21-diff-2026-09-19-vs-10-05.txt` (112 lines,
  namespace-aware, every leaf field of every `<VYZVA>`, keyed by `KOD`).

**Code diff: 819 → 819. +0 / −0.** Today's sorted list hashes to `2cbbd8ab…7a9026`, byte-identical to the 09-28 list.

**Newly OPENED or DECLARED calls since 09-28 (all minted, none in the ledger):**

| KOD | Call | Change | Window | Allocation | Outcome |
|---|---|---|---|---|---|
| `04_26_046` | OPD 46, ultra-fast car charging ≥150 kW, whole ČR | Finalizovaná → **Otevřená** | 2026-10-14 → 2027-01-06 | 315,000,000 CZK | **staged** `dotace-opd-46-ultrarychle-dobijeci-cela-cr` |
| `13_26_018` | OP FVB 18, asset recovery and confiscation (Dir. 2024/1260) | Plánovaná → **Otevřená** | 2026-09-30 → 2026-12-31 | 62,000,000 CZK | **staged** `dotace-fvb-18-vymahani-konfiskace-majetku` |
| `10_26_117` | OP ST 117, AI/VR teaching in secondary schools, Karlovarský kraj | Rozpracovaná → **Vyhlášená** | 2026-10-14 → 2027-04-30 | 58,823,529.41 CZK | **staged** `dotace-opst-117-ai-vyuka-ss-karlovarsky` |
| `10_26_118` | OP ST 118, the same, Ústecký kraj | Rozpracovaná → **Vyhlášená** | 2026-10-14 → 2027-04-30 | 211,764,705.88 CZK | **staged** `dotace-opst-118-ai-vyuka-ss-ustecky` |

Each record is receipted from the call text itself, not only the XML: `pages/opd-46-text-vyzvy.pdf`,
`pages/fvb-18-text-vyzvy.pdf`, `pages/opst-117-text-vyzvy.pdf` and `pages/opst-118-text-vyzvy.pdf`, each with a `.txt`.
Every quote was verified as a literal substring of the call text after whitespace collapse (`pdftotext`, both layout
and raw modes). 117 and 118 are *Vyhlášená* (declared on 30. 9.; receipt opens 14. 10.). They are minted on the
precedent of OPŽP 107 and OPD 44/45, which were minted before receipt opened, and each record states that status in
its notes.
**A source discrepancy is recorded in the record, not resolved.** The call-117 text (Karlovarský kraj) prints
`Číslo výzvy v MS 10_26_118`. The XML and the opst.cz page put Karlovarský under `10_26_117`. The record follows the XML
and the document's own number "117/2026".

**Other state and field changes, 09-28 → 10-05, none mintable:**
- *Declared, already in the ledger:* `05_26_107` OPŽP 107 went Schválená → **Vyhlášená**. The XML now lists the
  eligible applicant types, and the call text is out (see errata 1).
- *Pipeline, not yet open:* `04_26_047` OPD 47, truck fast charging, 500,000,000 CZK, is still **Rozpracovaná**. It
  becomes accessible 2026-10-31 and opens 2026-11-16. Its page `opd3.opd.cz/stranka/vyzva-47/` returns HTTP 200 and is
  still a stub with no call text (saved).
- *Closures (Otevřená → Uzavřená, all on their 2026-09-30 deadline):* `03_24_059` OP Z+ "Politiky, které fungují"
  (171,959,000 CZK), `06_23_085` IROP 85 public-health protection (119,999,508.88 CZK), `14_26_018` OP NSHV 18
  (290,000,000 CZK) and `14_26_020` OP NSHV 20 (5,000,000 CZK). `03_24_059` and `14_26_018` were open-call backlog
  items (09-28 gap 2). **Both closed unminted.**
- *Allocation change on a closed call:* `01_23_018` OP TAK small hydro plants I (closed 2026-06-30) went
  700,000,000 → **1,100,000,000 CZK**. It is not in the ledger and not mintable, because it is closed.
- State counts today: Otevřená 130, Uzavřená 626, Plánovaná 24, Zrušená 19, Vyhlášená 7, Pozastavená 5, Ukončená 5,
  Rozpracovaná 3.

**Today's full MS2021+ call-id list is the next pass's left-hand side.** It holds 819 codes, sorted. The sha256 of the
newline-terminated list is `2cbbd8ab807b3c8a0f792ecb973eeec785749a059368838576fb96e5e57a9026`, the same convention as
the 09-21 and 09-28 hashes, both of which verified. A copy is also at `pages/ms21-kody-2026-10-05.txt`, but that copy
is pruned at 28 days. The list below is the durable one.

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

Each page was fetched on 2026-10-05 between 07:06Z and 07:15Z and diffed against its 2026-09-19 capture in
`localproblems/data/raw/2026-09-19/dotace/pages/`, using visible text only (tags, scripts, styles and comments
stripped). The 09-21 and 09-28 sections list every 09-19 → 09-28 change, so any change below that they do not list
happened after 09-28.

- **IROP.** `https://irop.gov.cz/cs/vyzvy-2021-2027` returned **HTTP 200**. Three rows went *Otevřená → Uzavřená*:
  `06_23_103` and `06_23_104` (already in 09-28) and, new this week, `06_23_085`. No row was added.
  `…/Vyzvy-2021-2027/Vyzvy/70vyzvaIROP` returned HTTP 200 and is still *Otevřená*. The only change is its statistics
  box (`4. 10. 2026`: 664,634,419 Kč requested, 374 applications, 76.7 %), which is project traffic. **Nothing new.**
  The XML shows no new `06_*` code and no IROP code moving into Vyhlášená or Otevřená.
- **OPŽP.** `https://opzp.cz/nabidka-dotaci/` returned **HTTP 200**. Calls 101–104 and 73 left the listing (closed
  25. 9.). The 107 card now shows *Vyhlášená*, 14. 10. – 25. 11. 2026, `Alokace 100 000 000 Kč`. *Výzva č. 2/2026 FN*
  is visible and already in the ledger (`dotace-sfzp-2-2026-fn-cov`). `https://opzp.cz/dotace/107-vyzva/` returned
  **HTTP 200 and CHANGED**: Plánovaná → **Vyhlášená**, with eight dated documents attached, including *Text výzvy –
  107. výzva* (Platnost 30. 9. 2026). That text was fetched (`pages/opzp-107-text-vyzvy.pdf`, HTTP 200). It reads
  "vyhlašuje ke dni 30. 9. 2026", receipt "od 14. října 2026 (9:00) do 25. listopadu 2026 (20:00)" and allocation "ve
  výši 100 mil. Kč" (EU share). These are the ledger's values, so only the status caveat is now stale (errata 1).
  **No new call.**
- **OPJAK.** `https://opjak.cz/vyzvy/` returned **HTTP 200**, and `https://opjak.cz/harmonogram-vyzev/` returned
  **HTTP 200**. Both are unchanged since 09-28: the only differences from 09-19 are the 2027 v1 and 2026 v3 schedule
  links and the dashboard percentage (now 57 %), all documented on 09-28. No call row was added. **Nothing new.**
- **SFŽP.** `https://sfzp.gov.cz/dotace-a-pujcky/`, `…/dotace-a-pujcky/financni-nastroje-a-pujcky/` and
  `…/dotace-a-pujcky/modernizacni-fond/vyzvy/` all returned **HTTP 200**. The first two are text-identical to 09-19. The
  MF page's only change is the TRANSGov 2 allocation 7,175,000,000 → 10,175,000,000 Kč, already reported on 09-28 and
  already in `errata.jsonl`. **No new call.** A URL note for the next pass: the short form
  `sfzp.gov.cz/modernizacni-fond/vyzvy/` now **301s to `/faq/vyzvy/`**, a generic homepage-like page. Use the full
  `/dotace-a-pujcky/modernizacni-fond/vyzvy/` path. This pass first fetched the short form by mistake, caught it, and
  re-fetched the full one. The SFŽP news column also shows "01.10.2026 … MŽP vyhradilo 100 milionů korun na modernizaci
  ekocenter", which is OPŽP 107.
- **NPO.** `https://planobnovy.gov.cz/vyhlasene-vyzvy/` returned **HTTP 200**. Rows were removed and none added: the
  component 7.3 calls *NPO č. 14/2025 (SECAP+)* and *č. 16/2025 (semináře)* dropped off after their 30. 9. 2026 close.
  **Nothing new.**
- **TAČR.** `https://tacr.gov.cz/` returned **HTTP 200**. The box dropped RAMP and added a PRODEF *feedback survey*
  ("Pomozte nám nastavit další směrování Programu PRODEF") and the *Ceny TA ČR 2027* nominations. Neither is a funding
  call. `https://tacr.gov.cz/programy-a-souteze/` returned **HTTP 200**: FOREST went "V přípravě" → "Běží lhůta"
  (already in the ledger), and TREND, SIGMA and RAMP rotated out of the calendar. **No new competition.**
- **CINEA / HaDEA.** `https://cinea.ec.europa.eu/funding-opportunities/calls-proposals_en` returned **HTTP 200**. It
  lists **10** "Upcoming and open" calls, all on page 0 and title-for-title the same 10 as 09-28: CEF Transport 2026,
  HE fair transition €45 M, Cities Mission €85.5 M, batteries and mobility €263 M, energy supply €23.5 M, NEB Facility
  €101.1 M, HE energy €131.5 M, PSLF, LIFE SNaP and LIFE SIP CLIMA. `https://hadea.ec.europa.eu/calls-proposals_en`
  returned **HTTP 200 and CHANGED**, from 4 to **2** calls. DEP Call 10 *Advanced Digital Skills* and *Accelerating
  Best Use of Technologies* closed on 1 Oct. **`CEF-DIG-2026-CABLE-REPAIR-CAPACITIES` had its deadline moved
  8 Oct → 25 Nov 2026.** That call is not in the ledger: it is a carried gap (CEF-DIG budget owed since 09-21) and not
  newly opened (gap 1). SMP Food is unchanged (15 Oct). **No new call.** No 429s this pass.
- **Beyond the floor, visited because the XML diff pointed there:** `https://opd3.opd.cz/stranka/vyzva-46/` (200),
  `/vyzva-47/` (200, stub), `https://opd3.opd.cz/` (200), `https://mv.gov.cz/fondyeu/vyzvy-fvb-2` (200) and the
  18-call page (200), `https://www.opst.cz/` (200), `https://opst.cz/dotace/117-vyzva/` and `/118-vyzva/` (200),
  and the five call-text PDFs (all 200).

**Checklist: 8 of 8 sources visited**: the MS2021+ XML plus IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO and CINEA/HaDEA. Each
is named above with its URL and HTTP status.

### Records staged: 4

| id | date | money_eur | scores s/m/u/r | sector |
|---|---|---|---|---|
| `dotace-opd-46-ultrarychle-dobijeci-cela-cr` | 2027-01-06 | 12,875,536 | 2/3/3/2 | mobility |
| `dotace-fvb-18-vymahani-konfiskace-majetku` | 2026-12-31 | 2,534,233 | 1/3/3/1 | govtech |
| `dotace-opst-117-ai-vyuka-ss-karlovarsky` | 2027-04-30 | 2,404,395 | 1/3/2/1 | education |
| `dotace-opst-118-ai-vyuka-ss-ustecky` | 2027-04-30 | 8,655,823 | 1/3/2/1 | education |

Every record carries `evidence_type: tenders`, `extraction: manual`, `_needs: []`, a verbatim quote from the call
document of 300 characters or fewer, and an English "Thing — what it is" title. **Dedup:** none of the 4 ids is in
`seen.txt`, and no ledger record carries their URLs (grep across `data/signals/**`).
**Dry run** against a scratch copy:

```
cp -R data/signals $TMPDIR/dotace-sim-1005/
python3 scripts/normalize.py --raw data/raw/2026-10-05/dotace --complete --dry-run --today 2026-10-05 \
    --out-dir $TMPDIR/dotace-sim-1005/signals --seen $TMPDIR/dotace-sim-1005/signals/seen.txt \
    --dropped-log $TMPDIR/dotace-sim-1005/signals/dropped-log.jsonl
normalize --complete --dry-run: would append 4 records across 1 file(s); 0 dropped by materiality; 0 incomplete; 0 refused by AC-GDPR1.
  .../dotace-sim-1005/signals/tenders/2026-10-05.jsonl: +4
  dedup by identity key (append): 0 skipped
  AC-GDPR1 allowlist: dropped 8 non-allowlisted field(s) across 4 record(s): _needs, evidence_type
```

`git status --porcelain data/signals` is **empty** after the run.

### MATCH candidates

Under SCORING.md MONEY, a grant is at most PUBLIC MONEY NEARBY (0 on its own). It can lift a record 1 → 2 only if
the record already has an ASKING price receipt, the programme names that record's buyer type as eligible and its job
as eligible spend, and the buyer co-pays. Against `data/problems/cz/*.md`:

- **OPD 46** (eligible applicants are owners of public-access charging infrastructure with a Czech IČ; 55 % EU share,
  min. 45 % co-pay). It sits next to **p-0046-electric-bus-fleet-finance** (buyer `public`, city bus companies), but
  that record's job is depot charging and bus finance, not public-access car chargers. **Public money nearby only,
  no lift**: the job is not eligible spend.
- **OP ST 117 / 118** (sole eligible buyer is the Karlovarský or Ústecký *kraj* as school founder; 85 % max., so
  the region co-pays 15 %; eligible spend is AI/VR teaching tools, teacher training and school-administration
  efficiency). The closest record is **p-0042-special-needs-assessment-backlog** (buyer `public`, schools), whose job is
  remote psychologist and special-educator help. The call's activities do not name it. **Public money nearby at
  most, no lift.** There is no register record for AI in schools, so this is a possible new-problem lead for MATCH,
  not a match.
- **OP FVB 18** (eligible are only the Police Presidium and Zařízení služeb pro MV). **No problem.**
- **OPŽP 107** (unchanged record; eligible are municipalities, regions, schools, NGOs and others). **No problem.**

### Errata candidates (for the coordinator; this pass did not write `data/errata.jsonl`)

1. `dotace-opzp-107-environmentalni-centra`: the **status caveat is stale**. The notes say "opzp.cz lists the call as
   'Plánovaná' … no call text PDF is attached yet … drop it if the register requires a formally declared call". The call
   is now **declared**: the XML has `05_26_107` *Vyhlášená*, opzp.cz shows *Vyhlášená*, and the call text says
   "vyhlašuje ke dni 30. 9. 2026". The values are unchanged: window 14. 10. – 25. 11. 2026, 100 mil. Kč EU share. This
   is `source-updated`, `value_is_correct: true`, annotate-only. Receipts: `pages/opzp-107-text-vyzvy.pdf` and `.txt`,
   `pages/opzp-107-vyzva.html`.

No other published value on a ledger record changed at source this week. The OPD 44/45 dates and the TRANSGov 2
allocation from 09-28 are already in `errata.jsonl`. The XML still matches those corrected values: 44/45 close
2026-12-07, and TRANSGov 2 is 10,175,000,000 Kč on SFŽP.

### Coverage gaps (named, not silent)

1. **EU topic conditions are still owed** (carried from 09-21 and 09-28). They are the funding rates for
   `HORIZON-CL5-2026-11` and `SMP-FOOD`, the **CEF-DIG budget** (the cable-repair call is still open and its deadline
   is now 25 Nov 2026, so it can still be minted), `HORIZON-CID/MISS-CANCER/CL4-2026-03`, and the LIFE TA/PLP
   identifiers. Whether to mint the closed LIFE-2026 SAP family retroactively is still the coordinator's call.
   `ec.europa.eu` call-document PDFs were not opened this pass.
2. **Open-call backlog is still owed** (09-18/09-21/09-28). Updated against today's XML: `03_24_059` (OP Z+ "Politiky,
   které fungují", 172 M CZK) and `14_26_018` (OP NSHV 18, 290 M CZK) **closed 2026-09-30 unminted**, the same fate as
   AMIF `12_26_046` last week. Still open and not in the ledger: `10_25_089` (OP ST, closes 2026-11-04), `03_23_058`
   (OP Z+, closes 2026-11-30), `01_24_043` OP TAK Inovační vouchery IV (350 M CZK), and the IROP, OPD `04_25_038`,
   OP Z+ `03_24_062/03_22_012`, OP ST `10_25_095/10_26_110` and OP NSHV `14_26_019` items, none re-examined this pass.
   This backlog keeps losing calls to their deadlines, so a dedicated backfill sweep is the remedy, not the weekly
   delta.
3. **OPD 47 (trucks, 500 M CZK) is not yet declared.** It is Rozpracovaná, accessible from 2026-10-31, and its page is
   a stub. The 2026-10-12 pass may still see a stub. The 10-19 pass or later mints it once the text exists.
4. **OP JAK planned calls** are unchanged since 09-28: `02_25_044` (opens 2026-11-24), `02_25_045`, `02_26_046`,
   `02_27_049` and `02_27_050`. The 2026 v3 and 2027 v1 schedule PDFs were not re-read line by line this pass.
5. **Field-level left side reconstructed again.** The 09-28 XML is gone, so the diff ran against 09-19 and subtracted
   the documented deltas. The code-level left side verified by hash. **Next pass:** this pass's XML is in `pages/`. Use
   it directly while it survives the 28-day prune, and keep a copy outside the worktree if worktrees keep being removed.
6. **Not repeated this pass:** the IROP deep AJAX walk, the OPŽP POST API and the IROP status filters. The XML shows no
   delta that would need them.

### Pass summary (5 lines)

```
feed:              dotace-scan (weekly delta, 2026-10-05; left-hand side = 09-28 call-id list, 819 codes, hash-verified)
checklist sources: 8 of 8 visited — MS2021+ XML (200, 819→819, +0/−0; 2 opened + 2 declared by state change) + IROP, OPŽP, OPJAK, SFŽP, TAČR, NPO, CINEA/HaDEA
records:           4 staged — OPD 46 (315 M CZK), OP FVB 18 (62 M CZK), OP ST 117/118 AI in schools (58.8 / 211.8 M CZK); dry run 4/0/0/0, data/signals untouched
coverage gaps:     6 named — EU topic conditions (CEF-DIG cable repair re-dated to 25 Nov); open-call backlog (OP Z+ 03_24_059, OP NSHV 14_26_018 closed unminted); OPD 47 pending; OPJAK planned; field-level left side reconstructed; deep walks not repeated
errata candidates: 1 — dotace-opzp-107 status caveat now stale (call declared 30. 9. 2026; values unchanged)
```


## arb-scan pass — 2026-10-05 (weekly delta)

This was an attended pass in worktree `localproblems-weekly-2026-10-05`, branch `weekly/2026-10-05`. It only staged records. This pass did not write to `data/signals/**`, `seen.txt`, `dropped-log.jsonl`, `data/register.db`, `feeds.json`, the shared `data/raw/2026-10-05/manifest.md` or `staged.jsonl`, or any problem record. It changed no git state.

**Outputs:**

- `data/raw/2026-10-05/funded/staged.jsonl` holds **13 records**. Each one has:
  - `"evidence_type": "funded"`
  - `"_needs": []`
  - a structured `cz_check`
  - a verbatim `quote` that was mechanically verified
- `data/raw/2026-10-05/funded/manifest-section.md` is this file.
- `data/raw/2026-10-05/funded/pages/` holds 106 payloads. These are every page quoted or cited below, including:
  - the 403 bodies
  - the EU-Startups RSS item extracts (`eustartups-rss-*.txt`)

**Window.** The previous pass ran on 2026-09-28. Records fall into three groups:

- **Strict window (announced 2026-09-28 to 10-05), 7 records:**
  - `fr-voltaback` and `pt-frank` (10-01)
  - `dk-trypcom` (09-30)
  - `de-kuro` and `dk-good-tape` (10-02)
  - `fr-marble` (09-29)
  - `dk-pandektes` (10-05)
- **Owed from the 2026-09-28 pass, 3 records.** These were announced 09-22 to 09-24 and were not in any ledger:
  - `it-gamindo` and `es-reply-next`, which were held for an education pass and a retail pass
  - `fr-relaisante`, which comes from the tech.eu 09-28 weekly recap that the last pass owed
- **Older rounds found by the category sweep, 3 records.** None was in any ledger:
  - `it-nando` (2026-02-16)
  - `de-ark-climate` (2026-02-26)
  - `gb-xylo` (2026-07-01)

Each record carries the round date in `date` and states its provenance in `money_note`.

### The checklist source for this feed: THE CATEGORY-ROTATION DUTY

All 12 categories are named below. The starting rotation state was read from the `## arb-scan pass — 2026-09-28` section of `data/raw/2026-09-28/manifest.md`. The arb-record counts are the `source: arb-scan` lines in `data/signals/funded/*.jsonl` before this pass, 234 in total.

This pass covered the four longest-unswept categories (last swept 2026-09-19), then all four categories that sat at 2026-09-21. That is **8 categories swept**.

- **Swept** means category-targeted listing reads (tech.eu tag feeds for climate-tech, mobility, edtech, govtech and proptech), web searches, and a Czech check on every candidate staged.
- **fintech and health also received one record each.** In both cases the record turned up in the window listings rather than in a sweep of the category. Their last-swept dates therefore do **not** advance.

| category | last swept BEFORE | arb records before | covered this pass | records staged | last swept AFTER |
|---|---|---|---|---|---|
| other | 2026-09-19 | 7 | **YES** (owed) | 1 (`dk-good-tape`) | **2026-10-05** |
| mobility | 2026-09-19 | 10 | **YES** (owed) | 2 (`fr-voltaback`, `dk-trypcom`) | **2026-10-05** |
| housing | 2026-09-19 | 13 | **YES** (owed) | 1 (`de-kuro`) | **2026-10-05** |
| environment | 2026-09-19 | 18 | **YES** (owed) | 2 (`it-nando`, `de-ark-climate`) | **2026-10-05** |
| govtech | 2026-09-21 | 7 | **YES** | 1 (`gb-xylo`) | **2026-10-05** |
| education | 2026-09-21 | 10 | **YES** | 1 (`it-gamindo`) | **2026-10-05** |
| legal-compliance | 2026-09-21 | 13 | **YES** | 2 (`dk-pandektes`, `fr-marble`) | **2026-10-05** |
| retail-services | 2026-09-21 | 17 | **YES** | 1 (`es-reply-next`) | **2026-10-05** |
| energy | 2026-09-28 | 19 | no | 0 | 2026-09-28 |
| fintech | 2026-09-28 | 23 | no (window extra only) | 1 (`pt-frank`) | 2026-09-28 |
| health | 2026-09-28 | 31 | no (window extra only) | 1 (`fr-relaisante`) | 2026-09-28 |
| b2b | 2026-09-28 | 66 | no | 0 | 2026-09-28 |

**Where the next pass starts.** It starts from the four categories at 2026-09-28, thinnest first: `energy` (19), `fintech` (24 after this pass), `health` (32), `b2b` (66). The b2b debt carried from 09-28 is Kontext (DE, runtime security for AI agents). The eight categories swept today go last. Every category has now been swept within the last 17 days.

### Sources walked, each named with what it gave

| source | result |
|---|---|
| **tech.eu RSS** `https://tech.eu/feed/` | HTTP 200, 118 KB, 20 items from 2026-09-30 to 10-04 (`listing-techeu-feed.xml`). It gave Voltaback, FRANK, Tryp.com (via the round-up), Good Tape, Ahron, Restate, Deepslate, Osavul and Foundational. **`?paged=2` and `?paged=3` return the identical 20 items**, so pagination does not work. See GAP 4. |
| **tech.eu weekly recap 2026-09-28** (owed by the 09-28 pass, GAP 1 there) | HTTP 200 (`roundup-techeu-weekly-2026-09-28.html`), read in full: 65+ deals for 09-21 to 09-25. **Debt paid.** It gave Relaisanté (staged) and confirmed Gamindo and Reply Next (staged). It listed Noxtua's raise of more than EUR 100M with C.H.BECK taking a majority stake, which is cited on `dk-pandektes`. Unexamined in-recap items are listed under rejections. |
| **tech.eu Friday round-up 2026-10-02** | HTTP 200 (`roundup-techeu-2026-10-02.html`), read in full. It gave Tryp.com, Ahron, bilt.me, Sovera, Kyndred, Voi RCF, Reverion, Onomondo and Nscale, plus the Lottie/CareMaster and Robotiq.ai M&A. |
| **tech.eu Monday recap for 09-29 to 10-03** | **Not published at fetch time** (2026-10-05, about 07:20 UTC). `https://tech.eu/2026/10/05/` returned 404. The Friday round-up stands in for it. See GAP 3. |
| **tech.eu home** | HTTP 200. The newest item was dated 10-04. |
| **tech.eu tag feeds** (the category sweep) | `climate-tech`, `mobility`, `edtech`, `govtech` and `proptech` all returned HTTP 200. The climate-tech and govtech tags are stale (newest items are from 2024 and July 2026), so environment and govtech had to be swept by search. The mobility tag gave FRYTE (09-09, not examined) and Bikekey. The edtech tag gave Gamindo and Eevi. |
| **EU-Startups RSS** `https://www.eu-startups.com/feed/` plus `?paged=2..4` | All HTTP 200, 40 items from 09-28 to 10-05. **NEW ROUTE: each RSS item carries the full article text in `content:encoded`.** Article pages are still behind the Cloudflare 403, but the article text can be receipted from the site's own feed, so GAP 2 of 09-28 is half closed. Records from this route: Kuro, Pandektes, Marble and Good Tape, saved as `eustartups-rss-*.txt`. Other items it gave: Rayon, Everphone, KHOY, Klang, Metaview, Revnu, Voi, Blue Health Intelligence and Reactive Technologies. |
| **EU-Startups weekly round-up (Sept 28 – Oct 02) and tag feeds** | **403** (Cloudflare "Just a moment..."). This covers the round-up page and all six `/tag/*/feed/` URLs tried (cleantech, climate-tech, govtech, edtech, proptech, mobility). Bodies saved. See GAP 2. |
| **Sifted RSS** `https://sifted.eu/feed` | HTTP 200, 24 items from 09-30 to 10-05. No in-category funding round. The items were Summit coverage, funds (DIG, scale-up funds), ElevenLabs, Oura and the Nubank/Monzo deal. No article page was opened. |
| **Vestbee** `/insights`, `/insights/category/deals`, `/insights/latest-news` | All HTTP 200. Posts listed: Ahron, Inbolt, Onomondo, Osavul, Occam Industries, Spotable, BlackSwan Space, m-fly, CuspAI and LAUNCHub. The Ark Climate article (2026-02-26, HTTP 200) was reached through search. The sitemap was not re-probed, because it was retired as a route on 09-28. |
| **CzechCrunch RSS** | `www.czechcrunch.cz/feed/` now redirects to **`cc.cz/feed/`**, which returned HTTP 200 with 10 items from 10-04 to 10-05. All are lifestyle and portrait pieces with **no Czech funding round**. The feed shows only the latest 10 items. See GAP 5. |
| **Company and press pages** | NANDO's own release (200), Munich Startup (200), The BAE and Soapbox for Xylo (200), startup.eu (200), Maddyness for Relaisanté (200) and startupbusiness.it / CDP VC for NANDO (200). |
| **ARES** (`ekonomicke-subjekty/vyhledat` POST and `/ekonomicke-subjekty/{ico}`) | HTTP 200 on every call. There were 34 name or IČO lookups. The control `Wultra` returned 03643174 (2014-12-15). Every IČO in a `cz_check` was resolved. **INISOFT returned no hit**; see GAP 6. |
| **Czech-side pages** | 40+ pages were fetched and saved as `cz-*.html` (vendor sites, Czech trade press, MMR and ISVS, PF UK library). All returned 200 except `bystriceph.cz` (404, saved) and `amperepoint.cz`, which redirected to `.com` and was blocked by the sandbox (not retried, not cited). |
| **Own ledgers** | Checked: `data/signals/funded/*.jsonl` (6,202 lines), `seen.txt` (19,623 ids), `data/lookup/cz-contract-parties.jsonl` (14,918 lines) for public-buyer limbs, and `data/problems/cz/*.md`. |
| **Web search** | 37 searches in total: 9 discovery and receipt searches, and **28 Czech-language searches** (gap-check queries plus one KROS user-count receipt search). The Czech queries are recorded verbatim in each record's `cz_check.queries` and `notes`. |

### COVERAGE GAPS (named, with what a future pass owes them)

1. **The tech.eu weekly recap for 09-29 to 10-03 was not out at fetch time.** **Owed:** the next pass reads it first. Rounds in its own categories go in that pass. Rounds in the eight categories swept today are fair game as extras.
2. **EU-Startups article, round-up and tag pages are all Cloudflare-403.** The main RSS feed (`/feed/` and `?paged=N`) carries the full article text in `content:encoded`, and that is now the standing route. **Owed:** the weekly round-up list itself (the full deal table) is unreachable without a real browser session (`agent-browser`).
3. **The tech.eu feed ignores `?paged=`**, so items older than the newest 20 are reachable only through recaps, the home page and tag feeds. **Owed:** nothing, as long as each pass reads the Monday recap.
4. **The tech.eu climate-tech and govtech tag feeds are stale**, with newest items from 2024 and July 2026. The site does not tag those categories reliably. **Owed:** sweep environment and govtech by search, as this pass did.
5. **CzechCrunch moved to `cc.cz`** and the feed exposes only the latest 10 items. The 10 items read contained no Czech round. Czech rounds from 09-28 to 10-03 were **not** checked on cc.cz itself. **Owed:** a pass that wants Czech rounds should read `cc.cz/kategorie/startupy/` or an equivalent listing. The scripted `cc-cz` feed row in `feeds.json` names the old URL; that is for the owner to note, and this pass did not touch `feeds.json`.
6. **INISOFT's legal entity was not resolved.** The brand gets no ARES hit and the site's form points to `envita.cz`. On `it-nando` the player is recorded with a URL and no IČO. **Owed:** resolve the IČO before any problem record cites INISOFT in `locals[]`.
7. **The Bystřice pod Hostýnem page that names AI Efektivia s.r.o. as contractor returned 404 on re-fetch.** The link between AI Efektivia and the funded project rests on a search-result snippet, and the IČO is from ARES. **Owed:** if `gb-xylo` ever moves a gap, re-receipt the contractor from the town's contract register (smlouvy) or the MMR project file.
8. **Vendors for the six other MMR-funded "AI pro stavební úřad" projects are unknown** (Aš, Lovosice, Židlochovice, Valašské Klobouky, Vizovice, Úpice). **Owed:** search `smlouvy.gov.cz` for each town's AI contract. One of them could be an established direct seller, which would move `gb-xylo` from contested to taken.
9. **Some maturity limbs were not receipted:** Callida (euroCALC), ČEZ futurego (first generation dated only to "the year before Oct 2024"), C. H. Beck (Beck-Noxtua) and BROKER OFFICE (MIA). Each is recorded as early *on the test*. No verdict rests on any of them except `fr-voltaback`. If futurego's launch is shown to be before 2023-10 and a customer limb is found, `fr-voltaback` becomes taken. **Owed** to MATCH before any use.
10. **Schema validation was mechanical, not zod.** The `CzCheckSchema` and `CzPlayerSchema` invariants were checked in Python on the staged lines and all 13 pass. These checks covered the verdict against the players, `control.passed`, ≥2 queries for absent and contested, 8-digit IČO, and URL or IČO on every player. The build will run the real check.
11. **Not re-visited this pass, still owed:**
    - signteq (AT, legal-compliance), whose amount is still not receipted
    - Kontext (b2b)
    - Companion.energy (energy)
    - Humanos (fintech)

### Dedup suppressions — found, NOT staged

- **Tandem Health** (SE): already staged as `se-tandem-health` after the `se` prefix was added. The 09-28 GAP 5 is closed.
- **Pollen** (motorcycle battery swap): `round-pollen`.
- **Octostar** (IE): `ie-octostar`.
- **Tingit**: `round-tingit`.
- **Adaptavate** (UK, in the 09-28 recap): `round-adaptavate`.
- **Revnu**: `yc-revnu`.
- **Kontext**: `sk-kontext` is in seen.txt with a different company prefix. The DE Kontext round stays owed to b2b; check before minting.

### Candidates examined and rejected (so the selection is not silent)

**Rejected on the merits:**

- **Rayon** (FR, EUR 10M Series A, 2026-09-29, browser CAD for interior designers, housing). Not staged: it is a horizontal design tool, and no Czech check was run this pass. **Owed** to the next housing pass.
- **Scalera** (CH, EUR 5.7M seed, May 2025, AI for construction and public procurement bids). The only full receipt is the 403 EU-Startups page, and finsmes was not fetched. **Owed:** it is a natural second comparable for `de-kuro` / p-0007.
- **Ahron** (DE, EUR 2.2M, 2026-09-30, AI agents over enterprise HR systems). This is the same model as `is-50skills`, which was checked *taken* on 09-28 (ALVENO, Sloneek). A second record would add nothing.
- **Klang** (SE, EUR 1.32M, 2026-09-28, conversation transcription with a Swedish model). This is the same model as `dk-good-tape`, so it was covered by that check and not double-staged.
- **Everphone** (DE, EUR 15M), **Voi** (SE, EUR 150M RCF) and **Trustly** (SE, USD 40M equity commitment). These are debt facilities or shareholder top-ups, not a new model.
- **KHOY** (FI, EUR 2M, vacuum-packed sofa beds) and **ANote Music** (LU, EUR 2M, music royalties as an asset class). Consumer product or niche asset with no buyer-side problem the register tracks.
- **Defence, deeptech and infrastructure**, which have no register buyer:
  - Osavul, DOD Solution, Quantum Systems, ARX Robotics, Foundational
  - Inbolt, Onomondo, Restate, Deepslate, Nscale, Reverion, Reactive Technologies
  - Breye, Omnio, Blue Health Intelligence (health, not owed)
- **Funds and M&A** (not rounds):
  - Headline, DIG Ventures, LAUNCHub, Sofinnova, Eureka!
  - Lottie/CareMaster, Kortext/StudyStash, HCLSoftware/Robotiq.ai
  - The Lottie/CareMaster deal is worth noting for p-0011 (care-agency ops).
- **Manty** (FR govtech). The round web search surfaced is from **2020-03-02** (tech.eu govtech tag), so it is stale.
- **Ulobby** (DK, political tracking). Not receipted.
- **NANDO's sister model Orbisk** is already held as `nl-orbisk`. NANDO was staged because it adds the municipal-collection half.

**Unexamined, recorded so their absence is visible:**

- From the 09-28 recap, in categories not owned this pass: Pekata, Tundr, Spiich, Stasher, InspectRail, OKCargo, Givestar, Usawa Care, Tucuvi, Mirai RiskTech, Benford, Zeliq, Primo, Tiledesk, Aniwa, Spott.
- From the Vestbee listings: Occam Industries, Spotable, m-fly, BlackSwan Space.

### Records — 13 staged in `data/raw/2026-10-05/funded/staged.jsonl`

The verdict vocabulary is unchanged:

- **absent:** no Czech seller found, ≥2 query shapes, control passed
- **contested:** sellers exist, none established
- **taken:** an established direct seller exists

| id | category | what | money (as stated) | date | maturity abroad | CZ verdict |
|---|---|---|---|---|---|---|
| `fr-voltaback` | mobility | home-charging reimbursement for company EVs, from car and meter data | EUR 2.8M | 2026-10-01 | early on test (traction limb only) | **contested**. ČEZ, a. s. (45274649) sells the futurego cable with a billing meter and an employer dashboard; it is direct and early on test. Chargee eMobility (03947092) and MyBox (07750471) are adjacent. |
| `dk-trypcom` | mobility | multimodal trips sold as one booking | EUR 1.9M | 2026-09-30 | established (2021; 10M users) | **taken**. Kiwi.com s.r.o. (29352886, 2012; "used and trusted by millions"). |
| `de-kuro` | housing | AI for general contractors: reads documents, estimates, evaluates subcontractor bids | EUR 10M | 2026-10-02 | early (founded Nov 2024) | **taken**. ÚRS CZ a.s. (47115645; KROS with OFERTA and bid comparison plus an AI assistant; "thousands" of daily users). Callida (65415183) is early on test. RozpočetPRO and cifro are early. |
| `it-nando` | environment | computer-vision waste measurement for collection operators and canteens | EUR 3.3M | 2026-02-16 | established (2021; about 80 clients) | **taken** on the municipal half. INISOFT (RFID plus weighing smart collection; SOMPO since 2013/2017). No Czech camera-based canteen seller was found. |
| `de-ark-climate` | environment | software plus advisory to run and track municipal climate action | EUR 2.1M | 2026-02-26 | early (est. 2024; 43 municipalities) | **absent**. Adjacent only: ASITIS s.r.o. (07836686, SECAP consultancy) and CI2, o.p.s. (26415585, KLIMASKEN assessment). |
| `gb-xylo` | govtech | AI agents that prepare planning applications for officers | GBP 2.8M (EUR 3.3M per startup.eu) | 2026-07-01 | early (pre-seed) | **contested**. AI Efektivia s.r.o. (19760680, 2023) is direct and early. VITA software (61060631) is adjacent. The MMR is funding AI pilots in 7 building offices. |
| `dk-pandektes` | legal-compliance | AI legal research on its own structured legal database | EUR 13.5M Series A | 2026-10-05 | established (2022; 500+ customers) | **taken**. ATLAS consulting (46578706, CODEXIS with AI) and Wolters Kluwer ČR (63077639, ASPI); the named customer for both is PF UK. C. H. Beck (24146978, Beck-Noxtua) is early on test. |
| `fr-marble` | legal-compliance | no-code, open-source fraud and AML monitoring | EUR 6.5M Series A | 2026-09-29 | established (2021; 100+ institutions) | **taken** on the fraud half. ThreatMark s.r.o. (04222091, 2015; Česká spořitelna). AML solutions (10691766) is adjacent. No Czech no-code AML engine was found. |
| `dk-good-tape` | other | secure AI interview transcription | EUR 600k | 2026-10-02 | established (2022; 3M users) | **taken**. NEWTON Technologies, a.s. (28479777; Beey, "více než 50 000" users; ČT, Nova, Prima). |
| `pt-frank` | fintech (extra) | AI operator for broker paperwork across insurer portals | EUR 2.9M | 2026-10-01 | early (<12 months selling) | **contested**. BROKER OFFICE / MIA (47912057) and SpireusNeo are direct and early on test. Insurer-side claims AI is adjacent. |
| `it-gamindo` | education | no-code interactive and gamified corporate training | EUR 1.4M seed | 2026-09-22 | early on test (founding year not in source) | **taken**. KONTIS s.r.o. (62416448, 1994; iTutor, 300+ firms, České dráhy, CETIN). Clashing is early. |
| `es-reply-next` | retail-services | AI review and local-presence management for multi-location brands | EUR 400k pre-seed | 2026-09-24 | early | **contested**. SUPPOO (direct, early), Reviewly (23224061, 2025) and Reputive / OnTarget Labs (23894865, 2025). |
| `fr-relaisante` | health (extra) | hospitals match discharged patients to home nurses and carers | EUR 6M | 2026-09-23 | early (launched 2026; 315 establishments) | **absent**. Medevio (09675400) is adjacent. Discharge in Czech hospitals is arranged by phone by health-social workers. |

**Positive control (MATCH §4), run 2026-10-05 by this pass, two limbs on every record:**

- **(a)** ARES name search `Wultra` returned Wultra s.r.o., IČO 03643174, datumVzniku 2014-12-15.
- **(b)** In each record's own domain, a Czech descriptive query surfaced a known Czech vendor: MyBox, Kiwi.com, ÚRS/Callida, INISOFT, ASITIS, VITA software, CODEXIS/ASPI, ThreatMark, Beey, MIA/SpireusNeo, KONTIS, SUPPOO and Medevio.
- **Exceptions:**
  - `fr-marble` and `dk-good-tape` rest on limb (a) for the control.
  - The Good Tape query named the incumbent, so it is a confirmation query, not a discovery query. That is acceptable for a *taken* verdict, which asserts a positive.
- **The control PASSED on all 13.**

**Mechanical checks run before writing, all passing** (`/tmp/claude-501/build_staged.py` refuses to write otherwise):

- Every `quote` is a literal substring of its saved payload after whitespace collapse, and is ≤300 characters (80–236).
- Every `id` prefix is the lowercase ISO2 of its `geo_origin`. All prefixes (fr, dk, de, it, gb, pt, es) are in arb-scan's `id_prefixes`. **No prefix is missing.**
- No `id` is in `seen.txt`, and no `url` appears anywhere in `data/signals/**`.
- `scores.money` matches the ladder against `money_eur`. No record trips the materiality filter: every record has money ≥2 and scale ≥2.
- `http_status` is omitted on the four EU-Startups records, because their URLs answer 403. Their text was read from the RSS item, and the `money_note` says so.

**Dry run** against a scratch copy of `data/signals` (`$TMPDIR/arb-sim-1005-a/signals`):

- **Command:**
  `normalize.py --raw data/raw/2026-10-05/funded --complete --dry-run --today 2026-10-05 --out-dir <scratch>/signals --seen <scratch>/signals/seen.txt --dropped-log <scratch>/signals/dropped-log.jsonl`
- **Result:** `would append 13 records across 1 file(s); 0 dropped by materiality; 0 incomplete; 0 refused by AC-GDPR1`.
  - Identity-key dedup skipped 0.
  - The allowlist dropped only `_needs` and `evidence_type` (26 fields across 13 records), as designed.
- **Non-dry check:** a non-dry `--complete` into the same scratch copy wrote 13 lines, all 13 carrying `cz_check`.
- **Clean afterwards:** `git status --porcelain data/signals` was empty, and `data/raw/2026-10-05/funded/` still held only `pages/` and `staged.jsonl`.
- **What the coordinator owes:** one `--complete` over `data/raw/2026-10-05/funded`, then `db.py upsert data/signals/funded/2026-10-05.jsonl`.

### Which existing problem each record could be a comparable for

| record | existing problem in `data/problems/cz/` |
|---|---|
| `de-kuro` | **p-0007** (construction subcontractor management). Kuro is the bid-evaluation half of the general contractor's subcontractor workflow. The Czech incumbents (ÚRS KROS OFERTA, Callida) belong in its `locals[]` if not already there. |
| `gb-xylo` | **p-0003** (building-permit navigation). Xylo is the authority-side twin. The MMR "AI pro stavební úřady" call is a buyer-side receipt that p-0003 does not yet carry: 18 applications, 7 funded with 3,081,787 CZK on 2026-01-06 (`cz-mmr-ai-su-seznam.pdf`). |
| `fr-marble` | **p-0006** (investment-intermediary AML) and **p-0013** (instant-payments readiness: real-time fraud screening). |
| `de-ark-climate` | **p-0024** (EPBD retrofit analytics for towns) and **p-0031** (municipal PV procurement). The buyer is the same; the plan schedules those measures. |
| `fr-relaisante` | **p-0032** (residential care placement: the same hospital-discharge bottleneck) and **p-0011** (home-care agency ops: the supply side). |
| `it-gamindo` | **p-0008** (NIS2 implementation capacity): staff cyber-awareness training is one of its duties. |
| `it-nando` | none directly. The nearest is p-0037 (municipal environmental charging). |
| `fr-voltaback`, `dk-trypcom`, `dk-pandektes`, `dk-good-tape`, `pt-frank`, `es-reply-next` | none |

### New-problem candidates for the register

1. **Czech building offices (stavební úřady) drowning in permit paperwork, with the state paying for AI pilots.** Czech check: **contested**. AI Efektivia s.r.o. (IČO 19760680, since 2023-09-25) is early, and VITA software is adjacent agenda software.
   - **Demand receipts:**
     - The MMR NPO call 31_25_169 allocated 24.5M CZK.
     - 18 towns applied and 7 were funded on 2026-01-06 (3,081,787 CZK). Lovosice alone received 1,147,887 CZK.
     - The call targets "automatic document analysis, detecting incomplete or wrong documents, predicting case complexity" (ISVS.cz, 2026-02-18).
   - **Foreign proof:** `gb-xylo`, early, reporting 40% more applications per officer in trials.
   - **Positive control:** Wultra in ARES, plus VITA software surfaced by the agenda query. PASSED.
   - **Decision for MATCH:** a new record, or a widening of p-0003 to the authority side. It is the strongest candidate this pass, because it has a paying public buyer.
2. **Hospital discharge to home care: no Czech matching platform.** Czech check: **absent** across two query shapes (Medevio is adjacent). Control PASSED (Wultra, Medevio). Foreign proof: `fr-relaisante`, early but with 315 establishments in 9 months.
   - **Missing:** a sourced Czech pain receipt, such as discharge delays, bed-blocking or the time health-social workers spend phoning agencies. Without it this is a lead, not a candidate. It may also fold into p-0032.
3. **Running a town's climate-action plan (SECAP monitoring) as software.** Czech check: **absent** across three query shapes. Only consultancies and an assessment tool (ASITIS, CI2) were found. Control PASSED (Wultra, ASITIS).
   - **Missing:** a Czech cost or obligation receipt beyond the Covenant of Mayors' voluntary monitoring. The ledger's EPBD and municipal-energy regulation records should be checked first.
4. **Lead, not a candidate: home-charging reimbursement for company EVs.** The check came back **contested**, with ČEZ futurego early on test. fDrive reports that the reimbursement meter must be officially verified every 4 years from January 2026. This needs the ČEZ maturity limb (GAP 9) and a demand receipt.

### PASS SUMMARY

```
feed:               arb-scan (evidence_type funded), attended, 2026-10-05 (weekly delta)
checklist sources:  1 of 1 walked (THE CATEGORY-ROTATION DUTY); 12 of 12 categories named; 8 swept
                    (other, mobility, housing, environment, govtech, education, legal-compliance, retail-services);
                    listings visited and named: tech.eu RSS + 09-28 weekly recap (owed debt paid) + 10-02 round-up + 5 tag feeds,
                    EU-Startups RSS p1-4 (full text via content:encoded), Sifted RSS, Vestbee /insights x3, CzechCrunch (now cc.cz)
records staged:     13 - taken 7 (trypcom, kuro, nando, pandektes, marble, good-tape, gamindo), contested 4 (voltaback, xylo,
                    frank, reply-next), absent 2 (ark-climate, relaisante); controls passed 13/13; dry run +13, 0 dropped, 0 refused
coverage gaps:      11 named - tech.eu 10-05 recap not out; EU-Startups pages/round-up/tags 403 (RSS full text works); tech.eu
                    ?paged ignored; climate/govtech tags stale; CzechCrunch moved to cc.cz (10 items only); INISOFT IČO unresolved;
                    Bystřice page 404; 6 MMR pilot vendors unknown; 4 maturity limbs unreceipted; zod not run; 4 old leads still owed
rotation state:     other, mobility, housing, environment, govtech, education, legal-compliance, retail-services now 2026-10-05;
                    next: energy (19), fintech (24), health (32), b2b (66) at 2026-09-28
```

