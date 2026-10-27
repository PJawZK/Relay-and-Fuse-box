# STATUS — Relay-and-Fuse-box

_Updated 2026-10-27_

## 🚀 Next quest

- Use `docs/ORIGINAL_RELAY_BOARD_PDF_MAP.md` (transcribed from the actual two supplied PDFs) and request **text confirmation** of current X1–X3, JP1/JP2 uses and ECU/H-bridge shared power/ground terminals. Photos are not a prerequisite in the cramped installation. Then plan targeted voltage/current tests; F6/F7 remain open, no schematic/PCB yet.

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
