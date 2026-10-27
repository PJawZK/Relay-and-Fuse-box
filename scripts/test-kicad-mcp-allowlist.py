#!/usr/bin/env python3
"""Test Codex-facing MCP allowlist with real stdio protocol, no design edits."""
import asyncio
import hashlib
import os
from pathlib import Path
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/mcp-upstream-example.kicad_sch"


async def main():
    before = hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    params = StdioServerParameters(
        command="bash", args=[str(ROOT / "scripts/run-kicad-mcp.sh")],
        env=dict(os.environ),
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as client:
            await asyncio.wait_for(client.initialize(), timeout=30)
            tools = await asyncio.wait_for(client.list_tools(), timeout=30)
            names = [tool.name for tool in tools.tools]
            print("Codex-facing MCP tools:", names)
            assert names == ["list_schematic_components"], (
                "FAIL: unexpected or mutating MCP tools exposed: " + repr(names)
            )
            result = await asyncio.wait_for(
                client.call_tool("list_schematic_components", {}), timeout=30
            )
            response = "\n".join(
                getattr(part, "text", "") for part in result.content
                if getattr(part, "type", "") == "text"
            )
            assert not result.isError, response
            assert "R1:" in response and "R2:" in response, response
            print("Allowed read-only result includes R1 and R2.")
            try:
                blocked = await asyncio.wait_for(
                    client.call_tool("create_project", {"name": "forbidden"}),
                    timeout=10,
                )
            except Exception as exc:
                print("Unregistered editing tool rejected:", type(exc).__name__)
            else:
                assert blocked.isError, "FAIL: unregistered editing tool executed"
                print("Unregistered editing tool was rejected by MCP server.")
    after = hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    assert before == after, "FAIL: fixture mutated"
    print("PASS: exactly one fixture-only tool, editing tool rejected, source unchanged.")


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
