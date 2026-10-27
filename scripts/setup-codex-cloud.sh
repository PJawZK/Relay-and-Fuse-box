#!/usr/bin/env bash
set -euo pipefail
# Explicit task environment bootstrap (not auto-run by Codex Cloud).
# Suitable for Debian 13 based Linux environments with root/sudo. Do not run
# in a restricted shell with no apt permissions; Codex Cloud setup must allow it.
if ! command -v apt-get >/dev/null 2>&1; then
  echo "Requires a Debian apt environment." >&2
  exit 2
fi
if (( EUID == 0 )); then SUDO=""; else SUDO="sudo"; fi
$SUDO apt-get update
$SUDO apt-get install -y --no-install-recommends \
  ca-certificates git curl bash jq python3 python3-venv python3-pip kicad
if ! command -v node >/dev/null 2>&1 || [[ "$(node -p 'process.versions.node.split(".")[0]' || echo 0)" -lt 20 ]]; then
  echo "NOTICE: install Node.js >=20 for EpicWolf. No unpinned curl|bash installer is used." >&2
fi
bash scripts/verify-environment.sh
