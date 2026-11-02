# Authoritative installed-system corrections and compact relay shortlist — 2026-11-02

**Source:** direct user confirmations in active project conversation, superseding older 2026-11-02 handoff assumptions. **Evidence grade:** R (owner-reported as-built) for installation/function; P (future plan) for remaining hardware. No harness tracing or measured current supplied by these corrections. **F6 OPEN · F7 OPEN · F8 OPEN.**

## What changed (supersedes old proposals)

| Topic | Authoritative status | Engineering consequence |
|---|---|---|
| Fuel pump | **Walbro 255 L/h pump ALREADY INSTALLED** for some time | Remove old ~110 L/h “current” and 255 L/h “future upgrade” claims. Actual Walbro model/GSS variant, operating current versus pressure and inrush/stall remain unknown. The PD10-controlled relay and fail-safe must cover the installed 255 pump now |
| Legacy PWM Idle circuit | **One of the TWO installed Pierburg boost solenoids reuses the former PWM Idle circuit** | No PWM idle **valve** or Fast Idle actuator is used. **Do not declare the old circuit/wiring unused.** Determine whether reuse means ECU PWM channel, old harness conductor, old box JP1/FASTIDLE/K3/CB3 supply path, or some combination; preserve the actual boost control path until mapped. Do not assume K3 itself is needed or can be omitted before trace |
| Display plan | **Exactly TWO digital gauges**: first clock location; later tachometer/RPM gauge location | The older four-gauge/other additional-display plan is cancelled. No head-unit replacement or extra ESP32 displays. Identify actual two selected displays and consumption when available |
| Raspberry Pi | **No Pi 4, Pi Zero, CarPi/HAT/NVMe in vehicle plan** | Remove their feeder, ignition hold-up and 5 V/3 A assumptions from the active design; historic bench experiments are not future vehicle loads |
| Secondary control | **ESP32-P4 companion/secondary controller for EpicEFI**: connections, workload offloading and added functions | Protected regulated power and suitable physical signal/network interface TBD; primary ECU/pump power must remain operable without this secondary controller |
| Relay families | Explore current **Micro ISO / Micro 280 plug-in automotive relays**; optionally reserve **TWO external high-current/Maxi ISO relays** for potential future electromechanical conversions | Do not automatically include high-current relay sockets or their motor currents in engine ECU distribution box or existing X1 30 A feeder. “MAXI” relay is not the same object as an automotive MAXI blade fuse |
| Wiring proof | User will update the actual current EpicEFI wiring diagram | **Next F6 source of truth** when supplied. Check feeds, grounds, JP1/JP2/legacy PWM harness, relay coils/fuses and branch ownership against actual installation |

**Unchanged:** Four EV14 injector positives currently use TWO old MS-box fuses (one per pair); ONE common replacement injector B+ fuse is a proposal only; four sequential low-side ECU drivers remain isolated. DC idle H-bridge has its own recently installed relay/wiring and stays outside new box. Factory Volvo LH distribution remains out of scope. X1 has reported separately fused 30 A battery feed, estimated cable ~4 mm²; no claim of expansion capacity.

## Revised power domains and physical budget

- Engine-critical: R1 ECU main, R2 PD10 fuel pump, F01 ECU, F02 proposed single injector B+, F04 installed Walbro 255 positive; F03 ignition if ownership confirmed; boost F05 **must preserve the reused former PWM circuit** while F6 verifies true positive and driver path; LC-1 F06 conditional.
- Engine auxiliary: IOX/EGT, sensors and **ESP32-P4 companion** as protected 12 V to regulated low-voltage electronics supply, according to actual future board voltage requirements. P4 must not be a series element controlling primary ECU/fuel pump safety.
- Cabin: **two displays total**, with an appropriately protected cabin feeder and local regulation, not four screens, no Pi and no replacement head unit.
- External heavy: existing DC H-bridge and radiator fan remain independently protected; two **possible** larger Maxi ISO/high-current relay positions for future electrical conversions should be studied as **separate external mounting space / distribution**, not yet installed or electrically assigned. Consider separate protected feeders and motor returns and transient suppression; physical relay separation alone does not solve common-impedance EMI.

**Count correction:** Earlier four regular relay cavities / 12–14 fuse cavities was a packaging thought experiment, not an approved required count. Retain **two required Micro ISO-class functions** (R1 and R2) and study R3 auxiliary/R4 spare. Re-estimate actual fuse count after the updated harness and narrowed future loads. Separate pair of optional high-current relay positions is **not** part of those four standard cavities. Spare cavities remain disconnected/nonlive.

Provisional updated allocation (only function labels, no validated nets or ratings):

| Position | Proposed function |
|---|---|
| R1 / R2 | Main ECU / pump command |
| R3 / R4 | Optional auxiliary / spare |
| F01–F04 | ECU / four injector B+ proposed / ignition conditional / installed Walbro 255 |
| F05–F06 | Dual boost positive supplies conditional (one legacy PWM channel reuse) / LC-1 conditional |
| F07 | IOX/EGT auxiliary regulation |
| F08 | Two-gauge cabin feeder (not four) |
| F09 | P4 companion low-current/controller supply *if independent group justified* (not Pi) |
| F10–F14 | Contingent; not automatic live/built/needed |
| External high current | H-bridge and fan as installed; optional 2 future bigger relay cavities after load/alternator/battery review |

## Manufacturer relay shortlist for F7 review (examples, NOT selected parts)

1. **Omron G8HN Micro ISO plug-in family:** 12 V models include standard 20 A NO resistive and high-current 35 A NO resistive, variant and test conditions apply. Coil current roughly 97–125 mA for described DC12 versions, **not yet PD10 driver compatibility**. Source: https://components.omron.com/us-en/sites/components.omron.com.us/files/datasheet_pdf/J270-E1.pdf
2. **TE Micro Relay A / VFMA plug-in Micro ISO:** 12 V standard and HC types; high-current variant nominal limiting **30 A continuous at 85 °C**, actual contact/thermal curves apply. Source: https://www.mouser.com/datasheet/2/418/5/NG_DS_V23074-X0000-A001_1217-736346.pdf
3. **HELLA Micro Relay 280:** part 933332571 SPST 30 A, 933332591 SPST 35 A, resistive catalog rating at 125 °C with built-in coil resistor; exact mating socket/terminal must be checked. Source: https://www.hella.com/forvia-us/assets/documents/Relays_Catalogue_2024_EN_LRes.pdf
4. **TE Power Relay F / Maxi ISO** (external high-current candidate): e.g. 12 V **1-1414147-0 / V23134J0052X429** shown as 70 A contact rating; catalog lists product *active* but **not currently available** at manufacturer page, so availability and selected model need sourcing checks. Source: https://www.te.com/en/product-1-1414147-0.html

**Relay acceptance:** socket ecosystem, precise 85/86/30/87/87a pin arrangement, coil polarity and suppression, ECU PD10 sinking/sourcing and current limit, cold crank pickup/dropout, load-specific *motor inrush and contact endurance*, accessible extraction, ambient temperature and mating-terminal retention. “30 A” or “70 A” is **not** automatic pump/motor suitability, PCB copper rating or fuse rating. Favor resistor/other validated suppression based on pump release-time safety, not simply a diode without analysis.

### Separate big relays: reason and limits

A separate physically supported, fused high-current module is favored **provisionally** for potential electrical steering/hydraulic pump, fan or other motor conversions because it simplifies large-gauge cable/thermal handling, improves service access and avoids overloading the shared ECU trunk. **It is not guaranteed to reduce electrical noise by mere distance.** Correct source-side fusing, return topology, short motor loops, robust battery/engine bonds, suppression at the load/coil and proper wiring paths are more important. No extra high-current functions are committed or populated yet.

## Current measurement methods — actual user meter

**UNI-T UT132C** has DC current 10 A max direct measuring range, fused 10 A input; **up to 5 A continuous**, **over 5 A for <10 s with >15 min between such tests** per manual, and mA port is separately fused. See https://sensorfor.com/www/manual/Uni-T/UT132C.pdf. Always measure **in series**, isolate power before arranging secured rated connections, and use correct 10 A + COM terminals and DC mode. **Never put the ammeter across battery positive/negative or replace a high-current fuse with meter probes.** Fuse, lead and handheld meter burden may cause voltage drop and start-current exceeding 10 A may blow meter protection / arc. **Do not put UT132C inline with Walbro pump, fan, main feeder or unknown actuators.** For sustained large motor/branch current and start peaks, acquire/borrow a **DC-capable Hall-effect clamp meter** with suitable range and preferably inrush/min-max; clamp one conductor only. The UT132C remains useful for low-current individual loads within its limits and DC millivolt voltage-drop tests at existing closed circuits.

## F6/F7/F8 outstanding and next artifact

- F6: wait for owner's revised **as-built EpicEFI wiring diagram**, then annotate source vs switched relay outputs, old MS box positive, returns and the actual **boost PWM Idle reuse**, including whether K3/CB3/JP1 circuit is physically used. Map installed Walbro relay and PD10 fail-safe. No repeat request for known Walbro swap or two injector fuses.
- F7: measure current at pump under real pressure, main ECU, coil and boost loads with suitably rated instruments; quantify volts across upstream supply, contacts and harness; model coincident and peak loads; no fuse/bus/socket ratings until wire and return paths validated.
- F8: reevaluate PCB-only vs hybrid after **smaller real electronics load**, standard Micro relay/socket sourcing, optional separate two high-current positions, location and service space. Earlier preference for hybrid remains provisional and has to be retested; no physical schematic or release approved.

**F6 OPEN · F7 OPEN · F8 OPEN.**
