# run manifest — 2026-09-08

Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/2026-09-08`.
Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).
`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,
§7.2 step 0, never counts as a failure) · `error` (ok=0).

| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-08T1247 | ted | ok | 200 | 78185802 | 9408 | 48176 | 2026-09-08T12:47:39Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | hlidac | ok | 200 | 2087494 | 902 | 8158 | 2026-09-08T12:48:34Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | veklep | ok | 200 | 1630436 | 119 | 2035 | 2026-09-08T12:50:38Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | tacr | ok | 200 | 264232 | 14 | 860 | 2026-09-08T12:50:53Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | hackathon | ok | 200 | 5006497 | 23 | 19448 | 2026-09-08T12:50:54Z | data/raw/2026-09-08 | partial: upol:yield-zero |
| 2026-09-08T1247 | nen-ptk | ok | 200 | 46344743 | 133 | 187037 | 2026-09-08T12:51:14Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | edesky | skipped | 000 | 0 | 0 | 0 | 2026-09-08T13:41:17Z |  | registry status=planned |
| 2026-09-08T1247 | cc-cz | ok | 200 | 18489 |  | 353 | 2026-09-08T13:41:17Z | data/raw/2026-09-08/feed-czechcrunch.xml |  |
| 2026-09-08T1247 | yc-oss | ok | 200 | 10433207 |  | 8339 | 2026-09-08T13:41:17Z | data/raw/2026-09-08/yc-all.json |  |
| 2026-09-08T1247 | vestbee | ok | 200 | 1059048 | 52 | 1421 | 2026-09-08T13:41:26Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | suggest | ok | 200 | 11881 | 42 | 21948 | 2026-09-08T13:43:17Z | data/raw/2026-09-08/suggest-pain.jsonl |  |
| 2026-09-08T1247 | reddit-new | ok | 200 | 217717 | 100 | 1486 | 2026-09-08T13:47:23Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | reddit-search | ok | 200 | 331644 | 100 | 1648 | 2026-09-08T13:47:23Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | nku | ok | 200 | 76618 | 126 | 1095 | 2026-09-08T13:48:05Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | sukl | ok | 200 | 1620112 | 15 | 1200 | 2026-09-08T13:48:06Z | data/raw/2026-09-08 | validity=2026-09-08 rows_in_file=83096 aggregates=15 |
| 2026-09-08T1247 | ec-hys | ok | 200 | 176910 | 45 | 6124 | 2026-09-08T13:48:08Z | data/raw/2026-09-08 |  |
| 2026-09-08T1247 | nen | skipped | 000 | 0 | 0 | 0 | 2026-09-08T13:48:39Z |  | registry status=planned |
| 2026-09-08T1247 | mpsv | skipped | 000 | 0 | 0 | 0 | 2026-09-08T13:48:39Z | data/raw/2026-09-08 | month 2026-08 already present in seen.txt |
| 2026-09-08T1247 | coi | skipped | 304 | 0 | 0 | 220 | 2026-09-08T13:48:39Z | data/raw/2026-09-08 | both datasets 304 Not Modified — quarterly source, nothing new since the last run: sankce:304 kontroly:304 |
| 2026-09-08T1247 | smlouvy | skipped | 000 | 0 | 0 | 0 | 2026-09-08T13:48:39Z |  | registry status=planned |

---

# Ingest run 2026-09-08T1548
Run date: 2026-09-08  ·  mode: mechanical-only (no model, no secrets, no network)

## Feed contracts

| feed | http | bytes | fetched | kept | yield | parse | ok | error |
|---|---|---|---|---|---|---|---|---|
| `cc-cz` | 200 | 18489 | 10 | 10 | — | structured | yes |  |
| `coi` | 304 | 0 | 0 | 0 | — | none | yes | both datasets 304 Not Modified — quarterly source, nothing new since the last run: sankce:304 kontroly:304 |
| `ec-hys` | 200 | 176910 | 45 | 22 | — | structured | yes |  |
| `hackathon` | 200 | 5006497 | 23 | 14 | — | structured | yes | partial: upol:yield-zero |
| `hlidac` | 200 | 2087494 | 902 | 78 | — | structured | yes |  |
| `mpsv` | — | 0 | 0 | 0 | — | none | yes | month 2026-08 already present in seen.txt |
| `nen-ptk` | 200 | 46344743 | 133 | 72 | above-range | structured | yes |  |
| `nku` | 200 | 76618 | 126 | 123 | — | structured | yes |  |
| `reddit-new` | 200 | 217717 | 100 | 100 | — | structured | yes |  |
| `reddit-search` | 200 | 331644 | 100 | 78 | — | structured | yes |  |
| `suggest` | 200 | 11881 | 42 | 27 | — | structured | yes |  |
| `sukl` | 200 | 1620112 | 15 | 8 | — | structured | yes | validity=2026-09-08 rows_in_file=83096 aggregates=15 |
| `tacr` | 200 | 264232 | 14 | 9 | — | structured | yes |  |
| `ted` | 200 | 78185802 | 9408 | 3660 | — | structured | yes |  |
| `veklep` | 200 | 1630436 | 119 | 17 | — | structured | yes |  |
| `vestbee` | 200 | 1059048 | 52 | 16 | — | structured | yes |  |
| `yc-oss` | 200 | 10433207 | 6204 | 1152 | — | structured | yes |  |

## Staged records — PENDING, not appended

5331 records carry their mechanical fields and are waiting on a model. 11907 were dropped as already present in `seen.txt`.

| still owed by a model | records |
|---|---|
| `scores.scale` | 5331 |
| `scores.recurrence` | 5331 |
| `geo_origin` | 5331 |
| `sector` | 5323 |
| `title` | 4181 |
| `summary` | 4181 |
| `scores.urgency` | 355 |
| `pain` | 205 |
| `stated_need` | 94 |

**Transport status UNKNOWN for 1 feed(s):** `mpsv`. No fetch receipt was found in `.fetch/receipts.jsonl`, so no status is recorded. This is deliberately blank rather than inferred: bytes on disk are not evidence of a 200, and an invented status reads as proof.

## AC-GDPR1 — contact-field gate

No personal data detected. 5331 staged record(s) passed the field allowlist and the email/phone content scan.

## Republication candidates — same quote and value, new notice id

**199 staged tender record(s) repeat the verbatim quote and the value of a record already on file.** TED re-notifies the same procurement under a new number and neither dedup axis can see it. They are KEPT — a re-issued tender can be evidence (p-0031) — each carries the earlier id in `notes`, and MATCH decides dup or distinct.

| staged id | repeats | seen in |
|---|---|---|
| `ted-485076-2026` | `ted-484589-2026` | batch |
| `ted-487576-2026` | `ted-566505-2026` | ledger |
| `ted-489006-2026` | `ted-484821-2026` | batch |
| `ted-491128-2026` | `ted-525029-2026`, `ted-542754-2026` | ledger |
| `ted-493117-2026` | `ted-489002-2026` | batch |
| `ted-493408-2026` | `ted-484132-2026` | batch |
| `ted-498224-2026` | `ted-552301-2026` | ledger |
| `ted-500435-2026` | `ted-567618-2026`, `ted-594090-2026` | ledger |
| `ted-501122-2026` | `ted-499262-2026` | batch |
| `ted-504761-2026` | `ted-478672-2026` | batch |
| `ted-505034-2026` | `ted-567791-2026` | ledger |
| `ted-509261-2026` | `ted-585863-2026` | ledger |
| `ted-509825-2026` | `ted-479122-2026` | batch |
| `ted-512419-2026` | `ted-588567-2026` | ledger |
| `ted-512670-2026` | `ted-563450-2026` | ledger |
| `ted-514163-2026` | `ted-567618-2026`, `ted-594090-2026` | ledger |
| `ted-514916-2026` | `ted-514493-2026` | batch |
| `ted-515178-2026` | `ted-587084-2026` | ledger |
| `ted-515784-2026` | `ted-490506-2026` | batch |
| `ted-520051-2026` | `ted-478672-2026` | batch |
| `ted-520572-2026` | `ted-557909-2026` | ledger |
| `ted-520836-2026` | `ted-503369-2026` | batch |
| `ted-521185-2026` | `ted-564088-2026` | ledger |
| `ted-522170-2026` | `ted-503608-2026` | batch |
| `ted-522603-2026` | `ted-508734-2026` | batch |
| `ted-522931-2026` | `ted-485397-2026` | batch |
| `ted-524293-2026` | `ted-571033-2026`, `ted-578486-2026` | ledger |
| `ted-527994-2026` | `ted-490506-2026` | batch |
| `ted-529528-2026` | `ted-504717-2026` | batch |
| `ted-536806-2026` | `ted-499262-2026` | batch |
| `ted-536808-2026` | `ted-547009-2026` | ledger |
| `ted-536828-2026` | `ted-560207-2026` | ledger |
| `ted-541036-2026` | `ted-557909-2026` | ledger |
| `ted-543982-2026` | `ted-490506-2026` | batch |
| `ted-545152-2026` | `ted-521757-2026` | batch |
| `ted-545908-2026` | `ted-532795-2026` | batch |
| `ted-552739-2026` | `ted-528999-2026` | batch |
| `ted-555462-2026` | `ted-554061-2026` | batch |
| `ted-556897-2026` | `ted-521757-2026` | batch |
| `ted-556949-2026` | `ted-554061-2026` | batch |
| `ted-557720-2026` | `ted-599397-2026` | ledger |
| `ted-565027-2026` | `ted-553142-2026` | batch |
| `ted-565384-2026` | `ted-566023-2026` | ledger |
| `ted-566552-2026` | `ted-533014-2026` | batch |
| `ted-567143-2026` | `ted-559126-2026` | ledger |
| `ted-567470-2026` | `ted-483546-2026` | batch |
| `ted-567694-2026` | `ted-479365-2026` | batch |
| `ted-571334-2026` | `ted-570329-2026` | batch |
| `ted-573735-2026` | `ted-596228-2026` | ledger |
| `ted-579895-2026` | `ted-484112-2026` | batch |
| `ted-580531-2026` | `ted-585863-2026` | ledger |
| `ted-582057-2026` | `ted-482571-2026` | batch |
| `ted-582837-2026` | `ted-489002-2026` | batch |
| `ted-584625-2026` | `ted-553308-2026` | batch |
| `ted-595209-2026` | `ted-506720-2026` | batch |
| `ted-602172-2026` | `ted-600285-2026` | batch |
| `ted-602795-2026` | `ted-599397-2026` | ledger |
| `ted-603768-2026` | `ted-521757-2026` | batch |
| `ted-605581-2026` | `ted-596494-2026` | batch |
| `ted-606067-2026` | `ted-477579-2026`, `ted-507989-2026`, `ted-519602-2026`, `ted-538178-2026`, `ted-558024-2026`, `ted-581728-2026`, `ted-603543-2026` | ledger |
| `ted-606078-2026` | `ted-507960-2026`, `ted-511945-2026`, `ted-589580-2026` | ledger |
| `ted-606181-2026` | `ted-572276-2026` | ledger |
| `ted-606326-2026` | `ted-499571-2026`, `ted-545567-2026`, `ted-593972-2026` | ledger |
| `ted-606337-2026` | `ted-533174-2026` | batch |
| `ted-606366-2026` | `ted-555700-2026` | ledger |
| `ted-606455-2026` | `ted-602131-2026` | ledger |
| `ted-606524-2026` | `ted-513059-2026`, `ted-572059-2026` | ledger |
| `ted-606562-2026` | `ted-466905-2026`, `ted-548527-2026`, `ted-573412-2026` | ledger |
| `ted-606643-2026` | `ted-556658-2026` | ledger |
| `ted-606700-2026` | `ted-600306-2026` | ledger |
| `ted-607030-2026` | `ted-481507-2026`, `ted-567776-2026`, `ted-567994-2026` | ledger |
| `ted-607161-2026` | `ted-522335-2026` | batch |
| `ted-607320-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026` | ledger |
| `ted-607341-2026` | `ted-606027-2026` | ledger |
| `ted-607479-2026` | `ted-574123-2026` | ledger |
| `ted-608042-2026` | `ted-496004-2026`, `ted-523439-2026`, `ted-532372-2026`, `ted-581139-2026`, `ted-587853-2026` | ledger |
| `ted-608202-2026` | `ted-570749-2026`, `ted-581993-2026` | ledger |
| `ted-608251-2026` | `ted-543957-2026`, `ted-583079-2026`, `ted-590399-2026`, `ted-598886-2026`, `ted-605495-2026` | ledger |
| `ted-608757-2026` | `ted-471894-2026` | ledger |
| `ted-609008-2026` | `ted-588567-2026` | ledger |
| `ted-609023-2026` | `ted-589902-2026` | ledger |
| `ted-609049-2026` | `ted-488033-2026`, `ted-516010-2026`, `ted-547691-2026`, `ted-565387-2026`, `ted-576952-2026`, `ted-579054-2026`, `ted-583339-2026` | ledger |
| `ted-609059-2026` | `ted-593033-2026` | ledger |
| `ted-609196-2026` | `ted-567179-2026`, `ted-591507-2026` | ledger |
| `ted-609228-2026` | `ted-471894-2026` | ledger |
| `ted-609303-2026` | `ted-588762-2026` | ledger |
| `ted-609525-2026` | `ted-515497-2026` | ledger |
| `ted-609548-2026` | `ted-530977-2026`, `ted-599338-2026` | ledger |
| `ted-609578-2026` | `ted-489190-2026`, `ted-489765-2026`, `ted-548711-2026`, `ted-550090-2026` | ledger |
| `ted-609607-2026` | `ted-563748-2026` | ledger |
| `ted-609713-2026` | `ted-578250-2026` | ledger |
| `ted-609728-2026` | `ted-544953-2026`, `ted-554673-2026`, `ted-558343-2026` | ledger |
| `ted-609735-2026` | `ted-545018-2026`, `ted-545288-2026`, `ted-545893-2026`, `ted-546347-2026`, `ted-578596-2026` | ledger |
| `ted-609809-2026` | `ted-572611-2026` | ledger |
| `ted-609876-2026` | `ted-568576-2026` | ledger |
| `ted-609986-2026` | `ted-598664-2026` | ledger |
| `ted-610001-2026` | `ted-564208-2026`, `ted-575552-2026`, `ted-579550-2026`, `ted-604354-2026` | ledger |
| `ted-610006-2026` | `ted-589830-2026` | ledger |
| `ted-610027-2026` | `ted-514493-2026` | batch |
| `ted-610050-2026` | `ted-507116-2026` | ledger |
| `ted-610054-2026` | `ted-516082-2026` | ledger |
| `ted-610297-2026` | `ted-549328-2026` | ledger |
| `ted-610356-2026` | `ted-568887-2026`, `ted-570191-2026` | ledger |
| `ted-610363-2026` | `ted-464900-2026`, `ted-483913-2026`, `ted-517576-2026`, `ted-530720-2026`, `ted-548419-2026`, `ted-564300-2026`, `ted-566663-2026`, `ted-584437-2026`, `ted-598659-2026` | ledger |
| `ted-610420-2026` | `ted-587111-2026` | ledger |
| `ted-610436-2026` | `ted-595961-2026` | ledger |
| `ted-610466-2026` | `ted-538523-2026` | ledger |
| `ted-610739-2026` | `ted-569202-2026`, `ted-599255-2026` | ledger |
| `ted-610802-2026` | `ted-482102-2026`, `ted-482381-2026`, `ted-483079-2026`, `ted-483582-2026`, `ted-483771-2026`, `ted-514443-2026` | ledger |
| `ted-610957-2026` | `ted-583167-2026` | ledger |
| `ted-611044-2026` | `ted-470646-2026`, `ted-552097-2026`, `ted-577271-2026`, `ted-595383-2026` | ledger |
| `ted-611059-2026` | `ted-471761-2026`, `ted-479736-2026`, `ted-490749-2026`, `ted-505800-2026`, `ted-532517-2026`, `ted-555812-2026`, `ted-565673-2026`, `ted-576774-2026`, `ted-585277-2026`, `ted-596315-2026` | ledger |
| `ted-611280-2026` | `ted-502625-2026`, `ted-524816-2026`, `ted-541734-2026`, `ted-566497-2026`, `ted-589042-2026` | ledger |
| `ted-611301-2026` | `ted-514493-2026` | batch |
| `ted-611310-2026` | `ted-480379-2026` | batch |
| `ted-611559-2026` | `ted-545018-2026`, `ted-545288-2026`, `ted-545893-2026`, `ted-546347-2026`, `ted-578596-2026` | ledger |
| `ted-611674-2026` | `ted-560691-2026` | ledger |
| `ted-611704-2026` | `ted-595034-2026` | ledger |
| `ted-611791-2026` | `ted-471894-2026` | ledger |
| `ted-611847-2026` | `ted-608668-2026` | batch |
| `ted-611853-2026` | `ted-476510-2026`, `ted-523188-2026` | ledger |
| `ted-612005-2026` | `ted-468892-2026`, `ted-553646-2026`, `ted-578104-2026`, `ted-594889-2026` | ledger |
| `ted-612085-2026` | `ted-489190-2026`, `ted-489765-2026`, `ted-548711-2026`, `ted-550090-2026` | ledger |
| `ted-612086-2026` | `ted-610856-2026` | batch |
| `ted-612124-2026` | `ted-477968-2026`, `ted-481331-2026` | ledger |
| `ted-612317-2026` | `ted-502655-2026`, `ted-569629-2026` | ledger |
| `ted-612328-2026` | `ted-607044-2026` | batch |
| `ted-612438-2026` | `ted-540209-2026` | ledger |
| `ted-612495-2026` | `ted-545018-2026`, `ted-545288-2026`, `ted-545893-2026`, `ted-546347-2026`, `ted-578596-2026` | ledger |
| `ted-612734-2026` | `ted-542879-2026` | ledger |
| `ted-613065-2026` | `ted-498370-2026`, `ted-551264-2026`, `ted-578691-2026`, `ted-584275-2026` | ledger |
| `ted-613122-2026` | `ted-565159-2026`, `ted-590749-2026` | ledger |
| `ted-613142-2026` | `ted-517764-2026`, `ted-589490-2026`, `ted-600172-2026` | ledger |
| `ted-613252-2026` | `ted-546770-2026` | ledger |
| `ted-613260-2026` | `ted-604003-2026` | ledger |
| `ted-613288-2026` | `ted-515602-2026` | ledger |
| `ted-613474-2026` | `ted-605672-2026` | ledger |
| `ted-613727-2026` | `ted-583857-2026` | ledger |
| `ted-614067-2026` | `ted-496004-2026`, `ted-523439-2026`, `ted-532372-2026`, `ted-581139-2026`, `ted-587853-2026` | ledger |
| `ted-614156-2026` | `ted-602026-2026` | ledger |
| `ted-614250-2026` | `ted-510714-2026` | ledger |
| `ted-614263-2026` | `ted-555141-2026` | ledger |
| `ted-614413-2026` | `ted-539598-2026`, `ted-563658-2026`, `ted-586240-2026`, `ted-601708-2026` | ledger |
| `ted-614432-2026` | `ted-511992-2026`, `ted-583594-2026`, `ted-600702-2026` | ledger |
| `ted-614675-2026` | `ted-580642-2026` | ledger |
| `ted-614696-2026` | `ted-535070-2026` | ledger |
| `ted-614775-2026` | `ted-543957-2026`, `ted-583079-2026`, `ted-590399-2026`, `ted-598886-2026`, `ted-605495-2026` | ledger |
| `ted-614849-2026` | `ted-492201-2026` | ledger |
| `ted-614985-2026` | `ted-521757-2026` | batch |
| `ted-615022-2026` | `ted-463127-2026`, `ted-513722-2026`, `ted-527939-2026`, `ted-543194-2026`, `ted-554363-2026`, `ted-569190-2026`, `ted-575385-2026`, `ted-583108-2026`, `ted-588764-2026`, `ted-591811-2026`, `ted-603646-2026` | ledger |
| `ted-615079-2026` | `ted-612286-2026` | batch |
| `ted-615115-2026` | `ted-548448-2026` | ledger |
| `ted-615294-2026` | `ted-615049-2026` | batch |
| `ted-615390-2026` | `ted-580235-2026` | ledger |
| `ted-615443-2026` | `ted-471282-2026` | ledger |
| `ted-615474-2026` | `ted-577618-2026` | ledger |
| `ted-615525-2026` | `ted-560691-2026` | ledger |
| `ted-615564-2026` | `ted-587413-2026` | ledger |
| `ted-615618-2026` | `ted-544133-2026` | ledger |
| `ted-615619-2026` | `ted-613840-2026` | batch |
| `ted-615744-2026` | `ted-612639-2026` | batch |
| `ted-615753-2026` | `ted-588738-2026` | ledger |
| `ted-615757-2026` | `ted-597763-2026` | ledger |
| `ted-615794-2026` | `ted-613840-2026` | batch |
| `ted-615838-2026` | `ted-605299-2026` | ledger |
| `ted-615878-2026` | `ted-576968-2026` | ledger |
| `ted-615993-2026` | `ted-536671-2026`, `ted-546008-2026`, `ted-579206-2026` | ledger |
| `ted-616234-2026` | `ted-594219-2026` | ledger |
| `ted-616255-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026` | ledger |
| `ted-616414-2026` | `ted-491226-2026` | ledger |
| `ted-616438-2026` | `ted-534679-2026` | ledger |
| `ted-616629-2026` | `ted-597461-2026` | ledger |
| `ted-616997-2026` | `ted-563450-2026` | ledger |
| `ted-617002-2026` | `ted-599424-2026` | ledger |
| `ted-617088-2026` | `ted-471894-2026` | ledger |
| `ted-617149-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026` | ledger |
| `ted-617274-2026` | `ted-461180-2026`, `ted-477824-2026`, `ted-522836-2026`, `ted-560780-2026`, `ted-568558-2026` | ledger |
| `ted-617323-2026` | `ted-575145-2026` | ledger |
| `ted-617356-2026` | `ted-507960-2026`, `ted-511945-2026`, `ted-589580-2026` | ledger |
| `ted-617545-2026` | `ted-537814-2026`, `ted-571956-2026`, `ted-578420-2026` | ledger |
| `ted-617589-2026` | `ted-525777-2026`, `ted-581836-2026` | ledger |
| `ted-617683-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026` | ledger |
| `ted-617935-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026` | ledger |
| `ted-617953-2026` | `ted-514573-2026`, `ted-588520-2026` | ledger |
| `ted-618054-2026` | `ted-616283-2026` | batch |
| `ted-618197-2026` | `ted-487236-2026`, `ted-515186-2026` | ledger |
| `ted-618373-2026` | `ted-488911-2026`, `ted-533408-2026`, `ted-540928-2026`, `ted-550874-2026`, `ted-555408-2026`, `ted-568835-2026`, `ted-590021-2026`, `ted-593753-2026`, `ted-600559-2026` | ledger |
| `ted-618628-2026` | `ted-491226-2026` | ledger |
| `ted-618677-2026` | `ted-599764-2026` | ledger |
| `ted-618764-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026` | ledger |
| `ted-618771-2026` | `ted-567179-2026`, `ted-591507-2026` | ledger |
| `ted-618781-2026` | `ted-497451-2026` | batch |
| `ted-618801-2026` | `ted-589525-2026` | ledger |
| `ted-618853-2026` | `ted-574123-2026` | ledger |
| `ted-618884-2026` | `ted-563975-2026`, `ted-583122-2026`, `ted-595810-2026` | ledger |
| `ted-618916-2026` | `ted-491226-2026` | ledger |
| `ted-618982-2026` | `ted-537364-2026`, `ted-583837-2026` | ledger |
| `ted-619223-2026` | `ted-495169-2026`, `ted-496296-2026`, `ted-496698-2026`, `ted-496726-2026`, `ted-497073-2026`, `ted-497341-2026`, `ted-528791-2026` | ledger |
| `ted-619271-2026` | `ted-616283-2026` | batch |

## Dedup by identity key — same resource, different id

**55 staged record(s) name a resource the ledger already holds under a DIFFERENT id.** They were removed before staging, so no model was asked to complete them and nothing was appended. `seen.txt` is id-keyed and cannot see this case.

| staged id | already in the ledger as | key | feed | url |
|---|---|---|---|---|
| `echys-14628` | `consult-cloud-ai-act` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14628 |
| `echys-14638` | `consult-europol-mandate` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14638 |
| `echys-14842` | `consult-chips-act-2` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14842 |
| `echys-14858` | `consult-battery-recycled-content` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14858 |
| `echys-15252` | `consult-territorial-supply-constraints` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15252 |
| `echys-15352` | `consult-packaging-epr-register` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/15352 |
| `echys-16413` | `consult-horizon-partnerships` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16413 |
| `echys-16612` | `consult-learning-accounts-eval` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16612 |
| `echys-16795` | `consult-banking-competitiveness` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/16795 |
| `echys-17172` | `consult-dual-use-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17172 |
| `echys-17912` | `consult-mica-evaluation` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/17912 |
| `echys-18194` | `consult-victims-rights-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18194 |
| `echys-18575` | `consult-employer-sanctions-eval` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18575 |
| `echys-18592` | `consult-ai-cultural-strategy` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18592 |
| `echys-18658` | `consult-housing-simplification` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18658 |
| `echys-18804` | `consult-wrc27-spectrum` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18804 |
| `echys-18872` | `consult-teachers-agenda` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18872 |
| `echys-18874` | `consult-school-basic-skills` | `url` | `ec-hys` | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/18874 |
| `hack-ebca5de0` | `hack-c5c10e91` | `url` | `hackathon` | https://www.aimtechackathon.cz/hackathon/ |
| `hlidac-36459536` | `hlidac-38795752` | `url` | `hlidac` | https://smlouvy.gov.cz/smlouva/38795752 |
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
| `yc-d-model` | `yc-d_model` | `url` | `yc-oss` | https://www.ycombinator.com/companies/d_model |
| `yc-galactic-resource-utilization-space-inc-gru-spac` | `yc-galactic-resource-utilization-space-inc-gru-space` | `url` | `yc-oss` | https://www.ycombinator.com/companies/galactic-resource-utilization-space-inc-gru-space |

**4 key(s) were EXEMPTED from dedup**, because a key naming more than one record is a listing page, a dataset landing page or a roundup — not an identity. Merging on one would delete distinct records. Measured over the committed corpus: 67 urls are shared by 571 records (6.1%), one Vestbee roundup being the url of 32 funding rounds.

| key | why it was not used |
|---|---|
| `url:hackjakbrno.cz/` | carried by 8 ledger records — a listing or dataset page, not an identity |
| `url:rakathon.cz/` | carried by 2 ledger records — a listing or dataset page, not an identity |
| `url:idea13.cz/` | carried by 4 records in THIS batch — undecidable, so no merge |
| `url:nakopniprahu.cz/` | carried by 6 records in THIS batch — undecidable, so no merge |
