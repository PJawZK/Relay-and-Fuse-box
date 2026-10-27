## Do-Not-Repeat

- Do not infer current Mega144H7 harness pins from historic MegaSquirt DB37 maps, an EpicECU-Beta design or the 2002 Bowling & Grippo board.
- Do not call an ERC/DRC workflow a design pass when no KiCad design file exists.
- Do not assume a GitHub Actions token can create pull requests; repository policy blocked it during EpicWolf import even after successful tests and branch push.
- Do not use `wolf_migrate.js --buglog` on a newly initialized empty EpicWolf template with no legacy log entries. Start a real bug shard with `wolf_bug.js append` only for an actual error.
- Do not claim EpicWolf's Claude Code hook configuration delivers automatic memory capture in Codex.
