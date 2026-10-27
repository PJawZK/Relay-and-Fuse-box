# Volvo 940 EFI Relay and Fuse Distribution

A passive, serviceable relay-and-fuse power-distribution replacement concept for the Volvo 940 Turbo using Mega144H7 / EpicEFI. **Design phase: research only. No PCB has been validated for vehicle use.**

## Goals
- Low-resistance high-current supply paths; do not assume the old PCB alone caused measured voltage losses.
- Standard replaceable Micro ISO automotive relays, individually replaceable fuses, accessible wiring terminals.
- Separate high-current H-bridge feed and return from the ECU supply terminal.
- Automotive transient/EMI protection designed per load without imposing unnecessary series resistance.
- No MCU, proprietary configuration software, or Windows dependency for the power-distribution function.
- Document component sourcing, connector ratings, fuse coordination, tests, and fail-safe fuel pump behavior.

## Historical measurements (not component-level isolation)
- September 2025: alternator 13.9–14.0 V; ECU approximately 13.2 V, a system-wide difference of about 0.7–0.8 V.
- September 14 2025: relay-board output 13.56 V versus ECU 13.35 V using a common engine/star ground: 0.21 V drop downstream of the measured relay output.
- Previous estimate: alternator to relay input 0.34–0.44 V.
- Battery negative to engine/star ground below 0.1 V in one test; switched ignition supply within 0–0.3 V of battery.
- May 2026: approximate reported 0.2–0.5 V between relay-board input and ECU supply; measurement conditions/path need reconciling.
- No separately measured voltage drop across F1, K1, CB2, connectors or board traces; no measured current by branch yet.

## Historical source schematics
User-supplied Bowling & Grippo 'MegaSquirt Power Distribution Board' v1.2 (2002): `mspower_ShemV1.2.pdf` (2 pages) and `mspower_LayoutV1.2.pdf` (3 pages). Not yet added as binary files to this repository.

The schematic's main ECU feed is F1 (20A indicated, application-dependent) → K1 relay → CB2 RXE105 resettable polyfuse → 12 RAW / ECU. CB1 RXE110 and CB3 RXE110 also appear on the board; F2 is fuel-pump fuse; F3/F4 injector fuses. This schematic is a design reference, not proof that the user's manufactured board has identical copper/components after 15–16 years.

## Design gates
1. Confirm present wiring, actual circuit load currents, wire sizes, fuses, relays, and which power/ground connections share ECU terminals.
2. Re-measure loaded segment-by-segment voltage losses at input, F1, K1, CB2, output, downstream harness. Record temperature.
3. Draw system architecture, net names, power/ground topology, fuse/relay service policy, and connector pinout.
4. Select rated components, perform wire/fuse/trace temperature-rise and fault analysis, then draft KiCad schematic.
5. KiCad ERC, PCB DRC, independent netlist review, BOM/footprint audits, transient protection review.
6. Bench load, startup/brownout, relay flyback, H-bridge PWM noise, high-temperature and fault-injection tests before vehicle installation.

## Engineering rules
- Do not treat DC voltage drops as 'current drops'; measure both voltage and current separately.
- Never bypass or remove circuit protection to solve voltage drop without a safer equivalent.
- Critical ECU/fuel pump operation must not depend on agent tools, CAN messages or external software.
- AI-generated schematic and PCB edits require independent electrical review; automated ERC/DRC is necessary but insufficient.

## AI/KiCad tooling evaluation
- `ggurov/epicwolf`: multi-agent memory/handoff framework, not a circuit-design validator. Assess hook compatibility before vendoring; upstream contents licensed AGPL-3.0.
- KiCad 10 `kicad-cli`: baseline headless ERC/DRC/BOM/export tooling; ideal for CI.
- Seeed-Studio `kicad-mcp-server`: read-oriented inspection; schematic editing explicitly experimental.
- `nevenfo/kicad-agentic-mcp`: typed plans, rollback/evidence, KiCad IPC/CLI integration; evaluate license (AGPL-3.0) and maturity before adoption.
- Do not allow automatic Gerber release or direct commits to main solely based on AI review.

## Next step
Document actual connector/pin mapping and load paths of the existing installation; obtain circuit-by-circuit current and voltage drop measurements. Keep reference PDFs under `references/original-ms-power/` when uploaded.
