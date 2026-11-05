# Hazards v1

A first list to steer the design. It is not an ISO 14971 risk file: there is no scoring and nothing here has been verified. The status of every control is "designed" at most.

| # | Hazard | Harm | Design control | Check |
|---|---|---|---|---|
| H1 | Free flow: feed runs in by gravity with the door open, the cassette out or the pump broken | Aspiration, overfeeding | Spring-closed pinch on the cassette. It only opens when the closed door pushes it. The rollers also occlude the tube when the door is shut | Bag 1 m above the pump, door open, cassette in and out: measure zero flow |
| H2 | Runaway motor | Over-delivery | Second processor reads an independent rotor encoder and can cut motor power. The self-locking worm stops the rotor when unpowered | Inject a fault into the main processor, confirm the cut-off and alarm |
| H3 | Silent under-delivery: slipping rotor, worn tube, stall | Dehydration, low blood sugar, missed medication | Encoder compares commanded against actual rotation. Downstream pressure and air sensors. Replace the tube every 24 h, as the manual requires for its sets | Weigh delivered water over 24 h at several rates |
| H4 | Occlusion missed, or too much pressure | Tube burst, a bolus when it clears, missed feed | Upstream and downstream pressure sensors with alarm limits from the manual | Dead-head test against a gauge. **Open:** the v1 occlusion wall is rigid. If it exceeds 40 psi, add a spring-loaded shoe |
| H5 | Alarm does not sound | All of the above go unnoticed | Second processor drives its own sounder and has its own backup power. Self-test at power on | Cut main power while running, confirm the alarm |
| H6 | Connected to the wrong line | Feed in a vein can be fatal | ENFit connector only (ISO 80369-3). Never a Luer | Inspection |
| H7 | Contamination | Infection | Only the single-use tube and sealed set touch feed. Printed parts never do. Tube and connectors must be food or medical grade | Material records |
| H8 | Battery fault | Fire, burns | Protected cells, charger chip with temperature cut-off, vented bay away from the tube | Charge and fault tests |
| H9 | Leak into the case | Short circuit, loss of the pump | Tube ports exit at the bottom so liquid drains away from the electronics. Bay is sealed from the case | Spill test |
| H10 | Wrong settings entered | Wrong dose | Confirm screen, rate lock, settings kept through power loss | Usability test |
| H11 | Firmware fault | Any of the above | Two processors, independent checks, hardware cut-off that firmware cannot override | Firmware not started. Follow IEC 62304 practice when it is |
