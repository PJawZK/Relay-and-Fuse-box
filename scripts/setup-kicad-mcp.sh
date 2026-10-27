#!/usr/bin/env bash
# Explicit opt-in installation. No remote server, credentials or hardware access.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
MCP_REV="0b445be8668c00b0d71315e74fa2f180bca686c2"
VENV="${KICAD_MCP_VENV:-$PWD/.local/kicad-mcp-venv}"
SOURCE="${KICAD_MCP_SOURCE:-$PWD/.local/kicad-mcp-source}"
if ! command -v kicad-cli >/dev/null; then
  echo "kicad-cli not found: install KiCad first" >&2; exit 2
fi
kicad-cli version
python3 -m venv --system-site-packages "$VENV"
mkdir -p "$(dirname "$SOURCE")"
if [[ ! -d "$SOURCE/.git" ]]; then
  git clone https://github.com/Seeed-Studio/kicad-mcp-server.git "$SOURCE"
fi
git -C "$SOURCE" fetch --depth 1 origin "$MCP_REV"
git -C "$SOURCE" checkout --detach "$MCP_REV"
"$VENV/bin/python" -m pip install "$SOURCE"
"$VENV/bin/python" -c 'from kicad_mcp_server.server import mcp; print("MCP server import: OK")'
echo "Installed pinned KiCad MCP to $VENV (git revision $MCP_REV)"
echo "Next: $VENV/bin/python scripts/test-kicad-mcp.py"
