"""Tiny isometric hidden-line renderer -> compact SVG path data.

World: z up. Projection is true isometric (30 deg):
    sx = (x - y) * cos30,   sy = (x + y) / 2 - z
The viewer looks along -(1,1,1); depth toward the viewer = x + y + z.
Faces are planar polygons that occlude; every drawn primitive is sampled,
tested against the faces in front of it, and split exactly (bisection) where
it disappears. Styles: 'p' primary, 's' secondary (lighter), 'd' dashed secondary.
"""
import math

C30 = math.cos(math.pi / 6)
D = (1.0, 1.0, 1.0)
EPS = 0.06


def proj(p):
    x, y, z = p
    return ((x - y) * C30, (x + y) * 0.5 - z)


def add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def mul(a, k): return (a[0] * k, a[1] * k, a[2] * k)
def dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def lerp(a, b, t): return tuple(a[i] + (b[i] - a[i]) * t for i in range(len(a)))


def norm(a):
    l = math.sqrt(dot(a, a))
    return mul(a, 1 / l)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


AX = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}
# orthonormal in-plane pairs for circles whose normal is the given axis
PERP = {"x": ((0, 1, 0), (0, 0, 1)), "y": ((1, 0, 0), (0, 0, 1)), "z": ((1, 0, 0), (0, 1, 0))}


class Occ:
    __slots__ = ("n", "q", "nd", "poly", "bb")

    def __init__(self, pts):
        n = [0.0, 0.0, 0.0]
        k = len(pts)
        for i in range(k):
            c, m = pts[i], pts[(i + 1) % k]
            n[0] += (c[1] - m[1]) * (c[2] + m[2])
            n[1] += (c[2] - m[2]) * (c[0] + m[0])
            n[2] += (c[0] - m[0]) * (c[1] + m[1])
        self.n = tuple(n)
        self.q = pts[0]
        self.nd = dot(self.n, D)
        self.poly = [proj(p) for p in pts]
        xs = [p[0] for p in self.poly]
        ys = [p[1] for p in self.poly]
        self.bb = (min(xs), min(ys), max(xs), max(ys))

    def hides(self, P, s):
        if abs(self.nd) < 1e-9:
            return False
        x, y = s
        b = self.bb
        if x <= b[0] or x >= b[2] or y <= b[1] or y >= b[3]:
            return False
        t = dot(self.n, sub(self.q, P)) / self.nd
        if t <= EPS:
            return False
        return inside(s, self.poly)


def inside(s, poly, margin=0.03):
    x, y = s
    k = len(poly)
    c = False
    for i in range(k):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % k]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xi:
                c = not c
    if not c:
        return False
    for i in range(k):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % k]
        dx, dy = x2 - x1, y2 - y1
        L = dx * dx + dy * dy
        if L == 0:
            continue
        t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / L))
        ex, ey = x1 + t * dx - x, y1 + t * dy - y
        if ex * ex + ey * ey < margin * margin:
            return False
    return True


class Scene:
    def __init__(self):
        self.occ = []
        self.prims = []  # (kind, data, style, occlude)
        self.dots = []
        self._edges = set()

    # ---- occluders -------------------------------------------------------
    def occluder(self, pts):
        self.occ.append(Occ(pts))

    # ---- primitives ------------------------------------------------------
    def line(self, p, q, style="p", occlude=True):
        key = (tuple(round(v, 3) for v in p), tuple(round(v, 3) for v in q))
        key = tuple(sorted(key))
        if key in self._edges:
            return
        self._edges.add(key)
        self.prims.append(("L", (p, q), style, occlude))

    def poly(self, pts, style="p", closed=True, occlude=True):
        k = len(pts)
        for i in range(k if closed else k - 1):
            self.line(pts[i], pts[(i + 1) % k], style, occlude)

    def face(self, pts, style="p", draw=True):
        self.occluder(pts)
        if draw:
            self.poly(pts, style)

    def arc(self, c, u, v, t0=0.0, t1=2 * math.pi, style="p", occlude=True):
        self.prims.append(("A", (c, u, v, t0, t1), style, occlude))

    def circle(self, c, r, axis="z", style="p", fill=True, draw=True, occlude=True):
        u, v = PERP[axis] if isinstance(axis, str) else axis
        u, v = mul(u, r), mul(v, r)
        if draw:
            self.arc(c, u, v, 0, 2 * math.pi, style, occlude)
        if fill:
            self.occluder(ring(c, u, v, 48))
        return u, v

    def bez(self, p0, p1, p2, p3, style="p", occlude=True):
        self.prims.append(("C", (p0, p1, p2, p3), style, occlude))

    def dot(self, p, r=1.5):
        self.dots.append((p, r))

    # ---- compound --------------------------------------------------------
    def box(self, x, y, z, a, b, h, style="p", skip=(), draw=True):
        P = lambda i, j, k: (x + a * i, y + b * j, z + h * k)
        faces = {
            "bottom": [P(0, 0, 0), P(1, 0, 0), P(1, 1, 0), P(0, 1, 0)],
            "top": [P(0, 0, 1), P(1, 0, 1), P(1, 1, 1), P(0, 1, 1)],
            "x0": [P(0, 0, 0), P(0, 1, 0), P(0, 1, 1), P(0, 0, 1)],
            "x1": [P(1, 0, 0), P(1, 1, 0), P(1, 1, 1), P(1, 0, 1)],
            "y0": [P(0, 0, 0), P(1, 0, 0), P(1, 0, 1), P(0, 0, 1)],
            "y1": [P(0, 1, 0), P(1, 1, 0), P(1, 1, 1), P(0, 1, 1)],
        }
        for k, f in faces.items():
            if k in skip:
                continue
            self.face(f, style, draw)
        return faces

    def cyl(self, c, axis, r, h, style="p", top=True, bottom=True, n=48, side_style=None):
        a = AX[axis]
        u, v = PERP[axis]
        u, v = mul(u, r), mul(v, r)
        c2 = add(c, mul(a, h))
        if bottom:
            self.arc(c, u, v, 0, 2 * math.pi, style)
            self.occluder(ring(c, u, v, n))
        if top:
            self.arc(c2, u, v, 0, 2 * math.pi, style)
            self.occluder(ring(c2, u, v, n))
        pts = ring(c, u, v, n)
        pts2 = ring(c2, u, v, n)
        for i in range(n):
            j = (i + 1) % n
            self.occluder([pts[i], pts[j], pts2[j], pts2[i]])
        # silhouette generators
        ud, vd = dot(u, D), dot(v, D)
        t = math.atan2(-ud, vd)
        for tt in (t, t + math.pi):
            p = add(c, add(mul(u, math.cos(tt)), mul(v, math.sin(tt))))
            self.line(p, add(p, mul(a, h)), side_style or style)
        return c2, u, v

    def sphere(self, c, r, style="p"):
        n = norm(D)
        u = norm(cross(n, (0, 0, 1)))
        v = cross(n, u)
        u, v = mul(u, r), mul(v, r)
        self.arc(c, u, v, 0, 2 * math.pi, style)
        self.occluder(ring(c, u, v, 48))

    # ---- rendering ---------------------------------------------------------
    def visible(self, P):
        s = proj(P)
        for o in self.occ:
            if o.hides(P, s):
                return False
        return True

    def runs(self, f, n):
        ts = [i / n for i in range(n + 1)]
        vis = [self.visible(f(t)) for t in ts]
        out = []
        i = 0
        while i <= n:
            if not vis[i]:
                i += 1
                continue
            j = i
            while j + 1 <= n and vis[j + 1]:
                j += 1
            a = ts[i] if i == 0 else self.refine(f, ts[i - 1], ts[i])
            b = ts[j] if j == n else self.refine(f, ts[j + 1], ts[j])
            out.append([a, b])
            i = j + 1
        return out

    def refine(self, f, hid, vis):
        for _ in range(22):
            m = (hid + vis) / 2
            if self.visible(f(m)):
                vis = m
            else:
                hid = m
        return vis

    def render(self):
        """-> list of segments in pre-fit screen space, per style."""
        segs = []
        for kind, d, style, occl in self.prims:
            if kind == "L":
                p, q = d
                f = lambda t, p=p, q=q: lerp(p, q, t)
                L = math.dist(proj(p), proj(q))
                if L < 1e-6:
                    continue
            elif kind == "A":
                c, u, v, t0, t1 = d
                f = lambda t, c=c, u=u, v=v, t0=t0, t1=t1: add(
                    c, add(mul(u, math.cos(t0 + (t1 - t0) * t)), mul(v, math.sin(t0 + (t1 - t0) * t))))
                L = (t1 - t0) * max(math.hypot(*proj(u)), math.hypot(*proj(v)))
            else:
                p0, p1, p2, p3 = d
                f = lambda t, d=d: bez3(d, t)
                L = sum(math.dist(proj(f(i / 16)), proj(f((i + 1) / 16))) for i in range(16))
            n = max(8, int(L / 0.3))
            rr = self.runs(f, n) if occl else [[0.0, 1.0]]
            # merge micro gaps, drop micro runs
            merged = []
            for a, b in rr:
                if merged and (a - merged[-1][1]) * L < 0.4:
                    merged[-1][1] = b
                else:
                    merged.append([a, b])
            for a, b in merged:
                if (b - a) * L < 0.8:
                    continue
                if kind == "L":
                    segs.append((style, ("L", proj(f(a)), proj(f(b)))))
                elif kind == "A":
                    c, u, v, t0, t1 = d
                    ta, tb = t0 + (t1 - t0) * a, t0 + (t1 - t0) * b
                    segs.append((style, ("A", proj(c), proj_v(u), proj_v(v), ta, tb)))
                else:
                    sub_ = split3(d, a, b)
                    segs.append((style, ("C",) + tuple(proj(p) for p in sub_)))
        dots = [(proj(p), r) for p, r in self.dots]
        return segs, dots


def proj_v(u):
    return ((u[0] - u[1]) * C30, (u[0] + u[1]) * 0.5 - u[2])


def ring(c, u, v, n):
    return [add(c, add(mul(u, math.cos(2 * math.pi * i / n)), mul(v, math.sin(2 * math.pi * i / n)))) for i in range(n)]


def bez3(d, t):
    p0, p1, p2, p3 = d
    mt = 1 - t
    return tuple(mt ** 3 * p0[i] + 3 * mt * mt * t * p1[i] + 3 * mt * t * t * p2[i] + t ** 3 * p3[i] for i in range(3))


def split3(d, a, b):
    """Sub-curve of cubic d on [a, b]."""
    def split_at(pts, t):
        p0, p1, p2, p3 = pts
        p01, p12, p23 = lerp(p0, p1, t), lerp(p1, p2, t), lerp(p2, p3, t)
        p012, p123 = lerp(p01, p12, t), lerp(p12, p23, t)
        m = lerp(p012, p123, t)
        return (p0, p01, p012, m), (m, p123, p23, p3)
    pts = d
    if b < 1:
        pts = split_at(pts, b)[0]
    if a > 0:
        pts = split_at(pts, a / b)[1]
    return pts


# ---- SVG emission ------------------------------------------------------------

def seg_points(seg):
    k = seg[0]
    if k == "L":
        return [seg[1], seg[2]]
    if k == "C":
        return [bez2(seg[1:], i / 12) for i in range(13)]
    _, c, u, v, ta, tb = seg
    return [arcpt(c, u, v, ta + (tb - ta) * i / 24) for i in range(25)]


def bez2(d, t):
    p0, p1, p2, p3 = d
    mt = 1 - t
    return tuple(mt ** 3 * p0[i] + 3 * mt * mt * t * p1[i] + 3 * mt * t * t * p2[i] + t ** 3 * p3[i] for i in range(2))


def arcpt(c, u, v, t):
    return (c[0] + u[0] * math.cos(t) + v[0] * math.sin(t), c[1] + u[1] * math.cos(t) + v[1] * math.sin(t))


def fmt(v):
    s = f"{v:.1f}"
    if s.endswith(".0"):
        s = s[:-2]
    if s == "-0":
        s = "0"
    return s


def P2(p):
    return f"{fmt(p[0])} {fmt(p[1])}"


def emit(segs, dots, box=(120, 80), fit=None):
    """Fit to the target footprint, return {style: d} and dots."""
    pts = [p for _, s in segs for p in seg_points(s)] + [p for p, _ in dots]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    w, h = max(xs) - min(xs), max(ys) - min(ys)
    W, H, A = fit or (172, 118, 150 * 104)
    k = min(W / w, H / h, math.sqrt(A / (w * h)))
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    T = lambda p: ((p[0] - cx) * k + box[0], (p[1] - cy) * k + box[1])
    Tv = lambda p: (p[0] * k, p[1] * k)
    out = {}
    pieces = {}
    for style, s in segs:
        kind = s[0]
        if kind == "L":
            a, b = T(s[1]), T(s[2])
            pieces.setdefault(style, []).append(["L", a, b])
        elif kind == "C":
            pp = [T(p) for p in s[1:]]
            pieces.setdefault(style, []).append(["C", pp[0], pp[3], pp[1], pp[2]])
        else:
            _, c, u, v, ta, tb = s
            c, u, v = T(c), Tv(u), Tv(v)
            # split > pi spans to keep flags simple
            nseg = max(1, math.ceil((tb - ta) / (math.pi * 0.999)))
            for i in range(nseg):
                a0 = ta + (tb - ta) * i / nseg
                a1 = ta + (tb - ta) * (i + 1) / nseg
                pieces.setdefault(style, []).append(["A", arcpt(c, u, v, a0), arcpt(c, u, v, a1), u, v])
    for style, lst in pieces.items():
        out[style] = chain(lst)
    dd = [(T(p), r) for p, r in dots]
    return out, dd, k


def ellipse_params(u, v):
    a, c = u
    b, d = v
    E, F, G = a * a + b * b, a * c + b * d, c * c + d * d
    m = (E + G) / 2
    r = math.sqrt(((E - G) / 2) ** 2 + F * F)
    rx, ry = math.sqrt(m + r), math.sqrt(max(m - r, 0))
    rot = math.degrees(0.5 * math.atan2(2 * F, E - G))
    det = a * d - b * c
    return rx, ry, rot, det


def piece_cmd(pc, rev):
    kind = pc[0]
    if kind == "L":
        return "L" + P2(pc[1] if rev else pc[2])
    if kind == "C":
        _, a, b, c1, c2 = pc
        if rev:
            return "C" + " ".join(P2(p) for p in (c2, c1, a))
        return "C" + " ".join(P2(p) for p in (c1, c2, b))
    _, a, b, u, v = pc
    rx, ry, rot, det = ellipse_params(u, v)
    sweep = 1 if det > 0 else 0
    if rev:
        sweep = 1 - sweep
    end = a if rev else b
    return f"A{fmt(rx)} {fmt(ry)} {fmt(rot)} 0 {sweep} {P2(end)}"


def chain(pieces):
    """Greedy chaining of pieces that share endpoints (after rounding)."""
    key = lambda p: (round(p[0], 1), round(p[1], 1))
    remaining = list(pieces)
    out = []
    while remaining:
        pc = remaining.pop(0)
        start, end = pc[1], pc[2]
        cmds = [piece_cmd(pc, False)]
        path_start = start
        cur = end
        grown = True
        while grown:
            grown = False
            for i, q in enumerate(remaining):
                if key(q[1]) == key(cur):
                    cmds.append(piece_cmd(q, False)); cur = q[2]
                elif key(q[2]) == key(cur):
                    cmds.append(piece_cmd(q, True)); cur = q[1]
                else:
                    continue
                remaining.pop(i)
                grown = True
                break
        if key(cur) == key(path_start) and cmds[-1].startswith("L") and len(cmds) > 2:
            cmds[-1] = "Z"
        out.append("M" + P2(path_start) + "".join(cmds))
    s = "".join(out)
    # drop redundant separators: "L12 3" -> "L12 3" already compact; strip spaces before '-'
    s = s.replace(" -", "-")
    return s
