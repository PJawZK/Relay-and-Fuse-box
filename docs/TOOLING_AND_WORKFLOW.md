# KiCad automation and agent-memory adoption plan

## Objective
Make KiCad 10 design reproducible on Linux without requiring a Windows-only PDM configuration program. Keep power distribution passive. Keep safety decisions human-reviewed.

## Phase A — deterministic foundation
- Require KiCad 10, kicad-cli and Python with compatible pcbnew bindings on developer machines.
- Define CI to run `kicad-cli sch erc` and `kicad-cli pcb drc` on committed project files; fail on new unapproved errors.
- Also export netlist, PDF schematic, Gerbers/drill and BOM only as non-production review artifacts.
- Add Python checks for mandatory fuse on each load, relay footprint/pin mapping, short-circuit isolation, and connector-current/wire-rating worksheets. These are design-specific checks to implement, not features currently present.

## Phase B — AI-assisted editing
- Consider `Seeed-Studio/kicad-mcp-server` first for inspecting net connectivity and drawings. It warns schematic edits are experimental.
- Evaluate `nevenfo/kicad-agentic-mcp` in a disposable test branch for guarded editing; assess its AGPL licensing before integration.
- Agents can propose placements/wiring but must not self-certify DRC, electrical robustness, temperature or fail-safe behavior.
- No automated release of manufacturing outputs; required sign-off on schematic, layout, BOM, connectors, automotive transient and thermal tests.

## EpicWolf evaluation (ggurov/epicwolf)
- This is a modified OpenWolf template with vendored Claude Code hooks, shard-based memory and per-session handoffs, Node.js 20+ runtime, and AGPL-3.0 licensing.
- Useful for tracking circuit decisions, failed tests, pin assignment changes, and multi-agent edits. Not a PCB editor, circuit simulator or electrically authoritative design review.
- Pilot in a branch with source attribution and exact upstream commit pinned; do not blindly overlay its `.claude/settings.json` on existing agent configuration.
- Verify hooks on each intended agent (Codex, Claude Code, etc.). README states shipped hooks are wired for Claude Code; integration with others requires setup.
- Preserve original license notices and review distribution implications before vendoring code.
- Alternative if hooks prove too invasive: adopt only a lightweight `docs/decisions/`, `docs/tests/`, `docs/handoffs/` file convention without importing runtime hooks.

## First technical design milestones
1. Existing-board real-world schematic/wiring audit (not merely the 2002 reference).
2. Segment voltage-drop and current tests across hot/cold load conditions.
3. Power-tree and ground-tree diagram, protection coordination and fault matrix.
4. Symbol/footprint selection for Micro ISO relays, fuses and serviceable terminals.
5. Concept schematic and automated ERC/DRC.
