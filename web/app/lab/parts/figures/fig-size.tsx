// Option G — the size of the problem as one number, with a part of the whole
// where the record states one. A bar is drawn only from a share the sources
// give; "more than half" is drawn to half with an open end, never to a guessed
// 60%. A part and a whole taken from two different sources are flagged on the
// figure itself — the ratio is then the register's inference, not a fact.
import type { ReactNode } from "react";
import type { Size } from "./hand";

type Cite = (nums: number[]) => ReactNode;

export function SizeFig({ s, cite }: { s: Size; cite: Cite }) {
  return (
    <div className="fgz">
      <p className="fgz-fig">{s.figure}</p>
      <p className="fgz-counts">{s.counts} {cite(s.cites)}</p>
      {s.segments && (
        <div className="fgz-segs" role="img" aria-label={s.segLabel}>
          {s.segments.map((g, i) => (
            <span key={i} className={g.on ? "fgz-seg is-on" : "fgz-seg"}>{g.label}</span>
          ))}
        </div>
      )}
      {s.segLabel && <p className="fgz-plabel">{s.segLabel}</p>}
      {s.part && (
        <>
          <div className="fgz-bar" role="img" aria-label={s.part.label}>
            <span className={s.part.atLeast ? "fgz-fill is-open" : "fgz-fill"} style={{ width: `${Math.max(1.2, s.part.share * 100)}%` }} />
          </div>
          <p className="fgz-plabel">
            <b>{s.part.label}</b>{s.part.rest && <span className="fgz-rest"> · {s.part.rest}</span>} {cite(s.part.cites)}
          </p>
          {s.part.crossSource && <p className="fgz-flag"><span className="fgz-flag-k">Cross-source</span> {s.part.crossSource}</p>}
        </>
      )}
    </div>
  );
}
