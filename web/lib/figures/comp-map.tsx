// lib/figures — where the comparables are based and sell, against Czechia.
//
// The map is the production choropleth (web/lib/geomap.tsx), unmodified, in
// lab grays via kit.css, with one dot per comparable over it. `band` keeps the
// PROOF ladder's own distance bands — SCORING.md rung 3 needs a market
// "CEE-adjacent (DE/AT/PL/Nordics/Baltics/SI/SK/HU)".
//
// WORDING RULE: comps[] records where a comparable is based and sells, never
// whether it sells THIS exact product (p-0010's German comparable, cargo.one,
// sells air-cargo booking — which is why that record's proof is 2, not 3). So
// this figure says "next door", never "proven next door".
import type { CSSProperties, ReactNode } from "react";
import type { Problem } from "../data";
import { countryName } from "../format";
import { EuropeMap, INSET_IN_CROP, type MapView } from "../geomap";
import europe from "../geo/europe.json";
import americas from "../geo/americas.json";
import { buildShapes } from "../geo/shapes";
import { EXT, ExtArrow } from "../site/cite";
import { DotPeek, firstLine } from "./field";
import { shortName } from "./text";

/** SCORING.md, PROOF rung 3, verbatim: DE/AT/PL/Nordics/Baltics/SI/SK/HU. */
const CEE_ADJACENT = new Set(["DE", "AT", "PL", "SI", "SK", "HU", "DK", "SE", "NO", "FI", "IS", "EE", "LV", "LT"]);
const EUROPE = new Set([
  "GB", "IE", "FR", "NL", "BE", "LU", "ES", "PT", "IT", "CH", "GR", "HR", "RO", "BG", "RS",
  "UA", "MD", "MK", "BA", "ME", "AL", "MT", "CY", "LI", "MC", "CZ", "BY", "XK", "TR", "RU",
]);
export const band = (iso: string): 0 | 1 | 2 => (CEE_ADJACENT.has(iso) ? 0 : EUROPE.has(iso) ? 1 : 2);

/** Countries the map can actually draw: the Europe frame and the US/CA inset. */
const DRAWABLE = new Set([...europe.features, ...americas.features].map((f) => f.properties.iso));

/** Any comparable based, or selling on the record, in the CEE-adjacent set. */
export const compNextDoor = (p: Problem) =>
  (p.comps ?? []).some((c) => band(c.geo) === 0 || (c.markets ?? []).some((m) => band(m) === 0));

// Dot positions, in the map's own user units. MUST mirror geomap.tsx: the
// Europe frame at 448 wide, the North-America inset at 148 wide, boxed at
// (2,2) with a 4-unit pad, riding in the crop's top-left corner scaled by
// crop width / 448 × INSET_IN_CROP. geomap.tsx owns the drawing; change both together.
const FRAME = { w: -12, s: 34, e: 41, n: 71.5 };
const EU = buildShapes(europe, FRAME, 448);
const NA = buildShapes(americas, { w: -128.5, s: 24, e: -52, n: 61.5 }, 148);
const NA_PAD = 2 + 4;
const KLAT = Math.cos((((FRAME.s + FRAME.n) / 2) * Math.PI) / 180);
const SCALE = EU.vw / ((FRAME.e - FRAME.w) * KLAT);
const proj = (lon: number, lat: number) => ({ x: (lon - FRAME.w) * KLAT * SCALE, y: (FRAME.n - lat) * SCALE });

/** The crop (owner via coordinator, 2026-09-17: the full frame ran ~780px
    tall at 680 wide). The box around every drawn country's label anchor
    (home, bases, markets), padded, never smaller than central Europe, then
    widened or deepened to about 0.62 high per 1 wide (~420px at 680) and
    kept inside the frame. A spread that needs more height keeps it. */
function cropFor(isos: string[]): MapView {
  const a = proj(2, 57.5), b = proj(27, 43.5);
  let x0 = a.x, y0 = a.y, x1 = b.x, y1 = b.y;
  for (const iso of isos) {
    const s = EU.shapes.get(iso);
    if (!s) continue;
    x0 = Math.min(x0, s.anchor.x - 44); x1 = Math.max(x1, s.anchor.x + 44);
    y0 = Math.min(y0, s.anchor.y - 36); y1 = Math.max(y1, s.anchor.y + 36);
  }
  const R = 0.62;
  let w = x1 - x0, h = y1 - y0;
  if (h < w * R) { y0 -= (w * R - h) / 2; h = w * R; } else { x0 -= (h / R - w) / 2; w = h / R; }
  if (w > EU.vw) { x0 = 0; w = EU.vw; }
  if (h > EU.vh) { y0 = 0; h = EU.vh; }
  x0 = Math.max(0, Math.min(x0, EU.vw - w));
  y0 = Math.max(0, Math.min(y0, EU.vh - h));
  const r = (n: number) => Math.round(n * 10) / 10;
  return { x: r(x0), y: r(y0), w: r(w), h: r(h) };
}

/** A country's dot anchor in user units, or null when the map cannot draw it. */
function spot(iso: string, v: MapView): { x: number; y: number } | null {
  const eu = EU.shapes.get(iso);
  if (eu) return eu.anchor;
  const na = NA.shapes.get(iso);
  const k = (v.w / EU.vw) * INSET_IN_CROP;
  return na ? { x: v.x + k * (NA_PAD + na.anchor.x), y: v.y + k * (NA_PAD + na.anchor.y) } : null;
}

/** `null` without comparables, or with none in a country the map can draw.

    READS WITHOUT A CAPTION (owner, 2026-09-17: "make it self explanatory …
    fit the whole width … We should still keep a list and the map"). Full
    column width. Where each company is BASED is a numbered dot on a darker
    country; the other markets it sells in (`markets`) are a lighter shade. The
    list under the map is the key: number, name ↗, based in, also sells in,
    and its two column heads carry the two shades, so no sentence is needed.
    Czechia is outlined and keeps its "CZ" code on the map.

    Pointing at a dot or a list row (or opening a dot's card) brings up that
    company's countries in ink, with a hairline from its dot to each market;
    the rest of the shading steps back. CSS `:has()` only, keyed by `data-i`
    (kit.css enumerates 0–11). Several dots in one country sit as a small
    centred cluster. `scope` keeps popover and title ids unique when the page
    renders the figure twice. */
export function CompMap({ p, scope = "" }: { p: Problem; scope?: string }): ReactNode {
  const comps = p.comps ?? [];
  const home = p.region.toUpperCase();
  const countries = [...new Set(comps.flatMap((c) => [c.geo, ...(c.markets ?? [])]))].filter((c) => c !== home);
  if (comps.length === 0 || !countries.some((c) => DRAWABLE.has(c))) return null;

  const view = cropFor([home, ...countries]);
  const k = (view.w / EU.vw) * INSET_IN_CROP;
  const byGeo = new Map<string, number[]>();
  comps.forEach((c, i) => { if (spot(c.geo, view)) byGeo.set(c.geo, [...(byGeo.get(c.geo) ?? []), i]); });
  // numbers follow the list order, which is record order
  const num = new Map<number, number>();
  comps.forEach((c, i) => { if (spot(c.geo, view)) num.set(i, num.size + 1); });
  const also = (c: (typeof comps)[number]) => [...new Set(c.markets ?? [])].filter((m) => m !== c.geo);
  // "Also sells in" and the two swatches only when some company has markets
  // on file: otherwise the lighter shade never appears and the column is dashes
  const anyMk = comps.some((c) => also(c).length > 0);
  const pathOf = (iso: string) => {
    const eu = EU.shapes.get(iso);
    if (eu) return <path key={iso} d={eu.d} />;
    const na = NA.shapes.get(iso);
    return na ? <path key={iso} d={na.d} transform={`translate(${view.x} ${view.y}) scale(${k}) translate(${NA_PAD} ${NA_PAD})`} /> : null;
  };

  return (
    <figure className="lk lk-map" style={{ "--lk-u": view.w / 680 } as CSSProperties}>
      <div className="lk-map-svg">
        <EuropeMap comps={comps.map((c) => ({ geo: c.geo, markets: c.markets }))} home={p.region} titleId={`geomap-title${scope}`} view={view} />
        <svg className="lk-map-hl" viewBox={`${view.x} ${view.y} ${view.w} ${view.h}`} aria-hidden="true" focusable="false">
          {comps.map((c, i) => {
            const at = spot(c.geo, view);
            if (!at) return null;
            const mk = also(c).filter((m) => m !== home);
            return (
              <g key={i} className="lk-hl" data-i={i}>
                <g className="lk-hl-mk">{mk.map(pathOf)}</g>
                <g className="lk-hl-hq">{pathOf(c.geo)}</g>
                {mk.map((m) => {
                  const to = spot(m, view);
                  return to ? <line key={m} className="lk-hl-ln" x1={at.x} y1={at.y} x2={to.x} y2={to.y} /> : null;
                })}
              </g>
            );
          })}
        </svg>
        <div className="lk-map-dots">
          {[...byGeo].flatMap(([iso, is]) => {
            const at = spot(iso, view)!;
            const cols = Math.min(is.length, 3);
            const rows = Math.ceil(is.length / cols);
            return is.map((i, k) => {
              const c = comps[i];
              const r = Math.floor(k / cols);
              const inRow = r === rows - 1 ? is.length - r * cols : cols;
              const mk = also(c);
              return (
                <DotPeek
                  key={`${c.name}-${i}`}
                  id={`lk-map${scope}-${i}`}
                  index={i}
                  className="lk-map-pin"
                  mark={<span className="lk-num">{num.get(i)}</span>}
                  label={`${num.get(i)}: ${c.name}, based in ${countryName(c.geo)}, since ${c.since}${mk.length ? `, also sells in ${mk.map(countryName).join(", ")}` : ""}`}
                  name={c.name}
                  href={c.url}
                  m={null}
                  head={[countryName(c.geo), `since ${c.since}`]}
                  line={firstLine(c.traction)}
                  style={{
                    "--x": (at.x - view.x) / view.w, "--y": (at.y - view.y) / view.h,
                    "--dx": (k % cols) - (inRow - 1) / 2, "--dy": r - (rows - 1) / 2,
                  } as CSSProperties}
                />
              );
            });
          })}
        </div>
      </div>
      <table className="lk-map-t">
        <thead className={anyMk ? undefined : "lk-sr"}>
          <tr>
            <th scope="col"><span className="lk-sr">Number</span></th>
            <th scope="col"><span className="lk-sr">Company</span></th>
            <th scope="col">{anyMk && <span className="lk-sw is-hq" aria-hidden="true" />}Based in</th>
            {anyMk && <th scope="col"><span className="lk-sw is-mk" aria-hidden="true" />Also sells in</th>}
          </tr>
        </thead>
        <tbody>
          {comps.map((c, i) => {
            const mk = also(c);
            return (
              <tr key={i} data-i={i}>
                <td className="lk-map-tn">{num.has(i) ? <span className="lk-num" aria-hidden="true">{num.get(i)}</span> : null}</td>
                <td className="lk-map-tc"><a href={c.url} {...EXT}>{shortName(c.name)}<ExtArrow /></a></td>
                <td>{countryName(c.geo)}{num.has(i) ? "" : <span className="lk-map-off"> · not on the map</span>}</td>
                {anyMk && <td className={mk.length ? undefined : "is-none"}>{mk.length ? mk.map(countryName).join(", ") : "—"}</td>}
              </tr>
            );
          })}
        </tbody>
      </table>
    </figure>
  );
}
