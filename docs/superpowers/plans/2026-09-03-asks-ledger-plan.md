# Plan — land the `asks` ledger (design: ../specs/2026-09-03-asks-ledger-design.md)

Executed 2026-09-03 with three parallel builders and one orchestrator session.

## Tasks

| # | task | owner | verifies |
|---|------|-------|----------|
| A | Registration, zero records: `EVIDENCE_TYPES` + source enum, ledger copy, about page, `TYPE_TO_DIM` ×2, feeds.json rows (`planned`), CONVENTIONS / SPEC / design skill / MATCH / template / sources-catalog wave 4, `db.py health` | builder 1 | `npm --prefix web run build`, `parity`, `check-records --strict` |
| B1 | `scripts/fetch_tacr.sh` + `scripts/tacr_extract.py` + `scripts/tacr_contract_selftest.py` | builder 2 | self-test exit 0; live run into `$TMPDIR` |
| B2 | `scripts/fetch_hackathons.sh` + `scripts/hack_extract.py` + `scripts/hack_contract_selftest.py` | builder 3 | self-test exit 0; live run into `$TMPDIR`; zero email/phone hits |
| B3 | Wire `normalize.py` (tokens `tacr`, `hack`; EXTRACTORS) and `fetch_all.sh` (argv cases) — after B1/B2 exist, so imports never break an interim tree | orchestrator | `normalize.py --mechanical-only` over a live run |
| B4 | Attended ingest: `fetch_all.sh data/raw/2026-09-03 tacr hackathon` → mechanical → pass A/B via session subagents (`model_pass.py plan` / `model_pass_agent.py worklist` / `collect` / `apply`) → `--complete` → `db.py upsert` → `db.py health`; flip both feeds to `active` | orchestrator + scoring subagents | `check-records --strict`, build, parity |
| B5 | Deploy: `cd web && vercel build --prod && vercel deploy --prebuilt --prod`; verify `/signals/asks` and `/sources` live | orchestrator | curl the production URLs |
| C | Attach: `type: ask` sources on existing problem records where the fit is direct (MATCH.md); DEMAND only | judgment subagent | `check-records --strict`, build |
| D | Critique: an owner-voice review of the diff and the live pages; fix what it finds | review subagent | re-run gates |

## Commit order (CONVENTIONS: widen the enum BEFORE the first record)

1. `feat(register): asks — a sixth evidence type, registered empty` (A)
2. `feat(register): tacr + hackathon fetchers; first asks records` (B)
3. `feat(register): asks cited on N records` (C), if any fit
