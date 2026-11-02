# F8 concept trade study — complete power PCB versus hybrid serviceable distribution

**2026-11-02 · Concept review v0.1 · Status: PROVISIONAL RECOMMENDATION ONLY. F6, F7 and F8 remain OPEN. No schematic, PCB, wiring change, fuse value, component rating or manufacturing release is authorized.**

## Scope and source of truth

**Superseding 2026-11-02 corrections:** See [installed-system relay scope update](AS_BUILT_CORRECTIONS_AND_RELAY_OPTIONS_2026_11_02.md). **Walbro 255 L/h already installed; old PWM Idle circuit reused for one Pierburg boost valve; only two gauges; no Pi; ESP32-P4 companion planned; two optional *external* higher-current relay positions.** Any outdated four-display/Pi/unused-PWM wording below is superseded. Provisional preference for hybrid must be reconsidered against narrower loads.

Compare two physical ways of replacing the aging **aftermarket** MegaSquirt/DIYAutoTune EFI relay/fuse box on the 1997 Volvo 940 Turbo (Mega144H7/EpicEFI). See [HANDOFF](HANDOFF.md), [F6 circuit matrix](F6_REPLACEMENT_CIRCUIT_MATRIX.md), [F7 requirements](F7_ELECTRICAL_REQUIREMENTS_V0.md), [v0.2 load inventory](POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md), and [expansion allocation](POWER_DISTRIBUTION_EXPANSION_CAPACITY.md). All load envelopes, connector/fuse/relay contact ratings, conductor sizes, quantitative voltage and heat limits, and mounting dimensions are **TBD**.

**Preserve confirmed state**: X1 is permanent B+ via an existing separately protected 30 A upstream branch; its conductor is visually estimated near 4 mm², NOT measured/accepted for future expansion. X2 is keyed positive; X3 engine ground. Four EV14 injector positives currently use **two fused pairs** via the MS box; **one** positive fuse for four injectors is the replacement *proposal*, with four independent sequential ECU low-side drivers preserved. No PWM idle valve or Fast Idle actuator; **one boost solenoid reuses the former PWM Idle circuit**, so the K3/JP1/CB3 physical role is UNVERIFIED until the as-built diagram is traced. Independently relayed DC idle H-bridge now works better and stays **external**, with its final as-built source and return still unknown. Present coil, dual boost valves, LC-1, fan positive ownership is unresolved. The **Walbro 255 L/h pump is installed**, but its exact model and operating/start/stall currents remain unmeasured.

## Candidate architecture definitions

**A — full current-carrying PCB**: automotive replaceable relay/fuse sockets connect through designed and rated PCB copper, plated-through interconnects, connector pins and appropriate attachments. Heavy motor feed is *not* automatically included; keeping fan and existing H-bridge external applies to both candidates. A still needs external upstream circuit protection and a rated wiring interface. Single-board integration does not eliminate contact/fuse/socket resistance.

**B — hybrid serviceable carrier**: replaceable automotive relay and blade-fuse sockets are retained in a protective enclosure, but principal B+ distribution and higher-current relay/fuse paths use **rated busbars, crimped terminals or equivalent insulated high-current conductors** independently of signal PCB copper. A small optional PCB may host only validated low-current relay control, suppression, diagnostics or connector organization. No MCU or software is required. Keep bus and socket contacts mechanically secured, strain-relieved, insulated and accessible. *Hybrid must not mean a loose set of unprotected jumpers or unfused studs.*

For a fair comparison, the same electrical ownership, safe relay state machine, fuse coordination, physical environment and source capacity apply to A and B.

## Side-by-side engineering trade

| Criterion | A: full power PCB | B: hybrid rated bus / socket carrier | Decision evidence / constraint |
|---|---|---|---|
| Total power-path resistance | Potentially excellent with appropriately specified copper, parallel conductors, short paths and contacts; board copper and vias add modeled resistance | Potentially excellent with short, suitably sized bus/conductors; each bolted/crimp interface adds resistance and aging risk | **TBD** cold and hot full path mΩ, including fuse clips, relay, connectors, *positive and return*. No unconditional winner |
| I²R heating and hotspots | Distributed copper loss, via bottlenecks, contact heating and enclosure thermal coupling; needs worst-simultaneous-load modeling | Higher-current heat can be carried away from low-current PCB; bus, joint and fuse clip still heat | **TBD** sustained/peak current, mounting temperature, allowable temperature rise, test duration |
| Relay and fuse replacement | Easy if rated PCB-mounted sockets have top clearance and survive insertion/extraction loads; solder pads/traces become repair risk on a damaged socket | Easy if standardized socket carrier is accessible; individually replaceable crimp/socket parts can avoid replacing whole PCB | Service clearance, push/pull forces, replacement method and available market parts **TBD** |
| Wire entry and strain | Potentially few connectors, but big multi-pin power connector can become thermal/current bottleneck; PCB must not carry harness strain | Often more terminations and larger volume; can isolate harness forces through terminal support and cable clamps | Confirm actual old-box wires, connector cavity count, gauges, bends, mechanical restraint |
| Enclosure footprint | Usually best planar packaging; may require extra PCB area/layers for copper, slot spacing and heat | May be deeper/larger from busbars, studs, service space and cover; may distribute into submodules | Car location, L×W×H, mounting direction, lid opening and loom approach **TBD** |
| Moisture/vibration/corrosion | Coating/sealing can help electronics; fuse clips, relay contacts, power connectors still require environmental design | More potentially exposed junctions; mechanical supports, plating/insulation, sealed housing needed | Installation environment, ingress requirements, thermal cycling and vibration **TBD** |
| EMI / common-impedance coupling | Controlled current loops are feasible, but common PCB copper can couple coil/pump/heater noise into ECU power or ground | Easier to physically segregate heavy and clean supply/returns; careless wiring can create longer loops and worse EMI | Draw actual return tree and test ECU voltage/sensor reference during pulsed loads |
| Cost and replaceability | Higher engineering/NRE and potentially PCB fabrication/assembly cost; compact repeat production may be economical | Standard components and mechanical assembly may cost more labor/volume, but power-path repairs often remain modular | Parts list, minimum order, labor, maintainability, spares and enclosure cost **TBD** |
| Codespaces/KiCad | Full schematic/PCB/DRC and detailed stackup calculations required; KiCad 9.0.2 observed, arbitrary MCP editing NOT verified | KiCad still valuable for low-current PCB and electrical drawing; mechanical bus/terminal drawing and manual electrical checks are essential | Neither KiCad DRC nor electrical ERC proves automotive high-current safety |
| Installed Walbro 255 L/h pump | Possible if actual current motor/contact/load/fuse/wire/copper path passes F7 | Easier to externalize a heavier rated pump power stage *if required* while retaining PD10 control | Exact installed Walbro model, pressure-dependent run current, inrush/stall, supply source and safe shutdown **TBD** |
| Future electronics | PCB offers labeled preplanned fuse banks, but enlarging board does not expand a source feed's rating | Modular sensor-IOX 12 V feeder and cabin subdistribution can be added without loading engine PCB copper | Future source capacity, voltage regulation and load coincidence **TBD** |

**Interpretation**: With no measured currents or enclosure dimensions, neither design can be claimed objectively lower resistance, cheaper, cooler or safer. A is competitive for a bounded modest-current engine-core module; B decouples high-current sizing and servicing from a custom PCB more flexibly, at the cost of mechanical design and additional contact interfaces.

## Quantitative decision method to complete in F7

Compare **all** simultaneously active paths, not nominal fuse ratings alone:

1. For each branch, capture steady, worst sustained and transient current **with duration**, voltage and environmental state; include ECU, injectors, ignition, pump, boost, LC-1 and future powered auxiliaries *only where F6 assigns them*. Capture source coincidence (CRANK, pump start, coil charge, injector pulses, fan start on any **shared upstream trunk**, Pi/display wake).
2. For each candidate, construct a segment ledger: battery/source protection → feed wire → inlet terminal → distribution element → branch fuse clips → relay contacts (actual fuse/relay order **TBD**) → output terminals → harness → load → power return. Compute and later measure `ΔV = Σ(Isegment × Rsegment)` and `Psegment = Isegment² × Rsegment`. PCB copper starting estimate: `R = ρL/(width × copper thickness)`; real current sharing/via plating, temperature and joints need separate validation. Busbar has the same physical-resistance and joint-heat obligations.
3. Derive an acceptable loss at **ECU connector during CRANK and worst RUN**, with the ECU's true input minimum and battery voltage; reserve budgets for existing external harness and source, NOT just the replacement box. Record contact and bus/copper temperature rises at hot ambient after thermal equilibration.
4. Fuse coordination must protect the **smallest downstream conductor** and be coordinated with the upstream source wire/fuse and fault current; evaluate each fault branch, spare, jumper and terminal. Do not reuse old F1/F2/F3/F4 printed values as approved ratings.
5. Check part datasheets for relay coil/contacts, fuse holder, bus/terminal and connectors under correct ambient/inrush/vibration. Confirm release speed of the PD10 pump relay with proposed coil suppression. Review welded pump-relay contact, stuck/absent PD10 control, backfeed and simultaneous open-fuse failures.
6. Only after calculations: bench a worst-case representative hot-loaded path and compare segment mV at simultaneous current. Neither candidate passes on CAD alone.

### Flip conditions (no invented current thresholds)

**Favor A** if F6 proves a genuinely bounded core power path; F7 confirms worst-case copper/contact thermal and voltage budgets **with margin**, verified automotive socket and connector parts survive service cycles, and a compact single box fits the measured location and loom without stress.

**Favor B** if F7 shows higher pump/actuator or coincident demand making PCB copper/via/connectors disproportionate, hot fuse/socket junctions would be too close to ECU circuitry, harness wire sizes and cable bends strain a PCB, service replacements should not require desoldering, or expansion needs independent source-protected buses. The hybrid must separately pass its joint corrosion, loose-terminal, hot-spot and enclosure tests.

**Revisit the footprint budget now:** the former four-screen/Pi plan has been cancelled. Actual scope is two gauges and an ESP32-P4 companion; do not presume 12–14 fuses are needed. Retain only justified Micro ISO functions, with optional two high-current/Maxi ISO cavities **outside the critical engine box** if future electromechanical conversions occur.

## Provisional physical arrangement — B preferred for concept development, not selected for manufacture

**Preferred investigation order**: compare a **hybrid modular engine-core enclosure** with an equally documented compact PCB-only reference. This is a *working ranking* driven by modular serviceability and uncertain future load current, **not an F8 architecture sign-off**.

- **Input/protection zone** at one mechanically supported enclosure end: rated source entry and branch distribution, source protection coordinated at origin; no assumption the **existing 30 A / estimated 4 mm² X1** can support planned cabin, IOX or uprated motor feeders. Additional source-protected trunks must be considered at their origins rather than simply raising that fuse.
- **Relay zone** next to distribution: four *physical planning spaces* R1 main and R2 pump initially populated; R3 auxiliary optional; R4 reserved, normally **unwired/unpowered**. Keep R2 coil driver behavior and fuel-pump power path separately reviewed. Provide service access from removable cover, not from behind fixed harness bundles.
- **Fuse zone**: determine required physical fuse count from revised two-gauge/P4 scope; the former **two banks of six** is only a historical packaging option, with F13/F14 extra space conditional; physical arrangement, fuse-before/after-switch order and cavity energization are not assigned electrical nets. Labels must distinguish populated, optional and unfused spare positions.
- **Engine-core grouping** near R1/R2: F01 ECU, F02 proposed single 4-injector B+, F04 pump, and conditional F03 ignition / F05 boost / F06 LC-1 **only after ownership review**. Protect ECU from relay/pump/heater common-return paths. Never combine four independent injector driver signals.
- **Expansion interface**: F07 IOX/EGT electronics → local regulated supplies; F08 two-gauge/CAN feeder; F09 **ESP32-P4 companion supply only if a separate protected group is justified**; F10+ contingent/unused. **No Pi or additional displays**. A 5 V/3.3 V sensor is not a separate automotive fuse position; CAN wires carry signals, not node power.
- **External heavy zone**, outside the engine ECU PCB power copper and preferably outside this enclosure: existing independently relayed H-bridge and fan; **up to two OPTIONAL external Maxi ISO/high-current relay positions** for possible electromechanical conversions; the **already installed Walbro 255** heavy power stage external only if real F7 measurements justify it. This zone may share an upstream vehicle source only after the **total source and return** are verified. Fuel-pump control must still obey PD10 and stall/reset fail-safe.
- **Low-current interface**: optional small PCB for relay-coil interface and validated suppression only; avoid routing pump/ignition power or motor grounds through the logic board. ECU sensor ground stays at ECU/reference; no chassis/engine motor return through sensor reference. Do not assume X3 maps to a new shared ground bus without F6.
- **Enclosure and wire exit**: distinct power and signal entries, strain relief, optional keyed/sealed harness connectors, protected terminals, fuse extraction clearance, a serviceable lid and mounting for vibration/heat/moisture. Exact envelope and mounting position **TBD**.

### Functional position ledger (v0.3 corrected scope, NOT a netlist)

| Position(s) | Provisional function | Ownership/control condition |
|---|---|---|
| R1 / R2 | Main ECU-run / ECU-PD10-commanded pump | Baseline relays, RUN+CRANK and fail-safe characterization pending |
| R3 / R4 | Auxiliary optional / spare | Not energized or preassigned without review |
| F01 / F02 / F04 | ECU / four-injector common positive proposal / pump | Core protection; old injector arrangement remains two separate fuses until migrated |
| F03 / F05 / F06 | Coil / dual boost / LC-1 | Conditionally consolidated depending actual present supply ownership |
| F07 / F08 / F09 | IOX+EGT / two-gauge cabin CAN feeder / ESP32-P4 companion if separately protected | Smaller future feeds subject to regulator/load evidence; not a Pi, never silently added to existing X1 |
| F10–F12 / F13–F14 | Control/aux reserves / optional space | Unused cavities non-live, physical positions only |

## Hazard / maintenance differences that F8 must review

| Failure case | A-specific concern | B-specific concern | Shared mandatory behavior |
|---|---|---|---|
| High-resistance fuse/relay socket | Hot joint can damage PCB copper/pads | Hot socket/joint can damage carrier/nearby wiring | Rated contacts, accessible inspection, replacement and thermal test |
| Harness pulled during maintenance | PCB solder pads and connectors are vulnerable | Lug/crimp loosening and unsupported bus stresses | Independent clamp and strain relief |
| Loose/corroded power connection | Board inlet heat and intermittent supply | Additional screwed/bolted interfaces may oxidize or loosen | Mechanical locking, correct crimp/torque process and hot-load testing |
| Short on optional expansion | Spare copper tracks could be energized if incorrectly bused | Spare studs/jumpers may be accidentally live | No live unfused spare, source/branch fusing and label control |
| ECU reset / PD10 inactive | Pump relay wiring/backfeed still safety critical | Same | Pump cannot remain on due solely to lost ECU command beyond allowed prime; review welded contacts explicitly |
| Source shared with H-bridge/fan | Heavy external loads may still cause source droop | Same | Prove upstream cable/fuse/return capacity; separation *at the box* alone does not cure common upstream loss |

## Evidence matrix and next non-invasive task

| Gate / item | Current evidence | Required before closure |
|---|---|---|
| **F6** | X1/X2/X3 functions, two fused injector pairs, obsolete idle, new external H-bridge **user-reported** | Trace actual ECU output protection/terminal, pump feed/PD10 coil interface and JP2 pair destinations; **target remaining coil B+, dual boost B+, LC-1 heater B+ and fan B+ ownership**; define branch count, connector/ground and old→new migration |
| **F7** | Requirements and load classes documented; **no measured ratings** | Electrical currents/peaks and coincidence; X1 source and branch wire cross sections; voltages under hot/crank load; relay/fuse/connector/bus/copper ratings; source and fault protection; thermal and pump failure testing |
| **F8** | This trade study only; B is **tentative preferred investigation** | Compare rated candidate hardware, measured space and migration layout; user approval of architecture; independent review; then authorization for first schematic |
| **Infrastructure** | KiCad 9.0.2 observed in Codespaces; restricted one-tool MCP read-only fixture passed | Real design editing and ERC/DRC not validated; no fabrication outputs |

**Immediate next evidence:** reconcile the owner's forthcoming revised EpicEFI **wiring diagram** for ECU, installed Walbro 255, coil, both boost valves including former PWM Idle path, LC-1 and fan actual supply/return source and terminal, plus physical mounting envelope. Do not repeat already answered pump-upgrade or injector questions. Collect source and return paths before any relay/socket/fuse rating or relocation decision. Physical envelope and access under bonnet are the next packaging facts. Retain dated as-built evidence labels; do not infer from the 2002 B&G reference PCB.

**Review conclusion:** After removal of old four-gauge/Pi expansion assumptions and confirmation of installed Walbro/boost-PWM reuse, **re-evaluate A (compact PCB) versus B (hybrid) on revised loads and actual enclosure data**; B remains a working concept but not an F8 choice. Previously: B was the provisional concept to develop further because it can keep engine-critical current paths and service parts modular while isolating expansions and externally rated heavy loads; **A remains a valid alternative** if actual load and packaging evidence make it better. **F6 OPEN · F7 OPEN · F8 OPEN.**
