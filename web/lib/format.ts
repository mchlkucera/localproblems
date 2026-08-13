// House data formatting (design-language: data always looks like evidence).

/** Compact euro figure: €41k / €1.3M / €78M. Null → em dash. */
export function euro(v: number | null): string {
  if (v == null) return "—";
  if (v >= 1_000_000) {
    const m = v / 1_000_000;
    return `€${m >= 10 ? Math.round(m) : Math.round(m * 10) / 10}M`;
  }
  if (v >= 1_000) return `€${Math.round(v / 1_000)}k`;
  return `€${v}`;
}

/** Zero-padding is the house tic. */
export const pad2 = (n: number) => String(n).padStart(2, "0");

/** ISO-8601 week number of an ISO date string. */
export function isoWeek(date: string): number {
  const d = new Date(`${date}T00:00:00Z`);
  const day = d.getUTCDay() || 7;
  d.setUTCDate(d.getUTCDate() + 4 - day);
  const yearStart = Date.UTC(d.getUTCFullYear(), 0, 1);
  return Math.ceil(((d.getTime() - yearStart) / 86_400_000 + 1) / 7);
}

const CATEGORY_LABELS: Record<string, string> = {
  "b2b": "B2B",
  "legal-compliance": "Legal",
  "retail-services": "Retail",
  "govtech": "Govtech",
  "fintech": "Fintech",
};
export function categoryLabel(category: string): string {
  return CATEGORY_LABELS[category] ?? category.charAt(0).toUpperCase() + category.slice(1);
}

/** Register locality display. Unknown codes render as recorded (mono truth). */
export function localityLabel(geo: string): string {
  if (geo === "CZ-national") return "Czechia";
  if (geo === "EU") return "EU";
  return geo;
}
export function localityLong(geo: string): string {
  if (geo === "CZ-national") return "Czechia · national";
  return geo;
}
