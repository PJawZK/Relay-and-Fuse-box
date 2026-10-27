#!/usr/bin/env python3
"""Fixture-only KiCad MCP facade for Codex acceptance.

Exposes exactly one tool. Never registers the upstream editing tools.
The permitted input is an immutable, predetermined upstream test fixture.
"""
from pathlib import Path

from fastmcp import FastMCP
from kicad_mcp_server.parsers.schematic_parser import SchematicParser

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = (ROOT / "tests/fixtures/mcp-upstream-example.kicad_sch").resolve(strict=True)
mcp = FastMCP(name="relay-kicad-fixture-readonly")


@mcp.tool()
def list_schematic_components() -> str:
    """List components from the pinned disposable KiCad test schematic only."""
    components = SchematicParser(str(FIXTURE)).get_components()
    if not components:
        return "No components in fixture"
    return "\n".join(f"{component.reference}: {component.value}" for component in components)


if __name__ == "__main__":
    mcp.run(show_banner=False)
