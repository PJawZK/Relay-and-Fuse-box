# Power and ground tree — as-installed reconstruction (2026-10-27)

This is a **partial logical map**, not a verified pin-to-pin harness drawing. Do not use as a production wiring diagram. Source categories: (R) user-reported installed, (H) historical previous-generation wiring, (P) planned, (?) not confirmed.

## Current positive power (known segments)
```text
Alternator B+ / Battery +  (R: charge voltage 13.9–14.0 V)
  |
  +-- vehicle feed / protection (?) --> DIYAutoTune/MS-type relay board +12V inlet (R)
        |
        +-- F1 main fuse --> K1 main ECU relay --> CB2 polyfuse --> 12RAW ECU output
        |       [REFERENCE B&G 2002 V1.2 ONLY; actual physical board needs verification]
        |
        +-- K2 fuel pump relay --> F2 fuel pump fuse --> pump wiring (reference only)
        |
        +-- F3/F4 injector branches (reference only)
        |
        +-- K3 'fast idle' relay (reference only; current IAC is PWM; needs trace)
        |
        +-- ECU main supply (R, actual terminals/voltage loss must be checked)
        |
        +-- DC idle H-bridge + (R: connected at the same ECU screw terminal)
```

**Potentially independent branches (unconfirmed):** ignition coil +12V, dual boost solenoid +12V, Innovate LC-1 heater, fan power, pump downstream factory fuse/relay, dash/CAN power. Their physical origins must not be inferred from older ECU wiring or schematic.

## Current returns (known segments)
```text
Battery - (?) ---- chassis return (?) ---- engine block / alternator case (?)
                                          |
                                          +-- ECU ground (?)  [pins/studs not audited]
                                          +-- coil power grounds (?) [studs not audited]
                                          +-- sensor ground return (?) [ECU reference]
                                          +-- pump return (?) [location not audited]
                                          +-- idle H-bridge power ground (R: same ECU screw terminal)
```
Signal/sensor grounds are **not** interchangeable with motor/coil/chassis current paths. A historical battery-negative-to-engine/star-ground test measured <0.1 V under one operating condition; it does not verify every return segment under motor PWM transients.

## Proposed power and ground structure (P; NOT wired)
```text
Battery/source + -- protected main feed -- rated bus (proper mechanical terminals)
                      |-- fuse + main relay --> ECU dedicated supply
                      |-- fuse + relay --> fuel pump
                      |-- fuse --> injectors
                      |-- fuse --> coil power
                      |-- fuse --> IAC/solenoids as appropriate
                      |-- fuse --> DC idle H-bridge own supply and local noise suppression

Return tree: ECU power reference -> specified engine/star ground
             sensor reference -> ECU sensor ground only
             H-bridge motor return -> separately routed high-current star return
             coils/pump/actuators -> appropriate power ground(s)
```
Actual star locations, conductor cross sections, relay states and fuse ratings remain TBD. Avoid routing pulsed motor return currents through ECU ground screws or signal reference conductors. High-side/low-side suppression and transient energy paths must be engineered for the actual drive topology.

## Measurement protocol
1. Load-specific voltage-drop tests with a single explicitly documented negative reference; include both supply and return paths. Use cold and heat-soaked conditions.
2. Measure separately: battery+ to box inlet; fuse contacts; relay contacts; polyfuse if present; box outlet to ECU; ECU ground to battery-. Document load, voltage, RPM and temperature simultaneously.
3. Branch currents (continuous and inrush) have **not yet been measured**. Use correct DC-rated equipment and protect the circuit during tests.
4. Inspect original installed PCB (not just reference PDF), fuses, relay model numbers, connectors, solder cracks and terminal tension before relying on component-level attribution.
5. Do not bypass a protective component in vehicle service just to reduce its voltage drop.

## Exact unknowns to resolve
- All current ECU feed and ground pins after Mega144H7 retrofit.
- Actual fuel pump relay coil command and downstream power return.
- Injector/ignition distribution, in-use fuse values and ground routing.
- H-bridge motor supply/return cable sizes, filter/TVS and measured current.
- Whether original CB2/CB1/CB3 resettable polyfuses remain fitted.
- Fan/fuel-pump/LC-1 heater and solenoid power sources.
- Any current dependence on factory Volvo fuse/relay board.

## Trace and measurement register

Individual positive and return segments, especially the **shared ECU/H-bridge terminal** and the fuel pump relay shutdown path, are tracked as E01–E09 and E19–E20 in [the electrical evidence ledger](ELECTRICAL_EVIDENCE_LEDGER.md). Use [the measurement worksheet](ELECTRICAL_MEASUREMENT_WORKSHEET.md) for actual probe locations, load states, current and temperature. These documents do not assert that the proposed return-tree topology is installed.
