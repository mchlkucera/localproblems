# localproblems.org

**A public register of local problems and opportunities. Every claim links to its source.**

Solvers are abundant; well-stated problems are scarce. This repo collects public
signals (tenders, regulation, foreign-market arbitrage, funding rounds, complaints),
normalizes them into an objective evidence layer, and runs a per-region Claude agent
that turns them into scored, source-backed problem records — published as a static
register and a weekly newsletter draft.

- **Why** → [FOUNDER VISION.md](FOUNDER%20VISION.md)
- **How (authoritative spec)** → [SPEC.md](SPEC.md)
- **Scoring rubric** → [SCORING.md](SCORING.md) · **Vocab & schemas** → [data/CONVENTIONS.md](data/CONVENTIONS.md)
- **The weekly agent prompt** → [pipeline/PROCESS.md](pipeline/PROCESS.md) (scheduled Mon 06:00; the whole
  pipeline is launchable by Claude from this file alone)
- **Design system** → [skills/design-language/](skills/design-language/) (binding; content runs never edit CSS)
- **History** → [docs/archive/](docs/archive/) (superseded research & drafts)

## Status (2026-08-13)

**v2 is live locally.** The evidence layer (71 signals in `data/signals/`), the region
layer (26 scored problems in `data/problems/cz/`), and the generated register
(`web/`, Next.js pure SSG — 32 static pages, zod-validated build) all landed per
SPEC.md §8. `pipeline/PROCESS.md` is the pipeline's only entry point.

## Do next

1. Register domains (verified free 2026-08-13): `localproblems.org`, defensive `problems.cz` / `problems.city`.
2. ~~GitHub remote + Vercel project~~ — done: [github.com/mchlkucera/localproblems](https://github.com/mchlkucera/localproblems) + [localproblems.vercel.app](https://localproblems.vercel.app) (deploy = local prebuilt, see SPEC §5; optionally connect the repo in Vercel with root `web/` for push-to-deploy).
3. Point the weekly scheduled Claude task at `pipeline/PROCESS.md` (Mon 06:00).
4. Newsletter issue #0 by hand via Buttondown — go/no-go: ≥300 subs in 14 days from one LinkedIn post, or reposition.
