// Option C — the field, by the year each player started.
// Three lanes on one year axis: companies abroad (comps[]), Czech players that
// sell this (locals[] competes: direct) and Czech players nearby that sell
// something else (competes: adjacent). Filled = established, hollow = early —
// for Czech players only, because comps[] carries NO maturity field and the
// figure will not invent one. Players with no published year sit in a gutter
// rather than at a guessed position. Height inside a lane means nothing; it
// only keeps labels apart.
import type { Problem } from "../../../../lib/data";
import { scoreRead } from "../../../../lib/scorecard";
import { median, packRows, shortName, textW, yearFrac } from "./kit/text";

type Mark = { label: string; title: string; year: number | null; est?: boolean };
type Lane = { key: "abroad" | "direct" | "adjacent"; label: string; sub: string; marks: Mark[] };

const W = 680;
const LW = 124;
const RH = 19;
const FS = 11;

export function FieldStrip({ p, today }: { p: Problem; today: string }) {
  const comps = p.comps ?? [];
  const locals = p.locals ?? [];
  const direct = locals.filter((l) => l.competes === "direct");
  const adjacent = locals.filter((l) => l.competes === "adjacent");
  const plural = (n: number, one: string, many: string) => `${n} ${n === 1 ? one : many}`;
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
  const t = yearFrac(today);
  const noYear = lanes.some((l) => l.marks.some((m) => m.year === null));
  const GW = noYear ? 136 : 0;
  const X0 = LW + 12;
  const X1 = W - GW - (noYear ? 20 : 14);
  const y0 = Math.min(...years, Math.floor(t) - 4) - 1;
  const y1 = Math.max(t, Math.max(...years) + 1) + 0.35;
  const x = (yr: number) => X0 + ((yr - y0) / (y1 - y0)) * (X1 - X0);
  const tx = x(t);
  const span = y1 - y0;
  const step = span > 32 ? 10 : span > 14 ? 5 : 2;
  const ticks: number[] = [];
  for (let yr = Math.ceil(y0 / step) * step; yr <= y1; yr += step) ticks.push(yr);

  // ---- lay out each lane ---------------------------------------------------
  const AXIS = 24;
  let top = AXIS + 12;
  const laid = lanes.map((lane) => {
    const dated = lane.marks.filter((m) => m.year !== null);
    const undated = lane.marks.filter((m) => m.year === null);
    const boxes = dated.map((m) => {
      const cx = x((m.year as number) + 0.5);
      const w = textW(m.label, FS, 500);
      // right of the dot unless it would overflow, or run across the today line
      const crossesToday = cx < tx && cx + 8 + w > tx - 3;
      const right = cx + 8 + w <= X1 + 4 && !(crossesToday && cx - 8 - w >= X0);
      return { m, cx, right, a: right ? cx - 5 : cx - 8 - w, b: right ? cx + 8 + w : cx + 5 };
    });
    const rows = packRows(boxes.map(({ a, b }) => ({ a, b })), 10);
    const nRows = Math.max(1, rows.length ? Math.max(...rows) + 1 : 1, undated.length);
    const h = Math.max(48, nRows * RH + 16);
    const res = { lane, top, h, boxes, rows, undated };
    top += h;
    return res;
  });
  const H = top + 6;

  // ---- the one-line read under the figure, derived -----------------------
  const nowY = Number(today.slice(0, 4));
  const ages = (ys: (number | null)[]) => ys.filter((y): y is number => y !== null).map((y) => nowY - y);
  const aAbroad = ages(comps.map((c) => c.since));
  const aDirect = ages(direct.map((l) => l.since ?? null));
  const mA = median(aAbroad);
  const mD = median(aDirect);
  const estHere = direct.filter((l) => l.maturity === "established").length;

  return (
    <div className="fgs">
      <svg className="fgs-svg" viewBox={`0 0 ${W} ${H}`} width={W} height={H} role="img"
        aria-label={`The field by start year. Abroad: ${comps.map((c) => `${c.name} ${c.since}`).join(", ")}. Here, selling this: ${direct.map((l) => `${l.name} ${l.since ?? "year unknown"} ${l.maturity}`).join(", ") || "none"}.`}>
        {/* axis */}
        <line className="fgs-axis" x1={X0} x2={X1} y1={AXIS} y2={AXIS} />
        {ticks.map((yr) => (
          <g key={yr}>
            <line className="fgs-grid" x1={x(yr)} x2={x(yr)} y1={AXIS} y2={H - 6} />
            {Math.abs(x(yr) - tx) > 34 && <text className="fgs-tick" x={x(yr)} y={AXIS - 8}>{yr}</text>}
          </g>
        ))}
        {/* today */}
        <line className="fgs-today" x1={tx} x2={tx} y1={AXIS - 2} y2={H - 6} />
        <text className="fgs-today-t" x={tx} y={AXIS - 8}>today</text>

        {laid.map(({ lane, top: lt, boxes, rows, undated }) => (
          <g key={lane.key} className={`fgs-lane fgs-lane--${lane.key}`}>
            <line className="fgs-sep" x1={0} x2={W} y1={lt} y2={lt} />
            <text className="fgs-lk" x={0} y={lt + 20}>{lane.label}</text>
            <text className="fgs-ls" x={0} y={lt + 35}>{lane.sub}</text>
            {lane.marks.length === 0 && (
              <text className={lane.key === "direct" ? "fgs-none is-open" : "fgs-none"} x={X0} y={lt + 20}>
                {lane.key === "direct" ? "Nobody on file sells this here" : "Nobody on file"}
              </text>
            )}
            {boxes.map(({ m, cx, right }, i) => {
              const cy = lt + 8 + rows[i] * RH + RH / 2;
              return (
                <g key={m.title} className={m.est === undefined ? "fgs-m" : m.est ? "fgs-m is-est" : "fgs-m is-early"}>
                  <title>{m.title}</title>
                  <circle cx={cx} cy={cy} r={lane.key === "adjacent" ? 3.6 : 4.4} />
                  <text className="fgs-lbl" x={right ? cx + 8 : cx - 8} y={cy} dy="0.35em" textAnchor={right ? "start" : "end"}>{m.label}</text>
                </g>
              );
            })}
            {undated.map((m, i) => {
              const gx = W - GW + 4;
              const cy = lt + 8 + i * RH + RH / 2;
              return (
                <g key={m.title} className={m.est ? "fgs-m is-est" : "fgs-m is-early"}>
                  <title>{m.title}</title>
                  <circle cx={gx} cy={cy} r={lane.key === "adjacent" ? 3.6 : 4.4} />
                  <text className="fgs-lbl" x={gx + 9} y={cy} dy="0.35em">{m.label}</text>
                </g>
              );
            })}
          </g>
        ))}
        {noYear && (
          <g>
            <line className="fgs-gut" x1={W - GW - 8} x2={W - GW - 8} y1={AXIS - 14} y2={H - 6} />
            <text className="fgs-gut-t" x={W - GW + 4} y={AXIS - 8}>year not published</text>
          </g>
        )}
      </svg>
      <p className="fgs-read">
        {mA !== null && <>Abroad, selling for a median of <b>{Math.round(mA)} years</b>. </>}
        {direct.length === 0
          ? <>Here, <b>nobody on file sells this</b>{adjacent.length ? `; ${adjacent.length} nearby sell something else` : ""}.</>
          : <>Here, the {direct.length === 1 ? "one player" : `${direct.length} players`} selling it {mD !== null ? <>have a median of <b>{Math.round(mD)} {Math.round(mD) === 1 ? "year" : "years"}</b></> : "publish no year"}{estHere ? `, ${estHere} established` : ", all early"}.</>}
        <span className="fgs-read-gap"> Local opportunity reads: “{scoreRead(p, "gap")}”.</span>
      </p>
    </div>
  );
}

/** Rail variant — who is in the room, as the gap rule sees it: does it sell
    THIS (competes) × how proven (maturity). The top-right cell is the one that
    takes the space; the others never move the gap score. */
export function RoomMatrix({ p }: { p: Problem }) {
  const locals = p.locals ?? [];
  const cell = (c: "direct" | "adjacent", m: "early" | "established") => locals.filter((l) => l.competes === c && l.maturity === m);
  const names = (xs: typeof locals) => {
    const s = xs.map((l) => shortName(l.name));
    return s.length > 3 ? `${s.slice(0, 3).join(", ")} +${s.length - 3}` : s.join(", ");
  };
  const rows: { c: "direct" | "adjacent"; k: string }[] = [
    { c: "direct", k: "Sells this" },
    { c: "adjacent", k: "Nearby" },
  ];
  return (
    <div className="fgm">
      <div className="fgm-grid">
        <span />
        <span className="fgm-ch">Early</span>
        <span className="fgm-ch">Established</span>
        {rows.map(({ c, k }) => (
          <div key={c} className="fgm-row">
            <span className="fgm-rh">{k}</span>
            {(["early", "established"] as const).map((m) => {
              const xs = cell(c, m);
              const key = c === "direct" && m === "established";
              return (
                <span key={m} className={`fgm-cell${key ? " is-key" : ""}${xs.length ? "" : " is-empty"}`}>
                  <b className="fgm-n">{xs.length}</b>
                  <span className="fgm-names">{xs.length ? names(xs) : "—"}</span>
                  {key && <span className="fgm-keyk">takes the space</span>}
                </span>
              );
            })}
          </div>
        ))}
      </div>
      <p className="fgm-read">{scoreRead(p, "gap")}.</p>
    </div>
  );
}
