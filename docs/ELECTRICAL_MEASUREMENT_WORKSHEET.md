# As-built inspection and electrical measurement worksheet

**Vehicle:** Volvo 940 Turbo / EpicEFI Mega144H7  
**Purpose:** close F6 (physical inventory) and support F7 (quantitative requirements). Record raw observations. Empty fields mean **not measured**, not zero.

## Session identification

| Field | Record |
|---|---|
| Date/time/time zone | TBD |
| Technician / observer | TBD |
| Vehicle condition (cold/heat-soaked) | TBD |
| Ambient / board / relay temperature (method) | TBD |
| Battery resting voltage and condition | TBD |
| Engine RPM, CLT, fan, pump and other load states | TBD |
| Charging voltage at specified reference | TBD |
| Instrument model, range, calibration / resolution | TBD |
| Test reference point and physical probe location | TBD |
| Evidence: text description, existing wiring drawing, photo (optional), log or meter record | TBD |

## Current confirmed-by-user wiring (2026-10-27)

| Connection | User-reported as installed | What this does not establish |
|---|---|---|
| External main protection | Separate **30 A** fuse close to battery on permanent + feed to MS box | Cable cross section, fuse type/location distance and onboard F1 value |
| MS X1 | Permanent battery +12 V downstream of external 30 A fuse | Installed internal board distribution and voltage drop |
| MS X2 | Switched +12 V | Source circuit and loaded drop |
| MS X3 | Engine ground | Full return route and loaded drop |
| ECU + screw | MS box positive cable; ECU and DC H-bridge positive both connected here | Whether actual feed passes K1/CB2 |
| ECU ground screw | MS box ground cable; ECU and DC H-bridge ground both connected here | Whether PWM return causes voltage offset |

These observations are retained as **user-reported installed** rather than laboratory measurements. Do not repeat photo requests for these facts.

### Highest-priority measurements (when safe and accessible)

1. With known, **normal** operating states, compare MS box ECU-feed output and ECU + screw voltage relative to the same documented reference; do not purposely induce shutdowns by aggressive PID tuning.
2. Measure the DC voltage between ECU ground screw and the MS box return / engine reference while H-bridge is operating normally. For fast PWM spikes, a properly grounded oscilloscope/differential measurement may be necessary; a DMM average cannot exclude transients.
3. Record ECU logged battery voltage, RPM and DC idle output/PWM simultaneously if available, noting timestamp, temperature and load.
4. If accessible without live-circuit short risk, measure the voltage across installed F1, K1 and any confirmed CB2 under steady load to localize a resistive/protective device. **Do not bridge or defeat protection.**
5. Establish external 30 A fuse protection suitability only after cable size, routing and additional downstream protections are documented.

## Physical trace sheet — repeat per branch

| ID | Source terminal | Destination terminal | Connector cavity | Conductor marking / measured size | Fuse position and installed marking | Relay markings/contact terminals | Ground return path | Evidence text/record/date |
|---|---|---|---|---|---|---|---|---|
| E01–E20 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

Begin with the PDF-derived X1–X3, JP1 and JP2 labels in `ORIGINAL_RELAY_BOARD_PDF_MAP.md`, then record *actual* uses in words. Photos are optional when installation is cramped. Label wire markings as **observed** until conductor cross-section is confirmed. Record uncertain or modified splices separately, including whether they are crimped, soldered or terminal-block connections.

## Loaded voltage-drop session — one row per segment per load state

Measure directly across the two ends of the segment when feasible, and note polarity. If using a shared negative reference for two separately measured absolute voltages, take readings promptly under the same stable load and record their difference; never combine readings across separate sessions.

| Timestamp | Segment (e.g. battery+→box input) | Probe A physical point | Probe B physical point | Load/RPM state | Voltage A-to-B (mV) | Current (A, independently measured) | Temperature | Instrument/method | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | Not measured | Not measured | TBD | TBD | TBD |

**Required segment set (where physically confirmed):** source positive→box inlet; fuse inlet→outlet; main relay contact inlet→outlet; any *actually installed* polyfuse inlet→outlet; box outlet→ECU terminal; ECU power-ground→battery-negative/engine-star ground; H-bridge feed and return individually. Repeat in appropriate load states rather than assuming one total result covers all conditions.

## Dynamic observations / fault-state record

| Test/state | Expected safe behavior (to verify) | Observation | Evidence |
|---|---|---|---|
| Key OFF | Fuel pump OFF, no unintended retained engine loads | Not tested | TBD |
| Key ON, engine stopped after any allowed prime | Fuel pump OFF outside any explicitly documented prime window | Not tested | TBD |
| Engine running normally | Stable ECU supply and correct fuel-pump behavior | Not tested | TBD |
| Engine stall / ECU command loss | Pump shuts down through the defined hardware/ECU control logic | Not tested | TBD |
| DC idle H-bridge PWM change | No unacceptable ECU supply/ground disturbance | Not tested | TBD |
| Hot relays / fan or pump startup | No thermal anomaly or supply brownout | Not tested | TBD |

These are **observation targets**, not instructions to disable fuel, unplug the running ECU or provoke dangerous faults on the road. Failure injection and high-current tests require a separately planned safe bench procedure and suitable instruments.

## Measurement safety and acceptance boundaries

- Do not bridge fuse or relay contacts, bypass protection, probe high-current conductors with an unfused meter-current input, or disturb ECU sensor ground.
- Check meter lead placement and fuse rating before changing voltage/current modes. Current must be measured with a suitable, rated clamp or other appropriate non-destructive method; do not place a handheld ammeter across the battery.
- Identify terminals from the original schematic and the user's text wiring description first; do not require cramped-space photos or intrusive access. Disconnect battery negative only according to an appropriate vehicle-service procedure, protecting ECU and other electronics.
- Keep probes clear of belts, fan, hot manifold and moving linkages. For live tests use appropriately secured probes and an assistant where needed.
- Never treat heat felt through plastic as a temperature measurement. Record instrument, surface and ambient conditions if thermal comparison is needed.
- No fuse, cable, relay, TVS or PCB rating is finalized until measured currents, wiring and thermal/fault requirements are reviewed.
