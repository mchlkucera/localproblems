// MOCKUPS ONLY (2026-09-18) — three ways to find a problem in the register,
// built as their own routes (/filter-a, /filter-b, /filter-c) so the owner can
// click all three before one of them touches the real front page. NOTHING here
// is imported by `/` or `/by-category`; `lib/site/front.tsx` is untouched, and
// these pages reuse its `Entry`, `item` and `byOpportunity` rather than copying
// a row card.
//
// THE RULES THESE OBEY
//   · Build-time JS is free; a client script is a tiny island that only HIDES
//     rows already in the HTML. No library, no "use client" (check-site S2), no
//     component state — one inline module per page, under 2 kB of our own code.
//   · The page is complete with scripts off: all 29 rows render, the count line
//     states the plain total ("29 problems", never "29 of 29"), the category
//     chips are real links to /category/<slug>, and every control a dead script
//     would leave inert is hidden by CSS alone — `@media (scripting: enabled)`,
//     never a class the script adds. A control that cannot work is not shown.
//   · NOTHING in either island touches the DOM before React hydrates: every
//     aria state is server-rendered and the script only flips a value that is
//     already in the HTML, on a click or a keystroke. (The first cut set
//     `role`/`aria-pressed` on load and Next's dev overlay caught it as a
//     hydration mismatch, which is exactly what that gate is for.)
//   · No hover-only content. Chips are links or buttons: Tab reaches them,
//     Enter activates them. The search box takes Escape to clear. The palette
//     is a native popover: it opens on click without a script and closes on
//     Escape without one.
//   · One font, the gray ramp, teal only where the record page already spends
//     it (the meter), the score dots in the record page's three tones.
//
// EVERY FACET IS DERIVED, never authored:
//   category  = p.category                      (counts = categoryCounts())
//   band      = the SCORING.md thresholds (lib/scorecard BANDS), as numbers
//   deadline  = a source dated after the extract date and within 12 months of
//               it — the register's own clock (extractDate()), never today's
//   open field= no local seller recorded as `competes: direct`, which is the
//               same fact the row's meter card states as "No Czech seller on file"
import type { ReactNode } from "react";
import {
  CATEGORIES, categoryCounts, extractDate, registerRows, type Problem,
} from "../data";
import { categoryLabel } from "../format";
import { BANDS } from "../scorecard";
import { CORRECTIONS_MAILTO } from "../chrome";
import { TopBar } from "./bar";
import { CountrySwitcher } from "./country";
import { Entry, byOpportunity, item, type Item } from "./front";
import { protoScores, protoTotal } from "./score-proto";

// ---- facets ----------------------------------------------------------------

/** The same date arithmetic the register already does: strings, ISO, no clock. */
function plusYear(iso: string): string {
  const [y, m, d] = iso.split("-");
  return `${Number(y) + 1}-${m}-${d}`;
}

const BAND_MINS = BANDS.map(([min]) => min); // [10, 8, 5, 0]

/** Which band a score falls in, named by its floor. */
export function bandOf(score: number): string {
  return String(BAND_MINS.find((min) => score >= min) ?? 0);
}

/** "10–12", "8–9", "5–7", "0–4" — the thresholds as numbers, no rubric words. */
export const BAND_RANGES = BAND_MINS.map((min, i) => ({
  id: String(min),
  label: `${min}–${i === 0 ? 12 : BAND_MINS[i - 1] - 1}`,
}));

/** A dated rule lands within a year of the extract date. */
export function deadlineWithinYear(p: Problem): boolean {
  const today = extractDate();
  const limit = plusYear(today);
  return p.sources.some((s) => s.date > today && s.date <= limit);
}

/** Nobody sells it here yet: no local player recorded as direct competition. */
export function openField(p: Problem): boolean {
  return !(p.locals ?? []).some((l) => l.competes === "direct");
}

type Facet = { c: string; b: string; d: 0 | 1; l: 0 | 1; t?: string };

const searchText = (it: Item) =>
  [it.p.title, it.brief ?? "", it.solution, it.goodFor ?? "", categoryLabel(it.p.category), it.p.category]
    .join(" ")
    .toLowerCase();

/** href → facets. The rows carry no new attributes, so `Entry` stays as the
    front page renders it; the script keys each <li> by its title link. */
export function facetIndex(items: Item[], withText: boolean): Record<string, Facet> {
  const out: Record<string, Facet> = {};
  for (const it of items) {
    const f: Facet = {
      c: it.p.category,
      b: bandOf(it.p.score),
      d: deadlineWithinYear(it.p) ? 1 : 0,
      l: openField(it.p) ? 1 : 0,
    };
    if (withText) f.t = searchText(it);
    out[it.href] = f;
  }
  return out;
}

export function FacetData({ items, withText }: { items: Item[]; withText: boolean }) {
  return (
    <script
      id="fm-idx"
      type="application/json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(facetIndex(items, withText)).replace(/</g, "\\u003c") }}
    />
  );
}

/** How many rows each facet would show — counted here, at build time, so a
    chip's number is the register's own and cannot drift from the list. */
export function facetCounts(items: Item[]) {
  const cats = categoryCounts();
  return {
    cats: CATEGORIES.filter((c) => cats[c] > 0).map((c) => ({ id: c, label: categoryLabel(c), n: cats[c] })),
    bands: BAND_RANGES.map((b) => ({ ...b, n: items.filter((it) => bandOf(it.p.score) === b.id).length }))
      .filter((b) => b.n > 0),
    deadline: items.filter((it) => deadlineWithinYear(it.p)).length,
    open: items.filter((it) => openField(it.p)).length,
  };
}

// ---- chrome ----------------------------------------------------------------

const OPTIONS = [
  { id: "a", href: "/filter-a", label: "A · chips" },
  { id: "b", href: "/filter-b", label: "B · search + chips" },
  { id: "c", href: "/filter-c", label: "C · keyboard" },
] as const;

/** A mockup says so, and lets the owner jump to the other two. */
function MockFlag({ current, note }: { current: string; note: string }) {
  return (
    <div className="fm-flag">
      <div className="lf-wrap fm-flag-in">
        <span className="fm-flag-k">Mockup</span>
        <span className="fm-flag-t">{note}</span>
        <span className="fm-flag-opts">
          {OPTIONS.map((o) => (
            <a key={o.id} href={o.href} aria-current={o.id === current ? "page" : undefined}>{o.label}</a>
          ))}
          <a href="/">Live front page</a>
        </span>
      </div>
    </div>
  );
}

/** A chip. `href` makes it a link that works with no script (the category
    pages); without one it is a button, shown only where scripting is enabled
    (`@media (scripting: enabled)`), so nothing inert is ever on screen.

    EVERY ARIA STATE IS SERVER-RENDERED, and nothing in the island touches the
    DOM before React hydrates: a chip toggled by script flips a value that is
    already in the HTML. A link cannot carry `aria-pressed` (its role is link,
    not button), so its state is `aria-current` — "the one of this set you are
    looking at" — which is what a selected category chip means. */
function Chip({ k, v, href, label, n }: { k: string; v: string; href?: string; label: string; n: number }) {
  const inner = (
    <>
      {label}
      <span className="fm-chip-n">{n}</span>
    </>
  );
  return href
    ? <a className="fm-chip" data-k={k} data-v={v} href={href} aria-current={false}>{inner}</a>
    : <button type="button" className="fm-chip fm-chip--js" data-k={k} data-v={v} aria-pressed="false">{inner}</button>;
}

function ChipRow({ label, children }: { label: string; children: ReactNode }) {
  return (
    <div className="fm-row">
      <span className="fm-row-k">{label}</span>
      <span className="fm-row-v">{children}</span>
    </div>
  );
}

/** The chip bar, shared by A and B. Category chips are links; the rest are
    buttons inside `.fm-js`, which the stylesheet keeps hidden until the script
    sets `data-js` on the page. */
export function ChipBar({ items, search }: { items: Item[]; search: boolean }) {
  const f = facetCounts(items);
  return (
    <section className="fm-bar" aria-label="Filter the register">
      {search && (
        <div className="fm-row fm-js">
          <label className="fm-row-k" htmlFor="fm-q">Search</label>
          <span className="fm-row-v">
            <input
              id="fm-q" className="fm-q" type="search" data-q autoComplete="off"
              placeholder="Title, story, suggested solution, category…"
            />
          </span>
        </div>
      )}
      <ChipRow label="Category">
        {f.cats.map((c) => (
          <Chip key={c.id} k="cat" v={c.id} href={`/category/${c.id}`} label={c.label} n={c.n} />
        ))}
      </ChipRow>
      <div className="fm-js">
        <ChipRow label="Opportunity">
          {f.bands.map((b) => <Chip key={b.id} k="band" v={b.id} label={b.label} n={b.n} />)}
        </ChipRow>
        <ChipRow label="Also">
          <Chip k="flag" v="d" label="Deadline within a year" n={f.deadline} />
          <Chip k="flag" v="l" label="Nobody sells it here yet" n={f.open} />
          <button type="button" className="fm-clear" data-clear>Clear</button>
        </ChipRow>
      </div>
    </section>
  );
}

/** The one honest count. With scripts off it stays exactly this: the total. */
export function CountLine({ n }: { n: number }) {
  return (
    <div className="fm-count-wrap">
      <p className="fm-count" data-count aria-live="polite">{n} problems</p>
      <p className="fm-none" data-none hidden>
        No problems match. <button type="button" className="fm-clear" data-clear>Clear filters</button>
      </p>
    </div>
  );
}

/** The register, grouped by opportunity band, exactly as the front page groups
    it — `Entry` and `byOpportunity` are imported, never re-implemented. Each
    section carries the two hooks the script needs: `data-sec` and
    `data-sec-count`, both true as rendered. */
export function Register({ items }: { items: Item[] }) {
  return (
    <>
      {byOpportunity(items).map((g) => (
        <section key={g.id} className="lf-sec" data-sec aria-labelledby={`${g.id}-h`}>
          <header className="lf-sec-h">
            <h2 id={`${g.id}-h`}>{g.label}</h2>
            <p data-sec-count>{g.items.length} {g.items.length === 1 ? "problem" : "problems"}</p>
          </header>
          <ol className="lf-entries">
            {g.items.map((it) => <Entry key={it.p.id} it={it} showCategory />)}
          </ol>
        </section>
      ))}
    </>
  );
}

function Foot() {
  return (
    <footer className="lf-foot">
      <div className="lf-wrap lf-foot-in">
        <span>localproblems.org · Czechia · mockup</span>
        <a href={CORRECTIONS_MAILTO}>Report a correction</a>
      </div>
    </footer>
  );
}

export function rows(): Item[] {
  return registerRows().map(item);
}

/** The page shell for A and B: the real top bar, the mockup flag, the lede the
    front page uses shortened to one line, then the bar, the count and the list. */
export function ChipPage({ current, note, search }: { current: string; note: string; search: boolean }) {
  const items = rows();
  return (
    <div className="lab lf fm" data-fm>
      <TopBar current="problems" />
      <MockFlag current={current} note={note} />
      <main className="lf-wrap">
        <section className="fm-intro">
          <h1>Czech problems worth solving</h1>
        </section>
        <ChipBar items={items} search={search} />
        <CountLine n={items.length} />
        <Register items={items} />
      </main>
      <Foot />
      <FacetData items={items} withText={search} />
      <script type="module" dangerouslySetInnerHTML={{ __html: CHIP_JS }} />
    </div>
  );
}

// ---- option C: the palette -------------------------------------------------

/** A solid dot in the record page's three score tones (problem.css
    --ls-score-good/mid/bad, mirrored in front.css). Decorative: the score
    reads as text beside it. */
const tone = (n: number, max: number) => (n >= max ? "good" : n / max >= 0.5 ? "mid" : "bad");

/** The result rows are SERVER-RENDERED, all 29 of them, so the palette is a
    complete index of the register with no script at all: the button is a native
    `popovertarget`, so a click opens it and Escape closes it. The script only
    adds `/`, live matching and Enter-opens-the-first-hit. */
function Palette({ items }: { items: Item[] }) {
  return (
    <div id="fm-pal" popover="auto" className="fm-pal" role="dialog" aria-label="Search problems">
      <div className="fm-pal-top">
        <input
          id="fm-pal-q" className="fm-q" type="search" data-q autoComplete="off"
          placeholder="Search problems…" aria-label="Search problems"
        />
        <p className="fm-pal-hint">
          <span className="fm-key">Enter</span> opens the first hit ·
          <span className="fm-key">Esc</span> closes
        </p>
      </div>
      <p className="fm-pal-count" data-count aria-live="polite">{items.length} problems</p>
      <ol className="fm-pal-list">
        {items.map((it) => {
          const t = protoTotal(protoScores(it.p));
          return (
            <li key={it.p.id} className="fm-pal-row" data-row data-t={searchText(it)}>
              <a href={it.href}>
                <span className="fm-pal-name">{it.p.title}</span>
                <span className="fm-pal-cat">{categoryLabel(it.p.category)}</span>
                <span className={`lf-sdot is-${tone(t.n, t.max)}`} aria-hidden="true" />
                <span className="fm-pal-score">{t.n}/{t.max}</span>
              </a>
            </li>
          );
        })}
      </ol>
      <p className="fm-none" data-none hidden>No problems match.</p>
    </div>
  );
}

const NAV = [
  { href: "/", label: "Problems", current: true },
  { href: "/signals/funded", label: "Signals" },
  { href: "/how-it-works", label: "How it works" },
];

/** C's own top bar. The shared `TopBar` is left alone: the search affordance
    has to sit IN the bar, and a mockup does not get to edit the live one. It
    keeps the live bar's promise that all three links stay reachable on a phone
    (owner, 2026-09-17), behind the same native-popover burger. */
function SearchBar() {
  return (
    <header className="lf-bar">
      <div className="lf-bar-in">
        <a className="lf-brand" href="/">localproblems.org</a>
        <CountrySwitcher />
        <button type="button" className="fm-open" popoverTarget="fm-pal">
          <Magnifier />
          <span>Search problems…</span>
          <span className="fm-key fm-key--slash">/</span>
        </button>
        <nav className="lf-nav" aria-label="Site">
          {NAV.map((l) => (
            <a key={l.href} href={l.href} aria-current={l.current ? "page" : undefined}>{l.label}</a>
          ))}
        </nav>
        <button type="button" className="lf-burger" popoverTarget="fm-menu" aria-label="Menu">
          <svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor" aria-hidden="true">
            <path d="M2 3.25h12v1.5H2Z M2 7.25h12v1.5H2Z M2 11.25h12v1.5H2Z" />
          </svg>
        </button>
        <div id="fm-menu" popover="auto" className="lf-menu" role="dialog" aria-label="Menu">
          <nav aria-label="Site menu">
            {NAV.map((l) => (
              <a key={l.href} href={l.href} className="lf-menu-item" aria-current={l.current ? "page" : undefined}>
                {l.label}
              </a>
            ))}
          </nav>
        </div>
      </div>
    </header>
  );
}

/** Drawn for this site on the 16-unit grid, one 1.5 stroke, round caps. */
const Magnifier = () => (
  <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor"
    strokeWidth="1.5" strokeLinecap="round" aria-hidden="true">
    <circle cx="6.75" cy="6.75" r="4.25" />
    <path d="M10 10l3.5 3.5" />
  </svg>
);

export function PalettePage() {
  const items = rows();
  return (
    <div className="lab lf fm" data-fm>
      <SearchBar />
      <MockFlag current="c" note="press / or click Search problems… — the page below is untouched" />
      <main className="lf-wrap">
        <section className="fm-intro">
          <h1>Czech problems worth solving</h1>
        </section>
        <Register items={items} />
      </main>
      <Foot />
      <Palette items={items} />
      <script type="module" dangerouslySetInnerHTML={{ __html: PAL_JS }} />
    </div>
  );
}

// ---- the two islands -------------------------------------------------------
// Both are plain modules: no import, no framework, no state outside the DOM.
// Each only sets `hidden` on rows the HTML already carries, and rewrites the
// two counts it is allowed to rewrite. Turn either off and the page is the
// whole register with a true total.

const CHIP_JS = `
const root = document.querySelector("[data-fm]");
if (root) {
  const idx = JSON.parse(document.getElementById("fm-idx").textContent);
  const rows = [...root.querySelectorAll(".lf-entry")]
    .map((li) => ({ li, f: idx[li.querySelector(".lf-title a").getAttribute("href")] || {} }));
  const chips = [...root.querySelectorAll("[data-k]")];
  const box = root.querySelector("[data-q]");
  const on = { cat: new Set(), band: new Set(), flag: new Set() };
  const state = (c) => (c.tagName === "A" ? "aria-current" : "aria-pressed");
  const apply = () => {
    const q = box ? box.value.trim().toLowerCase() : "";
    let n = 0;
    for (const { li, f } of rows) {
      const ok = (!on.cat.size || on.cat.has(f.c)) && (!on.band.size || on.band.has(f.b))
        && (!on.flag.has("d") || f.d) && (!on.flag.has("l") || f.l) && (!q || (f.t || "").includes(q));
      li.hidden = !ok;
      n += ok;
    }
    for (const sec of root.querySelectorAll("[data-sec]")) {
      const all = [...sec.querySelectorAll(".lf-entry")], vis = all.filter((li) => !li.hidden);
      sec.hidden = !vis.length;
      for (const li of all) li.classList.toggle("fm-first", li === vis[0]);
      sec.querySelector("[data-sec-count]").textContent = vis.length + (vis.length === 1 ? " problem" : " problems");
    }
    const live = on.cat.size + on.band.size + on.flag.size + (q ? 1 : 0);
    root.querySelector("[data-count]").textContent =
      live ? n + " of " + rows.length + " problems" : rows.length + " problems";
    root.querySelector("[data-none]").hidden = n > 0;
  };
  root.addEventListener("click", (e) => {
    const c = e.target.closest("[data-k]");
    if (c) {
      e.preventDefault();
      const s = on[c.dataset.k], v = c.dataset.v;
      s.has(v) ? s.delete(v) : s.add(v);
      c.setAttribute(state(c), String(s.has(v)));
    } else if (e.target.closest("[data-clear]")) {
      for (const k in on) on[k].clear();
      for (const x of chips) x.setAttribute(state(x), "false");
      if (box) box.value = "";
    } else return;
    apply();
  });
  if (box) {
    box.addEventListener("input", apply);
    box.addEventListener("keydown", (e) => { if (e.key === "Escape") { box.value = ""; apply(); } });
  }
}
`.trim();

const PAL_JS = `
const pal = document.getElementById("fm-pal");
if (pal) {
  const box = pal.querySelector("[data-q]");
  const rows = [...pal.querySelectorAll("[data-row]")];
  const count = pal.querySelector("[data-count]");
  const none = pal.querySelector("[data-none]");
  const apply = () => {
    const q = box.value.trim().toLowerCase();
    let n = 0;
    for (const r of rows) {
      const ok = !q || r.dataset.t.includes(q);
      r.hidden = !ok;
      if (ok) n++;
    }
    count.textContent = q ? n + " of " + rows.length + " problems" : rows.length + " problems";
    none.hidden = n > 0;
  };
  box.addEventListener("input", apply);
  box.addEventListener("keydown", (e) => {
    if (e.key !== "Enter") return;
    const hit = rows.find((r) => !r.hidden);
    if (hit) { e.preventDefault(); hit.querySelector("a").click(); }
  });
  pal.addEventListener("toggle", (e) => {
    if (e.newState !== "open") return;
    box.value = "";
    apply();
    box.focus();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey) return;
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
    e.preventDefault();
    if (!pal.matches(":popover-open")) pal.showPopover();
  });
}
`.trim();
