# Core replacement relay/fuse-box design scope — 2026-11-02

## Return to the primary project objective

Design a passive, serviceable, low-voltage-drop relay/fuse distribution replacement for the **aging aftermarket DIYAutoTune/MegaSquirt-style relay box** powering the user's **1997 Volvo 940 Turbo B230FK Mega144H7/EpicEFI installation**. The original Volvo LH2.4 relay/fuse wiring is **not** in use for current EFI. Its October 2026 diagnostic investigation is closed for this design phase at user's direction; do not pursue abandoned factory relay options unless the user reopens them.

**Latest change:** The user **installed a new relay and new wiring for the DC idle H-bridge** and reports improved behavior. This is user-reported installation and operation, not measured cure of ECU brownouts. The installed final H-bridge feed/branch fuse/control/ground specifics are not yet documented; it is not an outstanding request to continue the OEM relay search. The new distribution design should **not route H-bridge motor power through the ECU's protected supply or reference ground**.

## Current planning deliverables — 2026-11-02

The first specification pass is now in place:

- [F6 replacement circuit ownership matrix](F6_REPLACEMENT_CIRCUIT_MATRIX.md) — 20 physical power/control boundaries, inclusion/omission policies, source-board migration constraints and evidence batches. **F6 remains open** until wiring is physically reconciled.
- [F7 electrical requirements baseline](F7_ELECTRICAL_REQUIREMENTS_V0.md) — 16 functional requirements, ignition/fail-safe state matrix, required load and thermal measurements, branch-protection and relay-suppression considerations. **F7 remains open** until quantitative ratings and tests are supported.
- [Functional architecture v0](REPLACEMENT_FUNCTIONAL_ARCHITECTURE_V0.md) — two-relay baseline plus appropriate protected outputs; PCB-vs-hybrid tradeoff and explicit pre-schematic decisions. **Review concept only**.

## Minimum replacement architecture (proposed FUNCTIONAL inventory, not a schematic)

The old Bowling & Grippo board is a **reference**, not a literal functional specification. The existing source layout uses X1 constant +12 V, X2 ignition +12 V, X3 engine ground, ECU relay K1, pump relay K2, fast-idle relay K3, main F1, pump F2, injector branches F3/F4, and polyfuses CB1/CB2/CB3. Source files: `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md`. Only as-built evidence may establish what is currently connected.

| Power/control domain | Candidate role for replacement | Current evidence / design boundary |
|---|---|---|
| Battery/source distribution | Protected common supply from known-good battery-fed source | X1 historical permanent supply behind 30 A upstream fuse; conductor gauge estimated by user as roughly 4 mm², **not verified**. Don't assume old fuse remains the correct new rating. |
| ECU supply | Replace aged K1 and any current high-impedance/thermally stressed path with low-drop protected relay-switched ECU feed | Actual installed ECU feed via K1/CB2 not traced; must maintain ECU power on RUN/START with correct low-voltage/crank behavior |
| Fuel-pump relay | Preserve ECU Mega144H7 PD10 controlled pump relay and fail-safe OFF after engine stop | Original current aftermarket K2/fuse circuit presumed from source board; actual as-connected terminals, coil drive topology, current/prime logic not established |
| Injector supply | Protected +12 V to four EV14 injectors with sequential ground-side drivers | Old design has two injector feed fuses F3/F4; actual branch assignments to four EV14 not established |
| Fast idle function | Only implement if a load still needs a mechanical switched relay | Old K3 Fast Idle is not equivalent to modern PWM IAC or separate H-bridge. **Do not automatically replicate K3** |
| Ignition-coil supply | Evaluate inclusion as protected distribution branch | Current VAG wasted-spark coil positive and return path not yet mapped |
| PWM IAC / boost valves | Evaluate inclusion as fused actuator power branch(es), with appropriate driver topology and flyback | Two boost solenoids, two-wire PWM valve; actual current ownership of MS box unknown |
| Wideband heater / fan | Evaluate only if current wiring shows they belong to this box | Do not assume new board will own every car accessory circuit |
| DC idle H-bridge | **Already moved to a new relay and wiring**, as reported 2026-11-02 | Treat as an external motor-current branch unless user elects to integrate it. Preserve separate motor-current ground and supply, no ECU reference return |
| Sensors, CAN nodes, displays | Low-current regulated/sensor supplies and future nodes | **Out of core high-current relay-box scope** without a specific evidenced need; do not place sensor-return current on high-current distribution |

## Design priorities (decision-ready without guessing ratings)

1. **Reliability and isolation:** avoid long/thermally sensitive high-current series paths, ECU ground contamination and unwanted fuel-pump power on ECU stall; use properly rated automotive relays, fuses, terminals and strain relief.
2. **Serviceability:** standard replaceable Micro ISO relay family and accessible individually replaceable blade fuses, connectors labelled by function, field-replaceable failure components.
3. **Low electrical loss:** preserve good battery-to-ECU voltage during loads, crank/start, and idle-control transients. Define loss/thermal targets from actual circuit currents before selecting copper or hardware.
4. **Minimal complexity:** relay/fuse distribution **not** another microcontroller, CAN node or software-controlled safety dependency. Avoid reinventing original obsolete low-current sensor interface.
5. **Reproducible workflow:** KiCad 9 toolchain verified, CI and EpicWolf foundation partially validated. KiCad 10 and automatic source editing remain unverified and cannot be assumed required.

## Next scoped engineering deliverables — F6, F7, F8

**F6 — as-built ownership map (OPEN).** For each circuit above, record if its positive supply currently comes from the old aftermarket MS relay/fuse box, from a separate new harness, or is unknown. For circuits owned by the box, establish terminal/connector, fuse, relay, switch source, current return and current conductor size using `docs/ELECTRICAL_INVENTORY.md` and `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md`. No new photos required where existing user descriptions suffice.

**F7 — electrical design requirements (OPEN).** For each included load, establish expected steady/inrush/peak current, source RUN/START/OFF requirements, branch-fuse/wire sizing, maximum voltage drop, thermal/service limits, fault behavior and driver/flyback compatibility. Quantities remain TBD; do not select nominal values from B&G 2002 schematic or unverified current cable guesses.

**F8 — architecture readiness (OPEN).** When F6/F7 circuit ownership and requirements are evidenced, create system-level net and connector concept and review safety-critical ECU/fuel-pump behavior, then authorize actual KiCad schematic. No hardware layout is approved yet.

## Deliberately closed / deferred branch

Historical Oct 2026 original Volvo E white relay / M blue Hella testing, old pink pump loom, LH2.4 pins 20/21, and original fuse-box voltage losses were diagnostic exercises, **not the central replacement board design**. Those notes remain available in `docs/VOLVO_FACTORY_RELAY_REUSE_RESEARCH.md`, but should not dominate next development steps. The H-bridge rewiring is **installed/reported better**; avoid additional idle stalling tests, OEM relay tracing, or new H-bridge rewiring proposals unless the user specifically asks.
