// The source model behind the Perplexity-style citations.
// Server-only data shaping: every record source becomes one LabSource with the
// four things a peek has to answer — WHO published it (publisher + domain),
// WHAT it is (title + type), WHEN (date), and WHY it backs the claim (the
// record's own `why`, else its signal's summary) — plus the source's own words
// (`quote`) when the ingest captured them. Nothing here fetches anything: the
// "favicon" is a monogram derived from the publisher name.
import { getSignal, type Problem, type ProblemSource } from "../data";

export type LabSource = {
  /** 1-based S-number — the position in `p.sources`, what `[S3]` resolves to. */
  n: number;
  url: string | null;
  /** Bare host, `www.` stripped — the domain line of the peek. */
  host: string | null;
  /** Short human publisher name — the text of the inline pill. */
  publisher: string;
  /** One letter for the monogram chip. */
  mono: string;
  title: string;
  type: string;
  typeLabel: string;
  date: string;
  dateLabel: string;
  why: string | null;
  gist: string | null;
  /** Verbatim text from the source (signal `quote`) — the peek's snippet. */
  quote: string | null;
};

// The publishers this register cites most, by host. A pill that says "TED" or
// "Registr smluv" tells a reader more than "ted.europa.eu"; anything not listed
// falls back to its bare domain, which is always honest.
const PUBLISHERS: Record<string, string> = {
  "ted.europa.eu": "TED",
  "smlouvy.gov.cz": "Registr smluv",
  "hlidacstatu.cz": "Hlídač státu",
  "ycombinator.com": "Y Combinator",
  "eur-lex.europa.eu": "EUR-Lex",
  "vestbee.com": "Vestbee",
  "odok.cz": "VeKLEP",
  "odok.gov.cz": "VeKLEP",
  "data.mpsv.cz": "MPSV",
  "mpsv.gov.cz": "MPSV",
  "mpsv.cz": "MPSV",
  "e-sbirka.gov.cz": "e-Sbírka",
  "zakonyprolidi.cz": "Zákony pro lidi",
  "mpo.gov.cz": "MPO",
  "mzd.gov.cz": "MZd",
  "csu.gov.cz": "ČSÚ",
  "cnb.cz": "ČNB",
  "nukib.gov.cz": "NÚKIB",
  "irop.gov.cz": "IROP",
  "apiagentura.gov.cz": "API",
  "techfundingnews.com": "Tech Funding News",
  "tech.eu": "Tech.eu",
  "sme-union.cz": "SME Union",
  "cybersecurity-centre.europa.eu": "ECCC",
  "ec.europa.eu": "European Commission",
  "rowan.legal": "Rowan Legal",
  "mordorintelligence.com": "Mordor Intelligence",
  "uradprace.cz": "Úřad práce",
  "apss.cz": "APSS ČR",
  "apsscr.cz": "APSS ČR",
  "crunchbase.com": "Crunchbase",
  "ares.gov.cz": "ARES",
  "zdravotnickydenik.cz": "Zdravotnický deník",
  "eu-startups.com": "EU-Startups",
  "techcrunch.com": "TechCrunch",
};

const TYPE_LABELS: Record<string, string> = {
  regulation: "Regulation",
  tender: "Tender",
  tenders: "Tender",
  contract: "Contract",
  subsidy: "Subsidy",
  round: "Funding round",
  funded: "Funding round",
  statistic: "Statistic",
  complaint: "Complaint",
  "gap-check": "Market check",
  price: "Price",
  demand: "Demand",
  hiring: "Hiring",
  asks: "Stated need",
  report: "Report",
  news: "News",
  arbitrage: "Company abroad",
  ask: "Stated need",
};

/** What each KIND of source is, and why it counts — the Evidence tooltips.
    Grounded in data/CONVENTIONS.md ("Evidence types and their feeds" and the
    source type → scorecard dimension map: arbitrage→proof ·
    tender/contract/subsidy→money · regulation→urgency · complaint/news→demand
    · gap-check→gap) and SCORING.md (no source, no point). A kind the map does
    not tie to a dimension says what it backs, never a point it does not earn. */
const TYPE_NOTES: Record<string, string> = {
  arbitrage: "A company already selling this in another market. It is what Validated abroad reads.",
  round: "A funding round raised by a company doing this abroad: investors backing the model.",
  funded: "A funding round raised by a company doing this abroad: investors backing the model.",
  tender: "A public tender: a buyer asking the market to supply this, with a budget attached. It counts toward Money nearby.",
  tenders: "A public tender: a buyer asking the market to supply this, with a budget attached. It counts toward Money nearby.",
  contract: "A signed contract from the state contracts register: public money that has already moved. It counts toward Money nearby.",
  subsidy: "A grant or subsidy call that can pay for this work. It counts toward Money nearby.",
  regulation: "A law or rule with a date that forces buyers to act. It counts toward Why now.",
  complaint: "Documented pain: an association, audit, survey or complaint saying this hurts. It counts toward Demand signal.",
  news: "Reporting that documents the pain. It counts toward Demand signal.",
  demand: "Documented complaints and unmet needs. It counts toward Demand signal.",
  statistic: "A published figure — an official count, survey or market sizing — that sizes a claim in the text.",
  price: "A price receipt: what a named Czech buyer actually pays for this, or for doing it by hand. It answers who pays.",
  "gap-check": "The register's own search for Czech companies already selling this, run with a control that proves the search can find one. It is what Local opportunity reads.",
  hiring: "Employers posting paid vacancies for this work through the Labour Office — committing their own budget to the need.",
  ask: "A named institution stating this problem in public before money is attached.",
  asks: "A named institution stating this problem in public before money is attached.",
};

export function typeNote(t: string): string | null {
  return TYPE_NOTES[t] ?? null;
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

/** `2026-02-08` → `8 Feb 2026`. Manual, so it renders identically everywhere. */
export function fmtDate(iso: string): string {
  const [y, m, d] = iso.split("-").map(Number);
  if (!y || !m || !d) return iso;
  return `${d} ${MONTHS[m - 1]} ${y}`;
}

export function typeLabel(t: string): string {
  return TYPE_LABELS[t] ?? t.charAt(0).toUpperCase() + t.slice(1).replace(/-/g, " ");
}

function hostOf(url: string): string | null {
  if (!url.startsWith("http")) return null;
  try {
    return new URL(url).host.replace(/^www\./, "");
  } catch {
    return null;
  }
}

function publisherOf(host: string | null, fallback: string): string {
  if (!host) return fallback;
  if (PUBLISHERS[host]) return PUBLISHERS[host];
  // a subdomain of a listed publisher (e.g. `www2.mpsv.cz`) keeps its name
  const parent = Object.keys(PUBLISHERS).find((k) => host.endsWith(`.${k}`));
  return parent ? PUBLISHERS[parent] : host;
}

export function labSource(s: ProblemSource, i: number): LabSource {
  const sig = s.signal ? getSignal(s.signal) : undefined;
  const url = s.url.startsWith("http") ? s.url : null;
  const host = hostOf(s.url);
  const tl = typeLabel(s.type);
  // A market check is the register's own search; its url is one page the
  // search found, not the publisher of the finding — so it is credited as the
  // check, and the page it landed on stays visible as the domain line.
  const publisher = s.type === "gap-check" ? "Market check" : publisherOf(host, tl);
  const title = s.name ?? sig?.title ?? (s.type === "gap-check" ? "Market check" : `${tl}${host ? ` — ${host}` : ""}`);
  return {
    n: i + 1,
    url,
    host,
    publisher,
    mono: publisher.replace(/^[^\p{L}\p{N}]+/u, "").charAt(0).toUpperCase() || "·",
    title,
    type: s.type,
    typeLabel: tl,
    date: s.date,
    dateLabel: fmtDate(s.date),
    why: s.why ?? sig?.summary ?? null,
    gist: s.gist ?? null,
    quote: sig?.quote ?? null,
  };
}

export function labSources(p: Problem): LabSource[] {
  return p.sources.map(labSource);
}

/** Clip for the peek card — the full text lives in the ledger at the foot. */
export const clip = (s: string, n: number) =>
  s.length <= n ? s : `${s.slice(0, n - 1).replace(/\s+\S*$/, "").trimEnd()}…`;
