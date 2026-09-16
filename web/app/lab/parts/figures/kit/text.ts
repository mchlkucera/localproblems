// /lab/parts/figures — tiny layout helpers for the build-time SVG figures.
// No DOM, no canvas: server components cannot measure text, so label widths
// are ESTIMATED from Inter's rough advance widths. The estimate only keeps
// labels from colliding; nothing is fitted to it exactly, so a 5% error costs
// a few pixels of air, never an overlap that matters.

/** Approximate advance width of a string set in Inter, in px. */
export function textW(s: string, size: number, weight = 400): number {
  let w = 0;
  for (const ch of s) {
    if (ch === " ") w += 0.27;
    else if ("il.,:;'|!·".includes(ch)) w += 0.27;
    else if ("fjrt()[]/-".includes(ch)) w += 0.36;
    else if ("mwMW€".includes(ch)) w += 0.84;
    else if (/[A-Z]/.test(ch)) w += 0.67;
    else if (/[0-9]/.test(ch)) w += 0.6;
    else w += 0.55;
  }
  return w * size * (weight >= 600 ? 1.05 : weight >= 500 ? 1.02 : 1);
}

/** Greedy interval packing: returns a row index per item, in input order.
    Items are placed left to right; each goes into the first row whose last
    occupant ends at least `gap` px before it starts. */
export function packRows(items: { a: number; b: number }[], gap = 8): number[] {
  const order = items.map((it, i) => ({ ...it, i })).sort((x, y) => x.a - y.a || x.b - y.b);
  const ends: number[] = [];
  const row = new Array<number>(items.length).fill(0);
  for (const it of order) {
    let r = ends.findIndex((e) => it.a >= e + gap);
    if (r === -1) { r = ends.length; ends.push(it.b); } else ends[r] = it.b;
    row[it.i] = r;
  }
  return row;
}

/** Drop the parenthetical product name: "STAPRO (AI asistent výkaznictví)" →
    "STAPRO". Cuts at the FIRST paren, because some nest: "ICZ (Asistent
    vykazování AV(D))". */
export const shortName = (s: string) => s.replace(/\s*\(.*$/, "").trim() || s;

/** ISO date → fractional year (2026-09-04 → 2026.68). */
export function yearFrac(iso: string): number {
  const [y, m, d] = iso.split("-").map(Number);
  const start = Date.UTC(y, 0, 1);
  const end = Date.UTC(y + 1, 0, 1);
  return y + (Date.UTC(y, m - 1, d) - start) / (end - start);
}

/** Compact CZK for axis ticks and labels: 3k · 91k · 9M · 2.5bn. */
export function czkShort(v: number): string {
  const f = (x: number) => (x >= 10 ? String(Math.round(x)) : String(Math.round(x * 10) / 10));
  if (v >= 1e9) return `${f(v / 1e9)}bn`;
  if (v >= 1e6) return `${f(v / 1e6)}M`;
  if (v >= 1e3) return `${f(v / 1e3)}k`;
  return String(Math.round(v));
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
/** `2026-12-17` → `17 Dec 2026`; `short` drops the year. */
export function dayLabel(iso: string, short = false): string {
  const [y, m, d] = iso.split("-").map(Number);
  return short ? `${d} ${MONTHS[m - 1]}` : `${d} ${MONTHS[m - 1]} ${y}`;
}
export const monthLabel = (iso: string) => {
  const [y, m] = iso.split("-").map(Number);
  return `${MONTHS[m - 1]} ${y}`;
};

export const median = (xs: number[]): number | null => {
  if (!xs.length) return null;
  const s = [...xs].sort((a, b) => a - b);
  const h = Math.floor(s.length / 2);
  return s.length % 2 ? s[h] : (s[h - 1] + s[h]) / 2;
};
