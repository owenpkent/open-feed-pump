"""The Brief's "Numbers to check", measured on the exact B-rep (not the tessellation) from the project's own parts.

Run from the repo root:
  PYTHONPATH=/w/dev/nl-cad uv run --project /w/dev/nl-cad python projects/feed-pump/tools/brief_numbers.py
Read-only: it builds the assembly in memory and prints. The tessellated cross-checks live in assembly.yaml `checks:`
(squeeze_gap, door_pin_reach, pinch_*). Millimetres.
"""
import math
import sys
from pathlib import Path

from build123d import Axis, GeomType

from nlcad import assembly
from nlcad.geometry import part_mass

ROOT = Path(__file__).resolve().parents[1]
asm = assembly.load(ROOT)
I = asm.by_path()
AX = (41.5, 42.0, 66.0)           # rotor axis point, world_frames.rotor_axis (+X)


def vol(a, b):
    c = a.intersect(b)
    return 0.0 if c is None else sum(s.volume for s in c.solids())


def rot(shape, origin, direction, deg):
    return shape.rotate(Axis(origin, direction), deg)


def main():
    # 1. envelope (door shut), the tube stands 15 below by design
    bbs = [i.shape.bounding_box() for i in asm.instances if "tube" not in i.path]
    lo = [min(b.min.X for b in bbs), min(b.min.Y for b in bbs), min(b.min.Z for b in bbs)]
    hi = [max(b.max.X for b in bbs), max(b.max.Y for b in bbs), max(b.max.Z for b in bbs)]
    tube = I["cassette/tube"].shape.bounding_box()
    print(f"envelope without tube: {hi[0]-lo[0]:.2f} x {hi[1]-lo[1]:.2f} x {hi[2]-lo[2]:.2f} (limit 58 x 160 x 110); tube lowest Z {tube.min.Z:.1f}")
    # 2. mass
    print(f"mass: {sum(part_mass(i.part) for i in asm.instances) * 1000:.1f} g (limit 600)")
    # 3. squeeze gap at the arc wall, and a roller at the wall at every rotor angle
    cas = I["cassette/cassette"].shape
    wall_in = [f for f in cas.faces().filter_by(GeomType.CYLINDER) if abs(f.radius - 20.0) < 1e-6 and abs(f.bounding_box().min.X - 44.0) < 0.01]
    assert len(wall_in) == 1, wall_in
    rollers = [I[f"rotor_grp/roller_{k}"].shape for k in (1, 2, 3)]
    start = [90, 210, 330]                                       # roller angles at rest, degrees from +Y toward +Z
    gaps, margin = [], []
    for a in range(0, 360, 3):
        best, deep = None, -1.0
        for r, s in zip(rollers, start):
            th = (s + a) % 360
            if th <= 180:
                g = min(rot(r, AX, (1, 0, 0), a).distance_to(f) for f in wall_in)
                best = g if best is None else min(best, g)
                deep = max(deep, min(th, 180 - th))
        gaps.append(best)
        margin.append(deep)
    print(f"squeeze gap at the arc wall, rollers inside the wrap, every 3 deg of rotor angle: min {min(gaps):.4f} max {max(gaps):.4f} (target 2.7)")
    print(f"a roller is inside the 0 to 180 wrap at {sum(1 for m in margin if m >= 0)} of {len(margin)} angles; the deepest roller is at least "
          f"{min(margin):.0f} deg from either wall end at the worst angle")
    # 4. door pin reaches the pinch lever when shut; lever closed, pin pushes it open
    door, lever = I["door/door"].shape, I["cassette/lever"].shape
    piv = I["cassette/lever"].frame_world("pivot")[:3, 3]
    print(f"door pin to lever ramp, door shut, lever open: gap {door.distance_to(lever):.3f} mm")
    for q in (-24, -15, -10, -5, 0):
        print(f"  lever at {q:+d} deg: pin x lever overlap {vol(door, rot(lever, tuple(piv), (1, 0, 0), q)):.2f} mm3")
    tube_s = I["cassette/tube"].shape
    anvil = [f for f in cas.faces() if abs(f.bounding_box().min.Y - 62.0) < 0.01 and abs(f.bounding_box().max.Y - 62.0) < 0.01 and f.bounding_box().min.Z < 20]
    closed = rot(lever, tuple(piv), (1, 0, 0), -24)           # pinch joint lower limit
    closed_gap = min(closed.distance_to(f) for f in anvil)
    open_gap = lever.distance_to(tube_s)
    print(f"pinch closed (-24 deg): jaw to anvil face {closed_gap:.2f} mm, limit at most 2.2: {'PASS' if closed_gap <= 2.2 else 'FAIL'}; jaw into the uncompressed tube {vol(closed, tube_s):.1f} mm3")
    print(f"pinch open: lever to tube {open_gap:.2f} mm, limit at least 1.0: {'PASS' if open_gap >= 1.0 else 'FAIL'}")
    # 5. door swing clear of everything, 0 to 102.5 degrees (100 plus 2.5 overtravel)
    hinge = (55.0, 77.5, 56.0)
    swing = [I["door/door"].shape, I["door/latch"].shape]
    others = [i for i in asm.instances if not i.path.startswith("door/") and "hinge_" not in i.path]
    worst = {}
    for a in (0, 10, 20, 30, 45, 60, 80, 90, 95, 100, 102.5):
        min_gap = 1e9
        ov, who = 0.0, []
        for s in swing:
            m = rot(s, hinge, (0, 0, 1), a)
            bb = m.bounding_box()
            for o in others:
                ob = o.shape.bounding_box()
                if ob.min.X > bb.max.X + 1 or ob.max.X < bb.min.X - 1 or ob.min.Y > bb.max.Y + 1 or ob.max.Y < bb.min.Y - 1:
                    continue
                v = vol(m, o.shape)
                ov += v
                if v > 1e-6:
                    who.append(f"{o.path} {v:.1f}")
                g = m.distance_to(o.shape)
                if g > 1e-6 and g < min_gap:
                    min_gap = g
        worst[a] = (ov, min_gap, who)
    for a, (ov, g, who) in worst.items():
        print(f"  door {a:5.1f} deg: overlap with the rest {ov:.3f} mm3 {who}, nearest non-touching part {'none within 1 mm (the hinge line touches the case face by design)' if g > 1e8 else f'{g:.2f} mm'}")


if __name__ == "__main__":
    sys.exit(main())
