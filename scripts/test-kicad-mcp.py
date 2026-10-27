#!/usr/bin/env python3
"""Actual MCP stdio handshake + read-only schematic tool smoke test.

Works only on a disposable copy of a committed upstream fixture. Never edits
vehicle hardware and verifies the fixture bytes stay unchanged.
"""
import asyncio
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    fixture = Path(__file__).resolve().parents[1] / "tests/fixtures/mcp-upstream-example.kicad_sch"
    assert fixture.is_file(), "Missing isolated schematic fixture"
    source_hash = hashlib.sha256(fixture.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix="relay-mcp-fixture-") as folder:
        sample = Path(folder) / "example.kicad_sch"
        shutil.copy2(fixture, sample)
        initial_hash = hashlib.sha256(sample.read_bytes()).hexdigest()
        params = StdioServerParameters(
            command=sys.executable,
            args=["-m", "kicad_mcp_server"],
            env=dict(os.environ),
        )
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                init = await asyncio.wait_for(session.initialize(), timeout=30)
                result = await asyncio.wait_for(session.list_tools(), timeout=30)
                names = sorted(tool.name for tool in result.tools)
                print(f"MCP protocol: {init.protocolVersion}")
                print(f"Registered tools: {len(names)}")
                for name in names:
                    print(" -", name)
                if "list_schematic_components" not in names:
                    raise RuntimeError("Required read-only schematic tool missing")
                reply = await asyncio.wait_for(session.call_tool(
                    "list_schematic_components", {"file_path": str(sample)}
                ), timeout=30)
                response = "\n".join(str(x.text) for x in reply.content if getattr(x, "type", "") == "text")
                if reply.isError or "R1" not in response or "R2" not in response:
                    raise AssertionError(f"Component read did not match fixture: {response[:1500]}")
                print("Read-only schematic query confirmed R1 and R2.")
        if hashlib.sha256(sample.read_bytes()).hexdigest() != initial_hash:
            raise AssertionError("MCP modified the disposable schematic")
        if hashlib.sha256(fixture.read_bytes()).hexdigest() != source_hash:
            raise AssertionError("MCP modified the committed upstream fixture")
        print("PASS: stdio handshake, tools/list, fixture component query, unchanged bytes.")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
