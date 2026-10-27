# Electrical evidence and coverage ledger — 2026-10-27

**Scope:** 1997 Volvo 940 Turbo with EpicEFI Mega144H7 and existing DIYAutoTune-style relay/fuse board. This ledger tracks what is known about the **current physical installation**. It is neither a schematic nor a pinout. The references in `docs/ELECTRICAL_INVENTORY.md` and `docs/POWER_AND_GROUND_TREE.md` are the baseline, not independently verified hardware.

## Evidence grades

| Grade | Meaning | Can authorize a net/part rating? |
|---|---|---|
| V | Verified on current car by dated photo, continuity check, marking or measurement with conditions | Only for the exact fact measured |
| R | User-reported installed/current, not independently traced | No |
| H | Historical or previous ECU/board documentation | No |
| P | Planned/proposed | No |
| U | Unknown/unmeasured | No |

Each entry must distinguish a **connection observation** from a **measured electrical quantity**. A photo or written marking may identify a relay model but not its contact resistance; a voltage drop may locate a weak segment but does not establish branch current.

## Coverage by circuit

| ID | Circuit or junction | Present evidence | Still unknown | Required evidence to close |
|---|---|---|---|---|
| E01 | Alternator B+, battery+, charge feed | R (2026-10-27): separate 30 A fuse near battery on permanent feed into MS box X1; historic charging 13.9–14.0 V | Upstream fuse package, cable size, physical route/protection and loaded drop | Confirm wire gauge, fuse location as needed, voltage under load; do not adopt 30 A as new design rating |
| E02 | Relay-box power inlet | R (2026-10-27): X1 unswitched +12V (through external 30 A), X2 switched +12V, X3 engine ground; aligns with PDF labels | Physical input cable sizes/terminal condition, onboard F1 installed rating, loaded drop | Input functions confirmed by user; measure/characterize remaining unknowns |
| E03 | F1, K1, CB2 ECU branch | H: B&G 2002 V1.2 reference | Whether same devices actually fitted; relay/contact/polyfuse drop | Compare installed usage to `ORIGINAL_RELAY_BOARD_PDF_MAP.md`; only investigate physical board where revision/component behavior matters; segment drops |
| E04 | ECU main power | R (2026-10-27): cables from MS box terminate on ECU supply/ground screw terminals; both shared with H-bridge | Exact MS board output net/protection feeding ECU screw, conductor size, ECU current and terminal voltage | Determine actual relay-board output path; measure loaded voltage at ECU screw |
| E05 | ECU power return | R (2026-10-27): ECU and H-bridge share ECU ground screw, return cable originates at MS box | Internal MS box/X3 routing, cable gauge, loaded and dynamic return drop | Text mapping of box return plus ground-drop measurement |
| E06 | ECU sensor/reference ground | R: sensor systems installed | Sensor return pins and any shared high-current connection | Signal/reference continuity map, **no current injection into sensor ground** |
| E07 | DC idle H-bridge supply | R (2026-10-27): H-bridge + attached to ECU positive screw fed from MS box | Whether downstream of CB2 as historical PDF suggests; current/inrush, suppression, conductor gauge | Determine feed/net, measure H-bridge current and ECU supply disturbance under PWM |
| E08 | DC idle H-bridge return | R (2026-10-27): H-bridge - attached to ECU ground screw, supplied with MS-box ground cable | Return routing and common impedance; dynamic ground offset | Determine return path and measure loaded return drop/PWM disturbance |
| E09 | Fuel pump relay/branch | R: ECU PD10 command; pump installed | Coil wiring, independent failure mode, fuses, factory interaction, branch/return current | Relay state truth table + physical trace + measured current; verify stop/fault OFF |
| E10 | Injector B+ branches | R: four EV14 injectors/sequential ECU drivers | Fuse allocation, actual common feed, connector state | As-built +12V trace and protected current test |
| E11 | Wasted-spark coil supply/return | R: VAG 032 905 106B | Fuse, positive supply and power-ground termination | Written wiring trace, available part/terminal markings, pulse-noise observation |
| E12 | PWM 2-wire IAC | R: installed | Feed fuse, ECU low-side driver routing, diode/suppression | Wiring trace and driver-topology evidence |
| E13 | Upper/lower boost solenoids | R: installed; some temporary wiring | B+ branching, two driver returns, suppression and bracket | Trace both circuits independently by text/connection evidence |
| E14 | LC-1 heater and analog return | R: LC-1 installed | Heater feed/ground vs analog return | Pin-to-pin trace and supply/ground documentation |
| E15 | Fan branch | U: actual relay/power topology | Whether vehicle factory system or custom board supplies power | Trace relay, fuses, motors, control return |
| E16 | VSS, TPS, CLT, IAT, crank/cam | R: installed sensors | Connector/reference mapping | Pin-to-pin signal/ground inventory only |
| E17 | Fuel-pressure and future EMAP | R/P: current 200 PSI sensor; EMAP reuse later | Present 5V/reference; timing of rail change | Sensor trace, distinguish present and planned |
| E18 | Dash/CAN/auxiliary loads | P/partial | Current source, future allocations | Keep separate from critical supply until physically verified |
| E19 | Battery negative/chassis/engine strap network | H: one test under 0.1 V at a particular condition | Full topology; cold/hot loaded drop | Reported/verified connection routes, separate return-segment measurement |
| E20 | Actual box fuses, three relay housings | R: 30 A **external upstream** fuse installed; MINI fuses and three warm relay housings previously reported | F1–F4 onboard values, relay models, contact/PCB condition and thermal behavior | Keep 30 A external distinct from onboard F1; obtain readily known markings and loaded contact drops |

## Historical voltage observations (do not merge different test sessions)

| Observation | Date/context | Recorded value | Interpretation limit |
|---|---|---|---|
| Charging system versus ECU | Sep 2025, conditions incompletely recorded | 13.9–14.0 V vs about 13.2 V (roughly 0.7–0.8 V difference) | Different points; not a component-isolated drop |
| Board output versus ECU | 2025-09-14, common engine/star-ground reference | 13.56 V vs 13.35 V (0.21 V difference) | Downstream section, not necessarily one contact |
| Alternator to board inlet | Historical estimate | 0.34–0.44 V | Estimate, method and conditions need reconciliation |
| Battery minus to engine/star reference | Historical test | Less than 0.1 V | One operating condition, no PWM transient proof |
| Board inlet to ECU | May 2026 report | Approx. 0.2–0.5 V | Not necessarily comparable with September 2025 |

**Do not sum** these observations into one present-day loss estimate without simultaneous readings under identical load, RPM, temperature and meter references.

## Coverage rule

A circuit is **closed for inventory** only when source node, destination node, connector and pin, conductor, protection, relay/contact state, intended power return and date/source are documented. A circuit is **closed for electrical characterization** only after load-specific voltage drop and measured current (including startup/inrush as relevant) are recorded. For sensor circuits, use suitable non-invasive reference/signal checks, not power-load current injection.

## Work order

1. Start with the **two original relay-board PDFs**, transcribed in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`. Collect user-provided **text** mapping of actual X1–X3, JP1, JP2, fuse/relay usage and shared ECU/H-bridge screw terminals. Photos and access to PCB backsides are optional; avoid disturbing uncertain circuits.
2. As-built trace: E01–E09 and E19 first, particularly common ECU/H-bridge paths and fuel-pump shutdown logic.
3. Loaded supply and return measurements using `docs/ELECTRICAL_MEASUREMENT_WORKSHEET.md`.
4. Complete remaining actuator branches E10–E18, thermal/fault behavior and trace evidence.
5. Reconcile dated results and use them to define quantitative requirements and fault matrix. Only then reassess authorization to begin schematic design.

## Open findings

- **New conditional fault hypothesis:** The user reports H-bridge power/ground directly on ECU screw terminals fed from the MS relay box. The historical B&G drawing routes `12 RAW` through `CB2 RXE105`. **If** that physical ECU terminal is on this protected output and the CB2 component is actually installed, H-bridge PWM current could elevate drop or heat/trip the PTC; recovery after cooling could resemble the reported restart delay. Equally, common supply/ground impedance, wiring joints or H-bridge electrical noise remain plausible. Confirm actual protection/net before ranking causes. Do not bypass CB2 or the 30 A fuse as a diagnostic shortcut.

- Sharing the ECU supply/return screw terminal with a PWM H-bridge is a **plausible** common-impedance coupling mechanism. It is **not proven** to have caused the reported engine shutdowns.
- Three relay housings being warm does **not**, by itself, prove failing relays or excessive contact resistance.
- Current limits, conductor sizes and fuse/relay ratings cannot be selected from this ledger alone.
