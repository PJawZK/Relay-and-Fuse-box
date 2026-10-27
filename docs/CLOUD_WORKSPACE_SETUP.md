# Browser-first workspace — infrastructure baseline

## Core principle
The Git repository owns electrical data and agent memory; cloud environments are disposable execution workers. No circuit-design requirement shall depend on a specific home computer, a permanently-running Codespace, or Windows.

## Codex Cloud (first choice from a work browser)
- Connect the GitHub repository in Codex and start tasks against a branch.
- Configure its environment setup to install the project toolchain. Codex Cloud setup is **not** automatically identical to Codespaces. Run `bash scripts/verify-environment.sh` in each environment.
- Do not assume a remote Codex task has the working state of a Codespace or can operate the native KiCad GUI.
- Avoid secrets in setup scripts, prompts, or EpicWolf memory.

## GitHub Codespaces (interactive browser IDE)
1. Open repository > **Code** > **Codespaces** > **Create codespace** on the infrastructure branch.
2. The repository's `.devcontainer/` builds a Debian Linux environment with KiCad and Node 22.
3. Open Terminal and run `bash scripts/verify-environment.sh`.
4. Commit or push all important work. A Codespace can stop or be deleted while repo history remains.
5. Watch Codespaces storage quotas; installed KiCad libraries consume space even when stopped.

## Version policy
- The initial package-managed environment uses the KiCad version shipped with Debian Trixie (verify with `kicad-cli version`), not an unverified 10.0 image.
- The initial GitHub Actions checks should use a corresponding confirmed KiCad CLI container version.
- Upgrade to KiCad 10 only as a controlled cross-environment migration, after verifying container availability, file compatibility and test results.

## MCP rollout
- Phase 1: KiCad CLI, deterministic artifacts, version check and GitHub Actions.
- Phase 2: add and pin a KiCad MCP implementation *after* proving it can start inside both selected cloud execution environments.
- Phase 3: read-only MCP interrogation on a dummy project, then reviewed schematic editing and rollback tests.
- Do not publish a Codespaces forwarded port to host an unauthenticated MCP server.
- Configuration inside `.codex/config.toml` works only where the Codex runtime trusts and reads project-scoped config; it does not install a server automatically.

## Acceptance criteria before electrical design
- Fresh Codespace builds and reports KiCad/Node/Python versions.
- Codex Cloud setup runs the same smoke checks successfully.
- EpicWolf import is reviewed/merged, tests pass and memory files survive environment recreation.
- PR validation reports its real KiCad version and explicit 'no project files' status when no board exists.
- A disposable KiCad example passes ERC/DRC in *both* cloud environments.
