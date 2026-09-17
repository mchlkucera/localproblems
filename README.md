# localproblems.org

**A public register of local problems and opportunities. Every claim links to its source.**

Solvers are abundant; well-stated problems are scarce. This repo collects public
signals (tenders, regulation, foreign-market arbitrage, funding rounds, complaints),
normalizes them into an objective evidence layer, and runs a per-region Claude agent
that turns them into scored, source-backed problem records — published as a static
register and a weekly newsletter draft.

- **Why** → [docs/FOUNDER VISION.md](docs/FOUNDER%20VISION.md)
- **How (authoritative spec)** → [SPEC.md](SPEC.md)
- **Scoring rubric** → [SCORING.md](SCORING.md) · **Vocab & schemas** → [data/CONVENTIONS.md](data/CONVENTIONS.md)
- **The two agent entry points** → [pipeline/INGEST.md](pipeline/INGEST.md) (fetch → contract check →
  normalize; hourly-ish, region-blind, never commits) and [pipeline/PROCESS.md](pipeline/PROCESS.md)
  (match → score → build → newsletter → commit → deploy; on demand, Mon 06:00 by default).
  Each is launchable by Claude from that file alone; the handoff between them is the git
  working tree.
- **Ingest architecture** → [docs/architecture-v3.md](docs/architecture-v3.md) (the DB, the feeds
  registry, runners, receipts, feed health)
- **Design system** → [skills/design-language/](skills/design-language/) (binding; content runs never edit CSS)
- **History** → [docs/archive/](docs/archive/) (superseded research & drafts)

## Status

**Live and publicly deployed.** The evidence layer, the region layer and the generated
register (`web/`, Next.js pure SSG, zod-validated build) all landed per SPEC.md §8, and
the public site has run in the modern design since 2026-09-16. v3 splits the single
weekly loop into the two entry points listed above.

Counts rot, so this file carries none. Re-derive them:

```
cat data/signals/*/*.jsonl | wc -l      # signals
ls -1 data/problems/cz/*.md | wc -l     # problems
python3 scripts/db.py stats             # the store production actually reads
```

A hardcoded figure still reads as authoritative long after it stops being true (this file
once carried counts off by 87×), so prefer the command that regenerates it.

**Production reads `data/register.db`**, not the JSONL directly (`LP_SOURCE` defaults to
`db`). The store is gitignored and rebuilt from the committed journal by a prebuild gate
that verifies it against the tree and **fails rather than falling back**. The journal stays
the append-only audit trail. `npm --prefix web run parity` builds both ways and asserts
byte-identical HTML.

## Do next

1. ~~Register `localproblems.org`~~ — done: live at [www.localproblems.org](https://www.localproblems.org). Defensive `problems.cz` / `problems.city` still unregistered (verified free 2026-08-13).
2. ~~GitHub remote + Vercel project~~ — done: [github.com/mchlkucera/localproblems](https://github.com/mchlkucera/localproblems) + [localproblems.vercel.app](https://localproblems.vercel.app) (deploys are manual: a local `vercel build --prod` then `vercel deploy --prebuilt --prod --archive=tgz` from `web/`, see `CLAUDE.md`. Never connect the repo for push-to-deploy: a remote build cannot see `../skills` or `../data`, so the build gates would fail).
3. Point the weekly scheduled Claude task at `pipeline/PROCESS.md` (Mon 06:00). The ingest
   loop (`pipeline/INGEST.md`) runs separately and more often; it is proven in an attended
   Claude session today. **There is no unattended runner** — no launchd plist and no
   `.github/` directory exist (SPEC §9.5; `docs/architecture-v3.md` §5.4 carries the
   design). Scheduling is still an open decision, and `scripts/ingest.sh` is what a
   scheduler would call.
4. Newsletter issue #0 by hand via Buttondown — go/no-go: ≥300 subs in 14 days from one LinkedIn post, or reposition.
