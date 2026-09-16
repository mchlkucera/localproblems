// /lab/modern/how-it-works — the three-circle Venn, COPIED from the front
// page's header (../page.tsx, 2026-09-16) rather than imported: that file is
// being edited by another session, and the Venn is not exported from it. The
// drawing, its hover cards and their words are the front page's, unchanged;
// its styles are read from ../front.css (`.lf-venn*`), so the two figures stay
// one design. If the front page's Venn changes, change this copy with it.
//
// Three monoline circles, the shared core faintly filled. r = 40, centres 58
// apart; every label sits inside the 344×160 box so it scales on a phone.
// Each circle (with its label) and the core is a focusable part; hovering,
// focusing or tapping one shows its card under the figure, and hovering the
// figure anywhere else explains the whole drawing. CSS only (`:has`), no JS.
import type { ReactNode } from "react";

const VENN_TIPS = [
  {
    k: "all",
    h: "What this diagram means",
    t: "Each circle is one kind of public evidence. A problem is most worth building for where all three overlap: people feel it, something is pushing buyers to act, and a similar product already sells abroad, so you aren’t guessing.",
  },
  { k: "people", h: "People want", t: "People are visibly asking for this, or complaining that it’s missing." },
  { k: "gov", h: "Government wants", t: "A new rule, a deadline or public money is pushing buyers to act." },
  { k: "abroad", h: "Works abroad", t: "A company in another country already sells this, so there is proof that buyers pay for it." },
  {
    k: "core",
    h: "Where all three meet",
    t: "The register looks for problems in this middle area. Not every problem on the list sits here; its opportunity score shows how strong the evidence is.",
  },
] as const;

function VennPart({ k, label, children }: { k: string; label: string; children: ReactNode }) {
  return (
    <g className="lf-venn-part" data-k={k} tabIndex={0} role="img" aria-label={label} aria-describedby={`lf-venn-${k}`}>
      {children}
    </g>
  );
}

export function Venn({ className }: { className?: string }) {
  return (
    <div className={className ? `lf-venn-fig ${className}` : "lf-venn-fig"}>
      <svg className="lf-venn" viewBox="0 0 344 160" width="344" height="160" role="group" aria-label="What the register looks for">
        <VennPart k="people" label="People want">
          <rect className="lf-venn-hit" x="0" y="30" width="82" height="26" />
          <circle cx="124" cy="44" r="40" />
          <text x="74" y="48" textAnchor="end">People want</text>
        </VennPart>
        <VennPart k="gov" label="Government wants">
          <rect className="lf-venn-hit" x="224" y="30" width="120" height="26" />
          <circle cx="182" cy="44" r="40" />
          <text x="232" y="48">Government wants</text>
        </VennPart>
        <VennPart k="abroad" label="Works abroad">
          <rect className="lf-venn-hit" x="108" y="138" width="90" height="22" />
          <circle cx="153" cy="94.23" r="40" />
          <text x="153" y="154" textAnchor="middle">Works abroad</text>
        </VennPart>
        <VennPart k="core" label="Where all three meet">
          <path d="M143.64 55.34A40 40 0 0 1 162.36 55.34A40 40 0 0 1 153 71.55A40 40 0 0 1 143.64 55.34Z" />
        </VennPart>
      </svg>
      <div className="lf-venn-tips">
        {VENN_TIPS.map((tip) => (
          <p key={tip.k} id={`lf-venn-${tip.k}`} className="lf-venn-tip" data-k={tip.k} role="tooltip">
            <strong>{tip.h}</strong> {tip.t}
          </p>
        ))}
      </div>
    </div>
  );
}
