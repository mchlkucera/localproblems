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

## Status (2026-08-20)

**v2 is live and publicly deployed.** The evidence layer, the region layer and the
generated register (`web/`, Next.js pure SSG, zod-validated build) all landed per
SPEC.md §8. v3 splits the single weekly loop into the two entry points listed above.

Counts rot, so here is how to re-derive them rather than trust them:

```
cat data/signals/*/*.jsonl | wc -l      # 6,181 signals  (2026-08-20)
ls -1 data/problems/cz/*.md | wc -l     # 31 problems    (2026-08-20)
```

The numbers this file carried before today read 71 and 26 — off by 87× and by 5. That is
the failure this repo keeps re-learning: a hardcoded figure still reads as authoritative
long after it stops being true, so prefer the command that regenerates it.

## Do next

1. Register domains (verified free 2026-08-13): `localproblems.org`, defensive `problems.cz` / `problems.city`.
2. ~~GitHub remote + Vercel project~~ — done: [github.com/mchlkucera/localproblems](https://github.com/mchlkucera/localproblems) + [localproblems.vercel.app](https://localproblems.vercel.app) (deploy = local prebuilt, see SPEC §5; optionally connect the repo in Vercel with root `web/` for push-to-deploy).
3. Point the weekly scheduled Claude task at `pipeline/PROCESS.md` (Mon 06:00). The ingest
   loop (`pipeline/INGEST.md`) runs separately and more often; it is proven in an attended
   Claude session today, and its unattended runner ships wired but unproven.
4. Newsletter issue #0 by hand via Buttondown — go/no-go: ≥300 subs in 14 days from one LinkedIn post, or reposition.
