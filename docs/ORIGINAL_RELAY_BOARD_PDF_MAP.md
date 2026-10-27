# Bowling & Grippo MegaSquirt power/relay board — PDF reference terminal map

**Reference status:** Historical/source-documented, **not yet verified as the exact PCB revision or as-connected installation in the Volvo 940**. This document is extracted from the two user-supplied original PDFs, read on 2026-10-27:

- `mspower_ShemV1.2.pdf` — 2-page `MegaSquirt Power Distribution Board - Bowling & Grippo` schematic, title block **V1.2** (2002-05-01).
- `mspower_LayoutV1.2.pdf` — 3-page layer artwork (`Mspower.top`, `Mspower.bot`, `Mspower.sst`), dated 2002-06-09. Despite filename `V1.2`, the board silkscreen in the layout visibly says **`MS Power/Relay V1.1`**. The V1.1/V1.2 relationship is **not resolved**, and the PDF is not proof of the version mounted in the car.

These PDFs were supplied to the project conversation; the original binary PDFs are **not committed** in this repository. Do not silently substitute another Internet schematic.

## Documented external supply connections (schematic page 1)

| Identifier | Source label | Source-documented function | Current Volvo hookup |
|---|---|---|---|
| X1 | `+12 Battery (Unswitched)` | Battery +12V unswitched input; passes through F1 to board net `12U` | Unconfirmed |
| X2 | `+12 Battery (Switched)` | Switched +12V input / `12S` | Unconfirmed |
| X3 | `Engine Ground` | Ground input | Unconfirmed |

X1/X2/X3 are the schematic's named power/ground inputs and should not be conflated with the twenty `JP1` signal/connector positions below.

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
| CB2 | RXE105 polyfuse | Series protection between K1-fed ECU path and `12 RAW` | Unconfirmed |
| K2 | Fuel Pump Relay (SPDT symbol) | Supplies fuel-pump branch controlled by ECU `FP1` signal; F2 in output path | Unconfirmed |
| F2 | Fuel-pump fuse; **10 A (ATO)** shown | K2-to-fuel-pump `FPO` path | Unconfirmed |
| K3 | Fast Idle Relay (SPDT symbol) | Fast-idle relay output; jumper J1 changes output polarity | Unconfirmed usage |
| CB3 | RXE110 polyfuse | Fast-idle branch `FASTIDLE` | Unconfirmed |
| CB1 | RXE110 polyfuse | Present on board/sensor-reference-related branch in schematic | Unconfirmed |
| F3 | Injector 2 fuse; **10 A (ATO)** shown | One injector +12V fused branch | Unconfirmed |
| F4 | Injector 1 fuse; **10 A (ATO)** shown | Other injector +12V fused branch | Unconfirmed |

The physical board is reported to use **MINI fuses**. The PDF schematic's ATO notation therefore must not be assumed to describe the user's installed fuse package or ratings. The three relays reported warm by touch are not proven faulty from that observation alone.

## J1 — fast-idle relay jumper (schematic page 2)

The schematic explicitly states:

- `1 & 2`: relay supplies **+12V** to the fast-idle solenoid.
- `2 & 3`: relay supplies **GND** to the fast-idle solenoid.

This is historical *fast-idle relay* functionality, and does not establish wiring for the present Bosch PWM IAC valve or the separate DIY DC idle H-bridge.

## Current-vehicle confirmation — text-first

The source pin names above are **already extracted**; users should not be asked to re-photograph or redraw them. For the real vehicle, ask for simple text answers, accepting `connected`, `unused`, `unknown`, or a destination name:

1. X1, X2, X3: actual supply/ground source.
2. JP1 positions 1–20: current wire destination/function, if used. Blank/unknown is acceptable.
3. JP2 positions 1–4: present injector power wiring, or any repurposed load.
4. K1/K2/K3, F1–F4, J1: whether installed and used as the reference would suggest; record actual markings only when readily available.
5. ECU main + and ground, and DIY H-bridge + and ground: clarify *which physical screw terminals* are shared and whether these are located on the relay box or near the ECU.
6. Any bypassed/repurposed connection from Speeduino to Mega144H7.

No cramped-space photographs are required as a blanket condition. A text description can establish a **user-reported installed** wiring map; verified measurements or an existing reliable harness drawing may later raise confidence for a particular fact. Avoid demanding PCB-side physical probing solely to repeat information already established in the PDF.

## Engineering caveats

- PDF source mapping ≠ verified manufactured board revision ≠ current installation. Maintain these three evidence levels separately.
- Never presume the old B&G DB37 pin assignments correspond to the current EpicEFI Mega144H7.
- Protect fuel-pump fail-safe operation, ECU voltage references and motor-current return separation.
- The PDFs alone do not provide today's wire gauge, fuse values, relay condition, electrical loss, current, thermal condition or fault behavior. Those remain measurement/confirmation gates.
