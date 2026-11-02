# Replacement relay/fuse-box functional architecture — v0.2

_2026-11-02 · REVIEW CONCEPT ONLY: **not a KiCad schematic, production wiring drawing or approved netlist**_

## Architectural question

What is the smallest reliable, serviceable set of relay and fuse functions required to replace **only the currently used** portion of the aftermarket MegaSquirt power board? The 2002 B&G PCB had main ECU power, pump, injectors, fast idle, signal pass-through, and PTC protection; the 2026 Mega144H7/EpicEFI car has different electronics and an independently powered DC idle H-bridge.

**Working proposal (corrected 2026-11-02):** R1 engine main and R2 **installed Walbro 255 L/h** pump control (PD10); separate ECU/pump and proposed single four-EV14 positive fuse, keeping four sequential low-side drivers. No PWM **idle valve** or Fast Idle actuator, but one of the **two Pierburg boost valves reuses the former PWM Idle circuit**, so preserve its used output/terminal/path until F6 maps whether K3/JP1/CB3 is physically involved. Coil, wideband, fan source still unverified. Study compact Micro ISO relay sockets; two possible high-current/Maxi ISO motor relay sites separately external. Exactly two gauges, no Pi, ESP32-P4 secondary planned. F6/F7/F8 OPEN.

## Functional boundaries (no electrical pin numbers implied)

```mermaid
flowchart TD
    BAT[Battery / charging +] --> UP[Source protection and cable]
    UP --> DIST[New rated distribution input]
    IGN[Ignition-switched X2-equivalent] --> CTRL[Keyed relay-coil control]
    DIST --> ECUF[ECU fuse domain]
    CTRL --> K1[Main ECU relay K1-equivalent]
    ECUF --> K1
    K1 --> ECUB[ECU Mega144H7 B+]

    DIST --> PF[Pump fuse domain]
    PF --> K2[Fuel-pump relay K2-equivalent]
    PD10[ECU PD10 command, verified driver interface] -.-> K2
    K2 --> PUMP[Installed Walbro 255 L/h fuel pump]

    DIST --> IF1[One injector B+ fuse]
    IF1 --> INJ[Four EV14 injector positive connectors]
    ECUB -.-> DRV[Current sequential injector & ignition drivers, stay in ECU]

    DIST -. F6 ownership only .-> OPT[Optional coil / TWO boost valves (one old PWM channel reuse) / LC-1 / fan external]
    DIST -. existing source branch status unknown .-> HBE[Newly separately wired H-bridge relay: external]
    GRD[Rated battery/engine return network] --> RET[Power returns; sensor return stays ECU-side]
    ECUB --> RET
    PUMP --> RET
    HBE --> RET
```

This chart is **topological only**. The *actual* safe choice of whether ECU/fuel-pump/injector feeds branch from battery-unswitched or main-relay-switched nodes, the location of fuses relative to relays, and whether they share the battery X1 trunk are **unresolved**. The chart deliberately avoids implying that PD10 itself can directly sink any arbitrarily selected relay-coil current.

## Two candidate physical implementations (no decision to manufacture)

| Concept | Benefit | Main risk / tradeoff | When it becomes suitable |
|---|---|---|---|
| **A: relay/fuse PCB as complete power carrier** | Compact, all fuse/relay sockets and labels integrated | Board copper, connectors, thermal margins and contact resistance must safely carry all real currents | Only after F7 load/thermal data establish valid PCB copper layers and high-current paths |
| **B: hybrid relay/fuse carrier with heavy-current external distribution** | Fuse/relay sockets can be serviceable while heavy current uses appropriate terminals/busbar, PCB restricted to control and any suitably rated distribution | More wiring/mechanical parts and potential contact points | Useful if measured pump/coil/fan currents or enclosure thermal conditions make PCB copper too demanding |

**Recommendation for design review:** Keep both options open through F7; prioritize low loss and serviceability over achieving a single-board aesthetic. Reusing old PCB high-current traces or CB2-type PTC devices without analysis would recreate historical failure risks. Avoid an MCU, CAN dependency or custom software for essential supply switching.

## Confirmed controls vs assumptions

| Interface | Confirmed current description | What must NOT be inferred |
|---|---|---|
| Existing X1 | Constant B+ behind upstream separate 30 A protection; estimated ~4 mm² cable | Available current headroom, fuse adequacy or max combined load |
| Existing X2 | Ignition-switched +12 V | Behavior during CRANK and coil-driver fuse logic |
| Existing X3 | Engine-ground reference | That all ECU/sensor/motor returns should use shared PCB copper |
| ECU PD10 | Current ECU fuel-pump relay output | Polarity, maximum coil current, flyback components, safe boot state |
| Existing B&G K1/CB2 | Historic K1 → CB2 → `12 RAW`; actual fitted parts/path unknown | Never infer whether old K3/CB3 PWM terminal has been repurposed for boost without mapping |
| EV14 injectors | Four sequential injector low-side outputs | Historical 2-channel JP1 can be copied or grounded together |
| DC idle H-bridge | New wiring/relay installed and reported to improve operation | Exact source, relay contact/fuse and ground location; no reason to rewire or merge it |
| Factory Volvo LH | Current EpicEFI does not use OEM LH fuel relay/fuse harness | That old Volvo relay sockets belong in new box |

## Proposed naming policy for design discussion

Reference names describe **functions only**, not approved schematics or physical wire connections.

| Proposed logical name | Function |
|---|---|
| `VBAT_PROTECTED_IN` | Protected battery-fed input to replacement module |
| `IGN_RUN_START_SENSE` | Ignition logic/control reference |
| `ECU_PWR_SW` | Relay-switched ECU positive output |
| `ECU_PWR_RET` | ECU power return boundary, **not sensor ground** |
| `PUMP_PWR_SW` | ECU-authorized pump-positive output |
| `PUMP_RELAY_CMD` | ECU relay command interface from PD10 via validated driver/suppression |
| `INJ_BAT_ALL` | **One** proposed protected positive feed to all four EV14 injectors, independent low-side drivers remain unchanged |
| `ACTUATOR_BAT_OPT` | Optional protected power output(s), count TBD |
| `CHASSIS_ENGINE_PWR_RET` | Defined high-current return network reference outside sensor returns |
| `SENSOR_GND_EXCLUDED` | No high-current load allowed |

## Required reviews before schematic work

1. Freeze included **load ownership** based on `docs/F6_REPLACEMENT_CIRCUIT_MATRIX.md`; EV14 positive already confirmed as two paired fuses and **no PWM idle actuator**, while one boost valve actively reuses the former PWM Idle circuit; verify K3/JP1/CB3 before circuit removal. Evaluate one common EV14 positive fuse, ECU/pump fuse functions, ignition coil and boost/wideband owners.
2. Determine actual ECU/ignition/pump driver behavior in **OFF/RUN/CRANK/STALL/ECU_RESET**, including the exact allowable prime behavior and how the relay drops out if PD10 is lost.
3. Evaluate whether main-relay source feeds injectors and pump and whether fused individual branches must be **before or after** contact, accounting for source fault, contact welding and source voltage drop. No unreviewed direct battery bypass of pump failsafe.
4. Assign branch current, relay making/continuous/breaking ratings, fuse curves, connector and wire sizes, and maximum allowed voltage/thermal drops from `docs/F7_ELECTRICAL_REQUIREMENTS_V0.md`.
5. Choose concept A or B after F7 load analysis; design for realistic enclosure, moisture, vibration and replaceable parts.
6. Map **every old physically connected wire** to a replacement connector, preserve appropriate ECU signal references, and plan a reversible migration/bench harness where possible.
7. Only after design review (F8) create KiCad schematic with explicit source/net traces and automated ERC/DRC, followed by independent review and bench fault testing. Current KiCad 9 capabilities are supported; KiCad 10 and design editing tool claims require later verification.

**Decision status:** Functional architecture v0.3 corrected scope established, **not frozen**. F6/F7/F8 remain OPEN, no board layout, component value or manufacturing release approved.


## Expansion architecture v0.3

See [latest installed-system corrections](AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md), `docs/POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md` and `docs/POWER_DISTRIBUTION_EXPANSION_CAPACITY.md`. Former 12–14 fuse study was based on four gauges/Pi and must be **recounted** for two gauges/P4, installed Walbro 255 and two optional external high-current relay sites. Two Micro ISO core relays remain working functions; other sockets are unapproved mechanical options.
