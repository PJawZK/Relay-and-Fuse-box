# Electrical inventory — installed vs planned (reconciled 2026-11-02)

**Purpose:** A starting inventory compiled from older Volvo 940 Turbo ECU project discussions. This is **not** a verified as-built harness map. Each entry must be compared with the car and latest ECU/tune before drawing a replacement PCB.

**Current electrical architecture correction (user, 2026-10-27):** The entire EpicEFI EFI electrical harness and its relays/fuses are **separately installed**. **No original Volvo OEM EFI wires, relays or fuses remain in use by the current EFI system.** The aged MS/DIYAutoTune relay board described here is *aftermarket* and still serves EpicEFI; its own internal circuitry is stock/unmodified. Do not conflate these two meanings of “stock.” The former Volvo EFI relay positions are candidates for unrelated future reuse, subject to proving current socket/coil/feed status. See `VOLVO_FACTORY_RELAY_REUSE_RESEARCH.md`.

Evidence labels: **reported installed** = user reported installation, not independently inspected; **planned** = future/unfinished; **historical** = earlier configuration, do not assume still installed; **verify** = topology or part assignment not established.

| Circuit/component | State | Known information | Power-path / ground-path status | Action |
|---|---|---|---|---|
| ECU | Reported installed | EpicEFI Mega144H7 with Speeduino 0.4.3C adapter, October 2026 firmware | ECU main feed through old DIYAutoTune/MS relay system; exact real-life terminals and fusing unverified | Document exact ECU B+, ignition feed, controller and sensor grounds |
| Relay/fuse box | Reported installed | DIYAutoTune/MegaSquirt-type relay box aged about 15–16 years, three warm relay housings recently reported; MINI fuses; **separate 30 A upstream fuse near battery** confirmed by user report 2026-10-27 | X1 permanent +12 V through external 30 A; X2 switched +12 V; X3 engine ground, per current user text. Original B&G schematic V1.2/layout V1.1 silkscreen mapped in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`; physical revision and onboard F1 remain unknown | Capture JP1/JP2 actual uses by **text**; distinguish upstream 30 A from onboard F1; record fuse/relay markings when known |
| Alternator / charging | Reported installed | Regulator replaced, typically 13.9–14.0 V measured | Alternator/battery relay-box input routing, fusible link and ground return need tracing | Diagram charging and engine-ground links |
| Fuel pump | **Installed Walbro 255 L/h — owner confirmed 2026-11-02** | Mega144H7 PD10 controls aftermarket fuel pump relay, pump replacement was done ages ago; exact Walbro part/model/current TBD | Independent new aftermarket wiring/fuse, NOT original Volvo LH, true relay/fuse/output still to document | Measure current at pressure, start/stall and fail-safe with a meter appropriately rated for motor inrush |
| Injectors | **Reported installed and positively supplied by MS box, split into two fused injector pairs (2026-11-02)** | Bosch EV14 0280158117, sequential, four independent NCV8403A ECU low-side drivers | **Two positive-supply fuses, one per injector pair — user-confirmed**. Exact JP2 cavity/cylinder pair assignment, fuse values and gauge unknown | Draft replacement uses **ONE fused B+** to all four injectors; verify fuse time/current and four branch wires; keep individual sequential control outputs |
| Ignition | Reported installed | VAG wasted-spark coil 032 905 106B, IGN1/IGN3 | Coil +12V branch, noise suppression and high-current ground unknown | Trace 12V and engine-ground pathway |
| PWM / Fast Idle circuit | **NO IDLE VALVE; BOOST CHANNEL ACTIVE — owner confirmed 2026-11-02** | One of two Pierburg boost valves **reuses former PWM Idle circuit**; DC idle actuator separately relayed H-bridge | Unknown whether reuse is ECU PWM channel only, old JP1 conductor, old K3/CB3 power path or combination | Preserve used boost control path; mark idle-only load absent. Do not definitively remove K3/CB3/JP1 before as-built map |
| DC idle H-bridge | **Reported rewired and operating better (2026-11-02)** | New separate relay and wiring installed for DC idle H-bridge, replacing previous supply/ground arrangement near ECU (exact final routing not yet documented) | **Do not assume** whether new positive branches from MS X1 upstream, battery, or independent source, whether relay coil uses X2, or where power ground lands. Existing fuse was earlier described as downstream of H-bridge output; new input-fuse installation is unverified. | Capture new source, fuse and relay terminal map, power-ground destination and motor-output protection as **as-built**; H-bridge no longer an OEM-reuse design candidate. Quantitative idle/ECU stability validation remains unmeasured. |
| Boost control | Reported installed | TWO Pierburg solenoids; one uses former PWM Idle circuit, upper/lower mapping TBD | Positive power source, drivers, ground and flyback wiring unverified | Trace both independently including old channel and suppression |
| Fuel pressure | Reported installed / planned change | Existing 200 PSI rail sensor; custom fuel rail, regulator and replacement FP sensor pending | Sensor power/reference/ground and +12V actuator loads as applicable | Mark replacement dependency before EMAP reuse |
| EMAP | Planned | Existing 200 PSI sensor to be reused after fuel-rail swap, analog input on Mega144H7 | Sensor reference/ground routing still planned | Reserve protected sensor wiring, **not high-current relay output** |
| EGO | Reported installed | Innovate LC-1 LSU 4.2, analog output changed during project | Heater +12V and heater ground vs analog reference must be traced | Verify heater circuit separate from sensor ground |
| Electric fan | Existing ECU control / harness verify | Fan output power stage/relay in current setup not established | Factory relay vs project box topology unknown | Don't presume relay-box ownership |
| VSS | Reported installed | Cluster/VSS BC547 conditioner, signal issues previously repaired | Signal ground and power separate from motor return | Document signal/reference only |
| Dash/CAN nodes | PLANNED revised | **Two digital gauges** (clock then RPM), no other ESP32 display conversion, existing head unit retained; optional CAN nodes; **ESP32-P4 secondary EpicEFI controller** | Separate protected regulated low-current supply, no Pi/CarPi/Zero | Design according to actual chosen modules; no main ECU/pump dependence on P4 |
| Crank/cam/TPS/CLT/IAT | Reported installed | Engine sensors and cam sync; CLT 8653103 isolated 2-pin | Dedicated sensor grounds and 5V references must **not** be routed through power relay distribution indiscriminately | Current harness pin-by-pin map |
| AOS and mechanical hardware | Planned | No electrical power allocation expected | Out of scope unless sensor/heater added | Track dependencies separately |

## Previous wiring assertions that must not be treated as current pinouts
- 2025 Speeduino DB37 mapping included fuel-pump pin 37, main +12V pin 28 and shared DB37 sensor wiring. Current Mega144H7 and adapter mapping may differ.
- Prior reports describe different injector and IGN pin maps across ECU revisions. **Do not copy these values into the new PCB netlist without checking the actual assembled harness.**
- **Authoritative newer 2026-11-02 correction:** no PWM idle *valve* and no Fast Idle actuator; one Pierburg boost solenoid **reuses former PWM Idle circuit**. H-bridge uses its independent new relay. Walbro 255 L/h is ALREADY installed; only two gauges and ESP32-P4 are future vehicle electronics; no Pi. Owner to provide updated EpicEFI wiring diagram. See [corrections](AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md).
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

**Current 2026-11-02 scope:** Begin with [the F6 replacement circuit ownership matrix](F6_REPLACEMENT_CIRCUIT_MATRIX.md) and its priority batches, rather than pursuing old original Volvo relay troubleshooting. X1 permanent via separate 30 A upstream fuse, X2 switched power, and X3 engine ground are **already user-reported**; do not ask again. **Historical-only 2026-10-27:** H-bridge positive/ground shared ECU screw terminals. User has since installed new H-bridge relay and wiring with improved operation (final routes unverified). The 30 A upstream fuse is **not** source-board F1.

1. Use the source-derived X1–X3, JP1 (20 pins), JP2 (4 pins), F1–F4 and K1–K3 mapping in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`; collect **text descriptions** of present wire destinations, used/unused terminals and readily known fuse/relay details. Photographs optional, not prerequisite.
2. Establish **remaining** source ownership for ECU B+, installed Walbro pump, coil, both Pierburg boost valves including former PWM Idle wiring, LC-1 and fan; injector two-pair positive feed confirmed, idle valve absent (not equivalent to unused PWM wiring). Use updated current EpicEFI wiring diagram when supplied.
3. Current of each separately isolated load branch using an appropriately rated instrument and test method.
4. Separate chassis, battery, engine, ECU, sensor, coil and H-bridge return points on a ground-tree drawing.
5. Update every 'reported installed' claim to 'verified installed' only with measurements, physical tracing or current schematic evidence.

## Traceability and capture (2026-11-02)

See [current and future load inventory](POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md) for planned 4× EGT, EMAP, IOX, pedal position, flex fuel, wheel signals, CAN display nodes and Pi, and [expansion capacity](POWER_DISTRIBUTION_EXPANSION_CAPACITY.md) for provisional fuse/relay reservations and local regulator roles.

Use [the evidence/coverage ledger](ELECTRICAL_EVIDENCE_LEDGER.md) for circuit IDs E01–E20 and current proof gaps. Record new vehicle observations in [the physical inspection and measurement worksheet](ELECTRICAL_MEASUREMENT_WORKSHEET.md) before upgrading any entry from **reported installed** to **verified installed**. Keep each measurement session separate; do not blend September 2025 and May 2026 observations into a single simultaneous drop budget.
