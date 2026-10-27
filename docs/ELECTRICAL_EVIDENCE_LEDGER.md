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

**Architecture correction (R, 2026-10-27):** The present Mega144H7/EpicEFI engine management uses an independent aftermarket wiring/relay/fuse system, and **none of the original Volvo EFI wiring, fuses or relays are in service for EFI**. Original factory injection relay positions can be evaluated for new uses; don't confuse factory LH relays with the currently installed *aftermarket* MS relay box. See `VOLVO_FACTORY_RELAY_REUSE_RESEARCH.md`.

## Coverage by circuit

| ID | Circuit or junction | Present evidence | Still unknown | Required evidence to close |
|---|---|---|---|---|
| E01 | Alternator B+, battery+, charge feed | R (2026-10-27): separate 30 A fuse near battery on permanent feed into MS box X1; historic charging 13.9–14.0 V | Upstream fuse package, cable size, physical route/protection and loaded drop | Confirm wire gauge, fuse location as needed, voltage under load; do not adopt 30 A as new design rating |
| E02 | Relay-box power inlet | R (2026-10-27): X1 unswitched +12V (through external 30 A), X2 switched +12V, X3 engine ground; aligns with PDF labels | Physical input cable sizes/terminal condition, onboard F1 installed rating, loaded drop | Input functions confirmed by user; measure/characterize remaining unknowns |
| E03 | F1, K1, CB2 ECU branch | **R 2026-10-27:** MS box internal power circuit unmodified/stock, with no CB2 bypass or removal reported. **H:** B&G V1.2 schematic routes K1→CB2→12 RAW; B&G BOM permits RXE105 **or** RXE110 | Actual fitted CB2 identity, whether current ECU feed uses 12 RAW, relay/contact/polyfuse drop | Confirm ECU feed source and measure protected path under normal load; retain fitted part number as unknown |
| E04 | ECU main power | R (2026-10-27): cables from MS box terminate on ECU supply/ground screw terminals; both shared with H-bridge | Exact MS board output net/protection feeding ECU screw, conductor size, ECU current and terminal voltage | Determine actual relay-board output path; measure loaded voltage at ECU screw |
| E05 | ECU power return | R (2026-10-27): ECU and H-bridge share ECU ground screw, return cable originates at MS box | Internal MS box/X3 routing, cable gauge, loaded and dynamic return drop | Text mapping of box return plus ground-drop measurement |
| E06 | ECU sensor/reference ground | R: sensor systems installed | Sensor return pins and any shared high-current connection | Signal/reference continuity map, **no current injection into sensor ground** |
| E07 | DC idle H-bridge supply | **R installed:** H-bridge + attached to ECU positive screw fed from MS box. **P change (2026-10-27):** move to a separate fused, switched factory-relay-fed branch | Whether existing path traverses CB2; prospective factory relay branch spare capacity, current/inrush, fuse/conductor suitability, flyback/EMI | Identify independently protected switch source and **separate power-ground return**, check relay loading and safe loss-of-power behavior, then re-log |
| E08 | DC idle H-bridge return | **R installed:** H-bridge - attached to ECU ground screw via MS-box ground cable. **P change:** move H-bridge power return away from ECU ground screw | Factory star/engine/chassis return point, conductor resistance, transient coupling | Choose appropriate dedicated actuator-current return and verify no ECU/sensor-ground sharing |
| E09 | Fuel pump relay/branch | R (2026-10-27): ECU PD10 command, pump installed, **fully new aftermarket EFI wiring/relay/fuse**. Original Volvo EFI fuel relay is **not part of current pump circuit** | Exact installed aftermarket coil wiring, branch/return current, stop/fault behavior | New-system relay state truth table and current/return measurement; preserve fuel-pump stop/fault OFF |
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

## Stock relay-board update — 2026-10-27

User reports **no internal modifications** to the MS box, including no bypass or removal of CB2. Because the original design uses CB2 in the ECU `12 RAW` line, it is now **reasonable to prioritize** this path for measurement; actual fitted part/revision remains uninspected. The B&G bill of materials names RXE105 *or* RXE110, so rating must not be assumed from schematic label alone.

Reference RXE110 from Raychem data (not installed-device proof): 1.10 A hold at 20°C, 0.69 A hold at 60°C, 2.20 A trip at 20°C, 0.15–0.25 Ω initial at 20°C. At 1 A this corresponds to 0.15–0.25 V *illustrative room-temperature device drop* before contact/wire losses; do not use this as the car's measured drop. Links and qualifications: `ORIGINAL_RELAY_BOARD_PDF_MAP.md`.

## Prior log-based supply evidence — October 26, 2026

**Provenance:** The following timings were extracted in the earlier ECU idle-control log analysis and are preserved as **prior analysis**, not newly recalculated in this repository. The most recent library upload appears as `2026-10-26_20.51.28.mlg.zip`; its raw bytes could not be rematerialized in the current project runtime on 2026-10-27, so no new independent raw-log validation is claimed.

| Recorded interval (log seconds) | Prior extracted observation | Interpretation boundary |
|---|---|---|
| 590–605 | Calm DC control; ECU VBatt minimum ~13.41 V; peak absolute H-bridge command ~49.6; about 0 direction reversals/s | Reference interval, not a whole-session baseline |
| 650–660 | Aggressive DC loop; ECU VBatt minimum ~10.67 V, peak absolute H-bridge command ~140, ~41 command reversals/s; outer D abs P95 42.4 and inner D abs P95 45.3 (versus 1.3/2.3 calm) | Association of high actuator activity with depressed logged supply; does not isolate CB2, ground return, supply relay or ADC artifacts |
| 657.85–662.75 | Reported VBatt <12 V at 657.85 s, <10 V at 660.78 s; logged IGN activity loss ~661.20 s while RPM ~952; RPM zero ~662.75 s | Voltage decline **preceded** shutdown; logged voltage is ECU-referenced measurement, not simultaneous battery-post voltage |
| ~714.79–716.39 | Second logged IGN loss ~714.79 s, engine zero RPM ~716.39 s | Same general ignition-before-stop sequence; local pre-event voltage pattern needs raw-log verification |
| ~1724.35–1725.8 | Final logged IGN loss and engine stop; prior analysis found outer D near zero during 1710–1724 s | High outer D cannot be claimed as the universal cause of every shutdown |
| Restart attempts | Failed crank/restart intervals ~676.53–680.07 s and ~726.85–730.35 s, later successful starts | Recovery delay may be consistent with several thermal, supply, connection or control issues; no PPTC trip has been proven |

**Measurement interpretation:** The ECU's `VBatt` channel measures the ECU's electrical environment through its input/scaling chain, and cannot tell where the voltage was lost. A drop under H-bridge PWM while RPM remains nonzero supports prioritizing shared PSU/return/CB2 investigation, but does not prove the battery, alternator, board polyfuse, wiring joint or H-bridge individually failed. Check for input calibration/reference distortion and log sampling limitations.

### Planned H-bridge supply relocation (not yet implemented)

The user plans to remove H-bridge motor positive and return from the **ECU** screw terminals, using a separate **switched and fused** source from the vehicle's factory relay system. Candidate existing fuel/ECU relay feeds are *not yet approved* merely because they are switched.

- **Distinguish abandoned OEM LH relay positions from new EpicEFI pump relay:** former Volvo 2/23 injection relay may be a candidate because none of its old EFI loads are used, but its original ECU-controlled coil may no longer energize. Never parallel the **currently operating aftermarket pump motor feed** or compromise EpicEFI fuel-pump shutdown.
- A repurposed **original Volvo** injection/system relay can be considered after its socket feed and coil switching are identified, and the H-bridge is protected independently. It must not be confused with **K1 in the current MS aftermarket relay box**: a new fuse *after* CB2 would still leave H-bridge load on CB2.
- Prefer an otherwise suitable ignition-switched, independently fused actuator/accessory supply and separate **actuator power return** with adequate current and automotive suppression; do not route motor return through ECU or sensor ground.
- Record the existing factory relay identity, existing loads, conductor size, voltage under load and fuse protection before connection; the presence of a spare fuse slot or relay output does not establish spare current capacity.
- Test loss-of-power behavior of the throttle-plate DC idle actuator before in-car service. A disconnected H-bridge must not leave throttle in an unsafe position; keep the ECU/fuel-pump engine-stop safety logic intact.
- Capture **same-channel, same-calibration** ECU VBatt and idle/PID data before and after relocation during similar normal load, temperature and RPM conditions; do not intentionally recreate dangerous shutdowns.

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
