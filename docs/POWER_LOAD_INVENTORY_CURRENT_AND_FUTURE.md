# Volvo 940 ECU electrical loads — present and planned power-feed inventory

**Version:** 0.2 planning draft, 2026-11-02. **Scope:** 1997 Volvo 940 Turbo B230FK / M90, EpicEFI Mega144H7, replacement of aging **aftermarket** MS power/relay board, plus provision for planned car electronics.

## Reading rules

**Status**: **INSTALLED** = user confirmed current part/function; **INSTALLED—SUPPLY UNKNOWN** = component present, electrical source/fuse ownership not established; **PLANNED** = user project roadmap, not fitted; **CONDITIONAL** = possible implementation, not a purchase/build commitment; **EXTERNAL** = already independently supplied or deliberately separate; **NOT USED** = do not design for.

**Current numbers**: unless from a part-specific credible specification, current is **UNMEASURED** and should not be a fuse-selection figure. **Voltage** is nominal functional supply domain, not necessarily acceptable direct supply to a raw IC. **Protection scope**: power feed/fuse covers source wiring and connected load; the ECU PWM/low-side signal and sensor input circuits are *not* power-feed fuses. Inputs should never have high actuator current flowing through ECU 5 V/sensor ground.

**Design zones**:
- **E — Engine critical**: engine ECU, injectors, ignition, fuel pump (control and protection remain hardwired, separate from accessory computers).
- **A — Engine auxiliary/sensors**: future IOX/EGT, pressure/temperature inputs, ethanol, low-current valves.
- **C — Cabin/CAN**: planned cluster screens, controls, nodes and logging; may use a separate **protected cabin subdistribution** instead of lengthy individual runs from engine board.
- **H — Heavy external**: fan motor, H-bridge, possible new fuel pump high-current branch; safe contact/relay/busbar design is primary.
- **S — Signal only**: no separate high-current protected feed for a passive sensor/switch.

### 1. Installed power consumers and controls

| Ref | Current item, evidence/state | Nominal power rail, demand behavior | Proposed fuse/relay responsibility | Confirm before rating |
|---|---|---|---|---|
| C01 | **EpicEFI Mega144H7 ECU**, INSTALLED | Ignition-switched automotive 12 V; stable during cranking and transients; internal electronics demand unknown | **E:** independent fuse and **main relay**; ECU sensor ground stays separate | Installed main-branch path, 12 V peak/steady, start/run/hold requirement, PSU min input |
| C02 | **4 Bosch EV14 0280158117 injectors**, INSTALLED, power from **MS box via TWO fuses, each serving a pair of injectors** — USER CONFIRMED 2026-11-02 | 12 V switched; high-impedance nominal 12 Ω per injector (supplier); current is pulsed, duty-dependent, worst simultaneous demand needs review | **E: PROPOSE ONE COMMON injector-positive fuse** feeding all 4 injectors. All 4 ECU ground-side sequential outputs remain independent. Eliminate second paired injector fuse from baseline. | Actual 4 injector feed wire size, switched source, peak/duty/inrush, time-current/fault handling. No fuse ampere chosen |
| C03 | **VAG 032 905 106B wasted-spark coil**, INSTALLED—SUPPLY UNKNOWN | 12 V switching and high pulsed ignition current | **E:** dedicated fused ignition power, optionally same ignition-run master control but **not** same fuse as ECU | Whether positive feed presently goes through MS box, coil electronics current/suppression, full harness routing |
| C04 | **Current in-tank fuel pump** (~110 L/h historic estimate), INSTALLED | 12 V motor with startup and possible stall surge | **E/H:** dedicated fuse and **PD10-commanded pump relay**, preserve prime/stop safety; main board or rated external power stage after sizing | Pump actual model, installed source and relay, current at fuel pressure, cold/hot startup, ground |
| C05 | **Two boost-control solenoids** (upper/lower), INSTALLED | 12 V inductive PWM actuator loads | **A:** a protected ignition-switched actuator feed; group if wiring/fault analysis allows. ECU controls individual switches | Power source, valve coil resistance/current, supply control states, suppression |
| C06 | **Innovate LC-1 wideband**, INSTALLED—SUPPLY UNKNOWN | 12 V controller **plus heater**, heater has cold-start transients | **A:** own fuse if board supplies it; keep analog sensor reference away from heater/motor return | Actual installed source/return, heater/controller startup and continuous current |
| C07 | **Radiator electric fan**, INSTALLED—SUPPLY UNKNOWN (earlier reports connect it through aftermarket relay hardware, current exact path unverified) | 12 V motor; high steady and much higher start/stall current | **H:** dedicated protected high-current supply and relay/driver, likely **external** to compact engine ECU PCB | Fan motor current, initial surge, fan existing relays, ECU command and ground |
| C08 | **DIY DC idle H-bridge + DC idle valve**, INSTALLED and freshly rewired 2026-11-02; user says operates better | 12 V motor supply, bidirectional PWM motor-output pair; independent new relay/wiring | **EXTERNAL:** preserve current separate new relay and dedicated motor return; no fast-idle relay on replacement | Record new positive branch source/fusing and return only for overall upstream source budget; no troubleshooting renewal |
| C09 | **Crank VR, cam Hall, TPS, Bosch MAP/IAT, CLT**, INSTALLED | ECU-defined sensor excitation/reference (some passive/unpowered, Hall/TPS active), **not common 12 V motor rail** | **S:** leave on ECU sensor 5 V and signal-return circuits as required | Each sensor's actual excitation, pin assignment and return; no new 12 V fuse each |
| C10 | **Fuel-pressure transducer** currently on stock rail, INSTALLED; sensor replacement pending rail swap | Typically regulated 5 V for installed analog transducer; actual fitted sensor spec confirm | **S:** ECU regulated sensor rail, not raw 12 V | Pressure sensor excitation/range; replacement sensor characteristics |
| C11 | **VSS BC547 conditioner and stock wheel speed/ABS signals**, INSTALLED/partial | Low-current logic pull-up/reference. Existing front ABS VR sensors are passive and not new powered nodes | **S:** ECU/IOX appropriate low-voltage conditioned input | Actual pull-up/conditioning power, front wheel VR interface and shielding |
| C12 | **Original MS K3 FASTIDLE/PWM idle circuit**, **NOT USED** — USER CONFIRMED 2026-11-02 | None | **REMOVE from baseline**: no fast-idle relay, no dedicated PWM idle valve load or fuse/driver pass-through | Confirm no unrelated current wire is accidentally using old K3 terminals during migration |
| C13 | **Original Volvo LH fuel/injection relays/wires**, **NOT USED** by EFI | None for replacement box | **EXCLUDE**: don't continue OEM relay research | None for this project |

**Injector decision detail:** Current two fuses supply two pairs; there is no benefit required merely by the EV14 high impedance or sequential injection. A single fused B+ distribution to four injectors is a sensible **draft design choice**, provided the common fuse and individual downstream wires are protected for faults and the starter/crank/engine-stop operating states. A single fuse failure stops all fuel injection; separate pair fuses could leave only two cylinders operating, with undesirable misfire. This is a tradeoff, **not a validated claim that every ECU must use one fuse**. Four ECU injector *control* wires stay independently switched. **Do not combine them**.

### 2. Planned/upgradable engine and chassis loads

| Ref | Component or upgrade, stage | Required electrical supply | Proposed place/power-feed requirement |
|---|---|---|---|
| F01 | **255 L/h fuel-pump upgrade**, PLANNED | 12 V pump motor; likely different/higher continuous and start current than existing pump; **part/model and peak current TBD** | **E/H:** preserve separately fused pump relay control from PD10 and allow heavier rated power path or external contactor/relay. Must be reassessed when pump model selected, not pre-rate from flow alone |
| F02 | **Custom rail + adjustable FPR + replacement fuel-pressure transducer**, PLANNED | Mechanical rail/FPR require **no electrical feed**; new pressure transducer needs its specified ECU-regulated sensor supply | **S** ECU analog input/reference; no fuse for mechanical pressure regulator |
| F03 | **EMAP via existing 200-PSI transducer after rail swap**, PLANNED | Likely 5 V analog sensor excitation if sensor remains as previously configured; input signal to free Mega144H7 ADC | **S** no new 12 V motor feed; share correct ECU 5 V reference and signal return; hot exhaust tubing mechanically independent |
| F04 | **4× exhaust gas temperature K-type probes + 4 converter channels**, PLANNED/bench experiments | K-type probes are **passive thermocouples**. MAX31856 IC supply **3.0–3.6 V**, active conversion typ ~1.2 mA *per IC* (not whole module) | **A:** one protected ignition-fed 12 V auxiliary electronics supply → **local regulated 5/3.3 V** for IOX + conversion boards. Include regulator, interface, CAN and wiring margin |
| F05 | **IOX expansion / Mega_EPIC_IOX**, PLANNED for nonessential channels | Controller requires appropriate low-voltage regulated input (Mega2560 design 5 V logic for many configurations; actual board connector specification TBD), CAN/transceiver rails model-dependent | **A:** ONE or more fused **12 V auxiliary logic feeds** into dedicated automotive DC/DC; not ECU sensor 5 V rail used to power multiple controllers. IOX handles EGT, EMAP if transferred, extra sensors and switch inputs |
| F06 | **Oil-pressure transducer and oil-temperature sensor**, PLANNED for 940-DDS | Pressure often regulated 5 V analog; temperature passive thermistor or active 5 V as selected | **S/A:** sensor reference from ECU/IOX; no raw 12 V directly. Reserve two input channels rather than two high-current fuses |
| F07 | **Fuel/oil temperature and other auxiliary pressure sensors**, PLANNED/CONDITIONAL | Passive thermistors / 5 V analog or frequency electronics depending selected parts | **S/A:** grouped low-voltage sensor reference and protected inputs; negligible relative to motors |
| F08 | **Flex-fuel/ethanol-content sensor**, PLANNED if changing to E85 blends | Many OEM frequency-output composition sensors accept 5–12 V depending exact part; logic conditioning to ECU/IOX | **A/S:** small protected switched auxiliary power rail compatible with selected sensor, filtered signal return; no dedicated mechanical relay |
| F09 | **Clutch pedal position**, high-priority PLANNED | Rotary/linear Hall or OEM dual-channel sensor often 5 V reference; exact part may have dual redundant feeds | **S:** ECU/IOX regulated sensor rail, appropriate fault checks, independent signal returns. No 12 V power fuse for one pedal |
| F10 | **Accelerator pedal position**, second-priority PLANNED | OEM dual-track Hall/potentiometric pedal commonly ECU 5 V or specified reference; currently **measurement only** | **S:** protected sensor reference and signal inputs; do **not** infer an electronic throttle motor from the pedal plan |
| F11 | **Brake pedal switch / optional continuous travel sensor**, installed stock switch, continuous sensing optional | Existing switched contact (check voltage/logic); optional sensor 5 V | **S:** isolate/condition 12 V switch before IOX; optional 5 V reference for analog brake position |
| F12 | **Wheel-speed inputs, up to four wheels**, PLANNED as signal sources | Existing front ABS VR pickups passive (no sensor supply); rear conditioned VSS currently available. Additional Hall sensors, if selected, require proper low-voltage excitation | **S:** input conditioning/IOX acquisition; no individual 12 V fuse for passive sensors |
| F13 | **Steering angle, handbrake, reverse, clutch, gear/auxiliary switches**, PLANNED/CONDITIONAL | 5 V potentiometric/Hall or conditioned switch contacts; resistive/VR as chosen | **S:** IOX sensor/reference rails with transient/ESD and input protection |
| F14 | **Accelerometer/G-sensor**, PLANNED (3D-printer accelerometer owned for experiments; vehicle use unconfirmed) | Low-voltage 3.3 V or 5 V module depending actual part | **S/A:** IOX low-voltage regulator, no individual automotive relay |
| F15 | **Alternator output upgrade**, PLANNED | **Power SOURCE**, not a board load; capable of increasing battery/charging trunk current and transients | Reassess feeder/cable/ground bonding, upstream protection and automotive transient behavior. Do not put entire alternator output through ECU fuse box |
| F16 | **Electronic throttle/DBW actuator**, only **CONDITIONAL** longer-term idea, not a confirmed conversion | High-current reversible motor and dual sensor safety architecture if ever pursued | **H:** separate fused protected actuator/driver branch with independent safety review; not included in baseline relay/fuse slots without specific user decision |

### 3. Planned dash, CAN, user interaction and logging power

The [Volvo-940-DDS architecture](https://github.com/PJawZK/Volvo-940-DDS/blob/main/docs/core/940-DDS-003_Display_Architecture_and_Information_Ownership.md) defines **two 2.8-inch 480×480 ESP32 round displays** and **two 1.75-inch 466×466 ESP32 AMOLED round displays**, retaining analogue speedometer; **future 7-inch touchscreen** is explicitly separate. The application and node architectures are planning concepts, not proof all boards are mounted in the car.

| Ref | Planned electronics | Input supply / practical design load | Best protected feed |
|---|---|---|---|
| D01 | **2× 2.8-inch ESP32-S3 cluster round LCD nodes** | Board/module supply may be 5 V, ESP32 chip **3.3 V**; LCD/backlight current and radio bursts dominate, manufacturer complete-board measurement required | **C:** cabin fused switched 12 V → one/two regulated 5 V branches; local 3.3 V conversion |
| D02 | **2× 1.75-inch ESP32 AMOLED nodes** | As above: board-dependent 5 V/3.3 V, variable display brightness current | **C:** separate fused cockpit/cluster group or redundancy split from D01, then regulated local supply |
| D03 | **CAN distributor with SN65HVD230/TWAI transceivers**, PLANNED | SN65HVD230 transceiver uses **3.3 V**, other CAN parts transceiver-specific; CAN twisted-pair is NOT a power feed | **C/A:** local 3.3 V rail at each powered node; future fused accessory 12 V trunk to cabins/nodes rather than CAN-H/CAN-L supplying power |
| D04 | **Rotary encoder/controller and button-box user inputs**, PLANNED | Low-current 3.3/5 V controller and contact signals | **C:** share regulated supply with nearby cabin CAN node, protected against automotive 12 V on switches |
| D05 | **Steering-wheel CAN node**, PLANNED | Low-current 3.3/5 V controller, buttons and possible backlighting | **C:** dedicated small regulated/conditioned accessory feed and appropriate clock-spring wiring/fusing; not ECU critical supply |
| D06 | **Other CAN nodes (centre, W/R, optional steering node)**, PLANNED | Low-current MCU + transceiver supply (3.3/5 V), module peripherals TBD | **C:** share protected cabin trunk, local conversion and branch protection; reserve two connector interfaces |
| D07 | **Future 7-inch touch interface**, PLANNED | Model/OS/brightness-dependent 5/12 V, not yet chosen | **C:** reserve separate protected cabin supply; no unsupported display-wattage claim |
| D08 | **CarPi Raspberry Pi 4 HAT, ignition timer, Tuner latch and NVMe**, PLANNED | Pi 4 requires a quality **5 V ~3 A-capable** supply; HAT/NVMe/USB may require extra margin and robust undervoltage startup/shutdown | **C:** protected 12 V accessory feed → automotive 5 V regulator, separate ignition sense + optionally permanent 12 V for graceful shutdown; NOT on ECU sensor 5 V |
| D09 | **Pi Zero 2 W EpicEFI TS shim**, bench/network operational, in-car installation/power ownership unverified | Separate regulated 5 V; Raspberry Pi guidance lists ~2 A recommended supply capability for Zero 2 W system incl peripherals, design depends USB | **C:** same protected accessory/logging domain if installed in vehicle; never power from ECU sensor voltage reference |
| D10 | **Existing 9-inch Android head unit (or possible Pioneer alternative)**, installed/planned alternative | Existing automotive radio switched/constant +12 V, load and fuse rating device-dependent | **EXTERNAL:** preserve appropriate radio/accessory wiring; not necessary to move radio power through engine ECU box |
| D11 | **EpicHub phone/tablet**, installed personal devices and diagnostic tools | Powered by USB/charger, not an ECU-relay-board load | **EXTERNAL:** cabin USB power converter with own protection if integrated; avoid main ECU feed |
| D12 | **Extra CAN nodes and nonessential auxiliaries**, CONDITIONAL | Protected 12 V + local regulated 5 V/3.3 V; load TBD from actual node BOM | **C:** reserve a protected accessory trunk and physical fuse/cavity expansion, not one fuse per sensor |

### 4. Power-domain summary and installation boundary

| Domain | Key position/control | Required branch approach | Reason |
|---|---|---|---|
| **E1: ECU power** | ignition RUN + CRANK | Fused ECU-only relay feed | no actuator-heater/motor current in ECU supply/return |
| **E2: injector B+** | engine-enabled RUN + CRANK, ECU controls each injector low-side | **one shared injector supply fuse** from appropriate switched source | current two paired fuses unnecessary for baseline, but verify wire protection |
| **E3: ignition coil** | engine-enabled RUN + CRANK | own switched protected supply | ignition pulse currents separately isolatable |
| **E4: pump** | ECU PD10 only when permitted | own relay and fuse, reliable OFF on ECU loss | pump fault must not hold ECU output active |
| **A1: boost solenoids** | switched RUN (start mode TBD) | one grouped protected 12 V actuator circuit | inductive loads isolated from ECU electronics rail |
| **A2: LC-1/heater** | switched; heater controller manages cold/start | separate filtered 12 V branch | heater current and analog reference noise |
| **A3: sensor IOX / thermocouple electronics** | switched RUN/START as needed | low-current protected 12 V → automotive regulated 5 V and local 3.3 V | many sensors share **regulated** reference, not 12 V fuse each |
| **C1/C2: cabin CAN/cluster** | switched plus limited retained power if required | separately fused **cabin accessory feeder/subdistribution**, 12→5→3.3 V | avoid long bundled sensor/PCB-current wiring and accessory brownout affecting ECU |
| **C3: logging Pi** | controlled ignition latch with shutdown period | dedicated protected accessory feed + timer/hold-up / regulated 5 V | clean shutdown without keeping ECU/pump powered |
| **H: high-current motors** | individual appropriate controls | existing separate H-bridge; external fan; pump as rated | compact ECU PCB should not carry unrelated high-current motors |

**Sensor rule:** EGT thermocouples and VR wheel sensors are passive; raw Hall/pressure sensors and pedal devices typically need clean regulated 3.3 or 5 V chosen by model. Do **not** assign an automotive fuse or mechanical relay to every sensor: power the *IOX/controller* through a fused 12 V low-current source and distribute properly protected regulated sensor reference locally.

**Important all-shared-feed caveat:** Existing upstream X1 feeder (~4 mm² estimated by user) and 30 A fuse are **current observations only**, not proof of spare capacity for upgraded pump, cabin displays, Pi and future modules. Future expansion current must be measured/planned on its own separately protected power trunk before any actual wiring change.

## Concrete official supply reference points (not ratings for the final board)

- EV14 supplier model 0280158117 nominal 12 Ω: https://www.racetronix.biz/p/bosch-fuel-injector-50-lb-hr-520-cc-min-uscar-ev-14s/0280158117
- MAX31856 ADC 3.0–3.6 V and 1.2 mA typical active *IC current*, excluding module hardware: https://www.analog.com/en/products/max31856.html
- Espressif ESP32-S3 chip 3.3 V, reference **≥500 mA supply capability per bare chip power design**, not whole LCD current: https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/schematic-checklist.html
- Raspberry Pi 4 recommended 5 V 3 A; Pi Zero 2 W also needs dedicated 5 V system supply and peripherals accounted: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
- 940-DDS approved proposed display roles: https://github.com/PJawZK/Volvo-940-DDS/blob/main/docs/core/940-DDS-003_Display_Architecture_and_Information_Ownership.md

**Source boundary:** Installed/planned items are taken from the user's current confirmations, relevant previous Volvo/EpicEFI project discussions and the 940-DDS repository. Electrical voltage/current reference specifications are manufacturer/supplier references where specified. **Unmeasured automotive loads remain explicitly unquantified**, and speculative additions are flagged CONDITIONAL.

## Decision status and next work

- **AUTHORITATIVE NOW:** Injectors powered via **two fuses, each serving a pair**; PWM and FAST IDLE from old MS box not used; H-bridge independently relayed and recently wired.
- **V0.2 DESIGN CHOICES:** one common injector B+ fuse, omit K3 fast-idle, preserve main ECU and pump relay, supply two boost solenoids as individually controlled low-side loads, heavy fan supply external, H-bridge external, one or more auxiliary branches for IOX/cabin electronics rather than a fuse per sensor.
- **OPEN:** exact existing fuse/relay loading and other current positive-wire ownership (ignition/LC-1/fan/boost), actual component rated currents, protection design, expansion power budget, connector count and motherboard-versus-hybrid copper implementation.
- **NEXT:** develop power-zone and future-slot budget in `docs/POWER_DISTRIBUTION_EXPANSION_CAPACITY.md`, then reconcile against F6/F7 matrices and physical wiring.
