# Foundation phase gates — no board design yet

Current status (2026-10-27): **infrastructure implementation, unvalidated**.

| Gate | Objective | Definition of done | Status |
|---|---|---|---|
| F1 | EpicWolf installed | Baseline pinned; tests pass; memory/handoff semantics validated in fresh agent sessions | Pending |
| F2 | Browser-only Codespaces | A fresh, 2-core Codespace builds `.devcontainer`, runs the tool smoke checks and resumes from the repo | Configured, not run |
| F3 | Codex Cloud | Environment install documented, tool smoke check passes and a repo PR can be created | Pending |
| F4 | KiCad validation | Known KiCad version, a non-vehicle sample has ERC/DRC pass in Actions and cloud workers | CI configured, untested |
| F5 | KiCad MCP | Server license and dependency audit; STDIO read-only tool roundtrip and agent discovery; no public port | Pending |
| F6 | As-built electrical inventory | Current physical harness / ground tree, values and measurements clearly traced and evidenced | Draft |
| F7 | Requirements | Load currents, fuse coordination, voltage-drop and thermal acceptance targets agreed | Pending |
| F8 | Readiness review | Signed-off documentation / tool results before any vehicle PCB production or installation | Pending |

## Policies
- A successful blank-file CI job is **not** an ERC/DRC design pass.
- Initial cloud toolchain may use KiCad 9 while KiCad 10 availability is investigated; no mixed-version PCB authoring without documented migration.
- Keep physical circuit design off the implementation branch until foundation gates have passed.
- EpicWolf tracks decisions and work history; measurements and current source files remain the electrical authorities.
- Review workflows and inherited settings when integrating third-party agent hooks. Never store credentials in source control.
