// Gazette chrome — reproduces the v1.3 hand-built structures verbatim, for the
// one page still in the gazette design (the private /sources admin page). Class
// vocabulary comes from shared.css only; nothing invented here.
// CORRECTIONS_MAILTO is shared with the modern pages.
import { EVIDENCE_TYPES } from "./data";

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
    signal ledgers it is distilled from. About lives in the masthead, not here.

    `.sitenav` is a WRAPPER (v1.20): on the desk it is transparent and the nav
    inside it is the `.filters` line it always was; on a phone the wrapper is
    the STRIP — one line that runs off the right edge of the screen and scrolls
    sideways, the way a newspaper's section nav does on a phone. `children` is
    the register's region line, which rides in the same wrapper so the two
    share one strip on a phone and stay two lines on the desk. The v1.19
    footer sink is retired (owner: "a menu in the footer is not a good
    solution"). Markup identical at every width; the strip is CSS. */
export function SiteNav({ current, children }: { current?: string; children?: React.ReactNode }) {
  return (
    <div className="sitenav">
      <nav className="filters" aria-label="Site">
        <a href="/" aria-current={current === "/" ? "page" : undefined}>Problems</a>
        {"  ·  Signals: "}
        {SIGNAL_NAV.map(([href, label], i) => (
          <span key={href}>
            {i > 0 && " · "}
            <a href={href} aria-current={current === href ? "page" : undefined}>{label}</a>
          </span>
        ))}
      </nav>
      {children}
    </div>
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

// The one contact address on the site (owner, 2026-09-16: "Make sure the
// contact is for michal.kucera04@gmail.com"). Every public footer links it.
export const CORRECTIONS_MAILTO = "mailto:michal.kucera04@gmail.com?subject=CORRECTION";

/** The corrections invitation, in one place because it is one sentence.
 *
 *  It read "Source wrong? Corrections →" on all six page templates — telegraphic,
 *  and the bare arrow made it look like an internal tool's affordance rather
 *  than an offer to a person. Same target, plain English. Six copies of one
 *  string is also how six copies drift, so it is a component now. */
export function CorrectionsLink() {
  return <a href={CORRECTIONS_MAILTO}>Report a correction</a>;
}

// The status dot and claim devices are retired (owner, 2026-08-13):
// lifecycle statuses live in data frontmatter only until they diverge.
