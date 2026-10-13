# YouTube Transcript MCP Server

A lightweight, local [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server for extracting transcripts and captions from YouTube videos using `youtube-transcript-api`. No paid API keys or browser automation required.

This package includes the server implementation (`server.py`), dependencies (`requirements.txt`), and the companion agent skill (`skills/youtube-transcript/`).

---

## Package Contents

```text
youtube-transcript/
├── server.py                        # MCP server executable
├── requirements.txt                 # Dependencies: mcp, youtube-transcript-api
├── README.md                        # Setup, tool specs, and deployment guide
└── skills/
    └── youtube-transcript/
        └── SKILL.md                 # Agent instructions for invoking this MCP
```

---

## Prerequisites

- **Python**: Version 3.10 or higher.

---

## Installation & Setup

1. **Navigate to the server directory**:
   ```bash
   cd mcps/youtube-transcript
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   - **macOS / Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Tool Reference

### `get_youtube_transcript`

Retrieves the spoken transcript and timestamps for any public or unlisted YouTube video.

#### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `url` | `string` | *Required* | Full YouTube URL (watch URL, youtu.be, or Shorts) |
| `languages` | `list[string]` | `null` | Optional list of language preference codes (e.g. `["en", "es"]`) |
| `include_timestamps` | `boolean` | `true` | When `true`, formats transcript with `[MM:SS]` markers and segment objects. When `false`, returns continuous text. |

#### Return Value

Returns a JSON string containing:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "is_generated": false,
  "segments": [
    {
      "text": "We're no strangers to love",
      "start": 18.5,
      "duration": 3.2
    }
  ],
  "transcript": "[00:18] We're no strangers to love\n..."
}
```

If the video has disabled transcripts or is private, returns a descriptive error message:
- `Error: Transcripts are disabled for this video (ID: ...)`
- `Error: No transcript found for this video (ID: ...)`
- `Error: The video is unavailable or private (ID: ...)`

---

## 📍 Where to Put the Files Later

When sharing or integrating this MCP package into other projects or systems, place the files as follows:

### 1. Where to Keep the Server Files
- **Option A (In this repository)**: Keep the server in `mcps/youtube-transcript/`.
- **Option B (In a dedicated tools folder)**: You can copy this entire `youtube-transcript` folder into a central tools location, for example:
  - Windows: `C:\Users\<USERNAME>\.gemini\tools\youtube-transcript-mcp\`
  - macOS / Linux: `~/.config/mcp-tools/youtube-transcript-mcp/`

### 2. Where to Put the MCP Configuration
Add the server entry to your client's MCP configuration file:

- **Google Antigravity IDE**:
  - Global config: `~/.gemini/antigravity-ide/mcp_config.json`
  - Workspace config: `<PROJECT_ROOT>/.agents/mcp_config.json`
- **Claude Desktop**:
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Cursor**:
  - Settings > Features > MCP > "Add New MCP Server"

#### Windows Configuration Snippet:
```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "<ABSOLUTE_PATH_TO>/youtube-transcript/.venv/Scripts/python.exe",
      "args": [
        "<ABSOLUTE_PATH_TO>/youtube-transcript/server.py"
      ]
    }
  }
}
```

#### macOS / Linux Configuration Snippet:
```json
{
  "mcpServers": {
    "youtube-transcript": {
      "command": "<ABSOLUTE_PATH_TO>/youtube-transcript/.venv/bin/python",
      "args": [
        "<ABSOLUTE_PATH_TO>/youtube-transcript/server.py"
      ]
    }
  }
}
```

### 3. Where to Put the Companion Skill (`skills/youtube-transcript`)
The bundled folder `skills/youtube-transcript/` tells your AI agent when and how to call this tool.
- **For Antigravity (Workspace)**: Copy `skills/youtube-transcript/` to `<PROJECT_ROOT>/.agents/skills/youtube-transcript/`
- **For Antigravity (Global)**: Copy `skills/youtube-transcript/` to `~/.gemini/config/skills/youtube-transcript/` (Windows: `C:\Users\<USERNAME>\.gemini\config\skills\youtube-transcript\`)
- **For Obsidian Vaults**: Copy `skills/youtube-transcript/` to `<VAULT_ROOT>/.agents/skills/youtube-transcript/`
- **For Cursor**: Copy the instructions from `SKILL.md` into `.cursor/rules/youtube-transcript.mdc`
- **For GitHub Copilot**: Copy `skills/youtube-transcript/` to `.github/skills/youtube-transcript/`

---

## Troubleshooting

- **Process hanging / zombie processes**: Run `mcps/scripts/Clean-Zombie-MCPs.bat` on Windows to cleanly terminate lingering background Python MCP processes.
- **Transcripts Disabled**: Some creators explicitly disable captions for their videos; in such cases, the tool reports that transcripts are unavailable.
