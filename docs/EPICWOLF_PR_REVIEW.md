# EpicWolf PR #2 review — 2026-10-27

## Reviewed state
- Upstream pinned: `ggurov/epicwolf@e2d446b76b97a2f88a41f261a5796964dc3df68a`.
- 57 initial vendor files imported, upstream license retained in `EPICWOLF-LICENSE`.
- The imported `.claude/settings.json` consists of Claude Code lifecycle/tool hooks invoking Node scripts under `.wolf/hooks/` and `.wolf/tools/bootstrap.js`. These hooks have not been exercised by a live Claude session.
- **Automatic Codex memory hooks are NOT established.** `AGENTS.md` directs agents to explicit shared read-only `scripts/agent-context.sh`.
- Project memory seeded: `.wolf/STATUS.md`, cerebrum preferences, decisions, project rules, and do-not-repeat.
- `.wolf/config.json`: cron, dashboard and designqc set disabled for this project; `hardware` removed from anatomy exclusion.
- First real import/CI defect recorded in a committed `.wolf/buglog/*.jsonl` shard. Never substitute a placeholder empty shard.
- Cross-agent context command and CI added; **EpicWolf memory checks run 40529605653 passed**, including Node guard + upstream tests (GitHub Actions).
- Import workflow's prior failure was a GitHub Actions PR-creation policy block. Draft PR #2 was opened via authenticated GitHub connector. A second defect (bad multiline workflow string) was found by PR CI and corrected on main in commit `286e5c60`; the checked-in bug shard resolved the failing memory check.

## Limitations and cautions
- The upstream hooks are third-party code with mutation capabilities. Passing vendor tests and reading hook registration is **not** a full source-security audit or runtime event test. Do not assume security certification.
- Import is subject to AGPL-3.0 license terms; retaining license and provenance does not settle distribution/use compliance for all future product scenarios.
- GitHub Free browser-first setup is the goal: Codespaces for IDE, Codex Cloud for agent tasks. This PR neither installs Codex nor enables native event-hooks in it.
- No KiCad schematic, PCB, or automotive electrical validation is created by this PR.
- A smoke test inside a real Codex Cloud task and a fresh Codespace remains necessary to demonstrate cross-agent use.
- Recommend keeping PR in draft until compatibility smoke test and hook source review are complete. No automatic merge.

## Live Codex Cloud F1 verified
- On 2026-10-27, Codex Cloud ran read-only context, wolf_guard and 31/31 vendor tests successfully, with Node 22.23.4 and no pre-existing source/memory mutations.
- PR #3 delivered the report and was squash-merged into the EpicWolf integration branch only, not main.
- Report: `docs/validation/CODEX_CLOUD_EPICWOLF_RUN.md`.
- No automatic EpicWolf hook execution was observed. This does not block explicit, read-only project memory access but remains a separate enhancement.
- Remaining acceptance: fresh Codespaces read-only test at matching revision, and review of inherited Claude-only hooks before enabling them.

## Codespaces browser runtime comparison (user-supplied evidence, 2026-10-27)
- Existing browser Codespace `codespaces-995a05` checked out `integration/epicwolf-vendored` revision `17dbc56` and ran `bash scripts/agent-context.sh` successfully.
- Reported guard: `wolf_guard: clean`; one valid bug record in one shard, five cerebrum sections.
- Node native runner: **31 tests passed, 0 failed** (total approximately 4.36 seconds).
- Read-only EpicWolf context and reported project status matched the Codex Cloud acceptance. Test fixture log output about absorbed entries is from the test harness, not proof of mutation of committed project files.
- User provided an initial empty `git status --short` before checkout, but no post-test `git status --short`; therefore Codespaces no-mutation is not independently confirmed.
- CI and Codex Cloud previously passed separate clean-worktree integrity checks. Cross-environment **explicit read/context** is validated. Automatic Codex lifecycle hooks remain unverified.
