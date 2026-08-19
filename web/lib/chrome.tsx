// Gazette chrome — reproduces the v1.3 hand-built structures verbatim.
// Class vocabulary comes from shared.css only; nothing invented here.
import { extractDate } from "./data";
import { isoWeek, pad2 } from "./format";

export function issueLine(): { vol: string; no: string } {
  const date = extractDate();
  return { vol: date.slice(0, 4), no: pad2(isoWeek(date)) };
}

export function Masthead({ index = false }: { index?: boolean }) {
  const { vol, no } = issueLine();
  return (
    <header className={index ? "masthead index-head" : "masthead"}>
      <a className="brand" href="/">localproblems.org</a>
      <span className="issue">vol. {vol} · no. {no}</span>
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
    source ledgers it is distilled from. */
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
      {"  ·  "}
      <a href="/about" aria-current={current === "/about" ? "page" : undefined}>About</a>
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

export function Tally({ s, max }: { s: number; max?: number }) {
  const style = max === undefined
    ? ({ "--s": s } as React.CSSProperties)
    : ({ "--s": s, "--max": max } as React.CSSProperties);
  return <span className="tally" style={style} />;
}

// The status dot and claim devices are retired (owner, 2026-08-13):
// lifecycle statuses live in data frontmatter only until they diverge.
