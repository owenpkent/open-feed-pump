"""Front half of the case, PETG, mm. Case coordinates: X forward (26 = split, 55 = front face; the door fills 55 to 58), Y left, Z up.
Holds the bulkhead (X 38 to 41) that seals the bay from the electronics (H9), the bay pocket (cassette recess), rotor boss with two bearing
seats, sensor pockets, display window, button holes, sounder grille, port holes and the hinge and latch features. Frames are the mount
points of everything that sits in it. Numbers are Brief v1 (estimated) except the choices noted in the BUILD_LOG.
Sensor sizes are passed in from assembly.yaml so the pockets always match the stand-ins."""
from build123d import Box, Cylinder, Plane, Pos, Rot, RectangleRounded, extrude

from nlcad.part import Frame, Part

X = (1, 0, 0)


def bx(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def cx(x0, x1, y, z, r):
    """Cylinder along X from x0 to x1 about (y, z)."""
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(r, x1 - x0)


def make(x_split=26.0, x_front=55.0, w=160.0, h=110.0, r=8.0, wall=2.5, rotor=(42.0, 66.0), leg_dy=16.8, tube_x=48.0,
         bay=(6.8, 77.2, 9.5, 96.5), p_size=(10, 8, 8), air_size=(12, 14, 10), sw_size=(6, 6, 6),
         p_up=(25.2, 42.0), p_dn=(58.8, 34.0), air=(58.8, 45.0), sw_cass=(12.0, 84.0), sw_door=(60.0, 102.0),
         hinge=(77.5, 56.0), latch=(1.85, 4.45, 43.0, 77.0), screw=(70.0, 10.0, 100.0), btn_r=3.2):
    ry, rz = rotor
    out = extrude(Plane.YZ.offset(x_split) * Pos(0, h / 2) * RectangleRounded(w, h, r), amount=x_front - x_split)
    cav = extrude(Plane.YZ.offset(x_split - 1) * Pos(0, h / 2) * RectangleRounded(w - 2 * wall, h - 2 * wall, r - wall),
                  amount=x_front - wall - x_split + 1)
    body = out - cav
    y0, y1, z0, z1 = bay
    body += bx(38, 41, y0 - wall, w / 2, z0 - wall, z1 + wall)           # bulkhead behind the bay, 3 thick (H9)
    body += bx(41, x_front, y0 - wall, w / 2, z0 - wall, z1 + wall)      # bay tray: walls around the pocket, cut out below
    for ly in (ry - leg_dy, ry + leg_dy):
        body += bx(41, x_front, ly - 8, ly + 8, wall, z0)               # solid under the tray at each tube leg, so a chute does not open into the case
    body += bx(50, x_front, 0, y0, latch[2] - 3, latch[3] + 3)           # latch boss
    body += bx(46, x_front, sw_door[0] - 4.5, sw_door[0] + 4.5, z1, h - wall + 0.1)   # door switch boss
    body += cx(28, 41.5, ry, rz, 8.0)                                    # rotor boss
    cut = bx(41, x_front + 1, y0, y1, z0, z1)                            # cassette pocket
    for ly in (ry - leg_dy, ry + leg_dy):
        cut += bx(tube_x - 4.4, x_front + 1, ly - 4.4, ly + 4.4, -1, z0 + 1)   # tube chutes, open to the front so the cassette drops straight in
    cut += cx(27, 41.01, ry, rz, 5.5)                                    # bearing bore, 11
    for (y, z), s, xc in ((p_up, p_size, 39.8), (p_dn, p_size, 39.8), (air, air_size, 45.8), (sw_cass, sw_size, 38.0)):
        cut += bx(xc - s[0] / 2 - 0.2, 41.5, y - s[1] / 2 - 0.2, y + s[1] / 2 + 0.2, z - s[2] / 2 - 0.2, z + s[2] / 2 + 0.2)
    cut += bx(52 - sw_size[0] / 2 - 0.2, x_front + 0.5, sw_door[0] - 3.2, sw_door[0] + 3.2, sw_door[1] - 3.2, sw_door[1] + 3.2)   # door switch
    for hz, hl in HINGE:
        cut += Pos(x_front, hinge[0], hz) * Cylinder(1.55, hl + 0.4)       # hinge pin grooves, top and bottom: the cassette passes between them
    ly0, ly1, lz0, lz1 = latch
    cut += bx(x_front - 3.2, x_front + 1, ly0 - 0.2, ly1 + 0.2, lz0, lz1)  # latch catch pocket
    cut += bx(x_front - wall - 0.1, x_front + 1, -61, -7, 65, 101)        # display window, 54 x 36 active area
    for k, (y, z) in enumerate(BTN, 1):
        cut += cx(x_front - wall - 1, x_front + 1, y, z, btn_r)
    for dy, dz in ((-1.5, 0), (1.5, 0), (0, 2.6)):
        cut += cx(x_front - wall - 1, x_front + 1, -8 + dy * 2, 45 + dz, 1.2)   # sounder grille
    cut += bx(46.0, 50.1, -67.2, -56.8, -1, wall + 1) + bx(45.9, 51.9, -25.2, -18.8, -1, wall + 1)   # USB-C and jack openings
    body = body - cut
    sy, bz0, bz1 = screw
    frames = {"origin": Frame((0, 0, 0)), "split": Frame((x_split, 0, 0), z=X), "cassette_seat": Frame((41.0, ry, bay[2] + 0.5), z=X, x=(0, 1, 0)),
              "pressure_up": Frame((39.8, *p_up)), "pressure_down": Frame((39.8, *p_dn)), "air": Frame((45.8, *air)),
              "sw_cass": Frame((38.0, *sw_cass)), "sw_door": Frame((52.0, *sw_door)),
              "pcb": Frame((45.6, -46.0, 56.0)), "display": Frame((50.5, -34.0, 83.0)),
              "sounder": Frame((47.75, -8.0, 45.0), z=X), "usb": Frame((48.05, -62.0, 3.65)), "jack": Frame((48.9, -22.0, 5.5)),
              "bearing_front": Frame((39.0, ry, rz), z=X), "bearing_rear": Frame((30.0, ry, rz), z=X), "hinge_top": Frame((x_front, hinge[0], HINGE[0][0])), "hinge_bot": Frame((x_front, hinge[0], HINGE[1][0]))}
    for k, (y, z) in enumerate(BTN, 1):
        frames[f"btn_{k}"] = Frame((x_front, y, z), z=X)
    for k, (sy_, z) in enumerate([(-1, bz0), (1, bz0), (-1, bz1), (1, bz1)], 1):
        body += cx(x_split, x_split + 10.0, sy_ * sy, z, 4.0)
    for k, (y, z) in enumerate(((-72, 52), (-20, 52), (-72, 22), (-20, 22)), 1):
        body += cx(46.4, x_front - wall + 0.5, y, z, 2.5)                  # PCB standoffs
    return Part(shape=body, frames=frames, density_kg_m3=1270, material="PETG", provenance="estimated",
                bom={"description": "Case, front half with bay, bulkhead, printed PETG", "source": "estimated: Brief v1"})


HINGE = ((102.0, 8.0), (6.0, 6.0))                                                  # (z centre, length) of the two hinge pin stubs
BTN = ((-66.0, 30.0), (-46.0, 30.0), (-26.0, 30.0), (-58.0, 12.0), (-34.0, 12.0))   # Menu, minus, plus, Prime, Run/Hold (Brief v1 sketch)
