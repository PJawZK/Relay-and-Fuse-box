# HANDOFF — Volvo 940 EFI relay/fuse-box replacement

**Updated:** 2026-11-02  
**Repository:** `PJawZK/Relay-and-Fuse-box`  
**Authoritative baseline:** `main` at `0ecdeb1d53427caf14821544c135507135097dc7` (PR #24 merged; verified before preparing this handoff).  
**Phase:** F6/F7 planning and concept comparison; **no vehicle-ready schematic or PCB**.

> This document is the short entry point for the next ChatGPT/Codex/Codespaces session. Read it with `AGENTS.md`, `.wolf/STATUS.md`, and the linked source specifications. When old chat advice or archived investigations conflict with the **2026-11-02 user confirmations**, the confirmations below take precedence.

## Project objective and operating constraints

Replace the approximately 15–16-year-old aftermarket DIYAutoTune/MegaSquirt/Bowling & Grippo relay and fuse board powering the **1997 Volvo 940 Turbo B230FK, M90, Mega144H7/EpicEFI**. The original Volvo LH2.4 relay/fuse hardware is **not** part of the active EFI installation. The owner favors ordinary accessible replaceable automotive relays and blade fuses, neat centralized terminals, low voltage drop, good EMI/transient behavior, and no MCU, proprietary configuration program, Windows dependency, or CAN dependency for critical supply operation.

The project is browser-first across home PCs and browser-restricted work PCs: GitHub repo is the source of truth; Codespaces and Codex Cloud are the intended environments; GitHub Actions provides independent reproducible checks; EpicWolf is the chosen memory/status system. Do not assume a cloud chat can invoke the Codespaces-only KiCad MCP tool directly.

## Latest confirmed installed hardware and wiring (2026-11-02)

| Topic | Current authoritative status | Important boundary |
|---|---|---|
| ECU | Mega144H7 with EpicEFI, powered through existing aftermarket MS box | Exact existing ECU positive/return output and protection/current remain to be mapped |
| Main old-box inputs | **X1 permanent 12 V** with separate **30 A upstream fuse** near battery; **X2 ignition-switched 12 V**; **X3 engine ground**, user reported | X1 conductor is **estimated** about 4 mm² from insulation/appearance; not measured or approved to carry future expansion |
| Injectors | **Four Bosch EV14 0280158117 get +12 V from the MS box through TWO fuses, one per pair** | Exact pair/cylinder/JP2 terminal mapping remains unverified; four independent Mega144H7 sequential low-side driver channels must remain independent |
| Idle | Owner explicitly uses **NO PWM idle valve and NO Fast Idle** | Old B&G K3/J1/CB3 fast-idle function is obsolete and omitted from replacement; any older descriptions of a current PWM idle valve are superseded |
| DC idle H-bridge | Owner **installed a new independent relay and wiring**, reports operation is better | Keep external to new ECU box; actual new source branch/fuses/ground landing not confirmed, and the improvement does not prove root cause of all previous shutdowns |
| Fuel pump | Current pump is powered through the **aftermarket** relay system; ECU **PD10** commands fuel-pump relay | Preserve ECU-controlled prime/run/stop fail-safe; exact driver polarity/coil suppression/output/fuse/current to verify |
| Ignition | VAG 032 905 106B wasted-spark coil installed | Its present positive supply ownership and duty/peak current unknown |
| Boost | Two boost-control solenoids installed | Present +12 V source and fault grouping unknown |
| Wideband | Innovate LC-1 installed | Controller/heater supply and ground return ownership unknown |
| Fan | Radiator fan installed | Existing relay/feed and high motor start current unknown; external high-current branch preferred by default |
| Sensors | Current MAP/IAT/CLT/TPS/crank/cam/VSS/fuel-pressure wiring exists | Provide proper ECU reference or local IOX regulation, not one separate automotive relay/fuse per sensor |

**The existing injector two-fuse arrangement is an as-built fact; converting to one shared fuse is a PROPOSAL, not an already-made change.**

## Decisions already established — preserve without reopening

1. **Injector positive feed:** Favor **ONE** appropriately rated fused +12 V injector branch feeding all four EV14s; preserve four independent ECU ground-side controls. This decision awaits conductor/fault/peak-load analysis and is not permission to select a fuse ampere rating.
2. **Obsolete idle circuitry:** Do not reserve a relay/fuse for Fast Idle or PWM idle. Keep the new independently wired DC idle H-bridge external.
3. **Core engine functions:** Main ECU relay and ECU fuse, separate ECU PD10-controlled pump relay/fuse, injector positive fuse, ignition coil fuse if integrated, protected boost solenoid branch if integrated, LC-1 heater/controller branch if integrated. Fan and H-bridge high-current feeds may stay external.
4. **Physical expandability:** Study **four physical relay cavities** (R1 main; R2 pump; R3 optional auxiliary; R4 spare), with **12–14 physical blade-fuse cavities**. Only R1/R2 are baseline required; spare positions must not be left unintentionally live. This count is a **provisional packaging allowance**, not a finalized bill of materials or board size.
5. **Fuse-allocation concept:** F01 ECU; F02 all four injector positives; F03 ignition; F04 pump; F05 two boost valves; F06 wideband; F07 IOX/EGT electronics; F08 cabin CAN/displays feeder; F09 CarPi/logger; F10 sensor-controller aux; F11 actuator aux; F12 spare; F13/F14 optional. Positions are provisional **functions** with unknown ratings and some conditional ownership.
6. **Three principal distribution zones:** (E) engine-critical hardwired ECU/injectors/ignition/pump; (A) sensor and IOX expansion via protected automotive input and local 5 V/3.3 V conversion; (C) protected cabin/CAN/computer distribution with local regulation and branch fuses. Heavy motor feeds (H-bridge, fan, potentially upgraded pump) can use external high-current distribution.
7. **Avoid legacy complexity:** Do not copy historical JP1/JP2 signal pass-through, K3 fast idle, or CB2 series PTC solely because the 2002 reference PCB has them. The old B&G source schematic is historical evidence; installed board is stock by user report, but exact fitted components and thermal resistance paths remain unverified.
8. **Design goals:** Standard field-replaceable relays/fuses, good access and wire termination, low path resistance, appropriate source/branch fusing, distinct ECU sensor-ground and motor returns, suitable automotive transient/relay-coil protection, fail-safe pump shutdown and RUN/CRANK behavior.

## Planned upgrades and future feed implications

- **Fuel:** Replace current pump with a **255 L/h** unit; exact model/inrush/stall current is unknown. The pump relay/fuse path may need an external higher-current stage. Custom rail/FPR is mechanical; pressure transducer uses a sensor supply.
- **Engine instrumentation:** Reuse existing 200-PSI sensor for EMAP after fuel-rail conversion; four K-type EGT channels with MAX31856 converters and IOX controller; oil/fuel pressure and temperature; optional flex-fuel sensor. Sensors typically use ECU/IOX low-current reference or local regulated power. IOX and converter electronics get protected 12 V upstream with local 5 V/3.3 V rails.
- **User/chassis inputs:** Clutch/accelerator pedal sensors, possible brake position/switch, reverse/handbrake, front ABS VR/wheel speeds and additional wheel-speed channels. These mostly need protected signal conditioning and input capacity, not power relays.
- **Cockpit:** 940-DDS with two 2.8-inch 480×480 round LCDs and two 1.75-inch 466×466 AMOLEDs, ESP32-S3 nodes, 500-kbit/s CAN, rotary/steering/center nodes; reserve a **separate protected cabin feeder** and local display/node regulation.
- **Logging and computing:** Raspberry Pi 4 CarPi/HAT/NVMe, possible Pi Zero 2 shim, and future touch display. Plan dedicated protected feed and ignition/shutdown behavior; do not power cabin computers through the ECU critical rail.
- **No load-current extrapolation:** Part-level numbers quoted during planning (e.g., EV14 nominal resistance, EGT converter IC current, ESP32-S3 chip supply recommendation, Pi 4 5 V/3 A class) are starting reference specs and **not** measured complete-branch currents or approved fuse values.

Primary evidence: `docs/POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md` and `docs/POWER_DISTRIBUTION_EXPANSION_CAPACITY.md` (v0.2).

## Repo work already completed — do not repeat

- Browser/Codespaces foundation, EpicWolf integration, agent context and CI workflows are in repo. **F1 passed** for explicit EpicWolf status/context and tests; automatic native Codex memory hooks remain unverified.
- Codespaces observed **KiCad 9.0.2 / pcbnew 9.0.2** working. KiCad 10 is **not verified**. F2 limited pass; F3/F4 partial. A **fixture-only** restricted KiCad MCP façade with exactly one tool, `list_schematic_components`, returned R1/R2 through native Codex CLI: **F5 limited pass**, not general KiCad editing.
- PR #22 recorded the **new H-bridge relay installed** and restored central replacement-box scope. PR #23 defined F6 electrical ownership matrix, F7 requirements and functional architecture. **PR #24 merged at 0ecdeb1d** with injector-feed correction, unused idle removal, full future loads, and 4-relay/12–14-fuse expansion concept.
- 2002 Bowling & Grippo source map captured in `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md`. Source PDF schematic is V1.2 while one layout silkscreen reads V1.1; do not assume exact manufactured-board revision from filename.
- Original Volvo LH2.4 relay E/M, pink pump lead and factory voltage-drop investigations are **archived diagnostic work**, not the present design path. Owner explicitly closed that line of troubleshooting after installing a new H-bridge relay; do not reopen unless asked.

## Current formal gates

| Gate | Status | Needed to close |
|---|---|---|
| F1–F5 | Limited infrastructure passes and partial results per `docs/FOUNDATION_GATES.md` | Keep exact test boundaries; do not claim unrestricted MCP or production KiCad verification |
| **F6** | **OPEN** | Establish actual MS-box ECU, pump, injector JP2 mapping; ownership of coil, boost, wideband, fan; old terminal → new terminal migration and ground boundary |
| **F7** | **OPEN** | Measure/verify continuous and peak current, branch/source wire sizes, fuse coordination, relay contacts, startup/brownout/relay-failure behavior, EMI/transient and thermal limits, quantitative voltage-drop acceptance |
| **F8** | **OPEN** | Select physical architecture and review rated parts, fault paths, service envelope and migration interface before schematic authorization |
| KiCad hardware | **Not started** | No board schematic, PCB, manufacturing Gerbers, finalized fuse rating or copper sizing authorized |

**Known uncertainty:** X1 shared source is behind 30 A fuse and estimated ~4 mm² wire; it must **not** be assumed adequate for 12–14 future branches. The new H-bridge may share an upstream trunk; its as-built source remains unknown.

## Unresolved design choice and exact next step

**Current decision point:** Compare **A) a complete relay/fuse PCB carrying all intended engine power currents** against **B) a hybrid serviceable relay/fuse carrier with a dedicated rated busbar/terminal distribution for high-current paths**. Both remain viable. No final selection has been made.

**Next step for the continuation session:** Prepare a **side-by-side physical architecture trade study** using the current v0.2 load inventory and proposed R1–R4/F01–F14 footprint budget. Compare current path resistance and heat, connector and fuse/socket serviceability, wiring volume/strain relief, enclosure size, environmental protection, cost/replaceability, and practical Codespaces/KiCad manufacturability. Mark every rating requiring F6/F7 evidence as TBD. Recommend a **provisional** physical layout concept and identify what measurement or vehicle-space constraint would flip the recommendation. Do **not** produce schematic/PCB files or treat the provisional allocation as approved hardware until F6/F7 and F8 evidence is satisfied.

The next parallel evidence task after the concept comparison is targeted confirmation of **coil B+, pump output/relay, boost solenoid B+, LC-1 heater and fan positive feed ownership** from the actual aftermarket MS box. The already confirmed two injector-fuse pairs and unused idle functions must **not** be asked again.

## Authoritative reading order for new agent/chat

1. This `docs/HANDOFF.md` and `AGENTS.md`.
2. `.wolf/STATUS.md` **current top section**; lower entries are chronological/historical and may describe superseded hardware.
3. `docs/POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md` and `docs/POWER_DISTRIBUTION_EXPANSION_CAPACITY.md` (latest planning state).
4. `docs/F6_REPLACEMENT_CIRCUIT_MATRIX.md`, `docs/F7_ELECTRICAL_REQUIREMENTS_V0.md`, and `docs/REPLACEMENT_FUNCTIONAL_ARCHITECTURE_V0.md`.
5. `docs/FOUNDATION_GATES.md`, `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md` and any actual committed KiCad source files when they exist.

**Handoff integrity note:** This handoff summarizes an uploaded post-branch chat excerpt ending with PR #24 and the existing committed repository state. The excerpt is a final planning summary, **not raw meter data or a new independent source of part specifications**. All unmeasured currents, exact wire/fuse values, installed optional supply paths and board envelope remain explicitly unresolved.
