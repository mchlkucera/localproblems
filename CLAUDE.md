# localproblems.org

A public register of Czech problems worth solving, distilled from public evidence.

## Before you touch anything

| You are about to… | Read first |
|---|---|
| author or edit a **problem record** | **`pipeline/MATCH.md`** — the judgment. Then `SCORING.md` and `data/RECORD-TEMPLATE.md` |
| change a **score or a ladder** | `SCORING.md`, then `pipeline/MATCH.md` §0 and §1 |
| add a **source or ingest script** | `pipeline/INGEST.md`, `docs/sources-catalog.md` |
| change the **site** | `web/AGENTS.md`, and note `web/shared.css` is checksum-gated to `skills/design-language/assets/style.css` |
| change **architecture** | `SPEC.md` |

## The two rules that matter most

**1. One field, one meaning.** Every public contradiction this register has shipped
came from a single field carrying two different questions — `gap: 0` meaning both
"unchecked" and "taken"; `proof: 2` meaning both "proven abroad" and "no local
player". If a field's value would be set for two different reasons, it is two
fields. See `pipeline/MATCH.md` §0.

**2. A rule enforced by prose is not enforced.** `SPEC.md` forbade the
proof-vs-comps contradiction from the start; nothing checked it, so 13 records
carried it for weeks. New rule ⇒ new invariant in `scripts/check-records.py`,
in the same change. It runs inside `prebuild`, so a contradiction fails the build.

## Gates

`npm --prefix web run build` runs all four: `check-css` · `db-gate` ·
`lint-citations` · `check-records --strict`. Then `npm --prefix web run parity`
proves the SQLite and JSONL loaders produce byte-identical HTML.

`data/signals/**` and `data/problems/**` are canonical and committed.
`data/register.db` is a gitignored projection, rebuilt by the build. Never edit it
by hand, never commit it.

## Deploys are manual

There is no git auto-deploy. `git push` does not publish; production only changes
when someone runs a Vercel CLI deploy.
