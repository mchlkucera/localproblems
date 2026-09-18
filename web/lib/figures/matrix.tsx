// lib/figures — the Czech players as a 2×2 (owner, 2026-09-17: "a 2d
// gartner-like matrix showing established, early etc (just the local
// competition)").
//
//   x  maturity           New → Established          locals[].maturity
//   y  how directly       Sells nearby → Sells this  locals[].competes
//
// LOCALS ONLY. comps[] carries no maturity and competes abroad, so it is the
// map's job (CompMap), never a dot here.
//
// Each player is ONE LABELLED DOT in its quadrant (owner, 2026-09-17: "just
// place dots there, so that I can hover them and see more"; 2026-09-18:
// "include SOME information … like year or name … Keep the axes very
// simple"). Hollow = early, filled = established, the rows' MaturityDot, then
// the short name and, muted, the year it started: "NIS2 Doku · 2025". Dot and
// label are ONE DotPeek button, so the whole label opens the card (name ↗,
// what it sells, since when). Position inside a quadrant carries NO meaning:
// the labels stack as a short list, oldest first, so they are placed
// deterministically and can never overlap; a quadrant of 6+ splits into two
// columns when the matrix is wide. A figure with a crowded quadrant (5+) drops every year when narrow
// (kit.css), so the four quadrants always read alike.
//
// Text is the axes and the labels, nothing else: one short word at each end
// of each axis, no quadrant names, no counts. The only other words are "The
// space is still open", in the one quadrant where emptiness is the finding.
//
// Colour: gray, except teal where the quadrant is in the builder's favour —
// "new, selling this" always (an early seller does not take the space), and
// "established, selling this" only while it is EMPTY (the space nobody has
// taken). A wash of teal, a teal label, nothing else. No legend: the axes
// already say what a position means, and the dot is the rows' own mark.
import type { ReactNode } from "react";
import { localHref, type Problem } from "../data";
import { DotPeek, MaturityDot, firstLine } from "./field";
import { shortName } from "./text";

type Local = NonNullable<Problem["locals"]>[number];
type Competes = Local["competes"];
type Maturity = Local["maturity"];

const QUAD: Record<Competes, Record<Maturity, string>> = {
  direct: { early: "New, selling this", established: "Established, selling this" },
  adjacent: { early: "New, selling something nearby", established: "Established, selling something nearby" },
};

const order = (a: Local, b: Local) =>
  (a.since ?? 9999) - (b.since ?? 9999) || shortName(a.name).localeCompare(shortName(b.name), "cs");

/** `null` without local players. `scope` keeps popover ids unique when the
    page renders the figure twice (on the page and in its Read more sheet). */
export function LocalMatrix({ p, scope = "" }: { p: Problem; scope?: string }): ReactNode {
  const locals = p.locals ?? [];
  if (locals.length === 0) return null;
  const cell = (c: Competes, m: Maturity) => locals.filter((l) => l.competes === c && l.maturity === m).sort(order);
  const takenBy = cell("direct", "established");
  // any quadrant of 5+: a narrow matrix drops every year, so all four read alike
  const crowded = (["direct", "adjacent"] as const).some((c) => (["early", "established"] as const).some((m) => cell(c, m).length > 4));

  const quad = (c: Competes, m: Maturity) => {
    const xs = cell(c, m);
    const favour = c === "direct" && (m === "early" || xs.length === 0);
    // one note, in the one quadrant where emptiness is the news
    const note = xs.length === 0 && c === "direct" && m === "established" ? "The space is still open" : null;
    const sells = c === "direct" ? "sells this" : "sells something nearby";
    return (
      <div key={`${c}-${m}`} className={`lk-mx-q is-${c} is-${m}${favour ? " is-favour" : ""}`}>
        {xs.length > 0 ? (
          <ul className={xs.length > 5 ? "lk-mx-l is-many" : "lk-mx-l"}>
            {xs.map((l, i) => (
              <li key={l.name} className="lk-mx-i">
                <DotPeek
                  id={`lk-mx${scope}-${c}-${m}-${i}`}
                  className="lk-mx-pin"
                  label={`${l.name}, ${m}, ${sells}${l.since ? `, since ${l.since}` : ""}`}
                  name={l.name}
                  href={localHref(l)}
                  m={l.maturity}
                  mark={<>
                    <MaturityDot m={l.maturity} />
                    <span className="lk-mx-t">
                      <span className="lk-mx-n">{shortName(l.name)}</span>
                      {l.since && <span className="lk-mx-s">{"\u00a0·\u00a0"}{l.since}</span>}
                    </span>
                  </>}
                  head={[m === "established" ? "Established" : "Early", c === "direct" ? "Sells this" : "Sells something nearby", ...(l.since ? [`since ${l.since}`] : [])]}
                  line={firstLine(l.evidence)}
                />
              </li>
            ))}
          </ul>
        ) : note ? (
          <p className="lk-mx-none">{note}</p>
        ) : null}
      </div>
    );
  };

  const say = (c: Competes, m: Maturity) => {
    const xs = cell(c, m);
    return `${QUAD[c][m]}: ${xs.length ? xs.map((l) => `${l.name}${l.since ? ` (since ${l.since})` : ""}`).join(", ") : "nobody on file"}.`;
  };

  return (
    <figure className={crowded ? "lk lk-mx is-crowded" : "lk lk-mx"} aria-label="Czech players by maturity and by how directly they sell this">
      <p className="lk-sr">
        {say("direct", "early")} {say("direct", "established")} {say("adjacent", "early")} {say("adjacent", "established")}
        {takenBy.length === 0 ? " No established player sells this here." : ""}
      </p>
      <div className="lk-mx-grid">
        <span className="lk-mx-y is-direct" aria-hidden="true">Sells this</span>
        {quad("direct", "early")}
        {quad("direct", "established")}
        <span className="lk-mx-y is-adjacent" aria-hidden="true">Sells nearby</span>
        {quad("adjacent", "early")}
        {quad("adjacent", "established")}
        <span className="lk-mx-x is-early" aria-hidden="true">New</span>
        <span className="lk-mx-x is-est" aria-hidden="true">Established</span>
      </div>
    </figure>
  );
}
