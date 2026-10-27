# Shared agent instructions: Relay-and-Fuse-box

This repository is the **single source of truth** for this Volvo 940 Turbo EFI electrical project, independent of the computer/chat agent used.

## Start here
1. Read `README.md`, `docs/ELECTRICAL_INVENTORY.md`, `docs/TOOLING_AND_WORKFLOW.md`, and (once vendored) `.wolf/SHARDS.md` and `.wolf/STATUS.md`.
2. Read actual KiCad source files from `hardware/` when present; never infer their contents from previous chat or old PDF reference alone.
3. Start read-only context inspection with `bash scripts/agent-context.sh` when EpicWolf is present. Record important project decisions and failed approaches in its cerebrum/buglog using the shard protocol and reviewed commits. Do not assume automatic memory capture in Codex or ChatGPT.
4. Changes to the schematic/PCB must be checked against the **current committed design**, not historic assumptions.
5. Separate evidence categories: **verified installed**, **user reported installed**, **planned**, **historic**, **unknown**, **design proposal**.

## Agent / cloud tools
- Chat interfaces with GitHub access can inspect/edit committed files and documentation. GitHub access **does not inherently give a chat process access to KiCad MCP tools**.
- A cloud computer, Codespace or agent runner with a tested KiCad + compatible MCP server installed is required for interactive KiCad editing. Codespaces currently has **KiCad 9.0.2** and native pcbnew bindings; KiCad 10 and MCP remain unvalidated. Keep all source and config in this repo and commit changes on branches.
- GitHub Actions can run CLI ERC/DRC and export review artifacts when design files exist. These checks do not establish automotive electrical safety.
- Never claim an MCP tool, EpicWolf hook, KiCad runner or CI check is operational until tested in that runtime.
- Do not rely on personal-machine-only installations or Windows-only applications as authoritative project dependencies.

## Electrical safety and ground rules
- Preserve fuel-pump shutdown on engine stop/ECU failure; no unsafe always-on fallback.
- ECU power and sensor-ground references must remain isolated from H-bridge motor currents in the intended topology.
- Do not select copper thickness, fuse rating, wire size, relay ratings or TVS protection on guesses alone.
- Treat Bosch/VAG/OEM parts and source-board schematics as references; verify installed markings and datasheets.
- Never publish Gerbers as production-ready without independent electrical, thermal, fault and vehicle bench validation.
- User's **measured problem** is voltage loss, not a measured drop in current.

## Scope
Design a passive or minimally complex low-drop fuse/relay distribution replacement for the aging DIYAutoTune MegaSquirt-style relay board. Standard serviceable Micro ISO relays and fuses, neat central wiring and Linux/cloud-first KiCad workflow are preferred. EpicWolf is the chosen project-memory stack.
