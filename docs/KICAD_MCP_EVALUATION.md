# KiCad MCP evaluation — browser-first F5 (candidate)

Candidate: Seeed-Studio/kicad-mcp-server, pinned to git revision `0b445be8668c00b0d71315e74fa2f180bca686c2` (2026-10-22). Repo package metadata identifies MIT licensing, Python 3.10+, KiCad 9+ and `mcp[cli]>=1.27,<2`, `fastmcp>=3.2,<4`. Review exact license text and every transitive dependency before redistribution.

## What is actually established
- Browser Codespaces has KiCad CLI **9.0.2** and pcbnew **9.0.2** from Debian Trixie, as verified by user in a real Codespace.
- Existing GitHub Actions KiCad startup checks passed; no vehicle schematic or PCB exists.
- Pinned source describes an STDIO MCP server and a silent `python -m kicad_mcp_server` entrypoint. This is NOT evidence it can start in our cloud environments.
- Pinning git source **does not pin PyPI transitive dependency versions**. For long-term reproducibility, generate reviewed lockfile with hashes after proving the runtime.

## Optional installation in Codespaces
```bash
git fetch origin
git switch --track origin/infra/kicad-mcp-smoke
bash scripts/setup-kicad-mcp.sh
.local/kicad-mcp-venv/bin/python scripts/test-kicad-mcp.py
```
The script uses `venv --system-site-packages` so the installed KiCad Python `pcbnew` binding is visible, but this also inherits system Python packages. It installs files under ignored local `.local/`; it must not run automatically on every Codespace launch.

## Acceptance gates
1. Pin source SHA, inspect dependencies, license and startup behavior.
2. Install in a fresh Linux cloud environment and perform a **real STDIO MCP initialize + tools/list** test.
3. Inventory returned tool capabilities; classify read-only versus mutating tools; **do not assume every advertised tool is safe**. The test selects only `list_schematic_components`.
4. Run a read-only tool against a disposable copy of upstream `tests/fixtures/example_schematic.kicad_sch` (pinned 0b445be8; licensed by upstream), require R1 and R2, and verify SHA-256 unchanged. Independent `kicad-cli` netlist/export comparison remains a separate follow-up.
5. Verify no source mutations, no public forwarded port, no token access or unexpected network calls.
6. Only then configure Codex CLI/Cloud MCP discovery and test its agent-driven read-only calls. Codex Cloud and Codespaces have **different** environments: never infer success in one from the other.

## Limits
No vehicle schematic, pinout, netlist, Gerber, BOM or PCB work is authorized by these tests. CI startup is not proof of electrical safety.

## Verification record
- Initial GitHub Actions run `40543131535` **passed**, proving real MCP STDIO initialize and tools/list in an isolated KiCad environment, with no tracked source mutations. This **did not invoke any schematic tool**.
- Follow-up on this PR extends the test to invoke `list_schematic_components` against a disposable copy of a pinned upstream schematic fixture and checks R1/R2 and input hashes. Treat as pending until the workflow completes successfully.
- The sample fixture comes from `Seeed-Studio/kicad-mcp-server/tests/fixtures/example_schematic.kicad_sch` at upstream commit `0b445be8668c00b0d71315e74fa2f180bca686c2`. It is a test artifact, not the Volvo relay-box design.
