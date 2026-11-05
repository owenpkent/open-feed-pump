"""Pinch lever (hazard H1), PETG, mm: a 4 x 14.4 arm beside a 6.6 mm hub that squeezes the outlet leg against the cassette anvil, with a long shallow ramped tab (overhanging the arm on its low side) the
door pin pushes. Local Z is the pivot axis (out of the front of the pump), X is +Y of the pump, Y is +Z of the pump. Origin: the pivot axis, mid-width.
As modelled (door shut) the lever is open, jaw face 1.2 from the round tube; turning it -24 degrees about +Z closes the jaw to a 2.05 gap against the
anvil (Brief: at most 2.2 closed, at least 1.0 open, about 5.2 travel; here 5.45). Pivot 3.6 off the jaw face so the hub (3.3 radius) clears the tube by 1.5 and the case floor by 1.2. Estimated (first-build choice). Frame: pivot."""
from build123d import Box, Cylinder, Polygon, Pos, Rot, extrude

from nlcad.part import Frame, Part


def make(arm_w=4.0, arm_l=14.4, arm_off=3.6, width=8.0, hub_r=3.3, bore=3.2, tab=(9.4, 14.4), ramp=((-4.4, 6.8), (3.6, 4.0))):
    hub = Cylinder(hub_r, width)
    arm = Pos(arm_off - arm_w / 2, arm_l / 2, 0) * Box(arm_w, arm_l, width)        # jaw face 3.6 from the axis, so the hub (3.5 radius) clears the tube
    (x0, z0), (x1, z1) = ramp                                                         # ramp: z falls from z0 at x0 to z1 at x1
    wedge = extrude(Polygon((x0, width / 2 - 0.5), (x0, z0), (x1, z1), (x1, width / 2 - 0.5), align=None), amount=tab[1] - tab[0])
    wedge = Rot(90, 0, 0) * wedge
    wedge = Pos(0, tab[0] - wedge.bounding_box().min.Y, 0) * wedge                   # tab spans y = tab[0] to tab[1]
    return Part(shape=hub + arm + wedge - Cylinder(bore / 2, width + 2), frames={"pivot": Frame((0, 0, 0))}, density_kg_m3=1270, material="PETG", provenance="estimated",
                bom={"description": "Pinch lever, printed", "source": "estimated: Brief v1"})
