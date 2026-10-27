# KiCad MCP: actual Codex agent acceptance (F5)

This gate is distinct from the standalone Python MCP test. Both GitHub Actions
and a genuine Codex agent must see the same MCP capabilities. The upstream
server can advertise **mutating** tools: do not interpret its overall registration
as read-only. No vehicle-board edit is authorized.

## Proven
- Candidate `Seeed-Studio/kicad-mcp-server@0b445be8668c00b0d71315e74fa2f180bca686c2`.
- GitHub Actions run `40543131535` passed isolated STDIO initialization/tools-list.
- GitHub Actions run `40543925876` passed isolated STDIO, `list_schematic_components`
  on a disposable upstream fixture (R1 and R2), and unchanged file checks.
- GitHub Actions run `40544532382` passed installation, real MCP fixture query, checked disabled TOML registration, Bash launcher syntax, and tracked-file integrity.\n- These do **not** prove Codex recognizes the MCP registration.

## Codespaces agent test (opt-in)

Check out `infra/kicad-mcp-smoke` with a clean worktree. The installed
Codespace has KiCad 9.0.2 and pcbnew 9.0.2, but MCP venv is separate.

1. Run `bash scripts/setup-kicad-mcp.sh`, then
   `.local/kicad-mcp-venv/bin/python scripts/test-kicad-mcp.py`.
2. Only if both pass, change `enabled = false` to `enabled = true`
   in a local, uncommitted `.codex/config.toml`. Do **not commit** this toggle.
3. Start a new Codex CLI/IDE session in the **trusted repository** and run
   `codex mcp list` or use the IDE MCP servers panel. Confirm the exact server
   appears with no errors. Codex Cloud may not honor that local config.
4. Ask the agent to list tools from `kicad_relay_readonly_test` and invoke
   **only** `list_schematic_components` on a temporary copy of
   `tests/fixtures/mcp-upstream-example.kicad_sch`. It must return R1 and R2.
   Never allow mutating tools or use actual project electrical files.
5. Check `git diff --exit-code`, untracked file inventory, and SHA-256 of
   committed fixture against baseline. Report exact agent/runtime evidence.

## Codex Cloud (separate executor)

Codex Cloud does not access the Codespaces filesystem or its `.local` venv.
Before agent launch, the Codex Cloud environment must provision the same
pinned server and Python venv **in that environment**. The project's MCP
configuration is intentionally disabled by default until this is proven.
The cloud agent must confirm whether project-scoped MCP config is loaded in
its execution mode. Absence of a Codex-provided MCP tool is a test failure,
not permission to substitute a manually scripted `ClientSession` call.

## Security / provenance
- Launcher is STDIO only and requires a local venv, without opening a port.
- Upstream server is third-party code; its tools include capabilities beyond
  read-only inspection. Disable server when not performing the controlled test.
- Project-scoped `.codex/config.toml` only applies to trusted projects, per
  official Codex configuration documentation.
- Real read-only behavior on sample does not prove isolation against malicious
  prompts; tool restrictions need explicit review before enabling it for
  engineering design.
- Source-of-truth data: `docs/ELECTRICAL_INVENTORY.md`,
  `docs/POWER_AND_GROUND_TREE.md`; no design work yet.

Reference: https://learn.chatgpt.com/docs/extend/mcp

## Proposed live Codex acceptance report

A genuine Codex session is still required. In the actual environment, first
show `codex --version`, `codex mcp list`, MCP server state and the exact
project commit. Do not count a direct Python `ClientSession` call as Codex
MCP discovery; that portion was already proven in GitHub Actions.

**Safety prerequisite:** upstream MCP registers editing operations as well as
read-only methods. Since the project config currently enables or disables the
**entire** server, enabling it is only acceptable in an isolated disposable
agent workspace with **no writable real project electrical designs**. A prompt
that says 'do not edit' is not a tool-level read-only restriction. Do not
activate in a workspace holding sensitive or real KiCad design files until a
server-side allowlist or equivalent restriction has been tested.

An acceptance report should contain the native Codex session transcript/evidence,
MCP registration, actual tool call and R1/R2 output, fixture hash before/after,
worktree status, and an explicit separation of Codex Cloud versus Codespaces.
