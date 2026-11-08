# Design-direction variations for the minimap framed case.
# Builds several variants from model_case.build_case(), exports STEP/STL per
# variant into output/variants/, renders top + perspective PNGs, and composes
# two labelled contact sheets (sheet_top.png / sheet_persp.png).
# Run headless: xvfb-run python variations.py
from pathlib import Path
from build123d import export_step, export_stl
from model_case import build_case, DEFAULT_PROFILE
import vtk
from PIL import Image, ImageDraw

BASE = Path(__file__).parent / "output" / "variants"
BASE.mkdir(parents=True, exist_ok=True)

FREECAD_PROFILE = [   # three even steps + hairline groove, cf. FreeCAD concept
    (0.0, 1.0, 12.0),
    (1.0, 2.0, 11.7),   # hairline groove
    (2.0, 3.3, 11.9),
    (3.3, 6.8, 11.5),
    (6.8, 11.6, 11.1),  # tick band
]
MINIMAL_PROFILE = [   # one plain step, almost no decoration
    (0.0, 1.4, 12.0),
    (1.4, 11.6, 11.55),
]

VARIANTS = [
    ("1_base",        "current design, no seam",
     dict()),
    ("2_seam_minimal", "plain rim + miter seam only",
     dict(profile=MINIMAL_PROFILE, tick_style="none", star=False, seam=True)),
    ("3_seam_full",   "current design + miter seam",
     dict(seam=True)),
    ("4_freecad_step", "even 3 steps, 10mm ticks + seam",
     dict(profile=FREECAD_PROFILE, tick_style="ten", tick_depth=0.25,
          star=False, seam=True)),
    ("5_wide_front",  "front rim +9mm, no seam",
     dict(front_extra=9.0)),
]

def render(stl_path, out, cam_pos, cam_up, focal=(0, 0, 5), zoom=None):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(str(stl_path))
    reader.Update()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    prop = actor.GetProperty()
    prop.SetColor(0.85, 0.77, 0.60)
    prop.SetAmbient(0.35)
    prop.SetDiffuse(0.8)
    prop.SetSpecular(0.25)
    ren = vtk.vtkRenderer()
    ren.SetBackground(0.15, 0.14, 0.12)
    ren.AddActor(actor)
    key = vtk.vtkLight()
    key.SetPosition(70, -50, 150)
    key.SetFocalPoint(0, 0, 0)
    key.SetIntensity(1.1)
    ren.AddLight(key)
    fill = vtk.vtkLight()
    fill.SetPosition(-90, 70, 60)
    fill.SetFocalPoint(0, 0, 0)
    fill.SetIntensity(0.35)
    ren.AddLight(fill)
    win = vtk.vtkRenderWindow()
    win.SetOffScreenRendering(1)
    win.AddRenderer(ren)
    win.SetSize(760, 760)
    cam = ren.GetActiveCamera()
    cam.SetFocalPoint(*focal)
    cam.SetPosition(*cam_pos)
    cam.SetViewUp(*cam_up)
    if zoom is None:
        ren.ResetCamera()
    else:
        cam.Zoom(zoom)
    ren.ResetCameraClippingRange()
    win.Render()
    img = vtk.vtkWindowToImageFilter()
    img.SetInput(win); img.Update()
    w = vtk.vtkPNGWriter()
    w.SetFileName(str(out)); w.SetInputConnection(img.GetOutputPort()); w.Write()

def sheet(names, kind, out_path):
    cell, label_h, cols = 440, 30, 3
    rows = (len(names) + cols - 1) // cols
    W, H = cols * cell, rows * (cell + label_h)
    canvas = Image.new("RGB", (W, H), (38, 36, 31))
    d = ImageDraw.Draw(canvas)
    for i, name in enumerate(names):
        im = Image.open(BASE / f"{name}_{kind}.png").resize((cell, cell))
        x, y = (i % cols) * cell, (i // cols) * (cell + label_h)
        canvas.paste(im, (x, y))
        d.text((x + 10, y + cell + 8), name, fill=(232, 226, 210))
    canvas.save(out_path)
    print("sheet", out_path)

names = []
for name, _desc, kw in VARIANTS:
    solid = build_case(**kw)
    print(name, "volume", round(solid.volume))
    export_step(solid, str(BASE / f"{name}.step"))
    stl = BASE / f"{name}.stl"
    export_stl(solid, str(stl))
    render(stl, BASE / f"{name}_top.png", (0, 0, 190), (0, 1, 0))
    render(stl, BASE / f"{name}_persp.png", (105, -120, 95), (0, 0, 1))
    # corner close-up (top-down on the front-right corner) to judge the seam;
    # zoom=1.0 is a sentinel to skip ResetCamera and keep the close framing
    render(stl, BASE / f"{name}_corner.png", (56, -56, 62), (0, 1, 0),
           focal=(56, -56, 10), zoom=1.0)
    names.append(name)

sheet(names, "top", BASE / "sheet_top.png")
sheet(names, "persp", BASE / "sheet_persp.png")
sheet(names, "corner", BASE / "sheet_corner.png")
print("done")
