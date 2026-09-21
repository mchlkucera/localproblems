# localproblems.org

A public register of Czech problems worth solving, distilled from public evidence.

## Before you touch anything

| You are about to… | Read first |
|---|---|
| author or edit a **problem record** | **`pipeline/MATCH.md`** — the judgment. Then `SCORING.md` and `data/RECORD-TEMPLATE.md` |
| rewrite a **record's body** | **`pipeline/REWRITE.md`** — the procedure and checklist. Then `data/RECORD-TEMPLATE.md` "Writing the body"; p-0008 is the reference |
| change a **score or a ladder** | `SCORING.md`, then `pipeline/MATCH.md` §0 and §1 |
| add a **source or ingest script** | `pipeline/INGEST.md`, `docs/sources-catalog.md` |
| change the **site** | `skills/design-language/SKILL.md` (the modern design, adopted 2026-09-16), `web/app/(site)/DESIGN.md`, and `web/AGENTS.md`. `web/app/(site)/styles/tokens.css` is checksum-gated to `skills/design-language/assets/tokens.css` |
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

`npm --prefix web run build` runs them all: before `next build`, `check-css` ·
`check-site pages` · `db-gate` · `lint-citations` · `check-records --strict`; after
it, `check-site html`. Then `npm --prefix web run parity` proves the SQLite and
JSONL loaders produce byte-identical HTML.

`check-css` locks the modern tokens (`web/app/(site)/styles/tokens.css`) to the skill
asset. The gazette stylesheet and its lock are gone: every page, the private
`/sources` included, is in the modern design.
`check-site` fails the build on: `searchParams` / `cookies(` / `headers(` in any page,
`"use client"` outside its allow-list, any `href="/lab/`, a public page for a rejected
record (or a missing page for a live one), a record page without `id="s1…sN"`, and a
`/lab` page emitted without `LP_ADMIN`.

`data/signals/**` and `data/problems/**` are canonical and committed.
`data/register.db` is a gitignored projection, rebuilt by the build. Never edit it
by hand, never commit it.

## Deploys are manual

Production only changes when someone runs a Vercel CLI deploy, and it must be a
**prebuilt** one. **`--scope` is not optional**: the committed
`web/.vercel/project.json` carries `orgId: team_HTPoNl4AIqaUhP5C1qViXPRl`, which
does not resolve, and without the flag the deploy fails with a bare
`Not authorized` that names nothing (measured 2026-09-21).

```
cd web
vercel build --prod                            # runs the full prebuild gate locally
vercel deploy --prebuilt --prod --archive=tgz \
  --scope michal-kueras-projects-732d66fe      # uploads .vercel/output only, as ONE archive
```

**`git push` DOES trigger a Vercel build, and this file used to say it did not.**
Measured 2026-09-21: pushing `main` at 124b2e3 started a deployment that cloned
the repo from GitHub and failed in 9 s with *"No Next.js version detected …
check your Root Directory setting matches the directory of your package.json"* —
`package.json` is in `web/`, the project's Root Directory is not. Every push for
at least two days has produced one of these, on branches as well as `main`.

They are noisy, not dangerous: the build fails before anything is served, so
production keeps serving the last good deployment and a failed git build can
never publish a half-finished branch. But the claim "there is no git auto-deploy"
was false, and a wrong sentence here is worse than a missing one.

**This needs a decision nobody has made.** Either disconnect the Git integration,
which restores what this file claimed, or set the Root Directory to `web` and
accept that `git push` publishes — which would contradict "deploys are manual"
and lose the local-only `check-css` and `db-gate` coverage the prebuilt recipe
exists for. Until then, expect a failed deployment after every push and ignore it.

Build locally and ship the output — the gate runs `check-css` against `../skills`
and `db-gate` against `../data`, which only a local build can see. Deploying any
other way is costly, not merely wrong: a root deploy pushes ~650 MB across
thousands of files and burns the account's free-tier upload quota for 24 hours.
`.vercelignore` documents both failure modes. `--archive=tgz` is not optional
either: the free tier counts uploaded FILES (5,000 per 24 h, code
`api-upload-free`), and a prebuilt output of ~220 pages is thousands of files,
so a second deploy in one evening fails without it (measured 2026-09-03).
