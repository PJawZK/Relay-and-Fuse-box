# KiCad MCP: actual Codex agent acceptance (F5)

This gate is distinct from the standalone Python MCP test. Both GitHub Actions
and a genuine Codex agent must see the same MCP capabilities. The upstream server advertises **mutating** tools, so Codex's project launcher now deliberately starts a **separate fixture-only façade** exposing exactly one read-only method. The unrestricted upstream server is used only in isolated CI. No vehicle-board edit is authorized.

## Proven
- Candidate `Seeed-Studio/kicad-mcp-server@0b445be8668c00b0d71315e74fa2f180bca686c2`.
- GitHub Actions run `40543131535` passed isolated STDIO initialization/tools-list.
- GitHub Actions run `40543925876` passed isolated STDIO, `list_schematic_components`
  on a disposable upstream fixture (R1 and R2), and unchanged file checks.
- GitHub Actions run `40544532382` passed installation, real MCP fixture query, checked disabled TOML registration, Bash launcher syntax, and tracked-file integrity.\n- GitHub Actions run `40549444779` **passed** on commit `719b7ad`: launcher resolves path independent of Git ownership, fixture-only tool is registered and callable, unregistered edit operation is rejected, fixture remains unchanged, and no tracked files changed.\n- These do **not** prove Codex recognizes the MCP registration.

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
   **only** `list_schematic_components` **without arguments**. The façade reads the fixed committed
   `tests/fixtures/mcp-upstream-example.kicad_sch` and should return R1 and R2.
   The agent must confirm that **no editing tools are registered**. Do not use actual project electrical files.
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
- Launcher is STDIO only and requires a local venv, without opening a port. The launcher starts `scripts/kicad-mcp-fixture-only.py`, **not** the unrestricted upstream server.
- The façade imports the upstream schematic parser but registers **only** one fixture-bound, no-argument read tool. MCP editing methods are not registered or callable.
- CI exercises a hostile `create_project` call and requires rejection; it also confirms unchanged fixture bytes.
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

**Safety prerequisite:** use only the fixture-only façade. The full upstream MCP server is not authorized for Codex. Only enable the project's disabled config locally after the allowlist CI passes. The façade's tool has no file-path input, so agents cannot point it at the real electrical designs. A prompt
that says 'do not edit' is not a tool-level read-only restriction. Do not
activate in a workspace holding sensitive or real KiCad design files until a
server-side allowlist or equivalent restriction has been tested.

An acceptance report should contain the native Codex session transcript/evidence,
MCP registration, actual tool call and R1/R2 output, fixture hash before/after,
worktree status, and an explicit separation of Codex Cloud versus Codespaces.

## Next gate — native Codex agent (not yet executed)

In a trusted **disposable** Codespace/agent workspace, use this checklist:

1. Verify branch `infra/kicad-mcp-smoke`, an empty `git status --short`, and `kicad-cli version`.
2. Run `bash scripts/setup-kicad-mcp.sh` and `.local/kicad-mcp-venv/bin/python scripts/test-kicad-mcp-allowlist.py`.
3. Change `enabled = false` to `enabled = true` in the **local, uncommitted** `.codex/config.toml`, then start a new Codex session. This is only for the fixture-only server; never enable the full upstream server.
4. Inspect the Codex client's *actual* MCP registration; then have **the Codex agent** invoke `list_schematic_components` without arguments, proving it returns R1/R2. Running the Python test again does not satisfy this gate.
5. Restore `enabled = false`, check worktree and fixture SHA-256, and save a report with the Codex version, evidence, and observed limitations. **Do not claim Codex Cloud and Codespaces share one environment**.

The above gate is pending until a real agent session executes it. Keep this PR in draft until that outcome is reviewed.
