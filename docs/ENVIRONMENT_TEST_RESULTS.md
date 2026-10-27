# Infrastructure evidence — October 27, 2026

## Automated CI (no KiCad vehicle design files yet)
- GitHub Actions **Devcontainer build smoke** run 40523355859: SUCCESS. Proved `.devcontainer/Dockerfile` built and KiCad CLI/Python commands ran in its container. **Did not test the VS Code Codespaces feature provisioning or Node 22 integration.**
- Follow-up Devcontainer run 40523549451: SUCCESS on revision edf2eeac.
- KiCad CLI validation run 40523540268: SUCCESS on revision edf2eeac. Host checkout and isolated KiCad CLI invocation both succeeded. **No schematic or PCB existed, so this did not validate any electrical design.**
- KiCad CLI validation run 40523549511: SUCCESS.
- Earlier CI runs 40518278591 and 40523355743: FAILED during `actions/checkout` inside the KiCad job container; corrected by invoking the container from the Ubuntu host runner.

## Pending manual or agent-cloud smoke tests
- Create fresh 2-core Codespace from `infra/browser-first-foundation`; verify VS Code browser, Node 22, Python, `kicad-cli version`, persistent git changes.
- Configure Codex Cloud environment using `scripts/setup-codex-cloud.sh`, verify Node >=20 and KiCad version, run repository checks and push test branch.
- Run reviewed EpicWolf integration workflow, complete license/protocol and hook compatibility checks and merge separately.
- Confirm candidate KiCad MCP server startup, tool listing and read-only query on dummy schematic; do not expose remote public port.
- Validate a non-car KiCad example schematic through ERC/DRC and inspect generated artifacts.

## Version and validation boundary
The GitHub Actions image is `ghcr.io/kicad/kicad:9.0`; devcontainer installs Debian Trixie's KiCad package. Precise patch versions and compatibility remain subject to environment confirmation. KiCad 10 has **not** been deployed or verified. No circuit design or production approval is implied by any of these passes.
