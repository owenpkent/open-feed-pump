"""Rotor, steel, mm: 5 mm shaft, 30 mm hub disc and three roller pins on a 13.3 radius, 120 degrees apart. Local Z is the rotor axis, out of the
front of the pump; X is +Y of the pump, Y is +Z of the pump. Origin: rotor axis at the back of the hub (X=41.5 in the pump).
Shaft runs 26.5 behind the hub (to X=15). Numbers are Brief v1 (estimated); hub size and pin length are first-build choices.
Frames: axis, pin_1..3 (roller centre, at hub + 6.5), wheel_seat (worm wheel centre), magnet_seat (magnet centre, behind the shaft end)."""
import math

from build123d import Cylinder, Pos

from nlcad.part import Frame, Part


def make(shaft_d=5.0, shaft_back=26.5, hub_r=15.0, hub_t=2.5, pin_d=3.0, pin_len=9.0, pitch_r=13.3, roller_z=6.5, wheel_z=-21.5, magnet_h=2.5):
    shape = Pos(0, 0, (hub_t - shaft_back) / 2) * Cylinder(shaft_d / 2, hub_t + shaft_back) + Pos(0, 0, hub_t / 2) * Cylinder(hub_r, hub_t)
    frames = {"axis": Frame((0, 0, 0)), "wheel_seat": Frame((0, 0, wheel_z)), "magnet_seat": Frame((0, 0, -shaft_back - magnet_h / 2))}
    for k, a in enumerate((90, 210, 330), 1):
        x, y = pitch_r * math.cos(math.radians(a)), pitch_r * math.sin(math.radians(a))
        shape += Pos(x, y, hub_t - 0.5 + pin_len / 2) * Cylinder(pin_d / 2, pin_len)
        frames[f"pin_{k}"] = Frame((x, y, roller_z))
    return Part(shape=shape, frames=frames, density_kg_m3=7850, material="steel", provenance="estimated",
                bom={"description": "Rotor shaft with hub and three roller pins", "source": "estimated: Brief v1"})
