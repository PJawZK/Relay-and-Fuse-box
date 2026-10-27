## Project Rules

- Source of truth is committed GitHub files, not conversational recollection or an uncommitted Codespace.
- Inspect README.md, AGENTS.md, .wolf/SHARDS.md and .wolf/STATUS.md before substantial implementation.
- Do not claim that Claude-specific hooks operate in Codex or ChatGPT. Use documented explicit tools for cross-agent status/validation.
- Engineering evidence levels: physically verified installed, user-reported installed, historical, proposed, unresolved. Never silently promote historical pinouts or schematic examples into current facts.
- Current ECU: EpicEFI Mega144H7 on Speeduino 0.4.3C adapter. The original Bowling & Grippo MS relay schematic is only a reference until the installed board is inspected.
- Do not add schematic, Gerbers or manufacturing releases until foundation gates in docs/FOUNDATION_GATES.md are satisfied.
- Keep electrical protection, relay fail-safe behavior, sensor-ground separation and H-bridge motor-current return path as mandatory review concerns.
- Never open a Codespace MCP port publicly or commit credentials to EpicWolf memory.
- When editing EpicWolf logs, use the shard protocol and guarded utilities; leave derived views uncommitted.
