# F6 — replacement-box circuit ownership and connector matrix (v0.1)

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
| P06 | Electric fuel pump | **R:** active pump run by aftermarket MS-box relay; user's relay-removal test established no OEM Volvo relay needed | K2 and F2 output, JP1-5 `Fuel Pump` as source **H** | **CORE:** own fused output, controlled by ECU command with engine-stall shutoff | Current pump +12 branch, fuse, wire, ground; relay/contact & coil wiring; steady/inrush/stall current |
| P07 | Fuel pump command | **R:** Mega144H7 **PD10** runs the installed fuel-pump relay arrangement; electrical polarity/driver interface **U** | `FP1` control `K2` **H** | **CORE:** compatible coil input, appropriate suppression, off on ECU reset/stop | Actual PD10 control electrical type/polarity, permitted current, startup prime and fault truth table |
| P08 | EV14 injectors #1–#4, positive feeds | **R:** Bosch 0280158117 EV14 with sequential ECU-side low-side MOSFET control; **U** which B+ supply/fuses currently serve four injectors | F3 & F4 → JP2 four-position injector +12 distribution **H** | **CORE:** protected injector B+; **provisionally 2 fuse groups**, no assumption of pair mapping | Present harness positive feed grouping, max simultaneous current, fuse protection and fault segregation |
| P09 | Injector ground-side drivers | **R:** individual Mega144H7 NCV8403A sequential drives | Old JP1-1..4 `INJ1/2` references **H**, not current pinout | **SIGNAL-ONLY:** no switching transistors on passive power board unless needed for existing connector pass-through | Determine if old box still passes any injector command wires (vs direct ECU wiring) |
| P10 | Wasted-spark ignition-coil B+ | **R:** VAG 032 905 106B used; positive supply origin **U** | No trustworthy direct contemporary mapping | **CANDIDATE:** individual fuse/branch if powered from box or deliberately consolidated | Existing coil source/fuse, peak/inrush, shared protection, return and switching |
| P11 | Two-wire PWM idle valve, supply | **R:** ECU-controlled Bosch PWM valve working; +12 V ownership **U** | K3 fast-idle relay `FASTIDLE` is a different function **H** | **CANDIDATE:** fuse +12 actuator feed; preserve ECU PWM driver and suppression | Present power feed, fuse, valve wiring and its electrical current |
| P12 | Boost solenoid, upper chamber | **R:** installed Pierburg control with EpicEFI; source **U** | Not uniquely represented in 2002 board | **CANDIDATE:** fuse protected +12 actuator feed, preserve ECU driver | Source wire/fuse, flyback, operating load and control return |
| P13 | Boost solenoid, lower chamber | **R:** installed second solenoid; source **U** | Not uniquely represented | **CANDIDATE:** individual or grouped protection after current/fault study | As P12; verify no temporary connection remains unsafe |
| P14 | LC-1 wideband controller / heater | **R:** installed Innovate LC-1; heater +12 source and signal reference **U** | JP1-20 `O2` is source-era signal reference **H** | **CANDIDATE:** heater/controller fused branch if currently MS-box powered; analog return separate | Existing heater and controller feed/ground and its operating/fault current |
| P15 | Electric radiator fan | **R:** ECU control present; actual fan relay, source/fuse **U** | Not proven MS-box circuit | **CANDIDATE ONLY IF INCLUDED:** fan is heavy duty and may deserve external relay/fuse, not PCB | Confirm which hardware actually powers fan, continuous/inrush current and thermal requirements |
| P16 | DC idle H-bridge + motor | **R 2026-11-02:** fresh relay and wiring installed, reported better; exact new feed/fuses/ground **U** | Previously shared ECU screw; now historical | **EXTERNAL by default**; do not merge motor output or return into ECU branch | Record as-built final branch for boundary, without reopening obsolete OEM relay investigation |
| P17 | Sensors (crank/cam/TPS/CLT/IAT/VSS/fuel pressure) | **R:** sensors installed; reference and some conditioning at ECU | JP1-12..20 provide historical signal/ground pass-through **H** | **SIGNAL-ONLY:** preserve low-current ECU 5 V/ref/sensor return topology | Identify any physical existing board pass-through before eliminating JP1 sections |
| P18 | Digital cluster, ESP32 CAN, accessories | **R/P:** future nodes; separate planned power distribution | None | **EXTERNAL:** expansion interface only if documented; no CAN dependency in power safety | Separate accessory design later |
| P19 | Original K3 fast-idle mechanical relay | **U:** existing use not verified; 2-wire PWM IAC and DC H-bridge are distinct | K3, J1, CB3 `FASTIDLE` **H** | **OMIT provisionally**, reinstate only for identified consumer | Determine whether a current engine load uses a mechanical fast-idle relay |
| P20 | Original CB1/CB2/CB3 PTC / old sensor interface | **R:** old box internally unmodified, actual installed PTC net/current **U** | CB2 on ECU feed, CB1 ref protection, CB3 fast-idle **H** | **DO NOT CLONE** automatically; select modern appropriate protection with fault evidence | Map current critical feeds, type/hold trip temp; decide no excessive series loss |

**F6 interpretation:** Core functional capabilities P01–P08 are confidently required at a *system* level, not yet proven to occupy the exact historically labelled output terminals. P10–P15 must **not** inflate the new board simply because the vehicle has those components. P16 stays external by current decision. P17–P18 are excluded from the high-current PCB.

## Legacy connector preservation vs simplification

Historical interface **X1/X2/X3, JP1 (20 positions), JP2 (4 positions)** is recorded in `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md`:
- **X1/X2/X3** are *real as-used input functions*, but the replacement may use a higher-quality keyed/sealed connector or terminal distribution; physical pin compatibility not yet decided.
- **JP1 position 5** historically says pump; current pump wire landing there is **not verified**.
- **JP1 positions 1–4** historically had injector channels grouped 1/2, whereas current ECU is sequential with 4 separate drivers. **Do not short or merge sequential driver signals** to mimic historic labels.
- **JP1 position 6** historically `Fast Idle` is **not** the modern PWM IAC or H-bridge supply.
- **JP1 positions 7–20** historically combine spare/control/sensor/O2/tach wires. Keep these out of high-current PCB design unless present physical harness routing demands a passive pass-through block.
- **JP2 four positions** historically supply two fused injector groups; verify how the present four EV14s are connected before deciding new connector count.

**Connection policy:** preserve *electrical function and documented harness migration*, not necessarily the original PCB's screw-terminal geometry; no destructive changes to a running ECU harness without a reviewed conversion map.

## Four batches to close F6 without a general troubleshooting detour

| Batch | Included entries | Evidence to extract / observe | Output |
|---|---|---|---|
| **A — board ownership** | P01–P09, P19 | Map existing source/relay/fuse names to *actual* ECU supply, pump, injector positive and command connections; identify unused K3 and signal pass-through | A list of actual must-keep terminals and safe redundant functions |
| **B — conditional powered loads** | P10–P15 | Identify who powers coil, PWM valve, 2 boost valves, LC-1 heater, fan | Short include/exclude list with source ownership |
| **C — electrical boundaries** | P03, P05, P16–P18, P20 | Separate ground nets, H-bridge external interface, sensor pass-through and old PTC paths | Final ground and interface boundary |
| **D — migration review** | All chosen | Old terminal → new connector/function/fuse/relay map, labeled as measured or proposed | Freeze new board connector count and physical function, then F8 |

No requirement to repeat the discontinued old Volvo OEM relay exercise. No new photos needed when reliable source documentation or wire descriptions suffice.

## Unresolved critical facts (not permission to invent them)

1. Which present physical output terminal powers the ECU, pump, injector positive groups, and whether JP1 handles any current ECU signal wiring.
2. Which non-core loads still pass through the MS board rather than their own fuses/relays.
3. Current fuse markings on the actual box, installed CB2 path, wire sizes, branch currents and allowable supply-drop budgets.
4. Current fuel-pump stop/prime/failure behavior and the Mega144H7 PD10 electrical relay-control interface.
5. Whether final H-bridge relay power feed shares a protected upstream trunk with the box (relevant to total source budget, **not** a reason to reopen its separate troubleshooting).

**Status:** F6 **OPEN**. This v0.1 matrix performs the functional scoping and evidence reconciliation; it does not falsely promote unmeasured paths to verified as-built status.
