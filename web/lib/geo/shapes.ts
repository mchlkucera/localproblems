// Shape-building for the where-it-works map (../geomap.tsx): a hand-rolled
// equirectangular projection with a mid-latitude correction, applied to a
// vendored Natural Earth frame (europe.json, americas.json). Pure functions,
// no JSX, erasable types — node can import this file directly, which is how
// the scratchpad render-check harness stays honest.

export type Ring = number[][];
export type Feature = { properties: { iso: string }; geometry: { coordinates: Ring[][] } };
export type FeatureCollection = { features: Feature[] };
export type Frame = { w: number; s: number; e: number; n: number };
export type Shape = { d: string; anchor: { x: number; y: number } };
export type ShapeSet = { shapes: Map<string, Shape>; vw: number; vh: number };

/** Project a frame's features to pixel-space paths + label anchors.
    `vw` is the pixel width; height follows from the frame's aspect. */
export function buildShapes(fc: FeatureCollection, frame: Frame, vw: number): ShapeSet {
  const klat = Math.cos((((frame.s + frame.n) / 2) * Math.PI) / 180);
  const scale = vw / ((frame.e - frame.w) * klat);
  const vh = Math.ceil((frame.n - frame.s) * scale);
  const px = (lon: number) => (lon - frame.w) * klat * scale;
  const py = (lat: number) => (frame.n - lat) * scale;

  /** Compact path: integer coordinates, relative `l` deltas, minus signs as
      separators — roughly halves the inline-SVG bytes on every record page. */
  function ringPath(ring: Ring): string {
    const pts = ring.map(([lon, lat]) => [Math.round(px(lon)), Math.round(py(lat))]);
    let [x, y] = pts[0];
    const d = `M${x} ${y}l`;
    const parts: string[] = [];
    for (const [nx, ny] of pts.slice(1)) {
      const [dx, dy] = [nx - x, ny - y];
      if (dx === 0 && dy === 0) continue;
      parts.push(`${dx}${dy < 0 ? "" : " "}${dy}`);
      [x, y] = [nx, ny];
    }
    if (parts.length < 2) return "";                   // degenerate after rounding
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

  const shapes = new Map(
    fc.features.map((f) => [
      f.properties.iso,
      {
        d: f.geometry.coordinates.map((poly) => poly.map(ringPath).join("")).join(""),
        anchor: labelAnchor(f.geometry.coordinates),
      },
    ]),
  );
  return { shapes, vw, vh };
}
