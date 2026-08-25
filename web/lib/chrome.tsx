// Gazette chrome — reproduces the v1.3 hand-built structures verbatim.
// Class vocabulary comes from shared.css only; nothing invented here.
import { EVIDENCE_TYPES } from "./data";
import { pad2 } from "./format";

/** `current` is the page path; the About link marks itself on /about.
    The right-hand slot keeps the issue line's styling (`.issue`, mono meta). */
export function Masthead({ index = false, current }: { index?: boolean; current?: string }) {
  return (
    <header className={index ? "masthead index-head" : "masthead"}>
      <a className="brand" href="/">localproblems.org</a>
      <a className="issue" href="/about" aria-current={current === "/about" ? "page" : undefined}>About</a>
    </header>
  );
}

/** SIGNALS = the records; SOURCES = the feeds we ingest from (architecture-v3 §9).
    Derived from EVIDENCE_TYPES so registering a type lights up its nav entry in
    the same line that lights up its route — an empty ledger is a registered
    fact, not a hidden one. */
export const SIGNAL_NAV = EVIDENCE_TYPES.map(
  (t) => [`/signals/${t}`, t[0].toUpperCase() + t.slice(1)] as const
);

/** The two surfaces, kept visibly distinct: the problem register, and the
    signal ledgers it is distilled from. About lives in the masthead, not here. */
export function SiteNav({ current }: { current?: string }) {
  return (
    <nav className="filters">
      <a href="/" aria-current={current === "/" ? "page" : undefined}>Problems</a>
      {"  ·  Signals: "}
      {SIGNAL_NAV.map(([href, label], i) => (
        <span key={href}>
          {i > 0 && " · "}
          <a href={href} aria-current={current === href ? "page" : undefined}>{label}</a>
        </span>
      ))}
    </nav>
  );
}

/** The ledger pager — a volume index, not a widget.
 *
 *  THE PAGES ARE REAL DOCUMENTS. The site is pure SSG (SPEC.md §5), so every
 *  page number below is a pre-rendered file and this nav is plain links:
 *  nothing to hydrate, nothing to slice client-side, identical with JS off and
 *  on the photocopy. Client-side paging over a 7.6 MB payload would have moved
 *  the problem rather than fixed it.
 *
 *  NO NEW DEVICE, AND NO ELISION. It is the house `.filters` line the category
 *  and region navs already are — mono, `·` separated, zero-padded, the current
 *  entry marked with `aria-current="page"` for its 2px ink underline — so it
 *  costs the stylesheet nothing. Every page is listed rather than windowed
 *  behind `…`: a 37-page ledger IS 37 pages, the strip states that, and any
 *  page is one click from any other. A window would add a heuristic, two arrow
 *  glyphs and a lie of omission to save four lines of mono text.
 *
 *  One pager, at the foot of the table — where a reader is when the page runs
 *  out. The head of the ledger states the position in the crumb instead of
 *  repeating the strip. */
export function Pager({ base, page, pages }: { base: string; page: number; pages: number }) {
  if (pages < 2) return null;   // a one-page ledger has nothing to page
  return (
    <nav className="filters" aria-label="Ledger pages">
      {"Pages: "}
      {Array.from({ length: pages }, (_, i) => i + 1).map((n) => (
        <span key={n}>
          {n > 1 && " · "}
          <a href={n === 1 ? base : `${base}/${n}`} aria-current={n === page ? "page" : undefined}>
            {pad2(n)}
          </a>
        </span>
      ))}
    </nav>
  );
}

/** The one footer statement every page carries (owner, 2026-08-24): the region,
    and nothing else. The gazette self-narration — "Extract no. NN/YYYY,
    generated automatically", "Data as recorded, no warranty" — was retired
    then; the EXTRACT DATE goes now (owner, 2026-08-25, quoting the line back at
    us: "Czechia · updated 2026-08-25").

    IT WAS A DATE ABOUT US, NOT ABOUT THE EVIDENCE. `extractDate()` is when the
    register's newest record was touched — pipeline bookkeeping — and because it
    printed in the footer of every page it collided with the real currency
    marker wherever one existed. On a record page it was the FIFTH rendering of
    the same date; on the register, the category pages and the signal ledgers
    every row already carries its own date, which is the currency signal a
    reader actually uses. A fact that is either duplicated or irrelevant on
    every page it appears on is page furniture, and page furniture does not
    ship. */
export function FooterHouseLine() {
  return <>Czechia</>;
}

export const CORRECTIONS_MAILTO = "mailto:corrections@localproblems.org?subject=CORRECTION";

/** The corrections invitation, in one place because it is one sentence.
 *
 *  It read "Source wrong? Corrections →" on all six page templates — telegraphic,
 *  and the bare arrow made it look like an internal tool's affordance rather
 *  than an offer to a person. Same target, plain English. Six copies of one
 *  string is also how six copies drift, so it is a component now. */
export function CorrectionsLink() {
  return <a href={CORRECTIONS_MAILTO}>Report a correction</a>;
}

/** Sanctioned exception 2 (design-language v1.3): relative record dates.
    Verbatim v1 snippet; the page reads identically with JS off. */
export function RelDatesScript() {
  const js = `
  document.querySelectorAll('time.rel[datetime]').forEach(function (t) {
    var d = new Date(t.dateTime + 'T00:00:00');
    if (isNaN(d)) return;
    var now = new Date();
    var days = Math.round((new Date(now.getFullYear(), now.getMonth(), now.getDate()) - d) / 864e5);
    t.title = t.dateTime;
    // Notion-style full ladder (owner, 2026-08-20); ISO always kept in datetime + title.
    if (days <= 0) t.textContent = 'today';
    else if (days === 1) t.textContent = 'yesterday';
    else if (days < 7) t.textContent = days + ' days ago';
    else if (days < 30) { var w = Math.round(days / 7); t.textContent = w + (w === 1 ? ' week ago' : ' weeks ago'); }
    else if (days < 365) { var mo = Math.round(days / 30); t.textContent = mo + (mo === 1 ? ' month ago' : ' months ago'); }
    else { var y = Math.round(days / 365); t.textContent = y + (y === 1 ? ' year ago' : ' years ago'); }
  });`;
  return <script dangerouslySetInnerHTML={{ __html: js }} />;
}

/** Sanctioned exception 3 (owner, 2026-08-19): sortable register columns.
    Included on the register and category pages ONLY. Progressive: the
    server-rendered order (score desc) stays the no-JS default and the page
    reads identically with JS off. Clicking a header re-sorts client-side —
    first click descending, second ascending; aria-sort marks the active th.
    Sort keys are the cells' text (zero-padded scores and ISO dates sort
    fine as strings); a td may carry data-sort where its text would not.
    cursor:pointer comes from this script, never from the stylesheet. */
export function SortScript() {
  const js = `
  document.querySelectorAll("table.index").forEach(function (table) {
    var body = table.tBodies[0], head = table.tHead;
    if (!body || !head) return;
    var ths = head.rows[0].cells;
    Array.prototype.forEach.call(ths, function (th, col) {
      th.style.cursor = "pointer";
      th.tabIndex = 0;
      function sort() {
        var dir = th.getAttribute("aria-sort") === "descending" ? "ascending" : "descending";
        Array.prototype.forEach.call(ths, function (h) { h.removeAttribute("aria-sort"); });
        th.setAttribute("aria-sort", dir);
        var key = function (tr) {
          var td = tr.cells[col];
          return td ? (td.getAttribute("data-sort") || td.textContent.trim()) : "";
        };
        Array.prototype.slice.call(body.rows).sort(function (a, b) {
          return key(a).localeCompare(key(b), "en", { numeric: true }) * (dir === "ascending" ? 1 : -1);
        }).forEach(function (tr) { body.appendChild(tr); });
      }
      th.addEventListener("click", sort);
      th.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); sort(); }
      });
    });
  });`;
  return <script dangerouslySetInnerHTML={{ __html: js }} />;
}

export function Tally({ s, max }: { s: number; max?: number }) {
  const style = max === undefined
    ? ({ "--s": s } as React.CSSProperties)
    : ({ "--s": s, "--max": max } as React.CSSProperties);
  return <span className="tally" style={style} />;
}

// The status dot and claim devices are retired (owner, 2026-08-13):
// lifecycle statuses live in data frontmatter only until they diverge.
