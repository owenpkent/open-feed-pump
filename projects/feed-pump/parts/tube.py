"""Silicone tube 3.2 ID x 6.4 OD, mm, modelled uncompressed: inlet leg up, 180 degree wrap over the rotor, outlet leg down.
Local Z is out of the front of the pump, X is +Y of the pump, Y is +Z of the pump. Origin: rotor axis, tube centre plane.
Centre-line radius 16.8, so the outer surface (20.0) just meets the cassette arc wall. Legs run 81 mm below the axis (to 15 mm under the case).
Numbers are Brief v1 (estimated). Frame: top (centre line over the rotor)."""
from build123d import BuildLine, Circle, CenterArc, Line, Plane, sweep

from nlcad.part import Frame, Part


def make(od=6.4, idia=3.2, r=16.8, leg=81.0):
    with BuildLine() as p:
        Line((-r, -leg), (-r, 0))
        CenterArc((0, 0), r, 180, -180)
        Line((r, 0), (r, -leg))
    prof = Plane(origin=(-r, -leg, 0), z_dir=(0, 1, 0)) * (Circle(od / 2) - Circle(idia / 2))
    return Part(shape=sweep(prof, path=p.wire()), frames={"top": Frame((0, r, 0))}, density_kg_m3=1100, material="silicone",
                provenance="estimated", bought=True,
                bom={"vendor": "generic", "part_number": "silicone tube 3.2 x 6.4", "description": "Silicone tube, 3.2 ID x 6.4 OD (medical grade needed)",
                     "source": "estimated: Brief v1"})
