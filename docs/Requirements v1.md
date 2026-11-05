# Requirements v1

Reference values come from the [Infinity Operator's Manual](https://infusystem.com/images/catalog_manuals/English/Enteral_Pump_Manual/EnteraLite_Infinity_Operators_Manual_ENG-FRE_.pdf), section 7 (cited below as "manual"). Targets marked "estimated" are design calls that bench testing must confirm.

## Performance

| Item | Reference (manual) | Our target | Basis |
|---|---|---|---|
| Mechanism | Rotary peristaltic | Rotary peristaltic, 3 rollers | Published |
| Rate range | 0.1 to 600 mL/hr | Same | Published |
| Rate step | 0.1 mL/hr to 10 mL/hr, then 1 mL/hr | Same | Published |
| Prime rate | 700 mL/hr, alarms off while priming | Same | Published |
| Accuracy | +/- 5% | +/- 5%, checked by weighing delivered water | Published |
| Dose | 0.1 to 3000 mL, or infinite | Same | Published |
| Interval feeding | Yes | Yes | Published |
| Max pressure | 40 psi (276 kPa) dead head | No more than 40 psi | Published |
| Orientation | Any | Any | Published |
| Ingress | IP42 | IP42 goal, not testable on a printed prototype | Published |
| Operating range | 5 to 40 C, 10 to 95% RH | Same | Published |

## Size and power

| Item | Reference (manual) | Our target | Basis |
|---|---|---|---|
| Size | 49 D x 144 W x 103 H mm | 58 D x 160 W x 110 H mm for the first build, then shrink | Estimated |
| Weight | 411 g | 600 g or less | Estimated |
| Battery | Li-ion, 24 h at 125 mL/hr, 9 h at 600 mL/hr | Same run times from a protected 2S 18650 pack, about 24 Wh | Estimated |
| Charger | 5 V, 3 A | USB-C, 5 V, 3 A | Published |

**Power budget (estimated):** about 1.5 W with the motor running plus 0.1 W for electronics. At 125 mL/hr the motor runs in short bursts and stops between them, about 18% duty, so the average is about 0.4 W, or 10 Wh over 24 h. At 600 mL/hr it runs continuously at about 1.6 W, or 14 Wh over 9 h. Both fit a 24 Wh pack.

## Alarms

| Alarm | Reference (manual) | Our target |
|---|---|---|
| Upstream occlusion | -5 psi (-34 kPa), +/- 3 psi | Same |
| Downstream occlusion | 12 psi (83 kPa), +/- 3 psi. Time to alarm: 5 min at 125 mL/hr, 2 h at 1 mL/hr, 12 h at 0.1 mL/hr | Same pressure, and no slower |
| Bolus after occlusion clears | Up to 1 mL | No more than 1 mL |
| Air in line, empty bag | Optical sensor | Optical sensor |
| Door opened while running | Alarm | Alarm, and the tube pinches shut |
| Cassette not loaded | Alarm | Alarm, and the motor will not start |
| Low battery | Alarm | Alarm |
| Self-test failure | Error codes | Error codes, and motor power cut |
| Rotor not turning as commanded | Not listed | Alarm, from an independent encoder |
| Main processor stops responding | Not listed | Alarm from the second processor, and motor power cut |

## Mechanism numbers (estimated, to calibrate)

| Item | Value | How derived |
|---|---|---|
| Tube | Silicone, 3.2 mm ID x 6.4 mm OD | Common stock size, wall 1.6 mm |
| Delivery per rotor turn | About 0.9 mL | 3 pockets x (2 x pi x 18 mm / 3) x 8.04 mm2 bore |
| Rotor speed at 600 mL/hr | About 11 rpm | 600 / 0.9 / 60 |
| Rotor speed when priming | About 13 rpm | 700 / 0.9 / 60 |
| Drive | NEMA 11 stepper, 30:1 worm | Self-locking, so power can be off between bursts |
| Delivery per full step | About 0.00015 mL | 0.9 / (200 x 30) |
| Rotor torque needed | About 0.15 N m | 0.04 N m to hold 276 kPa, plus an estimated 0.1 N m to roll over the tube |
| Rotor torque available | About 0.6 N m | 0.06 N m motor x 30 x 0.35 efficiency |

## Usability

Designed for people with limited hand function, including wheelchair users. Where a choice trades convenience for these users against size or cost, these users win.

- Door and cassette load with one hand and low force, with no pinch grip needed.
- Five large buttons, at least 15 mm across: Run/Hold, plus, minus, Menu, Prime.
- A 3.5 mm socket for an assistive switch that acts as Run/Hold.
- An AMPS hole pattern on the back (30 x 38 mm, M4) for wheelchair mounts and pole clamps. Confirm the pattern against a real plate before printing.
- Alarms can be both heard and seen.

## Regulatory context

This repo does not seek clearance. These are recorded so the design does not paint itself into a corner.

| Item | Note | Status |
|---|---|---|
| US classification | Enteral pumps are product code LZH under 21 CFR 880.5725, Class II. See [K131154](https://fda.innolitics.com/device/K131154.md) | From 510(k) summaries, regulation text not read |
| [ISO 20695:2020](https://standards.iteh.ai/catalog/standards/iso/18415ed4-1a08-4ed9-80ce-ebf703e50d7e/iso-20695-2020) | Enteral feeding systems, design and testing | Abstract read only |
| ISO 80369-3 (ENFit) | Patient-side connector | Abstract read only |
| [IEC 60601-2-24](https://webstore.iec.ch/publication/2635) | Infusion pumps. Whether it covers enteral pumps is **not confirmed** | Check the scope |
| IEC 60601-1, IEC 60601-1-8, IEC 62304, ISO 14971 | General safety, alarms, software, risk management | From memory, not checked |
| Patents | Not covered in this repo | Have counsel review before anyone builds this to sell |
