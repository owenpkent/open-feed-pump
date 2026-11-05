"""Door, clear polycarbonate, 3 thick, mm. Local axes follow the case (X forward, Y left, Z up). Origin: hinge pin axis at the back face, mid-height.
Covers the bay: 75.5 wide (to the free edge), 103 high (Z 3 to 106). Carries the pinch-lever pin (3 dia, 2 proud of the back face), a half-round notch at each of the two
3 mm steel hinge pin stubs (top and bottom, so the cassette can leave between them), a notch for the latch slider and two slots for the tube legs at the bottom edge. Hinge at Y=77.5 and X=55 (Brief said about 78 and 58: a 3 mm pin at X=58 would stand outside the 58 deep envelope);
the hinge edge is bevelled 14 degrees so it clears the case wall up to 102.5 degrees.
Numbers estimated (Brief v1) except the notch, slot and pin positions, which are first-build choices.
Frames: hinge, latch (latch slider axis, bottom of travel), pin_tip."""
from build123d import Box, Cylinder, Plane, Polygon, Pos, Rot, extrude

from nlcad.part import Frame, Part


def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def make(t=3.0, w=75.5, h=103.0, z_lo=-53.0, pin_d=3.0, pin_proud=2.0, pin_at=(-24.46, -29.5), hinge_r=1.55,
         latch_notch=(-75.5, -69.6, -13.0, 15.0), latch_at=(1.5, -72.55, -1.0), slots=(-52.3, -18.7), slot_w=8.8, slot_h=8.0, bevel=0.75):
    body = bx(0, t, -w, 0, z_lo, z_lo + h)
    cut = Pos(0, 0, 46.0) * Cylinder(hinge_r, 8.4) + Pos(0, 0, -50.0) * Cylinder(hinge_r, 6.4)    # notches for the two pin stubs
    wedge = extrude(Polygon((0, 0), (t + 0.2, 0), (t + 0.2, -bevel), align=None), amount=h + 2)     # bevel the hinge edge so it clears the case to 102.5 degrees
    cut += Pos(0, 0, z_lo + h / 2 - (wedge.bounding_box().min.Z + wedge.bounding_box().max.Z) / 2) * wedge
    y0, y1, z0, z1 = latch_notch
    cut += bx(-1, t + 1, y0 - 1, y1, z0, z1)
    for sy in slots:
        cut += bx(-1, t + 1, sy - slot_w / 2, sy + slot_w / 2, z_lo - 1, z_lo + slot_h)
    py, pz = pin_at
    body = body - cut + Pos(-pin_proud / 2 + 0.2, py, pz) * Rot(0, 90, 0) * Cylinder(pin_d / 2, pin_proud + 0.4)
    return Part(shape=body, frames={"hinge": Frame((0, 0, 0)), "latch": Frame((*latch_at,)), "pin_tip": Frame((-pin_proud, py, pz), z=(-1, 0, 0))},
                density_kg_m3=1200, material="PC", provenance="estimated",
                bom={"description": "Door, clear polycarbonate 3 mm, with pinch pin", "source": "estimated: Brief v1"})
