"""Cylinder stand-in (optionally with a bore) along local Z, mm. Origin: centre; the axis follows the frame it is mated to. Frame: c.
d = outer diameter, l = length, bore = through-bore diameter or 0. All numbers estimated (Brief v1 envelopes)."""
from build123d import Cylinder

from nlcad.part import Frame, Part


def make(d=10.0, l=10.0, bore=0.0, mass_kg=0.005, material="steel", bought=True, vendor="generic", part_number="stand-in",
         description="Cylinder stand-in", source="estimated: brief envelope", provenance="estimated"):
    shape = Cylinder(d / 2, l)
    if bore:
        shape = shape - Cylinder(bore / 2, l + 2)
    return Part(shape=shape, frames={"c": Frame((0, 0, 0))}, mass_kg=mass_kg, material=material, bought=bought, provenance=provenance,
                bom={"vendor": vendor, "part_number": part_number, "description": description, "source": source})
