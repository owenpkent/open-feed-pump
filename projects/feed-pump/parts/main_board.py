"""Main board stand-in, mm: 100 x 60 x 1.6 PCB plus 8 mm of components on the back side. Local X is the board normal (front face +X).
Origin: centre of the PCB. Frame: c. PCB size from Brief v1 (estimated); components modelled as one 90 x 38 block (smaller than the board so the corner
notches and screw bosses clear); two 12 x 10 corner notches on the -Y edge. Mass 0.036 kg is an estimate (PCB 18 g, parts 18 g)."""
from build123d import Box, Pos

from nlcad.part import Frame, Part


def make(h=100.0, w=60.0, t=1.6, comp_h=8.0, comp_hh=90.0, comp_w=38.0, notch=(12.0, 10.0)):
    shape = Box(t, w, h) + Pos(-(t + comp_h) / 2, 0, 0) * Box(comp_h, comp_w, comp_hh)
    for sz in (-1, 1):                                                              # corner notches on the -Y edge clear the case screw bosses
        shape -= Pos(0, -w / 2 + notch[0] / 2 - 0.5, sz * (h / 2 - notch[1] / 2 + 0.5)) * Box(t + 20, notch[0] + 1, notch[1] + 1)
    return Part(shape=shape, frames={"c": Frame((0, 0, 0))}, mass_kg=0.036, material="fr4", bought=True, provenance="estimated",
                bom={"vendor": "generic", "part_number": "main board", "description": "Main PCB stand-in", "source": "estimated: Brief v1"})
