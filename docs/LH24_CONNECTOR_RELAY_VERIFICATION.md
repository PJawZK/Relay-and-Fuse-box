# LH2.4 ECU connector — non-invasive original relay wiring verification

_Date: 2026-10-27. Vehicle: 1997 Volvo 940 B230FK / M90 sedan, engine managed by separately installed Mega144H7/EpicEFI._

## User's intended approach

Before modifying/cutting wires beneath the original Volvo relay/fuse panel, **test the unused OEM LH2.4 ECU harness connector**. Existing wires are accessible near the former LH ECU and may connect directly to the original dual-section fuel-injection relay. The current EpicEFI installation uses **none** of the factory EFI wiring, relays or fuses. A candidate factory relay may be repurposed to supply the separate DC idle H-bridge, but **no change is installed or approved yet**.

**Critical logic:** On LH2.4 the ECU **produces** low-side relay-coil commands. With the original LH ECU absent, wires at its plug do not acquire the command from the ignition switch by themselves. A high-impedance voltmeter may see +12 V at a released low-side line through the relay coil: **this is not a ground/active trigger**. A new correctly rated low-side switch/relay driver would be required if using these OEM coil circuits. Do not bridge relay contacts or connect 12 V directly to the old ECU relay-control wires.

## Source-grounded candidate pin functions

Pin functions below are from Dave Barton's `LH 2.4 ECU PIN FUNCTIONS 940 B230F/FT` (2024 pin-function PDF, front-view connector), corroborated for pin 20/21 by LH ECU service data for 1993 940. This is a **model-family reference**, not verification of cavities/colors in this specific 1997 B230FK car.

| 35-way LH ECU connector cavity | Reference wire colour | Original function | Test interpretation |
|---|---|---|---|
| 20 | Y-BK (yellow/black) | ECU **ground-sinking** fuel-pump relay control, original relay `86/2` | Should be traced for **continuity** to correct relay-coil terminal; no LH ECU means no normal low-side drive |
| 21 | R (red) | ECU **ground-sinking** main-system relay control, original relay `86/1` | Candidate for independent coil control only after confirming relay type/socket and loads |
| 35 | BL (blue) | Ignition-switched **input** from key terminal 15 (RUN) | Check OFF/RUN/**START**, including voltage under appropriate load; reference not motor feed |
| 4 | W or Y-BN | Battery supply, **terminal 30** | May be permanently live even key OFF; test for unexpected backfeed |
| 9 | BL-Y (blue/yellow) | +12 V **output from energized main fuel-system relay** to ECU | If original relay is no longer commanded, pin 9 may remain dead; do not infer terminal-15 state from it |

Sources:
- https://www.davebarton.com/pdf/Harness_LH-2.4-940EZKPinFunctions2024.pdf
- https://lemon-manuals.org.ua/Volvo/1993/940%20L4-2320cc%202.3L%20SOHC%20VIN%2083%20B230FD/Repair%20and%20Diagnosis/Diagrams/Connector%20Views/Engine%20Control%20Module/
- https://www.240turbo.com/fuelpumprelay.html

**Connector orientation:** The reference diagram labels its cavity numbering as **front view of connector**. When measuring the loom side, positively identify cavity numbering rather than mirroring a rear/wire-side view. Wire colors may vary between model years and markets and cannot replace cavity identification.

## Two-pass verification without cutting harness wires

### Pass A: Voltage presence (ignition system intact; LH plug unplugged from ECU)

- Use a high-impedance DC voltmeter and insulated fine back-probe / suitable test lead; **never bridge adjacent LH connector cavities**. Verify the meter is in **voltage** mode, not ampere/current mode.
- Reference the **same confirmed battery-negative/chassis ground** for each voltage measurement. Record battery voltage too.
- At **pin 4**, compare OFF and RUN (expect constant supply **if original factory feed/fuse is intact**).
- At **pin 35**, compare OFF and RUN; START measurement only if safely arranged and useful to confirm coil availability while cranking. Pin 35 is originally a key input; do not use it as an H-bridge motor feed.
- At **pin 9**, check whether original main-relay switched output becomes live. Without LH ECU coil command this may remain OFF, which is expected and does **not** imply a broken terminal-15 ignition feed.
- At **pins 20/21**, a voltage reading alone does **not** prove relay activation. These were **ground-switching outputs** of an ECU which is no longer connected. If original relay coils remain connected, the released pins may appear positive via a coil feed.
- When operating the vehicle, keep testing non-invasive and avoid accidental contact with live heavy-current wiring. Do not deliberately recreate ECU brownouts or shutdowns during driving.

### Pass B: Static relay-coil continuity (engine OFF, all sources isolated)

- Confirm battery negative disconnected under an appropriate service procedure, no stored/alternative power sources, LH ECU connector still unused, and identify the actual old injection-relay socket.
- With old relay removed, confirm continuity between **LH pin 20 ↔ candidate relay socket 86/2** and **LH pin 21 ↔ 86/1** where those numbered cavities truly exist. Measure wire-to-wire continuity, not through an energized coil.
- Verify no shorts to adjacent cavities/ground and whether each candidate coil terminal remains connected to expected upstream circuit(s). A mismatch means stop and re-identify variant/harness.
- Identify separately the high-current contact **feed** and **output** terminals and any downstream legacy loads **without energizing** the circuit. Do not assume the relay has no consumers just because the engine management was replaced.
- The older 1995 wiring PDF was referenced in prior chats (`Volvo 940 (1995) Wiring Diagrams - Copy.pdf`), but exact previously uploaded bytes were inaccessible as of this note; it must be compared if recovered. Dave Barton's drawing depicts six-position original fuel-relay contact/coil names from **the bottom of the relay**, a different viewing direction from ECU-front connector view.

## Recorded measurement sheet

| Date / key state | Test node (LH pin or relay cavity) | Measured V or continuity / reference | Original relay fitted or removed | Interpretation / uncertainty |
|---|---|---|---|---|
| TBD OFF | LH 4 | Not measured | TBD | Terminal 30 check |
| TBD RUN | LH 35 | Not measured | TBD | Terminal 15 check |
| TBD START | LH 35 | Not measured | TBD | Cranking state check |
| TBD RUN | LH 9 | Not measured | TBD | Main-relay contact output |
| TBD power isolated | LH 20 ↔ old relay 86/2 | Not measured | Relay removed | Low-side control wire continuity |
| TBD power isolated | LH 21 ↔ old relay 86/1 | Not measured | Relay removed | Low-side control wire continuity |

## Decision boundary

- **If key 15 is still available at LH pin 35,** that is a useful **control signal candidate** for a *properly fused/engineered coil driver*, but does not establish the pin 35 harness is able to source the DC idle motor current.
- **If 20/21 continuity to an intact original relay socket is confirmed,** those abandoned lines may provide convenient access from the old ECU connector to the relay coils, avoiding immediate cutting beneath the fuse panel. The factory LH ECU used separate low-side commands for main-system and pump relay sections; controlling just one section must be assessed against the relay's internal operation and any retained outputs.
- **If no continuity, supply or suitable original socket exists,** stop and consider a dedicated relay/harness instead of guessing or cutting.
- The H-bridge shall have its own coordinated **fused motor supply**, **separate actuator power ground return**, switching supply in required RUN/START states and a safe position on power loss. Keep current EpicEFI ECU/fuel-pump power and shutdown paths untouched. Do not energize old factory pump wiring or abandoned circuits blindly.
- No relay socket pinout, wire splice, fuse rating or cutting/repurposing authorization is established by a 1995 document alone. The as-fitted 1997 loom measurement wins.
