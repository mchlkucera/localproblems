// The front page's search and filter bar (owner, 2026-09-18: "B, plus C's `/`
// shortcut" — option B of the parked mockups in docs/mockups/front-search/).
// A SERVER component: everything here is HTML at build time. The one client
// island that makes it live is ./filter-island.tsx.
//
// THE RULES IT OBEYS (design-language SKILL §9, the islands rule)
//   · With scripts off the page is complete: every row renders, the count line
//     states the plain total ("29 problems", never "29 of 29"), the category
//     chips are real links to /category/<slug>, and every control a dead script
//     would leave inert is hidden BY CSS — `@media (scripting: enabled)`, never a
//     class the script adds. A control that cannot work is not shown.
//   · Every aria state is server-rendered; the island only flips a value that is
//     already in the HTML, after hydration, on a click or a keystroke. (The
//     mockup's first cut set `aria-pressed` on load and hit a hydration mismatch.)
//   · The rows carry no new attributes: `Entry` renders as it always has. The
//     island keys each row by its title link into the JSON index below.
//
// EVERY FACET IS DERIVED, never authored:
//   category = p.category                         (counts = categoryCounts())
//   band     = the SCORING.md thresholds (lib/scorecard BANDS), as numbers —
//              the same bands byOpportunity() groups the list by
//   deadline = a source dated after the extract date and within 12 months of
//              it: the register's own clock (extractDate()), never today's
//   open     = no local player recorded as `competes: direct` — the same fact
//              the meter card states as "No Czech seller on file"
import type { ReactNode } from "react";
import { CATEGORIES, categoryCounts, extractDate, type Problem } from "../data";
import { categoryLabel } from "../format";
import { BANDS } from "../scorecard";
import type { Item } from "./front";

const BAND_MINS = BANDS.map(([min]) => min); // [10, 8, 5, 0]

/** Which opportunity band a score falls in, named by its floor. */
const bandOf = (score: number) => String(BAND_MINS.find((min) => score >= min) ?? 0);

/** "10–12", "8–9", "5–7", "0–4": the thresholds as numbers, no rubric words. */
const BAND_RANGES = BAND_MINS.map((min, i) => ({ id: String(min), label: `${min}–${i === 0 ? 12 : BAND_MINS[i - 1] - 1}` }));

/** ISO string arithmetic, as the register does it: no clock, no time zone. */
const plusYear = (iso: string) => `${Number(iso.slice(0, 4)) + 1}${iso.slice(4)}`;

function deadlineWithinYear(p: Problem): boolean {
  const today = extractDate();
  const limit = plusYear(today);
  return p.sources.some((s) => s.date > today && s.date <= limit);
}

const openField = (p: Problem) => !(p.locals ?? []).some((l) => l.competes === "direct");

/** href → facets. `n` is the category's name, so typing "health" finds rows
    even where the rail, not the row, names the category. */
type Facet = { c: string; n: string; b: string; d: 0 | 1; l: 0 | 1 };
function facetIndex(items: Item[]): Record<string, Facet> {
  return Object.fromEntries(items.map((it) => [it.href, {
    c: it.p.category,
    n: categoryLabel(it.p.category),
    b: bandOf(it.p.score),
    d: deadlineWithinYear(it.p) ? 1 : 0,
    l: openField(it.p) ? 1 : 0,
  }]));
}

/** A chip. With `href` it is a link that works with no script (a category
    page); the island turns it into a toggle, and its state is `aria-current`
    (a link has no `aria-pressed`). Without `href` it is a button, which lives
    only inside a script-only row. */
function Chip({ k, v, href, label, n }: { k: string; v: string; href?: string; label: string; n: number }) {
  const inner = <>{label}<span className="lf-chip-n">{n}</span></>;
  return href
    ? <a className="lf-chip" data-k={k} data-v={v} href={href} aria-current="false">{inner}</a>
    : <button type="button" className="lf-chip" data-k={k} data-v={v} aria-pressed="false">{inner}</button>;
}

function Row({ label, js, children }: { label: string; js?: boolean; children: ReactNode }) {
  return (
    <div className={js ? "lf-find-row lf-find-js" : "lf-find-row"} role="group" aria-label={label}>
      <span className="lf-find-k" aria-hidden="true">{label}</span>
      <span className="lf-find-v lf-chips">{children}</span>
    </div>
  );
}

/** Drawn for this site: solid, on the 16-unit grid, like the category glyphs —
    a ring (even-odd) and its handle. */
const Magnifier = () => (
  <svg className="lf-q-glyph" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true">
    <path fillRule="evenodd" d="M6.75 1.5a5.25 5.25 0 1 0 0 10.5a5.25 5.25 0 1 0 0-10.5Z M6.75 3.1a3.65 3.65 0 1 1 0 7.3a3.65 3.65 0 1 1 0-7.3Z" />
    <path d="M9.9 11.03l1.13-1.13l3.72 3.72l-1.13 1.13Z" />
  </svg>
);

const Caret = () => (
  <svg className="lf-find-caret" viewBox="0 0 10 10" width="10" height="10" fill="currentColor" aria-hidden="true">
    <path d="M2.2 3.6h5.6a.4.4 0 0 1 .3.66L5.3 7.1a.4.4 0 0 1-.6 0L1.9 4.26a.4.4 0 0 1 .3-.66Z" />
  </svg>
);

/** The bar: the search box, the chips, the count. `categories` is false on
    /by-category, whose index of folds already is the category list. */
export function FilterBar({ items, categories }: { items: Item[]; categories: boolean }) {
  const cats = categoryCounts();
  const bands = BAND_RANGES.map((b) => ({ ...b, n: items.filter((it) => bandOf(it.p.score) === b.id).length })).filter((b) => b.n > 0);
  const deadline = items.filter((it) => deadlineWithinYear(it.p)).length;
  const open = items.filter((it) => openField(it.p)).length;
  return (
    <section className={categories ? "lf-find" : "lf-find lf-find--cat"} data-find aria-label="Search and filter the problems">
      <div className="lf-find-row lf-find-js">
        <label className="lf-find-k" htmlFor="lf-q">Search</label>
        <span className="lf-find-v lf-find-top">
          <span className="lf-q-wrap">
            <Magnifier />
            <input id="lf-q" className="lf-q" type="search" data-q autoComplete="off" spellCheck={false}
              enterKeyHint="search" placeholder="Title, story or solution" aria-keyshortcuts="/" />
            <kbd className="lf-key" aria-hidden="true">/</kbd>
          </span>
          {/* phone only: the chips fold behind this one toggle (a CSS checkbox,
              like the rows' "Show more"), so the first row stays on screen */}
          <label htmlFor="lf-find-cb" className="lf-find-toggle">
            Filter<span className="lf-find-live" data-live hidden />
            <Caret />
          </label>
        </span>
      </div>
      <input type="checkbox" id="lf-find-cb" className="lf-find-cb" aria-label="Show the filters" />
      <div className="lf-find-chips">
        {categories && (
          <Row label="Category">
            {CATEGORIES.filter((c) => cats[c] > 0).map((c) => (
              <Chip key={c} k="cat" v={c} href={`/category/${c}`} label={categoryLabel(c)} n={cats[c]} />
            ))}
          </Row>
        )}
        <Row label="Opportunity" js>
          {bands.map((b) => <Chip key={b.id} k="band" v={b.id} label={b.label} n={b.n} />)}
        </Row>
        <Row label="Also" js>
          <Chip k="flag" v="d" label="Deadline within a year" n={deadline} />
          <Chip k="flag" v="l" label="Nobody sells it here yet" n={open} />
        </Row>
      </div>
      <div className="lf-find-row lf-find-count">
        <span className="lf-find-k" />
        <div className="lf-find-v">
          <p>
            <span data-count aria-live="polite">{items.length} problems</span>
            <button type="button" className="lf-find-clear" data-clear hidden>Clear</button>
          </p>
          <p className="lf-find-none" data-none hidden>No problems match these words and filters.</p>
        </div>
      </div>
      <script
        id="lf-find-idx"
        type="application/json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(facetIndex(items)).replace(/</g, "\\u003c") }}
      />
    </section>
  );
}
