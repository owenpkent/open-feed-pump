# Checks, feed-pump v8

73 pass, 4 warn (0 accepted, 4 untriaged), 0 fail

## Coverage

| Check | Ran over |
|---|---|
| interference | 98 of 101 pairs with overlapping bboxes |
| envelope.width | all |
| envelope.length | all |
| envelope.height | all |
| envelope.height_excl | all |
| door | all |
| ground.contact | all |
| ground.clearance | all |
| mass.total | 46 of 46 instances |
| mass.cg | 46 of 46 instances |
| qa.joints | all |
| qa.connected | all |
| qa.joint_contact | 45 of 45 joints |
| qa.mass_density | 21 of 46 instances |
| qa.mass_missing | 46 of 46 instances |
| qa.bom | 29 of 46 instances (bought only) |
| qa.mesh | 46 of 46 instances |
| checks.dist.squeeze_gap@rotor=0 | 4 of 46 instances |
| checks.dist.squeeze_gap@rotor=30 | 4 of 46 instances |
| checks.dist.squeeze_gap@rotor=60 | 4 of 46 instances |
| checks.dist.squeeze_gap@rotor=90 | 4 of 46 instances |
| checks.dist.squeeze_gap@rotor=120 | 4 of 46 instances |
| checks.dist.squeeze_gap@rotor=150 | 4 of 46 instances |
| checks.dist.door_pin_reach@home | 2 of 46 instances |
| checks.dist.pinch_open_gap@pinch=0 | 2 of 46 instances |
| checks.dist.pinch_closed_gap@pinch=lo | 2 of 46 instances |
| checks.dist.pinch_closed_reach@pinch=lo | 2 of 46 instances |
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

- interference: pair declared in checks.interference.allow (overlap not measured) (3): rotor_grp/roller_1 x cassette/tube, rotor_grp/roller_2 x cassette/tube, rotor_grp/roller_3 x cassette/tube
- qa.mass_density: material has no density bound in qa/static.py DENSITY (25): back/case_back, back/cell_1, back/cell_2, back/encoder, cassette/cassette, cassette/lever, cassette/tube, door/door, and 17 more
- checks.dist.squeeze_gap@rotor=0: joint moves a part of this row and was held at home in this pose (3): roller_1, roller_2, roller_3
- checks.dist.squeeze_gap@rotor=30: joint moves a part of this row and was held at home in this pose (3): roller_1, roller_2, roller_3
- checks.dist.squeeze_gap@rotor=60: joint moves a part of this row and was held at home in this pose (3): roller_1, roller_2, roller_3
- checks.dist.squeeze_gap@rotor=90: joint moves a part of this row and was held at home in this pose (3): roller_1, roller_2, roller_3
- checks.dist.squeeze_gap@rotor=120: joint moves a part of this row and was held at home in this pose (3): roller_1, roller_2, roller_3
- checks.dist.squeeze_gap@rotor=150: joint moves a part of this row and was held at home in this pose (3): roller_1, roller_2, roller_3
- checks.dist.door_pin_reach@home: joint moves a part of this row and was held at home in this pose (2): door, pinch
- qa.insert.cassette/tube: allowed pair (checks.interference.allow): rides through, not an obstacle (3): cassette/tube x rotor_grp/roller_1, cassette/tube x rotor_grp/roller_2, cassette/tube x rotor_grp/roller_3

## Checks

| Status | Check | Value | Limit | Detail |
|---|---|---|---|---|
| PASS | Part overlap | 0 cm3 | 0 cm3 | no pair overlaps by 0.02 cm3 or more (3 smaller ignored) |
| PASS | Overall width | 0.16 m | 0.16 m | 160 mm |
| PASS | Overall length | 0.058 m | 0.058 m | 58 mm |
| INFO | Overall height | 0.125 m |  | 125 mm |
| PASS | Overall height without */tube | 0.11 m | 0.11 m | 110 mm |
| PASS | Doorway fit | 0.16 m | 0.813 m | +653 mm total clearance in an 813 mm door |
| PASS | Wheel ground contact | 0 m | 0.002 m | 0 wheels; lowest points  |
| INFO | Ground clearance | -0.015 m |  | lowest non-wheel point -15 mm (cassette/tube) |
| PASS | Total mass | 0.5941 kg | 0.6 kg | 0.6 kg over 46 instances |
| INFO | Centre of gravity height | 0.04862 m |  | x +28, y +7, z 49 mm (x forward of the drive-axle datum) |
| PASS | Joint definitions | 0 issues | 0 issues | 45 joints: axes, ranges, parents and origins are consistent |
| PASS | Parts form one connected body | 1 clusters | 1 clusters | 46 parts, each within 2 mm of another |
| PASS | Joint parts touch | 0.0005 m | 0.005 m | all 45 joints have parent and child surfaces within 5 mm |
| PASS | Mass is physically possible | 0 parts | 0 parts | no part is denser than a solid of its material |
| PASS | Every part has a mass | 0 parts | 0 parts | 46 instances carry a positive mass |
| PASS | Bought parts name a vendor or part number | 0 parts | 0 parts | 29 bought instances all named. Status tiers over 46 instances: confirmed 0, measured 0, published 4, estimated 42 |
| PASS | Part meshes are solid | 0 parts | 0 parts | 46 meshes closed with positive volume |
| PASS | Distance squeeze_gap at rotor=0 | 0.0027 m | 0.00285 m | rotor_grp/roller_* to cassette/cassette, nearest points: 2.70 mm at rotor=0; min 2.55 mm, max 2.85 mm |
| PASS | Distance squeeze_gap at rotor=30 | 0.0027 m | 0.00285 m | rotor_grp/roller_* to cassette/cassette, nearest points: 2.70 mm at rotor=30; min 2.55 mm, max 2.85 mm |
| PASS | Distance squeeze_gap at rotor=60 | 0.0027 m | 0.00285 m | rotor_grp/roller_* to cassette/cassette, nearest points: 2.70 mm at rotor=60; min 2.55 mm, max 2.85 mm |
| PASS | Distance squeeze_gap at rotor=90 | 0.0027 m | 0.00285 m | rotor_grp/roller_* to cassette/cassette, nearest points: 2.70 mm at rotor=90; min 2.55 mm, max 2.85 mm |
| PASS | Distance squeeze_gap at rotor=120 | 0.0027 m | 0.00285 m | rotor_grp/roller_* to cassette/cassette, nearest points: 2.70 mm at rotor=120; min 2.55 mm, max 2.85 mm |
| PASS | Distance squeeze_gap at rotor=150 | 0.0027 m | 0.00285 m | rotor_grp/roller_* to cassette/cassette, nearest points: 2.70 mm at rotor=150; min 2.55 mm, max 2.85 mm |
| PASS | Distance door_pin_reach at home | 7.105e-18 m | 0.0005 m | door/door to cassette/lever, nearest points: 0.00 mm at home (every joint at rest); min 0 mm, max 0.5 mm; home only is fine: door shut is the home pose; the sweep covers the swing |
| PASS | Distance pinch_open_gap at pinch=0 | 0.0012 m | 0.0011 m | cassette/lever to cassette/tube, nearest points: 1.20 mm at pinch=0; min 1.1 mm |
| PASS | Distance pinch_closed_gap at pinch=lo | 0.002054 m | 0.0022 m | cassette/lever to cassette/cassette@anvil_face, along y: 2.05 mm at pinch=lo; min 0 mm, max 2.2 mm |
| PASS | Distance pinch_closed_reach at pinch=lo | 0 m | 5e-05 m | cassette/lever to cassette/tube, nearest points: 0.00 mm at pinch=lo; max 0.05 mm |
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
| PASS | Insertion, cassette/lever | 0.011 m |  | clear along +x (11 mm to leave the 38 parts present at step 'Cassette and tube'); blocked: +z by electronics/air at 12 mm, -z by front/case_front at 2 mm |
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
| WARN | Stale warn accept | 1 accepts | 0 accepts | accepted_warns row for qa.sweep.door.clearance parts ['front/hinge_*'] matches no live warn; remove it or fix its check id (Hinge pin stubs run in 3.1 mm notches in the door (0.05 mm radial running fit, coaxial with the joint). The gap is constant over the swing.) |
| WARN | Stale warn accept | 1 accepts | 0 accepts | accepted_warns row for qa.sweep.door parts ['front/case_front'] matches no live warn; remove it or fix its check id (Only the overtravel pose -2.5 degrees warns: the closed door rests on the case front face, which is its physical stop. There is no overlap inside 0 to 100 degrees; the hinge edge is bevelled to clear the case to 102.5 degrees (tools/brief_numbers.py).) |
| WARN | Stale warn accept | 1 accepts | 0 accepts | accepted_warns row for qa.sweep.rotor.clearance parts ['rotor_grp/rotor'] matches no live warn; remove it or fix its check id (Hub back face runs 0.50 mm off the bearing boss front face (axial running clearance, set by the 41.5 hub datum against the 41.0 bulkhead face).) |
| WARN | Stale warn accept | 1 accepts | 0 accepts | accepted_warns row for qa.sweep.latch.clearance parts ['door/latch'] matches no live warn; remove it or fix its check id (Latch slider runs in its door notch with 0.20 mm clearance each side (sliding fit).) |

