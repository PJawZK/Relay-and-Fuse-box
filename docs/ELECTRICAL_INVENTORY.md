# Electrical inventory — installed vs planned (2026-10-27)

**Purpose:** A starting inventory compiled from older Volvo 940 Turbo ECU project discussions. This is **not** a verified as-built harness map. Each entry must be compared with the car and latest ECU/tune before drawing a replacement PCB.

Evidence labels: **reported installed** = user reported installation, not independently inspected; **planned** = future/unfinished; **historical** = earlier configuration, do not assume still installed; **verify** = topology or part assignment not established.

| Circuit/component | State | Known information | Power-path / ground-path status | Action |
|---|---|---|---|---|
| ECU | Reported installed | EpicEFI Mega144H7 with Speeduino 0.4.3C adapter, October 2026 firmware | ECU main feed through old DIYAutoTune/MS relay system; exact real-life terminals and fusing unverified | Document exact ECU B+, ignition feed, controller and sensor grounds |
| Relay/fuse box | Reported installed | DIYAutoTune/MegaSquirt-type relay box aged about 15–16 years, three warm relay housings recently reported; MINI fuses; **separate 30 A upstream fuse near battery** confirmed by user report 2026-10-27 | X1 permanent +12 V through external 30 A; X2 switched +12 V; X3 engine ground, per current user text. Original B&G schematic V1.2/layout V1.1 silkscreen mapped in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`; physical revision and onboard F1 remain unknown | Capture JP1/JP2 actual uses by **text**; distinguish upstream 30 A from onboard F1; record fuse/relay markings when known |
| Alternator / charging | Reported installed | Regulator replaced, typically 13.9–14.0 V measured | Alternator/battery relay-box input routing, fusible link and ground return need tracing | Diagram charging and engine-ground links |
| Fuel pump | Reported installed / planned upgrade | Fuel pump output at Mega144H7 PD10; existing in-tank ~110 L/h, 255 L/h replacement planned | Actual relay coil, output wiring, downstream factory circuit and grounds need verification | Current, cold/hot startup inrush, ignition-off fail-safe |
| Injectors | Reported installed | Bosch EV14 0280158117, sequential; four channels via NCV8403A drivers. Connector swap noted pending | +12V fuse assignments and distribution point unresolved | Trace each 12V feed and driver return; verify which upgrades finished |
| Ignition | Reported installed | VAG wasted-spark coil 032 905 106B, IGN1/IGN3 | Coil +12V branch, noise suppression and high-current ground unknown | Trace 12V and engine-ground pathway |
| PWM IAC valve | Reported installed | Bosch 2-wire PWM; Mega144H7 and driver changes restored IAC | Steady +12V supply vs ECU low-side path to verify; older advice was to avoid switching PWM through mechanical relay | Verify source fuse and driver topology |
| DC idle H-bridge | Reported installed DIY circuit | H-bridge positive and ground landed on **the ECU's own positive and ground screw terminals**, which also receive supply/return cables from the MS box (user confirmed 2026-10-27) | This common junction makes supply/return coupling plausible; whether both loads sit downstream of the B&G-reference CB2 polyfuse remains **unknown** | Trace exact MS-board ECU output net, measure PSU/return disturbance and branch current; design independent protected feed/return later |
| Boost control | Reported installed | Two Pierburg-type solenoids, upper/lower open-loop tables, one bracket/wiring temporary | +12V and driver/ground wiring need tracing | Include each solenoid and flyback arrangement |
| Fuel pressure | Reported installed / planned change | Existing 200 PSI rail sensor; custom fuel rail, regulator and replacement FP sensor pending | Sensor power/reference/ground and +12V actuator loads as applicable | Mark replacement dependency before EMAP reuse |
| EMAP | Planned | Existing 200 PSI sensor to be reused after fuel-rail swap, analog input on Mega144H7 | Sensor reference/ground routing still planned | Reserve protected sensor wiring, **not high-current relay output** |
| EGO | Reported installed | Innovate LC-1 LSU 4.2, analog output changed during project | Heater +12V and heater ground vs analog reference must be traced | Verify heater circuit separate from sensor ground |
| Electric fan | Existing ECU control / harness verify | Fan output power stage/relay in current setup not established | Factory relay vs project box topology unknown | Don't presume relay-box ownership |
| VSS | Reported installed | Cluster/VSS BC547 conditioner, signal issues previously repaired | Signal ground and power separate from motor return | Document signal/reference only |
| Dash/CAN nodes | Planned / partial | ESP32-S3 cluster nodes, 500 kbps CAN bus, power distribution developing | Future loads not to be silently merged into engine-critical feeds | Reserve optional AUX fuse only |
| Crank/cam/TPS/CLT/IAT | Reported installed | Engine sensors and cam sync; CLT 8653103 isolated 2-pin | Dedicated sensor grounds and 5V references must **not** be routed through power relay distribution indiscriminately | Current harness pin-by-pin map |
| AOS and mechanical hardware | Planned | No electrical power allocation expected | Out of scope unless sensor/heater added | Track dependencies separately |

## Previous wiring assertions that must not be treated as current pinouts
- 2025 Speeduino DB37 mapping included fuel-pump pin 37, main +12V pin 28 and shared DB37 sensor wiring. Current Mega144H7 and adapter mapping may differ.
- Prior reports describe different injector and IGN pin maps across ECU revisions. **Do not copy these values into the new PCB netlist without checking the actual assembled harness.**
- Original B&G board documentation includes a fast-idle relay; the current PWM IAC and separate DC idle H-bridge are not equivalent functions.
- A separate EpicECU-Beta wiring master exists for another future ECU: `EpicECU-Beta_Wiring_Assignments.md` and diagram `EpicECU-Beta_Wiring_Diagram_v0.8.drawio`. **Do not treat Beta Lxx/Sxx cavity allocations as the current Mega144H7 installation.**

## Source and measurement status
- Historical measurements are captured in root README. The original B&G PDFs were supplied in conversation; their source-derived terminal/component details are now transcribed in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`. Binary PDFs are not yet in the repository.
- Loaded **current** of each circuit has not been measured.
- Box input/output, relays, fuses and polyfuses have not been separately probed under the same load in a complete segment-by-segment test.
- Any vehicle-critical fuse value, wire gauge, terminal rating, topology and ground stud remains **TBD until verified**.

## Circuit trace record (fill one row per physical connection)
| From node / terminal | To node / terminal | Conductor gauge | Connector and pin | Fuse | Relay | Operating current | Start/inrush current | Ground return | Evidence/date |
|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | Not measured | Not measured | TBD | Awaiting as-built inspection |

## Next physical inspection

**Already established in user text (2026-10-27):** X1 permanent via separate 30 A upstream fuse; X2 switched power; X3 engine ground; ECU and H-bridge share ECU positive/ground screw terminals, with wires from MS box. These do not need to be asked or photographed again. The 30 A part is **not** the schematic's F1.

1. Use the source-derived X1–X3, JP1 (20 pins), JP2 (4 pins), F1–F4 and K1–K3 mapping in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`; collect **text descriptions** of present wire destinations, used/unused terminals and readily known fuse/relay details. Photographs optional, not prerequisite.
2. Voltage measured relative to the **same ground reference** at alternator B+, board input, each fuse inlet/outlet, K1 contacts, CB2 (if fitted), board output and ECU B+ while operating.
3. Current of each separately isolated load branch using an appropriately rated instrument and test method.
4. Separate chassis, battery, engine, ECU, sensor, coil and H-bridge return points on a ground-tree drawing.
5. Update every 'reported installed' claim to 'verified installed' only with measurements, physical tracing or current schematic evidence.

## Traceability and capture (2026-10-27)

Use [the evidence/coverage ledger](ELECTRICAL_EVIDENCE_LEDGER.md) for circuit IDs E01–E20 and current proof gaps. Record new vehicle observations in [the physical inspection and measurement worksheet](ELECTRICAL_MEASUREMENT_WORKSHEET.md) before upgrading any entry from **reported installed** to **verified installed**. Keep each measurement session separate; do not blend September 2025 and May 2026 observations into a single simultaneous drop budget.
