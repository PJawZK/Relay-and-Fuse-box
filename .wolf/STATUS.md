# STATUS — Relay-and-Fuse-box

_Updated 2026-10-27_

## 🚀 Next quest

- Validate Codex/Codespaces access to the committed EpicWolf memory without assuming Claude-only hooks run in Codex. Acceptance: an explicit, read-only project-status command succeeds in CI and a fresh Codespace; shared docs and memory distinguish reported wiring from physically verified evidence.

## Context

- GitHub repository: PJawZK/Relay-and-Fuse-box. This is a **foundation/infrastructure** project phase; **no schematic or PCB design** is authorized yet.
- Browser-first workflow: Codex Cloud is intended for agent tasks; Codespaces for browser IDE; GitHub Actions for independent tests.
- KiCad 9.0.2 and pcbnew 9.0.2 were verified in a user-created Codespace on 2026-10-27. KiCad 10 and KiCad MCP are not yet validated.
- Current and proposed power and ground paths: docs/ELECTRICAL_INVENTORY.md and docs/POWER_AND_GROUND_TREE.md. Treat all unknown pins, fuses and measured branch currents as unresolved.
- Infrastructure work: draft PR #1 infra/browser-first-foundation. This EpicWolf integration is draft PR #2, separate from electrical work.
- EpicWolf hooks in .claude/settings.json are Claude Code-specific; Codex receives repo instructions via AGENTS.md and must explicitly run the repo's status/guard commands until native hook compatibility has been proven.
