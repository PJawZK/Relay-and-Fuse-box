# Power and ground tree — as-installed reconstruction (2026-10-27)

This is a **partial logical map**, not a verified pin-to-pin harness drawing. Do not use as a production wiring diagram. Source categories: (R) user-reported installed, (H) historical previous-generation wiring, (P) planned, (?) not confirmed.

## Important separation: aftermarket EFI vs original Volvo harness

**Authoritative user clarification (2026-10-27):** No wiring, fuse or relay from the original Volvo/LH-Jetronic EFI system is used for the current EpicEFI engine management. The MS relay/fuse box shown below is a separately installed **aftermarket** component, despite its age and unmodified internal design. The Volvo's old LH fuel/EFI relays are therefore **potential spare/reuse hardware**, but their present electrical state, available feed and remaining non-ECU branches must still be proven. See `VOLVO_FACTORY_RELAY_REUSE_RESEARCH.md`.

## Current positive power (user-reported connections plus PDF reference)

```text
Battery permanent +12 V
  |
  +-- external 30 A fuse (R: close to battery; exact position/type/gauge TBD)
       |
       +-- MS relay-box X1 (R: unswitched battery +12 V)
              |
              +-- internal board power distribution
                   [H: B&G schematic suggests F1 -> 12U -> K1 -> CB2 -> 12 RAW]
                   [U: exact installed PCB revision, fuse rating and feed net]
                   |
                   +-- cable from MS box -> ECU positive screw terminal (R)
                                           |--> ECU power (R)
                                           +--> DIY DC idle H-bridge + (R)

Switched +12 V ----> MS box X2 (R)
Engine ground -----> MS box X3 (R)
```

**Source distinction:** The upstream **30 A fuse** is a separate, user-reported part located closer to the battery; it is **not** the B&G drawing's onboard F1 (nominal 20 A illustrated, application-dependent). The actual F1 fuse and installed K1/CB2 status remain unverified. The reported ECU/H-bridge common junction is on the **ECU screw terminals**, not at the relay-box screw block.

Other reference-only branches in the B&G PDF: K2/F2 fuel-pump relay/fuse; F3/F4 injector feeds; K3 fast-idle relay. Their current physical wiring and loading are unconfirmed. Coil +12V, dual boost solenoids, LC-1 heater, fan, dash/CAN and other auxiliary feeds must be mapped independently; do not infer their origins from earlier ECU wiring.

## Current return path (user-reported junction; upstream net unresolved)

```text
MS relay-box ground cable (R: ground cable supplied from box)
   |
   +--> ECU ground screw terminal (R)
          |--> ECU ground (R)
          +--> DIY DC idle H-bridge power ground (R)

MS box X3 <---- engine ground (R: terminal connected as original design)

How ECU ground screw connects through the MS box to X3 and the
battery-/engine/chassis network = not yet independently traced.
```

The shared supply **and** return represent possible common-impedance coupling under H-bridge PWM. If the actual ECU screw-terminal feed traverses the schematic's resettable **CB2** polyfuse, H-bridge load transients could also increase its voltage drop or lead to a thermal trip and delayed recovery. These are **two distinct hypotheses**, neither confirmed as the cause of ECU shutdown. The 30 A upstream fuse does not rule out a local protective device operating or a downstream ground disturbance.

A historical battery-negative-to-engine/star-ground test measured <0.1 V in one operating condition; it does not verify every return segment during PWM transients.

## Near-term H-bridge relocation plan — **not installed**

As of 2026-10-27 the user intends to remove H-bridge motor positive and power ground from the ECU's screw terminals and connect the actuator to a **separate switched and fused circuit** from the Volvo's original relay/fuse system. This is a practical isolation experiment and may eliminate both shared ECU screw-terminal impedance and H-bridge load on the MS-board `CB2` branch **if** the new positive takeoff is truly upstream/independent of `12 RAW`. The existing configuration remains as drawn above until the user confirms physical completion.

The current EpicEFI fuel-pump system uses its **own** relay, fuse and wiring; the factory Volvo fuel-injection relays are not part of the current pump/ECU safety circuit. Abandoned OEM fuel-injection relay positions (especially reference 2/23, conditionally 2/13) are thus meaningful **reuse candidates**, but their coils may no longer energize when the LH ECU is gone, and no socket capacity or remaining load is established. The original Volvo 940 distribution includes fuel-injection/system relay functions (1995 Volvo 940 turbo factory-style diagram overview: https://charm.li/Volvo/1995/940%20L4-2320cc%202.3L%20SOHC%20Turbo%20VIN%2086%20B230FT/Repair%20and%20Diagnosis/Diagrams/Electrical%20Diagrams/Power%20and%20Ground%20Distribution/System%20Diagram/). The exact 1997 B230FK as-retrofitted relay usage and control state must be confirmed; an LH-era relay may be unused, partly repurposed, or still feed ignition/other loads.

**Selection checks:** switched ON in both RUN and START if the throttle actuator requires it; off when key off; current capacity/relay/contact condition; fuse and conductor coordination; no dependency on fuel pump run/prime command; no disturbance to actual pump voltage or shutdown; a dedicated H-bridge motor-current ground return; appropriate H-bridge electrical suppression; acceptable throttle-plate failsafe position on relay/fuse loss. Do not tap a motor directly into ECU sensor ground, `12 RAW`, or a fuel-pump motor output simply because it has a convenient terminal.

## Updated H-bridge supply and grounding plan — user decision 2026-10-28 (NOT installed)

The user has **rejected reusing old factory Volvo relay modules and old OEM supply wiring** after load-related voltage drop findings (including direct battery+→LH pin4 0.87–1.25 V while original white E relay energized, followed by further old M circuit voltage loss). Historical relay mapping remains diagnostic evidence only. **Recommended plan:** use a new independent automotive relay and appropriately rated upstream fuse and wire, with confirmed supply in RUN and START where needed, and positive shutoff key OFF; DO NOT rely on now-suspect original distribution rails, the aged aftermarket MS/EpicEFI ECU feed/CB2 polyfuse, or existing ECU screws for H-bridge motor power.

**Ground comparison:** The user already has a deliberately arranged engine-block star-ground architecture, with higher-load and low-level grounds separated in nearby locations on the engine. Prefer a **new dedicated adequately sized H-bridge motor-power ground conductor from H-bridge's power GND to the high-current engine-block star stud or adjacent verified power-ground point**, using its own properly crimped lug, clean protected metal, tight mechanical connection and full-size shared engine↔battery negative bond. Do not daisy-chain via ECU ground, ECU sensor return, ECU supply screw, 5 V sensor ground or small-signal logic reference. A chassis return near the H-bridge is *electrically acceptable* if the chosen bare-metal, mechanically robust ground stud and chassis-to-engine/battery straps pass a loaded **actual ground-voltage-drop measurement** at the H-bridge's PWM/inrush current; an unverified factory body screw is not an equivalent substitute. Avoid unnecessary parallel chassis+engine motor-return cables.

Keep motor's **both leads on the H-bridge output pair**, not chassis. H-bridge logic may require a separate, low-current **ECU signal return/reference**: preserve driver datasheet ground/common-mode requirements even though high-current motor return is separately routed. Keep local low-ESR decoupling, loop area, transient suppression and coil flyback control appropriate to exact H-bridge and relay. Size fuse to wire/driver/motor rated and peak current after those data are obtained; no specific ampacity or relay part yet approved.

**Post-install measurements:** With motor PWM active, measure battery positive→H-bridge supply positive, H-bridge power GND→battery negative, and H-bridge power GND→ECU ground reference; log engine RPM, ECU VBatt, actuation and crank/run transition. Validate safe idle control and no power-loss induced unintended engine behavior. This plan is uninstalled, not a proven cure for ECU shutdowns.

Sources: https://www.ti.com/lit/an/slva959b/slva959b.pdf ; https://support.haltech.com/portal/en/kb/articles/ecu-grounding-the-dos-and-donts ; https://diyautotune.com/blogs/technical-articles/grounds

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
4. Start with `ORIGINAL_RELAY_BOARD_PDF_MAP.md` for source-defined terminals/components and user text to identify current hookup. Investigate the installed PCB, contact state, and fuse/relay markings only where a specific discrepancy or measured loss demands it; photographs are optional.
5. Do not bypass a protective component in vehicle service just to reduce its voltage drop.

## Exact unknowns to resolve
- All current ECU feed and ground pins after Mega144H7 retrofit.
- Actual fuel pump relay coil command and downstream power return.
- Injector/ignition distribution, in-use fuse values and ground routing.
- H-bridge motor supply/return cable sizes, filter/TVS and measured current.
- Whether original CB2/CB1/CB3 resettable polyfuses remain fitted.
- Fan/fuel-pump/LC-1 heater and solenoid power sources.
- Current EpicEFI **does not depend on original Volvo EFI fuse/relay board** (user-confirmed); remaining unknown is whether original factory relay/socket hardware provides an appropriate separate ignition-switched feed for the proposed H-bridge.

## Trace and measurement register

Individual positive and return segments, especially the **shared ECU/H-bridge terminal** and the fuel pump relay shutdown path, are tracked as E01–E09 and E19–E20 in [the electrical evidence ledger](ELECTRICAL_EVIDENCE_LEDGER.md). Use [the measurement worksheet](ELECTRICAL_MEASUREMENT_WORKSHEET.md) for actual probe locations, load states, current and temperature. These documents do not assert that the proposed return-tree topology is installed.
