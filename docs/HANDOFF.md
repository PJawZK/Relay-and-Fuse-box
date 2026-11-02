# HANDOFF — Volvo 940 EFI relay/fuse-box replacement

**Updated:** 2026-11-02  
**Repository:** `PJawZK/Relay-and-Fuse-box`  
**Verified starting baseline:** `main` at `f7729f0218f13821da67620a9bf4adcc5b6b2171` (post-PR #24 handoff commit). PR #24 design baseline: `0ecdeb1d53427caf14821544c135507135097dc7`. This trade study is proposed on a separate branch, not yet merged.  
**Phase:** F6/F7 planning; initial PCB-versus-hybrid concept trade study drafted for review; **no vehicle-ready schematic or PCB**.

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
| Idle / reused PWM channel | **No PWM idle valve or Fast Idle actuator**; one of two installed Pierburg boost solenoids **reuses the former PWM Idle circuit** | Preserve active boost control/wiring. Determine whether old board K3/JP1/CB3 or only ECU channel/harness is used; do not omit as physically unused without F6 proof |
| DC idle H-bridge | Owner **installed a new independent relay and wiring**, reports operation is better | Keep external to new ECU box; actual new source branch/fuses/ground landing not confirmed, and the improvement does not prove root cause of all previous shutdowns |
| Fuel pump | **Walbro 255 L/h ALREADY INSTALLED**, supplied by aftermarket relay system; ECU **PD10** commands pump relay | Actual Walbro part/model and operating/start/stall current TBD. Preserve prime/run/stop fail-safe; exact driver polarity/coil suppression and supply map to verify |
| Ignition | VAG 032 905 106B wasted-spark coil installed | Its present positive supply ownership and duty/peak current unknown |
| Boost | **Two Pierburg solenoids installed; one reuses the former PWM Idle circuit** | Determine actual reused ECU driver/terminal, +12 V source, suppression and fault grouping; no idle-valve functional load |
| Wideband | Innovate LC-1 installed | Controller/heater supply and ground return ownership unknown |
| Fan | Radiator fan installed | Existing relay/feed and high motor start current unknown; external high-current branch preferred by default |
| Sensors | Current MAP/IAT/CLT/TPS/crank/cam/VSS/fuel-pressure wiring exists | Provide proper ECU reference or local IOX regulation, not one separate automotive relay/fuse per sensor |

**The existing injector two-fuse arrangement is an as-built fact; converting to one shared fuse is a PROPOSAL, not an already-made change.**

## Decisions already established — preserve without reopening

1. **Injector positive feed:** Favor **ONE** appropriately rated fused +12 V injector branch feeding all four EV14s; preserve four independent ECU ground-side controls. This decision awaits conductor/fault/peak-load analysis and is not permission to select a fuse ampere rating.
2. **Idle function absent, legacy circuit reused:** No Fast Idle or PWM idle **actuator**, but one boost solenoid reuses former PWM Idle circuitry/wiring. Preserve the mapped boost path; K3/JP1/CB3 physical involvement remains F6-unknown. Independently relayed DC idle H-bridge remains external.
3. **Core engine functions:** Main ECU relay and ECU fuse, separate ECU PD10-controlled pump relay/fuse, injector positive fuse, ignition coil fuse if integrated, protected boost solenoid branch if integrated, LC-1 heater/controller branch if integrated. Fan and H-bridge high-current feeds may stay external.
4. **Physical expandability:** Study **compact Micro ISO automotive relays** for R1 main/R2 pump (R3 auxiliary optional/R4 spare), then **recount fuses** for reduced two-gauge/P4 load. Old **12–14 blade-fuse** count is an unapproved historical packaging allowance, not a new requirement. Separately consider **two optional external Maxi ISO/high-current relay cavities** for possible future motor conversions, not part of R1–R4. No spare cavity unintentionally live.
5. **Fuse-allocation concept:** F01 ECU; F02 proposed four-injector positive branch; F03 ignition conditional; F04 **installed Walbro 255**; F05 both boost valves (one legacy PWM circuit reuse to be mapped); F06 wideband conditional; F07 IOX/EGT; F08 feeder for **only two** digital gauges/CAN; F09 **secondary ESP32-P4** if distinct regulated feed justified; F10+ discretionary. No planned Pi/CarPi or extra digital displays; positions/rating remain unapproved.
6. **Three principal distribution zones:** (E) engine-critical ECU/injectors/ignition/**installed Walbro pump**; (A) regulated sensor, IOX and noncritical ESP32-P4 secondary controller; (C) only **two digital gauges** and required CAN accessories. Heavy motor feeds (existing H-bridge/fan, future optional conversions) use independently rated external distribution when justified; no Pi load.
7. **Avoid legacy complexity, preserve reused wiring:** Do not clone K3 solely for idle or CB2 PTC based on the 2002 drawing, but **do not remove the legacy PWM Idle circuit before tracing its reuse by a boost valve**. Historical JP1/JP2 mapping is not the current physical netlist. Old box stock by user report, exact fitted parts/Thermal paths unknown.
8. **Design goals:** Standard field-replaceable relays/fuses, good access and wire termination, low path resistance, appropriate source/branch fusing, distinct ECU sensor-ground and motor returns, suitable automotive transient/relay-coil protection, fail-safe pump shutdown and RUN/CRANK behavior.

## Planned upgrades and future feed implications

- **Fuel:** **Walbro 255 L/h ALREADY INSTALLED**. Its exact part/model and inrush/stall/pressure-dependent operating current remain unknown and must be measured. Its existing PD10 pump path may need an external rated stage, to be decided from F7. Custom rail/FPR mechanical; pressure transducer separately regulated.
- **Engine instrumentation:** Reuse existing 200-PSI sensor for EMAP after fuel-rail conversion; four K-type EGT channels with MAX31856 converters and IOX controller; oil/fuel pressure and temperature; optional flex-fuel sensor. Sensors typically use ECU/IOX low-current reference or local regulated power. IOX and converter electronics get protected 12 V upstream with local 5 V/3.3 V rails.
- **User/chassis inputs:** Clutch/accelerator pedal sensors, possible brake position/switch, reverse/handbrake, front ABS VR/wheel speeds and additional wheel-speed channels. These mostly need protected signal conditioning and input capacity, not power relays.
- **Cockpit:** **Two digital gauges total**: clock location first, later tachometer/RPM replacement. Head unit retained; **no additional ESP32 display conversions**. Exact selected gauge/display boards TBD; protect a small cabin/CAN feeder with local regulation rather than reserving four screens.
- **Secondary processing:** **ESP32-P4 companion controller** for EpicEFI connectivity, workload offloading and additional functions. Properly protected/regulator-fed, isolated as a noncritical companion; **NO Raspberry Pi, CarPi or extra screen** in vehicle scope. Critical ECU/pump power must work without P4.
- **No load-current extrapolation:** Component reference values (EV14, EGT and ESP32 devices) are not complete-branch measurements or approved fuse values. Legacy Pi 5 V/3 A budgeting is **no longer relevant**.

Primary evidence: `docs/AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md` and v0.3 `docs/POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md` / `docs/POWER_DISTRIBUTION_EXPANSION_CAPACITY.md`.

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

**Known uncertainty:** X1 source has 30 A upstream fuse and ~4 mm² cable estimate; **not approved** for future branches or optional high-current conversions. H-bridge source as-built remains unknown. Physical fuse cavity count must be re-evaluated after narrowed two-gauge/P4 plan.

## 2026-11-02 continuation — physical concept study (provisional)

**Newer authoritative user correction:** [current installed-system and relay-option corrections](AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md) supersede this handoff's older four-screen/Pi/future-pump/unused-PWM assumptions. The updated EpicEFI as-built wiring diagram is forthcoming and is the next F6 evidence source.

[PCB versus hybrid architecture trade study](PCB_VS_HYBRID_ARCHITECTURE_TRADE_STUDY.md) compares resistance/thermal paths, replaceable sockets, harness strain, packaging, ingress/EMI, build tooling, fault behavior and expansion. **Provisional preference: modular hybrid** with a mechanically rated power-distribution path and separate low-current control PCB if needed, plus the existing independently powered H-bridge and external fan. **This is a concept ranking only; full PCB remains a viable alternative, and F6/F7/F8 are still OPEN.**

The remaining next work is to establish positive-feed ownership for ECU and aftermarket pump paths, VAG coil, dual boost solenoids, LC-1 heater and radiator fan; map injector two-pair terminals (without questioning the already confirmed two-fuse arrangement), and measure the mounting envelope/source/loads. Use the [trade-study flip conditions](PCB_VS_HYBRID_ARCHITECTURE_TRADE_STUDY.md#flip-conditions-no-invented-current-thresholds) to decide A versus B only when that evidence exists. No schematic or production ratings are authorized.

## Unresolved design choice and exact next step

**Decision point after first concept pass:** Evaluate **A) complete power PCB** against **B) hybrid rated distribution** using the new trade study; B is provisionally preferred, A remains viable and no F8 architecture choice is signed off.

**Next step for the continuation session:** Resolve targeted **F6 supply ownership** and **F7 source/load/space measurements** identified by the trade study; use real part ratings, measured currents, wiring and enclosure constraints to confirm or reject the provisional hybrid preference. **Do not** produce schematic/PCB files or treat the provisional fuse allocation as approved hardware until F6/F7 and F8 evidence is satisfied.

The next parallel evidence task after the concept comparison is targeted confirmation of **coil B+, pump output/relay, boost solenoid B+, LC-1 heater and fan positive feed ownership** from the actual aftermarket MS box. The already confirmed two injector-fuse pairs, absence of PWM **idle valve** and **presence of reused boost-PWM wiring** must **not** be asked again; only its actual routing remains open.

## Authoritative reading order for new agent/chat

1. This `docs/HANDOFF.md` and `AGENTS.md`.
2. `.wolf/STATUS.md` **current top section**; lower entries are chronological/historical and may describe superseded hardware.
3. `docs/AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md`, `docs/POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md`, `docs/POWER_DISTRIBUTION_EXPANSION_CAPACITY.md` and `docs/PCB_VS_HYBRID_ARCHITECTURE_TRADE_STUDY.md` (newer user corrections override older capacity assumptions).
4. `docs/F6_REPLACEMENT_CIRCUIT_MATRIX.md`, `docs/F7_ELECTRICAL_REQUIREMENTS_V0.md`, and `docs/REPLACEMENT_FUNCTIONAL_ARCHITECTURE_V0.md`.
5. `docs/FOUNDATION_GATES.md`, `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md` and any actual committed KiCad source files when they exist.

**Handoff integrity note:** This handoff summarizes an uploaded post-branch chat excerpt ending with PR #24 and the existing committed repository state. The excerpt is a final planning summary, **not raw meter data or a new independent source of part specifications**. All unmeasured currents, exact wire/fuse values, installed optional supply paths and board envelope remain explicitly unresolved.
