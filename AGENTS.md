# Instructions for any coding agent (Cursor, Codex, others)

This repo is a job-search agent. **Read and follow `CLAUDE.md`** — it is the full instruction set; the name is
historical, it applies to you too.

Workflows live in `.claude/skills/<name>/SKILL.md`: `setup`, `daily`, `find`, `apply`, `prep`, `strategist`.
When the user asks for one of them (or types `/setup`, `/daily`, …), read that file and follow it step by step.
If `profile.md` does not exist, start with `setup`.

Hirelog (shared hiring memory) is an MCP server at `https://hirelog.dev/mcp` (`.cursor/mcp.json` for Cursor;
for Codex add it to `~/.codex/config.toml`, see https://hirelog.dev/docs). If MCP tools are not available,
read through the REST API instead: `curl "https://hirelog.dev/api/v1/check?url=<posting>&company=<name>"`,
`/api/v1/companies/<name>`, `/api/v1/ats/<slug>`; write with `python3 tools/hirelog.py`.
