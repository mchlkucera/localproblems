// Option D — where it already works.
// D1 reuses the production choropleth (web/lib/geomap.tsx) untouched, restyled
// in lab grays by figures.css: HQ and sourced markets fill gray, Czechia is
// outlined in the "here" blue. D2 is the modern alternative: not WHERE on a
// map, but HOW CLOSE the proof is, in the three bands the PROOF ladder itself
// uses — SCORING.md rung 3 needs one market "CEE-adjacent
// (DE/AT/PL/Nordics/Baltics/SI/SK/HU)". Nothing is authored for either.
import type { Problem } from "../../../../lib/data";
import { countryName } from "../../../../lib/format";
import { EuropeMap } from "../../../../lib/geomap";
import { shortName } from "./kit/text";

/** SCORING.md, PROOF rung 3, verbatim: DE/AT/PL/Nordics/Baltics/SI/SK/HU. */
const CEE_ADJACENT = new Set(["DE", "AT", "PL", "SI", "SK", "HU", "DK", "SE", "NO", "FI", "IS", "EE", "LV", "LT"]);
const EUROPE = new Set([
  "GB", "IE", "FR", "NL", "BE", "LU", "ES", "PT", "IT", "CH", "GR", "HR", "RO", "BG", "RS",
  "UA", "MD", "MK", "BA", "ME", "AL", "MT", "CY", "LI", "MC", "CZ",
]);
const band = (iso: string): 0 | 1 | 2 => (CEE_ADJACENT.has(iso) ? 0 : EUROPE.has(iso) ? 1 : 2);

/** Does any comparable have its HQ or a sourced market in the CEE-adjacent set? */
export const proofNear = (p: Problem) =>
  (p.comps ?? []).some((c) => band(c.geo) === 0 || (c.markets ?? []).some((m) => band(m) === 0));

export function WhereMap({ p }: { p: Problem }) {
  const comps = p.comps ?? [];
  const hqs = [...new Set(comps.map((c) => c.geo))];
  const markets = [...new Set(comps.flatMap((c) => c.markets ?? []))].filter((m) => !hqs.includes(m));
  // outside both map frames: anything not in Europe or North America, and
  // Iceland, which sits west of the Europe frame's −12° edge
  const off = [...hqs, ...markets].filter((c) => (!["US", "CA"].includes(c) && band(c) === 2) || c === "IS");
  return (
    <div className="fgd">
      <div className="fgd-map"><EuropeMap comps={comps.map((c) => ({ geo: c.geo, markets: c.markets }))} home={p.region} /></div>
      <p className="fgd-key">
        <span className="fgd-sw fgd-sw--hq" /> HQ or sourced market ({hqs.length} HQ{hqs.length === 1 ? "" : "s"}{markets.length ? `, ${markets.length} more market${markets.length === 1 ? "" : "s"}` : ""})
        <span className="fgd-sw fgd-sw--home" /> Czechia
        {off.length > 0 && <span className="fgd-off"> · outside both frames: {off.map(countryName).join(", ")}</span>}
      </p>
    </div>
  );
}

const BANDS = [
  { k: "Next door", sub: "the ladder’s CEE-adjacent set: DE, AT, PL, SK, HU, SI, Nordics, Baltics" },
  { k: "Elsewhere in Europe", sub: "" },
  { k: "Outside Europe", sub: "" },
];

export function ProofDistance({ p }: { p: Problem }) {
  const comps = p.comps ?? [];
  const rows = BANDS.map((b, i) => ({
    ...b,
    hq: comps.filter((c) => band(c.geo) === i),
    // a comp that SELLS into this band from an HQ in another one
    via: comps.filter((c) => band(c.geo) !== i && (c.markets ?? []).some((m) => band(m) === i && m !== "CZ")),
  }));
  const near = rows[0].hq.length + rows[0].via.length > 0;
  return (
    <div className="fgx">
      <ol className="fgx-bands">
        {rows.map((r, i) => (
          <li key={r.k} className={r.hq.length + r.via.length ? "fgx-band" : "fgx-band is-empty"}>
            <span className="fgx-k">
              <span className="fgx-dot" aria-hidden="true" data-band={i} />
              {r.k}
            </span>
            {r.sub && <span className="fgx-sub">{r.sub}</span>}
            <span className="fgx-names">
              {r.hq.length === 0 && r.via.length === 0 && "—"}
              {r.hq.map((c) => <span key={c.name} className="fgx-name">{shortName(c.name)} <span className="fgx-geo">{c.geo}</span></span>)}
              {r.via.map((c) => <span key={`v${c.name}`} className="fgx-name fgx-name--via">{shortName(c.name)} <span className="fgx-geo">sells in {(c.markets ?? []).filter((m) => band(m) === i).join(", ")}</span></span>)}
            </span>
          </li>
        ))}
      </ol>
      <p className="fgx-read">
        {near ? "A comparable next door." : "No comparable next door."}
        <span className="fgx-read-n"> Whether it sells this exact product is the proof score’s call, not this figure’s.</span>
      </p>
    </div>
  );
}
