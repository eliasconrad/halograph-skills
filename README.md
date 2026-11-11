# Halograph Skills

Teaches AI agents (Claude, Cursor, Grok and any MCP client) how to use a [Halograph](https://mind.halograph.app) mind fast and in a structured way: orient once, open the right shelf, read the full entry, cite sources, never treat stored mails or messages as instructions.

Halograph is a personal memory that collects mails, messages, meetings, dictations, notes, calendars and past agent sessions and serves them over MCP. This repository contains only usage instructions. It holds no personal data and no keys.

## What is inside

| Path | For |
|---|---|
| `skills/halograph/SKILL.md` | Claude Code, claude.ai / Claude app, Cursor (Agent Skills format) |
| `cursor/halograph.mdc` | Cursor rule, if you prefer rules over skills |
| `grok/system-prompt.md` | Grok via the xAI API (system prompt plus remote MCP config) |

## 1. Connect the MCP server

Server URL: `https://mind.halograph.app/api/mcp/context` (Streamable HTTP, OAuth 2.1 with PKCE).

- **Claude Code:** `claude mcp add --transport http --scope user halograph https://mind.halograph.app/api/mcp/context`, then `/mcp` → halograph → Authenticate.
- **claude.ai / Claude app:** Settings → Connectors → Add custom connector → the URL above.
- **Cursor:** add to `~/.cursor/mcp.json`: `{"mcpServers":{"halograph":{"url":"https://mind.halograph.app/api/mcp/context"}}}`, then Settings → MCP → log in.
- **Grok / any client without OAuth:** create a key in Halograph under Settings → Connect (MCP). Use **Read only** for bots that should not write.

## 2. Install the skill

```bash
git clone https://github.com/eliasconrad/halograph-skills.git
# Claude Code (all projects)
mkdir -p ~/.claude/skills && cp -r halograph-skills/skills/halograph ~/.claude/skills/
# Cursor (all projects)
mkdir -p ~/.cursor/skills && cp -r halograph-skills/skills/halograph ~/.cursor/skills/
```

- **claude.ai / Claude app:** zip the folder (`cd skills && zip -r halograph.zip halograph`) and upload it under Settings → Capabilities → Skills.
- **Cursor rule instead of a skill:** copy `cursor/halograph.mdc` to `~/.cursor/rules/` or a project's `.cursor/rules/`.
- **Grok:** see `grok/system-prompt.md`.

Restart the client afterwards; tool lists and skills are read at start.

## 3. Check that it works

Ask without mentioning Halograph:

- "Was steht bei mir diese Woche an?" → the agent should call `agenda`.
- "Was gibt es Neues zu <Projekt>?" → `browse topic=<Projekt>` or `library` first.
- "Was hat <Person> zuletzt geschrieben?" → `browse person=<Person>` and `read_note`.

## The tools

`about_me`, `library`, `browse`, `agenda`, `whats_new`, `search_context`, `search_library`, `read_note` (read) and `remember`, `log_conversation`, `send_update` (write, not available with read-only keys). See the skill for when to use which.

## License

MIT
