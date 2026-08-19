// The "Where it works" map — a locality-shapes data device (heir of the
// retired v1 map): build-time inline SVG from a server component, encoding
// which countries a record's comparables operate in. Zero client JS, no d3 —
// a hand-rolled equirectangular projection over vendored geometry.
//
// Geometry: web/lib/geo/europe.json — vendored from Natural Earth 50m
// admin-0 countries ("Made with Natural Earth", naturalearthdata.com,
// public domain). Clipped to lon −12…41 / lat 34…71.5 (Russia and Turkey
// clip at the frame; overseas territories and speck islands dropped),
// Douglas–Peucker simplified at 0.05°, coordinates rounded to 0.01°.
// Comparables outside the frame (US, CA, IL, IS …) get no shape — they are
// still named in the map title and in the comps ledger below it.
import europe from "./geo/europe.json";

type Ring = number[][];
type Feature = { properties: { iso: string }; geometry: { coordinates: Ring[][] } };

// ---- projection: equirectangular with a mid-latitude correction ----------
const W = -12, S = 34, E = 41, N = 71.5;              // the vendored frame
const KLAT = Math.cos((((S + N) / 2) * Math.PI) / 180);
const VW = 448;                                        // 28rem at 16px — 1 unit ≈ 1px at full width
const SCALE = VW / ((E - W) * KLAT);
const VH = Math.ceil((N - S) * SCALE);
const px = (lon: number) => (lon - W) * KLAT * SCALE;
const py = (lat: number) => (N - lat) * SCALE;

// ---- shapes, computed once at module load (build time) -------------------
/** Compact path: integer coordinates, relative `l` deltas, minus signs as
    separators — roughly halves the inline-SVG bytes on every record page. */
function ringPath(ring: Ring): string {
  const pts = ring.map(([lon, lat]) => [Math.round(px(lon)), Math.round(py(lat))]);
  let [x, y] = pts[0];
  let d = `M${x} ${y}l`;
  const parts: string[] = [];
  for (const [nx, ny] of pts.slice(1)) {
    const [dx, dy] = [nx - x, ny - y];
    if (dx === 0 && dy === 0) continue;
    parts.push(`${dx}${dy < 0 ? "" : " "}${dy}`);
    [x, y] = [nx, ny];
  }
  if (parts.length < 2) return "";                     // degenerate after rounding
  return d + parts.map((p, i) => (i > 0 && !p.startsWith("-") ? ` ${p}` : p)).join("") + "z";
}

/** Shoelace area + centroid of a projected ring. */
function ringMetrics(ring: Ring): { area: number; cx: number; cy: number } {
  let a = 0, cx = 0, cy = 0;
  for (let i = 0; i < ring.length; i++) {
    const [x1, y1] = [px(ring[i][0]), py(ring[i][1])];
    const [x2, y2] = [px(ring[(i + 1) % ring.length][0]), py(ring[(i + 1) % ring.length][1])];
    const w = x1 * y2 - x2 * y1;
    a += w; cx += (x1 + x2) * w; cy += (y1 + y2) * w;
  }
  return { area: Math.abs(a / 2), cx: cx / (3 * a), cy: cy / (3 * a) };
}

/** Label anchor: centroid of the largest ring, x re-centred on the widest
    horizontal chord at that height — keeps the label inside bent shapes
    (Norway, Croatia) instead of drifting into a neighbour. */
function labelAnchor(polys: Ring[][]): { x: number; y: number } {
  let best: Ring = polys[0][0], bestArea = -1;
  for (const poly of polys) {
    const m = ringMetrics(poly[0]);
    if (m.area > bestArea) { bestArea = m.area; best = poly[0]; }
  }
  const { cx, cy } = ringMetrics(best);
  const xs: number[] = [];
  for (let i = 0; i < best.length; i++) {
    const [x1, y1] = [px(best[i][0]), py(best[i][1])];
    const [x2, y2] = [px(best[(i + 1) % best.length][0]), py(best[(i + 1) % best.length][1])];
    if (y1 === y2 || cy < Math.min(y1, y2) || cy >= Math.max(y1, y2)) continue;
    xs.push(x1 + ((cy - y1) * (x2 - x1)) / (y2 - y1));
  }
  xs.sort((a, b) => a - b);
  let x = cx;
  for (let i = 0, wMax = -1; i + 1 < xs.length; i += 2) {
    if (xs[i + 1] - xs[i] > wMax) { wMax = xs[i + 1] - xs[i]; x = (xs[i] + xs[i + 1]) / 2; }
  }
  return { x: Math.round(x), y: Math.round(cy) };
}

const SHAPES = new Map(
  (europe as { features: Feature[] }).features.map((f) => [
    f.properties.iso,
    {
      d: f.geometry.coordinates.map((poly) => poly.map(ringPath).join("")).join(""),
      anchor: labelAnchor(f.geometry.coordinates),
    },
  ]),
);

// ---- the component -------------------------------------------------------

export function EuropeMap({ comps, home }: { comps: string[]; home: string }) {
  const homeIso = home.toUpperCase();
  const compIsos = [...new Set(comps.map((c) => c.toUpperCase()))].filter((c) => c !== homeIso);
  const shaded = compIsos.filter((c) => SHAPES.has(c));
  const title = `Where it works: ${compIsos.join(", ")} — home market ${homeIso}`;
  return (
    <svg
      className="geomap"
      viewBox={`0 0 ${VW} ${VH}`}
      width={VW}
      height={VH}
      role="img"
      aria-labelledby="geomap-title"
    >
      <title id="geomap-title">{title}</title>
      {[...SHAPES].map(([iso, s]) =>
        iso === homeIso || shaded.includes(iso) ? null : <path key={iso} d={s.d} />,
      )}
      {shaded.map((iso) => <path key={iso} className="comp" d={SHAPES.get(iso)!.d} />)}
      {SHAPES.has(homeIso) && <path className="home" d={SHAPES.get(homeIso)!.d} />}
      {shaded.map((iso) => {
        const { x, y } = SHAPES.get(iso)!.anchor;
        return <text key={iso} className="lbl" x={x} y={y} dy="0.35em">{iso}</text>;
      })}
      {SHAPES.has(homeIso) && (
        <text
          className="lbl lbl-home"
          x={SHAPES.get(homeIso)!.anchor.x}
          y={SHAPES.get(homeIso)!.anchor.y}
          dy="0.35em"
        >
          {homeIso}
        </text>
      )}
    </svg>
  );
}
