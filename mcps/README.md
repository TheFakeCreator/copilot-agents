# YouTube MCP Package

A complete, self-contained package providing local [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers and agent skills for YouTube integration.

---

## 📦 Package Layout

Everything needed for the servers, companion agent skills, configurations, and utilities is organized directly within this directory:

```text
mcps/
├── README.md                      # Complete guide & deployment instructions
├── mcp_config.example.json        # Config template for Antigravity, Claude, and Cursor
│
├── scripts/                       # Maintenance & helper scripts
│   └── Clean-Zombie-MCPs.bat      # Windows utility to kill orphaned Python MCP processes
│
├── youtube-transcript/            # Self-contained Transcript MCP
│   ├── server.py                  # Server code (youtube-transcript-api)
│   ├── requirements.txt           # Dependencies
│   ├── README.md                  # Setup & parameter guide
│   └── skills/                    # Dedicated skill
│       └── youtube-transcript/
│           └── SKILL.md
│
├── youtube-screenshot/            # Self-contained Frame Capture MCP
│   ├── server.py                  # Server code (yt-dlp + ffmpeg)
│   ├── requirements.txt           # Dependencies
│   ├── README.md                  # Setup & ffmpeg guide
│   └── skills/                    # Dedicated skill
│       └── youtube-visual-extraction/
│           └── SKILL.md
│
└── skills/                        # Complete bundle of all 3 skills
    ├── README.md                  # Skill catalog & installation guide
    ├── youtube-transcript/
    ├── youtube-visual-extraction/
    └── youtube-to-obsidian-notes/ # End-to-end lecture-to-Obsidian workflow
        ├── SKILL.md
        ├── references/
        └── templates/
```

---

## ⚙️ Prerequisites

1. **Python 3.10+**: Must be installed and available in your system `PATH`.
2. **`ffmpeg`** *(required for `youtube-screenshot`)*:
   - Must be installed and accessible via `PATH`.
   - **Verification**: Run `ffmpeg -version`.
   - **Quick Install**:
     - Windows: `winget install Gyan.FFmpeg` or `choco install ffmpeg`
     - macOS: `brew install ffmpeg`
     - Linux: `sudo apt install ffmpeg`

---

## 🚀 Setup & Virtual Environments

Run these commands once for each server:

### 1. YouTube Transcript Server
```bash
cd mcps/youtube-transcript
python -m venv .venv

# Activate:
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Windows (CMD):
.\.venv\Scripts\activate.bat
# macOS / Linux:
source .venv/bin/activate

# Install:
pip install -r requirements.txt
```

### 2. YouTube Screenshot Server
```bash
cd mcps/youtube-screenshot
python -m venv .venv

# Activate:
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Windows (CMD):
.\.venv\Scripts\activate.bat
# macOS / Linux:
source .venv/bin/activate

# Install:
pip install -r requirements.txt
```

---

## 📍 Where to Put the Files Later

When integrating these servers and skills into your setup or distributing them to other users, follow these placement rules:

### 1. MCP Server Folders (`youtube-transcript/` & `youtube-screenshot/`)
You can either:
- **Keep them inside this repository**: Point your MCP config directly to `<ABSOLUTE_PATH_TO_REPO>/mcps/youtube-transcript/` and `<ABSOLUTE_PATH_TO_REPO>/mcps/youtube-screenshot/`.
- **OR Move to a centralized tools folder**:
  - Windows: `C:\Users\<USERNAME>\.gemini\tools\youtube-transcript-mcp\` and `C:\Users\<USERNAME>\.gemini\tools\youtube-screenshot-mcp\`
  - macOS / Linux: `~/.config/mcp-tools/youtube-transcript/` and `~/.config/mcp-tools/youtube-screenshot/`

---

### 2. MCP Client Configuration (`mcp_config.json`)
Copy the template from [`mcp_config.example.json`](./mcp_config.example.json) into your client's configuration file:

| Client | Platform | Target Configuration File Path |
|---|---|---|
| **Google Antigravity IDE** | Global | `C:\Users\<USERNAME>\.gemini\antigravity-ide\mcp_config.json` (or `~/.gemini/antigravity-ide/mcp_config.json`) |
| **Google Antigravity IDE** | Project | `<PROJECT_ROOT>/.agents/mcp_config.json` |
| **Claude Desktop** | Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Claude Desktop** | macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Cursor** | All | `Settings > Features > MCP > Add New MCP Server` |

#### Windows Config Snippet:
```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "<PATH_TO_DIR>/youtube-transcript/.venv/Scripts/python.exe",
      "args": ["<PATH_TO_DIR>/youtube-transcript/server.py"]
    },
    "youtube-screenshot": {
      "command": "<PATH_TO_DIR>/youtube-screenshot/.venv/Scripts/python.exe",
      "args": ["<PATH_TO_DIR>/youtube-screenshot/server.py"]
    }
  }
}
```

#### macOS / Linux Config Snippet:
```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "<PATH_TO_DIR>/youtube-transcript/.venv/bin/python",
      "args": ["<PATH_TO_DIR>/youtube-transcript/server.py"]
    },
    "youtube-screenshot": {
      "command": "<PATH_TO_DIR>/youtube-screenshot/.venv/bin/python",
      "args": ["<PATH_TO_DIR>/youtube-screenshot/server.py"]
    }
  }
}
```

---

### 3. Agent Skills (`skills/`)
To enable AI agents to automatically discover and use the MCP tools:

- **Google Antigravity IDE**:
  - **Project-Specific**: Copy the folders from `mcps/skills/` into `<YOUR_PROJECT>/.agents/skills/`
  - **Global (All Projects)**: Copy the folders from `mcps/skills/` into:
    - Windows: `C:\Users\<USERNAME>\.gemini\config\skills\`
    - macOS / Linux: `~/.gemini/config/skills/`

- **Obsidian Vaults (for `youtube-to-obsidian-notes`)**:
  - Copy all three skill folders into `<VAULT_ROOT>/.agents/skills/`.

- **Cursor**:
  - Copy instructions from each `SKILL.md` into `.cursor/rules/<skill-name>.mdc` or `.cursorrules`.

- **GitHub Copilot**:
  - Copy skill folders into `.github/skills/` or reference them in `.github/copilot-instructions.md`.

---

### 4. Cleanup Script (`scripts/Clean-Zombie-MCPs.bat`)
- Keep in `mcps/scripts/Clean-Zombie-MCPs.bat` or place on your Desktop / system PATH.
- Run whenever an MCP client terminates unexpectedly and background Python processes remain running.
