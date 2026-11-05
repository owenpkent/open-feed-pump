"""Rear half of the case, PETG, mm. Drawn in case coordinates: X forward (0 = back face, 26 = split), Y left, Z up. Origin: back face, centre
of the width, bottom. Holds the motor (two ribs), battery bay, encoder post and the AMPS pattern (4 x M4 inserts, 30 across x 38 high).
Everything is Brief v1 (estimated) except the split plane at X=26 and the ribs, posts and bosses, which are first-build choices."""
from build123d import Box, Cylinder, Plane, Pos, Rot, RectangleRounded, extrude

from nlcad.part import Frame, Part

XD = (1, 0, 0)


def shell(x0, x1, w, h, r, wall, back):
    """Rounded-rectangle shell between x0 and x1; closed at x0 by `back` thick, open at x1."""
    out = extrude(Plane.YZ.offset(x0) * Pos(0, h / 2) * RectangleRounded(w, h, r), amount=x1 - x0)
    cav = extrude(Plane.YZ.offset(x0 + back) * Pos(0, h / 2) * RectangleRounded(w - 2 * wall, h - 2 * wall, r - wall), amount=x1 - x0 - back + 1)
    return out - cav


def make(depth=26.0, w=160.0, h=110.0, r=8.0, wall=2.5, boss=(70.0, 10.0, 100.0), amps_y=15.0, amps_z=55.0, amps_dz=19.0, rotor=(42.0, 66.0),
         motor_z=54.5, motor_y=16.0, cb=3.2):
    body = shell(0, depth, w, h, r, wall, wall)
    by, bz0, bz1 = boss
    frames = {"origin": Frame((0, 0, 0)), "motor_seat": Frame((20.0, 32.0, motor_z), z=(0, 1, 0)),  # motor front face centre, shaft toward +Y
              "encoder": Frame((10.7, rotor[0], rotor[1]), z=XD, x=(0, 1, 0))}
    for k, (sy, bz) in enumerate([(-1, bz0), (1, bz0), (-1, bz1), (1, bz1)], 1):
        body += Pos(depth / 2, sy * by, bz) * Rot(0, 90, 0) * Cylinder(4.0, depth)
        body = body - Pos(cb / 2 - 0.5, sy * by, bz) * Rot(0, 90, 0) * Cylinder(3.25, cb + 1)      # counterbore: head sinks below the back face
        frames[f"scr_{k}"] = Frame((cb, sy * by, bz), z=(-1, 0, 0))
    k = 1
    for sy in (-1, 1):
        for sz in (-1, 1):
            y, z = sy * amps_y, amps_z + sz * amps_dz
            body += Pos(4.0, y, z) * Rot(0, 90, 0) * Cylinder(5.0, 3.0)
            body = body - Pos(3.5, y, z) * Rot(0, 90, 0) * Cylinder(2.85, 7.0)      # insert hole, 5.7
            frames[f"amps_{k}"] = Frame((3.5, y, z), z=XD)
            k += 1
    for y in (motor_y - 12.0, motor_y + 12.0):                                       # two ribs the motor back face rests on
        body += Pos(4.25, y, motor_z) * Box(3.5, 2.0, 30.0)
    body += Pos(6.2, rotor[0], 64.5) * Box(7.4, 4.0, 4.0)                           # encoder post, top at X=9.9
    for k, y in enumerate((-32.5, 32.5), 1):
        frames[f"cell_{k}"] = Frame((11.75, y, 11.75), z=(0, 1, 0))
    return Part(shape=body, frames=frames, density_kg_m3=1270, material="PETG", provenance="estimated",
                bom={"description": "Case, rear half, printed PETG, 2.5 mm walls", "source": "estimated: Brief v1"})
