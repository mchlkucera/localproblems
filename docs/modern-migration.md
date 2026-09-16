# Modern design migration: checklist

*Written 2026-09-16. It follows the owner's decision to adopt the modern lab design as
the site's official design. Source: the 2026-09-16 audit "can `/lab/modern` replace the
live site?" (blockers B1–B14, decisions D1–D12, migration plan). This file is for the
agent that moves the routes and reworks the gates. Tick boxes as you go, and put the
commit hash beside each finished step.*

> **Status, 2026-09-16 (branch `modern-migration`):** steps 3–7 are done — route
> groups, the move to the public URLs (D3 = ported, D5 = 12 category pages, D7 = 404,
> D4 = redirect, D12 = `next/font`), `check-site` (source + HTML halves, each proven to
> fail), the reworked `check-css` (tokens locked; gazette clause kept for `/sources`),
> and parity green with the modern pages in the build. Step 8 (deleting the gazette
> stylesheet) waits on `/sources`. Print styles and the rest of step 1's blockers
> (B13 record contrast/keyboard, D9 content cuts) were not part of this pass.

Rules that still apply throughout:
- **Never** run `next build` alongside a running dev server.
- **Never** deploy any way other than CLAUDE.md's prebuilt `--archive=tgz` recipe.
- Other sessions edit `web/app/lab/` concurrently, so coordinate before moving files
  (ListAgents / SendMessage) and stage by patch.

---

## Decisions

**Decided by the owner, 2026-09-16**
- **D1:** the modern design is the binding design. The skill has been rewritten and the
  gazette skill archived at `skills/design-language-gazette-archive/`. Done in the docs
  change that added this file.
- **D2:** client JS is allowed for the named progressive enhancements: `PeekHover` and
  native popovers (SPEC §5 and §7). Pages must still read fully without JS and stay
  static.
- **D7:** **rejected records return 404.** SPEC §5 records this and its trade-off.
- **D4:** `/about` redirects permanently to `/how-it-works`.

**Implied by the adoption; confirm with the owner when convenient**
- **D6:** each grouping gets its own static path (`/by-category`), because
  `?group=` can't be SSG.
- **D8:** the rail tooltips restate the SCORING.md ladders, and the rows are sorted by
  fill. The new skill records both as rules.

**Still open. Ask before the step that needs the answer.**
- **D3** (before step 4): port signals, 404 and the rest before launch, or launch with a
  visible style jump for a stated period?
- **D5** (before step 4): 12 static modern category pages at `/category/[slug]`, or
  redirects into `/by-category#cat-{slug}`?
- **D9** (before step 1): are these record content cuts intentional? `entry.why`, the
  five-gates list, the comps `evidence →` links, the whenline, past urgency receipts,
  the record corrections link.
- **D10** (before step 1): does print ("photocopies beautifully") survive? If yes, B12
  blocks launch.
- **D11:** the front page drops `[Sn]` receipts, IDs and the Entry level. Accept?
- **D12:** self-host Inter through `next/font`, or keep the Google Fonts link? Is
  "(which is A LOT of money)" the launch tone for p-0008?
- **`/sources`** (before step 8): the private admin page is gazette. Port it to modern
  tokens, or keep a local, ungated copy of the gazette stylesheet for it alone?

---

## Order of operations

Each numbered step is **its own commit** and leaves `npm --prefix web run build`
green, so any one step can be reverted alone. Steps 1–3 change no public URL. Step 4 is
the swap. Step 8 happens only after a production deploy of step 4 has been live
without trouble.

### 0. Preconditions
- [ ] The modern tree is committed (`web/app/lab/modern/`, `web/app/lab/parts/`), with
      no untracked files left under `web/app/lab/` that the move depends on.
- [ ] The docs change is committed: this file, the new `skills/design-language/SKILL.md`,
      the archive, SPEC §5/§7/§10/§12 and CLAUDE.md.
- [ ] Tag the last gazette commit: `git tag gazette-final`. This is the rollback anchor.
- [ ] Record a baseline: `npm --prefix web run build` green, `npm --prefix web run
      parity` green, and the list of emitted routes. Save the list to the scratchpad; it
      is compared in step 9.

### 1. Close the blockers inside the lab (still LP_ADMIN-gated, no URL change)
Other sessions may already have closed some of these, so check the code first.
- [ ] **B1:** no `searchParams` in any page. Grouping is `/…/by-category` (a static
      path), and the tabs are plain links.
- [ ] **B3 / D7:** `generateStaticParams` and `find()` exclude `status: rejected`, so a
      rejected id gets no page and 404s. This is already the modern behaviour; keep it.
- [ ] **B4 / D5:** category pages or redirects, as decided.
- [ ] **B5 + B6:** add an inline sources ledger `<section id="sources">` with
      `id="sN"` rows and a `#how-big` alias on Who pays. Make the rail sticky only when
      it fits.
- [ ] **B7 / D9:** restore whatever the owner keeps.
- [ ] **B12 / D10:** add a `@media print` block if print survives.
- [ ] **B13:**
  - text grays ≥4.5:1 on the record page (scope `--l-text-3` as `front.css` does)
  - pills don't auto-open on Tab, or card links get `tabindex=-1` until pinned
  - the rail comes before `main` in DOM order, or add a skip link
  - Escape closes `.ls-tip`
- [ ] **B14:** no "lab" in titles; descriptions come from `brief`.
- [ ] Screenshots at 1440 and 375 after each item (headless `agent-browser`).

### 2. Delete dead lab code (git history is the archive)
- [ ] `web/app/lab/paper/` (it imports modern, so delete it before moving anything),
      `web/app/lab/deprecated-paper/`, `web/app/front/`
- [ ] the demo galleries `web/app/lab/parts/art/page.tsx` and
      `web/app/lab/parts/figures/page.tsx`, plus the kit-unused `fig-*.tsx`, `hand.ts`,
      `coverage.ts`, `figures.css`. Confirm nothing imports them first:
      `grep -rn "fig-\|hand\"\|coverage\"" web/app web/lib`.
- [ ] Build green.

### 3. Split the layouts into route groups (B9); still no URL change
Route groups (`(name)`) don't appear in URLs, so this step is invisible to readers. Do
it before the move, so a problem with the move can't be confused with a problem with
the CSS.
- [ ] `web/app/layout.tsx` keeps only `<html>`, `<body>` and `assertScoringVocabulary()`.
      No stylesheet import and no font link.
- [ ] `web/app/(gazette)/layout.tsx` imports `../../shared.css` and the Source Serif +
      Plex Mono font link. `git mv` every live gazette route into it: `page.tsx`,
      `problem/`, `category/`, `signals/`, `about/`, `sources/`.
- [ ] **`not-found.tsx`:** the global 404 renders under the root layout, which no
      longer loads `shared.css`. Either give it a modern design now (D3), or import the
      stylesheet it needs in the file itself. Check `/nonexistent` renders styled.
- [ ] `web/app/(site)/layout.tsx` imports the modern tokens and Inter (D12 decides
      between `next/font` and the link). Nothing lives in it yet.
- [ ] Build green, **parity green**, and the emitted route list identical to the step 0
      baseline. Screenshots of a gazette record and a lab record at 1440: neither
      changed visually. Modern CSS was written assuming `shared.css` was present, so
      look hard at the lab pages.

### 4. Move the modern routes to the root (B2): the swap
Use `git mv` and fix relative imports. Map the tree **as it is at that moment**; other
sessions have been adding `by-category/`, `category/` and `signals/` under
`lab/modern/`.

| From | To |
|---|---|
| `web/app/lab/modern/page.tsx` (+ `front.tsx`) | `web/app/(site)/page.tsx` |
| `web/app/lab/modern/by-category/` | `web/app/(site)/by-category/` |
| `web/app/lab/modern/category/` (if D5 = pages) | `web/app/(site)/category/` (delete `(gazette)/category/`) |
| `web/app/lab/modern/[region]/[id]/` | `web/app/(site)/problem/[region]/[id]/` (delete `(gazette)/problem/`) |
| `web/app/lab/modern/how-it-works/` | `web/app/(site)/how-it-works/` (delete `(gazette)/about/`) |
| `web/app/lab/modern/signals/` (if D3 = port) | `web/app/(site)/signals/` (delete `(gazette)/signals/`) |
| `lab/modern/{bar,country,cite,prose,sources,peek-hover}.tsx/ts` | `web/lib/site/` |
| `lab/modern/*.css`, `lab/tokens.css` | `web/app/(site)/styles/` |
| `lab/parts/art/{category-art.tsx,art.css,_gen/}` | `web/lib/art/` |
| `lab/parts/figures/kit/*` | `web/lib/figures/` |
| `web/app/(gazette)/page.tsx` | deleted, replaced by `(site)/page.tsx` |

- [ ] **Remove every LP_ADMIN gate on the moved pages.** Find them with
      `grep -rn LP_ADMIN web/app`. These are the `enabled()` helpers, the
      `generateStaticParams → []` branches and the page-level `notFound()`. Delete
      `web/app/lab/layout.tsx` and then `web/app/lab/` entirely.
- [ ] **Keep LP_ADMIN on `/sources` only.** It stays private: `app/sources/page.tsx`
      keeps its own check, and `npm run dev` keeps setting `LP_ADMIN=1`.
- [ ] **Replace every `/lab/…` href** with `/`, `/by-category`, `/problem/…` or
      `/how-it-works`. `grep -rn '/lab/' web/app web/lib` must return nothing.
- [ ] `tokens.css` neutralises the gazette body with `body:has(.lab)`. Remove that
      override now that `shared.css` doesn't load on `(site)` pages, and re-verify.
- [ ] **Redirects** in `web/next.config.ts`, all `permanent: true`:
  - [ ] `/about` → `/how-it-works` (D4)
  - [ ] keep `/sources/:type` → `/signals/:type` exactly as it is (one segment, no
        fragment)
  - [ ] if D5 = redirects: `/category/:slug` → `/by-category`. Verify whether a
        fragment destination survives, and note that it overrides any incoming
        fragment.
  - [ ] **No redirect for rejected records.** They 404 by decision (D7).

### 5. Fail-the-build checks (CLAUDE.md rule 2: add them in the same change as step 4)
Add `web/scripts/check-site.mjs`. Run its source half in `prebuild`, and add a
`postbuild` script for the HTML half, so a violation fails `npm run build`. Prove each
check can fail before trusting it: plant a violation, see red, remove it.
- [ ] **Source:** no `searchParams`, `cookies(` or `headers(` under `web/app`.
- [ ] **Source:** `"use client"` appears only in the sanctioned files (today only
      `peek-hover.tsx`). A new client component then needs an explicit edit to the
      allow-list, which is SPEC §10's sign-off.
- [ ] **HTML:** no `href="/lab/` in any `.next/server/**/*.html`.
- [ ] **HTML:** every non-rejected record has a page, and **no rejected record does**
      (read statuses from the data, not a hard-coded list).
- [ ] **HTML:** if B5 is kept, every record page carries `id="s1"…id="sN"` for its
      source count, plus `id="sources"`.
- [ ] **Output:** after `vercel build --prod`, `.vercel/output/functions` has no
      function other than Next's built-ins, so every public route is static.
- [ ] **Optional:** export `ENTRY_WEIGHTS` from `lib/format.ts` instead of restating it,
      and assert the `DIM_INFO` / `BANDS` ladder wording against SCORING.md, next to
      `assertScoringVocabulary()`.

### 6. Rework `check-css`
While any gazette route still exists (`/sources`, and signals or 404 if D3 = later):
- [ ] Keep the gazette clause. `web/shared.css` must equal
      `skills/design-language/assets/style.css`. **Don't point it at the archive copy**,
      because the archive is history, not a live source.
- [ ] Add the modern clause: sha(`web/app/(site)/styles/tokens.css`) must equal
      sha(`skills/design-language/assets/tokens.css`). Copy `tokens.css` into the skill
      as a new asset in the same commit, and update SKILL.md §12 to name it.
- [ ] Decide whether the component CSS (`front.css`, `problem.css`, `kit.css`) is
      locked too. The lighter option: lock only the tokens, and lint for raw hex
      literals outside the token blocks the skill names. Write whichever you choose into
      SKILL.md §12 and SPEC §5.
- [ ] `db-gate`, `lint-citations` and `check-records --strict` read data only and stay
      unchanged.

### 7. Parity
- [ ] `npm --prefix web run parity` must be green **with the modern pages in the
      build**. It has never covered them, because every earlier build ran without
      LP_ADMIN. The `PeekHover` client chunk and every popover must come out
      byte-identical across the two loaders. The pinned `generateBuildId` in
      `next.config.ts` is what makes this possible; don't unpin it.

### 8. Delete the gazette stylesheet and its gate: a LATER commit and deploy
Do this only when step 4 has been live in production without a rollback **and** no
route under `(gazette)` remains, `/sources` included (decide its styling first).
- [ ] Delete `web/app/(gazette)/` and its layout.
- [ ] Delete `web/shared.css` and `skills/design-language/assets/style.css`. The byte
      copy at `skills/design-language-gazette-archive/assets/style.css` remains as
      history.
- [ ] Remove the gazette clause from `check-css.mjs`. If only the tokens clause is left,
      rename the script to say so.
- [ ] Remove the gazette font link, and the gazette-only helpers in `web/lib/chrome.tsx`
      (`RelDatesScript`, `SortScript`, masthead and nav) if nothing imports them. Check
      with grep, not by assuming.
- [ ] Docs, in the same commit:
  - SKILL.md: drop the "migration in progress" block and the "keep `assets/style.css`"
    sentences; move settled §11 items into the rules
  - SPEC §5: rewrite the route table for the modern routes; delete the "during the
    migration" paragraphs and the "table describes the live gazette routes" note; drop
    the gazette-snippet line from the sanctioned JS list
  - SPEC §7 and §12, the CLAUDE.md "change the site" row and gates paragraph
  - `README.md` line ~21 ("content runs never edit CSS")
  - mark this file done

### 9. Verify locally (owner-run, never alongside a dev server)
- [ ] `npm --prefix web run build`: every gate green, including `check-site`.
- [ ] `npm --prefix web run parity`: green.
- [ ] Compare the emitted route list with the step 0 baseline. The only differences
      should be: rejected records gone, `/about` now a redirect, `/by-category` and
      `/how-it-works` added, and nothing under `/lab`.
- [ ] Screenshots at 1440 and 375:
  - `/`, `/by-category`, a category page
  - p-0008, p-0036, p-0001, one record with a title over 120 characters
  - a rejected id (expect the 404), `/signals/funded`, the 404 page, `/how-it-works`
- [ ] One record with every `<script>` stripped: full text renders, and pills open on
      click.
- [ ] A print PDF of one record, if D10 keeps print.
- [ ] `cd web && vercel build --prod`, then check that `.vercel/output/functions` holds
      only Next's built-ins.

### 10. Deploy (manual, prebuilt, one archive)
```
cd web
vercel build --prod
vercel deploy --prebuilt --prod --archive=tgz
```
Smoke-test production:
- [ ] `/problem/cz/p-0001` → 200 (newsletter links), modern page
- [ ] `/problem/cz/p-0012` → **404** (rejected, D7)
- [ ] `/about` → 308 to `/how-it-works` → 200
- [ ] `/sources/tenders` → 308 to `/signals/tenders`
- [ ] `/category/health` → 200, or its redirect (D5)
- [ ] `/by-category` → 200; `/?group=category` serves the same static `/` (the query is
      ignored)
- [ ] `/lab/modern` → 404
- [ ] `/sources` → 404 (private)

---

## Rollback

**Before deploying:** each step is one commit, so `git revert <step commit>` undoes that
step alone. To abandon the whole migration, revert back to `gazette-final`. Don't use
`git reset --hard` on a shared tree, because other sessions have uncommitted work in it.

**After deploying step 4:**
1. **Fastest:** promote the previous production deployment in Vercel (`vercel rollback`,
   or `vercel promote <previous-deployment-url>`). It needs no build and no upload, so it
   doesn't touch the free-tier upload quota. The gazette site comes back as it was,
   including the 8 rejected-record pages, `/about` and every old anchor.
2. **Then fix forward or revert in git:** `git revert` the step 4–7 commits and deploy
   with the prebuilt recipe. Until that happens, `main` and production disagree, so note
   it in the run summary.
3. Step 8 hasn't happened yet at this point, which is exactly why it is a separate,
   later deploy. The gazette stylesheet, its gate and the `(gazette)` routes still exist
   on `main`, so a revert restores a working gazette build with no file resurrection.

**After step 8:** rolling back means restoring deleted files:
`git revert <step 8 commit>` brings back `web/shared.css`,
`skills/design-language/assets/style.css` and the gate. The archive copy is **not** a
substitute: `check-css` compares against the original path.

**Search engines:** rejected-record 404s and the `/about` redirect are visible to
crawlers as soon as step 4 deploys. A rollback within days costs nothing lasting.
