# Bowling & Grippo MegaSquirt power/relay board — PDF reference terminal map

**Reference status:** Historical/source-documented, **not yet verified as the exact PCB revision or as-connected installation in the Volvo 940**. This document is extracted from the two user-supplied original PDFs, read on 2026-10-27:

- `mspower_ShemV1.2.pdf` — 2-page `MegaSquirt Power Distribution Board - Bowling & Grippo` schematic, title block **V1.2** (2002-05-01).
- `mspower_LayoutV1.2.pdf` — 3-page layer artwork (`Mspower.top`, `Mspower.bot`, `Mspower.sst`), dated 2002-06-09. Despite filename `V1.2`, the board silkscreen in the layout visibly says **`MS Power/Relay V1.1`**. The V1.1/V1.2 relationship is **not resolved**, and the PDF is not proof of the version mounted in the car.

These PDFs were supplied to the project conversation; the original binary PDFs are **not committed** in this repository. Do not silently substitute another Internet schematic.

## Documented external supply connections (schematic page 1)

| Identifier | Source label | Source-documented function | Current Volvo hookup |
|---|---|---|---|
| X1 | `+12 Battery (Unswitched)` | Battery +12V unswitched input; passes through F1 to board net `12U` | **R (2026-10-27):** permanent battery feed via a separate **30 A fuse located nearer the battery**, upstream of the MS box |
| X2 | `+12 Battery (Switched)` | Switched +12V input / `12S` | **R (2026-10-27):** wired as switched +12V |
| X3 | `Engine Ground` | Ground input | **R (2026-10-27):** wired as engine ground |

X1/X2/X3 are the schematic's named power/ground inputs and should not be conflated with the twenty `JP1` signal/connector positions below.

**External 30 A fuse ≠ board F1.** The user confirms a separate 30 A fuse on the permanent feed near the battery, before X1. The B&G PDF specifies an application-dependent main F1 and illustrates 20 A (ATO); the *actual* F1 fuse value/type, cable gauge and suitability of the external 30 A protection are still unknown. Do not claim the 30 A fuse proves adequate conductor protection or avoids downstream voltage drops.

## ECU screw-terminal junction as installed (user-reported 2026-10-27)

The **DIY DC idle H-bridge positive and ground leads land on the respective power/ground screw terminals on the ECU itself**, not on a screw terminal on the relay board. The supply and ground wires originate from the MS relay box and reach those ECU screw terminals; **both ECU and H-bridge therefore share the same terminals and incoming feed/return cables at that junction**.

This resolves the junction location but **does not prove which internal relay-board net or protective element** powers the ECU screw positive terminal, nor the complete ground path within the box. The reference schematic's `K1 → CB2 → 12 RAW` path is a hypothesis to confirm against the actual ECU feed before attributing drop/trip behavior to CB2. Keep the H-bridge common-impedance and possible polyfuse thermal-trip mechanisms as testable hypotheses rather than established engine shutdown causes.

## JP1 — 20-terminal screw block (schematic page 1)

Numbers and names below follow the PDF's **`Terminal Block Definition`**, preserving the document's terminology. The two Injector 2 and two Injector 1 positions are separate physical positions even when labelled alike.

| JP1 position | PDF function | Actual connected load/wire in car |
|---:|---|---|
| 1 | Injector 2 | Unconfirmed |
| 2 | Injector 2 | Unconfirmed |
| 3 | Injector 1 | Unconfirmed |
| 4 | Injector 1 | Unconfirmed |
| 5 | Fuel Pump | Unconfirmed |
| 6 | Fast Idle | Unconfirmed |
| 7 | S1 | Unconfirmed |
| 8 | S2 | Unconfirmed |
| 9 | S3 | Unconfirmed |
| 10 | S4 | Unconfirmed |
| 11 | S5 | Unconfirmed |
| 12 | Vref | Unconfirmed |
| 13 | TPS | Unconfirmed |
| 14 | TPS Return | Unconfirmed |
| 15 | Tach/Ignition | Unconfirmed |
| 16 | Air Temp | Unconfirmed |
| 17 | Air Temp Return | Unconfirmed |
| 18 | Coolant | Unconfirmed |
| 19 | Coolant Return | Unconfirmed |
| 20 | O2 | Unconfirmed |

**Important:** The JP1 table describes a 2002 MegaSquirt-era interface. The installed ECU is now Mega144H7/EpicEFI, so the actual purpose of any wire currently landed at a numbered JP1 position must be supplied by the user or verified by a contemporary connection record. Do not interpret `S1`–`S5`, `Tach/Ignition`, etc. as current ECU pin assignments.

## JP2 — injector +12V distribution (schematic page 1)

- Four-position terminal block labelled `+12 Supply For Injectors`.
- F3 and F4 are two separate injector-feed fuse branches in the schematic; it labels both as **10 A (ATO)**.
- The layout silkscreen labels F3 as **`INJ2 Fuse`** and F4 as **`INJ1 Fuse`**.
- This source documents **two fused injector power branches**, not four independently fused injector channels. Whether the current sequential installation retains this arrangement is unconfirmed.

## Relay, fuse and circuit-breaker identities

| Ref | PDF name / schematic nominal marking | Source-documented connection or function | Actual installed |
|---|---|---|---|
| F1 | Main fuse; **20 A (ATO)** shown | Unswitched supply → net `12U`. Schematic says value depends on total load/application | Unconfirmed; do not adopt 20 A as required rating |
| K1 | ECU Power Relay (SPDT symbol) | Controls `12 RAW` branch; downstream CB2 | Unconfirmed |
| CB2 | RXE105 polyfuse in schematic; designer BOM also permits RXE110 | Series protection between K1-fed ECU path and `12 RAW` | **R (2026-10-27): original/stock internal circuitry, never intentionally modified or bypassed**. Presence is expected from source design, but exact fitted marking and live output path remain unmeasured |
| K2 | Fuel Pump Relay (SPDT symbol) | Supplies fuel-pump branch controlled by ECU `FP1` signal; F2 in output path | Unconfirmed |
| F2 | Fuel-pump fuse; **10 A (ATO)** shown | K2-to-fuel-pump `FPO` path | Unconfirmed |
| K3 | Fast Idle Relay (SPDT symbol) | Fast-idle relay output; jumper J1 changes output polarity | Unconfirmed usage |
| CB3 | RXE110 polyfuse | Fast-idle branch `FASTIDLE` | Unconfirmed |
| CB1 | RXE110 polyfuse | Present on board/sensor-reference-related branch in schematic | Unconfirmed |
| F3 | Injector 2 fuse; **10 A (ATO)** shown | One injector +12V fused branch | Unconfirmed |
| F4 | Injector 1 fuse; **10 A (ATO)** shown | Other injector +12V fused branch | Unconfirmed |

The physical board is reported to use **MINI fuses**. The PDF schematic's ATO notation therefore must not be assumed to describe the user's installed fuse package or ratings. The three relays reported warm by touch are not proven faulty from that observation alone.

## Stock-board confirmation and CB2 source ratings (user report 2026-10-27)

The user confirms the **MS relay box remains in its stock/internal original form**: no CB2 bypass, removal or deliberate internal power-circuit changes. This upgrades the expected presence of the original polyfuse circuit to **user-reported stock**, not **physically inspected/verified fitted part**. The board's exact manufacturing revision and currently fitted CB2 marking are still unknown.

Source comparison:
- The user-supplied B&G V1.2 schematic labels **CB2 RXE105**, in the ECU `12 RAW` feed following K1.
- The original B&G documentation/BOM explicitly allows **`RXE105 or RXE110`** for the Polyfuse devices. Source: https://www.bgsoflex.com/mspower/mspower.html (bill of materials, `RXE105 or RXE110`). Therefore **do not assign RXE110 or RXE105 ratings to the fitted part as fact**.
- Raychem's RXE-series manufacturer catalog gives **RXE110**, specifically, a 20°C hold rating of **1.10 A**, 20°C trip rating of **2.20 A**, initial 20°C resistance **0.15–0.25 Ω**, and hold rating **0.69 A at 60°C**. Source: https://www.silicon-ark.co.uk/datasheets/polyswitch-rxe-datasheet-raychem.pdf (Raychem RXE catalog, product data/temperature table). These figures are **illustrative reference specifications**, not an assessment of aged installed CB2.

**Fault hypothesis (not a diagnosis):** If the ECU positive screw is supplied from the original board `12 RAW` net, the present DIY DC idle H-bridge—connected to that same ECU positive terminal—adds current through the CB2 path. A relatively low-current-rated PPTC could then contribute to steady voltage loss, heat-related resistance increase, or thermal trip/recovery. The shared PSU and ground screws, relay contacts, solder joints and H-bridge switching noise remain competing explanations for ECU brownouts/shutdowns. The external **30 A battery-feed fuse does not prevent local CB2 operation**.

**Evidence needed to resolve:** identify ECU feed from MS box (source `12 RAW` versus another output), capture normal-operation voltage on both sides of CB2/at ECU without bypassing any protection, assess H-bridge branch and total protected current with rated tools, and relate supply/ground changes to ECU log/brownout data. Never deliberately overload CB2 or provoke shutdown during driving.

## J1 — fast-idle relay jumper (schematic page 2)

The schematic explicitly states:

- `1 & 2`: relay supplies **+12V** to the fast-idle solenoid.
- `2 & 3`: relay supplies **GND** to the fast-idle solenoid.

This is historical *fast-idle relay* functionality, and does not establish wiring for the present Bosch PWM IAC valve or the separate DIY DC idle H-bridge.

## Current-vehicle confirmation — text-first

The source pin names above are **already extracted**; users should not be asked to re-photograph or redraw them. For the real vehicle, ask for simple text answers, accepting `connected`, `unused`, `unknown`, or a destination name:

1. **Completed at user-report level:** X1 permanent +12V through separate upstream 30 A fuse; X2 switched +12V; X3 engine ground. Confirm fuse physical value and wire gauge only if readily available.
2. JP1 positions 1–20: current wire destination/function, if used. Blank/unknown is acceptable.
3. JP2 positions 1–4: present injector power wiring, or any repurposed load.
4. **Stock status confirmed by user:** no deliberate internal modifications/bypasses. Remaining: actual F1–F4 values, exact CB2 marking/revision and use of K1/K2/K3/J1 if readily known.
5. **Completed at user-report level:** ECU and H-bridge share the ECU's own positive and negative screw terminals, fed/returned by cables originating at the MS box. The terminal location is no longer an open question; exact internal MS-box feed/return nets remain unknown.
6. Any bypassed/repurposed connection from Speeduino to Mega144H7.

No cramped-space photographs are required as a blanket condition. A text description can establish a **user-reported installed** wiring map; verified measurements or an existing reliable harness drawing may later raise confidence for a particular fact. Avoid demanding PCB-side physical probing solely to repeat information already established in the PDF.

## Engineering caveats

- PDF source mapping ≠ verified manufactured board revision ≠ current installation. Maintain these three evidence levels separately.
- Never presume the old B&G DB37 pin assignments correspond to the current EpicEFI Mega144H7.
- Protect fuel-pump fail-safe operation, ECU voltage references and motor-current return separation.
- The PDFs alone do not provide today's wire gauge, fuse values, relay condition, electrical loss, current, thermal condition or fault behavior. Those remain measurement/confirmation gates.
