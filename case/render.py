# Preview renderer for model_case.py output.
# Reads output/minimap_case.stl (STL on purpose: the GLTF reader path renders
# blank PNGs in this environment) and writes preview_top.png / preview_persp.png
# into output/. Run headless: xvfb-run python render.py
from pathlib import Path
import vtk

BASE = Path(__file__).parent / "output"

def render(out, cam_pos, cam_up):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(str(BASE / "minimap_case.stl"))
    reader.Update()
    print("points:", reader.GetOutput().GetNumberOfPoints())
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
    win.SetSize(900, 900)
    cam = ren.GetActiveCamera()
    cam.SetFocalPoint(0, 0, 5)
    cam.SetPosition(*cam_pos)
    cam.SetViewUp(*cam_up)
    ren.ResetCamera()
    ren.ResetCameraClippingRange()
    win.Render()
    img = vtk.vtkWindowToImageFilter()
    img.SetInput(win); img.Update()
    w = vtk.vtkPNGWriter()
    w.SetFileName(str(out)); w.SetInputConnection(img.GetOutputPort()); w.Write()
    print("rendered", out)

render(BASE / "preview_top.png", (0, 0, 190), (0, 1, 0))
render(BASE / "preview_persp.png", (105, -120, 95), (0, 0, 1))
