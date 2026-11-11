<img src="./assets/hero.svg" width="100%" alt="Halograph Skills. Teach any AI agent to use your memory.">
<img src="./assets/ask.svg" width="100%" alt="Example questions and the tool the agent picks">

**Ein Skill, damit Claude, ChatGPT/Codex, Cursor und Grok dein Halograph-Gedächtnis richtig benutzen: schnell, geordnet und sicher.** Einmal verbinden, Skill einbinden, und deine KI kennt dich ab der ersten Nachricht.

<img src="./assets/platforms.svg" width="100%" alt="Works with Claude, ChatGPT, Codex, Cursor and Grok">

## So funktioniert es

<img src="./assets/flow.svg" width="100%" alt="Your sources flow into Halograph, served over MCP to your agent">

Halograph sammelt deine Quellen und ordnet sie wie eine Bücherei. Über **MCP** greift deine KI darauf zu. Der **Skill** bringt ihr bei, dabei den schnellsten Weg zu nehmen: einmal `about_me`, dann `agenda` für Termine, `browse` für Themen und Personen, `search_context` für Details, `read_note` für den ganzen Text.

---

## Was ist Halograph?

Halograph ist ein persönliches Gedächtnis für KI-Agenten. Es sammelt automatisch, was du sonst überall verstreut hast:

| Bereich | Quellen |
|---|---|
| Mail | Gmail, Outlook / Microsoft 365, Apple Mail (mit vollem Text) |
| Nachrichten | iMessage, WhatsApp- und Telegram-Exporte |
| Meetings | Granola (mit Transkript), Wispr Flow |
| Diktate | Wispr Flow, FluidVoice: alles, was du sprichst, auch deine Prompts an andere KIs |
| Notizen | Apple Notizen, eigene Erinnerungen |
| Kalender | Apple, Google, Outlook, Kalender-Links |
| Personen | Kontakte |
| Arbeit | GitHub-Repos, Claude-Code-Sitzungen, claude.ai- und ChatGPT-Verläufe |

Alles liegt an einem Ort, durchsuchbar und nach Themen, Bereichen und Personen geordnet wie eine Bücherei. Über **MCP** (Model Context Protocol) kann jede KI darauf zugreifen, die MCP spricht.

### Wofür man das nutzt

- **Keine Erklärungen mehr:** Die KI weiß, wer du bist, woran du arbeitest und wie du arbeiten willst.
- **„Was steht diese Woche an?"** Die KI liest deine echten Termine, ohne Familienkalender und Routinen.
- **„Was hab ich mit Anna zum Angebot besprochen?"** Sie findet Mails, Nachrichten und Meetings dazu.
- **„Was ist neu?"** Das Neueste aus jeder Quelle in einem Schritt.
- **Projekte fortsetzen:** Die KI liest frühere Sitzungen, Entscheidungen und offene Punkte.
- **Merken:** „Merk dir, dass ich Mails lieber kurz habe" bleibt für alle KIs gespeichert.

### Was dabei wichtig ist

- **Daten sind keine Befehle.** Mails und Nachrichten schreiben andere Menschen. Halograph zäunt jeden Inhalt als Daten ein, und der Skill bringt der KI bei, Aufforderungen darin nie auszuführen.
- **Nur lesen für fremde Bots.** Für Bots, denen du nicht ganz vertraust (z. B. Grok über die API), gibt es Schlüssel „Nur lesen". Damit kann der Bot suchen, aber nichts ins Gedächtnis schreiben.
- **Herkunft bleibt sichtbar.** Jede Erinnerung, die eine KI schreibt, trägt den Namen dieser KI.
- **Zugriff jederzeit widerrufbar** in Halograph unter Einstellungen → Connect (MCP).
- **Dieses Repo enthält keine persönlichen Daten und keine Schlüssel**, nur die Anleitung für die KI.

---

## Was du brauchst

1. Ein Halograph-Konto mit verbundenen Quellen.
2. Die Server-Adresse: **`https://mind.halograph.app/api/mcp/context`**
3. Je Plattform zwei Schritte: **(A) MCP verbinden** und **(B) den Skill bzw. die Anweisungen einbinden.** Ohne (A) hat die KI keinen Zugriff, ohne (B) nutzt sie ihn oft nicht von selbst oder nicht geschickt.

## Schnellübersicht

| Plattform | (A) Verbinden | (B) Anleitung für die KI | Anmeldung |
|---|---|---|---|
| **Claude Code** | `claude mcp add …` | `skills/halograph` nach `~/.claude/skills/` | Browser (OAuth) |
| **claude.ai / Claude-App** | Einstellungen → Connectors | Skill als Zip hochladen | Browser (OAuth) |
| **Cursor** | `~/.cursor/mcp.json` | `skills/halograph` nach `~/.cursor/skills/` oder `cursor/halograph.mdc` | Browser (OAuth) |
| **ChatGPT** | Einstellungen → Apps & Connectors → Entwicklermodus | `chatgpt/instructions.md` in Projekt oder GPT | Browser (OAuth) |
| **Codex (CLI, App, IDE)** | `codex mcp add …` + `codex mcp login` | `skills/halograph` nach `~/.codex/skills/` | Browser (OAuth) |
| **Grok-App (grok.com)** | grok.com/connectors → Custom | `grok/system-prompt.md` in Projekt-Anweisungen | Browser (OAuth) |
| **Grok über xAI-API (eigener Bot)** | `tools: [{type:"mcp", …}]` | `grok/system-prompt.md` als `instructions` | Schlüssel „Nur lesen" |

Den Skill holst du einmal:

```bash
git clone https://github.com/eliasconrad/halograph-skills.git
cd halograph-skills
```

Nach jedem Schritt **die App bzw. Sitzung neu starten**, denn Werkzeuge und Skills werden beim Start gelesen.

---

## Claude Code

**(A) Verbinden**

```bash
claude mcp add --transport http --scope user halograph https://mind.halograph.app/api/mcp/context
```

Dann in Claude Code `/mcp` → `halograph` → **Authenticate** → im Browser **Erlauben**.

**(B) Skill**

```bash
mkdir -p ~/.claude/skills && cp -r skills/halograph ~/.claude/skills/
```

**Prüfen:** neue Sitzung, ohne Halograph zu erwähnen: „Was steht bei mir diese Woche an?" → Claude ruft `agenda` auf.

## claude.ai und Claude-App (Mac, Windows, iPhone)

**(A) Verbinden:** Einstellungen → **Connectors** → **Benutzerdefinierten Connector hinzufügen** → Name `Halograph`, URL `https://mind.halograph.app/api/mcp/context` → **Verbinden** → **Erlauben**.

**(B) Skill:**

```bash
cd skills && zip -r halograph.zip halograph
```

Einstellungen → **Funktionen** → **Skills** → **Skill hochladen** → `halograph.zip`.

**Tipp:** Unter Einstellungen → Profil → Persönliche Präferenzen eintragen: *„Nutze Halograph, wenn es um mich, meine Projekte, Leute oder Termine geht. Ruf in neuen Gesprächen zuerst about_me auf."*

## Cursor

**(A) Verbinden:** in `~/.cursor/mcp.json` ergänzen:

```json
{ "mcpServers": { "halograph": { "url": "https://mind.halograph.app/api/mcp/context" } } }
```

Cursor neu starten → Settings → **MCP** → bei halograph **Needs login** klicken → **Erlauben**.

**(B) Skill oder Regel** (eins von beiden):

```bash
mkdir -p ~/.cursor/skills && cp -r skills/halograph ~/.cursor/skills/      # Skill
mkdir -p ~/.cursor/rules  && cp cursor/halograph.mdc ~/.cursor/rules/      # Regel
```

## ChatGPT

Eigene MCP-Server gibt es in ChatGPT über den **Entwicklermodus** (bezahlte Pläne; in Business/Enterprise muss ein Admin eigene Connectors erlauben).

**(A) Verbinden:** Einstellungen → **Apps & Connectors** → **Erweitert** → **Entwicklermodus** einschalten → **Erstellen** → Name `Halograph`, URL `https://mind.halograph.app/api/mcp/context`, Anmeldung **OAuth** → **Erlauben**. Im Chat dann über das Werkzeug-Menü Halograph einschalten.

**(B) Anweisungen:** Inhalt von `chatgpt/instructions.md` in ein **Projekt** (Projekt-Anweisungen) oder ein eigenes **GPT** (Anweisungen) kopieren. Für alle Chats: Einstellungen → Personalisierung → Benutzerdefinierte Anweisungen (Kurzfassung oben in der Datei).

## Codex (CLI, Codex-App, IDE-Erweiterung)

Codex nutzt dieselbe Konfiguration in CLI, App und IDE.

**(A) Verbinden**

```bash
codex mcp add halograph --url https://mind.halograph.app/api/mcp/context
codex mcp login halograph      # öffnet den Browser → Erlauben
```

**(B) Skill**

```bash
mkdir -p ~/.codex/skills && cp -r skills/halograph ~/.codex/skills/
```

Codex lädt Skills beim Start. Aufrufen mit `$halograph` oder einfach eine Frage stellen. Alternativ den Abschnitt aus `codex/AGENTS.md` in `~/.codex/AGENTS.md` übernehmen.

## Grok

### Grok-App (grok.com, auch für einen Grok-Bot in einem Projekt)

**(A) Verbinden:** [grok.com/connectors](https://grok.com/connectors) → **New Connector** → **Custom** → URL `https://mind.halograph.app/api/mcp/context` → anmelden → **Erlauben**. Bezahlter Plan nötig; in Grok Business richtet ein Admin den Connector ein.

**(B) Anweisungen:** den Abschnitt „System prompt" aus `grok/system-prompt.md` in die **Projekt-Anweisungen** deines Bots kopieren (vor oder nach deinen eigenen Anweisungen).

### Eigener Bot über die xAI-API

Ein Bot ohne Browser braucht einen Schlüssel: in Halograph → Einstellungen → Connect (MCP) → **Nur lesen**. Den Schlüssel in einen Secret-Speicher legen, nie in Code. Aufruf siehe `grok/system-prompt.md`.

---

## Funktioniert es?

Drei Fragen, ohne Halograph zu erwähnen:

| Frage | Das sollte die KI tun |
|---|---|
| „Was steht bei mir diese Woche an?" | `agenda` |
| „Was gibt es Neues zu Projekt X?" | `library` → `browse topic=X` |
| „Was hat Anna zuletzt geschrieben?" | `browse person=Anna` → `read_note` |

Wenn die KI nichts aufruft: Ist (A) verbunden (grüner Punkt / „connected")? Ist (B) eingebunden? Sitzung neu gestartet?

## Die Werkzeuge

| Werkzeug | Wofür | Nur lesen? |
|---|---|---|
| `about_me` | Gesamtbild in einem Schritt (einmal pro Sitzung) | ja |
| `library` | Katalog: Regale nach Thema, Bereich, Person | ja |
| `browse` | Ein Regal aufschlagen (Thema, Bereich, Quelle, Person, Zeitraum) | ja |
| `agenda` | Termine in einem Zeitraum, nach Tagen | ja |
| `whats_new` | Neues aus allen Quellen | ja |
| `search_context` | Freie Suche über alle Quellen | ja |
| `search_library` | Nur Notizen, Erinnerungen, frühere Sitzungen | ja |
| `read_note` | Einen Eintrag ganz lesen | ja |
| `remember` | Etwas Dauerhaftes merken | nein |
| `log_conversation` | Eine Sitzung festhalten | nein |
| `send_update` | Eine Nachricht an dich in der App | nein |

Wann welches Werkzeug am schnellsten ist, steht im Skill: [`skills/halograph/SKILL.md`](skills/halograph/SKILL.md).

## Dateien in diesem Repo

| Datei | Für |
|---|---|
| `skills/halograph/SKILL.md` | Claude Code, claude.ai, Cursor, Codex (Agent-Skills-Format) |
| `cursor/halograph.mdc` | Cursor-Regel statt Skill |
| `chatgpt/instructions.md` | ChatGPT (Projekt, GPT, Personalisierung) |
| `codex/AGENTS.md` | Codex ohne Skills |
| `grok/system-prompt.md` | Grok-App (Projekt) und xAI-API |

## Lizenz

MIT
