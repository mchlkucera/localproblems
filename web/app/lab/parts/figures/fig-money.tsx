// Option E — the money on one scale.
// Lane 1: what ONE buyer pays (price receipts, CZK as recorded, each with its
// own unit — never normalised, never summed). Lane 2: public money nearby
// (the sources backing Money nearby that carry an amount on their signal),
// converted at a flat 25 CZK/EUR. A grant POT (a `dotace` signal) is drawn
// hollow: it is shared by many buyers and is not one sale. A price receipt
// drawn from the same contract as a money source (same url) is drawn ONCE —
// otherwise the same money would appear twice, a real trap on p-0008 and
// p-0033. The axis is logarithmic: the point is the spread in orders of
// magnitude, not the distance between two dots.
import { getSignal, priceReceipts, type Problem } from "../../../../lib/data";
import { euro } from "../../../../lib/format";
import { dimRefs } from "../../../../lib/scorecard";
import { typeLabel } from "../../modern/sources";
import { czkShort, packRows, textW } from "./kit/text";

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
      // `source` field reads "hlidac", the mirror it was fetched through, so
      // the id prefix is the only field that says "pot" — noted for the owner.
      n, v: sig.money_eur * RATE, kind: sig.id.startsWith("dotace-") ? "pot" : "award",
      label: s.gist ?? `${euro(sig.money_eur)} ${typeLabel(s.type).toLowerCase()}`,
      title: `S${n}: ${euro(sig.money_eur)} (≈${czkShort(sig.money_eur * RATE)} CZK), ${s.name ?? sig.title}`,
    });
  }
  return { pay, pub, merged, noAmount };
}

export function MoneyScale({ p }: { p: Problem }) {
  const { pay, pub, merged, noAmount } = moneyDots(p);
  const all = [...pay, ...pub];
  if (all.length === 0) {
    return (
      <div className="fge fge--empty">
        <p className="fge-empty-t">No figure to draw</p>
        <p className="fge-empty-d">
          No price receipt is on file, and {noAmount.length
            ? <>the {noAmount.length === 1 ? "source" : `${noAmount.length} sources`} backing Money nearby ({noAmount.map((n) => `S${n}`).join(", ")}) {noAmount.length === 1 ? "carries" : "carry"} no amount the figure can read, though the prose may state one.</>
            : "no source backs Money nearby."}
          {p.price_search && <> The record says where to look instead.</>}
        </p>
      </div>
    );
  }
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
      const text = `S${d.n}  ${d.label}`;
      const w = textW(text, FS, 500);
      const right = cx + 9 + w <= X1 + 6;
      return { d, cx, right, text, a: right ? cx - 6 : cx - 9 - w, b: right ? cx + 9 + w : cx + 6 };
    });
    const rows = packRows(boxes, 10);
    const nRows = Math.max(1, rows.length ? Math.max(...rows) + 1 : 1);
    const h = Math.max(46, nRows * RH + 14);
    const out = { ...lane, boxes, rows, top, h };
    top += h;
    return out;
  });
  const H = top + 4;
  const decades = Array.from({ length: hi - lo + 1 }, (_, i) => lo + i);

  return (
    <div className="fge">
      <svg className="fge-svg" viewBox={`0 0 ${W} ${H}`} width={W} height={H} role="img"
        aria-label={`Money on a log scale in CZK. ${all.map((d) => d.title).join("; ")}`}>
        <line className="fgs-axis" x1={X0} x2={X1} y1={AXIS} y2={AXIS} />
        {decades.map((d) => (
          <g key={d}>
            <line className="fgs-grid" x1={x(10 ** d)} x2={x(10 ** d)} y1={AXIS} y2={H - 4} />
            <text className="fgs-tick" x={x(10 ** d)} y={AXIS - 8}>{czkShort(10 ** d)}</text>
          </g>
        ))}
        <text className="fgs-tick fgs-tick--unit" x={0} y={AXIS - 8} textAnchor="start">CZK, log scale</text>
        {lanes.map((lane) => (
          <g key={lane.k}>
            <line className="fgs-sep" x1={0} x2={W} y1={lane.top} y2={lane.top} />
            <text className="fgs-lk" x={0} y={lane.top + 20}>{lane.k}</text>
            <text className="fgs-ls" x={0} y={lane.top + 35}>{lane.sub}</text>
            {lane.boxes.map(({ d, cx, right }, i) => {
              const cy = lane.top + 7 + lane.rows[i] * RH + RH / 2;
              return (
                <g key={d.n} className={`fge-m fge-m--${d.kind}`}>
                  <title>{d.title}</title>
                  {d.kind === "pot"
                    ? <rect x={cx - 4.5} y={cy - 4.5} width={9} height={9} rx={1.5} />
                    : <circle cx={cx} cy={cy} r={d.kind === "price" ? 5 : 4.2} />}
                  <text className="fgs-lbl" x={right ? cx + 9 : cx - 9} y={cy} dy="0.35em" textAnchor={right ? "start" : "end"}>
                    <tspan className="fge-sn">S{d.n}</tspan>{"  "}{d.label}
                  </text>
                </g>
              );
            })}
          </g>
        ))}
      </svg>
      <p className="fge-key">
        <span className="fge-k fge-k--price" /> one buyer’s price, its own unit
        <span className="fge-k fge-k--award" /> a public award or contract
        <span className="fge-k fge-k--pot" /> a grant pot, shared by many buyers
        <span className="fge-k-note">€ converted at 25 CZK.</span>
      </p>
      {(merged.length > 0 || noAmount.length > 0) && (
        <p className="fge-foot">
          {merged.length > 0 && <>Drawn once: {merged.map((m) => `S${m.money} is the same document as price S${m.price}`).join("; ")}. </>}
          {noAmount.length > 0 && <>Not drawn: {noAmount.map((n) => `S${n}`).join(", ")} back{noAmount.length === 1 ? "s" : ""} Money nearby with no amount on {noAmount.length === 1 ? "its" : "their"} signal.</>}
        </p>
      )}
    </div>
  );
}
