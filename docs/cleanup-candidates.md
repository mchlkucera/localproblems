# Cleanup candidates (survey, 2026-09-17)

*A read-only survey. Nothing was deleted or edited, and this file is the only thing it
wrote. It was taken against `main` at `ab8040d`, with another session's work still
uncommitted: `skills/design-language/SKILL.md`, `web/app/(site)/DESIGN.md`,
`data/RECORD-TEMPLATE.md`, `scripts/check-records.py` and `web/app/(site)/styles/problem.css`.
Every grep below excludes `node_modules`, `.next` and `.claude/worktrees`.*

**Method.** The survey mapped every internal `import` under `web/app` and `web/lib` by
exact path, then grepped every exported symbol for importers. It also ran
`tsc --noEmit --incremental false`: the app sources and both untracked lab routes
type-check. The only errors come from the stale `web/.next/types` described in A7.
Branches, worktrees, tags and ignored files were read from git.

**One trap to know first.** The record page reads the figure kit through a namespace, by
string name: `kitCall("ProcessToday", …)` and `hasKit("MaturityDot")` in
`web/app/(site)/problem/[region]/[id]/page.tsx:174-187`. A plain grep for an importer
misses these calls. Every "unused" claim below was checked against those strings as well.

---

## Summary

| # | Path | Type | Rec. |
|---|---|---|---|
| A1 | `web/lib/figures/money.tsx` (MoneyScale, moneyDots) + its export in `index.ts:48` | dead code | DELETE |
| A2 | `FieldTimeline`, `FieldGrid`, `FieldStrip` in `web/lib/figures/field.tsx` + exports in `index.ts:45` | dead code | DELETE |
| A3 | Unused small exports: `criterion`, `bandWord` (scorecard.ts); `isoWeek`, `entryRank`, `localityLabel` (format.ts); `sourceExpired` (data.ts); `splitProse` (sections.ts) | dead code | DELETE |
| A4 | `web/app/lab/modern/` (empty apart from `.claude/.cc-writes/`) | stray artifact | DELETE |
| A5 | `modern-align-captop.png` (repo root, untracked) | stray artifact | DELETE |
| A6 | worktree `.claude/worktrees/agent-a7f8d63336dda9bc5` (740 MB) + branches `modern-migration`, `worktree-agent-a7f8d63336dda9bc5` | branch / worktree | DELETE |
| A7 | `web/.next/` (1.0 GB, built 2026-09-15, before the migration) and `web/.vercel/output/` (106 MB, same date) | stray build output | DELETE (regenerable) |
| B1 | `web/app/lab/paper/`, `web/app/lab/deprecated-paper/` (untracked) + the tracked shim `web/app/lab/parts/art/category-art.tsx` | dead code (lab) | ASK OWNER |
| B2 | `ProcessToday`, `ProcessAfter`, `reentryTally` in `process.tsx` + the `PROCESS_VIEW` "figures" branch in the record page | dead code (switched off) | ASK OWNER |
| B3 | Gazette `/sources`: `web/app/(gazette)/`, `web/shared.css`, `skills/design-language/assets/style.css`, the gazette clause in `check-css.mjs`, gazette helpers in `web/lib/chrome.tsx` | dead-ish code + gate | ASK OWNER |
| B4 | `record-redesign-pilot` branch | branch | ASK OWNER (lean DELETE) |
| B5 | `docs/modern-migration.md` | stale doc | ASK OWNER |
| B6 | `docs/record-page-redesign.md` | stale doc | ASK OWNER |
| B7 | root `.vercel/` project link | stray config | ASK OWNER |
| B8 | memory `localproblems-layout.md` (+ its MEMORY.md line), `design-taste-editorial-svg.md` | stale memory | ASK OWNER |
| C1 | `SPEC.md` lines 311-312, 331, 409, 563 | stale doc | UPDATE |
| C2 | `README.md` lines 24-47, 53 | stale doc | UPDATE |
| C3 | Page labels that point at retired section names: `web/lib/scorecard.ts:139,177,186` and `web/lib/site/sources.ts:103-110` | stale copy (live) | UPDATE |
| C4 | `SCORING.md:98,105`, `pipeline/MATCH.md:175`, `data/CONVENTIONS.md:337,493` | stale doc | UPDATE |
| C5 | `web/lib/figures/index.ts:1-43` header, `kit.css` header and its dead-figure CSS blocks | stale comments / CSS | UPDATE |
| C6 | Record page: `kitCall`/`hasKit` indirection and the local `Dot` fallback | code hygiene | UPDATE |
| C7 | `docs/scoring-presentation-options.md` status line ("Nothing here is built") | stale doc | UPDATE |
| C8 | `.gitignore`: add `.claude/worktrees/` | config | UPDATE |
| D1 | `docs/scoring-v2/*` | proposal pending decision | KEEP |
| D2 | `web/lib/site/score-proto.ts` (a PROTOTYPE, live in production) | live code | KEEP |
| D3 | `skills/design-language-gazette-archive/` | history | KEEP |
| D4 | tag `gazette-final` | tag | KEEP |
| D5 | `web/AGENTS.md`, `web/CLAUDE.md` | generated doc | KEEP |
| D6 | `pipeline/PROCESS.md:39-46`, `SPEC.md:195-205` ("Who pays:", "First moves" lead-ins) | data grammar, not page names | KEEP |
| D7 | `web/app/lab/layout.tsx`, `check-site` H1/H4, the `.lab` class in the live CSS | live gate / live class | KEEP |
| D8 | `docs/archive/`, `docs/superpowers/`, dated audits, `newsletter/`, `docs/TODO.md` | history / referenced | KEEP |

Counts: **A = 7, B = 8, C = 8, D = 8.**

---

## A. Safe to delete

### A1. `web/lib/figures/money.tsx`: MoneyScale, cut
- **Type:** dead code (tracked).
- **Evidence:** `grep -rlw MoneyScale app lib` finds only `money.tsx` and `figures/index.ts:48`.
  `moneyDots` has the same result. No `kitCall("MoneyScale")` exists (the record page
  calls only `MaturityDot`, `ProcessAfter`, `ProcessSteps` and `ProcessToday` by string).
  The file's other mentions are comments: `pay.tsx:39` ("money.tsx's rule") and
  `docs/record-page-redesign.md` D6, which removed it. Deleting it leaves `lib/figures/text.ts`
  in use: `czkShort` → pay.tsx, `packRows`/`textW` → field.tsx.
- **Risk:** none at runtime. `tsc` in `next build` fails only if an import is left behind,
  so delete the `index.ts:48` export in the same change. Its CSS is listed in C5.
- **Ownership:** tracked, last touched in the redesign commits. No session holds it open.
- **Rec.: DELETE.** Nothing calls it, and the owner cut the figure (redesign D6).

### A2. `FieldTimeline`, `FieldGrid`, `FieldStrip` in `web/lib/figures/field.tsx`
- **Type:** dead code (tracked; part of a live file).
- **Evidence:** `FieldTimeline` (lines 32-164), `FieldGrid` (165-217) and `FieldStrip` (243-318,
  plus its helpers `localRead`/`proofTail` at 226-242) have no importer and no string call
  (`grep -rlw` shows only field.tsx itself). The **live** parts of the file must stay:
  `MaturityDot` (called by string in the record page and imported by `matrix.tsx`), `DotPeek`
  and `firstLine` (both used by `comp-map.tsx` and `matrix.tsx`), and the `Maturity` type.
  Once the three are gone, `scoreRead`, `median`, `yearFrac`, `packRows` and `textW` may lose
  their last caller in this file. `scoreRead` is still used by `lib/site/front.tsx:340`.
- **Risk:** low. The build breaks only if `index.ts:45` still re-exports a deleted name.
- **Ownership:** tracked. `field.tsx` was modified in the working tree at session start;
  it is committed now.
- **Rec.: DELETE the three functions, keep the file.** The redesign split "Who already sells
  this" into Validated abroad and Competition (CompMap and LocalMatrix), and nothing draws
  a strip, timeline or grid.

### A3. Unused small exports
- **Type:** dead code (tracked).
- **Evidence:** each has zero references outside its definition line (`grep -rnw`):
  `criterion` (`lib/scorecard.ts:234`; deprecated-paper mentions the word only in comments),
  `bandWord` (`scorecard.ts:30`), `isoWeek` (`format.ts:22`), `entryRank` (`format.ts:160`),
  `localityLabel` (`format.ts:198`), `sourceExpired` (`data.ts:1119`), `splitProse`
  (`sections.ts:115`).
  Lab-only use: `gapSurface` (`format.ts`) → deprecated-paper only. `localityLong` → lab/paper
  only. `stats` (`data.ts`) → deprecated-paper only. These go with B1.
- **Risk:** none. Check `SCORING.md` with `assertScoringVocabulary` before touching
  `VERDICTS`/`BANDS`: they are used, so leave them.
- **Rec.: DELETE** the seven fully unused exports. A tidy-up, low value.

### A4. `web/app/lab/modern/`
- **Type:** stray artifact (untracked, and invisible to git because it holds no files).
- **Evidence:** `find web/app/lab/modern` shows only `.claude/.cc-writes/` (empty, 2026-09-16
  19:42). The route itself was deleted in `9053732` when it moved to the public URLs.
- **Risk:** none.
- **Rec.: DELETE.** It is a leftover of a session's write-tracking in a deleted route.

### A5. `modern-align-captop.png`
- **Type:** stray artifact (untracked, 136 KB, 2026-09-16 16:28).
- **Evidence:** `git status` shows `??`. Nothing references it. The `page2-p-0008-*.png`
  screenshots listed at session start are already gone. No PNG is tracked anywhere
  (`git ls-files | grep -i png` is empty).
- **Rec.: DELETE.** It is a one-off alignment screenshot.

### A6. Stale worktree and two merged branches
- **Type:** branch / worktree.
- **Evidence:** `git worktree list` shows `.claude/worktrees/agent-a7f8d63336dda9bc5` at
  `45aeedf [modern-migration]`, clean (`git status` is empty) and 740 MB.
  `git merge-base --is-ancestor modern-migration main` → merged (via `8016eec`).
  `worktree-agent-a7f8d63336dda9bc5` sits at `23e3757` (= tag `gazette-final`), also an
  ancestor of `main`. Neither branch exists on `origin` (only `main`).
- **Risk:** none. Everything is in `main`, and the tag keeps `23e3757` reachable.
  Use `git worktree remove` (not `rm`), then `git branch -d` (merged, so `-d` works).
- **Ownership:** the migration agent's worktree from 2026-09-16. Confirm no session is
  still running in it (ListAgents) before removing.
- **Rec.: DELETE.** Its work is merged, and the directory also shows as `??` in `git status`
  (see C8).

### A7. `web/.next/` and `web/.vercel/output/`
- **Type:** stray build output (gitignored).
- **Evidence:** both dated 2026-09-15 13:03, before the migration. `web/.next/types/validator.ts`
  still points at `app/about/page.js`, `app/front/page.js`, `app/lab/front/…` and
  `app/sources/page.js`. Those paths no longer exist, so `tsc --noEmit` reports 10
  TS2307 errors from this directory alone.
- **Risk:** `next dev` also writes `.next`, so don't delete it under a running dev server.
  The next `vercel build --prod` rewrites `.vercel/output`. The `web/.vercel/project.json`
  link must stay.
- **Rec.: DELETE `web/.next` and `web/.vercel/output` only.** They are regenerable and
  stale, and they cause false type errors.

---

## B. Needs an owner judgement

### B1. The paper-sheet lab prototypes
- **Paths:** `web/app/lab/paper/` (6 files + `[region]/[id]/page.tsx` + an empty
  `.claude/.cc-writes/`), `web/app/lab/deprecated-paper/` (10 files, including a 50 KB `sheet.css`),
  and the tracked shim `web/app/lab/parts/art/category-art.tsx`.
- **Type:** dead code, lab only.
- **Evidence:** both directories are **untracked and were never committed**
  (`git log --all -- 'web/app/lab/paper/*'` is empty); file mtimes are 2026-09-16 16:19. Both
  gate on `LP_ADMIN` and type-check against today's `lib`. No public route imports them.
  The shim's own header says *"delete this file together with the last /lab page that
  imports it"*, and only these two routes import it. `docs/modern-migration.md:99-100`
  (step 2) planned to delete both. They are the last users of `gapSurface`, `localityLong`
  and `stats` (A3). `lib/site/front.tsx:218-219` names `/lab/paper` in a comment as the
  source of the category-icon language.
- **Risk:** no gate depends on them. `check-site` H4 keeps passing. `web/app/lab/layout.tsx`
  would then guard nothing, so keep it anyway (D7).
- **Ownership:** another session's untracked work, per the brief. Ask before touching it.
- **Question:** *Are the /lab/paper and /lab/deprecated-paper prototypes finished with? If
  yes, delete both along with the category-art shim.*

### B2. The old process figures (`ProcessToday`, `ProcessAfter`)
- **Paths:** `web/lib/figures/process.tsx:67-239` (`ProcessToday`, `reentryTally`,
  `ProcessAfter`, `CHANGE_MARK`, `Q`, `Who`); `index.ts:44`; the record page's
  `PROCESS_VIEW` const (`page.tsx:42`), `processTodayFig` (608-609, 1169),
  `processAfterFig` (617, 1181) and `processAfterFull` (624, 629); the kit.css blocks at 271-371.
- **Type:** dead code behind a constant switch.
- **Evidence:** `const PROCESS_VIEW: "figures" | "steps" = "steps"`, and `ProcessSteps` exists,
  so `steps` is always true and every `kitCall("ProcessToday"|"ProcessAfter")` sits on the
  unreachable side of a ternary. The page comment at 34-40 still lists this switch as an
  "OPEN OWNER QUESTION". `reentryTally` has no caller at all. Keep `stateOf`, `colsFor`,
  `shortWho`, `bandLabel` and `ProcessSteps`: `ProcessSteps` uses them.
- **Risk:** none while `PROCESS_VIEW = "steps"`. After deletion, the switch goes.
- **Question:** *Is the two-lane ProcessSteps diagram final, so the "figures" fallback (the
  Today and After cards) can be deleted?*

### B3. The last gazette route, `/sources`
- **Paths:** `web/app/(gazette)/layout.tsx`, `(gazette)/sources/page.tsx`,
  `(gazette)/sources/registry.ts`; `web/shared.css`; `skills/design-language/assets/style.css`;
  clause 2 of `web/scripts/check-css.mjs` (lines 9-11 and 22); `web/lib/chrome.tsx` `Masthead`,
  `SIGNAL_NAV`, `SiteNav`, `FooterHouseLine`, `CorrectionsLink` (keep `CORRECTIONS_MAILTO`);
  `format.ts` `pad2`; `data.ts` `getSignals`.
- **Type:** private admin page in the retired design, plus the gate that locks it.
- **Evidence:** `/sources` is the only importer of `shared.css` and of the chrome helpers
  above (grep: each has `app/(gazette)/sources/page.tsx` as its sole user). All three
  stylesheet copies are byte-identical (sha `618df266…`): `web/shared.css`,
  `skills/design-language/assets/style.css` and `skills/design-language-gazette-archive/assets/style.css`.
  `check-css.mjs:9-11` says: "Delete this clause with the last gazette route."
  `docs/modern-migration.md` step 8 (205-226) is the full removal checklist, including the
  SPEC and SKILL.md edits. The `/sources/:type → /signals/:type` redirect in `next.config.ts:33`
  is **independent and must stay**.
- **Risk:** `check-css` fails the build if `shared.css` is deleted without its clause.
  `/sources` is `LP_ADMIN`-only, so production does not change either way.
- **Question:** *Should /sources move to the modern tokens, so the gazette stylesheet, its
  two extra copies and the check-css clause can be deleted? Or is the local gazette admin
  page kept as it is?*

### B4. Branch `record-redesign-pilot`
- **Type:** branch (local only).
- **Evidence:** one commit not in `main`: `f5b3761 wip(record): p-0008 record page redesign
  pilot (unapproved)`. It edits pre-migration paths (`web/app/lab/modern/…`,
  `web/app/lab/parts/figures/kit/…`, `web/lib/md.ts`), none of which exist on `main`. Its
  `docs/record-page-redesign.md` is **identical** to `main`'s (`git diff --stat` is empty). Its
  p-0008 rewrite was superseded by `b493e1e`, and its page work was ported in
  `5654447…ab8040d`.
- **Risk:** `git branch -d` refuses because the commit is unmerged, so deletion needs `-D`.
  After that the commit survives only in the reflog.
- **Question:** *Was the p-0008 pilot fully ported to main, so the record-redesign-pilot
  branch can be force-deleted?* (Lean yes.)

### B5. `docs/modern-migration.md`
- **Type:** stale doc (tracked, 286 lines).
- **Evidence:** every checkbox is still `[ ]` (e.g. lines 69-74, 80-96, 111-121, 145-162),
  though steps 0 and 3-7 landed and step 4's merge is `8016eec`. The status block at 9-15
  is dated before the merge. Step 2 (lines 98-105) is still undone (see B1). Step 8 (B3) is
  still open. The decisions at 25-58 list D3, D5, D9-D12 as "Still open", but the code
  settled them: 12 category pages, the 404 port and `next/font`. The file is still
  referenced by `SPEC.md:563` ("history once merged"), `web/app/layout.tsx:6`,
  `web/app/(gazette)/layout.tsx`, the lab shim and the gazette-archive SKILL.md.
- **Question:** *Keep modern-migration.md as the open checklist for step 8 (/sources)?* If yes,
  tick the finished steps and mark D3/D5/D9-D12 decided. If no, delete it and move step 8
  into docs/TODO.md. The code comments that cite it are history either way.

### B6. `docs/record-page-redesign.md`
- **Type:** stale doc (tracked, 519 lines, committed in `5654447`).
- **Evidence:** the implementation and the in-flight SKILL.md/RECORD-TEMPLATE.md contradict
  much of the spec:
  - **D1** (line 23) lists eight sections: The problem · Suggested solution · How it works ·
    Who already sells this · Who pays · Why now · Difficulty to enter · Suggested first moves.
    The page now has The opportunity · Suggested solution · Why now · Willing to pay ·
    Validated abroad · Competition · Execution difficulty · Suggested first moves
    (`page.tsx:961-968`).
  - **D4** (26), the merged "Who already sells this", was split again (`SKILL.md:291`).
  - **D5** (27) proposed an HTML step table. `ProcessSteps` is a two-lane diagram.
  - **D10** (32) removes the head drawing. The page keeps it (`SHOW_HEAD_ART = true`, "owner,
    2026-09-16: keep it, smaller").
  - §5.2 specifies `FieldStrip`, now unused (A2).
  - §9 (493-506) is the "codify after approval" list, being executed now by another session.
  - Still referenced by `figures/index.ts:16`, `kit.css:373`, p-0008's Revisions entry,
    `scoring-presentation-options.md` and `scoring-v2/builder-lens.md`.
- **Question:** *Once the SKILL.md/RECORD-TEMPLATE.md codification lands, should
  record-page-redesign.md be deleted?* The alternative is a "superseded, see SKILL.md §7"
  banner at the top, because p-0008's Revisions entry cites its §7.

### B7. Root `.vercel/` link
- **Type:** stray config (gitignored; `project.json` links the repo root to project
  `localproblems`).
- **Evidence:** `CLAUDE.md` says deploys must run from `web/`, and that a root deploy
  "pushes ~650 MB … and burns the account's free-tier upload quota". A root link makes
  that mistake one command away. `web/.vercel/project.json` is the link the recipe uses.
- **Risk:** some tool may rely on the root link (e.g. `vercel env` from the root).
- **Question:** *Is the root .vercel link intentional, or should it go so that
  `vercel deploy` only works from web/?*

### B8. Stale project memory (outside the repo, not writable from this sandbox)
- **Paths:** `~/.claude/projects/-Users-michalkucera-Documents-CODE-localproblems/memory/`
  `localproblems-layout.md` and the MEMORY.md line "design v2 landed";
  `design-taste-editorial-svg.md`; `localproblems-pipeline-ops.md:82-84`.
- **Evidence:** `localproblems-layout.md` (dated 2026-08-20) says:
  - `web/shared.css` "must stay a byte-copy", which is now true only for `/sources`
  - `TASK.md` is "the only entry point", but that file does not exist
  - routes are `/sources/[type]`
  - "zero client JS beyond the sanctioned relative-dates snippet"
  - deploy runs without `--archive=tgz`
  - the record-page order from 2026-08-19

  `pipeline-ops.md:82-84` repeats the shared.css lock as the general rule for site work.
  `design-taste-editorial-svg.md` describes "serif display + grotesk UI, ruled sheet", which
  is the paper-sheet language (B1), not the adopted modern design (Inter only).
- **Question:** *Should the layout memory be rewritten to today's layout (or deleted in
  favour of CLAUDE.md + SPEC.md)?* A second question: *is the editorial/serif taste memory
  still a preference, or only history now that the modern design is adopted?*

---

## C. Update, not delete

### C1. `SPEC.md`
- **311-312:** sanctioned JS item 3 ("The gazette relative-dates and table-sort snippets, only
  while their gazette routes exist"). No such snippet exists: `grep -rn "RelDatesScript\|SortScript"
  web/app web/lib` is empty, and `/sources` has no `<script>`. Remove item 3 now. The same
  applies to the **409** clause "and the gazette snippets while their routes last".
- **331:** the `/problem/[region]/[id]` route row lists "The problem · Suggested solution ·
  Proven abroad · Local competition · Who pays (`#how-big` alias) · Why now · Difficulty to
  enter · First moves; the Opportunity / Who is here / Evidence rail". Replace it with the
  shipped outline (`page.tsx:961-968`) and the TOC-with-scores rail. The in-flight SKILL.md
  §7 is the source to copy.
- **335, 338, 384-385, 562:** correct while `/sources` stays gazette. Revisit with B3.
- **563:** "`docs/modern-migration.md` … history once merged". It is merged, so align this
  line with B5.
- **Risk:** docs only. Rec.: **UPDATE.**

### C2. `README.md`
- **24-47:** "Status (2026-08-20)", "v2 is live", signal/record counts dated 2026-08-20.
- **53:** "optionally connect the repo in Vercel with root `web/` for push-to-deploy". This
  contradicts `CLAUDE.md` ("Deploys are manual … must be a prebuilt one"; a remote build
  cannot see `../skills` or `../data`, so `check-css` and `db-gate` would fail).
- Rec.: **UPDATE.** Drop the push-to-deploy suggestion, and re-date the status or reduce it
  to the re-derive commands.

### C3. Live page copy that names retired sections
- `web/lib/scorecard.ts:139` "— see Proven abroad", and `:177`, `:186` "— see Local competition".
  These are `scoreRead` lines rendered in the front page's opportunity tooltip
  (`lib/site/front.tsx:340`, via `OpportunityCard` at 384). The record page no longer has
  those sections: they are now **Validated abroad** and **Competition**.
- `web/lib/scorecard.ts:47,55` row labels "Demand signal", "Money nearby" (front-page card),
  against the record page's "The opportunity" and "Willing to pay".
- `web/lib/site/sources.ts:103-110` `typeNote` strings "It counts toward Money nearby / Demand
  signal", rendered in the record page's sources drawer (`page.tsx:1127`).
- **Risk:** `assertScoringVocabulary` (`scorecard.ts:~285`) checks only `VERDICTS` and `BANDS`
  words against SCORING.md, not these labels. Renaming is safe for the gate.
- Rec.: **UPDATE the two "see …" pointers now** (they send readers to sections that don't
  exist). Rename the row labels and type notes together with the scoring-v2 decision (D1),
  so the front page and the record page never disagree.

### C4. Rulebooks outside the two files being edited now
- `SCORING.md:98`: "the row reads 'Money nearby'". `:105`: the price receipt "renders under How
  big". The page section is **Willing to pay**, and `howbig` exists only as a body bucket in
  `sections.ts`.
- `pipeline/MATCH.md:175`: `solution:` is "always shown as 'Likely solution'". The page
  heading is **Suggested solution** (`page.tsx:962`), which `data.ts:584` also still calls
  "Likely solution".
- `data/CONVENTIONS.md:337`: the price receipt "renders under **How big**". `:493`: locals
  are "Rendered as a ledger under **Local competition**". Now → Willing to pay / Competition.
- `pipeline/MATCH.md:191` and `CONVENTIONS.md:442` "Difficulty to enter" are fine as the
  concept name for `entry`. The page says **Execution difficulty**, and
  `#difficulty-to-enter` is kept as an alias.
- Not stale: every `pipeline/*.md` mention of `Who pays:` / `## First moves` is **body grammar**
  that `sections.ts` still keys on (D6).
- **Ownership:** `data/RECORD-TEMPLATE.md` already carries the new names in the in-flight edit
  (lines 60, 80-81). Do C4 after that lands, to avoid a collision. Rec.: **UPDATE.**

### C5. Figure-kit comments and dead CSS
- `web/lib/figures/index.ts:1-43`: the usage example imports
  `ProcessToday, ProcessAfter, FieldTimeline, FieldGrid, CompMap, MoneyScale`. The "previous
  slots" table (36-43) lists removed sections (Local competition, Who pays, Opportunity card).
  Rewrite it after A1/A2/B2.
- `web/app/(site)/styles/kit.css:1-14`: "Renders inside the lab record page". The candidate
  dead blocks (verify with a class grep, since some names are built from templates,
  e.g. `lk-dot--${k}`, `lk-mark--${…}`):
  - 42-57 svg vocabulary (timeline, money)
  - 58-64 FieldTimeline marks
  - 65-76 MoneyScale marks
  - 77-93 FieldGrid
  - 271-371 ProcessToday / ProcessAfter / phone block
  - 384-399 FieldStrip

  About 160 of 545 lines. The live blocks are CompMap 94-191, LocalMatrix 192-230,
  DotPeek 231-262, LkPair 263-270, MaturityDot 378-383, ProcessSteps 400-466 and pay 467-545.
- **Risk:** `kit.css` is not checksum-locked. `check-css` locks only `tokens.css`.
- Rec.: **UPDATE** in the same change as A1/A2/B2.

### C6. Record page: indirection that outlived its reason
- `page.tsx:27-30, 174-187`: `import * as Kit` plus `kitCall`/`hasKit` ("a component that is
  not exported … draws nothing"). They existed so the page could build before the kit landed,
  and the kit has landed. The local `Dot` fallback (`182-187`, `.ls-mdot`) is unreachable
  because `MaturityDot` exists. The page's "OPEN OWNER QUESTIONS" comment (34-40) describes
  both switches as still open.
- Why it matters: string lookup hides usage from grep and from TypeScript, which is how
  dead figures went unnoticed here.
- Rec.: **UPDATE.** Import `ProcessSteps` and `MaturityDot` by name, drop `kitCall`/`hasKit`/`Dot`,
  and fold the answered switches into constants or remove them (after B2).

### C7. `docs/scoring-presentation-options.md`
- Lines 3-8 say "Nothing here is built". The TOC-with-scores rail and the section names it
  discusses shipped as a prototype in `5654447`/`ab8040d` (`lib/site/score-proto.ts`).
  The final rubric is still pending.
- Rec.: **UPDATE the status line** to say what is live as a prototype and what is still open.
  Keep the file.

### C8. `.gitignore`
- `.claude/worktrees/` shows as `??` in every `git status`. Worktrees are local by nature.
- Rec.: **UPDATE:** add `.claude/worktrees/`.

---

## D. Keep

- **D1. `docs/scoring-v2/` (builder-lens, evidence-feasibility, rubric-design).** These are
  2026-09-17 proposals, cited by the in-flight `SKILL.md` and `DESIGN.md`, and they await the
  owner's scoring decision. KEEP.
- **D2. `web/lib/site/score-proto.ts`.** Its header reads "PROTOTYPE … replace this module when they
  land", yet it drives the live record page's section scores (`page.tsx:20, 820`). It is
  not dead: replace it, don't delete it, when D1 is decided.
- **D3. `skills/design-language-gazette-archive/`.** Named read-only history in
  `SPEC.md:371,562` and `skills/design-language/SKILL.md:9`. It is not registered as a
  skill: `.claude/skills/` holds only the `design-language` symlink →
  `../../skills/design-language`, so it can't be loaded by mistake. Its `assets/style.css`
  becomes the only surviving gazette copy after B3. KEEP.
- **D4. Tag `gazette-final` (`23e3757`).** The rollback anchor named in
  `docs/modern-migration.md` §Rollback. Tags are free. KEEP.
- **D5. `web/AGENTS.md` / `web/CLAUDE.md`.** A block that `next dev` generates and re-adds
  (`@AGENTS.md`). It is not stale, and deleting it only re-creates it. KEEP.
- **D6. Body lead-ins in `pipeline/PROCESS.md:39-46`, `SPEC.md:195-205`,
  `data/CONVENTIONS.md:621-643`.** `Why now:`, `Who pays:`, `Existing non-solutions:`,
  `Solved elsewhere:` and `## First moves` are the record-body grammar that
  `web/lib/sections.ts:183` still parses (20 records carry `## First moves`). They are not
  page headings. KEEP.
- **D7. `web/app/lab/layout.tsx`, `check-site` H1/H4, and the `.lab` class.** The layout gate
  and H4 protect any future lab page. `.lab` is the live root class of every public page
  (`tokens.css:8-45`, `front.css:43`, `category/[slug]/page.tsx:64`, `page.tsx:973`): only
  the name is historical. KEEP.
- **D8. `docs/archive/`, `docs/superpowers/`** (cited from `scripts/*_extract.py` and
  `docs/sources-catalog.md`), **`docs/who-pays-audit-2026-09-03.md`** (cited by SCORING.md,
  data.ts, check-records.py), `docs/feeds-status.md` (SPEC), `docs/sources-catalog.md`,
  `docs/sources-unconventional-2026-09-04.md`, `docs/architecture-v3.md`, `docs/TODO.md`,
  `newsletter/`. KEEP. `architecture-v3.md:117,1382,1635,1808` describe the shared.css lock,
  so touch them only if B3 retires it.
- **Also checked, nothing to do:** no PNGs or images are tracked. `data/raw/**`,
  `data/register.db*`, `scripts/__pycache__/`, `.DS_Store`, `.envrc` and `web/node_modules` are
  all correctly gitignored. `web/lib/art/_gen/*.py` are the category-drawing generators (tracked
  and intended). `web/app/(site)/DESIGN.md` and `skills/design-language/SKILL.md` are being
  rewritten by another session. They were only grepped: SKILL.md 13, 478-479, 522 and 562
  describe the gazette lock, which is correct until B3.
