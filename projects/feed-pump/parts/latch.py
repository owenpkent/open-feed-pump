"""Door latch slider, PETG, mm: a 5.5 x 20 x 3 block in the door's free edge notch with a 2.6 x 2.5 tongue that goes back into the case catch pocket.
Local Z is the slide axis (up). Origin: block centre. Slides up 6 mm. The hook that would hold the tongue is not modelled yet (see BUILD_LOG).
Numbers estimated (Brief v1: single push, about 6 mm); size and tongue are first-build choices. Frame: slide."""
from build123d import Box, Pos

from nlcad.part import Frame, Part


def make(w=5.5, h=20.0, t=3.0, tongue=(2.6, 2.5), tongue_dy=-3.1):
    shape = Box(t, w, h) + Pos(-(t + tongue[1]) / 2 + 0.01, tongue_dy + tongue[0] / 2 + 0.0, 0) * Box(tongue[1], tongue[0], h)
    return Part(shape=shape, frames={"slide": Frame((0, 0, 0))}, density_kg_m3=1270, material="PETG", provenance="estimated",
                bom={"description": "Door latch slider, printed", "source": "estimated: Brief v1"})
