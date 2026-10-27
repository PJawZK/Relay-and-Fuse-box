#!/usr/bin/env python3
"""Read-only actual MCP stdio handshake and tool-list probe.

Tests the installed MCP transport; does not edit KiCad or vehicle files.
"""
import asyncio
import sys
import os
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    interpreter = sys.executable
    # Use the same Python venv, because stdio server must see identical packages.
    env = dict(os.environ)
    params = StdioServerParameters(
        command=interpreter,
        args=["-m", "kicad_mcp_server"],
        env=env,
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await asyncio.wait_for(session.initialize(), timeout=30)
            result = await asyncio.wait_for(session.list_tools(), timeout=30)
            names = sorted(t.name for t in result.tools)
            if not names:
                raise RuntimeError("MCP initialized but registered zero tools")
            print(f"MCP protocol: {init.protocolVersion}")
            print(f"Registered tools: {len(names)}")
            for name in names:
                print(" -", name)
            print("PASS: real stdio handshake + tools/list; no tools invoked.")
            return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
