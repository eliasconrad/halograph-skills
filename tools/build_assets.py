# Builds the graphics of this repo in the halograph.app style.  python3 tools/build_assets.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from style import *
A = os.path.join(os.path.dirname(__file__), "..", "assets")
si = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {}

# Hero
inner = sphere(960, 170, 150) + mark(64, 64, 34) + \
  f'<text x="112" y="88" fill="{MUTED}" font-family="{F}" font-size="17">halograph</text>' + \
  f'<text x="62" y="186" fill="{TEXT}" font-family="{F}" font-size="66" font-weight="600" letter-spacing="-2">Halograph Skills</text>' + \
  f'<text x="64" y="232" fill="{MUTED}" font-family="{F}" font-size="24">Teach any AI agent to use your memory.</text>' + \
  pill(64, 270, "Claude · ChatGPT · Codex · Cursor · Grok", pulse=False)
open(f"{A}/hero.svg", "w").write(frame(1200, 340, inner, "Halograph Skills. Teach any AI agent to use your memory."))

# Animated line: question -> tool
pairs = [("What's on this week?", "agenda"), ("Everything on project Atlas", "library → browse"), ("What did Anna write me?", "browse person → read_note"), ("What did I miss?", "whats_new"), ("Remember: I prefer short mails", "remember")]
items = [f'<text x="64" y="31" fill="{TEXT}" font-family="{M}" font-size="16">“{q}”</text><text x="1136" y="31" fill="{MUTED}" font-family="{M}" font-size="16" text-anchor="end">→ {t}</text>' for q, t in pairs]
open(f"{A}/ask.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="48" viewBox="0 0 1200 48" role="img" aria-label="Example questions and the tool the agent picks">{cycle(items, 0, 0)}</svg>')

# Platform tiles (monochrome like the website)
def logo(kind, x, y):
    if kind in si:
        return f'<g transform="translate({x},{y}) scale(1.4)"><path d="{si[kind]}" fill="{TEXT}"/></g>'
    ch = {"chatgpt": "G", "codex": "&gt;_", "grok": "X"}[kind]
    return f'<rect x="{x}" y="{y}" width="34" height="34" rx="17" fill="none" stroke="{LINE}"/><text x="{x+17}" y="{y+22}" fill="{TEXT}" font-family="{M}" font-size="14" font-weight="600" text-anchor="middle">{ch}</text>'
tiles = [("claude", "Claude", "Code · claude.ai · app", "skill + connector"), ("chatgpt", "ChatGPT", "developer mode", "prompt + connector"), ("codex", "Codex", "CLI · app · IDE", "skill + codex mcp"), ("cursor", "Cursor", "editor", "skill + mcp.json"), ("grok", "Grok", "grok.com · xAI API", "prompt + connector")]
tw, gap = 216, 12; el = []
for i, (k, name, sub, how) in enumerate(tiles):
    x = 12 + i * (tw + gap)
    el += [f'<rect x="{x}" y="12" width="{tw}" height="176" rx="20" fill="{CARD}" stroke="{LINE}"/>', logo(k, x + 22, 34),
           f'<text x="{x+22}" y="110" fill="{TEXT}" font-family="{F}" font-size="21" font-weight="600">{name}</text>',
           f'<text x="{x+22}" y="133" fill="{MUTED}" font-family="{F}" font-size="13.5">{sub}</text>',
           f'<text x="{x+22}" y="166" fill="{DIM}" font-family="{M}" font-size="12">{how}</text>']
open(f"{A}/platforms.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="1164" height="200" viewBox="0 0 1164 200" role="img" aria-label="Works with Claude, ChatGPT, Codex, Cursor and Grok">{"".join(el)}</svg>')

# Flow
cols = [("Your sources", ["Mail · iMessage · meetings", "dictations · notes · calendar", "contacts · past sessions"]),
        ("Halograph", ["catalog, shelves, search", "read-only or read-write", "data fenced, never commands"]),
        ("MCP", ["one URL, OAuth", "or a read-only key", "about_me · library · browse"]),
        ("Your agent", ["knows you on turn one", "picks the fastest tool", "cites source and date"])]
W, bw = 1200, 250; gap = (W - 48 - 4 * bw) / 3; el = []
for i, (t, ls) in enumerate(cols):
    x = 24 + i * (bw + gap); hl = i == 1
    el.append(f'<rect x="{x:.0f}" y="24" width="{bw}" height="150" rx="20" fill="{CARD}" stroke="{TEXT if hl else LINE}" stroke-opacity="{0.55 if hl else 1}"/>')
    if hl: el.append(mark(x + 22, 44, 22))
    el.append(f'<text x="{x + (54 if hl else 22):.0f}" y="62" fill="{TEXT}" font-family="{F}" font-size="20" font-weight="600">{t}</text>')
    el += [f'<text x="{x+22:.0f}" y="{98+j*24}" fill="{MUTED}" font-family="{F}" font-size="14">{l}</text>' for j, l in enumerate(ls)]
    if i < 3:
        x1, x2 = x + bw + 6, x + bw + gap - 6
        el.append(f'<line x1="{x1:.0f}" y1="99" x2="{x2:.0f}" y2="99" stroke="{LINE}" stroke-width="1.5"/>')
        el.append(f'<circle cx="{x1:.0f}" cy="99" r="3" fill="#fff"><animate attributeName="cx" values="{x1:.0f};{x2:.0f}" dur="1.6s" begin="{i*0.4}s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" dur="1.6s" begin="{i*0.4}s" repeatCount="indefinite"/></circle>')
open(f"{A}/flow.svg", "w").write(frame(W, 198, "".join(el), "Your sources flow into Halograph, served over MCP to your agent"))
print("ok")
