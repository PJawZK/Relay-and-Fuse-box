# Original Volvo LH2.4 fuel-pump relay: outputs and tank-wire isolation

_Date: 2026-10-28. Vehicle: 1997 Volvo 940 B230FK sedan, Scandinavian market, completely separate aftermarket Mega144H7/EpicEFI relay/fuse/wiring system._

## Immediate rule

**Do not manually ground abandoned LH ECU pin 20, bridge original relay socket 30–87/2, or otherwise energize the original factory pump section until its old rear/tank pump conductor is physically identified, disconnected from any pump/tank connector, safely terminated and checked de-energized.** The user is appropriately concerned that stranded original fuel-pump wiring may remain near/inside the fuel tank after conversion.

The original LH2.4 injection assembly may contain two controlled relay sections in one housing. Grounds from the original LH ECU are:

- **LH21 → 86/1 (system/main section) → 87/1** to original LH ECU pin 9 and engine-management components.
- **LH20 → 86/2 (pump section) → 87/2** to factory pump supply circuit. In variant schematics the second stage may receive its operating supply through the main stage; manually grounding LH20 **alone** is not a trustworthy independent relay or feed test.

Sources:
- Dave Barton, `LH 2.4 ECU PIN FUNCTIONS 940 B230F/FT`: https://www.davebarton.com/pdf/Harness_LH-2.4-940EZKPinFunctions2024.pdf
- Volvo/Bosch 940 combined-system-relay functional description: https://lemon-manuals.org.ua/Volvo/1993/940%20L4-2320cc%202.3L%20SOHC%20VIN%2083%20B230FD/Repair%20and%20Diagnosis/Relays%20and%20Modules/Relays%20and%20Modules%20-%20Powertrain%20Management/Relays%20and%20Modules%20-%20Fuel%20Delivery%20and%20Air%20Induction/Fuel%20Pump%20Relay/Description%20and%20Operation/Bosch/
- Original 1995 Volvo wiring manual TP 3908202, indexed text for fuse 1, fuse 11 and rear harness: https://forum.vccn.no/dokumentasjon/Volvo%20koblingsskjemaer/900-x90/tp3908202_940_1995_wiring_diagrams_section_3_39.pdf

## The relay is not pump-only as a complete assembly

The **combined relay system** supplies the original pump(s) plus original LH fuel-management circuits such as the ECU, MAF, injector power through the suppression relay, idle-air valve and, in specific variants, the oxygen-sensor heater. **Do not assume every listed consumer shares 87/2**: the main **87/1** and pump **87/2** outputs are different branches. Pump-only section is mainly for pump feed; heater connections and fuse details vary by year, engine and market.

The **1995 Volvo B230FK/FT fuse-function index** lists:
- **Fuse 1:** fuel system, original ignition-related functions, oxygen-sensor heater for turbo models, and supply associated with fuse 11;
- **Fuse 11:** original LH2.4 in-tank primer/pump branch, downstream of fuse 1 in referenced configuration.

These assignments are **1995 reference evidence**; the user's exact 1997 installation and previous wiring alterations must be checked. Multiple original pump layouts exist across 940 years; later 940s can have **single in-tank pump** rather than an under-car main pump plus a tank pre-pump. Sources:
- https://www.volvoclub.org.uk/faq/FuelSystem.html
- https://charm.li/Volvo/1994/940%20L4-2320cc%202.3L%20SOHC%20Turbo%20VIN%2086%20B230FT/Repair%20and%20Diagnosis/Maintenance/Fuses%20and%20Circuit%20Breakers/Fuse/Locations/

## Factory rear wiring and access

**Reference harness location:** 1995 Volvo diagram identifies **C93, four-pin**, at **left rear wheel housing**. In the original 1995 harness, a **pink (P) conductor** is used for the pump positive feed; fuel sender wires run through the same connector. Another original 1995 connector table lists **C1 (left A-post / sill-harness 53-way), position 17 = pink pump wire**, position 16 = brown and position 9 = gray/white fuel-sender related wires. This can guide **identification**, not authorization to cut/energize by color alone.

Sources:
- https://charm.li/Volvo/1995/940%20L4-2320cc%202.3L%20SOHC%20Turbo%20VIN%2087%20B230FT/Repair%20and%20Diagnosis/Instrument%20Panel%2C%20Gauges%20and%20Warning%20Indicators/Diagrams/Electrical%20Diagrams/
- https://www.volvoclub.org.uk/faq/FuelSystem.html
- https://forum.vccn.no/dokumentasjon/Volvo%20koblingsskjemaer/900-x90/tp3908202_940_1995_wiring_diagrams_section_3_39.pdf

**Exact original `Volvo 940 (1995) Wiring Diagrams - Copy.pdf` attachment is not currently directly readable here**, and the supplied year is 1995 rather than the user's 1997 car. All OEM C93/C1 pin assignments and variant routing must be verified in vehicle; some later fuel systems differ.

## De-energized verification sequence — do not activate old pump relay

1. **Keep LH20 ungrounded, original pump section OFF.** Work in a ventilated environment, away from fuel spills/vapour, heat, open flames and arcing/energized contacts. Engine and key OFF.
2. **Disconnect battery negative** and ensure aftermarket EFI/pump has no alternative energized supply. Identify which pump power harness currently actually serves the in-tank pump; the current EpicEFI wiring is reported new, but don't assume the obsolete OEM body-side wires are disconnected at the tank.
3. At the **trunk / left rear wheel arch**, identify original **C93-type pump/sender connector** by connector geometry and documented circuit, not color alone. If it is indeed the obsolete original harness, unplug it **only while electrically dead**; **isolate/secure its harness-side pump conductor** without disturbing current new EpicEFI pump power or fuel level-sender integrity.
4. With source and pump end **both demonstrably de-energized and disconnected**, trace by continuity between old factory pump output branch and original rear harness-side connector; verify no unexpected backfeed/other loads or short to chassis. **Never use resistance/continuity mode on a live circuit**, and don't probe/open fuel tank interior.
5. If unknown cut wiring or any open terminals may be inside/at the tank, **do not re-energize the factory circuit**. Have the old conductor physically isolated/capped away from vapour exposure before any relay activation tests. Pulling a fuse or removing a relay is not proof of permanent isolation; both may be reinstalled or bypassed later.
6. Confirm any independent H-bridge relay has appropriate protected supply, spare capacity, control during RUN/START if needed, isolated actuator power ground and failsafe position. **Prefer a different known-good independent OEM relay feed or new dedicated relay** over an old pump circuit showing uncertain wiring/voltage loss.

**No sparks should be created deliberately or tolerated near the tank**; don't manipulate or meter live connections in the trunk/tank area or use a test lamp to intentionally draw power from abandoned pump conductor. If fuel vapour/leaks are present, stop electrical testing and resolve the fuel issue first.

## Current test status

- Original LH21 manually grounded with key OFF → original main section clicks, pin 9 becomes powered.
- Battery 12.38 V OFF, 12.34 V ON.
- LH pin4 11.25 V and pin9 11.17–11.25 V ON.
- Direct battery+→LH pin4 fluctuated **0.87–1.25 V** under main-relay activation.
- **Original pump section LH20 not yet deliberately tested; original rear harness isolation unverified.**
- H-bridge still powered/grounded at the aftermarket ECU screw terminals, not relocated.

Do not merge the original OEM pump and current aftermarket EpicEFI fuel pump circuits into a single diagnostic without physical evidence.
