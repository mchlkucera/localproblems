"""The twelve category scenes, in world units (z up)."""
import math
from iso import Scene, add, mul, sub, dot, D, lerp, bez3, split3

PI = math.pi


# ---- helpers -----------------------------------------------------------------

def extrude(S, outline, o, e1, e2, e3, depth, style="p", draw_back=True, top_style=None):
    """Extrude a 2D outline (segments in (u,w)) living in plane o+e1*u+e2*w along e3."""
    M = lambda u, w, k=0.0: add(o, add(add(mul(e1, u), mul(e2, w)), mul(e3, k)))
    samples = []
    for seg in outline:
        if seg[0] == "L":
            samples.append(seg[1])
        else:
            _, c, r, a0, a1 = seg
            n = max(2, int(abs(a1 - a0) / (PI / 16)))
            for i in range(n):
                t = a0 + (a1 - a0) * i / n
                samples.append((c[0] + r * math.cos(t), c[1] + r * math.sin(t)))
    base = [M(u, w) for u, w in samples]
    top = [M(u, w, depth) for u, w in samples]
    S.occluder(base)
    S.occluder(top)
    k = len(base)
    for i in range(k):
        j = (i + 1) % k
        S.occluder([base[i], base[j], top[j], top[i]])
    for lvl, st in ((0.0, style), (depth, top_style or style)):
        for seg in outline:
            if seg[0] == "L":
                S.line(M(*seg[1], lvl), M(*seg[2], lvl), st)
            else:
                _, c, r, a0, a1 = seg
                S.arc(M(c[0], c[1], lvl), mul(e1, r), mul(e2, r), a0, a1, st)
    # vertical (extrusion) edges at sharp corners + arc silhouettes
    def tang(seg, end):
        if seg[0] == "L":
            return (seg[2][0] - seg[1][0], seg[2][1] - seg[1][1])
        _, c, r, a0, a1 = seg
        t = a1 if end else a0
        s = 1 if a1 > a0 else -1
        return (-math.sin(t) * s, math.cos(t) * s)

    def start(seg):
        if seg[0] == "L":
            return seg[1]
        _, c, r, a0, a1 = seg
        return (c[0] + r * math.cos(a0), c[1] + r * math.sin(a0))

    n = len(outline)
    for i in range(n):
        a, b = outline[i - 1], outline[i]
        ta, tb = tang(a, True), tang(b, False)
        la, lb = math.hypot(*ta), math.hypot(*tb)
        cosang = (ta[0] * tb[0] + ta[1] * tb[1]) / (la * lb)
        if cosang < 0.996:
            p = start(b)
            S.line(M(*p), M(*p, depth), style)
    ts = math.atan2(-dot(e1, D), dot(e2, D))
    for seg in outline:
        if seg[0] != "A":
            continue
        _, c, r, a0, a1 = seg
        lo, hi = min(a0, a1), max(a0, a1)
        for t in (ts, ts + PI, ts - PI, ts + 2 * PI, ts - 2 * PI):
            if lo + 1e-6 < t < hi - 1e-6:
                p = (c[0] + r * math.cos(t), c[1] + r * math.sin(t))
                S.line(M(*p), M(*p, depth), style)


def rrect(x0, y0, x1, y1, r):
    """Rounded rectangle outline, CCW in (u,w)."""
    return [
        ("L", (x0 + r, y0), (x1 - r, y0)),
        ("A", (x1 - r, y0 + r), r, -PI / 2, 0),
        ("L", (x1, y0 + r), (x1, y1 - r)),
        ("A", (x1 - r, y1 - r), r, 0, PI / 2),
        ("L", (x1 - r, y1), (x0 + r, y1)),
        ("A", (x0 + r, y1 - r), r, PI / 2, PI),
        ("L", (x0, y1 - r), (x0, y0 + r)),
        ("A", (x0 + r, y0 + r), r, PI, 3 * PI / 2),
    ]


def polyline_outline(pts):
    return [("L", pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts))]


def hexa(S, v, style="p"):
    b, t = v[:4], v[4:]
    S.face(b, style)
    S.face(t, style)
    for i in range(4):
        j = (i + 1) % 4
        S.face([b[i], b[j], t[j], t[i]], style)


X, Y, Z = (1, 0, 0), (0, 1, 0), (0, 0, 1)
O = (0, 0, 0)


def rect_on(S, o, e1, e2, u0, w0, u1, w1, style="s"):
    M = lambda u, w: add(o, add(mul(e1, u), mul(e2, w)))
    S.poly([M(u0, w0), M(u1, w0), M(u1, w1), M(u0, w1)], style)


# ---- scenes ----------------------------------------------------------------------

def other():
    S = Scene()
    s = 30
    # base course: one 2x2 slab, seams drawn
    S.box(0, 0, 0, 2 * s, 2 * s, s)
    S.line((s, 2 * s, 0), (s, 2 * s, s), "s")
    S.line((2 * s, s, 0), (2 * s, s, s), "s")
    # second course: three blocks, the front one missing
    S.box(0, 0, s, s, s, s)
    S.box(s, 0, s, s, s, s)
    S.box(0, s, s, s, s, s)
    S.line((s, s, 2 * s), (s, 2 * s, 2 * s), "s")
    S.line((s, s, 2 * s), (2 * s, s, 2 * s), "s")
    # the missing block's outline, dashed, and the block itself, lifted aside
    S.line((2 * s, 2 * s, s), (2 * s, 2 * s, 2 * s), "d")
    S.line((2 * s, 2 * s, 2 * s), (s, 2 * s, 2 * s), "d")
    S.line((2 * s, 2 * s, 2 * s), (2 * s, s, 2 * s), "d")
    d, lift = 36, 40
    S.box(s + d, s - d, s + lift, s, s, s)
    S.line((2 * s + d, 2 * s - d, s + lift), (2 * s, 2 * s, s), "d")
    return S


def fintech():
    S = Scene()
    # two cards, flat, the top one offset
    for (x, y, z) in ((0, 0, 0), (10, -12, 2.4)):
        extrude(S, rrect(0, 0, 86, 54, 5), (x, y, z), X, Y, Z, 2.4)
    top = (10, -12, 4.8)
    M = lambda u, w: add(top, (u, w, 0))
    # chip
    S.poly([M(10, 12), M(24, 12), M(24, 22), M(10, 22)], "p")
    S.line(M(17, 12), M(17, 22), "s")
    S.line(M(10, 17), M(24, 17), "s")
    # number groups
    for g in range(4):
        u0 = 10 + g * 18
        S.line(M(u0, 34), M(u0 + 13, 34), "s")
    S.line(M(10, 44), M(38, 44), "s")
    # coin stack
    cx, cy = 116, 30
    jit = [(0, 0)] * 5 + [(1.5, -2.5)]
    h = 4
    for i, (jx, jy) in enumerate(jit):
        S.cyl((cx + jx, cy + jy, i * h), "z", 14, h)
    top_c = (cx + jit[-1][0], cy + jit[-1][1], len(jit) * h)
    S.circle(top_c, 9.5, "z", "s", fill=False)
    return S


def health():
    S = Scene()
    L, W = 96, 44
    # frame + mattress
    S.box(0, 0, 22, L, W, 5)
    extrude(S, rrect(3, 2, L - 3, W - 2, 3), (0, 0, 27), X, Y, Z, 9)
    # pillow
    extrude(S, rrect(7, 7, 25, W - 7, 5), (0, 0, 36), X, Y, Z, 5)
    # sheet fold
    S.line((50, 2, 36), (50, W - 2, 36), "s")
    S.line((50, W - 2, 36), (50, W, 27), "s")
    # head and foot boards
    S.box(-4, 0, 6, 4, W, 50)
    rect_on(S, (0, 0, 0), Y, Z, 5, 34, W - 5, 50, "s")
    S.box(L, 0, 6, 4, W, 32)
    rect_on(S, (L + 4, 0, 0), Y, Z, 5, 26, W - 5, 32, "s")
    # legs + castors
    for (x, y) in ((4, W - 4), (L - 4, W - 4), (4, 4), (L - 4, 4)):
        S.box(x - 1.5, y - 1.5, 6, 3, 3, 16)
        S.cyl((x - 3, y + 1.5, 3.5), "y", 3.5, 2.5) if y > W / 2 else S.cyl((x - 3, y - 4, 3.5), "y", 3.5, 2.5)
    # bedside monitor on a stand, pulse trace on its screen
    px, py = -8, W + 16
    S.cyl((px, py, 0), "z", 7, 2.5)
    S.line((px, py, 2.5), (px, py, 56))
    mx0, my0, mz0 = px - 13, py - 3, 56
    S.box(mx0, my0, mz0, 26, 5, 19)
    fy = my0 + 5
    rect_on(S, (mx0, fy, mz0), X, Z, 3, 3, 23, 16, "s")
    ecg = [(3, 8), (8, 8), (10, 10), (12, 8), (13.5, 8), (15, 4.5), (16.5, 14), (18, 8), (23, 8)]
    for (u0, w0), (u1, w1) in zip(ecg, ecg[1:]):
        S.line((mx0 + u0, fy, mz0 + w0), (mx0 + u1, fy, mz0 + w1))
    # lead from the monitor to the bed
    S.bez((px, py - 3, 58), (px + 4, py - 12, 50), (10, W - 4, 44), (16, W - 10, 36), "s")
    return S


def housing():
    S = Scene()
    a, b, h = 100, 36, 80
    S.box(0, 0, 0, a, b, h)
    S.box(62, 9, h, 20, 18, 9)          # lift machine room
    fl = 15
    for f in range(5):
        z0 = 8 + f * fl
        for c in range(5):
            u0 = 7 + c * 18.5
            if f == 0 and c == 2:
                continue
            rect_on(S, (0, b, 0), X, Z, u0, z0, u0 + 11, z0 + 7, "p")
        for c in range(2):
            u0 = 6 + c * 15
            rect_on(S, (a, 0, 0), Y, Z, u0, z0, u0 + 9, z0 + 7, "p")
        if f:
            S.line((0, b, z0 - 4), (a, b, z0 - 4), "s")
            S.line((a, 0, z0 - 4), (a, b, z0 - 4), "s")
    # entrance: a door bay in place of the middle ground-floor window
    rect_on(S, (0, b, 0), X, Z, 44.5, 0, 55.5, 13, "p")
    S.line((42, b, 13), (58, b, 13), "s")
    return S


def energy():
    S = Scene()
    L, B, H = 70, 50, 34
    S.box(0, 0, 0, L, B, H)
    ridge_z, ov, th = 60, 4, 3
    ey = 25 + 30  # front eave y
    run = 30
    # roof planes as slabs
    front = [(-ov, 25, ridge_z - th), (L + ov, 25, ridge_z - th), (L + ov, ey, ridge_z - run - th), (-ov, ey, ridge_z - run - th),
             (-ov, 25, ridge_z), (L + ov, 25, ridge_z), (L + ov, ey, ridge_z - run), (-ov, ey, ridge_z - run)]
    back = [(-ov, 25, ridge_z - th), (L + ov, 25, ridge_z - th), (L + ov, 25 - run, ridge_z - run - th), (-ov, 25 - run, ridge_z - run - th),
            (-ov, 25, ridge_z), (L + ov, 25, ridge_z), (L + ov, 25 - run, ridge_z - run), (-ov, 25 - run, ridge_z - run)]
    hexa(S, front)
    hexa(S, back)
    # gable
    S.face([(L, 0, H), (L, B, H), (L, 25, ridge_z - th - 1)])
    # panels on the front plane
    o = (-ov, ey, ridge_z - run)
    e1 = (1, 0, 0)
    e2 = (0, -1 / math.sqrt(2), 1 / math.sqrt(2))
    nrm = (0, 1 / math.sqrt(2), 1 / math.sqrt(2))
    lift = mul(nrm, 1.6)
    M = lambda u, w: add(add(o, add(mul(e1, u), mul(e2, w))), lift)
    u0, u1, w0, w1 = 8, 70, 6, 36
    S.poly([M(u0, w0), M(u1, w0), M(u1, w1), M(u0, w1)], "p")
    for i in range(1, 4):
        u = u0 + (u1 - u0) * i / 4
        S.line(M(u, w0), M(u, w1), "p")
    S.line(M(u0, (w0 + w1) / 2), M(u1, (w0 + w1) / 2), "p")
    for i in range(1, 12):
        u = u0 + (u1 - u0) * i / 12
        if i % 3:
            S.line(M(u, w0), M(u, w1), "s")
    for w in (w0 + 7.5, w0 + 22.5):
        S.line(M(u0, w), M(u1, w), "s")
    # meter cabinet on the gable wall + cable
    S.box(L, 32, 9, 3, 11, 15)
    rect_on(S, (L + 3, 32, 9), Y, Z, 2.5, 8, 8.5, 12, "p")
    S.line((L + 3, 34.5, 4.5 + 9), (L + 3, 40.5, 4.5 + 9), "s")
    # cable from the array down the gable to the meter
    S.line((L + 1.5, 37.5, 24), (L + 1.5, 37.5, 31), "s")
    # door + window on the long side
    rect_on(S, (0, B, 0), X, Z, 12, 0, 23, 19, "s")
    rect_on(S, (0, B, 0), X, Z, 34, 8, 56, 19, "s")
    return S


def mobility():
    S = Scene()
    W = 36
    # cargo box
    S.box(0, 0, 16, 88, W, 44)
    for x in range(11, 88, 11):
        S.line((x, W, 16), (x, W, 60), "s")
    # chassis
    S.box(2, 5, 10, 124, W - 10, 6)
    # cab profile in xz, extruded along y
    prof = [(92, 10), (126, 10), (126, 32), (120, 50), (92, 50)]
    extrude(S, polyline_outline(prof), (0, 1, 0), X, Z, Y, W - 2)
    # windscreen on the slope, side window, door
    sl = lambda t, y: (126 - 6 * t, y, 32 + 18 * t)
    S.poly([sl(0.2, 4), sl(0.2, W - 4), sl(0.85, W - 4), sl(0.85, 4)], "p")
    rect_on(S, (0, W - 1, 0), X, Z, 104, 34, 116, 46, "p")
    S.poly([(100, W - 1, 12), (100, W - 1, 46)], "s", closed=False)
    S.line((126, 6, 16), (126, W - 4, 16), "s")
    for z in (20, 23, 26):
        S.line((126, 10, z), (126, W - 8, z), "s")
    # wheels
    for x in (16, 36, 112):
        for y0 in (W - 6, 0):
            S.cyl((x, y0, 9), "y", 9, 6)
        S.circle((x, W, 9), 3.5, "y", "s", fill=False)
    return S


def govtech():
    S = Scene()
    Wd = 76
    S.box(-6, -6, 0, 94, Wd + 12, 4)
    S.box(-3, -3, 4, 88, Wd + 6, 4)
    # cella (hall) behind the portico
    S.box(0, 0, 8, 58, Wd, 40)
    rect_on(S, (58, 0, 0), Y, Z, 30, 8, 46, 32, "s")
    for u in (10, 26, 42):
        rect_on(S, (0, Wd, 0), X, Z, u, 18, u + 8, 38, "s")
    # columns
    for y in (7, 27.7, 48.3, 69):
        S.cyl((74, y, 8), "z", 3.4, 40)
    # entablature and pediment
    S.box(-1, -1, 48, 80, Wd + 2, 7)
    top = 55
    pz = top + 13
    S.face([(79, -1, top), (79, Wd + 1, top), (79, Wd / 2, pz)])
    S.face([(-1, -1, top), (-1, Wd + 1, top), (-1, Wd / 2, pz)], draw=False)
    S.face([(-1, Wd + 1, top), (79, Wd + 1, top), (79, Wd / 2, pz), (-1, Wd / 2, pz)])
    S.face([(-1, -1, top), (79, -1, top), (79, Wd / 2, pz), (-1, Wd / 2, pz)])
    S.poly([(79, 9, top + 2.5), (79, Wd - 9, top + 2.5), (79, Wd / 2, pz - 3.5)], "s")
    return S


def retail():
    S = Scene()
    W = 40
    # basket side profile (x, z), extruded along y; open top
    # side profile (x, z): near-vertical back, raked front; open top
    xb0, xb1, xf0, xf1, zb, zt = 4, 0, 56, 68, 22, 50
    prof = [(xb1, zt), (xf1, zt), (xf0, zb), (xb0, zb)]
    near = [(x, W, z) for x, z in prof]
    far = [(x, 0, z) for x, z in prof]
    S.face(near)
    S.face(far)
    S.face([far[1], far[2], near[2], near[1]])
    S.face([far[3], far[0], near[0], near[3]])
    S.face([far[2], far[3], near[3], near[2]])
    xat = lambda z, a, b: a + (b - a) * (zt - z) / (zt - zb)
    # mesh on the near side and the raked front
    for i in range(1, 7):
        t = i / 7
        S.line((lerp((xb0,), (xf0,), t)[0], W, zb), (lerp((xb1,), (xf1,), t)[0], W, zt), "s")
    for z in (29, 36, 43):
        S.line((xat(z, xb1, xb0), W, z), (xat(z, xf1, xf0), W, z), "s")
    for y in (10, 20, 30):
        S.line((xf0, y, zb), (xf1, y, zt), "s")
    # handle: side rails run back and up to a grip
    for y in (0, W):
        S.line((xb1, y, zt), (-9, y, zt + 7))
    S.cyl((-9, -3, zt + 7), "y", 1.8, W + 6)
    # chassis
    for y in (3, W - 3):
        S.line((8, y, zb), (8, y, 9))
        S.line((50, y, zb), (50, y, 9))
        S.line((4, y, 9), (66, y, 9))
    S.line((66, 3, 9), (66, W - 3, 9))
    # castors
    for x in (8, 62):
        for y in (W - 3, 3):
            S.cyl((x, y - 1.5, 4.5), "y", 4.5, 3)
    # a parcel in the basket
    S.box(20, 9, zb, 24, 22, 16)
    S.line((32, 9, zb + 16), (32, 31, zb + 16), "s")
    return S


def b2b():
    S = Scene()
    # forklift driving +x; its side faces the viewer (y = 30 plane)
    W = 30
    S.box(0, 0, 6, 38, W, 20)                       # body / counterweight
    S.line((0, W, 12), (38, W, 12), "s")
    # overhead guard: rear posts upright, front posts raked
    for y in (1, W - 1):
        S.line((3, y, 26), (3, y, 58))
        S.line((34, y, 26), (40, y, 58))
    S.poly([(1, 1, 58), (40, 1, 58), (40, W - 1, 58), (1, W - 1, 58)])
    for x in (11, 20, 29):
        S.line((x, 1, 58), (x, W - 1, 58), "s")
    # seat + steering
    S.poly([(10, W - 8, 26), (10, 8, 26), (10, 8, 36), (10, W - 8, 36)], "s")
    S.line((30, W / 2, 26), (27, W / 2, 36), "s")
    # mast: two uprights + top tie
    for y in (3, W - 6):
        S.box(42, y, 2, 3, 3, 66)
    S.box(42, 3, 64, 3, W - 6, 3)
    # carriage + forks
    S.box(45, 2, 9, 2, W - 4, 16)
    # pallet on the forks
    px0, pw = 47, 40
    py0 = -5
    S.box(px0, py0, 10, pw, pw, 1.5)
    for y in (py0, py0 + 17, py0 + 34):
        S.box(px0, y, 11.5, pw, 6, 3.5)
    S.box(px0, py0, 15, pw, pw, 2)
    # load: two cartons
    S.box(px0 + 2, py0 + 2, 17, pw - 4, pw - 4, 19)
    S.line((px0 + 2, py0 + 20, 36), (px0 + pw - 2, py0 + 20, 36), "s")
    S.line((px0 + pw - 2, py0 + 20, 36), (px0 + pw - 2, py0 + 20, 29), "s")
    S.box(px0 + 7, py0 + 7, 36, pw - 14, pw - 14, 14)
    S.line((px0 + 7, py0 + 20, 50), (px0 + pw - 7, py0 + 20, 50), "s")
    S.line((px0 + pw - 7, py0 + 20, 50), (px0 + pw - 7, py0 + 20, 44), "s")
    # wheels
    for x, r in ((34, 9), (8, 7)):
        for y0 in (W, -5):
            S.cyl((x, y0, r), "y", r, 5)
        S.circle((x, W + 5, r), r * 0.4, "y", "s", fill=False)
    return S


def legal():
    S = Scene()
    a, b, t = 62, 86, 2
    for i, (x, y) in enumerate(((0, 0), (4, -3), (-2, -6))):
        S.box(x, y, i * t, a, b, t)
    top = (-2, -6, 3 * t)
    M = lambda u, w: add(top, (u, w, 0))
    S.line(M(8, 10), M(40, 10), "p")
    for i, w in enumerate(range(18, 58, 6)):
        S.line(M(8, w), M(54 if i % 3 != 2 else 36, w), "s")
    # signature
    s0 = M(10, 72)
    S.bez(s0, M(16, 60), M(20, 80), M(26, 70), "p")
    S.bez(M(26, 70), M(30, 64), M(32, 76), M(40, 70), "p")
    # seal impression
    c = M(46, 72)
    S.circle(c, 9, "z", "s", fill=False)
    S.circle(c, 6.5, "z", "s", fill=False)
    # rubber stamp standing near the seal
    sc = M(40, 32)
    S.box(sc[0] - 10, sc[1] - 10, sc[2], 20, 20, 3)
    S.box(sc[0] - 8, sc[1] - 8, sc[2] + 3, 16, 16, 6)
    S.cyl((sc[0], sc[1], sc[2] + 9), "z", 3.8, 19, top=False)
    S.sphere((sc[0], sc[1], sc[2] + 28), 7.5)
    return S


def education():
    S = Scene()
    L, Wp = 64, 46
    S.box(-3, -Wp - 3, 0, L + 6, 2 * Wp + 6, 2.5)
    z0 = 2.5
    def curve(side):
        s = side
        return [(0, 0, z0 + 2), (0, s * 7, z0 + 11), (0, s * 22, z0 + 12), (0, s * Wp, z0 + 8)]
    for side in (1, -1):
        c = curve(side)
        # surface occluders
        n = 16
        pts = [bez3(c, i / n) for i in range(n + 1)]
        for i in range(n):
            p, q = pts[i], pts[i + 1]
            S.occluder([p, add(p, (L, 0, 0)), add(q, (L, 0, 0)), q])
        # page block side down to cover
        e = c[3]
        S.occluder([e, add(e, (L, 0, 0)), (L, e[1], z0), (0, e[1], z0)])
        S.occluder([(L, 0, z0), (L, 0, z0 + 2)] + [add(p, (L, 0, 0)) for p in pts[1:]] + [(L, e[1], z0)])
        S.occluder([(0, 0, z0), (0, 0, z0 + 2)] + pts[1:] + [(0, e[1], z0)])
        for x in (0, L):
            cc = [add(p, (x, 0, 0)) for p in c]
            S.bez(*cc)
            S.line(add(e, (x, 0, 0)), (x, e[1], z0))
        S.line(e, add(e, (L, 0, 0)))
        for dz in (2.7, 5.4):
            S.line((0, e[1], e[2] - dz), (L, e[1], e[2] - dz), "s")
        # text lines
        for i, x in enumerate(range(10, L - 6, 6)):
            cc = [add(p, (x, 0, 0)) for p in c]
            b = 0.88 if i % 4 != 3 else 0.55
            sub_ = split3(cc, 0.22, b)
            S.bez(*sub_, style="s")
    S.line((0, 0, z0 + 2), (L, 0, z0 + 2))
    return S


def environment():
    S = Scene()
    L, B, H = 48, 34, 34
    # a cut-away block of ground under the building, drawn as a section (edges only)
    gx0, gy0, gx1, gy1, gz = -6, -6, L + 6, B + 22, -12
    S.poly([(gx0, gy0, 0), (gx1, gy0, 0), (gx1, gy1, 0), (gx0, gy1, 0)], "s")
    for (x, y) in ((gx1, gy0), (gx1, gy1), (gx0, gy1)):
        S.line((x, y, 0), (x, y, gz), "s")
    S.line((gx1, gy0, gz), (gx1, gy1, gz), "s")
    S.line((gx1, gy1, gz), (gx0, gy1, gz), "s")
    # the building, mono-pitch roof falling to the gutter side
    S.box(0, 0, 0, L, B, H)
    ov, th = 4, 3
    y0, y1, zh, zl = -ov, B + 3.5, H + 12, H + 1
    hexa(S, [(-ov, y0, zh - th), (L + ov, y0, zh - th), (L + ov, y1, zl - th), (-ov, y1, zl - th),
             (-ov, y0, zh), (L + ov, y0, zh), (L + ov, y1, zl), (-ov, y1, zl)])
    # gutter + downpipe
    gy, gzz = B + 4, zl - th - 2.2
    S.cyl((-ov, gy, gzz), "x", 3.2, L + 2 * ov)
    px, py = L - 7, B + 4
    S.cyl((px, py, 0), "z", 3, gzz - 3.2, top=False)
    for z in (9, 21):
        S.line((px - 3.4, B, z), (px + 3.4, B, z), "s")
    # below ground: the pipe drops into a shaft and on into the sewer main
    my = B + 15
    S.line((px, py, 0), (px, py, -7), "d")
    S.line((px, py, -7), (px, gy1, -7), "d")
    S.circle((px, my, 0), 5, "z", "p", fill=False)
    S.circle((px, my, 0), 2.8, "z", "s", fill=False)
    S.circle((px, gy1, -7), 3.6, "y", "p", fill=False)
    # openings
    rect_on(S, (0, B, 0), X, Z, 6, 0, 16, 20, "s")
    rect_on(S, (0, B, 0), X, Z, 22, 10, 34, 22, "s")
    rect_on(S, (L, 0, 0), Y, Z, 9, 10, 25, 22, "s")
    # rain, on the iso grid above the roof
    for i, (x, y) in enumerate(((4, 2), (22, 2), (40, 2), (13, 15), (31, 15), (49, 15), (4, 28), (22, 28), (40, 28))):
        z = zh + 5 + (i % 3) * 3 - (y / B) * 9
        S.line((x, y, z), (x, y, z + 6), "s", occlude=False)
    return S


SCENES = {
    "fintech": fintech,
    "health": health,
    "housing": housing,
    "energy": energy,
    "mobility": mobility,
    "govtech": govtech,
    "retail-services": retail,
    "b2b": b2b,
    "legal-compliance": legal,
    "education": education,
    "environment": environment,
    "other": other,
}
