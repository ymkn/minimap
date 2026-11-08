# minimap case — "framed chart" motif, one-piece bathtub, case only.
# build123d algebra mode. Units mm. Dimensions are provisional (motif check only).
# Parameterised builder: build_case() returns the solid; variations.py drives
# it to compare design directions. Running this file directly exports the
# default variant to ./output/. Preview rendering lives in render.py.
import math
from pathlib import Path
from build123d import *

OUT = 128.0      # outer size (square): key field 102 + rim 11.6 x2 + slack
TOP_Z = 12.0     # rim top height
FLOOR_T = 2.0    # bathtub floor thickness
FIELD = 102.0    # 6 x 17mm pitch
RIM = 11.6       # total rim width

# Rim profile as steps, outside -> inside: (segment start inset, segment end inset, top z)
# CNC assumptions (2026-11-06): 3-axis from top; groove/line widths >= 1.0mm so a
# phi1 endmill can cut them; internal corner radii >= R1.0 (phi2-compatible);
# ticks and the compass star are engraving work (V-bit / small endmill).
DEFAULT_PROFILE = [
    (0.0, 1.2, 12.0),    # bead
    (1.2, 5.0, 11.5),    # wide flat
    (5.0, 6.2, 10.7),    # groove (1.2 wide)
    (6.2, 8.8, 11.3),    # recovery terrace
    (8.8, 9.8, 11.0),    # thin line (1.0 wide)
    (9.8, 11.6, 10.8),   # inner flat (ticks live here)
]

def _prism(w, d, cy, inset, z0, z1, rmin=1.0, r_override=None):
    r = r_override if r_override is not None else max(4.0 - inset * 0.55, rmin)
    return Pos(0, cy, z0) * extrude(
        RectangleRounded(w - 2 * inset, d - 2 * inset, r), amount=z1 - z0)

def _tick(cx, cy, along_y, length, width, top_z, depth):
    sx, sy = (width, length) if along_y else (length, width)
    return Pos(cx, cy, top_z - depth) * extrude(
        Rectangle(sx, sy), amount=depth + 0.45)

def build_case(profile=DEFAULT_PROFILE, tick_style="key", tick_depth=0.6,
               star=True, seam=False, front_extra=0.0):
    out_w = OUT
    out_d = OUT + front_extra
    ocy = -front_extra / 2.0          # outer rectangle centre
    cav = OUT - 2 * RIM               # cavity size (square, centred on field)

    case = _prism(out_w, out_d, ocy, 0.0, 0.0, TOP_Z)
    # cavity corner radius is R1.0, as in the original prism(inset=RIM) call
    case -= _prism(cav, cav, 0.0, 0.0, FLOOR_T, TOP_Z + 2, r_override=1.0)

    # terrace cuts on the rim
    for a, b, z in profile:
        if z >= TOP_Z:
            continue
        case -= (_prism(out_w, out_d, ocy, a, z, TOP_Z + 2)
                 - _prism(out_w, out_d, ocy, b, z, TOP_Z + 2))

    # ticks on the innermost profile band
    if tick_style != "none":
        band_inset = (profile[-1][0] + RIM) / 2.0
        band_z = profile[-1][2]
        if tick_style == "key":
            longs = [-FIELD / 2 + k * 17.0 for k in range(7)]
            shorts = [p + 8.5 for p in longs[:-1]]
            marks = [(p, 1.4, 0.8) for p in longs] + [(p, 1.0, 0.5) for p in shorts]
        else:  # "ten": 10mm spacing, long every 50mm
            marks = [(float(p), 2.4 if p % 50 == 0 else 1.5, 1.0)
                     for p in range(-50, 51, 10)]
        fx = OUT / 2 - band_inset                 # side band |x|
        fy_back = OUT / 2 - band_inset            # back band y
        fy_front = -(OUT / 2 + front_extra) + band_inset
        cuts = []
        for p, ln, wd in marks:
            cuts.append(_tick(p, fy_back, True, ln, wd, band_z, tick_depth))
            cuts.append(_tick(p, fy_front, True, ln, wd, band_z, tick_depth))
            cuts.append(_tick(fx, p, False, ln, wd, band_z, tick_depth))
            cuts.append(_tick(-fx, p, False, ln, wd, band_z, tick_depth))
        u = cuts[0]
        for t in cuts[1:]:
            u += t
        case -= u

    # compass star on the floor at the omitted top-left switch position
    if star:
        cx, cy = -FIELD / 2 + 8.5, FIELD / 2 - 8.5
        ring = Pos(cx, cy, FLOOR_T - 0.3) * extrude(Circle(6.6) - Circle(6.3), amount=0.9)
        case -= ring
        pts = []
        for i in range(16):
            ang = -math.pi / 2 + i * math.pi / 8
            R = 5.8 if i % 4 == 0 else (3.5 if i % 2 == 0 else 1.5)
            pts.append((cx + R * math.cos(ang), cy + R * math.sin(ang)))
        case -= Pos(0, 0, FLOOR_T - 0.3) * extrude(Polygon(*pts), amount=0.9)

    # miter seams: a 45-degree hairline groove across the rim at each corner,
    # suggesting four joined frame pieces (motif only, the case is one piece)
    if seam:
        for sx in (1, -1):
            for sy in (1, -1):
                cx = sx * (OUT / 2 - RIM / 2)
                cy = sy * ((OUT / 2 + (front_extra if sy < 0 else 0.0)) - RIM / 2)
                ang = math.degrees(math.atan2(sy, sx))
                groove = (Pos(cx, cy, 10.55) * Rot(0, 0, ang)
                          * Box(17.5, 0.8, 1.9,
                                align=(Align.CENTER, Align.CENTER, Align.MIN)))
                case -= groove
    return case

if __name__ == "__main__":
    out_dir = Path(__file__).parent / "output"
    out_dir.mkdir(exist_ok=True)
    solid = build_case()
    bb = solid.bounding_box()
    print("bbox min", bb.min, "max", bb.max, "volume", round(solid.volume))
    export_step(solid, str(out_dir / "minimap_case.step"))
    export_stl(solid, str(out_dir / "minimap_case.stl"))
    export_gltf(solid, str(out_dir / "minimap_case.gltf"), unit=Unit.MM)
    print("exported to", out_dir)
