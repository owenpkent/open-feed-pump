"""Run inside Blender: blender -b -P render_ok.py -- <glb> <manifest.json> <stills dir> <frames dir> <version>

Renders one build in OK Studio's arctic theme (okstudio-style tokens.json, dark mode): two stills, and the frames of a looping
animation that shows the free-flow safety sequence. The rotor runs with the door shut, stops, the door opens and the pinch lever
closes on the tube, then the door shuts, the lever opens and the rotor runs again. The rotor never turns with the door open, because
the pump must not. Angles come from the joints in the manifest, so the animation follows the design. Driven by make_gif.py.
"""
import json
import math
import sys

import bpy
from mathutils import Matrix, Vector

BG, LINE = "#0c1118", "#5d7087"            # tokens.json mode.dark: bg, axis
DOOR_ALPHA = 0.28                          # the door is clear polycarbonate
FRAMES = 150                               # 10 s at 15 fps
RUN_1, OPEN, HOLD, SHUT = 40, 28, 14, 28   # frames per phase; the rest is the second run
PINCH_END = 0.25                           # the lever finishes moving in the first quarter of the door's swing

glb, manifest_path, stills, frames_dir, ver = sys.argv[sys.argv.index("--") + 1:][:5]
man = json.load(open(manifest_path, encoding="utf-8"))
inst_sub = {i["path"]: i["subassembly"] for i in man["instances"]}
subs = {s["id"]: s for s in man["subassemblies"]}
joints = {j["name"]: j for j in man["joints"]}


def linear(h, a=1.0):
    """A hex colour as linear RGBA, with the true sRGB curve: Blender applies its inverse on output, so the render matches the hex."""
    h = h.lstrip("#")
    c = [int(h[k:k + 2], 16) / 255 for k in (0, 2, 4)]
    return tuple(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c) + (a,)


bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
bpy.context.view_layer.update()
objs = {}
for o in bpy.data.objects:
    if o.type == "MESH" and (o.get("path") or o.name) in inst_sub:
        objs[o.get("path") or o.name] = o
assert objs, "no instance meshes found in the GLB"
home = {}
for p, o in objs.items():                  # flatten the import hierarchy so each object's world matrix can be set directly
    mw = o.matrix_world.copy()
    o.parent = None
    o.matrix_world = mw
    home[p] = mw

for p, o in objs.items():
    sid = inst_sub[p]
    m = bpy.data.materials.new(p)
    m.diffuse_color = linear(subs[sid]["color"], DOOR_ALPHA if p == "door/door" else 1.0)
    o.data.materials.clear()
    o.data.materials.append(m)

sc = bpy.context.scene
sc.render.engine = "BLENDER_WORKBENCH"
sc.render.film_transparent = False
sc.display.render_aa = "8"
sh = sc.display.shading
sh.light, sh.color_type = "STUDIO", "MATERIAL"
sh.show_cavity, sh.cavity_type = True, "WORLD"
sh.show_object_outline, sh.object_outline_color = True, linear(LINE)[:3]
sh.background_type, sh.background_color = "VIEWPORT", linear(BG)[:3]
sc.view_settings.view_transform = "Standard"
world = bpy.data.worlds.new("w")
world.color = linear(BG)[:3]
sc.world = world

cam_data = bpy.data.cameras.new("cam")
cam_data.type = "ORTHO"
cam_data.clip_start, cam_data.clip_end = 0.05, 30
cam = bpy.data.objects.new("cam", cam_data)
sc.collection.objects.link(cam)
sc.camera = cam

corners = [o.matrix_world @ Vector(c) for o in objs.values() for c in o.bound_box]
centre = sum(corners, Vector()) / len(corners)
radius = max((c - centre).length for c in corners)


def point_camera(d, scale):
    d = Vector(d).normalized()
    u = Vector((0, 0, 1))
    u = (u - u.dot(d) * d).normalized()
    r = u.cross(d).normalized()
    pos = centre + d * 6.0
    cam.matrix_world = Matrix(((r.x, u.x, d.x, pos.x), (r.y, u.y, d.y, pos.y), (r.z, u.z, d.z, pos.z), (0, 0, 0, 1)))
    cam_data.ortho_scale = scale


def turn(name, angle):
    j = joints[name]
    o = Vector(j["origin"])
    return Matrix.Translation(o) @ Matrix.Rotation(angle, 4, Vector(j["axis"])) @ Matrix.Translation(-o)


def pose(rotor=0.0, door=0.0, pinch=0.0):
    """Angles in radians. Children of the rotor and door move with their parent; the lever and spring turn on the cassette."""
    rr = turn("rotor", rotor)
    dd = turn("door", door)
    pp = turn("pinch", pinch)
    for p, o in objs.items():
        m = Matrix.Identity(4)
        if p.startswith("rotor_grp/"):
            m = rr
            if "roller_" in p:             # the rollers roll on the tube, opposite to the rotor
                m = rr @ turn(p.split("/")[1], -rotor * 2.5)
        elif p.startswith("door/"):
            m = dd
        elif p == "cassette/lever":
            m = pp
        o.matrix_world = m @ home[p]
    bpy.context.view_layer.update()


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


door_open = joints["door"]["range"][1] * 0.95
lo, hi = joints["pinch"]["range"]
pinch_closed = lo if abs(lo) > abs(hi) else hi
RUN_2 = FRAMES - RUN_1 - OPEN - HOLD - SHUT


def timeline(f):
    """Pose and caption at frame f. The rotor makes one whole turn across both run phases, so the loop is seamless."""
    t_open_start = RUN_1
    t_shut_start = RUN_1 + OPEN + HOLD
    t_run2_start = t_shut_start + SHUT
    if f < t_open_start:
        rotor, s, cap = (f / (RUN_1 + RUN_2)), 0.0, "RUNNING"
    elif f < t_shut_start:
        rotor, s, cap = (RUN_1 / (RUN_1 + RUN_2)), ease((f - t_open_start) / OPEN), "DOOR OPEN: MOTOR OFF, TUBE PINCHED"
    elif f < t_run2_start:
        rotor, s, cap = (RUN_1 / (RUN_1 + RUN_2)), 1 - ease((f - t_shut_start) / SHUT), "DOOR SHUTTING: PIN OPENS THE PINCH"
    else:
        rotor, s, cap = ((RUN_1 + f - t_run2_start) / (RUN_1 + RUN_2)), 0.0, "RUNNING"
    return rotor * 2 * math.pi, s * door_open, ease(s / PINCH_END) * pinch_closed, cap


# Stills
sc.render.resolution_x, sc.render.resolution_y = 1280, 800
sc.render.image_settings.file_format = "JPEG"
sc.render.image_settings.quality = 92
for name, d in (("iso", (1, 0.75, 0.55)), ("front", (1, 0, 0.0001))):
    pose()
    point_camera(d, radius * 2.6)
    sc.render.filepath = f"{stills}/ok_{name}_v{ver}.jpg"
    bpy.ops.render.render(write_still=True)
pose(door=door_open, pinch=pinch_closed)
point_camera((1, -0.45, 0.45), radius * 3.0)
sc.render.filepath = f"{stills}/ok_door_open_v{ver}.jpg"
bpy.ops.render.render(write_still=True)

# Animation frames
sc.render.resolution_x, sc.render.resolution_y = 800, 500
sc.render.image_settings.file_format = "PNG"
captions = []
for f in range(FRAMES):
    rotor, door, pinch, cap = timeline(f)
    pose(rotor, door, pinch)
    az = -0.12 + 0.42 * math.cos(2 * math.pi * f / FRAMES)  # sways between the two sides and returns, for a seamless loop
    point_camera((1, az, 0.42), radius * 2.6)
    sc.render.filepath = f"{frames_dir}/f{f:04d}.png"
    bpy.ops.render.render(write_still=True)
    captions.append(cap)
json.dump(captions, open(f"{frames_dir}/captions.json", "w", encoding="utf-8"))
