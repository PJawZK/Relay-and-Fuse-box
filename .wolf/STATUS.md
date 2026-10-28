# STATUS — Relay-and-Fuse-box

_Updated 2026-10-27_

## 🚀 Next quest

- **2026-10-28 immediate safety gate:** User proposes testing original LH20 fuel-pump relay stage but flags possible abandoned pump conductors near tank. **DO NOT energize LH20/86/2 or bridge 30→87/2 until original tank feed(s) are identified, de-energized, isolated from the tank/pump connector and secured.** The original LH relay is combined, not pump-only: LH21 main section and LH20 pump section in same module. 1995 OEM reference identifies C93 4-pin left rear wheel housing luggage area; original pink pump conductor (verify 1997 actual). See `docs/OEM_FUEL_PUMP_RELAY_AND_TANK_WIRE_ISOLATION.md`. H-bridge remains unrelocated; factory relay feed still shows prior 0.87–1.25V battery+ to LH4 drop.


- **2026-10-28 newest direct test:** battery+ (red) to original LH pin4 (black) measured **1.25 V**, gradually ~**0.87 V**, then rose slowly again while original LH21 main relay commanded ON; not stable. This verifies a positive feed path voltage difference, **not necessarily a bad relay contact**, because LH4 is a permanent feed rather than 87/1 switched output. Volvo 700/900 original fuel relays are known to suffer cracked solder, bad contacts and socket crimps, so first compare a confirmed **identical** known-good replacement relay with matched OFF/ON battery+→LH4 readings; pin20 pump-section test is NOT another independent relay. If testing a separate OEM relay circuit, first verify it has a truly independent feed and a safe free socket (old M90-unused overdrive is only a conditional candidate). No H-bridge hookup pending supply diagnosis; see `docs/LH24_CONNECTOR_RELAY_VERIFICATION.md`.


- **Latest measured battery baseline (2026-10-28):** OEM LH relay OFF battery 12.38 V; relay ON battery 12.34 V. In same activated test LH pin 4 ~11.25 V and LH pin 9 11.17–11.25 V relative to chassis, a ~1.09 V *apparent* pin4/battery difference while battery drops only 0.04 V. Next test direct DC differential battery+ to pin4 with relay on (and ground reference offset), not a relay-contact failure assumption. H-bridge relocation still uninstalled; avoid connecting it to old feed before source health is measured.


- **2026-10-28 confirmed test (user):** LH pin 21 released ~12.38 V (consistent with coil pull-up), manual ground command activates the abandoned OEM main EFI relay (audible click), and pin 9 now reads 11.17–11.25 V while battery measured 12.38 V. **Apparent 1.13–1.21 V gap**, not yet a same-state isolated relay contact drop. Before reusing the original relay for H-bridge, compare battery/LH pin 4/LH pin 9 with same ground and relay activated; inspect factory feed versus relay contacts/output only after narrowing. Do not load H-bridge until checked. See `docs/LH24_CONNECTOR_RELAY_VERIFICATION.md`.


- **2026-10-27 architecture correction:** No *original Volvo factory EFI* wires, relays or fuses are used by current EpicEFI. All EFI wiring, relays and fuses were separately installed (including aged aftermarket MS relay board). Original LH injection relay/socket positions can be assessed for reuse. Do **not** imply factory Volvo injection relay remains required for new EFI/fuel pump. See `docs/VOLVO_FACTORY_RELAY_REUSE_RESEARCH.md`.
- **Next non-invasive test (user proposal):** before cutting beneath original Volvo fuse box, inspect/test the now-unused LH2.4 ECU connector. Source candidate pins: 20 original pump relay coil low-side (86/2), 21 main fuel-system coil low-side (86/1), 35 ignition terminal 15, 4 constant battery 30, 9 main relay output; confirm 1997 pinout. With LH ECU gone, **20/21 do not generate coil-ground trigger**, and any released-coil +12V reading is not an ON command. See `docs/LH24_CONNECTOR_RELAY_VERIFICATION.md` for safe OFF/RUN/START voltage and isolated continuity checks.
- **Planned, not installed:** move DC idle H-bridge off shared ECU supply/ground screws to separately fused, switched factory relay branch. Reused OEM 2/23 turbo injection relay is a candidate pending coil feed, run/start, downstream loads and safe actuator loss-of-power behavior. Do not tap currently active new pump output or ECU `12 RAW` branch.
- **X1/X2/X3 and existing ECU/H-bridge junction confirmed by user text:** X1 permanent through external upstream 30 A fuse, X2 switched, X3 engine ground; MS box cables feed ECU +/ground screw terminals currently shared by H-bridge. Next map the candidate OEM relay and re-log supply under matched normal operating conditions. F6/F7 remain open; no schematic/PCB.

## Context

- GitHub repository: PJawZK/Relay-and-Fuse-box. This is a **foundation/infrastructure** project phase; **no schematic or PCB design** is authorized yet.
- Browser-first workflow: Codex Cloud is intended for agent tasks; Codespaces for browser IDE; GitHub Actions for independent tests.
- KiCad 9.0.2 and pcbnew 9.0.2 were verified in a user-created Codespace on 2026-10-27. KiCad 10 remains unvalidated. Pinned KiCad MCP fixture-only read-only interface and native Codespaces Codex CLI 0.164.0 invocation passed on 2026-10-27.
- Current and proposed power and ground paths: docs/ELECTRICAL_INVENTORY.md and docs/POWER_AND_GROUND_TREE.md. Treat all unknown pins, fuses and measured branch currents as unresolved.
- KiCad MCP infrastructure PR #4 merged into main as 6d1de6e5; fixture-only allowed tool, edit-call rejection and real Codex native invocation verified. No schematics or PCB designed.
- Infrastructure PR #1 (browser-first environment) merged into main as 58f4f166. EpicWolf PR #2 merged into main as 03d08432. F1 read-only shared-memory availability is validated; automatic Codex memory hooks remain unverified.
- Codex Cloud F1 executed successfully on 2026-10-27: Node 22.23.4, context and guard clean, 31/31 tests, no source/memory mutations. Evidence: docs/validation/CODEX_CLOUD_EPICWOLF_RUN.md (PR #3 merged into integration branch). Automatic hooks were not observed.
- Browser Codespaces F1 executed successfully on 2026-10-27 at integration revision 17dbc56: context and guard clean, 1 valid bug record and 31/31 tests. User supplied actual terminal output; final user-confirmed `git status --short` after tests was empty.
- EpicWolf hooks in .claude/settings.json are Claude Code-specific; Codex receives repo instructions via AGENTS.md and must explicitly run the repo's status/guard commands until native hook compatibility has been proven.

## Electrical closure evidence

- Circuit coverage ledger: `docs/ELECTRICAL_EVIDENCE_LEDGER.md` (E01–E20). All physical paths and branch currents remain open unless directly verified.
- Repeatable measurement fields and safe load-state checklist: `docs/ELECTRICAL_MEASUREMENT_WORKSHEET.md`.
- Foundation gates were reconciled to verified CI/Codespaces evidence in `docs/FOUNDATION_GATES.md`: F1/F5 limited passes, F2–F4 partial/limited, F6–F8 still open.
- Priority electrical uncertainty: ECU and DC idle H-bridge feed/return share a screw terminal by user report. This is a coupling hypothesis, not an established shutdown cause.

- The two original B&G PDFs were reviewed: schematic title block V1.2; layout PDF filename V1.2 but **silkscreen says V1.1**. Preserve this source revision difference rather than assuming installed board identity.

- **2026-10-27 user confirmation:** internal MS relay-box circuitry is stock/original; CB2 was not deliberately removed or bypassed. Original B&G BOM allows RXE105 **or** RXE110, despite schematic CB2 label RXE105; fitted marking remains unknown.
- Potential mechanism only: B&G source schematic ECU feed passes CB2 RXE105. If installed output to shared ECU/H-bridge screw actually traverses CB2, PWM load could cause voltage loss/PTC thermal trip; this is not established and must be distinguished from shared return impedance or other failures. Do not bypass protective components.

- Previous October 26 idle-log analysis (archived evidence; raw ZIP not rematerializable here) found ECU VBatt minimum ~13.41 V during calm 590–605 s, ~10.67 V during aggressive DC PWM 650–660 s; <10 V by 660.78 s, logged IGN loss 661.20 s and RPM zero 662.75 s. Later stops 716.39 s and 1725.8 s; final stop had near-zero outer D, so H-bridge D activity is not established as universal cause. Full detail in `docs/ELECTRICAL_EVIDENCE_LEDGER.md`.

- Old chats 2025-09-14 and 2026-02-06 discuss user-uploaded `Volvo 940 (1995) Wiring Diagrams - Copy.pdf` and factory relay candidates. Exact original PDF bytes not accessible in this Project on 2026-10-27; matching public TP 3908032/TP 3908202 document index found, but don't claim byte identity or full 1997 model equivalence. The old advice that OEM 2/23 **must remain** has been superseded by user clarification.
