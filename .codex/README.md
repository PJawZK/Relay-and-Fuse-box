# Codex and KiCad MCP

This project contains an opt-in, **disabled** Codex MCP candidate in
`.codex/config.toml`. It points to `scripts/run-kicad-mcp.sh`, which launches
the pinned server from a local Python virtual environment. It **never**
installs packages, starts a network listener, or accesses vehicle hardware.

## Verified
- A Linux container installed the pinned MCP candidate and completed a
  genuine STDIO handshake and tool list.
- A follow-up isolated test invoked `list_schematic_components` on an
  upstream example and confirmed R1/R2 and unchanged fixture bytes.
- GitHub Actions runs: 40543131535 and 40543925876.

## Still unverified
- A live Codex agent launching MCP from a trusted project and selecting the
  actual tool. Neither Python tests nor a present config file prove that.
- A separate Codex Cloud executor provisioning and using the server.
- Restricting **all** mutating upstream KiCad tools. Keep the server disabled
  by default, and grant no access to real electrical designs.

Read `docs/CODEX_KICAD_MCP_ACCEPTANCE.md` for the controlled opt-in test,
and `docs/KICAD_MCP_EVALUATION.md` for the candidate's pin and provenance.
