# Volvo 940 original relay/fuse system — reuse research (2026-10-27)

## Installed architecture: authoritative user correction

**User-reported current state (2026-10-27):** **None of the original Volvo OEM EFI wiring, relays or fuses supplies or controls the current Mega144H7 / EpicEFI installation.** The present engine-management electrical system uses **separately installed aftermarket wires, relays and fuses**, including an approximately 15–16-year-old DIYAutoTune/MegaSquirt-type aftermarket relay board. "Original MS box" means that aftermarket board has *unmodified internal circuitry*; it **does not** mean the Volvo's original LH-Jetronic relay/fuse system is still serving the engine.

The original Volvo injection-system relay sockets, wiring and fuse positions may **remain physically present** and may be reusable, but the user has not confirmed their present continuity, contact wiring, control signals, existing non-EFI consumers, fuse condition or whether relay coils still energize. **No factory OEM EFI load should be presumed still active.** In particular, do not repeat the earlier claim that OEM turbo fuel-injection relay 2/23 must remain for the current EFI system.

The H-bridge currently shares the aftermarket ECU's own positive and power-ground screw terminals, and the user plans to move it to an independently fused, ignition-switched Volvo original-system relay output. This relocation is **planned, not installed**.

## Wiring manual provenance and current access

- The user explicitly named an old upload: **`Volvo 940 (1995) Wiring Diagrams - Copy.pdf`**.
- Historical conversations on **2025-09-14** discussed its charging/starter pages (reported pages 188–189 and 194); conversations on **2026-02-06** discussed potential unused relay positions and cabin fuse-box reuse. These are **prior-conversation evidence**, not a fresh reading of the PDF.
- The exact historical uploaded PDF bytes were **not found/mountable in this project/runtime** on 2026-10-27 despite a search of current Project, Library and connected Drive. No original-file page-by-page or image-level review is claimed here.
- A publicly indexed matching title, **`Volvo 940 (1995) Wiring Diagrams`**, identifies manual numbers **TP 3908032 (UK)** and **TP 3908202 (USA/Canada)**; the indexed contents specify fuse pages 4–6, electrical distribution pages 6–9, B230FK/FT injection page 48, ignition page 58, and power/starter page 60 (manual's *printed* page labels). It may not be byte-identical to the user's `- Copy.pdf`. Public index: https://www.fichier-pdf.fr/2016/03/06/940-1995-wiring-diagrams/ ; also listed by Volvo Owners' Club: https://www.volvoclub.org.uk/wiring_diagrams_940_960.shtml .
- A **different 1995 Mitchell-derived** public power/ground list confirms the nomenclature of 2/13 and 2/23 as fuel-injection relays, but **not the user's exact 1997 wiring or current coil state**: https://charm.li/Volvo/1995/940%20L4-2320cc%202.3L%20SOHC%20Turbo%20VIN%2086%20B230FT/Repair%20and%20Diagnosis/Diagrams/Electrical%20Diagrams/Power%20and%20Ground%20Distribution/System%20Diagram/ .

**Applicability:** Vehicle is **1997 Volvo 940 sedan, Scandinavian-market B230FK turbo, M90 manual, MCC**. The 1995 book is close-generation reference, not an automatic authority for every late-1997 fuse/relay, package option or retrofit.

## Candidate factory relay positions — research list, not approved wiring

| Reference | Historical circuit / qualification | Reuse assessment given wholly separate current EFI |
|---|---|---|
| **2/23** | Fuel injection relay on original turbo system | **Priority candidate for inspection**, no longer needed *by EpicEFI*; actual socket, battery feed, former LH coil-control signal and whether any other OEM loads remain must be determined. The former ECU control line may not energize a relay anymore. |
| **2/13** | Fuel injection (MFI) relay in 1995 reference/component list; variant use can differ | **Conditional candidate** only if the car has that relay/socket and a suitable verified switched feed. Do not assume 2/13 and 2/23 both physically coexist or that both were used in this turbo. |
| **2/12** | Radio-interference suppression relay in 1995 electrical component list | Another **conditional** former-engine-management-related part, but location, current usage, physical terminals and power switching must be checked; do not choose solely on name. |
| **2/16** | Tailgate intermittent-wiper relay | 940 **sedan** does not require a tailgate wiper; a factory relay location may be unpopulated or lack useful harness pins. No ready-to-use energized supply assumed. |
| **2/15** | Exhaust gas temperature relay/sensor for Japan variant | Historically discussed as likely absent on Nordic car; harness/socket availability unknown. |
| **2/14** | Diesel glow-plug relay | Gasoline B230FK does not use diesel glow plugs; no implication that a useful energized harness exists. |
| **2/38** | Diesel EGR timer (variant-specific) | Similar conditional/likely absent on gasoline Nordic car. |
| **2/5** | Seat-belt/key-warning reminder for certain markets | Equipment-specific; cannot be called free without checking warning-system configuration. |

The **2/23 vs 2/13** distinction must be settled from the exact original Volvo variant schematic or by unambiguous installed relay/socket identification, rather than inferring from a generic component index. Historical February 2026 conversation also listed the above candidate positions; any claim then that `2/23 must remain` is **superseded** by the user's October 2026 explicit no-OEM-EFI-reuse correction.

## Preferred first diagnostic — use the unused LH2.4 ECU plug

The user proposes measuring the retained original **LH2.4 35-position ECU harness connector** first. This may avoid accessing/cutting the cramped fuse-board wiring altogether. A 940 LH2.4 pin-function source identifies **20 → fuel-pump relay low-side coil control (86/2)**, **21 → main injection relay low-side control (86/1)**, **35 → terminal-15 ignition-switched +12V input**, **4 → terminal-30 constant +12V**, **9 → switched output from original main EFI relay**. Their pin numbers and relay cavity connections require verification on the 1997 B230FK wiring. With LH ECU removed, **pins 20/21 will not actively command the relay**; a positive reading through a connected coil is *not* a valid trigger.

Use the read-only voltage and isolated-continuity checklist in [`LH24_CONNECTOR_RELAY_VERIFICATION.md`](LH24_CONNECTOR_RELAY_VERIFICATION.md) before considering any harness cutting, new coil drive, or fuse/relay selection. A terminal-15 signal at pin 35 is a possible low-current control reference, **not motor supply**. Keep ECU, live aftermarket pump supply and sensor grounds out of the proposed actuator feed.

## Original pump section — stop before energizing unknown tank conductors

The combined Volvo LH2.4 fuel-injection relay is **not pump-only as an assembly**. Main LH21/86/1/87/1 feeds the old engine management and LH20/86/2/87/2 controls the original pump branch; exact heater/fuse feeds are variant dependent. **Do not try LH20 as an independent substitute for the suspicious LH21 relay.** The user explicitly flagged the possibility of unconnected old harness wires near the fuel tank posing a spark/short risk.

A 1995 factory reference locates the original fuel-tank pump/sender connector **C93 (4-way) near the left rear wheel housing in the luggage area**, with a pink wire as one original pump feed. The 1995 wiring index also shows fuse 1 supplying fuel functions and fuse 11 identifying the original LH in-tank pump branch. **Don't presume these colors/connector positions are identical on 1997 B230FK.**

**Prioritize no-power trace and safe isolation of any abandoned old tank pump conductor** before energizing the factory pump section. See [`OEM_FUEL_PUMP_RELAY_AND_TANK_WIRE_ISOLATION.md`](OEM_FUEL_PUMP_RELAY_AND_TANK_WIRE_ISOLATION.md) for the documented safety gates. Cutting beneath the original fuse panel and live electrical testing near the tank are not prerequisites.

## Selection and test gates for DC idle H-bridge relocation

1. **Identify candidate's actual relay/socket location, contacts and feed net**, from an applicable diagram and/or user text inspection. A documented relay symbol or an empty socket does not guarantee wired terminals. Avoid requesting inaccessible photographs when text identification is sufficient.
2. Check **coil command**: relay should provide H-bridge supply in **RUN** and, if required by the actuator, **START**, and switch off with key off. A stock LH-ECU-controlled coil likely requires an independent new command when LH electronics are absent. Do **not** silently energize it permanently or bridge relay contacts.
3. Confirm **battery-feed source and protected output**. Add an appropriately rated fuse to the isolated H-bridge branch, coordinated with the actual conductor and expected/inrush H-bridge motor current; the factory feed/relay/socket must also be fit for that load.
4. Keep the current EpicEFI fuel-pump command, pump relay and pump shutdown logic entirely in their **new independent aftermarket system**. Reusing an abandoned OEM injection relay is distinct from tapping the *current* pump output.
5. Give H-bridge motor current a separate appropriate **power-ground return** so it no longer flows through the ECU positive/ground screw terminals or ECU sensor reference.
6. Verify safe throttle/idle-air actuator behavior with lost power and at the ignition transitions. Suppression/EMI must be appropriate for actual H-bridge topology.
7. After relocation, repeat matched idle logging: ECU VBatt, H-bridge commanded PWM/position, RPM, ignition-related channels, and preferably external voltage reference under normal operation. Keep October 26 event evidence separate from new observations.

Do not pick relay/fuse ampere ratings, pin/cavity numbers or splice points from a 1995 diagram alone. The 1997 actual car and the user-supplied 1995 PDF, when available, take priority over general reference examples.
