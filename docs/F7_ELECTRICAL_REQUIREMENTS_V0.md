# F7 — electrical requirements baseline (v0.2)

_2026-11-02 · design requirements / validation plan · **F7 OPEN — numbers not yet qualified**_

## Design intent

A **passive / minimally complex low-drop 12 V automotive power-distribution board** replaces only functions now served by the aging aftermarket MS/DIYAutoTune board. It must remain serviceable, protect each relevant load/wire, retain Mega144H7/EpicEFI shutdown controls and operate correctly through ignition, cranking and vehicle supply disturbances. The factory Volvo LH2.4 relay system is out of scope. The newly installed H-bridge relay and wiring are out of the board by default.

Mandatory new hardware details (ampere limits, mΩ, fuse sizes, copper width, connector rating, wire cross-sections) **cannot be signed off from the 2002 B&G schematic**, the estimated 4 mm² X1 cable, or unlabeled existing fuses. Use current installed measurements, manufacturer datasheets and actual mounting environment. Define baseline as **system capability**, and each gate's electrical quantity as **TBD until verified**.

## High-level functional requirements and test evidence

| ID | Requirement | Preliminary status / acceptance method |
|---|---|---|
| R01 | Source distribution accepts actual 12 V vehicle supply, ignition OFF/RUN/START and charging conditions without unexpected latching or backfeed | Must test OFF/RUN/START, battery and alternator operating ranges; exact electrical min/max and fault pulses TBD |
| R02 | ECU main feed has independently serviceable branch protection and switches when required | Determine Mega144H7 minimum input operating voltage and cold-cranking behavior; measure ECU B+ vs board input during normal and starting loads |
| R03 | **Fuel pump cannot remain energized solely due to an absent/stalled/booting ECU control command**, beyond verified prime policy | Directly document actual ECU PD10 control polarity, current, output state during reset and stop; test on isolated safe bench/controlled stationary vehicle only |
| R04 | Loss of ignition key control removes selected relay outputs; power-on sequencing must not inadvertently supply injectors or coil with stalled/absent ECU | Capture OFF/RUN/START truth table; ensure ignition feed isn't confused with constant battery feed |
| R05 | Every controlled load/wire branch has coordinated protection at appropriate upstream point | Calculate from conductor gauge, installation temp/bundle, terminal, load continuous/inrush, fuse time-current and interrupt ratings; no adoption of schematic's F1=20A or F2–F4=10A by default |
| R06 | ECU sensor 5 V/ground reference and high-current motor/relay return are separate functional nets with explicitly controlled reference relationships | Continuity review, netlist/ERC and loaded ground-drop; never carry motor current in ECU sensor ground |
| R07 | Relay contact current rating, switch-off behavior, coil polarity and flyback network match actual ECU driver/load | Use coil-driver specifications, contact making/breaking current under inrush, thermal derating, correct suppression and release timing |
| R08 | Board internal supply path is low resistance and thermally safe under simultaneous connected loads | Set a quantitative voltage-drop and temperature-rise budget **after** current source/branch values measured; measure each contact/fuse/connector/copper segment at steady/warm |
| R09 | No unnecessary PTC or other high-series-resistance component may sit in an ECU-critical feed without justified hold/trip/thermal analysis | Old B&G CB2 RXE105/RXE110 reference is not an approved new component. Choose fault protection to suit ECU branch and wiring |
| R10 | PCB/terminal block supports maintenance, labels, realistic enclosure access, strain relief, vibration, moisture and service replacement | Physical envelope and cable entry/connector family TBD; review before placement; no unsupported relay-footprint assumptions |
| R11 | Coil, TWO boost solenoids (including one reusing former PWM Idle channel), LC-1 and fan included based on actual positive ownership; no PWM **idle valve** | Preserve active boost channel/old physical wiring until F6 verifies exact K3/JP1/CB3 participation; no idle-only load; F6 P11/P12/P13/P19 reconciled |
| R12 | H-bridge motor supply and motor-current ground remain off ECU critical power/control path | User has separate relay installed and reports improvement; verify board harness design doesn't backfeed it or share sensor reference. No new H-bridge redesign |
| R13 | Migration harness preserves control-signal polarity and injector sequential drive independently | Do not equate original JP1 `INJ1/2` with four current NCV8403A outputs; before cutting, verify pin map, passive pass-through and connector adapter |
| R14 | Replacement remains functional without MCU, network, dashboard, Wi-Fi, CAN or laptop | Hardware relays/fuses/diodes only as needed; no software dependency for fuel pump safety or ECU ignition power |
| R15 | Existing factory Volvo electrical distribution remains untouched, except unrelated already completed modifications | Scope explicitly restricted to independent aftermarket engine-management box |
| R16 | Full design passes native KiCad ERC/DRC, netlist audit, wiring/fuse audit, bench load/fault testing and independent review before vehicle install | Current GitHub infra fixture tests do not meet these later hardware validation gates |

## Per-domain operating-state contract (proposed; not an electrical schematic)

Modes: **OFF** key removed; **RUN** ignition position II and engine may or may not run; **CRANK** ignition position III; **STALL** key RUN but engine speed is zero after allowed initial prime; **ECU_RESET** key RUN but firmware command output unreliable/absent; **FAULT** local branch open/short/overtemp. Actual ECU firmware control behavior must be demonstrated, not merely assumed.

| Domain | OFF | RUN, ECU operating | CRANK | STALL / ECU_RESET | Fault isolation |
|---|---|---|---|---|---|
| Main ECU feed | OFF, unless explicitly required memory retention via separate fused feed | ON | **ON if ECU requires continued start power** | Power may remain ON while key RUN to allow diagnostics/restart; ECU itself must not command pump ON indefinitely | ECU fuse/relay protection independent of pump load fault |
| Fuel pump | OFF | **Only during valid ECU commanded prime / run** | As explicitly commanded by EpicEFI strategy | **OFF after allowed prime / stop timeout**, even if ignition key stays RUN | No bypass path that supplies pump indefinitely following ECU command loss; review single welded relay |
| Injector positive | OFF | ON in intended engine-enabled state | ON for cranking injection | Can remain powered with ignition if ECU drivers OFF; confirm safe failure logic | Short must trip injector branch, not remove all unrelated power where avoidable |
| Coil positive | OFF | ON in intended engine-enabled state | ON for cranking spark | ECU driver off; verify fail-safe if ECU control absent | Distinct branch if current evidence supports |
| **Boost solenoids only (two)** | OFF except justified behavior | ON when required | source per run/start policy | ECU low-side PWM released safely | One uses former PWM Idle circuit: must map actual driver/harness, positive protection, inductive suppression; NO idle valve |
| H-bridge (already external) | Separate relay should switch off | Operates using its independent new circuit | Confirm independently only if relevant | External safety and idle-air behavior not part of replacement board | Motor power and ground must not route through ECU or signal nets |

**Important fuel-pump design decision still open:** Determine whether pump relay contact supply derives from its own protected battery source or an ignition-controlled/main relay switched source. A separate relay with a key-on/ECU-command logic interface needs a reviewed failure analysis for **welded contacts, stuck drive and ECU reset**, not just a relay click test. Adding series switching has current/voltage/thermal tradeoffs and is not authorized without F6/F7 evidence.

## Quantities to determine (not guessed values)

| Domain / check | Steady operating current | Peak / startup current | Proposed fuse/contact/wire | Max acceptable drop or temperature | Evidence source |
|---|---|---|---|---|---|
| ECU electronic supply, Mega144H7 | TBD | TBD on cold crank / boot | TBD | Determine from ECU minimum voltage and measured cable budget | ECU electrical specification and branch measurement |
| Fuel pump current model in use | TBD | TBD start or stall | TBD | Determine contact/fuse thermal at hot tank/vehicle conditions | Pump actual part, current test |
| **Combined injector B+ for all four EV14s** | TBD | TBD max duty/simultaneous; nominal 12 Ω per injector per model supplier | **One common fuse** proposed, value TBD | Verify shared harness conductor and four individual branch-wire protection plus thermal | User confirmed old two-pair fuses; final group fault analysis pending |
| VAG ignition coil B+ if included | TBD | TBD dwell/inrush | TBD | Determine from coil driver and cycle behavior | Installed coil specification |
| **Legacy PWM idle ACTUATOR / Fast Idle ACTUATOR — NOT USED** | 0 separate idle-actuator current | N/A | No idle-valve fuse; K3/CB3 removal conditional | N/A for idle valve; boost circuit ratings TBD | Trace reused boost PWM circuit before removing old conductor or relay path |
| Boost solenoid 1 if included | TBD | TBD | TBD | Driver safe transient | Installed valve |
| Boost solenoid 2 if included | TBD | TBD | TBD | Driver safe transient | Installed valve |
| LC-1 heater/controller if included | TBD | TBD cold heater | TBD | Analog interference/return | Installed LC-1 wiring |
| Fan if included | TBD | TBD locked rotor/inrush | **External high-current path may be appropriate** | Contactor/connector thermal under hot environment | Present motor/relay layout |
| New H-bridge (EXTERNAL budget only if sharing source) | Not measured | Not measured | Separate wiring already installed | Exclude from ECU branch and sensor ground | User-reported rewire, actual source still unknown |
| Total upstream source cable, fuse and junction | **Sum of coincident load envelope**, TBD | Worst concurrent transient, TBD | Existing 30 A and ~4 mm² cable **not adopted as design rating** | Source→board and cable safety target after load measurement | X1 feed, physical cable marking and installed protection |

### Engineering calculation templates (not complete calculations)

- **DC path loss:** `ΔV = I × R_total`, with `R_total` covering source terminal, fuse, fuse clips, relay contacts, PCB copper, connector and return path individually. Test supply and ground independently.
- **Conductor/trace heating:** `P = I² × R`, using simultaneous, continuous and repetitive pulse load envelopes. PCB copper/terminal temperature and bundle conditions matter.
- **Fuse coordination:** account for normal current, ambient derating, cold-start/inrush profiles, conductor insulation and connector ratings, fault interruption and fuse time-current, not only a nominal ampere number.
- **Relay selection:** distinguish coil pull-in/dropout and release behavior, DC current rating at elevated ambient, continuous current versus make/break and load type. Existing relay K1/K2/K3 and CB2 part numbers are historical source data only.
- **Supply disturbance:** scope START/RUN and normal controlled loads; differentiate true drop across the new board from common battery droop and ground-reference differences.

## Automotive protection, standards and reference context

The new module is installed in a 12 V car environment. Test planning should **consider** reverse battery, jump start, cold crank, supply transients/load dump, ESD, relay-coil inductive kick, vibration, heat and moisture. **No claim of formal ISO compliance** is made here; choose applicable test profiles and acceptance numbers in F8 from the actual mounting location and ECU operating envelope.

Manufacturer reference guidance:
1. Littelfuse, *Automotive Fuses* (temperature derating and current selection): https://www.littelfuse.com/fuse
2. TE Connectivity, *Relay Coil Suppression with DC Relays* (suppression changes relay release/contacts, not only transient amplitude): https://www.te.com/en/products/relays-and-contactors/electromechanical-relays/intersection/relay-coil-suppression-dc-relays.html
3. TE Connectivity, *Automotive Relay Applications* (contact ratings depend on resistive/capacitive/inductive loads and inrush): https://www.te.com/en/products/relays-and-contactors/electromechanical-relays/intersection/application-notes.html
4. Texas Instruments TIDA-01167 (automotive 12/24 V input protection, ISO 7637-2 / ISO 16750-2 reference design): https://www.ti.com/tool/TIDA-01167

**Avoid assuming** a simple flyback diode is always optimal; release timing of the fuel-pump relay matters. Also avoid copying an ancient series PTC design into ECU supply solely because it existed on the stock source board.

## Focused verification plan and stopping rules

| Phase | Work | Result allowing next phase |
|---|---|---|
| F6-A | Identify **which branches actually use old box** and fuse/terminal functions | Actual ECU/pump/injector/command ownership known |
| F6-B | Decide coil/boost/LC-1/fan power ownership; document installed Walbro and boost reutilization of former PWM Idle; no idle valve | Exact box output, connector migration including reused PWM wiring and future IOX/two-gauge/P4 loads |
| F7-A | Measure source, critical load currents and duty/peak states without provoking engine faults | Relay/fuse/contact/connector/wire design envelopes grounded in current/hot state |
| F7-B | Measure board supply and ground loss under normal/heat-soaked loads; set electrical loss and thermal acceptance limits | Numerical targets with evidence and decision rationale |
| F7-C | Analyze coil suppression, ignition/ECU reset, pump relay weld, branch faults, and start/stop requirements | Failure behavior agreed and bench test plan |
| F8 | Review component ratings and migration interfaces; explicitly authorize schematic | No unclosed safety-critical assumption; reproducible toolchain and independent review plan |

**F7 status: OPEN.** This document establishes *what must be true and how to demonstrate it*; it does not invent fuse values, measured load currents, relay contact ratings, voltage budgets or PCB dimension decisions.


## Future power feeders — newly scoped 2026-11-02

F7 load list now covers **INSTALLED Walbro 255 L/h**, four EGT channels/IOX, EMAP, pedals/other sensors, **two planned gauges**, CAN and **ESP32-P4 secondary control**. Old four-screen and Raspberry Pi/CarPi/Zero allocations are cancelled. The former PWM Idle circuit is **actively reused by one boost solenoid** and must be mapped. Compact Micro ISO relay families and two **optional external** Maxi ISO/high-current slots are candidate packaging; no measured current, source/copper/fuse rating or count is authorized. F7 OPEN.
