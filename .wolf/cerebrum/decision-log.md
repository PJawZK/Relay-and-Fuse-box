## Decision Log

- 2026-10-27 — Select EpicWolf fork ggurov/epicwolf (pinned e2d446b76b97a2f88a41f261a5796964dc3df68a) for persistent project state. Import under a separate draft PR; review hooks and license before merge.
- 2026-10-27 — Choose browser-first, repository-centered workflow: Codex Cloud for agent work, GitHub Codespaces for interactive web IDE, GitHub Actions for validation, local Linux optional.
- 2026-10-27 — Preserve vehicle fuse/relay box design as unstarted until existing power/ground topology, component register, load measurements and validation gates have been reviewed.
- 2026-10-27 — Prefer standard serviceable Micro ISO relays and conventional fuses; prioritize low-loss reliable power paths, accessible wiring, and separate H-bridge motor return from ECU/sensor grounds.
- 2026-10-27 — Initial cloud runtime verified KiCad CLI and pcbnew 9.0.2, not KiCad 10. Use version-aware migration later; don't assume matching CAD versions across runners.
- 2026-10-27 — Claude hooks do not automatically transfer to Codex or ChatGPT. Initially use an explicit cross-agent read-only context entrypoint and validation checks.

- 2026-10-27 — User clarified **entire current EpicEFI EFI electrical system** is separately wired and fused with new aftermarket relays; **no original Volvo factory EFI wiring, fuses or relays are reused**. The aged aftermarket MS relay box is distinct from the Volvo factory LH EFI relay system. Original LH injection relay positions (including 2/23 turbo, conditional 2/13) may be repurposed only after actual socket feed/coil/control validation. Prior statements that OEM 2/23 must remain for EpicEFI are superseded.
