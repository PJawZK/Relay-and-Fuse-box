# Agent-to-KiCad connection research — 2026-10-27

## Decision
Use **repository-first agent execution**, with two validated target environments:
1. Codex CLI or IDE in GitHub Codespaces, using a local STDIO KiCad MCP server.
2. Codex Cloud in its own prepared environment, using KiCad CLI first and MCP where supported/tested.

Do **not** require ChatGPT web to connect directly to a Codespace's forwarded port. GitHub repository files are the source of truth; MCP is runtime-specific.

## Verified documentation findings
- Codex CLI/IDE supports local STDIO and Streamable HTTP MCP; project-scoped `.codex/config.toml` works for trusted projects. Source: https://learn.chatgpt.com/docs/extend/mcp
- Seeed Studio KiCad MCP documents local Python STDIO invocation: `python -m kicad_mcp_server`. Test pcbnew import and tool discovery before relying on full capability. Source: https://github.com/Seeed-Studio/kicad-mcp-server
- GitHub Codespaces private forwarded ports require GitHub authentication. Public ports permit unauthenticated internet access and must **never** expose board-editing MCP endpoints. Source: https://docs.github.com/en/codespaces/reference/security-in-github-codespaces
- Codespaces stop after inactivity, usually 30 minutes default. Thus they are NOT always-on MCP endpoints. Source: https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle
- ChatGPT custom MCP supports remotely reachable server connections under account/workspace entitlement restrictions; full write actions are not universally available on personal plans. Source: https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt
- Codex Cloud tasks use isolated prepared environments and can run repo commands, but are not the same running Codespace. Source: https://help.openai.com/en/articles/20001545-using-codex-cloud
- GitHub Actions validation remains independent and requires no persistent Codespace.

## Connection matrix
| Calling agent | KiCad execution | Technical connection | Status |
|---|---|---|---|
| Codex CLI within Codespace | Same Codespace | STDIO MCP | Documented feasible; untested here |
| VS Code agent within Codespace | Same Codespace | Extension-specific MCP | Documented feasible; untested here |
| Codex Cloud task | Its own cloud environment | CLI/tools; MCP only if configured | Documented feasible for tool execution; untested KiCad |
| ChatGPT web + GitHub connection | Changes checked into GitHub | GitHub tools | Working for docs/repo edits; not remote KiCad MCP |
| ChatGPT web + Codespace | Codespace remotely | Custom MCP via HTTPS/tunnel and plan entitlement | Not adopted |
| GitHub Actions | Ephemeral runner/container | CLI | Workflow committed; first run not validated |

## Proposed infrastructure tests (before board creation)
1. Pin compatible KiCad installation and MCP server revision in a devcontainer. Test installation and Python bindings.
2. Run a trivial *non-vehicle* example schematic through KiCad CLI ERC/netlist export and invoke one read-only MCP tool using Codex CLI.
3. Repeat CLI validation in Codex Cloud task, with no assumption it sees Codespaces' state.
4. Confirm EpicWolf hooks actually run in selected agent environment; Codex integration may require explicit wiring, separate from Claude hooks.
5. Generate a validation report in GitHub Actions and confirm workflow startup and container tag exists.
6. Confirm the repo restores tool versions and memory state in a newly-created disposable Codespace.
7. Require human review for any generated electrical design. No live vehicle connections or manufactured PCB from this test.

## Security/operations
- Local STDIO MCP is preferred; do not expose unprotected MCP on public forwarded ports.
- Store credentials in platform secrets, not in repository or EpicWolf memory.
- MCP server tools should start read-only until changeset / rollback / approval workflows are proven.
- Stop idle Codespaces; do not make availability of the KiCad agent depend on a running paid VM.
- Repository-wide instructions live in AGENTS.md; tool installation is an environment concern.
