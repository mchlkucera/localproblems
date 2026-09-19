# Front-page search mockups (parked 2026-09-18)

Three owner-reviewed options for searching and filtering the register, built on
the real rows and parked for later ("keep them as backup, don't install now").

- **A** — chips only: category links, opportunity band, "deadline within a year",
  "nobody sells it here yet"; a count line.
- **B** — A plus an instant text box over title, story, solution and category.
  Recommended when this is picked up, with C's `/` shortcut added.
- **C** — keyboard-first: `/` or a top-bar box opens a match overlay; Enter opens
  the first hit, Escape closes.

Each is a ~2 KB inline island with no dependency; with scripts off the full list
shows and the counts stay true (script-only controls hide via
`@media (scripting: enabled)`). To look at them again, restore the routes on a
dev server (below); the review screenshots were lost with a machine crash.

**To restore:** copy `routes/filter-*/` back under `web/app/(site)/`,
`filter-mock.tsx` to `web/lib/site/` and `filter-mock.css` to
`web/app/(site)/styles/`, then check `check-site pages` (the islands must be on
its client allow-list once the JS-islands rule lands in SKILL.md §9).

**2026-09-19: install of B plus `/` was built and then cancelled by the owner. Kept
parked; not installed.** The built version is better than the mockup and lives in
`install-b/`: `front-filter.tsx` (the server bar: box, chips, count line, facet
index), `filter-island.tsx` (the `"use client"` island: renders nothing, listens
after hydration, so no mismatch; also runs `/by-category`, opening matching folds and
restoring them on clear) and `front-filter.css` (the block that went before the
footer section of `front.css`, phone "Filter" toggle included). To install: copy the
two `.tsx` files to `web/lib/site/`, the CSS block into `front.css`, render
`<FilterBar items={items} categories={group !== "category"} />` after `<GroupBy>` and
`<FilterIsland />` at the end of `FrontPage`, and add the island with its job to
`ISLANDS` in `web/scripts/check-site.mjs`.
