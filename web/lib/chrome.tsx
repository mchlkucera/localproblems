// Gazette chrome — reproduces the v1.3 hand-built structures verbatim.
// Class vocabulary comes from shared.css only; nothing invented here.
import { extractDate } from "./data";
import { isoWeek, pad2 } from "./format";

/** Gazette numbering. Lives in the footer house line only (owner, 2026-08-19):
    the masthead's vol./no. slot passed to the About link. */
export function issueLine(): { vol: string; no: string } {
  const date = extractDate();
  return { vol: date.slice(0, 4), no: pad2(isoWeek(date)) };
}

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

export const SOURCE_NAV = [
  ["/sources/funded", "Funded"],
  ["/sources/regulation", "Regulation"],
  ["/sources/tenders", "Tenders"],
  ["/sources/demand", "Demand"],
] as const;

/** The two surfaces, kept visibly distinct: the problem register, and the
    source ledgers it is distilled from. About lives in the masthead, not here. */
export function SiteNav({ current }: { current?: string }) {
  return (
    <nav className="filters">
      <a href="/" aria-current={current === "/" ? "page" : undefined}>Problems</a>
      {"  ·  Sources: "}
      {SOURCE_NAV.map(([href, label], i) => (
        <span key={href}>
          {i > 0 && " · "}
          <a href={href} aria-current={current === href ? "page" : undefined}>{label}</a>
        </span>
      ))}
    </nav>
  );
}

export function FooterHouseLine() {
  const { vol, no } = issueLine();
  return <>Data as recorded, no warranty. Sources with links. Extract no. {no}/{vol}, generated automatically.</>;
}

export const CORRECTIONS_MAILTO = "mailto:corrections@localproblems.org?subject=CORRECTION";

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
    if (days <= 0) t.textContent = 'today';
    else if (days === 1) t.textContent = 'yesterday';
    else if (days < 7) t.textContent = days + ' days ago';
    // 7+ days: keep the ISO date — a register cites, it doesn't reminisce.
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
