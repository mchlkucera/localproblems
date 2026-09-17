// lib/figures — tiny text helpers for the build-time figures: short company
// names, compact CZK and date labels.

/** Drop the parenthetical product name: "STAPRO (AI asistent výkaznictví)" →
    "STAPRO". Cuts at the FIRST paren, because some nest: "ICZ (Asistent
    vykazování AV(D))". */
export const shortName = (s: string) => s.replace(/\s*\(.*$/, "").trim() || s;

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
