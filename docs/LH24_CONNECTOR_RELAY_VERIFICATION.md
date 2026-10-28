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

## Latest in-car measurements — 2026-10-28

**User-reported test, vehicle 1997 B230FK with disconnected original LH ECU:**

- Battery: **12.38 V**.
- LH harness pin **21 to chassis ground**: **12.38 V** with control apparently *released* (the user reports manually applying ground to operate the main relay; capture exact key/jumper state in future readings).
- Grounding LH pin **21** made the old factory main fuel-system relay **audibly click** and power appear on LH pin **9**.
- LH pin **9 to chassis ground**, main relay manually activated: **11.17–11.25 V**, fluctuating ~0.08 V; ignition position during this last test and any connected legacy load not yet recorded.
- The apparent battery-to-pin-9 gap is **1.13–1.21 V**, but battery and pin9 are not yet verified as *simultaneous* under the same load/reference. This is an **apparent system-level difference**, **not** a measured drop across relay contacts.

**Interpretation:** The successful click and energized pin 9 strongly support continuity of LH pin 21's low-side coil-control path and operation of the relay's main section. Released pin 21 being at battery potential can arise through the relay coil and is not itself a power-feed current-capacity measurement. Volvo LH 2.4 service data expects battery voltage at pin 9 when pin 21 is grounded; the observed ~11.2 V deserves further investigation rather than treating the original OEM switched output as ready to carry the H-bridge.

**Next noninvasive checks (no fuse or harness changes):**

1. With relay ground-control jumper *removed*, recheck pin 9 is off; record ignition state, battery voltage and measurement reference.
2. While the main relay is briefly energized normally via the already-established current-limited, fused low-side test, use the **same reference ground** for battery, LH **pin 4** (terminal 30 reference) and LH **pin 9** (main relay output), recording key position, and whether any original load remains connected. Compare within the same stable state.
3. If pin 4 stays near 12.38 V but pin 9 is ~11.2 V, isolate a loss **between the relay feed/contacts/output wiring and pin 9**, or a remaining connected load; don't conclude bad contacts from the connector voltages alone.
4. If pin 4 also drops toward ~11.2 V under the same relay-on state, check the **upstream original LH feed/fuses/connection route** before blaming relay contacts. The proper relay contact feed must eventually be checked independently, since pin 4 may not share precisely the same path.
5. If still unexplained and access allows safely, use the *correctly identified* relay socket/terminal data to measure separately **contact 30→87/1** under its normal load and **87/1→LH pin 9**. A relay click proves coil operation, not low-resistance contacts. Do **not** probe crowded live terminals with uninsulated tips or bypass contacts.
6. Treat voltage under current draw as a design prerequisite: a high-impedance meter alone cannot verify motor-current capacity. Do not attach the H-bridge or add a larger fuse to "fix" a 1 V discrepancy.

Distinguish this factory wiring measurement from the **independent aftermarket MS/EpicEFI relay-board and CB2 supply-drop investigation**; they are two different circuits.

## Battery-post repeat under relay load — 2026-10-28

**User-confirmed new measurement** while briefly grounding LH pin 21 to activate the original factory main relay, ignition key **OFF**:

| Test point | Relay OFF | Relay ON | Notes |
|---|---:|---:|---|
| Battery positive relative to battery negative, at battery | **12.38 V** | **12.34 V** | Voltage falls only ~0.04 V |
| LH connector pin 4 relative to chassis ground | **12.38 V** | **~11.25 V** | Previously reported with the same relay activation |
| LH connector pin 9 relative to chassis ground | **0 V** | **11.17–11.25 V** | Previous user report |

Under relay-on conditions, the battery-versus-LH-pin-4 comparison differs by **~1.09 V**, much more than the battery's own ~0.04 V drop. **Caveat:** battery values used battery-negative reference, and LH pin 4/pin 9 measurements used chassis ground. Until the voltage is measured directly across the positive feed and checked against the ground-reference offset under the same relay-on state, the difference must **not** be called a proven positive-side wiring drop. Pin 4 and 9 being nearly equal similarly does **not** prove the relay contact is free of voltage drop: they may have independent upstream branches.

**Most discriminating next safe measurement:** With appropriate protected access to LH pin 4, key OFF and original main relay briefly activated by its already-confirmed pin 21 control, measure **DC volts directly across battery positive (red probe) and LH pin 4 (black probe)**. A ~1.09 V reading implies an appreciable positive-feed drop to pin 4; ~0 V implies a chassis/reference offset or measurement artifact instead. Do not place an ammeter across these points. If feasible also measure **chassis-ground reference point to battery negative** under the same conditions; do not probe inaccessible live cavities or leave an unattended ground jumper. Keep H-bridge disconnected from the original circuit pending investigation.

## Dynamic direct positive-feed voltage loss and relay comparison — 2026-10-28

**New user measurement:** with original LH main relay manually energized via ground command at disconnected LH ECU **pin 21**, meter leads **red on battery positive, black on LH pin 4**, observed **1.25 V initially**, falling gradually toward **0.87 V**, then increasing again slowly. Value did not settle. Engine/key OFF as previously reported; current draw and exact run duration are not measured. Previous battery off/on readings were 12.38/12.34 V respectively.

This is a **direct positive-path voltage difference** between battery positive and the original LH pin 4, not an artifact of the chassis-ground reference used previously. The slowly varying gap is consistent with some combination of changing current and resistance in the original supply path; **neither defective relay contacts nor hot/cold solder joints is proved**. LH pin 4 is a permanent battery feed **not fed through the original main-relay switched contacts**, so a relay contact alone does not directly create the pin-4 drop. However the main relay may energize old connected loads, or a relay-related fault may cause abnormal load, revealing a weak common battery/fuse/connector feed.

### Reference-backed relay deterioration (context, not a vehicle diagnosis)

Volvo Owners' Club 700/900 electrical FAQ records cracked relay internal solder joints, high-resistance relay contacts and overheated/marginal female socket crimps as common failures, plus replacement-relay configuration differences in 1994+ 940s. Reference: https://www.volvoclub.org.uk/faq/ElectricalCircuitsRelays.html . The turbo fuel-injection relay's common **two-section** design uses low-side coil controls 86/1 via LH21 (main) and 86/2 via LH20 (pump); using LH20 is **not** a truly independent relay comparison, and may unexpectedly power old pump wiring. Sources: https://www.davebarton.com/pdf/Harness_LH-2.4-940EZKPinFunctions2024.pdf ; https://lemon-manuals.org.ua/Volvo/1993/940%20L4-2320cc%202.3L%20SOHC%20VIN%2083%20B230FD/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Powertrain%20Management/Relays%20and%20Modules%20-%20Fuel%20Delivery%20and%20Air%20Induction/Main%20Relay%20%28Computer%2FFuel%20System%29/Testing%20and%20Inspection/Bosch/ .

### Comparison plan — before H-bridge reuse

| Comparison | What to measure | What it establishes / does not |
|---|---|---|
| A. Existing original main relay | Direct battery+ to LH4, relay OFF then ON; battery voltage and LH9 to same ground, key and duration noted | Reconfirm time-varying 0.87–1.25 V positive feed difference and switched output |
| B. **Known-good exact electrical/part-number replacement** fuel relay in the same original socket | Repeat A under same conditions | Strong evidence for or against *relay module* contribution. Must match physical and electrical form, not just colour or shape; 1994+ Hella blue and older white relay variants may not be interchangeable |
| C. **Genuinely independent** factory relay source (different existing original relay circuit) | Identify its powered input and switched output; measure direct battery+ to that circuit's feed/output when energized, along with battery voltage | Helps determine whether issue is local to old injection wiring or is shared factory feed, but must use suitable genuinely available relay/socket and known loads |
| D. Same old relay, feed section isolation when accessible | Direct voltage drop across fuse and fuse holder, contact feed 30, across main contact 30→87/1, and from relay output to LH9 | Can localize fault if topology verified; avoid blind live probing in cramped panel |

**Avoid** replacing a still-used relay from another vehicle system, trying LH20 to trigger the pump section, inserting a visually similar but electrically different relay, bridging fuse/relay contacts, increasing fuse ratings, or attaching the H-bridge before the stock feed has been characterized. A genuinely independent spare OEM relay (e.g., a no-longer-used old overdrive position in an M90 vehicle) is only a **conditional candidate**: the socket/terminals may not be populated or switched, and other original vehicle systems still operate from the factory board. OEM relay 2/12 suppression may also be downstream of the old main-injection feed and so would not be independent.

**High-value next result:** exact part number/type of the currently installed factory fuel-injection relay and a matched battery+→LH4 comparison with an exact replacement, if one is available. This avoids needing to cut wiring under the fuse panel or prematurely blame the relay.

## Decision boundary

- **If key 15 is still available at LH pin 35,** that is a useful **control signal candidate** for a *properly fused/engineered coil driver*, but does not establish the pin 35 harness is able to source the DC idle motor current.
- **If 20/21 continuity to an intact original relay socket is confirmed,** those abandoned lines may provide convenient access from the old ECU connector to the relay coils, avoiding immediate cutting beneath the fuse panel. The factory LH ECU used separate low-side commands for main-system and pump relay sections; controlling just one section must be assessed against the relay's internal operation and any retained outputs.
- **If no continuity, supply or suitable original socket exists,** stop and consider a dedicated relay/harness instead of guessing or cutting.
- The H-bridge shall have its own coordinated **fused motor supply**, **separate actuator power ground return**, switching supply in required RUN/START states and a safe position on power loss. Keep current EpicEFI ECU/fuel-pump power and shutdown paths untouched. Do not energize old factory pump wiring or abandoned circuits blindly.
- No relay socket pinout, wire splice, fuse rating or cutting/repurposing authorization is established by a 1995 document alone. The as-fitted 1997 loom measurement wins.
