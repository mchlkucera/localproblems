// House data formatting (design-language: data always looks like evidence).
import type { GapChecked } from "./data";

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

/** Full country names for ledger prose positions — the comps ledger renders
    "Switzerland · since 2020", never bare ISO2 (owner, 2026-08-19). Covers
    every code present in the data (comps geo + signal geo_origin); fallback =
    the raw code as recorded. The geomap's small ISO2 labels stay ISO2. */
const COUNTRY_NAMES: Record<string, string> = {
  AE: "United Arab Emirates", AM: "Armenia", AR: "Argentina", AT: "Austria",
  AU: "Australia", BE: "Belgium", BG: "Bulgaria", BR: "Brazil", CA: "Canada",
  CH: "Switzerland", CO: "Colombia", CR: "Costa Rica", CZ: "Czechia",
  DE: "Germany", DK: "Denmark", EE: "Estonia", ES: "Spain", FI: "Finland",
  FR: "France", GB: "United Kingdom", GR: "Greece", HK: "Hong Kong",
  HR: "Croatia", HU: "Hungary", IE: "Ireland", IL: "Israel", IN: "India",
  IS: "Iceland", IT: "Italy", KE: "Kenya", KR: "South Korea",
  KY: "Cayman Islands", LT: "Lithuania", LU: "Luxembourg", LV: "Latvia",
  MD: "Moldova", MK: "North Macedonia", MX: "Mexico", NG: "Nigeria",
  NL: "Netherlands", NO: "Norway", PL: "Poland", PT: "Portugal",
  RO: "Romania", RS: "Serbia", SE: "Sweden", SG: "Singapore",
  SI: "Slovenia", SK: "Slovakia", TR: "Turkey", UA: "Ukraine",
  US: "United States",
};
export function countryName(iso: string): string {
  return COUNTRY_NAMES[iso] ?? iso;
}

/** The surfaces a gap-check actually searched, in English. THE ONE MAPPING:
    `checked` is a closed enum of slugs (data.ts GAP_CHECKED, vocabulary in
    data/CONVENTIONS.md) and slugs are storage, not display — a reader is owed
    "ARES business register", never `ares`. Record<GapChecked, string> makes a
    new token a TypeScript error here rather than a raw slug on the page.
    `gapSurface` still falls back to the code as recorded, the same way
    `countryName` does: mono truth beats a blank. */
export const GAP_SURFACES: Record<GapChecked, string> = {
  "ares": "ARES business register",
  "app-stores": "App stores",
  "cz-saas-directories": "CZ SaaS directories",
  "google-cz": "Czech-language web search",
  "startupjobs": "StartupJobs.cz",
  "own-funded-ledger": "Our funded-company ledger",
  "eshop-addon-marketplaces": "CZ e-shop add-on marketplaces",
};
export function gapSurface(token: string): string {
  return GAP_SURFACES[token as GapChecked] ?? token;
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
