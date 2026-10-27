# EpicWolf agent compatibility — review before merge

## Imported baseline
Pinned fork: ggurov/epicwolf at `e2d446b76b97a2f88a41f261a5796964dc3df68a`.

- Native hooks included in `.claude/settings.json` are Claude Code event handlers (`SessionStart`, `PreToolUse`, `PostToolUse`, etc.).
- These event handlers are **not automatically loaded by Codex CLI/Cloud or ChatGPT web**, even when working in the same repository.
- ChatGPT/GitHub can read the committed memory, but cannot invoke the local hook runtime without an associated agent-execution environment.
- `AGENTS.md` is the agent-neutral instruction entrypoint. `scripts/agent-context.sh` explicitly prints status and checks memory integrity, with no hook reliance.

## Read-only validation
```bash
bash scripts/agent-context.sh
node .wolf/tools/wolf_guard.js
node --test .wolf/tools/wolf_bug.test.js .wolf/hooks/*.test.js
```
The first command requires `git`, Bash and Node 20+. It reads from the checkout and does not intentionally mutate any tracked source. The Claude runtime should separately test hook event dispatch before we declare its automatic capture usable.

## Planned Codex compatibility phases
1. **Read-only context** from AGENTS.md, .wolf/STATUS.md, cerebrum and ledger.
2. **Guarded write commands** for explicit decisions and bug logs using the upstream shard protocol; code review confirms changes before merge.
3. Only after proving reliable operation, consider native Codex hooks/bridge where supported by its currently installed runtime.

Avoid claiming automatic memory capture without an actual Codex event test. The repo is authoritative regardless of which runtime opens it.

## Compatibility caution
The imported `.wolf/config.json` includes platform features not used by this project (cron daemon, dashboard, design quality settings), and inherited exclude patterns include `hardware`. They must not be interpreted as active services; hardware source remains authoritative in Git and must not be excluded from project reviews. Further adaptation should deliberately limit optional services and scan policies after observing real tool behavior.

## Review gate
- Inspect third-party hook commands and source behavior before allowing interactive hooks to run.
- Keep the existing `AGENTS.md` contract in force.
- Unit tests of the upstream hooks alone do not establish Codex runtime integration or safe read/write behavior in a vehicle project.
