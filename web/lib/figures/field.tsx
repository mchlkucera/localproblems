// lib/figures — a company's maturity mark and the dot that opens its card.
//
// MaturityDot: the 10px mark every company row, LocalMatrix and CompMap draw.
// DotPeek and firstLine: shared by LocalMatrix and CompMap.
//
// Pure: no hooks, no client code.
import type { CSSProperties, ReactNode } from "react";
import { EXT, ExtArrow } from "../site/cite";

/** `null` = maturity not on file (comps[] carries none yet). */
export type Maturity = "established" | "early" | null;

/** 10px mark: filled = established, ring = early, gray fill = not on file. */
export function MaturityDot({ m }: { m: Maturity }): ReactNode {
  const cls = m === "established" ? "lk-dot is-est" : m === "early" ? "lk-dot is-early" : "lk-dot is-none";
  return <span className={cls} aria-hidden="true" />;
}

// ---- DotPeek: one company as a dot that opens a small card (owner,
// 2026-09-17: "just place dots there, so that I can hover them and see more").
//
// Shared by LocalMatrix and CompMap. The dot is a native trigger, the card a
// native popover, and both borrow the source peek's classes so they read as
// one system and ride the same machinery:
//   · `data-peek` on the button: PeekHover's selector, so hover-intent, the
//     stay-open-inside-the-card grace and click-to-pin come for free
//   · `ls-peek` on the card: its look, its anchor placement and, at ≤640px,
//     its bottom sheet (problem.css). kit.css only retimes the motion.
// Without JS, click, tap or Enter opens the card and Escape closes it.
// Sources are not drawn here: the figure has no page citation context, and a
// peek inside a peek is exactly the complexity this replaces. The card points
// to Read more, where every company row carries its pills.

const MARKERS = /\s*\[S\d+(?:\s*,\s*S?\d+)*\](?!\()/g;

/** The first sentence (or `;`-clause) of a ledger line, markers stripped. */
export function firstLine(s: string): string {
  const t = s.replace(MARKERS, "").replace(/\s+/g, " ").trim().split(/;\s+/)[0];
  const m = t.match(/^.+?(?<!\b(?:incl|e\.g|i\.e|approx|vs|Inc|Ltd|Co|St|Dr|No|resp))[.!?](?=\s+[A-Z(„"]|\s*$)/);
  const out = m ? m[0] : t;
  return /[.!?…]$/.test(out) ? out : `${out}.`;
}

export type DotPeekProps = {
  id: string;
  /** The button's whole accessible name: "Secfix, Germany, since 2021". */
  label: string;
  name: string;
  href?: string;
  m: Maturity;
  /** The card's quiet head line, joined with " · ". */
  head: string[];
  line: string;
  className?: string;
  style?: CSSProperties;
  /** The mark inside the button; the MaturityDot by default. */
  mark?: ReactNode;
  /** `data-i` on the button, for a figure's own :has() highlight. */
  index?: number;
};

export function DotPeek(o: DotPeekProps): ReactNode {
  const anchor = `--${o.id}`;
  const cls = o.m === "established" ? "is-est" : o.m === "early" ? "is-early" : "is-none";
  return (
    <>
      <button
        type="button"
        className={`lk-pin ${cls}${o.className ? ` ${o.className}` : ""}`}
        popoverTarget={o.id}
        aria-label={o.label}
        data-peek=""
        data-i={o.index}
        style={{ ...o.style, anchorName: anchor } as CSSProperties}
      >
        {o.mark ?? <MaturityDot m={o.m} />}
      </button>
      <div id={o.id} popover="auto" role="dialog" aria-label={o.name} className="ls-peek lk-pk" style={{ positionAnchor: anchor } as CSSProperties}>
        <span className="ls-pk-entry">
          <span className="ls-pk-head">
            <MaturityDot m={o.m} />
            <span className="ls-pk-pub">{o.head[0]}</span>
            {o.head.length > 1 && <span className="ls-pk-host">{o.head.slice(1).join(" · ")}</span>}
          </span>
          {o.href
            ? <a className="ls-pk-title" href={o.href} {...EXT}>{o.name}<ExtArrow /></a>
            : <span className="ls-pk-title">{o.name}</span>}
          <span className="ls-pk-why">{o.line}</span>
          <span className="ls-pk-foot">Sources and the full note are in Read more.</span>
        </span>
      </div>
    </>
  );
}
