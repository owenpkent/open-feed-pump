# Brief v1, feed-pump

A portable rotary peristaltic enteral feeding pump. Requirements and their sources: [docs/Requirements v1.md](../../docs/Requirements%20v1.md). Safety intent: [docs/Hazards v1.md](../../docs/Hazards%20v1.md). This is an original layout: do not reproduce the look of any commercial pump.

All numbers here are estimated unless stated, and are design intent for the first build.

## Frame and envelope

Millimetres. Z up, X forward, Y left, as nl-cad requires. The case is 58 deep (X 0 at the back to 58 at the front), 160 wide (Y -80 to +80) and 110 high (Z 0 to 110). Rounded corners, about 8 mm radius.

## Sketch (front view, looking at the pump along -X, so +Y is on the viewer's right)

```
 Y=-80                 Y=0                   Y=+80
  +----------------------+----------------------+  Z=110
  |  +----------------+  |  +----------------+  |
  |  |    display     |  |  |  door (clear)  |  |
  |  |    60 x 42     |  |  |     _____      | H|
  |  +----------------+  |  |   /  ( )  \    | I|   rotor axis at
  |                      | L|  |  rotor  |   | N|   Y=+42, Z=66
  |  [Menu] [ - ] [ + ]  | A|  |         |   | G|
  |                      | T|  |         |   | E|
  |  [Prime]  [Run/Hold] | C|  |in|   |out|  |  |
  |                      | H|  |  |   | p |  |  |   p = pinch on the outlet leg
  +----------------------+--+--+--+---+---+--+--+  Z=0
                               |  |   |   |
                     tube legs exit through the bottom edge
```

Side section (looking along +Y): the door is at the front, then the cassette in a recess, then a bulkhead, then the rotor shaft runs back through two bearings to the worm wheel. The motor lies flat across the case. The battery lies along the bottom at the back.

## Joints first

| Joint | Type | Parent, child | Location | Range |
|---|---|---|---|---|
| rotor | revolute (continuous) | case, rotor | Axis along X at Y=+42, Z=66 | Full turn |
| roller_1, 2, 3 | revolute (continuous) | rotor, roller | Axis along X, 13.3 from the rotor axis, 120 degrees apart | Full turn |
| door | revolute | case, door | Axis along Z at about Y=+78, X=58 | 0 (shut) to about 100 degrees open |
| pinch | revolute | cassette, pinch lever | Axis along X on the cassette | Closed to open, enough for the gaps below (about 22 degrees on a 14.4 arm) |
| latch | prismatic | door, latch | Along Z on the free edge of the door | About 6 mm |

The door must swing clear of the case and everything else across its range.

## Pumping head

- **Tube:** silicone, 3.2 ID x 6.4 OD. Inverted U: it runs up the inlet leg, wraps 180 degrees over the top of the rotor, and runs down the outlet leg. Legs are straight, centred at Y = 42 +/- 16.8, and exit the bottom edge of the case. Show about 15 mm of tube below the case.
- **Inlet and outlet:** the leg at smaller Y is the inlet, and the leg at larger Y is the outlet.
- **Cassette (the open consumable, about 70 W x 80 H x 14 D):** a single plastic plate, printable or moulded, that holds the tube in a channel and has a rigid arc wall of **20.0 radius** on the rotor axis, on the outside of the tube. It drops straight into a recess in the front of the case. A cut-out lets the rotor reach the tube. It carries the pinch lever, and it has two flexible snap tabs at the top for low-force loading.
- **Rotor:** three rollers, 8.0 OD x 8 wide, with centres on a 13.3 radius. The roller's outer edge is therefore 17.3 from the rotor axis, leaving a 2.7 gap to the arc wall: about 85% of the 3.2 total of two tube walls. This squeeze is the most important number in the pump. The tube is modelled uncompressed, so the rollers will overlap it: this is **expected**, and should be accepted in the checks with that reason, not designed out.
- **Pinch lever (safety, hazard H1):** on the outlet leg below the rotor. A torsion spring closes it onto the tube by default (a spring stand-in is fine). A pin on the inside of the door pushes it open when the door is fully shut. Door open or cassette out means tube pinched. **Closed, the jaw must reach no more than 2.2 from the anvil** (about 70% of the 3.2 total of two tube walls, tighter than the rollers because a flat pinch leaves small channels at the tube's edges). **Open, it must stand at least 1.0 clear of the tube**, so print tolerance cannot leave it dragging. That needs about 5.2 of jaw travel. Whether the spring actually seals the tube against a 1 m head is a bench test (hazard H1): geometry can only allow it.

## Drive

Rotor shaft along X, diameter 5, with two 5 x 11 x 4 bearings (MR115 or similar) in the bulkhead. Worm wheel module 0.5, 30 teeth (15 pitch diameter), near the back of the shaft. Worm on the shaft of a **NEMA 11** stepper (28 x 28 x 32 body) lying flat with its axis along Y and its body toward -Y. The centre distance between worm and wheel is about 11.5, so the motor axis is at about Z=54.5. A diametric magnet on the back end of the shaft faces a small encoder board (AS5600 stand-in).

Model gears as plain cylinders at pitch diameter: real teeth are not needed. Accept their nominal touching in the checks.

## Sensors in the head (stand-ins at real envelope)

On the case side of the cassette, reaching the tube through windows: upstream pressure sensor on the inlet leg, and downstream pressure sensor on the outlet leg above the pinch, each about 8 x 8 x 10. Optical air sensor on the outlet leg, about 14 x 10 x 12, straddling the tube. A door switch and a cassette-present sensor, each about 6 x 6 x 6.

## Electronics and power (all stand-ins)

- **Main board:** about 100 x 60 x 1.6 PCB with 8 mm of component height, parallel to the front face, behind the display on the -Y half.
- **Display:** 60 x 42 x 4, on the -Y half of the front face, upper.
- **Keypad:** five silicone buttons, each at least 15 across, on the -Y half of the front face, lower. Labels are not needed. Must be pressable: leave room behind.
- **Battery:** protected 2S 18650 pack, 2 cells in line or side by side, in a bay along the bottom at the back. Cells 18.5 diameter x 65.
- **Sounder:** 12 diameter x 9.5, behind a small grille.
- **Ports in the bottom edge, on the -Y half:** USB-C and a 3.5 mm assistive switch socket.

## Case

- **case_back:** the rear half, holding the motor, battery, boards. An AMPS pattern on the back face: 4 x M4 holes at 30 x 38 centres, with inserts.
- **case_front:** the front half with the bay recess, the bulkhead that seals the bay from the electronics (hazard H9), the display window and button holes.
- **door:** clear polycarbonate, 3 thick, hinged on the +Y side and covering the bay. Carries the pinch pin and a slot for the tube legs at the bottom edge.
- **latch:** a slider on the free edge of the door, operated by a single push with a palm or knuckle, with no pinch grip.
- Join case_front and case_back with four M3 screws from the back, in bosses at the corners, using the nl-cad `fasteners:` list. The door hinge uses a 3 mm steel pin.
- Materials: PETG for prototype structure (density 1270), PC for the door (density 1200), silicone for the tube and buttons (density 1100). Printed walls about 2.5 thick.

## Numbers to check in the build

Add these to the build as checks if nl-cad allows it, otherwise report them from the geometry: squeeze gap 2.7 at the arc wall; envelope no larger than 58 x 160 x 110; total mass no more than 600 g; a roller is at the arc wall at every rotor angle across the 180 degree wrap; the door pin reaches the pinch lever when shut; door swing clear.
