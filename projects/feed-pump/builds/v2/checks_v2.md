# Checks, feed-pump v2

51 pass, 2 warn (0 accepted, 2 untriaged), 9 fail

## Coverage

| Check | Ran over |
|---|---|
| interference | 101 of 101 pairs with overlapping bboxes |
| envelope.width | all |
| envelope.length | all |
| envelope.height | all |
| envelope.height_excl | all |
| door | all |
| ground.contact | all |
| ground.clearance | all |
| mass.total | 45 of 45 instances |
| mass.cg | 45 of 45 instances |
| qa.joints | all |
| qa.connected | all |
| qa.joint_contact | 44 of 44 joints |
| qa.mass_density | 29 of 45 instances |
| qa.mass_missing | 45 of 45 instances |
| qa.bom | 28 of 45 instances (bought only) |
| qa.mesh | 45 of 45 instances |
| qa.insert.front/case_front | 0 of 44 other parts (those present at its step) |
| qa.insert.front/hinge_pin | 1 of 44 other parts (those present at its step) |
| qa.insert.front/bearing_f | 2 of 44 other parts (those present at its step) |
| qa.insert.front/bearing_r | 3 of 44 other parts (those present at its step) |
| qa.insert.electronics/pcb | 4 of 44 other parts (those present at its step) |
| qa.insert.electronics/display | 5 of 44 other parts (those present at its step) |
| qa.insert.electronics/usb | 6 of 44 other parts (those present at its step) |
| qa.insert.electronics/jack | 7 of 44 other parts (those present at its step) |
| qa.insert.electronics/sounder | 8 of 44 other parts (those present at its step) |
| qa.insert.electronics/p_up | 9 of 44 other parts (those present at its step) |
| qa.insert.electronics/p_down | 10 of 44 other parts (those present at its step) |
| qa.insert.electronics/air | 11 of 44 other parts (those present at its step) |
| qa.insert.electronics/sw_cass | 12 of 44 other parts (those present at its step) |
| qa.insert.electronics/sw_door | 13 of 44 other parts (those present at its step) |
| qa.insert.electronics/btn_1 | 14 of 44 other parts (those present at its step) |
| qa.insert.electronics/btn_2 | 15 of 44 other parts (those present at its step) |
| qa.insert.electronics/btn_3 | 16 of 44 other parts (those present at its step) |
| qa.insert.electronics/btn_4 | 17 of 44 other parts (those present at its step) |
| qa.insert.electronics/btn_5 | 18 of 44 other parts (those present at its step) |
| qa.insert.rotor_grp/rotor | 19 of 44 other parts (those present at its step) |
| qa.insert.rotor_grp/worm_wheel | 20 of 44 other parts (those present at its step) |
| qa.insert.rotor_grp/magnet | 21 of 44 other parts (those present at its step) |
| qa.insert.rotor_grp/roller_1 | 22 of 44 other parts (those present at its step) |
| qa.insert.rotor_grp/roller_2 | 23 of 44 other parts (those present at its step) |
| qa.insert.rotor_grp/roller_3 | 24 of 44 other parts (those present at its step) |
| qa.insert.back/case_back | 25 of 44 other parts (those present at its step) |
| qa.insert.back/motor | 26 of 44 other parts (those present at its step) |
| qa.insert.back/worm | 27 of 44 other parts (those present at its step) |
| qa.insert.back/encoder | 28 of 44 other parts (those present at its step) |
| qa.insert.back/cell_1 | 29 of 44 other parts (those present at its step) |
| qa.insert.back/cell_2 | 30 of 44 other parts (those present at its step) |
| qa.insert.back/insert_1 | 31 of 44 other parts (those present at its step) |
| qa.insert.back/insert_2 | 32 of 44 other parts (those present at its step) |
| qa.insert.back/insert_3 | 33 of 44 other parts (those present at its step) |
| qa.insert.back/insert_4 | 34 of 44 other parts (those present at its step) |
| qa.insert.cassette/cassette | 35 of 44 other parts (those present at its step) |
| qa.insert.cassette/tube | 36 of 44 other parts (those present at its step) |
| qa.insert.cassette/lever | 37 of 44 other parts (those present at its step) |
| qa.insert.cassette/spring | 38 of 44 other parts (those present at its step) |
| qa.insert.door/door | 39 of 44 other parts (those present at its step) |
| qa.insert.door/latch | 40 of 44 other parts (those present at its step) |
| qa.fastener.head_buried | 4 of 4 fasteners |
| qa.fastener.engagement | 4 of 4 fasteners |
| qa.fastener.bought_clash | 4 of 4 fasteners |
| qa.fastener.head_overlap | 4 of 4 fasteners |
| qa.fastener.stock | 4 of 4 fasteners |
| qa.fastener.access | 4 of 4 fasteners |
| qa.fastener.bom | 4 of 4 fasteners |

## Not checked

- qa.mass_density: material has no density bound in qa/static.py DENSITY (16): back/case_back, back/cell_1, back/cell_2, back/encoder, cassette/cassette, cassette/lever, cassette/tube, door/door, and 8 more

## Checks

| Status | Check | Value | Limit | Detail |
|---|---|---|---|---|
| FAIL | Part overlap | 0.1791 cm3 | 0 cm3 | 4 overlapping pairs: rotor_grp/roller_1 x cassette/tube 0.1 cm3; rotor_grp/roller_2 x cassette/tube 0.0 cm3; rotor_grp/roller_3 x cassette/tube 0.0 cm3; cassette/cassette x cassette/lever 0.0 cm3 |
| PASS | Overall width | 0.16 m | 0.16 m | 160 mm |
| PASS | Overall length | 0.058 m | 0.058 m | 58 mm |
| INFO | Overall height | 0.125 m |  | 125 mm |
| PASS | Overall height without */tube | 0.11 m | 0.11 m | 110 mm |
| PASS | Doorway fit | 0.16 m | 0.813 m | +653 mm total clearance in an 813 mm door |
| PASS | Wheel ground contact | 0 m | 0.002 m | 0 wheels; lowest points  |
| INFO | Ground clearance | -0.015 m |  | lowest non-wheel point -15 mm (cassette/tube) |
| WARN | Total mass | 0.606 kg | 0.6 kg | 0.6 kg over 45 instances |
| INFO | Centre of gravity height | 0.04913 m |  | x +28, y +6, z 49 mm (x forward of the drive-axle datum) |
| PASS | Joint definitions | 0 issues | 0 issues | 44 joints: axes, ranges, parents and origins are consistent |
| PASS | Parts form one connected body | 1 clusters | 1 clusters | 45 parts, each within 2 mm of another |
| PASS | Joint parts touch | 0.0005 m | 0.005 m | all 44 joints have parent and child surfaces within 5 mm |
| FAIL | Mass is physically possible | 9 parts | 0 parts | mass exceeds a solid of the stated material: electronics/air 3361 kg/m3 vs 1500 max for its material; electronics/display 2480 kg/m3 vs 1500 max for its material; electronics/jack 6061 kg/m3 vs 1500 max for its material; electronics/p_down 4687 kg/m3 vs 1500 max for its material; electronics/p_up 4687 kg/m3 vs 1500 max for its material; electronics/sounder 1862 kg/m3 vs 1500 max for its material. Either the mass or the material is wrong, or the shape is too small. |
| PASS | Every part has a mass | 0 parts | 0 parts | 45 instances carry a positive mass |
| PASS | Bought parts name a vendor or part number | 0 parts | 0 parts | 28 bought instances all named. Status tiers over 45 instances: confirmed 0, measured 0, published 4, estimated 41 |
| PASS | Part meshes are solid | 0 parts | 0 parts | 45 meshes closed with positive volume |
| PASS | Insertion, front/case_front | 0 m |  | first part of its step 'Case front': nothing present to get past |
| PASS | Insertion, front/hinge_pin | 0.1 m |  | clear along +z (100 mm to leave the 1 parts present at step 'Case front') |
| PASS | Insertion, front/bearing_f | 0.018 m |  | clear along +x (18 mm to leave the 2 parts present at step 'Case front'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, front/bearing_r | 0.006 m |  | clear along -x (6 mm to leave the 3 parts present at step 'Case front'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm, +x by front/bearing_f at 6 mm |
| WARN | Insertion, electronics/pcb | 0.02885 m |  | off-axis way in: clear only along (-1,+1,+0) (29 mm); every stated direction is blocked: +z by front/case_front at 3 mm; -z by front/case_front at 4 mm; +x by front/case_front at 2 mm; -x by front/case_front at 3 mm; +y by front/case_front at 21 mm; -y by front/case_front at 3 mm |
| FAIL | Insertion, electronics/display | 0 m |  | no way in at step 'Electronics': all 6 stated and axis directions and all 20 diagonals are blocked; +z by front/case_front at 4 mm; -z by front/case_front at 12 mm; +x by front/case_front at 2 mm; -x by electronics/pcb at 3 mm; +y by front/case_front at 18 mm; -y by front/case_front at 3 mm. Nearest blocker overall front/case_front along +x; reorder the steps, add an insert: direction, or open a path |
| PASS | Insertion, electronics/usb | 0.0073 m |  | clear along -z (7 mm to leave the 6 parts present at step 'Electronics'); blocked: +z by electronics/display at 56 mm |
| PASS | Insertion, electronics/jack | 0.011 m |  | clear along -z (11 mm to leave the 7 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm |
| PASS | Insertion, electronics/sounder | 0.0265 m |  | clear along -x (26 mm to leave the 8 parts present at step 'Electronics'); blocked: +z by front/case_front at 3 mm, -z by front/case_front at 93 mm, +x by front/case_front at 2 mm |
| PASS | Insertion, electronics/p_up | 0.0202 m |  | clear along +x (20 mm to leave the 9 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/p_down | 0.0202 m |  | clear along +x (20 mm to leave the 10 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/air | 0.0152 m |  | clear along +x (15 mm to leave the 11 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/sw_cass | 0.02 m |  | clear along +x (20 mm to leave the 12 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/sw_door | 0.006 m |  | clear along +x (6 mm to leave the 13 parts present at step 'Electronics'); blocked: +z by front/case_front at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, electronics/btn_1 | 0.00749 m |  | clear along +x (7 mm to leave the 14 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, electronics/btn_2 | 0.00749 m |  | clear along +x (7 mm to leave the 15 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, electronics/btn_3 | 0.00749 m |  | clear along +x (7 mm to leave the 16 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, electronics/btn_4 | 0.00749 m |  | clear along +x (7 mm to leave the 17 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by electronics/usb at 3 mm |
| PASS | Insertion, electronics/btn_5 | 0.00749 m |  | clear along +x (7 mm to leave the 18 parts present at step 'Electronics'); blocked: +z by front/case_front at 4 mm, -z by front/case_front at 4 mm |
| PASS | Insertion, rotor_grp/rotor | 0.04 m |  | clear along +x (40 mm to leave the 19 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 3 mm, -z by front/case_front at 3 mm |
| PASS | Insertion, rotor_grp/worm_wheel | 0.0075 m |  | clear along -x (8 mm to leave the 20 parts present at step 'Rotor and rollers'); blocked: +z by rotor_grp/rotor at 3 mm, -z by rotor_grp/rotor at 3 mm, +x by front/case_front at 6 mm |
| PASS | Insertion, rotor_grp/magnet | 0.018 m |  | clear along +z (18 mm to leave the 21 parts present at step 'Rotor and rollers') |
| PASS | Insertion, rotor_grp/roller_1 | 0.011 m |  | clear along +x (11 mm to leave the 22 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 14 mm, -z by front/case_front at 66 mm |
| PASS | Insertion, rotor_grp/roller_2 | 0.011 m |  | clear along +x (11 mm to leave the 23 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 33 mm, -z by electronics/p_up at 10 mm |
| PASS | Insertion, rotor_grp/roller_3 | 0.011 m |  | clear along +x (11 mm to leave the 24 parts present at step 'Rotor and rollers'); blocked: +z by front/case_front at 33 mm, -z by electronics/air at 6 mm |
| PASS | Insertion, back/case_back | 0.0135 m |  | clear along -x (14 mm to leave the 25 parts present at step 'Case back and drive'); blocked: +z by rotor_grp/worm_wheel at 57 mm, -z by rotor_grp/worm_wheel at 34 mm, +x by front/case_front at 2 mm |
| FAIL | Insertion, back/motor | 0 m |  | no way in at step 'Case back and drive': all 6 stated and axis directions and all 20 diagonals are blocked; +z by rotor_grp/worm_wheel at 2 mm; -z by front/case_front at 39 mm; +x by electronics/p_up at 2 mm; -x by back/case_back at 2 mm; +y by front/case_front at 3 mm; -y by front/case_front at 78 mm. Nearest blocker overall rotor_grp/worm_wheel along +z; reorder the steps, add an insert: direction, or open a path |
| FAIL | Insertion, back/worm | 0 m |  | no way in at step 'Case back and drive': all 6 stated and axis directions and all 20 diagonals are blocked; +z by back/motor at 2 mm; -z by back/motor at 2 mm; +x by back/motor at 2 mm; -x by back/motor at 2 mm; +y by back/case_back at 30 mm; -y by back/motor at 8 mm. Nearest blocker overall back/motor along +z; reorder the steps, add an insert: direction, or open a path |
| PASS | Insertion, back/encoder | 0.048 m |  | clear along +z (48 mm to leave the 28 parts present at step 'Case back and drive') |
| FAIL | Insertion, back/cell_1 | 0 m |  | no way in at step 'Case back and drive': all 6 stated and axis directions and all 20 diagonals are blocked; +z by back/case_back at 18 mm; -z by back/case_back at 2 mm; +x by front/case_front at 15 mm; -x by back/case_back at 2 mm; +y by back/case_back at 68 mm; -y by back/case_back at 3 mm. Nearest blocker overall back/case_back along -z; reorder the steps, add an insert: direction, or open a path |
| FAIL | Insertion, back/cell_2 | 0 m |  | no way in at step 'Case back and drive': all 6 stated and axis directions and all 20 diagonals are blocked; +z by back/case_back at 18 mm; -z by back/case_back at 2 mm; +x by front/case_front at 15 mm; -x by back/case_back at 2 mm; +y by back/case_back at 3 mm; -y by back/cell_1 at 2 mm. Nearest blocker overall back/case_back along -z; reorder the steps, add an insert: direction, or open a path |
| PASS | Insertion, back/insert_1 | 0.0065 m |  | clear along -x (6 mm to leave the 31 parts present at step 'Case back and drive'); blocked: +z by back/case_back at 2 mm, -z by back/case_back at 2 mm, +x by electronics/pcb at 39 mm |
| PASS | Insertion, back/insert_2 | 0.0065 m |  | clear along -x (6 mm to leave the 32 parts present at step 'Case back and drive'); blocked: +z by back/case_back at 2 mm, -z by back/case_back at 2 mm, +x by electronics/pcb at 39 mm |
| PASS | Insertion, back/insert_3 | 0.0065 m |  | clear along -x (6 mm to leave the 33 parts present at step 'Case back and drive'); blocked: +z by back/case_back at 2 mm, -z by back/case_back at 2 mm, +x by front/case_front at 32 mm |
| PASS | Insertion, back/insert_4 | 0.0065 m |  | clear along -x (6 mm to leave the 34 parts present at step 'Case back and drive'); blocked: +z by back/case_back at 2 mm, -z by back/case_back at 2 mm, +x by front/case_front at 32 mm |
| FAIL | Insertion, cassette/cassette | 0 m |  | no way in at step 'Cassette and tube': all 6 stated and axis directions and all 20 diagonals are blocked; +z by electronics/p_up at 2 mm; -z by front/case_front at 2 mm; +x by front/hinge_pin at 10 mm; -x by front/case_front at 2 mm; +y by front/case_front at 2 mm; -y by front/case_front at 2 mm. Nearest blocker overall electronics/p_up along +z; reorder the steps, add an insert: direction, or open a path |
| FAIL | Insertion, cassette/tube | 0 m |  | no way in at step 'Cassette and tube': all 6 stated and axis directions and all 20 diagonals are blocked; +z by cassette/cassette at 2 mm; -z by rotor_grp/roller_1 at 3 mm; +x by front/case_front at 2 mm; -x by front/case_front at 2 mm; +y by front/case_front at 2 mm; -y by front/case_front at 2 mm. Nearest blocker overall cassette/cassette along +z; reorder the steps, add an insert: direction, or open a path |
| PASS | Insertion, cassette/lever | 0.011 m |  | clear along +x (11 mm to leave the 37 parts present at step 'Cassette and tube'); blocked: +z by electronics/p_down at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, cassette/spring | 0.0035 m |  | clear along +x (4 mm to leave the 38 parts present at step 'Cassette and tube'); blocked: +z by cassette/cassette at 2 mm, -z by front/case_front at 2 mm |
| PASS | Insertion, door/door | 0.0035 m |  | clear along +x (4 mm to leave the 39 parts present at step 'Door and latch'); blocked: +z by cassette/lever at 3 mm, -z by cassette/spring at 9 mm |
| PASS | Insertion, door/latch | 0.00549 m |  | clear along +x (5 mm to leave the 40 parts present at step 'Door and latch'); blocked: +z by door/door at 6 mm, -z by door/door at 3 mm |
| PASS | Fastener heads not buried | 0 fasteners | 0 fasteners | no point 0.25 mm behind a bearing face lies in another solid of the body (4 screws) |
| PASS | Fastener engagement | 0 fasteners | 0 fasteners | all 4 screws engage their host or reach through their nut |
| PASS | Fasteners clear of bought parts | 0 fasteners | 0 fasteners | no shank or nut sits inside a bought part it does not thread into |
| PASS | Fastener heads and nuts clear of solids | 0 fasteners | 0 fasteners | no head or nut overlaps a solid of its body |
| PASS | Fastener stock lengths | 0 fasteners | 0 fasteners | all 4 lengths are stocked |
| PASS | Fastener driver access | 0 fasteners | 0 fasteners | every driven head has a free key path and hand space (4 screws) |
| PASS | Fastener BOM rows | 0 fasteners | 0 fasteners | all 4 BOM rows match their screw |

- interference: cassette/cassette, cassette/lever, cassette/tube, rotor_grp/roller_1, rotor_grp/roller_2, rotor_grp/roller_3
- mass.total: back/case_back, back/cell_1, back/cell_2, back/motor, front/case_front
- qa.mass_density: electronics/air, electronics/display, electronics/jack, electronics/p_down, electronics/p_up, electronics/sounder, electronics/sw_cass, electronics/sw_door, electronics/usb
- qa.insert.electronics/pcb: electronics/pcb, front/case_front
- qa.insert.electronics/display: electronics/display, electronics/pcb, front/case_front
- qa.insert.back/motor: back/case_back, back/motor, electronics/p_up, front/case_front, rotor_grp/worm_wheel
- qa.insert.back/worm: back/case_back, back/motor, back/worm
- qa.insert.back/cell_1: back/case_back, back/cell_1, front/case_front
- qa.insert.back/cell_2: back/case_back, back/cell_1, back/cell_2, front/case_front
- qa.insert.cassette/cassette: cassette/cassette, electronics/p_up, front/case_front, front/hinge_pin
- qa.insert.cassette/tube: cassette/cassette, cassette/tube, front/case_front, rotor_grp/roller_1
