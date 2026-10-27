#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "== Browser-first tool verification =="
git --version
python3 --version
node --version
if ! command -v kicad-cli >/dev/null 2>&1; then
  echo "ERROR: KiCad CLI is missing" >&2
  exit 1
fi
kicad-cli version
python3 - <<'PY'
try:
    import pcbnew
    print("pcbnew Python bindings available:", pcbnew.Version())
except ImportError:
    print("NOTICE: pcbnew bindings unavailable; CLI checks remain supported")
PY
if [[ -d .wolf ]]; then
  echo "EpicWolf tree present; validating memory protocol"
  node .wolf/tools/wolf_guard.js
else
  echo "NOTICE: EpicWolf not merged yet. Complete reviewed import."
fi
echo "Environment smoke checks completed. This is NOT a board ERC/DRC pass."
