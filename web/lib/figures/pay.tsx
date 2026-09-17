// lib/figures — Willing to pay: a column chart and a dot timeline, no legend,
// no caption.
//
// THE QUESTION (owner, 2026-09-17): "are people willing to pay for this right
// now?" Public money only raises that willingness; it is not a sale.
//
// WHAT WAS WEIGHED
//   (a) what buyers already pay → PayDots, ON THE PAGE. It is the builder's
//       first question (how much does one buyer spend?) and the data carries
//       it: 11 live records draw two or more marks. Since 2026-09-17 (owner:
//       "could we choose another graph? maybe columns") it is a COLUMN chart:
//       one gray column per price or purchase, height on a log CZK scale, the
//       lowest to the left, a word or two under each ("Hospital", "Town").
//       Each unit is its own group behind a gap and a small group label ("Per
//       seat, monthly", "One purchase"), so a monthly fee never stands in a
//       row it could be added to. (The export keeps its old name so the page
//       needs no change.)
//   (b) buying over time, dots stacked per month → PayTimeline, IN THE SHEET.
//       It answers "right now" (a column of dots in the last months), and it
//       COUNTS purchases, so a tender with no stated value still counts and no
//       money is summed. Open grant calls sit in one last column after the
//       months: they close in the future, and they raise willingness without
//       being a purchase. 9 live records draw it.
//   (c) who is buying, COUNTED by buyer type: rejected. Buyers are free text,
//       so a count per kind would be a regex guess drawn as data. The column
//       labels in (a) use the same words only as a reading aid under ONE
//       purchase each; a purchase that names no kind falls back to what it is
//       ("Tender", "List price"), never a guess.
//   (d) the grant pot as a lower cost: rejected as a graph. The support rate
//       lives only in prose (`why`), so a drawn "50%" would be parsed, not
//       recorded. The grant's own card shows the sentence instead.
//
// WHAT COUNTS AS WHAT (one field, one meaning: the source's `type` decides)
//   price receipt   priceReceipts(p): payer, amount_czk, unit, basis
//   purchase        type contract | tender | tenders, amount from the linked
//                   signal's money_eur (0 = none stated), at a flat 25 CZK/EUR
//                   for the axis only; the card prints the euro figure
//   open grant      type subsidy whose signal is a `dotace-` call (the
//                   dotace-scan prefix; money.tsx's rule) and whose date (the
//                   closing date) is on or after extractDate(). A `subsidy`
//                   without such a signal is ambiguous (a paid application, a
//                   programme page) and is drawn in neither figure.
//   SAME URL = SAME MONEY: a purchase whose url is a price receipt's url is the
//   receipt, drawn once, as the price.
//
// INTERACTION: every dot is a native `<button popovertarget>` with `data-peek`
// (PeekHover's selector: hover-intent, grace, click-to-pin) opening a
// `popover="auto"` card with the `ls-peek` classes (anchor placement, bottom
// sheet on a phone). Without JS a click, tap or Enter opens it. Every fact on a
// card is also in the sheet's rows, so nothing is hover-only.
//
// Both return `null` when the data is thin. `scope` keeps popover ids unique if
// a figure is rendered twice on one page.
import type { CSSProperties, ReactNode } from "react";
import { extractDate, getSignal, priceReceipts, type PriceUnit, type Problem } from "../data";
import { PRICE_BASIS_LABELS, PRICE_UNIT_LABELS, czk, euro } from "../format";
import { EXT, ExtArrow } from "../site/cite";
import { clip, labSource } from "../site/sources";
import { czkShort, dayLabel, monthLabel } from "./text";

const RATE = 25;
const PURCHASE = new Set(["contract", "tender", "tenders"]);
const KIND: Record<string, string> = { contract: "Signed contract", tender: "Tender", tenders: "Tender" };

type Lane = Exclude<PriceUnit, "one-off"> | "purchase";
const LANES: Lane[] = ["per-hour", "per-case", "per-seat-month", "per-year", "per-project", "purchase"];
const LANE_NAME: Record<Lane, string> = {
  "per-hour": "Per hour",
  "per-case": "Per case",
  "per-seat-month": "Per seat, monthly",
  "per-year": "Per year",
  "per-project": "Per project",
  purchase: "One purchase",
};

type Mark = {
  n: number;
  lane: Lane;
  czk: number | null;
  /** the card's big figure: "91 000 CZK", "€6.1M" */
  amount: string;
  /** after the figure: "one-off", "about 153M CZK" */
  unit: string;
  /** the card's foot: "Signed contract · Registr smluv · Jun 2026" */
  meta: string;
  title: string;
  href: string | null;
  line: string;
  date: string;
  label: string;
  /** the column label: a buyer kind read from the payer or title, else what
      the mark is ("Tender", "List price") */
  who: string;
  /** a real purchase: a contract, a tender, or a receipt taken from one (the
      timeline counts these) */
  buy: boolean;
};

function marks(p: Problem): { paid: Mark[]; grants: Mark[] } {
  const prices = priceReceipts(p);
  const priceUrls = new Set(prices.map(({ s }) => s.url));
  const buyUrls = new Set(p.sources.filter((s) => PURCHASE.has(s.type)).map((s) => s.url));
  const seen = new Set<string>();
  const paid: Mark[] = prices.map(({ n, s }) => {
    const ls = labSource(s, n - 1);
    const lane: Lane = s.unit === "one-off" ? "purchase" : s.unit;
    const unit = PRICE_UNIT_LABELS[s.unit];
    return {
      n, lane, czk: s.amount_czk, amount: czk(s.amount_czk), unit,
      meta: [cap(PRICE_BASIS_LABELS[s.basis]), ls.publisher, monthLabel(s.date)].join(" · "),
      title: ls.title, href: ls.url,
      line: `Paid by ${lower(s.payer)}.`,
      date: s.date,
      label: `${czk(s.amount_czk)} ${unit}, paid by ${s.payer}, ${monthLabel(s.date)}`,
      who: kindOf([s.payer]) ?? cap(PRICE_BASIS_LABELS[s.basis]),
      // a receipt lifted from a contract or tender line is that purchase
      buy: buyUrls.has(s.url) || s.basis === "signed-contract" || s.basis === "tender-line",
    };
  });
  const grants: Mark[] = [];
  const from = extractDate();
  p.sources.forEach((s, i) => {
    const n = i + 1;
    const sig = s.signal ? getSignal(s.signal) : undefined;
    const eur = sig?.money_eur ? sig.money_eur : null;
    const ls = labSource(s, i);
    const line = clip(ls.why ?? ls.gist ?? "", 240);
    if (PURCHASE.has(s.type)) {
      if (priceUrls.has(s.url) || seen.has(s.url)) return;
      seen.add(s.url);
      const kind = KIND[s.type];
      paid.push({
        n, lane: "purchase", czk: eur ? eur * RATE : null,
        amount: eur ? euro(eur) : "No amount stated", unit: eur ? `about ${czkShort(eur * RATE)} CZK` : "",
        meta: [kind, ls.publisher, monthLabel(s.date)].join(" · "),
        title: ls.title, href: ls.url, line, date: s.date,
        label: `${kind}${eur ? `, ${euro(eur)}` : ", no amount stated"}, ${monthLabel(s.date)}: ${ls.title}`,
        who: kindOf([ls.title, line]) ?? (s.type === "contract" ? "Contract" : "Tender"),
        buy: true,
      });
    } else if (s.type === "subsidy" && sig?.id.startsWith("dotace-") && s.date >= from) {
      grants.push({
        n, lane: "purchase", czk: eur ? eur * RATE : null,
        amount: eur ? euro(eur) : "Grant call", unit: eur ? "grant pot" : "",
        meta: ["Grant call", ls.publisher, `closes ${dayLabel(s.date)}`].join(" · "),
        title: ls.title, href: ls.url, line, date: s.date,
        label: `Open grant call${eur ? `, ${euro(eur)}` : ""}, closes ${dayLabel(s.date)}: ${ls.title}`,
        who: "Grant call",
        buy: false,
      });
    }
  });
  return { paid, grants };
}

/** One or two words for the buyer, read from the payer or the title first (a
    `why` often mentions OTHER buyers, so it is only the fallback). First match
    wins; the order puts the narrower kind first ("Domov pro seniory" is a care
    home before it is anything in a town). */
const KINDS: [string, RegExp][] = [
  ["Care home", /care home|domov\b|domov pro|senior|disability|social[- ]care|sociáln/i],
  ["Hospital", /hospital|nemocnic|\bFN\b|Motol|Homolka|clinic|klinik/i],
  ["University", /universit|univerzit/i],
  ["School", /\bschool|škol/i],
  ["Utility", /ČEZ|utilit|distribuc|vodárn|water compan|teplárn/i],
  ["Broadcaster", /televi|rozhlas|radio/i],
  ["Region", /\bregion\b|\bkraj\b|krajsk/i],
  ["Town", /\bměst|\bmesto|\btown|\bcity\b|\bobec|municipal|district|Praha|Prague/i],
  ["State body", /agency|ministr|institut|ústav|authority|úřad|NAKIT|\bstate\b|national/i],
  ["Company", /compan|firm|business|\bSME|e-?shop|installer|s\.r\.o|a\.s\./i],
];
function kindOf(texts: string[]): string | null {
  for (const t of texts) {
    const k = KINDS.find(([, re]) => re.test(t));
    if (k) return k[0];
  }
  return null;
}

const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);
/** "Město Český Brod, a town …" stays; "An obligated Czech company" → "an …" */
const lower = (s: string) => (/^(?:A|An|The|One|Each|Every)\s/.test(s) ? s.charAt(0).toLowerCase() + s.slice(1) : s);

function Dot({ id, m, cls = "lk-pay-dot", style }: { id: string; m: Mark; cls?: string; style?: CSSProperties }): ReactNode {
  const anchor = `--${id}`;
  return (
    <>
      <button
        type="button"
        className={cls}
        popoverTarget={id}
        aria-label={m.label}
        data-peek=""
        style={{ ...style, anchorName: anchor } as CSSProperties}
      />
      <div id={id} popover="auto" role="dialog" aria-label={m.title} className="ls-peek lk-pay-pk" style={{ positionAnchor: anchor } as CSSProperties}>
        <span className="ls-pk-entry">
          <span className="lk-pay-amt">
            {m.amount}
            {m.unit && <span className="lk-pay-unit"> {m.unit}</span>}
          </span>
          {m.line && <span className="ls-pk-why">{m.line}</span>}
          {m.href
            ? <a className="ls-pk-title" href={m.href} {...EXT}>{m.title}<ExtArrow /></a>
            : <span className="ls-pk-title">{m.title}</span>}
          <span className="ls-pk-foot"><span className="ls-pk-meta">{m.meta}</span></span>
        </span>
      </div>
    </>
  );
}

/** What buyers already pay: one gray column per price or purchase with an
    amount, height on a log CZK scale, lowest first, one group per unit.
    `null` under two columns. */
export function PayDots({ p, scope = "" }: { p: Problem; scope?: string }): ReactNode {
  const bars = marks(p).paid.filter((m): m is Mark & { czk: number } => !!m.czk && m.czk > 0);
  if (bars.length < 2) return null;

  const logs = bars.map((d) => Math.log10(d.czk));
  // the floor sits a little under the smallest amount, so no column is flat
  const lo = Math.floor(Math.min(...logs) - 0.3);
  // the top sits just over the largest amount, so the tallest column fills the plot
  const hi = Math.max(Math.max(...logs) + 0.12, lo + 2);
  const f = (v: number) => (Math.log10(v) - lo) / (hi - lo);
  // two or three labelled gridlines, counted down from the highest decade inside
  const step = Math.max(1, Math.ceil((hi - lo) / 3));
  const lines: number[] = [];
  for (let d = Math.floor(hi); d > lo && lines.length < 3; d -= step) lines.push(d);

  const groups = LANES.map((lane) => ({
    lane,
    items: bars.filter((d) => d.lane === lane).sort((a, b) => a.czk - b.czk),
  })).filter((g) => g.items.length > 0);

  return (
    <figure
      className={`lk lk-pay lk-payc${bars.length > 8 ? " is-many" : ""}${bars.length > 16 ? " is-dense" : ""}`}
      aria-label="What buyers already pay: one column per price or purchase, in CZK on a log scale"
    >
      <div className="lk-payc-grid" aria-hidden="true">
        {lines.map((d) => (
          <span key={d} className="lk-payc-line" style={{ "--f": f(10 ** d) } as CSSProperties}>
            <span className="lk-payc-tick">{czkShort(10 ** d)}{d === lines[0] ? " CZK" : ""}</span>
          </span>
        ))}
      </div>
      <div className="lk-payc-groups">
        {groups.map(({ lane, items }) => (
          <div key={lane} className={`lk-payc-group${lane === "purchase" ? "" : " is-unit"}`} style={{ "--k": items.length } as CSSProperties}>
            {items.map((d) => (
              <div key={d.n} className="lk-payc-slot">
                <Dot id={`lk-pay${scope}-d${d.n}`} m={d} cls="lk-payc-col" style={{ "--f": f(d.czk) } as CSSProperties} />
                <span className="lk-payc-who" aria-hidden="true">{d.who}</span>
              </div>
            ))}
            <p className="lk-payc-gl">{LANE_NAME[lane]}</p>
          </div>
        ))}
      </div>
    </figure>
  );
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

/** Buying over time: one dot per contract, tender or signed receipt, stacked in its
    month (quarter, past 15 months), from the first purchase to the extract
    date; open grant calls in one column after. `null` under three dated
    purchases or when they all fall in one column. */
export function PayTimeline({ p, scope = "" }: { p: Problem; scope?: string }): ReactNode {
  const { paid, grants } = marks(p);
  const buys = paid.filter((m) => m.buy && /^\d{4}-\d{2}/.test(m.date));
  if (buys.length < 3) return null;

  const idx = (iso: string) => { const [y, mo] = iso.split("-").map(Number); return y * 12 + mo - 1; };
  const first = Math.min(...buys.map((b) => idx(b.date)));
  const last = Math.max(idx(extractDate()), ...buys.map((b) => idx(b.date)));
  const q = last - first + 1 > 15 ? 3 : 1;
  const start = first - (first % q);
  const n = Math.floor((last - start) / q) + 1;
  const cols = Array.from({ length: n }, (_, i) => {
    const m0 = start + i * q;
    const y = Math.floor(m0 / 12), mo = m0 % 12;
    const name = q === 3 ? `Q${mo / 3 + 1}` : MONTHS[mo];
    const showYear = i === 0 || mo < q;
    return { key: m0, name, year: showYear ? String(y) : "", items: [] as Mark[] };
  });
  for (const b of buys) cols[Math.floor((idx(b.date) - start) / q)].items.push(b);
  if (cols.filter((c) => c.items.length).length < 2) return null;
  const tall = Math.max(...cols.map((c) => c.items.length), grants.length);

  return (
    <figure className="lk lk-pay lk-payt" aria-label={`Public contracts and tenders by ${q === 3 ? "quarter" : "month"}${grants.length ? ", then open grant calls" : ""}`}>
      <div className="lk-payt-cols" style={{ "--n": n, "--tall": tall } as CSSProperties}>
        {cols.map((c) => (
          <div key={c.key} className="lk-payt-col">
            <div className="lk-payt-stack">
              {[...c.items].sort((a, b) => a.date.localeCompare(b.date)).map((m) => <Dot key={m.n} id={`lk-payt${scope}-t${m.n}`} m={m} />)}
            </div>
            <p className="lk-payt-m">{c.name}{c.year && <span className="lk-payt-y">{c.year}</span>}</p>
          </div>
        ))}
        {grants.length > 0 && (
          <div className="lk-payt-col lk-payt-grants">
            <div className="lk-payt-stack">
              {grants.map((m) => <Dot key={m.n} id={`lk-payt${scope}-g${m.n}`} m={m} />)}
            </div>
            <p className="lk-payt-m">Grants open</p>
          </div>
        )}
      </div>
    </figure>
  );
}
