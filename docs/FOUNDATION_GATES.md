# Foundation phase gates — no vehicle board design yet

Status originally assessed **2026-10-27**, with planning updates **2026-11-02**, grounded in repository evidence and the user-observed Codespaces/Codex runs. A gate with a *limited pass* is **not** a broader feature sign-off.

| Gate | Objective | Evidence/definition of done | Current status |
|---|---|---|---|
| F1 | EpicWolf project memory | Pinned version, CI and cloud read-only context, integrity guard, 31 tests; automatic lifecycle capture separately assessed | **Passed for explicit context workflow** (Codex Cloud and Codespaces); native Codex automatic hooks **unverified** |
| F2 | Browser-only Codespaces | Existing Codespace runs KiCad 9.0.2 and pcbnew 9.0.2, MCP sample tests and CLI | **Passed for observed workspace**; fresh 2-core reproducibility not independently completed |
| F3 | Codex Cloud | Codex cloud F1 runs context/guard/tests and produces report; infrastructure install/PR path evaluated | **Partial**; F1 passed; broad Codex Cloud KiCad MCP tool invocation unverified |
| F4 | KiCad validation | CLI/pcbnew verified in Codespaces and CI image; non-vehicle ERC/DRC fixture tests if/when supplied | **Partial**; version/toolchain passed, full sample ERC/DRC gate not evidenced |
| F5 | KiCad MCP | Pinned server, isolated STDIO roundtrip, restricted fixture-only method, editing-method rejection, native agent invocation | **Passed for fixed-fixture read-only façade**; unrestricted read of arbitrary designs and editing unsupported |
| F6 | As-built electrical inventory | Current harness pin/terminal trace, ground return, installed fuse/relay markings and evidence | **Open**; v0.2 records EV14 positives from MS box in two fused pairs and old PWM/Fast Idle unused; exact injector pair JP2/coil/pump/other physical terminal ownership still missing. Future-load inventory added |
| F7 | Electrical requirements | Load currents, voltage-drop targets, start/inrush, fuse coordination, thermal and fault acceptance | **Open**; v0.2 requirements plus future expansion power domains/slot budget added; no measured steady/inrush loads, fuse/copper ratings or accepted numeric targets |
| F8 | Readiness review | Reviewed hardware evidence and design constraints before schematic/PCB and independently before vehicle installation | **Open** |

## Current future-load planning references (2026-11-02)

- [Installed and planned power-feed inventory](POWER_LOAD_INVENTORY_CURRENT_AND_FUTURE.md): owner-reported EV14 split and unused idle, 255 L/h pump, IOX/EGT/EMAP, pedal sensors, 940-DDS/CAN/CarPi power requirements.
- [Expansion distribution capacity](POWER_DISTRIBUTION_EXPANSION_CAPACITY.md): provisional 12–14 fuse cavities, 4 relay cavities, an external cabin accessory feed and separate regulated sensor supplies. This **does not close F6/F7** or authorize a PCB.

## Source evidence

- F1: `docs/validation/CODEX_CLOUD_EPICWOLF_RUN.md`, `docs/EPICWOLF_PR_REVIEW.md`; integration merged via PR #2.
- F2/F3: `docs/CLOUD_WORKSPACE_SETUP.md`, `docs/CODEX_CLOUD_VALIDATION.md`, `docs/ENVIRONMENT_TEST_RESULTS.md`, user-observed Codespaces F1 test.
- F5: `docs/KICAD_MCP_EVALUATION.md`, `docs/CODEX_KICAD_MCP_ACCEPTANCE.md`; PR #4 merged as `6d1de6e5`. Read-only tool returns R1/R2 through native Codex CLI.
- F6/F7: `docs/ELECTRICAL_INVENTORY.md`, `docs/POWER_AND_GROUND_TREE.md`, `docs/ELECTRICAL_EVIDENCE_LEDGER.md`, `docs/ELECTRICAL_MEASUREMENT_WORKSHEET.md` plus new `docs/F6_REPLACEMENT_CIRCUIT_MATRIX.md` and `docs/F7_ELECTRICAL_REQUIREMENTS_V0.md`. Functional concept: `docs/REPLACEMENT_FUNCTIONAL_ARCHITECTURE_V0.md`. New files are working specifications, **not gate closure or physical acceptance**.

## Non-negotiable progression rules

1. Successful blank-file CI does not establish schematic ERC/PCB DRC; likewise a fixture-only MCP success does not validate arbitrary project files.
2. KiCad 9 was verified; KiCad 10 availability and migration remain unvalidated. Never mix versions in board authoring without a documented compatibility/migration procedure.
3. No schematic, PCB, BOM, Gerber, conductor, fuse or transient-protection design is authorized by software infrastructure gates alone.
4. F6 and F7 must close using physical observations and measurements **before** entering detailed hardware design. Record limitations and signatures for F8.
5. EpicWolf records decisions; actual vehicle measurements, connection evidence and current committed design sources take priority over archived chats.
