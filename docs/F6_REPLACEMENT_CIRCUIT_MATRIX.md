# F6 — replacement-box circuit ownership and connector matrix (v0.2)

_2026-11-02 · **DESIGN PLANNING ONLY, F6 STILL OPEN** · Vehicle: 1997 Volvo 940 B230FK / M90, Mega144H7/EpicEFI_

## Purpose and evidence language

This matrix is the **first functional definition for replacing the aged aftermarket MegaSquirt/Bowling & Grippo relay/fuse board**. It is not an as-wired pinout or authorization to connect hardware. The original **Volvo** LH2.4 relays, fuses, and wires are not used for current EFI. The user completed a **new relay/wiring installation for the DC idle H-bridge on 2026-11-02** and reports it works better. That modification is **outside the replacement board scope** unless a later design choice explicitly changes it.

Evidence: **R** = user-reported present hardware/connection; **H** = historical source schematic; **U** = current connection/load unknown; **P** = proposed future function; **N** = deliberately excluded. A reference-board terminal name is not proof of a current attached load. Use `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md` for source-document terminal naming, and `docs/ELECTRICAL_EVIDENCE_LEDGER.md` for physical evidence gaps.

Design labels:
- **CORE**: required functional capability in the replacement system (may exist on another external module only after an explicit topology decision).
- **CANDIDATE**: consider if the current harness/load ownership warrants it; **not a commitment to build a footprint**.
- **EXTERNAL**: preserve present standalone wiring; no motor-current routing on new ECU board.
- **SIGNAL-ONLY**: do not route as a high-current relay/fuse branch.
- **OMIT**: do not reproduce obsolete source-board function without proof of a live consumer.

## Power-control and load ownership

| ID | Current load / boundary | As-built source / evidence | Historical B&G connection | Replacement intention | F6 proof required |
|---|---|---|---|---|---|
| P01 | Main unswitched input | **R:** permanent battery feed → separately installed 30 A fuse → MS X1; estimated ~4 mm² cable (unverified) | X1, F1 → `12U` | **CORE:** protected source distribution | Actual feed path, conductor/capacity, physical input, present F1 and external fuse markings |
| P02 | Ignition sense/switch control | **R:** key-switched +12 V at MS X2 | X2 → `12S` | **CORE:** relay control/reference in RUN/START | Verify X2 OFF/RUN/START and driver logic; never use X2 as high-current feed |
| P03 | Power-ground boundary | **R:** MS X3 tied to engine ground | X3 engine ground | **CORE:** defined control/return interface without high-current ground coupling into ECU/sensors | Return paths for relay coils vs ECU power vs sensor reference; engine/battery bond |
| P04 | ECU Mega144H7 supply | **R:** supplied from existing MS relay box to ECU positive screw; exact MS output/PCB net **U** | K1, F1, CB2 and `12 RAW` per source **H** | **CORE:** separately fused, switched ECU power with low series resistance | As-fitted source terminal; exact ECU fuse, relay, return, wire size, current, cranking behavior |
| P05 | ECU power return | **R:** from MS box to ECU negative screw; previous H-bridge common-ground condition superseded by installed separate wiring | X3 ground network **H** | **CORE:** distinguish power return from sensor reference; avoid circulating actuator currents | Installed ECU return path and any common internal board copper |
| P06 | **Walbro 255 L/h pump ALREADY INSTALLED** | **R 2026-11-02:** aftermarket MS-box-controlled pump, owner says Walbro 255 fitted ages ago; no Volvo OEM relay involved | K2 and F2 output, JP1-5 `Fuel Pump` per source **H** | **CORE:** own fused output, commanded by PD10 with engine-stall shutoff | Actual Walbro model, supply/ground, fuse/relay/coil connections, pressure-dependent steady and inrush/stall current |
| P07 | Fuel pump command | **R:** Mega144H7 **PD10** runs the installed fuel-pump relay arrangement; electrical polarity/driver interface **U** | `FP1` control `K2` **H** | **CORE:** compatible coil input, appropriate suppression, off on ECU reset/stop | Actual PD10 control electrical type/polarity, permitted current, startup prime and fault truth table |
| P08 | EV14 injectors #1–#4, **positive feeds** | **R 2026-11-02:** All four injector positive feeds supplied through existing MS box; **TWO fuses, each serving a pair**. Four sequential low-side MOSFET channels remain individual | F3 & F4 → JP2 4-position +12 distribution is historical and **consistent** with the user's two-pair observation, though actual JP2 terminal numbers and harness pin mapping still unverified | **CORE: ONE COMMON protected injector B+ fuse** proposed for four injectors; four separate +12 branch wires/connector endpoints and independent low-side drivers | Actual existing JP2 usage, wire gauge from split to each injector, summed duty/peak current, fuse/fault isolation and key-off behavior; no amp rating yet |
| P09 | Injector ground-side drivers | **R:** individual Mega144H7 NCV8403A sequential drives | Old JP1-1..4 `INJ1/2` references **H**, not current pinout | **SIGNAL-ONLY:** no switching transistors on passive power board unless needed for existing connector pass-through | Determine if old box still passes any injector command wires (vs direct ECU wiring) |
| P10 | Wasted-spark ignition-coil B+ | **R:** VAG 032 905 106B used; positive supply origin **U** | No trustworthy direct contemporary mapping | **CANDIDATE:** individual fuse/branch if powered from box or deliberately consolidated | Existing coil source/fuse, peak/inrush, shared protection, return and switching |
| P11 | **Former PWM Idle circuit REUSED by one Pierburg BOOST valve**; no PWM idle valve/Fast Idle actuator | **R 2026-11-02:** no idle-valve load, but exactly one of two boost valves reuses that channel/circuit | K3/J1/CB3 FASTIDLE / JP1-era circuitry per historic B&G drawing, physical current use **U** | **PRESERVE reused boost control** until tracing; omit only true idle-specific loads; K3/CB3 presence required or not **UNPROVEN** | Identify boost solenoid and whether ECU output vs board terminal, harness, supply branch, K3/CB3 is active; measure signal, source and suppression |
| P12 | Boost solenoid, upper chamber | **R:** installed Pierburg; one of P12/P13 uses old PWM Idle channel, which one **U** | Prior PCB/control link **U**, cannot infer | **CORE ACTUATOR FUNCTION:** preserve correct independent PWM and positive feed | Identify reused channel assignment and source/fuse, flyback, coil current, return |
| P13 | Boost solenoid, lower chamber | **R:** installed second Pierburg; one of P12/P13 uses old PWM Idle channel, which one **U** | Prior PCB/control link **U** | **CORE ACTUATOR FUNCTION:** preserve correct independent PWM and positive feed | Which boost valve reuses former idle, source/fuse, flyback, operating load, temporary connection safety |
| P14 | LC-1 wideband controller / heater | **R:** installed Innovate LC-1; heater +12 source and signal reference **U** | JP1-20 `O2` is source-era signal reference **H** | **CANDIDATE:** heater/controller fused branch if currently MS-box powered; analog return separate | Existing heater and controller feed/ground and its operating/fault current |
| P15 | Electric radiator fan | **R:** ECU control present; actual fan relay, source/fuse **U** | Not proven MS-box circuit | **CANDIDATE ONLY IF INCLUDED:** fan is heavy duty and may deserve external relay/fuse, not PCB | Confirm which hardware actually powers fan, continuous/inrush current and thermal requirements |
| P16 | DC idle H-bridge + motor | **R 2026-11-02:** fresh relay and wiring installed, reported better; exact new feed/fuses/ground **U** | Previously shared ECU screw; now historical | **EXTERNAL by default**; do not merge motor output or return into ECU branch | Record as-built final branch for boundary, without reopening obsolete OEM relay investigation |
| P17 | Sensors (crank/cam/TPS/CLT/IAT/VSS/fuel pressure) | **R:** sensors installed; reference and some conditioning at ECU | JP1-12..20 provide historical signal/ground pass-through **H** | **SIGNAL-ONLY:** preserve low-current ECU 5 V/ref/sensor return topology | Identify any physical existing board pass-through before eliminating JP1 sections |
| P18 | TWO digital gauges (clock position then later RPM), ESP32-P4 secondary and conditional CAN | **P 2026-11-02:** old four-screen and Pi/CarPi plans cancelled | None | **EXTERNAL LOW-CURRENT:** protected two-gauge cabin feed and optional protected companion supply, no ECU/pump dependency on P4 | Selected boards and regulation when installed; 12 V source capacity, no Pi feed |
| P19 | Historical K3 Fast Idle mechanical relay and CB3 path | **R:** no Fast Idle ACTUATOR; however one boost solenoid reuses old PWM Idle CIRCUIT, and physical use of K3/CB3 is **U** | K3/J1/CB3 `FASTIDLE` historical | Do **NOT** add idle-only relay; also do **NOT** disconnect/omit live reused boost path until tracing proves whether K3 is involved | Actual terminal/relay usage in revised wiring diagram, boost control correctness and source |
| P20 | Original CB1/CB2/CB3 PTC / old sensor interface | **R:** old box internally unmodified, actual installed PTC net/current **U** | CB2 on ECU feed, CB1 ref protection, CB3 fast-idle **H** | **DO NOT CLONE** automatically; select modern appropriate protection with fault evidence | Map current critical feeds, type/hold trip temp; decide no excessive series loss |

**F6 interpretation (updated 2026-11-02):** Core P01–P08 required at system level; P06 is ALREADY Walbro 255; P08 current injectors remain two fused pairs, one common new B+ fuse only proposed. P11/P19 show NO PWM idle-valve load but **active reuse of former PWM Idle circuit by one Pierburg boost solenoid**. Never drop reused wiring on historical assumptions. P10, P14–P15 ownership unresolved. P16 independent H-bridge external; P18 two gauges + optional P4, no Pi. F6 OPEN.

## Legacy connector preservation vs simplification

Historical interface **X1/X2/X3, JP1 (20 positions), JP2 (4 positions)** is recorded in `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md`:
- **X1/X2/X3** are *real as-used input functions*, but the replacement may use a higher-quality keyed/sealed connector or terminal distribution; physical pin compatibility not yet decided.
- **JP1 position 5** historically says pump; current pump wire landing there is **not verified**.
- **JP1 positions 1–4** historically had injector channels grouped 1/2, whereas current ECU is sequential with 4 separate drivers. **Do not short or merge sequential driver signals** to mimic historic labels.
- **JP1 position 6** historically `Fast Idle` and its ECU/path relationship may be **REUSED BY ONE PIERBURG BOOST SOLENOID**. Do not abandon the conductor/terminal until updated as-built wiring confirms exact reused output, positive source and old K3/CB3 relationship. No PWM idle valve.
- **JP1 positions 7–20** historically combine spare/control/sensor/O2/tach wires. Keep these out of high-current PCB design unless present physical harness routing demands a passive pass-through block.
- **JP2 four positions** historically supply two fused injector groups. **User now confirms the current four EV14s indeed have positive feeds divided into two fused injector pairs via the MS box**; exact JP2 terminal/cylinder mapping remains unverified. Proposed replacement removes the redundant *positive-feed fuse division*, **not** individual sequential ECU channels.

**Connection policy:** preserve *electrical function and documented harness migration*, not necessarily the original PCB's screw-terminal geometry; no destructive changes to a running ECU harness without a reviewed conversion map.

## Four batches to close F6 without a general troubleshooting detour

| Batch | Included entries | Evidence to extract / observe | Output |
|---|---|---|---|
| **A — board ownership** | P01–P09, P11, P19 | ECU/pump, installed Walbro 255, injector JP2 pair mapping; **trace old PWM Idle circuitry reused by one boost valve**, K3/CB3 electrical ownership unknown | Must-keep output map and no idle-only functional load, without losing boost |
| **B — conditional powered loads** | P10, P12–P15 | Coil, TWO installed boost valves (one reused former PWM), LC-1 heater, fan positive feed sources | Include/exclude list with source and driver ownership |
| **C — electrical boundaries** | P03, P05, P16–P18, P20 | Separate ground nets, H-bridge external interface, sensor pass-through and old PTC paths | Final ground and interface boundary |
| **D — migration review** | All chosen | Old terminal → new connector/function/fuse/relay map, labeled as measured or proposed | Freeze new board connector count and physical function, then F8 |

No requirement to repeat the discontinued old Volvo OEM relay exercise. No new photos needed when reliable source documentation or wire descriptions suffice.

## Unresolved critical facts (not permission to invent them)

1. Which present physical output terminal powers the ECU, pump, injector positive groups, and whether JP1 handles any current ECU signal wiring.
2. Which non-core loads pass through the MS board; **which Pierburg valve uses the former PWM Idle circuit, and whether that implies ECU output only, JP1 conductor, K3/CB3 or the board power branch**.
3. Current fuse markings on the actual box, installed CB2 path, wire sizes, branch currents and allowable supply-drop budgets.
4. Current fuel-pump stop/prime/failure behavior and the Mega144H7 PD10 electrical relay-control interface.
5. Whether final H-bridge relay power feed shares a protected upstream trunk with the box (relevant to total source budget, **not** a reason to reopen its separate troubleshooting).

**Status:** F6 **OPEN**. This v0.1 matrix performs the functional scoping and evidence reconciliation; it does not falsely promote unmeasured paths to verified as-built status.


## Additional current-use/future power evidence (2026-11-02)

See [corrected as-built scope](AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md), [current/planned loads](POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md), and [revised capacity](POWER_DISTRIBUTION_EXPANSION_CAPACITY.md). Walbro 255 is installed; two gauges and an ESP32-P4 companion replace the former four-screen/Pi plan. **No idle valve, but former PWM Idle channel is actively reused for boost.** F6 OPEN.
