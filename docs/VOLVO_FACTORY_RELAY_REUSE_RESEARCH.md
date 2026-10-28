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

## Alternate OEM relay locations — independent circuit shortlist (2026-10-28)

The user wants a **different physical relay** because the original fuel-injection relay has two sections **within one housing**, and original LH ECU pin 4 showed **0.87–1.25 V direct loss from battery positive while LH pin 21 main section was activated**. This does **not establish that the relay contacts caused the pin 4 drop**; LH pin 4 is a permanent feed, not the switched contact output. Other relays in the central box may share the same rail/fuses, so independence of upstream feed must be measured, not inferred from different physical housings.

The **1995 Volvo wiring manual relay location list** identifies these cabin central-box letter positions. It is historical model-family documentation; the actual 1997 Swedish-market B230FK/M90/MCC car may not have fitted/fully wired positions.

| Position / designation | Original circuit | Assessment for this user's 1997 sedan M90 |
|---|---|---|
| **I / 2/8** | Overdrive relay | **First location to inspect**. M90 has no electrically controlled M46 overdrive, hence original OD function unnecessary. Socket, contact 30 and 15 feeds may be absent, and old OD controller is a nonstandard logic module, not automatically a substitute for an ordinary 4/5-pin relay. If an original M46/AW harness exists, trace all outputs before using. Do not appropriate other loads from fuse 12. |
| **D / 2/16** | Tailgate intermittent-wiper relay | **Second to inspect**. Sedan has no tailgate wiper, so relay usually absent; socket may have no terminals. An intermittent-wiper module is not a simple power relay. |
| **F / 2/2** | Front fog-lamp relay | **Conditional** if front fog lamps absent and no planned restoration. Can have original relevant power/contact capacity, but old foglamp switch and lights wiring must be isolated. |
| **H / 2/15** | Japanese exhaust-temperature relay | **Conditional/likely absent** on Scandinavian-market car; do not presume fitted socket. |
| **2/12** (engine bay; not cabin letter universally established) | Original radio-interference suppression relay | Possible abandoned LH-era relay, if physically present. Might share original injection supply / no independent battery feed, must trace. |
| **2/11** (engine bay) | Engine cooling-fan relay | **Conditional** if replaced by fully independent aftermarket EpicEFI fan-control power path. Do not remove/bypass if original cooling fan still depends on it; stock relay may have high-current capable contacts but these are needed for safety if fan still active. |
| **E / 2/13** | MFI fuel injection relay in non-turbo/variant entries | Don't count it as a second extra existing physical fuel relay until the specific late-turbo installed configuration proves it. |
| **O/P/R/S** | No assigned function in 1995 manual | Physical spaces only; no guarantee of contacts, wiring, or a powered socket. |
| **J / 2/6** | 15I bypass/overload for power windows and heated seats | **Reserve**, because user plans stock donor power windows and possible heated seat operation; not a safe spare by default. |
| **A/B/C/G/K/L/M/N** | Existing lighting, warning, locking, fuel control, etc. depending on variant | Keep functioning original safety/body consumers; notably A is bulb failure monitor (large round unit). M is **2/23 fuel injection** in the **1995 Volvo OEM list**, even though some generic third-party box charts label M differently. |

Source: Volvo factory TP 3908202 940 1995 wiring diagram, page 9 (relay layout) as indexed via https://forum.vccn.no/dokumentasjon/Volvo%20koblingsskjemaer/900-x90/tp3908202_940_1995_wiring_diagrams_section_3_39.pdf ; cross-check https://charm.li/Volvo/1995/940%20L4-2.3L%20SOHC%20VIN%2088%20B230F/Repair%20and%20Diagnosis/Power%20and%20Ground%20Distribution/Diagrams/Diagram%20Information%20and%20Instructions/List%20of%20Components%20By%20Component%20Number/ ; layout image https://fuseandrelay.com/volvo/940-960-980.html ; https://www.volvoclub.org.uk/faq/ElectricalCircuitsRelays.html . 1995 factory diagram indexed content is available, but actual PDF image-level comparison with this user's original uploaded PDF has **not** been completed.

**Verification before selecting one:** (1) locate physically installed relay/socket from the letter; (2) determine whether all needed **coil/contact terminals are present**; (3) check source fused supply with ignition OFF/RUN/START and the return path; (4) compare actual battery+ to relay contact-feed voltage under realistic independent load to see if shared factory rail has the same drop; (5) fit only a relay with **verified matching contact function, polarity, suppression and ratings**; (6) isolate abandoned original outputs and add proper branch fuse, separate H-bridge motor return and safe power-off behavior. Prefer a **new dedicated automotive relay with a known good battery-fed fused power line** over a superficially free but unpopulated OEM location. A suitable OEM position could be used as mounting/wiring convenience, but that is not proven to be a pre-wired free supply.

## User-observed physical population — 2026-10-28

The user visually reports original electrical-distribution-unit relay positions **A, C, E, F, G, J, K, L, M, N as populated**. Positions **B, D, H, I** and apparently **O/P/R/S** are **not populated**. This is **visual occupancy**, not yet proof that each position contains the factory-documented module, a fully wired socket, functional contacts, suitable fused input, or spare output.

| Visually populated | 1995 TP3908202 factory-position label | Practical classification |
|---|---|---|
| A | 7/75 lamp failure warning | Preserve (user previously described large round unit) |
| C | 2/4 front intermittent wiper | Preserve |
| **E** | **2/13 fuel-injection MFI** | **Identify actual relay part number, color, body/pin layout; candidate unused old EFI wiring** |
| **F** | **2/2 front foglights** | Conditional only if factory front foglights are absent/unneeded; may be active safety/lighting equipment |
| G | 2/36 headlight flasher | Preserve |
| J | 2/6 bypass 15I, power windows/heated seats | Preserve for planned stock power-window installation, even if presently unused |
| K | 2/37 headlights | Preserve |
| L | 2/7 central locking | Preserve |
| **M** | **2/23 fuel-injection** | **Identify actual relay; possible distinct relay or variant alternate; do not assume second EFI module** |
| N | 2/50 high-beam bypass | Preserve |

**Refined original shortlist:** positions I (OD, M90 unused) and D (estate tailgate wiper, sedan unused) are physically empty: do not prioritize them as ready-to-use original wired relays. Focus first on **E and M** as actually present, then F if unused. The Volvo 1995 manual *lists both E and M as injection-related positions* but the 1994–95 wiring configurations can use either a **two-section traditional LH injection relay in E** or **a later separate single pump relay in M**, depending on engine/market; thus both being physically populated on this converted 1997 B230FK needs in-car confirmation, not model-general inference. Volvo service/reference materials: https://forum.vccn.no/dokumentasjon/Volvo%20koblingsskjemaer/900-x90/tp3908202_940_1995_wiring_diagrams_section_3_39.pdf and https://www.volvoclub.org.uk/faq/ElectricalCircuitsRelays.html ; Swedish owner discussion https://www.jagrullar.se/forum/viewtopic.php?t=88651

**Non-invasive discriminators:** first record **E and M relay-case printed Volvo/Bosch/Hella part numbers, body colors, terminal count and terminal numbers**, without moving the relay modules between sockets. Determine which physical relay clicks upon the **already-established LH21 low-side command** only if its original outputs are known safe; do not deliberately energize LH20/old pump feed before isolating the old pink tank conductor from the newly wired MS fuel pump. With car OFF/battery isolated for socket inspection, verify actual relay socket terminal population and continuity rather than assuming the generic 1995 variant's pinout. A relabeled replacement or pre-existing wiring change may explain divergent locations. Both may still share original common fusebox feed and the measured LH4 0.87–1.25V loss.

## Physical relay identification from user photographs — 2026-10-28

**Direct photo evidence supplied by user, confirmed relay positions:**

- **E / white:** Volvo **3523608**, additional embossed number **898151**, 12 V, Made in Hungary (housing photo). User explicitly identifies this as the **two-control LH2.4 system/fuel-pump relay**; grounding original LH ECU pin **21** actuated its main-system stage, and pin **20** is the separate original pump-control input on the **same relay module**. This replaces any speculation that original LH20 and LH21 are different physical relays.
- **M / blue:** HELLA **4RD 003 520-52**, 12 V, Made in Spain (housing photo). Volvo OE cross-reference **9130270**, also known from 1994+ 940 variants as a blue **fuel-pump / alternative general-purpose relay**, but also used for **fog lamps, high beams, A/C** and other roles in different sockets. Therefore **its role in THIS populated M socket is not proved by the relay part number alone**.
- The 1995 Volvo panel legend labels E as **2/13 MFI** and M as **2/23 fuel injection**. Source records and owner guides vary with engine/market/year and sometimes identify the blue Hella relay as a later pump relay *instead of* the white 3523608. Since **both** are physically installed in this 1997 B230FK, **do not assert either is electrically redundant or that M has any particular pump/ECU output until the actual M socket wiring is traced**.
- The blue relay is an automotive **changeover/5-terminal family** (30, 87, 87a, 85, 86) and published 940 fog-lamp discussions describe **a diode across 85/86** on Volvo 9130270. Confirm the printed symbol and orientation on the user's *actual* relay before making any powered test; diode-protected coils are polarity-sensitive. DO NOT substitute a generic relay with a different protection circuit, or blindly ground either 85/86.
- Physical confirmation of a second relay housing means M **is an independent physical component**, but it **may share the same OEM upstream feed/distribution/fuse** that has already shown a direct battery+ to unused LH4 **0.87–1.25 V fluctuating drop** with E/main activated. A separate physical relay does **not prove independent healthy power supply**.

References:
- Volvo Owners Club on blue Hella 4RD and non-interchangeability: https://www.volvoclub.org.uk/faq/ElectricalCircuitsRelays.html
- Volvo relay application and part cross-reference: https://www.prancingmoose.com/volvorelays.html
- 4RD 003 520-52 mapped to Volvo 9130270 in dismantler listings: https://www.varaosahaku.fi/en-se/OEM/4RD%20003%20520%2052/
- Volvo 940 owner fog-relay report for suppression diode in 9130270: https://volvospeed.com/index.php?app=forums&controller=topic&id=95523&module=forums
- 1995 Volvo OEM letters E=2/13, M=2/23 in TP3908202 index: https://forum.vccn.no/dokumentasjon/Volvo%20koblingsskjemaer/900-x90/tp3908202_940_1995_wiring_diagrams_section_3_39.pdf

**Next safe M-socket test, before any relay actuation:**
1. With car stopped and key OFF, carefully remove **only the blue M** relay and inspect terminal numbering/suppression symbol on its side/bottom and its socket for charring, loose terminals or corrosion. Do not interchange it with E/other blue relays.
2. With **battery disconnected**, establish which M socket terminals are populated, trace its output conductor **de-energized** (especially confirm old pump pink positive at driver-side A-pillar is cut/removed and isolated from new MS pump supply), and that no other old electrical load remains connected. Meter continuity/ohms **only on powered-off circuits**.
3. When old output is safely isolated and wiring is known, measure M socket voltage to battery-negative in OFF/RUN/START (engine not running), pin by pin as identified by **actual schematic**; no blind bridging or energizing relay/output. Determine whether coil positive is ignition-switched or battery constant, whether any existing command wire drives the *correct* coil negative, and whether M contact 30 has a separate healthy feed.
4. To compare with white E independently, measure **battery positive to M socket contact feed** under controlled conditions, then the correctly confirmed switched output under verified load, rather than using LH pin 4 as a proxy. Do not connect H-bridge until fuse/contact/wiring/ground return and loss-of-power behavior are confirmed.
5. **Key OFF manual ground at E/LH21** already energized original system, so a permanent ground would be unsafe. Any M control ultimately needs verified OFF/RUN/START behavior, protected low-side driver and fail-safe actuator shutdown.

The photo evidence **does not establish any measured voltage, current, continuity, socket pinout or actual M output branch**, and there is no hardware modification.

## Selection and test gates for DC idle H-bridge relocation

1. **Identify candidate's actual relay/socket location, contacts and feed net**, from an applicable diagram and/or user text inspection. A documented relay symbol or an empty socket does not guarantee wired terminals. Avoid requesting inaccessible photographs when text identification is sufficient.
2. Check **coil command**: relay should provide H-bridge supply in **RUN** and, if required by the actuator, **START**, and switch off with key off. A stock LH-ECU-controlled coil likely requires an independent new command when LH electronics are absent. Do **not** silently energize it permanently or bridge relay contacts.
3. Confirm **battery-feed source and protected output**. Add an appropriately rated fuse to the isolated H-bridge branch, coordinated with the actual conductor and expected/inrush H-bridge motor current; the factory feed/relay/socket must also be fit for that load.
4. Keep the current EpicEFI fuel-pump command, pump relay and pump shutdown logic entirely in their **new independent aftermarket system**. Reusing an abandoned OEM injection relay is distinct from tapping the *current* pump output.
5. Give H-bridge motor current a separate appropriate **power-ground return** so it no longer flows through the ECU positive/ground screw terminals or ECU sensor reference.
6. Verify safe throttle/idle-air actuator behavior with lost power and at the ignition transitions. Suppression/EMI must be appropriate for actual H-bridge topology.
7. After relocation, repeat matched idle logging: ECU VBatt, H-bridge commanded PWM/position, RPM, ignition-related channels, and preferably external voltage reference under normal operation. Keep October 26 event evidence separate from new observations.

Do not pick relay/fuse ampere ratings, pin/cavity numbers or splice points from a 1995 diagram alone. The 1997 actual car and the user-supplied 1995 PDF, when available, take priority over general reference examples.
