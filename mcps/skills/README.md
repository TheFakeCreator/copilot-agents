# Bundled MCP Agent Skills

This folder contains pre-configured agent skill packages designed to work hand-in-hand with the local YouTube MCP servers.

---

## Skills Included

| Skill Folder | Description | Requires MCP Server |
|---|---|---|
| [`youtube-transcript/`](./youtube-transcript) | Directs agents to fetch transcripts, captions, and timestamped segments for YouTube videos without paid APIs. | `youtube-transcript` |
| [`youtube-visual-extraction/`](./youtube-visual-extraction) | Guides vision-enabled agents to visually inspect candidate frames around a timestamp and extract the clearest diagram, architecture, or slide. | `youtube-screenshot` |
| [`youtube-to-obsidian-notes/`](./youtube-to-obsidian-notes) | End-to-end knowledge synthesis workflow converting YouTube videos into structured, revision-oriented Obsidian notes with embedded frame captures. | Both servers |

---

## 📍 Where to Put the Skill Files Later

To make these skills automatically discoverable by your AI agent, copy the skill folders according to your platform:

### 1. Google Antigravity IDE

- **Workspace-Level (Active only in a specific project/workspace)**:
  Copy the desired skill folder(s) into your project's `.agents/skills/` directory:
  ```text
  <YOUR_PROJECT_ROOT>/
  └── .agents/
      └── skills/
          ├── youtube-transcript/
          ├── youtube-visual-extraction/
          └── youtube-to-obsidian-notes/
  ```

- **Global-Level (Active across all projects on your computer)**:
  Copy the desired skill folder(s) into your Antigravity global configuration directory:
  - **Windows**: `C:\Users\<USERNAME>\.gemini\config\skills\`
  - **macOS / Linux**: `~/.gemini/config/skills/`

---

### 2. Obsidian Vaults (for `youtube-to-obsidian-notes`)

If you want an Antigravity agent or Copilot running inside your Obsidian vault to generate lecture notes:
Copy the skill folders directly into the vault root under `.agents/skills/`:
```text
<YOUR_OBSIDIAN_VAULT>/
└── .agents/
    └── skills/
        ├── youtube-transcript/
        ├── youtube-visual-extraction/
        └── youtube-to-obsidian-notes/
```

---

### 3. Claude Desktop / Cursor / GitHub Copilot

- **Claude Desktop**: Claude does not natively parse `SKILL.md` folder structures. You can copy the markdown contents of `SKILL.md` into Claude Desktop's **Custom Instructions** or **Project Knowledge**.
- **Cursor**: Copy the markdown contents or rules into `.cursor/rules/<skill-name>.mdc` or add them to `.cursorrules`.
- **GitHub Copilot**: Copy into `.github/skills/<skill-name>/` or reference in `.github/copilot-instructions.md`.
