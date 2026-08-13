# Fetch manifest — 2026-08-13 (second run of the day; first local run)

| source | status | items | note |
|--------|--------|-------|------|
| TED API v3 | OK | 3,048 unique notices (5 CPV groups, since 2026-06-01) | First successful TED run — cloud-sandbox egress block does not apply locally. `ted-*.json` + ranked `ted-shortlist.md` (876 candidates, 266 domain-matched). |
| Hlídač státu | FAILED | 0 | HLIDAC_TOKEN not set. Get free key at hlidacstatu.cz/api (README checklist #3). Script ready: `scripts/fetch_hlidac.sh`. |
| CzechCrunch RSS | OK | 10 | `feed-czechcrunch.xml` — no problem-relevant items this window (consumer/AI news), 0 kept. |
| Vestbee RSS | FAILED | 0 | `/blog/rss.xml` → 404 (site moved to /insights, no feed found there either). Re-probe next run. |
| yc-oss | OK | 6,156 companies | `yc-all.json` re-fetched; 615 in 2026+ batches unseen, 273 keyword-relevant, ~5 kept after strictness. |
| Research scan: regulatory triggers | OK | 12 dated items | Agent-run WebSearch sweep (no script). 12 verified deadlines + 6 checked-and-excluded. Kept selectively as `reg-*` signals. |
| Research scan: arbitrage rounds | OK | 14 candidates | DACH/CEE/Nordics May–Aug 2026 funded verticals, all with source URLs; 7 kept as signals (de-conmeet, de-skalar, de-varm, de-fuchs-eule, de-jupus, dk-festina, pl-sunbay), 4 discarded (CZ player exists / weak transfer), 3 held in agent output only. |

Notes:
- TED fetch scripts created this run: `scripts/fetch_ted.sh` (paginated, CPV groups it/health/bizserv/energy/construction), `scripts/filter_ted.py` (keyword+value shortlist).
- macOS bash 3.2 gotchas fixed in scripts (no associative arrays; `GROUPS` is a reserved bash variable).
- No sources/ folders older than 28 days exist yet; nothing pruned.
