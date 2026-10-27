# Codex and KiCad MCP

This directory intentionally does not enable a KiCad MCP server yet.

KiCad MCP requires a **real installed server**, compatible KiCad/Python
dependencies and successful smoke tests; an untested `config.toml` that silently
fails would make tools appear available when they are not.

Once the selected MCP server is pinned and installed in the devcontainer and
Codex Cloud setup, add a project-scoped `config.toml` pointing to that exact
entrypoint, and test `codex mcp list` plus a read-only sample-board query.

Repo guidance for every agent lives in `AGENTS.md`; electrical state remains
in `docs/`; cross-agent memory is EpicWolf once merged.
