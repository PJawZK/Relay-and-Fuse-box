#!/usr/bin/env bash
# MCP STDIO launcher; intentionally never installs dependencies or exposes ports.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
VENV="${KICAD_MCP_VENV:-$ROOT/.local/kicad-mcp-venv}"
PY="$VENV/bin/python"
if [[ ! -x "$PY" ]]; then
  echo "KiCad MCP not installed. Run: bash scripts/setup-kicad-mcp.sh" >&2
  exit 2
fi
cd "$ROOT"
exec "$PY" -m kicad_mcp_server
