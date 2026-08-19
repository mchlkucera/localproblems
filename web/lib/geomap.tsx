// The "Where it works" map — a locality-shapes data device (heir of the
// retired v1 map): build-time inline SVG from a server component, encoding
// which countries a record's comparables operate in. Zero client JS, no d3 —
// a hand-rolled equirectangular projection (lib/geo/shapes.ts) over vendored
// geometry.
//
// Each comparable contributes its HQ country (`geo`) and, optionally, the
// `markets` it demonstrably sells into. The union fills ink-muted; ISO2 mono
// labels sit on HQ countries only — market-only countries are a quiet
// presence, named in the svg title's "operating markets" segment instead.
//
// Geometry: web/lib/geo/*.json — vendored from Natural Earth 50m admin-0
// countries ("Made with Natural Earth", naturalearthdata.com, public
// domain); scripts follow the scratchpad vendor-europe.mjs pattern.
//   europe.json    main frame, lon −12…41 / lat 34…71.5 (Russia and Turkey
//                  clip at the frame; overseas territories and speck islands
//                  dropped), Douglas–Peucker 0.05°, rounded to 0.01°.
//   americas.json  the North-America inset, lon −128.5…−52 / lat 24…61.5
//                  (US + CA only, aggressively simplified at 0.3°; Alaska,
//                  Hawaii and the Arctic archipelago fall outside).
//
// The inset is an atlas-plate corner panel: hairline-boxed in the main
// frame's empty NW Atlantic — the direction North America actually lies —
// rendered only when a record's comp geography (HQ or market) includes US
// or CA. It adds no
// width or height; Europe keeps the full 28rem frame. Comparables outside
// both frames (IL, IS …) still get no shape — a south-east extension for
// Israel alone would add a near-empty Mediterranean band and shrink the
// protagonist, so they stay named in the map title and the comps ledger.
import { buildShapes } from "./geo/shapes";
import europe from "./geo/europe.json";
import americas from "./geo/americas.json";

// ---- frames, computed once at module load (build time) -------------------
const VW = 448;                        // 28rem at 16px — 1 unit ≈ 1px at full width
const EU = buildShapes(europe, { w: -12, s: 34, e: 41, n: 71.5 }, VW);
const NA = buildShapes(americas, { w: -128.5, s: 24, e: -52, n: 61.5 }, 148);

// Inset panel: box at (2,2), geometry inset by a 4px margin. The box stays
// clear of Norway (x ≥ 160 above y 119) and Shetland (y ≥ 148) — free ocean.
const INSET = { x: 2, y: 2, w: NA.vw + 8, h: NA.vh + 8, pad: 4 };

// ---- the component -------------------------------------------------------

/** One comparable's geography: `geo` is the HQ country (labelled), `markets`
    the countries it demonstrably sells into (filled, never labelled). */
export type CompGeo = { geo: string; markets?: string[] };

export function EuropeMap({ comps, home }: { comps: CompGeo[]; home: string }) {
  const homeIso = home.toUpperCase();
  const dedupe = (xs: string[]) =>
    [...new Set(xs.map((c) => c.toUpperCase()))].filter((c) => c !== homeIso);
  const hqs = dedupe(comps.map((c) => c.geo));
  const markets = dedupe(comps.flatMap((c) => c.markets ?? [])).filter((c) => !hqs.includes(c));
  const union = [...hqs, ...markets];
  const shaded = union.filter((c) => EU.shapes.has(c));
  const naShaded = union.filter((c) => NA.shapes.has(c));
  const title =
    `Where it works: ${hqs.join(", ")}` +
    (markets.length > 0 ? ` — operating markets: ${markets.join(", ")}` : "") +
    ` — home market ${homeIso}`;
  return (
    <svg
      className="geomap"
      viewBox={`0 0 ${EU.vw} ${EU.vh}`}
      width={EU.vw}
      height={EU.vh}
      role="img"
      aria-labelledby="geomap-title"
    >
      <title id="geomap-title">{title}</title>
      {[...EU.shapes].map(([iso, s]) =>
        iso === homeIso || shaded.includes(iso) ? null : <path key={iso} d={s.d} />,
      )}
      {shaded.map((iso) => <path key={iso} className="comp" d={EU.shapes.get(iso)!.d} />)}
      {EU.shapes.has(homeIso) && <path className="home" d={EU.shapes.get(homeIso)!.d} />}
      {shaded.filter((c) => hqs.includes(c)).map((iso) => {
        const { x, y } = EU.shapes.get(iso)!.anchor;
        return <text key={iso} className="lbl" x={x} y={y} dy="0.35em">{iso}</text>;
      })}
      {EU.shapes.has(homeIso) && (
        <text
          className="lbl lbl-home"
          x={EU.shapes.get(homeIso)!.anchor.x}
          y={EU.shapes.get(homeIso)!.anchor.y}
          dy="0.35em"
        >
          {homeIso}
        </text>
      )}
      {naShaded.length > 0 && (
        <g>
          <rect className="inset" x={INSET.x} y={INSET.y} width={INSET.w} height={INSET.h} />
          <g transform={`translate(${INSET.x + INSET.pad} ${INSET.y + INSET.pad})`}>
            {[...NA.shapes].map(([iso, s]) =>
              naShaded.includes(iso) ? null : <path key={iso} d={s.d} />,
            )}
            {naShaded.map((iso) => <path key={iso} className="comp" d={NA.shapes.get(iso)!.d} />)}
            {naShaded.filter((c) => hqs.includes(c)).map((iso) => {
              const { x, y } = NA.shapes.get(iso)!.anchor;
              return <text key={iso} className="lbl" x={x} y={y} dy="0.35em">{iso}</text>;
            })}
          </g>
        </g>
      )}
    </svg>
  );
}
