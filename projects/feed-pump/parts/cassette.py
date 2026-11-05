"""Cassette (the open consumable), PETG, mm: 70 W x 80 H x 14 D plate with rotor cut-out, rigid arc wall of 20.0 radius, sensor windows,
pinch-lever pivot post and anvil, two snap tabs. Local Z is out of the front of the pump, X is +Y of the pump, Y is +Z of the pump.
Origin: the rotor axis at the back face of the plate (X=41 in the pump). Numbers are Brief v1 (estimated); details (post, anvil, tabs) are first-build choices.
Frames: foot (plate back, bottom centre), tube_top (tube centre line over the rotor), lever_pivot, spring_seat, anvil_face (a point on the anvil face the lever closes onto)."""
from build123d import Box, Circle, Cylinder, Pos, Rot, extrude, Plane

from nlcad.part import Frame, Part


def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def make(w=70.0, bottom=-56.0, top=24.0, t=3.0, depth=14.0, arc_r=20.0, arc_t=3.0, leg_dy=16.8, tube_z=7.0, wall_z=(3.0, 11.0),
         p_up=(-16.8, -24.0), p_dn=(16.8, -32.0), air=(16.8, -21.0), pin=(8.8, -52.0), anvil=(20.0, 23.0, -52.0, -37.5)):
    plate = bx(-w / 2, w / 2, bottom, top, 0, t)
    cut = Cylinder(arc_r, 12.0)                                                       # rotor cut-out, same radius as the arc wall
    for (x, y), (sx, sy) in ((p_up, (10, 10)), (p_dn, (10, 10)), (air, (16, 12))):    # sensor windows
        cut += bx(x - sx / 2, x + sx / 2, y - sy / 2, y + sy / 2, -1, t + 1)
    z0, z1 = wall_z
    ring = Pos(0, 0, (z0 + z1) / 2) * (Cylinder(arc_r + arc_t, z1 - z0) - Cylinder(arc_r, z1 - z0 + 2)) - bx(-40, 40, -40, 0, 0, 20)   # top half
    body = plate - cut
    body += ring
    for s in (-1, 1):                                                                 # straight continuations of the wall down the legs
        body += bx(*sorted((s * arc_r, s * (arc_r + arc_t))), -14.0, 0.2, z0, z1)
    ax0, ax1, ay0, ay1 = anvil
    body += bx(ax0, ax1, ay0, ay1, z0, z1)
    px, py = pin
    body += Pos(px, py, 7.5) * Cylinder(1.5, 11.0)                                    # lever pivot post, z 2 to 13
    for s in (-1, 1):                                                                 # snap tabs: cantilever strip with a hook
        body += bx(s * 27 - 3, s * 27 + 3, top - 0.5, top + 6, 0.5, 1.7) + bx(s * 27 - 3, s * 27 + 3, top + 4, top + 6, 1.7, 2.9)
    return Part(shape=body, frames={"foot": Frame((0, bottom, 0)), "tube_top": Frame((0, leg_dy, tube_z)),
                                    "lever_pivot": Frame((px, py, tube_z)), "anvil_face": Frame((anvil[0], (anvil[2] + anvil[3]) / 2, tube_z)), "spring_seat": Frame((px, py, 11.75))},
                density_kg_m3=1270, material="PETG", provenance="estimated",
                bom={"description": "Cassette plate, printable or moulded, single use", "source": "estimated: Brief v1"})
