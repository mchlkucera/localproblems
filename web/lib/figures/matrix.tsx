// lib/figures — the Czech players as a 2×2 (owner, 2026-09-17: "a 2d
// gartner-like matrix showing established, early etc (just the local
// competition)").
//
//   x  maturity           Early → Established          locals[].maturity
//   y  how directly       Sells something nearby → Sells this   locals[].competes
//
// LOCALS ONLY. comps[] carries no maturity and competes abroad, so it is the
// map's job (CompMap), never a dot here.
//
// Each player is ONE DOT in its quadrant (owner, 2026-09-17: "just place dots
// there, so that I can hover them and see more … using interaction to
// simplify"). Hollow = early, filled = established, the rows' MaturityDot. A
// dot is a DotPeek: a native popover trigger whose card names the company,
// what it sells and since when. Position inside a quadrant carries NO meaning:
// the dots sit on a small lattice, oldest first, with a fixed jitter hashed
// from the name, so a render is deterministic and dots never touch. Each
// quadrant shows its name and a count; the names live in the cards, in the
// buttons' labels and in one visually hidden summary.
//
// LESS TEXT (owner, 2026-09-17: "Make the diagram clearly self explanatory,
// less text!"). No caption, no quadrant names, no counts: the two axes name
// every quadrant, and the dots are the count. The only words inside the
// frame are "The space is still open", in the one quadrant where emptiness
// is the finding.
//
// Colour: gray, except teal where the quadrant is in the builder's favour —
// "new, selling this" always (an early seller does not take the space), and
// "established, selling this" only while it is EMPTY (the space nobody has
// taken). A wash of teal, a teal label, nothing else. No legend: the axes
// already say what a position means, and the dot is the rows' own mark.
import type { CSSProperties, ReactNode } from "react";
import { localHref, type Problem } from "../data";
import { DotPeek, firstLine } from "./field";
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

/** A stable 0..1 from a string (FNV-1a), for the fixed jitter. */
const hash01 = (s: string, salt: number) => {
  let h = 2166136261 ^ salt;
  for (const ch of s) h = Math.imul(h ^ ch.charCodeAt(0), 16777619);
  return ((h >>> 0) % 1000) / 999;
};

/** Lattice slots for n dots in a quadrant about 2× wider than tall:
    fractions of the plot box, plus its height in rows. */
function lattice(names: string[]) {
  const n = names.length;
  const cols = Math.max(1, Math.min(n, Math.ceil(Math.sqrt(n * 2))));
  const rows = Math.ceil(n / cols);
  return {
    rows,
    at: names.map((nm, k) => {
      const r = Math.floor(k / cols);
      const inRow = r === rows - 1 ? n - r * cols : cols;
      const c = k % cols + (cols - inRow) / 2;   // a short last row is centred
      const jx = (hash01(nm, 1) - 0.5) * 0.36, jy = (hash01(nm, 2) - 0.5) * 0.36;
      return { x: (c + 0.5 + jx) / cols, y: (r + 0.5 + jy) / rows };
    }),
  };
}

/** `null` without local players. `scope` keeps popover ids unique when the
    page renders the figure twice (on the page and in its Read more sheet). */
export function LocalMatrix({ p, scope = "" }: { p: Problem; scope?: string }): ReactNode {
  const locals = p.locals ?? [];
  if (locals.length === 0) return null;
  const cell = (c: Competes, m: Maturity) => locals.filter((l) => l.competes === c && l.maturity === m).sort(order);
  const takenBy = cell("direct", "established");

  const quad = (c: Competes, m: Maturity) => {
    const xs = cell(c, m);
    const favour = c === "direct" && (m === "early" || xs.length === 0);
    // one note, in the one quadrant where emptiness is the news
    const note = xs.length === 0 && c === "direct" && m === "established" ? "The space is still open" : null;
    const { rows, at } = lattice(xs.map((l) => l.name));
    const sells = c === "direct" ? "sells this" : "sells something nearby";
    return (
      <div key={`${c}-${m}`} className={`lk-mx-q is-${c} is-${m}${favour ? " is-favour" : ""}`}>
        {xs.length > 0 ? (
          <div className="lk-mx-plot" style={{ "--rows": rows } as CSSProperties}>
            {xs.map((l, i) => (
              <DotPeek
                key={l.name}
                id={`lk-mx${scope}-${c}-${m}-${i}`}
                label={`${l.name}, ${m}, ${sells}${l.since ? `, since ${l.since}` : ""}`}
                name={l.name}
                href={localHref(l)}
                m={l.maturity}
                head={[m === "established" ? "Established" : "Early", c === "direct" ? "Sells this" : "Sells something nearby", ...(l.since ? [`since ${l.since}`] : [])]}
                line={firstLine(l.evidence)}
                style={{ "--x": at[i].x, "--y": at[i].y } as CSSProperties}
              />
            ))}
          </div>
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
    <figure className="lk lk-mx" aria-label="Czech players by maturity and by how directly they sell this">
      <p className="lk-sr">
        {say("direct", "early")} {say("direct", "established")} {say("adjacent", "early")} {say("adjacent", "established")}
        {takenBy.length === 0 ? " No established player sells this here." : ""}
      </p>
      <div className="lk-mx-grid">
        <span className="lk-mx-y is-direct" aria-hidden="true">Sells this</span>
        {quad("direct", "early")}
        {quad("direct", "established")}
        <span className="lk-mx-y is-adjacent" aria-hidden="true">Sells something nearby</span>
        {quad("adjacent", "early")}
        {quad("adjacent", "established")}
        <span className="lk-mx-x is-early" aria-hidden="true">Early</span>
        <span className="lk-mx-x is-est" aria-hidden="true">Established</span>
      </div>
    </figure>
  );
}
