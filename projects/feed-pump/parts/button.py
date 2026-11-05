"""Silicone keypad button, mm. Local Z is out of the front face. Origin: the front face of the case (cap back).
Cap 16 across x 2 high stands proud; stem 6 across x 7.5 long goes back through the wall. Sizes from Brief v1 (at least 15 across), estimated."""
from build123d import Cylinder, Pos

from nlcad.part import Frame, Part


def make(cap_d=16.0, cap_h=2.0, stem_d=6.0, stem_l=7.5):
    shape = Pos(0, 0, cap_h / 2) * Cylinder(cap_d / 2, cap_h) + Pos(0, 0, -stem_l / 2 + 0.01) * Cylinder(stem_d / 2, stem_l)
    return Part(shape=shape, frames={"seat": Frame((0, 0, 0))}, density_kg_m3=1100, material="silicone", provenance="estimated",
                bom={"description": "Silicone keypad button", "source": "estimated: Brief v1"})
