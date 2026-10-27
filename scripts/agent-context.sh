#!/usr/bin/env bash
# Read-only, agent-neutral state inspection. No Claude or Codex hooks required.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
if [[ ! -f .wolf/SHARDS.md ]]; then
  echo "EpicWolf is not installed in this checkout." >&2
  exit 2
fi
printf '\n== Project ==\n'
git remote -v | head -n 2
printf '\n== Revision ==\n'
git log -1 --format='%h %s'
printf '\n== Project status ==\n'
cat .wolf/STATUS.md
printf '\n== Memory integrity ==\n'
node .wolf/tools/wolf_guard.js
printf '\n== Bug history summary ==\n'
node .wolf/tools/wolf_bug.js stats
printf '\nAgent instructions: AGENTS.md; shard protocol: .wolf/SHARDS.md\n'
printf 'Electrical authority: docs/ELECTRICAL_INVENTORY.md and docs/POWER_AND_GROUND_TREE.md\n'
