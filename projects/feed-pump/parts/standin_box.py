"""Box stand-in for a bought or minor part, mm. Origin: centre; axes follow the frame it is mated to. Frame: c.
size = (x, y, z) envelope. notch = (depth, width): a slot cut into the +X face, centred in Y, through all of Z (optical sensor U).
All numbers estimated (Brief v1 envelopes); mass is an estimate unless the caller says otherwise."""
from build123d import Box, Pos

from nlcad.part import Frame, Part


def make(size=(10, 10, 10), mass_kg=0.005, material="plastic", vendor="generic", part_number="stand-in", description="Box stand-in",
         source="estimated: brief envelope", notch=None, provenance="estimated"):
    sx, sy, sz = size
    shape = Box(sx, sy, sz)
    if notch:
        d, w = notch
        shape = shape - Pos(sx / 2 - d / 2 + 0.5, 0, 0) * Box(d + 1, w, sz + 2)
    return Part(shape=shape, frames={"c": Frame((0, 0, 0))}, mass_kg=mass_kg, material=material, bought=True, provenance=provenance,
                bom={"vendor": vendor, "part_number": part_number, "description": description, "source": source})
