# Codex Cloud runtime acceptance test — EpicWolf foundation

**Gate:** F1 cross-agent context; no automotive schematic/PCB editing. This is a live-agent test, not a GitHub Actions substitute.

## Requirements
- In Codex Cloud, choose repository `PJawZK/Relay-and-Fuse-box` and source branch `integration/epicwolf-vendored`.
- Use a writable task branch for the report; leave `main` unchanged.
- Node 22, Bash and Git are sufficient. KiCad and MCP are not required for this **memory** test.
- Codex Cloud is a **separate** execution environment. The user's running Codespace and its contents are not automatically accessible.

## Exact Codex Cloud task prompt

> In the Relay-and-Fuse-box repository, read AGENTS.md, .wolf/SHARDS.md, .wolf/STATUS.md, docs/ELECTRICAL_INVENTORY.md, docs/POWER_AND_GROUND_TREE.md and docs/EPICWOLF_AGENT_COMPATIBILITY.md. On the integration/epicwolf-vendored baseline, perform a **read-only** Codex Cloud runtime acceptance test: run `node --version`, `bash scripts/agent-context.sh`, `node .wolf/tools/wolf_guard.js` and `node --test .wolf/tools/wolf_bug.test.js .wolf/hooks/*.test.js`. Record exit statuses and the Git revision. Verify `git diff --exit-code`, `git diff --cached --exit-code`, and that no untracked nonignored files exist. State explicitly whether Codex automatically executed any EpicWolf memory hook (do not infer that from reading files or from successful tests). Write only `docs/validation/CODEX_CLOUD_EPICWOLF_RUN.md` containing the observed results and evidence; commit that report on a new task branch and create a PR. Do not modify .wolf, schematic, board files, or electrical requirements. Do not manufacture success if execution is unavailable.

## Pass criteria
1. Actual Codex Cloud agent can read authoritative source files and run the neutral context command with exit code 0.
2. Vendored tests and guard pass, with exact counts and revisions reported.
3. No mutation to existing source/memory files from read-only checks.
4. Report explicitly distinguishes **agent reads instructions** from **native lifecycle hook integration**. Automatic capture remains *unverified* until an event-driven integration test exists.
5. A PR containing the report is accessible from an ordinary browser (without local tools).

## Codespaces comparison
Inside the browser Codespace, switch/check out the EpicWolf integration branch in a clean working tree (or open another Codespace) and run:

```bash
bash scripts/agent-context.sh
node --test .wolf/tools/wolf_bug.test.js .wolf/hooks/*.test.js
git status --short
```

Compare status/decision files with the Codex Cloud report. Versions can differ, but their committed memory and conclusions must match.

## Boundaries
- Do not expose a KiCad MCP server to the internet as part of this test.
- GitHub Actions passing does not establish live Codex Cloud integration.
- No code that writes to actual vehicle electrical outputs is authorized.
