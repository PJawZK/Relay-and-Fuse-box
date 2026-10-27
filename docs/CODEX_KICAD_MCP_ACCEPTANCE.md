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

## Live native Codex acceptance — 2026-10-27 (passed)

Evidence was supplied by the user as Codex CLI session JSONL records and reviewed locally. The raw log contains user/session metadata and is intentionally **not committed**. Extracted, non-sensitive evidence:

- Executor: existing browser Codespace `codespaces-995a05`, repository branch `infra/kicad-mcp-smoke`, Git HEAD `31281b9f9b2d04cff6e067f950a1d93cc2c1434d`.
- Agent: **Codex CLI 0.164.0**, authenticated with ChatGPT. Prior screenshot showed `kicad_relay_readonly_test: connected (1 tool)`.
- Native Codex tool discovery yielded exactly `mcp__kicad_relay_readonly_test__list_schematic_components` (no other tool from this server).
- The session includes an actual `McpToolCall` event: server `kicad_relay_readonly_test`, tool `list_schematic_components`, arguments `{}`, status `completed`, `isError: false`.
- Tool result: `R1: 10k`, `R2: 4.7k`, `C1: 100nF`, `U1: ESP32-WROOM-32`, `J1: Conn_01x04`, `R3: 0R`.
- The agent's final response reported no modified files. Independent post-agent `git status --short` was **not supplied**. GitHub Actions separately validated unchanged fixture hashes and no tracked source mutations for the restricted service.
- The Codex runtime invoked the actual server-provided MCP tool, not a stand-alone Python client. **Native Codespaces agent invocation gate: PASS.**

## Acceptance boundaries and next steps

- GitHub Actions run `40549945173` passed on branch commit `31281b9`. Earlier corrected allowlist smoke run `40549444779` passed.
- This closes infrastructure proof for the **fixed-fixture, single-tool read-only façade** and Codespaces-native Codex invocation. It does **not** validate a general-purpose read-only KiCad interface, editing access, Codex Cloud runtime provisioning, automotive design, or manufacturing.
- The user enabled the project config locally; `codex mcp add` also created persistent *user-scoped* registration. After acceptance, run `codex mcp remove kicad_relay_readonly_test` if no longer needed, and restore local `.codex/config.toml` to `enabled = false` without committing the temporary toggle. Keep the actual unrestricted upstream MCP server unavailable to Codex.
- Further KiCad work must stay inside the agreed foundation / electrical-evidence gates. Hardware profiling and vehicle board design remain deferred.
