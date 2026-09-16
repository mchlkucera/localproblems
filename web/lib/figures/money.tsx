// lib/figures — the money on one scale. Article column, 680px.
//
// Lane 1: what ONE buyer pays (price receipts, CZK as recorded, each with its
// own unit — never normalised, never summed). Lane 2: public money nearby
// (the non-price sources backing Money nearby that carry an amount on their
// signal), converted at a flat 25 CZK/EUR. A grant POT is drawn hollow: it is
// shared by many buyers and is not one sale. Log axis: the point is the spread
// in orders of magnitude, not the gap between two dots.
//
// SAME-URL DEDUPE. A price receipt is often lifted from a contract already on
// the ledger (p-0008 S23 is S7's contract, S24 is S6's; p-0033 S12 is S4's
// data): same url, same money. It is drawn ONCE, as the price.
//
// `null` below two marks: a single dot is not a chart.
import type { ReactNode } from "react";
import { getSignal, priceReceipts, type Problem } from "../data";
import { euro } from "../format";
import { dimRefs } from "../scorecard";
import { typeLabel } from "../site/sources";
import { czkShort, packRows, textW } from "./text";

const RATE = 25;
const W = 680;
const LW = 124;
const RH = 21;
const FS = 11;

type Dot = { n: number; v: number; label: string; title: string; kind: "price" | "award" | "pot" };

export function moneyDots(p: Problem) {
  const prices = priceReceipts(p);
  const priceUrls = new Map(prices.map(({ n, s }) => [s.url, n]));
  const pay: Dot[] = prices.map(({ n, s }) => ({
    n, v: s.amount_czk, kind: "price",
    label: s.gist ?? `${czkShort(s.amount_czk)} CZK`,
    title: `S${n}: ${s.amount_czk.toLocaleString("en")} CZK, ${s.unit}, ${s.payer}`,
  }));
  const pub: Dot[] = [];
  const merged: { money: number; price: number }[] = [];
  const noAmount: number[] = [];
  for (const n of dimRefs(p).money) {
    const s = p.sources[n - 1];
    if (s.type === "price") continue;
    const sig = s.signal ? getSignal(s.signal) : undefined;
    if (!sig?.money_eur) { noAmount.push(n); continue; }
    const same = priceUrls.get(s.url);
    if (same) { merged.push({ money: n, price: same }); continue; }
    pub.push({
      // A grant CALL is a `dotace-` signal (the dotace-scan prefix). Its
      // `source` reads "hlidac" — the mirror it came through — so the id
      // prefix is the only field that says "pot".
      n, v: sig.money_eur * RATE, kind: sig.id.startsWith("dotace-") ? "pot" : "award",
      label: s.gist ?? `${euro(sig.money_eur)} ${typeLabel(s.type).toLowerCase()}`,
      title: `S${n}: ${euro(sig.money_eur)} (≈${czkShort(sig.money_eur * RATE)} CZK), ${s.name ?? sig.title}`,
    });
  }
  return { pay, pub, merged, noAmount };
}

export function MoneyScale({ p }: { p: Problem }): ReactNode {
  const { pay, pub, merged, noAmount } = moneyDots(p);
  const all = [...pay, ...pub];
  if (all.length < 2) return null;

  const X0 = LW + 12;
  const X1 = W - 14;
  const lo = Math.floor(Math.log10(Math.min(...all.map((d) => d.v))));
  let hi = Math.ceil(Math.log10(Math.max(...all.map((d) => d.v))));
  if (hi - lo < 3) hi = lo + 3;
  const x = (v: number) => X0 + ((Math.log10(v) - lo) / (hi - lo)) * (X1 - X0);
  const AXIS = 22;
  let top = AXIS + 12;
  const lanes = [
    { k: "One buyer pays", sub: pay.length ? `${pay.length} price receipt${pay.length === 1 ? "" : "s"}` : "no price on file", dots: pay },
    { k: "Public money nearby", sub: pub.length ? `${pub.length} with an amount` : "none with an amount", dots: pub },
  ].map((lane) => {
    const boxes = lane.dots.map((d) => {
      const cx = x(d.v);
      const w = textW(`S${d.n}  ${d.label}`, FS, 500);
      const right = cx + 9 + w <= X1 + 6;
      return { d, cx, right, a: right ? cx - 6 : cx - 9 - w, b: right ? cx + 9 + w : cx + 6 };
    });
    const rows = packRows(boxes, 10);
    const h = Math.max(46, Math.max(1, rows.length ? Math.max(...rows) + 1 : 1) * RH + 14);
    const out = { ...lane, boxes, rows, top };
    top += h;
    return out;
  });
  const H = top + 4;
  const decades = Array.from({ length: hi - lo + 1 }, (_, i) => lo + i);

  return (
    <figure className="lk lk-fig lk-money">
      <div className="lk-scroll">
        <svg className="lk-svg" viewBox={`0 0 ${W} ${H}`} width={W} height={H} role="img"
          aria-label={`Money on a log scale in CZK. ${all.map((d) => d.title).join("; ")}`}>
          <line className="lk-axis" x1={X0} x2={X1} y1={AXIS} y2={AXIS} />
          {decades.map((d) => (
            <g key={d}>
              <line className="lk-grid" x1={x(10 ** d)} x2={x(10 ** d)} y1={AXIS} y2={H - 4} />
              <text className="lk-tick" x={x(10 ** d)} y={AXIS - 8}>{czkShort(10 ** d)}</text>
            </g>
          ))}
          <text className="lk-tick lk-tick--unit" x={0} y={AXIS - 8} style={{ textAnchor: "start" }}>CZK, log scale</text>
          {lanes.map((lane) => (
            <g key={lane.k}>
              <line className="lk-sep" x1={0} x2={W} y1={lane.top} y2={lane.top} />
              <text className="lk-lk" x={0} y={lane.top + 20}>{lane.k}</text>
              <text className="lk-ls" x={0} y={lane.top + 35}>{lane.sub}</text>
              {lane.boxes.map(({ d, cx, right }, i) => {
                const cy = lane.top + 7 + lane.rows[i] * RH + RH / 2;
                return (
                  <g key={d.n} className={`lk-dot lk-dot--${d.kind}`}>
                    <title>{d.title}</title>
                    {d.kind === "pot"
                      ? <rect x={cx - 4.5} y={cy - 4.5} width={9} height={9} rx={1.5} />
                      : <circle cx={cx} cy={cy} r={d.kind === "price" ? 5 : 4.2} />}
                    <text className="lk-lbl" x={right ? cx + 9 : cx - 9} y={cy} dy="0.35em" style={{ textAnchor: right ? "start" : "end" }}>
                      <tspan className="lk-sn">S{d.n}</tspan>{"  "}{d.label}
                    </text>
                  </g>
                );
              })}
            </g>
          ))}
        </svg>
      </div>
      <p className="lk-key2">
        <span className="lk-k lk-k--price" /> one buyer’s price, in its own unit
        <span className="lk-k lk-k--award" /> a public award or contract
        <span className="lk-k lk-k--pot" /> a grant pot, shared by many buyers
      </p>
      <figcaption className="lk-cap">
        Euro amounts converted at 25 CZK. Units differ and are never added up: a month, a one-off, a year, a pot.
        {merged.length > 0 && <> Drawn once: {merged.map((m) => `S${m.money} is the same document as price S${m.price}`).join("; ")}.</>}
        {noAmount.length > 0 && <> Not drawn: {noAmount.map((n) => `S${n}`).join(", ")}, which back{noAmount.length === 1 ? "s" : ""} Money nearby with no amount on file.</>}
      </figcaption>
    </figure>
  );
}
