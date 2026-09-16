// lib/figures — the field: who is in it, and since when.
//
// FieldTimeline (article column, 680px): every comparable abroad and every
// Czech player on one year axis, in three lanes — abroad (comps[]), here and
// selling this (locals[] competes: direct), here and nearby (competes:
// adjacent). Filled = established, hollow = early, for Czech players only:
// comps[] carries NO maturity field and the figure will not invent one.
// Players with no published year sit in a gutter, never at a guessed spot.
//
// FieldGrid (rail, 272px): the gap rule as a 2×2 — does it sell this ×
// how proven. Only the "sells this × established" cell takes the space.
//
// Both are pure: no hooks, no client code, `null` when the data is too thin.
import type { ReactNode } from "react";
import { extractDate, type Problem } from "../data";
import { scoreRead } from "../scorecard";
import { median, packRows, shortName, textW, yearFrac } from "./text";

type Mark = { label: string; title: string; year: number | null; est?: boolean };
type LaneKey = "abroad" | "direct" | "adjacent";
type Lane = { key: LaneKey; label: string; sub: string; marks: Mark[] };

const W = 680;
const LW = 124;
const RH = 19;
const FS = 11;
const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;

/** The field on one year axis. `null` with fewer than two dated players: an
    axis with one dot is not a timeline. */
export function FieldTimeline({ p }: { p: Problem }): ReactNode {
  const comps = p.comps ?? [];
  const locals = p.locals ?? [];
  const direct = locals.filter((l) => l.competes === "direct");
  const adjacent = locals.filter((l) => l.competes === "adjacent");
  const lanes: Lane[] = [
    {
      key: "abroad", label: "Abroad", sub: plural(comps.length, "company", "companies"),
      marks: comps.map((c) => ({ label: `${shortName(c.name)} · ${c.geo}`, title: `${c.name}, ${c.geo}, since ${c.since}`, year: c.since })),
    },
    {
      key: "direct", label: "Here, sells this", sub: direct.length ? plural(direct.length, "player", "players") : "none on file",
      marks: direct.map((l) => ({ label: shortName(l.name), title: `${l.name}, ${l.maturity}${l.since ? `, since ${l.since}` : ", year not published"}`, year: l.since ?? null, est: l.maturity === "established" })),
    },
    {
      key: "adjacent", label: "Here, nearby", sub: adjacent.length ? plural(adjacent.length, "sells something else", "sell something else") : "none on file",
      marks: adjacent.map((l) => ({ label: shortName(l.name), title: `${l.name}, ${l.maturity}, sells something else${l.since ? `, since ${l.since}` : ", year not published"}`, year: l.since ?? null, est: l.maturity === "established" })),
    },
  ];
  const years = lanes.flatMap((l) => l.marks.map((m) => m.year)).filter((y): y is number => y !== null);
  if (years.length < 2) return null;

  const today = extractDate();
  const t = yearFrac(today);
  const noYear = lanes.some((l) => l.marks.some((m) => m.year === null));
  const GW = noYear ? 136 : 0;
  const X0 = LW + 12;
  const X1 = W - GW - (noYear ? 20 : 14);
  const y0 = Math.min(...years, Math.floor(t) - 4) - 1;
  const y1 = Math.max(t, Math.max(...years) + 1) + 0.35;
  const x = (yr: number) => X0 + ((yr - y0) / (y1 - y0)) * (X1 - X0);
  const tx = x(t);
  const step = y1 - y0 > 32 ? 10 : y1 - y0 > 14 ? 5 : 2;
  const ticks: number[] = [];
  for (let yr = Math.ceil(y0 / step) * step; yr <= y1; yr += step) ticks.push(yr);

  const AXIS = 24;
  let top = AXIS + 12;
  const laid = lanes.map((lane) => {
    const undated = lane.marks.filter((m) => m.year === null);
    const boxes = lane.marks.filter((m) => m.year !== null).map((m) => {
      const cx = x((m.year as number) + 0.5);
      const w = textW(m.label, FS, 500);
      // right of the dot, unless it would overflow or run across the today line
      const crossesToday = cx < tx && cx + 8 + w > tx - 3;
      const right = cx + 8 + w <= X1 + 4 && !(crossesToday && cx - 8 - w >= X0);
      return { m, cx, right, a: right ? cx - 5 : cx - 8 - w, b: right ? cx + 8 + w : cx + 5 };
    });
    const rows = packRows(boxes, 10);
    const nRows = Math.max(1, rows.length ? Math.max(...rows) + 1 : 1, undated.length);
    const h = Math.max(48, nRows * RH + 16);
    const res = { lane, top, boxes, rows, undated };
    top += h;
    return res;
  });
  const H = top + 6;

  const nowY = Number(today.slice(0, 4));
  const ages = (ys: (number | null)[]) => ys.filter((y): y is number => y !== null).map((y) => nowY - y);
  const mA = median(ages(comps.map((c) => c.since)));
  const mD = median(ages(direct.map((l) => l.since ?? null)));
  const estHere = direct.filter((l) => l.maturity === "established").length;
  const yrs = (n: number) => `${Math.round(n)} ${Math.round(n) === 1 ? "year" : "years"}`;

  return (
    <figure className="lk lk-fig lk-timeline">
      <div className="lk-scroll">
        <svg className="lk-svg" viewBox={`0 0 ${W} ${H}`} width={W} height={H} role="img"
          aria-label={`The field by start year. Abroad: ${comps.map((c) => `${c.name} ${c.since}`).join(", ") || "none"}. Here, selling this: ${direct.map((l) => `${l.name} ${l.since ?? "year not published"} ${l.maturity}`).join(", ") || "none"}.`}>
          <line className="lk-axis" x1={X0} x2={X1} y1={AXIS} y2={AXIS} />
          {ticks.map((yr) => (
            <g key={yr}>
              <line className="lk-grid" x1={x(yr)} x2={x(yr)} y1={AXIS} y2={H - 6} />
              {Math.abs(x(yr) - tx) > 34 && <text className="lk-tick" x={x(yr)} y={AXIS - 8}>{yr}</text>}
            </g>
          ))}
          <line className="lk-today" x1={tx} x2={tx} y1={AXIS - 2} y2={H - 6} />
          <text className="lk-today-t" x={tx} y={AXIS - 8}>today</text>
          {laid.map(({ lane, top: lt, boxes, rows, undated }) => (
            <g key={lane.key} className={`lk-lane lk-lane--${lane.key}`}>
              <line className="lk-sep" x1={0} x2={W} y1={lt} y2={lt} />
              <text className="lk-lk" x={0} y={lt + 20}>{lane.label}</text>
              <text className="lk-ls" x={0} y={lt + 35}>{lane.sub}</text>
              {lane.marks.length === 0 && (
                <text className={lane.key === "direct" ? "lk-none is-open" : "lk-none"} x={X0} y={lt + 20}>
                  {lane.key === "direct" ? "Nobody on file sells this here" : "Nobody on file"}
                </text>
              )}
              {boxes.map(({ m, cx, right }, i) => {
                const cy = lt + 8 + rows[i] * RH + RH / 2;
                return (
                  <g key={m.title} className={m.est === undefined ? "lk-m" : m.est ? "lk-m is-est" : "lk-m is-early"}>
                    <title>{m.title}</title>
                    <circle cx={cx} cy={cy} r={lane.key === "adjacent" ? 3.6 : 4.4} />
                    <text className="lk-lbl" x={right ? cx + 8 : cx - 8} y={cy} dy="0.35em" style={{ textAnchor: right ? "start" : "end" }}>{m.label}</text>
                  </g>
                );
              })}
              {undated.map((m, i) => {
                const gx = W - GW + 4;
                const cy = lt + 8 + i * RH + RH / 2;
                return (
                  <g key={m.title} className={m.est ? "lk-m is-est" : "lk-m is-early"}>
                    <title>{m.title}</title>
                    <circle cx={gx} cy={cy} r={lane.key === "adjacent" ? 3.6 : 4.4} />
                    <text className="lk-lbl" x={gx + 9} y={cy} dy="0.35em">{m.label}</text>
                  </g>
                );
              })}
            </g>
          ))}
          {noYear && (
            <g>
              <line className="lk-gut" x1={W - GW - 8} x2={W - GW - 8} y1={AXIS - 14} y2={H - 6} />
              <text className="lk-gut-t" x={W - GW + 4} y={AXIS - 8}>year not published</text>
            </g>
          )}
        </svg>
      </div>
      <p className="lk-read">
        {mA !== null && <>Abroad, selling for a median of <b>{yrs(mA)}</b>. </>}
        {direct.length === 0
          ? <>Here, <b className="lk-teal">nobody on file sells this</b>{adjacent.length ? `; ${adjacent.length} nearby sell${adjacent.length === 1 ? "s" : ""} something else` : ""}.</>
          : <>Here, the {direct.length === 1 ? "one player" : `${direct.length} players`} selling it {mD !== null ? <>{direct.length === 1 ? "has" : "have"} a median of <b>{yrs(mD)}</b></> : "publish no year"}{estHere ? `, ${estHere} established` : ", all early"}.</>}
      </p>
      <figcaption className="lk-cap">
        Each dot is the year a player started. For a Czech player that is the year it began selling this, or its founding year when that is all that is published: the record’s one <code>since</code> field carries both, so two dots can mean different things. Filled is established, hollow is early. Comparables abroad carry no maturity on file, so they are drawn alike. Height within a lane means nothing; it only keeps names apart. A player with no published year sits in the gutter, never at a guessed year.
      </figcaption>
    </figure>
  );
}

/** Who is in the room, as the gap rule sees it. `null` without local players. */
export function FieldGrid({ p }: { p: Problem }): ReactNode {
  const locals = p.locals ?? [];
  if (locals.length === 0) return null;
  const cell = (c: "direct" | "adjacent", m: "early" | "established") => locals.filter((l) => l.competes === c && l.maturity === m);
  const names = (xs: typeof locals) => {
    const s = xs.map((l) => shortName(l.name));
    return s.length > 3 ? `${s.slice(0, 3).join(", ")} +${s.length - 3}` : s.join(", ");
  };
  const open = locals.every((l) => l.competes !== "direct");
  return (
    <figure className="lk lk-fig lk-grid2" aria-label="Local players: does it sell this, and how proven">
      <div className="lk-g">
        <span />
        <span className="lk-g-ch">Early</span>
        <span className="lk-g-ch">Established</span>
        {(["direct", "adjacent"] as const).map((c) => (
          <div key={c} className="lk-g-row">
            <span className="lk-g-rh">{c === "direct" ? "Sells this" : "Nearby"}</span>
            {(["early", "established"] as const).map((m) => {
              const xs = cell(c, m);
              const key = c === "direct" && m === "established";
              return (
                <span key={m} className={`lk-g-cell${key ? " is-key" : ""}${xs.length ? "" : " is-empty"}${open && c === "direct" ? " is-open" : ""}`}>
                  <b className="lk-g-n">{xs.length}</b>
                  <span className="lk-g-names">{xs.length ? names(xs) : "—"}</span>
                  {key && <span className="lk-g-keyk">takes the space</span>}
                </span>
              );
            })}
          </div>
        ))}
      </div>
      <p className="lk-read lk-read--sm">{scoreRead(p, "gap")}.</p>
      <figcaption className="lk-cap">Only an established player that sells this takes the space; the other cells never move Local opportunity.</figcaption>
    </figure>
  );
}
