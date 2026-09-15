// /lab/problem — the citation device.
//
// AT REST: a quiet gray pill carrying the publisher's short name ("NÚKIB",
// "Registr smluv"); a run of sources collapses to the first name plus "+2".
// ON PEEK: a card anchored under the pill — monogram, publisher, domain, date,
// the source's title, the one plain line saying why it backs the claim, the
// source's own words when the ingest captured them, and "Open source ↗".
//
// NATIVE FIRST. The pill is a <button popovertarget>, the card a `popover=auto`
// element positioned with CSS anchor positioning — so click/tap opens it,
// Escape and an outside click close it, and focus returns to the pill, all
// with no script. `peek-hover.tsx` only adds hover-intent and focus-to-open on
// top. Every card links out to the source and down to its ledger row (#sN).
import type { CSSProperties, ReactNode } from "react";
import { clip, type LabSource } from "./sources";

export type CiteCtx = {
  sources: LabSource[];
  /** Per-page counter — every pill instance owns its own card + anchor name. */
  seq: { n: number };
  /** The section being rendered, recorded against each cited source. */
  section: string;
  cited: Map<number, string[]>;
};

export function newCtx(sources: LabSource[]): CiteCtx {
  return { sources, seq: { n: 0 }, section: "", cited: new Map() };
}

function record(ctx: CiteCtx, nums: number[]) {
  for (const n of nums) {
    const list = ctx.cited.get(n) ?? [];
    list.push(ctx.section);
    ctx.cited.set(n, list);
  }
}

const EXT = { target: "_blank", rel: "noopener noreferrer" } as const;

/** One source inside a peek card. `compact` when the card holds a run. */
function PeekEntry({ s, compact }: { s: LabSource; compact: boolean }) {
  return (
    <span className="ls-pk-entry">
      <span className="ls-pk-head">
        <span className="ls-mono" aria-hidden="true">{s.mono}</span>
        <span className="ls-pk-pub">{s.publisher}</span>
        {s.host && s.host !== s.publisher && <span className="ls-pk-host">{s.host}</span>}
      </span>
      {s.url ? (
        <a className="ls-pk-title" href={s.url} {...EXT}>{s.title}</a>
      ) : (
        <span className="ls-pk-title">{s.title}</span>
      )}
      {s.why && <span className="ls-pk-why">{clip(s.why, compact ? 210 : 320)}</span>}
      {s.quote && (
        <span className="ls-pk-quote">
          <span className="ls-pk-qlabel">In the source’s words</span>
          <span className="ls-pk-qtext">“{clip(s.quote, compact ? 150 : 240)}”</span>
        </span>
      )}
      <span className="ls-pk-foot">
        <span className="ls-pk-meta">
          {s.typeLabel} · <time dateTime={s.date}>{s.dateLabel}</time>
        </span>
        <a className="ls-pk-ref" href={`#s${s.n}`} data-peek-close="" aria-label={`Source ${s.n} in the list below`} title="In the list below">#{s.n}</a>
        {s.url && (
          <a className="ls-pk-open" href={s.url} {...EXT}>
            Open source<span aria-hidden="true"> ↗</span>
          </a>
        )}
      </span>
    </span>
  );
}

/** The two halves of a citation: the pill (goes inline, glued to the word
    before it) and its card (a sibling, hidden until shown). Returned apart so
    the prose renderer can wrap the pill in a no-break span without trapping
    the card inside it. */
export function citeParts(nums: number[], ctx: CiteCtx): { pill: ReactNode; peek: ReactNode } {
  const group = nums.map((n) => ctx.sources[n - 1]);
  const more = group.length - 1;
  return peekParts(nums, ctx, {
    record: true,
    className: "ls-cite",
    children: (
      <>
        <span className="ls-cite-name">{group[0].publisher}</span>
        {more > 0 && <span className="ls-cite-more">+{more}</span>}
      </>
    ),
  });
}

/** Any trigger that peeks: the inline pill, or a card in the top strip
    (`record: false` — the strip is navigation, not a citation). */
export function peekParts(
  nums: number[],
  ctx: CiteCtx,
  o: { record: boolean; className: string; children: ReactNode },
): { pill: ReactNode; peek: ReactNode } {
  if (o.record) record(ctx, nums);
  const id = `ls-c${++ctx.seq.n}`;
  const anchor = `--${id}`;
  const group = nums.map((n) => ctx.sources[n - 1]);
  const first = group[0];
  const label =
    group.length === 1
      ? `Source ${first.n}: ${first.title}, ${first.publisher}`
      : `${group.length} sources: ${group.map((s) => s.title).join("; ")}`;

  const pill = (
    <button
      type="button"
      className={o.className}
      popoverTarget={id}
      aria-label={label}
      data-peek=""
      style={{ anchorName: anchor } as CSSProperties}
    >
      {o.children}
    </button>
  );

  const peek = (
    <span
      id={id}
      popover="auto"
      role="dialog"
      aria-label={group.length === 1 ? "Source preview" : `${group.length} sources`}
      className={group.length > 1 ? "ls-peek ls-peek--run" : "ls-peek"}
      style={{ positionAnchor: anchor } as CSSProperties}
    >
      {group.length > 1 && <span className="ls-pk-count">{group.length} sources</span>}
      {group.map((s) => (
        <PeekEntry key={s.n} s={s} compact={group.length > 1} />
      ))}
    </span>
  );

  return { pill, peek };
}

/** A citation outside running prose (ledger rows): pill then card. A plain
    function, not a component, on purpose — it records the citation into `ctx`
    when CALLED, so the page can build every section first and then read the
    complete citation counts for the strip at the top. */
export function cite(nums: number[], ctx: CiteCtx): ReactNode {
  const { pill, peek } = citeParts(nums, ctx);
  return (
    <span className="ls-cite-slot">
      {pill}
      {peek}
    </span>
  );
}
