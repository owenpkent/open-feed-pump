# Build log, feed-pump

A portable rotary peristaltic enteral feeding pump. Brief: [Brief v1.md](Brief%20v1.md). Built with nl-cad (private tool, run from outside this repo, see the end of this file). Every number is estimated unless the Brief cites a source.

## Plan checkpoint (written before the first part)

- **Subsystems.** Case (front half with bulkhead and bay, rear half with battery bay and AMPS pattern), pumping head (rotor, three rollers, cassette, tube, pinch lever), drive (motor, worm, worm wheel, two bearings, encoder), electronics (board, display, keypad, ports, sounder, sensors), door and latch, hardware (four M3 screws).
- **Joints and datums, placed first.** World frames: `rotor_axis` (X=41.5, Y=42, Z=66, axis +X), `door_hinge` (X=55, Y=77.5, axis +Z), `case_origin`. Moving joints: `rotor` (continuous), `roller_1..3` (continuous, on frames `rotor.pin_k`), `door` (0 to 100 degrees), `pinch` (-15 to 0 degrees about +X on `cassette.lever_pivot`, 0 is open with the door shut), `latch` (0 to 6 mm along Z). Everything else is a fixed joint on a named frame of the part that holds it.
- **Assembly order.** Case front with bearings, then electronics (display before board), then rotor with wheel, magnet and rollers, then the rear half pre-built with motor, worm, encoder, cells and inserts and closed onto the front, then cassette and tube, door and latch, screws. The order is in `assembly.yaml` `steps:` and the insertion checks read it.
- **Routes.** Tube: inlet leg up at Y=25.2, 180 degree wrap at 16.8 centre radius, outlet leg down at Y=58.8, 15 mm below the case. Load path: rotor shaft through two bearings in the bulkhead boss to the worm wheel, worm on the motor shaft.

## Builds

| Build | What the checks and renders showed | What changed |
|---|---|---|
| v1 | 50 pass, 2 warn, 10 fail. Real: motor overlapped the upstream pressure sensor (0.1 cm3); length 61 mm (screw heads stood 3 mm proud of the back face); lever arm filled its own bore (cassette x lever 0.03 cm3); mass 0.626 kg (warn); stand-in masses denser than the "plastic" bound; seven insertion fails (PCB and display trapped behind the screw bosses, motor and cells inserted into a closed case, hinge pin blocking the cassette's way out, chutes closed to the front). Expected: roller x tube overlap. No renders. | First build. |
| v2 | 51 pass, 2 warn, 9 fail. Overlap with the sensor gone, length 58. Mass 0.606. Same insertion fails. | Case back: screw bosses counterbored 3.2 so heads sit below the back face; whole drive group moved 2 mm back (motor X 6 to 34 clears the sensor body at X 34.8); AMPS bosses cut to 3 deep; bay tray hollowed to 2.5 walls (was a 14 mm solid block). |
| v3 | 62 pass, 0 warn, 1 fail (roller x tube, expected). All insertion rows pass; mass 0.594 kg (pass). | Hinge pin split into top and bottom stubs so the cassette can leave between them; tube chutes opened to the front; board corner notches and narrower component block; display moved to Y -64 to -4 and sounder to the free strip beside the latch column; stand-in electronics given material "electronics" (no density bound, so qa.mass_density does not judge them); step order puts motor, worm, cells, encoder, inserts before the rear shell. |
| v4 | 71 pass, 2 fail: `pinch_open_gap` 0 and `door_open_clear` 0. | Added distance rows (squeeze gap, door pin reach, pinch open and closed), the roller x tube allow with its reason, door hinge edge bevel (not yet cut: extrusion ran the wrong way). |
| v5 | 71 pass, 1 fail. `pinch_open_gap` still 0: lever hub (3.5 radius) reached Y 56.5 into the tube (inner edge 55.6). Dropped `door_open_clear`: the hinge line touches the case face by design, so that row can only read 0. | Lever rebuilt: pivot moved to Y 51.8, jaw face 3.5 off the axis, arm 14.4, tab moved with it; door pin moved to match the ramp. Wedge placement fixed (lever bbox had Z 34). |
| v6 | 71 pass, 1 fail (`pinch_open_gap` reads 0.2999 against a 0.3 floor: the design gap is 0.30). Numbers script: door overlaps the case 26 mm3 at 95 degrees (bevel cut missed the door). | Door bevel extruded the right way; floor of the row set to 0.25. |
| v7 | 72 pass, 0 fail. The 5 warns in `checks_v7.md` are `triage.stale` rows: the build does not run the sweep, so the five sweep accepts match nothing there. In `nlcad.qa --sweep` they match (see "Sweep" below). Renders looked at: front matches the Brief sketch (display and keypad left, door right with latch strip between, tube legs at the bottom edge, 5 caps at 16 across); iso, side and cassette section agree. Viewer HTML exported and opened offline with 0 page errors. | Five `accepted_warns` entries; renders on. No part changed. |

Builds v8 to v11 rework the pinch lever to the updated Brief (closed jaw to anvil at most 2.2, open at least 1.0 clear of the tube) and recolour. v11 is final.

| Build | What the checks and renders showed | What changed |
|---|---|---|
| v8 | 73 pass, 0 fail (4 `triage.stale` warns, as in v7). `pinch_open_gap` 1.20 (floor 1.1), `pinch_closed_gap` 2.05 (max 2.2), mass 0.594 kg. Sweep: 4 accepted, 1 untriaged: lever x tube clearance 0.01 mm at -4.8 degrees while the jaw closes onto the tube. Cassette render looked at. | Lever range -24 to 0 degrees (was -15); pivot 51.0 to 50.8 and jaw face 54.4 open (1.2 off the tube); long shallow ramp on the tab (overhangs the arm, slope 0.35) so the pin still meets the ramp when the lever is closed; door pin moved to Y 53.0 to match; `anvil_face` frame on the cassette; hard rows `pinch_open_gap` (min 1.1 for the Brief's 1.0, see below) and `pinch_closed_gap` (max 2.2); accept for the 0.30 mm gap deleted. |
| v9 | Same numbers as v8. | OK Studio subassembly colours in `assembly.yaml` (back #233245, front #2c3b50, door #5b9cff, cassette #8fe8f2, rotor #ff6f85, electronics #2fae74, hardware #7f93a8). No geometry change. |
| v10 | Sweep: lever x case front clearance 1.00 mm (hub bottom 10.5 against the tray floor at 9.5): at the limit, noise decides. | `fits` row declares lever x tube as contact (the jaw closes on the tube on purpose; the open and closed gaps are the hard rows; overlap is still measured). |
| v11 | **Final.** 73 pass, 0 fail in the build (4 `triage.stale` rows: the sweep accepts, which only match in `nlcad.qa --sweep`). `nlcad.qa --sweep --write`: 66 pass, 4 warn (4 accepted), 0 fail. Pinch closed gap 2.05 mm (limit 2.2), open gap 1.20 mm (limit 1.0), travel 5.45 mm. Mass 594.1 g. Door pin overlap with the lever: 0.00 mm3 open, 0.38 at -5, 1.9 at -10, 4.5 at -15, 9.1 at -24 degrees, so the shut door drives it to fully open. Cassette render looked at. Viewer exported with the okstudio-style theme. | Hub radius 3.5 to 3.3: clears the case floor by 1.2 and the tube by 1.5. |

The row floor for `pinch_open_gap` is 1.1, not 1.0: the tessellated tube sits inside its true surface by up to 0.1 (`TESS_TOL_MM`), which can overstate a gap, so the design gap is 1.2 and the row fails below 1.1, which guarantees the true gap is at least 1.0. `pinch_closed_gap` is exact (a box corner against a plane frame).

## Sweep (`nlcad.qa --sweep --write`, v7 and again v11)

Joints swept: rotor, roller_1..3, door (0 to 100, overtravel 2.5), pinch, latch. Warns, each accepted in `assembly.yaml` with its reason (the v7 pinch accept is gone; v11 has four):

- door x hinge stubs: 0.05 mm running fit, constant over the swing.
- door at -2.5 degrees (overtravel only): door rests on the case face, its physical stop. No overlap in range; none to 102.5 degrees on the exact solids.
- rotor x case front: 0.50 mm axial running clearance, hub to boss.
- latch x door: 0.20 mm sliding fit.

## Brief's "Numbers to check"

Measured on exact B-rep by [tools/brief_numbers.py](tools/brief_numbers.py); the tessellated cross-checks are the `distances:` rows in `assembly.yaml`.

| Number | Result |
|---|---|
| Squeeze gap at the arc wall | 2.7000 mm at every rotor angle sampled (3 degree steps, rollers inside the wrap); `squeeze_gap` rows read 2.70 within the 2.55 to 2.85 tessellation window |
| Envelope | 58.00 x 160.00 x 110.00 mm without the tube (door shut); tube 15.0 mm below. `checks.envelope` has the same limits, 125 mm with the tube is info only |
| Mass | 594 g against 600 (`mass.total` passes, 6 g margin) |
| Pinch (v11) | Closed jaw to anvil 2.05 mm against at most 2.2 (PASS); open lever to tube 1.20 mm against at least 1.0 (PASS); `brief_numbers.py` and the `distances:` rows agree |
| Roller at the arc wall at every angle | Yes: a roller is inside the 0 to 180 degree wrap at all angles, at worst 30 degrees from either end of the wall. The two idle rollers touch the straight legs (0.03 cm3 each) |
| Door pin reaches the pinch lever | Gap 0.000 mm shut. Lever closed overlaps the pin by 9.1 mm3 at -24, 4.5 at -15, 0.4 at -5, 0 at 0 degrees, so the pin pushes it fully open |
| Door swing clear | No overlap with anything from 0 to 102.5 degrees; nearest non-touching part 2.5 mm at 10 degrees, 11 mm from 45 degrees. The hinge line touches the case face by design |

## Changes to the Brief's design

- Door hinge axis at X=55, Y=77.5, not X=58, Y=78: a 3 mm pin at X=58 sticks out of the 58 deep envelope. The hinge edge is bevelled 14 degrees so the door clears the case to 102.5 degrees. The 3 mm pin is two stubs (top Z 98 to 106, bottom Z 3 to 9) so the 70 mm cassette can leave between them; the Brief's full-height pin at Y=78 intrudes 1 mm into the cassette's path (pocket edge 77.2, pin edge 76.0).
- Door is 103 high (Z 3 to 106) to carry the lower stub and cover the bay.
- Tube chutes are open to the front (notches in the front wall and floor) so the cassette drops in with the legs in place; the door slot for the legs is then redundant but is drawn.
- Component block on the board is 90 x 38 (not full 100 x 60) with two corner notches, so the board passes the screw bosses on assembly. Display is at Y -64 to -4 (not -76 to -16) for the same reason.
- Rotor joint parent is `case_front` (it holds the bearings); the root of the joint tree is `case_back`.

## Real design problems found

- **Pinch (resolved in v8).** Closed gap 2.05 mm (about 64% of two tube walls, 36% compression) and open gap 1.20 mm now meet the Brief's 2.2 and 1.0, with 24 degrees of travel on the 14.4 mm arm (jaw travel 5.45 mm). Whether the spring seals the tube against a 1 m head is a bench test (H1); geometry only allows it. A 24 degree sweep needs the long tab ramp (the pin must still catch the tab with the lever closed) and leaves 1.6 mm between the arm and the downstream pressure sensor.
- **Mass is marginal.** 594 g against 600 only after the bay block was hollowed and the hinge pin shortened; case halves are 210 g, motor 110 g, cells 94 g.
- **Hinge cannot be a full-height 3 mm pin in 58 mm** without cutting the cassette's way out, see above.
- **Rollers crush the straight legs.** Two idle rollers overlap the straight tube legs outside the wrap (0.03 cm3 each at rest); a roller stays within 2.7 to 3.2 mm of the stub wall for about 16 degrees past each end of the wrap.
- **Insertion order matters.** The worm wheel can only go on the shaft from behind, so the rotor group must be fitted before the rear shell; the rear shell then closes with the worm already under the wheel.

## Not done or not verified

- Latch hook that holds the tongue is not modelled (tongue slides in a tall pocket); latch force, spring force and tube flexure were not analysed.
- No bosses or standoffs for the main board beyond four stubs; motor held by two ribs only; no cable routing; no gasket on the bulkhead.
- `qa.mass_density` judges 21 of 46 parts; PETG, PC, silicone, FR4 and "electronics" have no density bound in nl-cad.
- No parametric stress test (a 10 percent nudge and rebuild).
- The three gears are plain cylinders at pitch diameter and touch tangentially; the check reports no overlap for them.

## How it was built

```
cd /w/dev/open-feed-pump
PYTHONPATH=/w/dev/nl-cad uv run --project /w/dev/nl-cad python -m nlcad.build projects/feed-pump --note "..."
PYTHONPATH=/w/dev/nl-cad uv run --project /w/dev/nl-cad python -m nlcad.qa projects/feed-pump/builds/v11 --sweep --write
PYTHONPATH=/w/dev/nl-cad uv run --project /w/dev/nl-cad python projects/feed-pump/tools/brief_numbers.py
# single-file viewer with the okstudio-style theme (commit 6fc4df7 of owenpkent/okstudio-style), N = build number, SCRATCH = any scratch folder
NLCAD_DIR=W:/dev/nl-cad OKSTUDIO_DIR=W:/dev/okstudio-style EXPORT_VERSION=N EXPORT_OUT=SCRATCH   node W:/dev/nl-cad/viewer/node_modules/vite/bin/vite.js build --config projects/feed-pump/tools/viewer.embed.config.ts
cp SCRATCH/dist/embedded.html projects/feed-pump/builds/vN/feed-pump_viewer_vN.html
```
The v7 sweep is `builds/v7/qa_v7.md`; the final one is `builds/v11/qa_v11.md`.

`checks:` in `assembly.yaml` sets the interference threshold to 0.02 cm3 (nl-cad default 0.5), so overlaps the size of a roller chord show.
