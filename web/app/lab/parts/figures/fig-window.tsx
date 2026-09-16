// Option F — the window: dated triggers against today.
// Only FUTURE dates are drawn, from rules (regulation) and money (subsidy,
// tender) — the same rule the lab page's "Dates on file" list uses. A future
// date on those types is almost always a deadline; a PAST date is not safe to
// read — it can be a law's start, a page's publication or the day the register
// read it (the audit found 77% of dates are ingest dates) — so past dates are
// listed under the figure, never plotted. Every date whose record and signal
// disagree is footnoted automatically, and a future date on any other type
// (p-0008's complaint) is refused and named.
import { extractDate, getSignal, type Problem } from "../../../../lib/data";
import { dayLabel, packRows, textW } from "./kit/text";

const W = 680;
const LW = 124;
const RH = 21;
const FS = 11;
const DAY = 86_400_000;
const ms = (iso: string) => Date.parse(`${iso}T00:00:00Z`);
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

type Item = { n: number; date: string; lane: 0 | 1; label: string; foot?: string };

export function windowItems(p: Problem) {
  const today = extractDate();
  const items: Item[] = [];
  const refused: string[] = [];
  const past: string[] = [];
  p.sources.forEach((s, i) => {
    const n = i + 1;
    const sig = s.signal ? getSignal(s.signal) : undefined;
    const fd = s.date > today ? s.date : sig && sig.date > today ? sig.date : null;
    const deadlineType = s.type === "regulation" || s.type === "subsidy" || s.type === "tender";
    if (!deadlineType) {
      if (fd) refused.push(`S${n} (${s.type}, ${dayLabel(fd)})`);
      return;
    }
    if (!fd) {
      if (s.type === "regulation") past.push(`S${n} ${dayLabel(s.date)}`);
      return;
    }
    const foot = sig && sig.date !== s.date
      ? `S${n}: ${dayLabel(s.date)} on the record, ${dayLabel(sig.date)} on its signal; drawn at ${dayLabel(fd)}`
      : undefined;
    items.push({ n, date: fd, lane: s.type === "regulation" ? 0 : 1, label: s.gist ?? s.name ?? s.type, foot });
  });
  return { today, items: items.sort((a, b) => a.date.localeCompare(b.date)), refused, past };
}

function out(from: string, to: string): string {
  const days = Math.round((ms(to) - ms(from)) / DAY);
  const months = Math.round(days / 30.44);
  if (months < 1) return `${Math.max(1, Math.round(days / 7))} weeks`;
  if (months < 18) return `${months} month${months === 1 ? "" : "s"}`;
  return `${Math.round((months / 12) * 10) / 10} years`;
}

export function WindowLine({ p }: { p: Problem }) {
  const { today, items, refused, past } = windowItems(p);
  const notes = (
    <>
      {items.some((it) => it.foot) && (
        <ul className="fgw-foot">
          {items.filter((it) => it.foot).map((it) => <li key={it.n}><span aria-hidden="true">†</span> {it.foot}</li>)}
        </ul>
      )}
      {(past.length > 0 || refused.length > 0) && (
        <p className="fgw-not">
          {past.length > 0 && <>Past rule dates not drawn (start, publication or read date; the record does not say which): {past.join(", ")}. </>}
          {refused.length > 0 && <>Refused: {refused.join(", ")}, a future date on a type that cannot carry a deadline.</>}
        </p>
      )}
    </>
  );
  if (items.length === 0) {
    return (
      <div className="fgw fge--empty">
        <p className="fge-empty-t">No dated trigger ahead</p>
        <p className="fge-empty-d">Nothing on file is dated after {dayLabel(today)} on a rule, grant or tender.</p>
        {notes}
      </div>
    );
  }

  const X0 = LW + 12;
  const X1 = W - 14;
  const first = items[0].date < today ? items[0].date : today;
  const last = items[items.length - 1].date;
  const spanD = (ms(last) - ms(first)) / DAY;
  const pad = Math.max(24, spanD * 0.06) * DAY;
  const t0 = ms(first) - pad;
  const t1 = ms(last) + pad;
  const x = (iso: string) => X0 + ((ms(iso) - t0) / (t1 - t0)) * (X1 - X0);
  const xm = (t: number) => X0 + ((t - t0) / (t1 - t0)) * (X1 - X0);

  // ticks: years for long windows, half-years for medium, months for short
  const ticks: { t: number; label: string; major: boolean }[] = [];
  const yA = new Date(t0).getUTCFullYear();
  const yB = new Date(t1).getUTCFullYear();
  const spanY = (t1 - t0) / (365.25 * DAY);
  for (let y = yA; y <= yB; y++) {
    for (let m = 0; m < 12; m++) {
      const t = Date.UTC(y, m, 1);
      if (t < t0 || t > t1) continue;
      if (spanY > 3 && m === 0) ticks.push({ t, label: String(y), major: true });
      else if (spanY > 1.2 && spanY <= 3 && (m === 0 || m === 6)) ticks.push({ t, label: m === 0 ? String(y) : "Jul", major: m === 0 });
      else if (spanY <= 1.2) ticks.push({ t, label: m === 0 ? `Jan ${y}` : MONTHS[m], major: m === 0 });
    }
  }

  const AXIS = 22;
  const tx = x(today);
  let top = AXIS + 12;
  const lanes = (["Rules", "Grants & tenders"] as const).map((k, li) => {
    const its = items.filter((it) => it.lane === li);
    const boxes = its.map((it) => {
      const cx = x(it.date);
      const text = `${it.label} · ${dayLabel(it.date)}${it.foot ? " †" : ""}`;
      const w = textW(text, FS, 500);
      const right = cx + 9 + w <= X1 + 6;
      return { it, cx, text, right, a: right ? cx - 6 : cx - 9 - w, b: right ? cx + 9 + w : cx + 6 };
    });
    const rows = packRows(boxes, 10);
    const h = Math.max(1, rows.length ? Math.max(...rows) + 1 : 1) * RH + 14;
    const res = { k, boxes, rows, top, h, empty: its.length === 0 };
    top += h;
    return res;
  });
  const H = top + 4;
  const next = items.find((it) => it.date > today)!;
  // the record page's own rule for its warm hue: a deadline under six months
  const soon = (ms(next.date) - ms(today)) / DAY < 183;

  return (
    <div className="fgw">
      <svg className="fgw-svg" viewBox={`0 0 ${W} ${H}`} width={W} height={H} role="img"
        aria-label={`Dated triggers after ${dayLabel(today)}: ${items.map((it) => `${it.label}, ${dayLabel(it.date)}`).join("; ")}`}>
        <line className="fgs-axis" x1={X0} x2={X1} y1={AXIS} y2={AXIS} />
        {ticks.map(({ t, label, major }) => (
          <g key={t}>
            <line className={major ? "fgs-grid is-major" : "fgs-grid"} x1={xm(t)} x2={xm(t)} y1={AXIS} y2={H - 4} />
            {Math.abs(xm(t) - tx) > 30 && <text className="fgs-tick" x={xm(t)} y={AXIS - 8}>{label}</text>}
          </g>
        ))}
        {/* the stretch from today to the first date, as a band */}
        <rect className={soon ? "fgw-run is-soon" : "fgw-run"} x={tx} y={AXIS - 2} width={Math.max(0, x(next.date) - tx)} height={4} rx={2} />
        <line className="fgs-today" x1={tx} x2={tx} y1={AXIS - 2} y2={H - 4} />
        <text className="fgs-today-t" x={tx} y={AXIS - 8}>today</text>
        {lanes.map((lane) => (
          <g key={lane.k}>
            <line className="fgs-sep" x1={0} x2={W} y1={lane.top} y2={lane.top} />
            <text className="fgs-lk" x={0} y={lane.top + 20}>{lane.k}</text>
            {lane.empty && <text className="fgs-none" x={X0} y={lane.top + 20}>Nothing dated ahead</text>}
            {lane.boxes.map(({ it, cx, text, right }, i) => {
              const cy = lane.top + 7 + lane.rows[i] * RH + RH / 2;
              return (
                <g key={it.n} className="fgw-m">
                  <title>{`S${it.n}: ${text}`}</title>
                  <line className="fgw-stem" x1={cx} x2={cx} y1={AXIS + 2} y2={cy} />
                  <circle cx={cx} cy={cy} r={4.4} />
                  <text className="fgs-lbl" x={right ? cx + 9 : cx - 9} y={cy} dy="0.35em" textAnchor={right ? "start" : "end"}>{text}</text>
                </g>
              );
            })}
          </g>
        ))}
      </svg>
      <p className="fgw-read">
        First date on file: <b>{dayLabel(next.date)}</b>, <span className={soon ? "fgw-soon" : undefined}>{out(today, next.date)} out</span> ({next.label}).
        {items.length > 1 && <> Last: {dayLabel(last)}, {out(today, last)} out.</>}
      </p>
      {notes}
    </div>
  );
}
