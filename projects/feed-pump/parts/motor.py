"""NEMA 11 stepper stand-in, mm: body 28 x 28 x 32 and a 5 mm shaft, 20 long. Local Z is the shaft axis.
Origin: centre of the front face, body toward -Z, shaft toward +Z. Frames: face (front face, z out), worm_seat (shaft, 10 from the face).
Sizes from Brief v1 (estimated); mass 0.11 kg is an estimate (typical NEMA 11, 32 mm)."""
from build123d import Box, Cylinder, Pos

from nlcad.part import Frame, Part


def make(w=28.0, body=32.0, shaft_d=5.0, shaft_l=20.0, worm_at=10.0):
    shape = Pos(0, 0, -body / 2) * Box(w, w, body) + Pos(0, 0, shaft_l / 2) * Cylinder(shaft_d / 2, shaft_l)
    return Part(shape=shape, frames={"face": Frame((0, 0, 0)), "worm_seat": Frame((0, 0, worm_at))}, mass_kg=0.11, material="steel",
                bought=True, provenance="estimated",
                bom={"vendor": "generic", "part_number": "NEMA11 28x28x32", "description": "NEMA 11 stepper, 5 mm shaft", "source": "estimated: Brief v1"})
