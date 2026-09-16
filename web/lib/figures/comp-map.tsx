// lib/figures — where the comparables are based and sell, against Czechia.
//
// The map is the production choropleth (web/lib/geomap.tsx), unmodified, in
// lab grays via kit.css; beside it, the same countries named and grouped by
// the PROOF ladder's own distance bands — SCORING.md rung 3 needs a market
// "CEE-adjacent (DE/AT/PL/Nordics/Baltics/SI/SK/HU)". Article column, 680px.
//
// WORDING RULE: comps[] records where a comparable is based and sells, never
// whether it sells THIS exact product (p-0010's German comparable, cargo.one,
// sells air-cargo booking — which is why that record's proof is 2, not 3). So
// this figure says "next door", never "proven next door".
import type { ReactNode } from "react";
import type { Problem } from "../data";
import { countryName } from "../format";
import { EuropeMap } from "../geomap";
import europe from "../geo/europe.json";
import americas from "../geo/americas.json";
import { shortName } from "./text";

/** SCORING.md, PROOF rung 3, verbatim: DE/AT/PL/Nordics/Baltics/SI/SK/HU. */
const CEE_ADJACENT = new Set(["DE", "AT", "PL", "SI", "SK", "HU", "DK", "SE", "NO", "FI", "IS", "EE", "LV", "LT"]);
const EUROPE = new Set([
  "GB", "IE", "FR", "NL", "BE", "LU", "ES", "PT", "IT", "CH", "GR", "HR", "RO", "BG", "RS",
  "UA", "MD", "MK", "BA", "ME", "AL", "MT", "CY", "LI", "MC", "CZ", "BY", "XK", "TR", "RU",
]);
export const band = (iso: string): 0 | 1 | 2 => (CEE_ADJACENT.has(iso) ? 0 : EUROPE.has(iso) ? 1 : 2);
const BANDS = ["Next door", "Elsewhere in Europe", "Outside Europe"] as const;

/** Countries the map can actually draw: the Europe frame and the US/CA inset. */
const DRAWABLE = new Set([...europe.features, ...americas.features].map((f) => f.properties.iso));

/** Any comparable based, or selling on the record, in the CEE-adjacent set. */
export const compNextDoor = (p: Problem) =>
  (p.comps ?? []).some((c) => band(c.geo) === 0 || (c.markets ?? []).some((m) => band(m) === 0));

/** `null` when there is no comparable, or none in a country the map can draw. */
export function CompMap({ p }: { p: Problem }): ReactNode {
  const comps = p.comps ?? [];
  const home = p.region.toUpperCase();
  const countries = [...new Set(comps.flatMap((c) => [c.geo, ...(c.markets ?? [])]))].filter((c) => c !== home);
  if (!countries.some((c) => DRAWABLE.has(c))) return null;

  // the legend: every country, the comparables based there and those that sell there
  const rows = countries.map((iso) => ({
    iso,
    band: band(iso),
    hq: comps.filter((c) => c.geo === iso).map((c) => shortName(c.name)),
    sells: comps.filter((c) => c.geo !== iso && (c.markets ?? []).includes(iso)).map((c) => shortName(c.name)),
    onMap: DRAWABLE.has(iso),
  })).sort((a, b) => a.band - b.band || b.hq.length - a.hq.length || b.sells.length - a.sells.length || a.iso.localeCompare(b.iso));
  const near = compNextDoor(p);

  return (
    <figure className="lk lk-fig lk-map">
      <div className="lk-map-row">
        <div className="lk-map-svg"><EuropeMap comps={comps.map((c) => ({ geo: c.geo, markets: c.markets }))} home={p.region} /></div>
        <div className="lk-map-key">
          {BANDS.map((label, b) => {
            const here = rows.filter((r) => r.band === b);
            if (here.length === 0) return null;
            return (
              <div key={label} className="lk-band">
                <p className="lk-band-k">{label}</p>
                <ul className="lk-band-l">
                  {here.map((r) => (
                    <li key={r.iso}>
                      <span className="lk-cty">{countryName(r.iso)}{!r.onMap && <span className="lk-off"> · not on the map</span>}</span>
                      <span className="lk-cty-n">
                        {r.hq.length > 0 && <>{r.hq.join(", ")} <span className="lk-dim">based here</span></>}
                        {r.hq.length > 0 && r.sells.length > 0 && " · "}
                        {r.sells.length > 0 && <>{r.sells.join(", ")} <span className="lk-dim">sell{r.sells.length === 1 ? "s" : ""} here</span></>}
                      </span>
                    </li>
                  ))}
                </ul>
              </div>
            );
          })}
          <p className="lk-read lk-read--sm">{near ? "A comparable is based or sells next door." : "No comparable is based or sells next door."}</p>
        </div>
      </div>
      <figcaption className="lk-cap">
        Gray: where the comparables on file are based, and the markets recorded for them. Czechia is outlined. Markets are recorded only when a source names them, so a blank country is unknown, not empty. Where a company is based does not show that it sells this exact product; that is Validated abroad’s call. “Next door” is the proof ladder’s own set: DE, AT, PL, SK, HU, SI, the Nordics and the Baltics.
      </figcaption>
    </figure>
  );
}
