# QA checks, feed-pump v7

65 pass, 5 warn (5 accepted, 0 untriaged), 0 fail

## Coverage

| Check | Ran over |
|---|---|
| qa.joints | all |
| qa.connected | all |
| qa.joint_contact | 45 of 45 joints |
| qa.mass_density | 21 of 46 instances |
| qa.mass_missing | 46 of 46 instances |
| qa.bom | 29 of 46 instances (bought only) |
| qa.mesh | 46 of 46 instances |
| qa.sweep.pinch | 45 of 45 pairs (8 poses; far pairs proven by bounding box) |
| qa.sweep.pinch.clearance | 45 of 45 pairs (8 poses; far pairs proven by bounding box) |
| qa.sweep.door | 88 of 88 pairs (8 poses; far pairs proven by bounding box) |
| qa.sweep.door.clearance | 88 of 88 pairs (8 poses; far pairs proven by bounding box) |
| qa.sweep.rotor | 237 of 240 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.rotor.clearance | 237 of 240 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.latch | 45 of 45 pairs (8 poses; far pairs proven by bounding box) |
| qa.sweep.latch.clearance | 45 of 45 pairs (8 poses; far pairs proven by bounding box) |
| qa.sweep.roller_1 | 44 of 45 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.roller_1.clearance | 44 of 45 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.roller_2 | 44 of 45 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.roller_2.clearance | 44 of 45 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.roller_3 | 44 of 45 pairs (6 poses; far pairs proven by bounding box) |
| qa.sweep.roller_3.clearance | 44 of 45 pairs (6 poses; far pairs proven by bounding box) |
| qa.insert.front/case_front | 0 of 45 other parts (those present at its step) |
| qa.insert.front/hinge_top | 1 of 45 other parts (those present at its step) |
| qa.insert.front/hinge_bot | 2 of 45 other parts (those present at its step) |
| qa.insert.front/bearing_f | 3 of 45 other parts (those present at its step) |
| qa.insert.front/bearing_r | 4 of 45 other parts (those present at its step) |
| qa.insert.electronics/display | 5 of 45 other parts (those present at its step) |
| qa.insert.electronics/pcb | 6 of 45 other parts (those present at its step) |
| qa.insert.electronics/usb | 7 of 45 other parts (those present at its step) |
| qa.insert.electronics/jack | 8 of 45 other parts (those present at its step) |
| qa.insert.electronics/sounder | 9 of 45 other parts (those present at its step) |
| qa.insert.electronics/p_up | 10 of 45 other parts (those present at its step) |
| qa.insert.electronics/p_down | 11 of 45 other parts (those present at its step) |
| qa.insert.electronics/air | 12 of 45 other parts (those present at its step) |
| qa.insert.electronics/sw_cass | 13 of 45 other parts (those present at its step) |
| qa.insert.electronics/sw_door | 14 of 45 other parts (those present at its step) |
| qa.insert.electronics/btn_1 | 15 of 45 other parts (those present at its step) |
| qa.insert.electronics/btn_2 | 16 of 45 other parts (those present at its step) |
| qa.insert.electronics/btn_3 | 17 of 45 other parts (those present at its step) |
| qa.insert.electronics/btn_4 | 18 of 45 other parts (those present at its step) |
| qa.insert.electronics/btn_5 | 19 of 45 other parts (those present at its step) |
| qa.insert.rotor_grp/rotor | 20 of 45 other parts (those present at its step) |
| qa.insert.rotor_grp/worm_wheel | 21 of 45 other parts (those present at its step) |
| qa.insert.rotor_grp/magnet | 22 of 45 other parts (those present at its step) |
| qa.insert.rotor_grp/roller_1 | 23 of 45 other parts (those present at its step) |
| qa.insert.rotor_grp/roller_2 | 24 of 45 other parts (those present at its step) |
| qa.insert.rotor_grp/roller_3 | 25 of 45 other parts (those present at its step) |
| qa.insert.back/motor | 26 of 45 other parts (those present at its step) |
| qa.insert.back/worm | 27 of 45 other parts (those present at its step) |
| qa.insert.back/encoder | 28 of 45 other parts (those present at its step) |
| qa.insert.back/cell_1 | 29 of 45 other parts (those present at its step) |
| qa.insert.back/cell_2 | 30 of 45 other parts (those present at its step) |
| qa.insert.back/insert_1 | 31 of 45 other parts (those present at its step) |
| qa.insert.back/insert_2 | 32 of 45 other parts (those present at its step) |
| qa.insert.back/insert_3 | 33 of 45 other parts (those present at its step) |
| qa.insert.back/insert_4 | 34 of 45 other parts (those present at its step) |
| qa.insert.back/case_back | 35 of 45 other parts (those present at its step) |
| qa.insert.cassette/cassette | 36 of 45 other parts (those present at its step) |
| qa.insert.cassette/tube | 37 of 45 other parts (those present at its step) |
| qa.insert.cassette/lever | 38 of 45 other parts (those present at its step) |
| qa.insert.cassette/spring | 39 of 45 other parts (those present at its step) |
| qa.insert.door/door | 40 of 45 other parts (those present at its step) |
| qa.insert.door/latch | 41 of 45 other parts (those present at its step) |
| qa.fastener.head_buried | 4 of 4 fasteners |
| qa.fastener.engagement | 4 of 4 fasteners |
| qa.fastener.bought_clash | 4 of 4 fasteners |
| qa.fastener.head_overlap | 4 of 4 fasteners |
| qa.fastener.stock | 4 of 4 fasteners |
| qa.fastener.access | 4 of 4 fasteners |
| qa.fastener.bom | 4 of 4 fasteners |

## Not checked

- qa.mass_density: material has no density bound in qa/static.py DENSITY (25): back/case_back, back/cell_1, back/cell_2, back/encoder, cassette/cassette, cassette/lever, cassette/tube, door/door, and 17 more
- qa.sweep.pinch: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (3): cassette/lever x cassette/cassette, cassette/lever x cassette/spring, cassette/lever x door/door
- qa.sweep.pinch.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (3): cassette/lever x cassette/cassette, cassette/lever x cassette/spring, cassette/lever x door/door
- qa.sweep.door: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (4): door/door x cassette/lever, door/door x electronics/sw_door, door/door x front/case_front, door/latch x front/case_front
- qa.sweep.door.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (4): door/door x cassette/lever, door/door x electronics/sw_door, door/door x front/case_front, door/latch x front/case_front
- qa.sweep.rotor: allowed pair (checks.interference.allow), overlap and clearance not measured (3): rotor_grp/roller_1 x cassette/tube, rotor_grp/roller_2 x cassette/tube, rotor_grp/roller_3 x cassette/tube
- qa.sweep.rotor: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (4): rotor_grp/rotor x cassette/tube, rotor_grp/rotor x front/bearing_f, rotor_grp/rotor x front/bearing_r, rotor_grp/worm_wheel x back/worm
- qa.sweep.rotor.clearance: allowed pair (checks.interference.allow), overlap and clearance not measured (3): rotor_grp/roller_1 x cassette/tube, rotor_grp/roller_2 x cassette/tube, rotor_grp/roller_3 x cassette/tube
- qa.sweep.rotor.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (4): rotor_grp/rotor x cassette/tube, rotor_grp/rotor x front/bearing_f, rotor_grp/rotor x front/bearing_r, rotor_grp/worm_wheel x back/worm
- qa.sweep.latch: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): door/latch x front/case_front
- qa.sweep.latch.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): door/latch x front/case_front
- qa.sweep.roller_1: allowed pair (checks.interference.allow), overlap and clearance not measured (1): rotor_grp/roller_1 x cassette/tube
- qa.sweep.roller_1: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): rotor_grp/roller_1 x rotor_grp/rotor
- qa.sweep.roller_1.clearance: allowed pair (checks.interference.allow), overlap and clearance not measured (1): rotor_grp/roller_1 x cassette/tube
- qa.sweep.roller_1.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): rotor_grp/roller_1 x rotor_grp/rotor
- qa.sweep.roller_2: allowed pair (checks.interference.allow), overlap and clearance not measured (1): rotor_grp/roller_2 x cassette/tube
- qa.sweep.roller_2: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): rotor_grp/roller_2 x rotor_grp/rotor
- qa.sweep.roller_2.clearance: allowed pair (checks.interference.allow), overlap and clearance not measured (1): rotor_grp/roller_2 x cassette/tube
- qa.sweep.roller_2.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): rotor_grp/roller_2 x rotor_grp/rotor
- qa.sweep.roller_3: allowed pair (checks.interference.allow), overlap and clearance not measured (1): rotor_grp/roller_3 x cassette/tube
- qa.sweep.roller_3: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): rotor_grp/roller_3 x rotor_grp/rotor
- qa.sweep.roller_3.clearance: allowed pair (checks.interference.allow), overlap and clearance not measured (1): rotor_grp/roller_3 x cassette/tube
- qa.sweep.roller_3.clearance: touching at rest or declared contact (checks.fits): clearance not judged, overlap still measured (1): rotor_grp/roller_3 x rotor_grp/rotor
- qa.insert.cassette/tube: allowed pair (checks.interference.allow): rides through, not an obstacle (3): cassette/tube x rotor_grp/roller_1, cassette/tube x rotor_grp/roller_2, cassette/tube x rotor_grp/roller_3

## Checks

| Status | Check | Value | Limit | Detail |
|---|---|---|---|---|
| PASS | Joint definitions | 0 issues | 0 issues | 45 joints: axes, ranges, parents and origins are consistent |
| PASS | Parts form one connected body | 1 clusters | 1 clusters | 46 parts, each within 2 mm of another |
| PASS | Joint parts touch | 0.0005 m | 0.005 m | all 45 joints have parent and child surfaces within 5 mm |
| PASS | Mass is physically possible | 0 parts | 0 parts | no part is denser than a solid of its material |
| PASS | Every part has a mass | 0 parts | 0 parts | 46 instances carry a positive mass |
| PASS | Bought parts name a vendor or part number | 0 parts | 0 parts | 29 bought instances all named. Status tiers over 46 instances: confirmed 0, measured 0, published 4, estimated 42 |
| PASS | Part meshes are solid | 0 parts | 0 parts | 46 meshes closed with positive volume |
| PASS | Sweep, joint pinch | 0.09726 cm3 | 0.5 cm3 | no new overlap of 0.5 cm3 or more (1 moving parts vs 45; 8 poses of revolute joint incl. overtravel 2.5 deg (+0.044 rad) either end, 0 extra poses from bisection; min clearance 0.30 mm) |
| PASS | Sweep, joint rotor | 0.008691 cm3 | 0.5 cm3 | no new overlap of 0.5 cm3 or more (6 moving parts vs 40; 6 poses of continuous joint, 186 extra poses from bisection; min clearance 0.50 mm) |
| PASS | Sweep, joint latch | 0.033 cm3 | 0.5 cm3 | no new overlap of 0.5 cm3 or more (1 moving parts vs 45; 8 poses of prismatic joint incl. overtravel 2.0 mm either end, 12 extra poses from bisection; min clearance 0.20 mm) |
| PASS | Sweep, joint roller_1 | 0 cm3 | 0.5 cm3 | no new overlap of 0.5 cm3 or more (1 moving parts vs 45; 6 poses of continuous joint, 0 extra poses from bisection; min clearance 2.40 mm) |
| PASS | Sweep clearance, joint roller_1 | 0.0024 m | 0.001 m | closest rotor_grp/roller_1 x cassette/cassette at 2.40 mm, any angle (revolved envelope, lower bound) (6 poses of continuous joint, 0 extra poses from bisection) |
| PASS | Sweep, joint roller_2 | 3.659e-05 cm3 | 0.5 cm3 | no new overlap of 0.5 cm3 or more (1 moving parts vs 45; 6 poses of continuous joint, 0 extra poses from bisection; min clearance 2.34 mm) |
| PASS | Sweep clearance, joint roller_2 | 0.002337 m | 0.001 m | closest rotor_grp/roller_2 x cassette/cassette at 2.34 mm, any angle (revolved envelope, lower bound) (6 poses of continuous joint, 0 extra poses from bisection) |
| PASS | Sweep, joint roller_3 | 3.659e-05 cm3 | 0.5 cm3 | no new overlap of 0.5 cm3 or more (1 moving parts vs 45; 6 poses of continuous joint, 0 extra poses from bisection; min clearance 2.34 mm) |
| PASS | Sweep clearance, joint roller_3 | 0.002337 m | 0.001 m | closest rotor_grp/roller_3 x cassette/cassette at 2.34 mm, any angle (revolved envelope, lower bound) (6 poses of continuous joint, 0 extra poses from bisection) |
| PASS | Insertion, front/case_front | 0 m |  | first part of its step 'Case front': nothing present to get past |
| PASS | Insertion, front/hinge_top | 0.0015 m |  | clear along +x (2 mm to leave the 1 parts present at step 'Case front'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, front/hinge_bot | 0.0015 m |  | clear along +x (2 mm to leave the 2 parts present at step 'Case front'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, front/bearing_f | 0.018 m |  | clear along +x (18 mm to leave the 3 parts present at step 'Case front'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, front/bearing_r | 0.006 m |  | clear along -x (6 mm to leave the 4 parts present at step 'Case front'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm, +x by front/bearing_f at 6 mm |
| PASS | Insertion, electronics/display | 0.0265 m |  | clear along -x (27 mm to leave the 5 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 12 mm, +x by front/case_front at 2 mm |
| PASS | Insertion, electronics/pcb | 0.0204 m |  | clear along -x (20 mm to leave the 6 parts present at step 'Electronics'); blocked: +z by front/case_front at 3 mm, -z by front/case_front at 4 mm, +x by front/case_front at 2 mm |
| PASS | Insertion, electronics/usb | 0.0073 m |  | clear along -z (7 mm to leave the 7 parts present at step 'Electronics'); blocked: +z by electronics/display at 56 mm |
| PASS | Insertion, electronics/jack | 0.011 m |  | clear along -z (11 mm to leave the 8 parts present at step 'Electronics'); blocked: +z by front/case_front at 9 mm |
| PASS | Insertion, electronics/sounder | 0.0265 m |  | clear along -x (27 mm to leave the 9 parts present at step 'Electronics'); blocked: +z by electronics/display at 12 mm, -z by front/case_front at 39 mm, +x by front/case_front at 2 mm |
| PASS | Insertion, electronics/p_up | 0.0202 m |  | clear along +x (20 mm to leave the 10 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/p_down | 0.0202 m |  | clear along +x (20 mm to leave the 11 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/air | 0.0152 m |  | clear along +x (15 mm to leave the 12 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/sw_cass | 0.02 m |  | clear along +x (20 mm to leave the 13 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/sw_door | 0.006 m |  | clear along +x (6 mm to leave the 14 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/btn_1 | 0.00749 m |  | clear along +x (7 mm to leave the 15 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, electronics/btn_2 | 0.00749 m |  | clear along +x (7 mm to leave the 16 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, electronics/btn_3 | 0.00749 m |  | clear along +x (7 mm to leave the 17 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, electronics/btn_4 | 0.00749 m |  | clear along +x (7 mm to leave the 18 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by electronics/usb at 3 mm |
| PASS | Insertion, electronics/btn_5 | 0.00749 m |  | clear along +x (7 mm to leave the 19 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, rotor_grp/rotor | 0.04 m |  | clear along +x (40 mm to leave the 20 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 3 mm, -z by front/case_front at 3 mm |
| PASS | Insertion, rotor_grp/worm_wheel | 0.0075 m |  | clear along -x (8 mm to leave the 21 parts present at step 'Rotor and rollers'); blocked: +z by rotor_grp/rotor at 3 mm, -z by rotor_grp/rotor at 3 mm, +x by front/case_front at 6 mm |
| PASS | Insertion, rotor_grp/magnet | 0.018 m |  | clear along +z (18 mm to leave the 22 parts present at step 'Rotor and rollers') |
| PASS | Insertion, rotor_grp/roller_1 | 0.011 m |  | clear along +x (11 mm to leave the 23 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 14 mm, -z by front/case_front at 66 mm |
| PASS | Insertion, rotor_grp/roller_2 | 0.011 m |  | clear along +x (11 mm to leave the 24 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 33 mm, -z by electronics/p_up at 10 mm |
| PASS | Insertion, rotor_grp/roller_3 | 0.011 m |  | clear along +x (11 mm to leave the 25 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 33 mm, -z by electronics/air at 6 mm |
| PASS | Insertion, back/motor | 0.0215 m |  | clear along -x (22 mm to leave the 26 parts present at step 'Case back and drive'); blocked: +z by rotor_grp/worm_wheel at 2 mm, -z by front/case_front at 38 mm, +x by electronics/p_up at 2 mm |
| PASS | Insertion, back/worm | 0.02 m |  | clear along +y (20 mm to leave the 27 parts present at step 'Case back and drive'); blocked: +z by back/motor at 2 mm, -z by back/motor at 2 mm, +x by back/motor at 2 mm, -x by back/motor at 2 mm |
| PASS | Insertion, back/encoder | 0.0065 m |  | clear along +z (6 mm to leave the 28 parts present at step 'Case back and drive') |
| PASS | Insertion, back/cell_1 | 0 m |  | clear along -z (nothing ahead of it among the 29 parts present at step 'Case back and drive'); blocked: +z by back/motor at 20 mm |
| PASS | Insertion, back/cell_2 | 0.0185 m |  | clear along -z (18 mm to leave the 30 parts present at step 'Case back and drive'); blocked: +z by back/motor at 20 mm |
| PASS | Insertion, back/insert_1 | 0 m |  | clear along +z (nothing ahead of it among the 31 parts present at step 'Case back and drive') |
| PASS | Insertion, back/insert_2 | 0 m |  | clear along +z (nothing ahead of it among the 32 parts present at step 'Case back and drive') |
| PASS | Insertion, back/insert_3 | 0 m |  | clear along -x (nothing ahead of it among the 33 parts present at step 'Case back and drive'); blocked: +z by back/motor at 2 mm, -z by back/cell_2 at 14 mm, +x by front/case_front at 32 mm |
| PASS | Insertion, back/insert_4 | 0 m |  | clear along +z (nothing ahead of it among the 34 parts present at step 'Case back and drive') |
| PASS | Insertion, back/case_back | 0.0255 m |  | clear along -x (26 mm to leave the 35 parts present at step 'Case back and drive'); blocked: +z by back/cell_1 at 2 mm, -z by back/insert_1 at 2 mm, +x by front/case_front at 2 mm |
| PASS | Insertion, cassette/cassette | 0.0155 m |  | clear along +x (16 mm to leave the 36 parts present at step 'Cassette and tube'); blocked: +z by electronics/p_up at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, cassette/tube | 0.0102 m |  | clear along +x (10 mm to leave the 37 parts present at step 'Cassette and tube'); blocked: +z by cassette/cassette at 2 mm, -z by electronics/air at 27 mm |
| PASS | Insertion, cassette/lever | 0.011 m |  | clear along +x (11 mm to leave the 38 parts present at step 'Cassette and tube'); blocked: +z by electronics/p_down at 3 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, cassette/spring | 0.0035 m |  | clear along +x (4 mm to leave the 39 parts present at step 'Cassette and tube'); blocked: +z by cassette/cassette at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, door/door | 0.0035 m |  | clear along +x (4 mm to leave the 40 parts present at step 'Door and latch'); blocked: +z by front/hinge_top at 2 mm, -z by front/hinge_bot at 2 mm |
| PASS | Insertion, door/latch | 0.00549 m |  | clear along +x (5 mm to leave the 41 parts present at step 'Door and latch'); blocked: +z by door/door at 6 mm, -z by door/door at 3 mm |
| PASS | Fastener heads not buried | 0 fasteners | 0 fasteners | no point 0.25 mm behind a bearing face lies in another solid of the body (4 screws) |
| PASS | Fastener engagement | 0 fasteners | 0 fasteners | all 4 screws engage their host or reach through their nut |
| PASS | Fasteners clear of bought parts | 0 fasteners | 0 fasteners | no shank or nut sits inside a bought part it does not thread into |
| PASS | Fastener heads and nuts clear of solids | 0 fasteners | 0 fasteners | no head or nut overlaps a solid of its body |
| PASS | Fastener stock lengths | 0 fasteners | 0 fasteners | all 4 lengths are stocked |
| PASS | Fastener driver access | 0 fasteners | 0 fasteners | every driven head has a free key path and hand space (4 screws) |
| PASS | Fastener BOM rows | 0 fasteners | 0 fasteners | all 4 BOM rows match their screw |

## Accepted warns

Triaged in `checks.accepted_warns` of assembly.yaml. Still warns, not failures.

| Status | Check | Value | Limit | Detail |
|---|---|---|---|---|
| ACCEPTED | Sweep clearance, joint pinch | 0.0003 m | 0.001 m | cassette/lever x cassette/tube 0.30 mm at +0.0 deg (+0.000 rad) (min 1 mm) (8 poses of revolute joint incl. overtravel 2.5 deg (+0.044 rad) either end, 0 extra poses from bisection) |
| ACCEPTED | Sweep, joint door | 2.402 cm3 | 0.5 cm3 | overtravel pose -2.5 deg (-0.044 rad) (past the range limit): door/door overlaps front/case_front by 2.4 cm3 more than at rest; no overlap inside the range (2 moving parts vs 44; 8 poses of revolute joint incl. overtravel 2.5 deg (+0.044 rad) either end, 155 extra poses from bisection; min clearance 0.05 mm) |
| ACCEPTED | Sweep clearance, joint door | 5e-05 m | 0.001 m | door/door x front/hinge_top 0.05 mm at +93.7 deg (+1.636 rad) (min 1 mm); door/door x front/hinge_bot 0.05 mm at +87.5 deg (+1.527 rad) (min 1 mm); gap not proven between samples for 2 pairs after 5 bisections, e.g. door/door x front/hinge_top between +0.0 deg (+0.000 rad) and +0.6 deg (+0.011 rad) (8 poses of revolute joint incl. overtravel 2.5 deg (+0.044 rad) either end, 155 extra poses from bisection) |
| ACCEPTED | Sweep clearance, joint rotor | 0.0005 m | 0.001 m | rotor_grp/rotor x front/case_front 0.50 mm at +0.0 deg (+0.000 rad) (min 1 mm) (6 poses of continuous joint, 186 extra poses from bisection) |
| ACCEPTED | Sweep clearance, joint latch | 0.0002 m | 0.001 m | door/latch x door/door 0.20 mm at +0.0 mm (min 1 mm) (8 poses of prismatic joint incl. overtravel 2.0 mm either end, 12 extra poses from bisection) |

- qa.sweep.pinch.clearance accepted: Open lever jaw is 0.30 mm from the tube by design. 15 degrees on a 14.4 mm arm moves the jaw 3.6 mm: 0.3 mm of free gap plus the 3.1 mm closed gap against the anvil. A wider opening needs a longer arm or more angle (real design finding, see BUILD_LOG).
- qa.sweep.door accepted: Only the overtravel pose -2.5 degrees warns: the closed door rests on the case front face, which is its physical stop. There is no overlap inside 0 to 100 degrees; the hinge edge is bevelled to clear the case to 102.5 degrees (tools/brief_numbers.py).
- qa.sweep.door.clearance accepted: Hinge pin stubs run in 3.1 mm notches in the door (0.05 mm radial running fit, coaxial with the joint). The gap is constant over the swing.
- qa.sweep.rotor.clearance accepted: Hub back face runs 0.50 mm off the bearing boss front face (axial running clearance, set by the 41.5 hub datum against the 41.0 bulkhead face).
- qa.sweep.latch.clearance accepted: Latch slider runs in its door notch with 0.20 mm clearance each side (sliding fit).

