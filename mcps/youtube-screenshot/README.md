# YouTube Screenshot MCP Server

A local [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server for fetching video metadata and extracting high-fidelity screenshots/frames from YouTube videos using `yt-dlp` and `ffmpeg`.

This package includes the server implementation (`server.py`), dependencies (`requirements.txt`), and the companion agent skill (`skills/youtube-visual-extraction/`).

---

## Package Contents

```text
youtube-screenshot/
├── server.py                        # MCP server executable
├── requirements.txt                 # Dependencies: mcp>=1.0.0, yt-dlp
├── README.md                        # Setup, ffmpeg prerequisite, and deployment guide
└── skills/
    └── youtube-visual-extraction/
        └── SKILL.md                 # Agent instructions for candidate inspection & saving
```

---

## Features

- **No Video Download Necessary**: Streams video frames directly into memory via `ffmpeg` using streaming URLs resolved by `yt-dlp`.
- **Single Frame Extraction**: Grabs exact frames at precise timestamps (e.g. diagrams, slides, architecture).
- **Batch Candidate Extraction**: Samples frames across a target time window at regular intervals for visual inspection by the AI.
- **Video Metadata**: Retrieves title, duration in seconds, and uploader channel.

---

## Prerequisites

1. **Python**: Version 3.10 or higher.
2. **`ffmpeg`** *(Required)*:
   - Must be installed and registered in your system `PATH`.
   - **Verification**: Run `ffmpeg -version` in your terminal.
   - **Installation Guide**:
     - **Windows**: Run `winget install Gyan.FFmpeg` or `choco install ffmpeg`
     - **macOS**: Run `brew install ffmpeg`
     - **Linux (Ubuntu/Debian)**: Run `sudo apt update && sudo apt install -y ffmpeg`

---

## Installation & Setup

1. **Navigate to the server directory**:
   ```bash
   cd mcps/youtube-screenshot
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

### 1. `get_video_info`

Fetches metadata for a YouTube video.

#### Parameters
| Parameter | Type | Default | Description |
|---|---|---|---|
| `url` | `string` | *Required* | Full YouTube URL |

#### Return Value
```json
{
  "title": "System Design: How to design YouTube",
  "duration": 1845,
  "channel": "Tech Lead"
}
```

---

### 2. `extract_frame`

Extracts a single frame at an exact timestamp and saves it directly to a local file path.

#### Parameters
| Parameter | Type | Default | Description |
|---|---|---|---|
| `url` | `string` | *Required* | Full YouTube URL |
| `timestamp` | `string` | *Required* | Target timestamp (`"18:44"`, `"00:18:44"`, or seconds like `"1124"`) |
| `output_path` | `string` | *Required* | Absolute path where the image will be saved (PNG/JPEG) |

---

### 3. `extract_frames`

Extracts candidate frames across a defined time window at regular intervals. Used by vision-enabled agents to visually inspect scenes and choose the clearest frame.

#### Parameters
| Parameter | Type | Default | Description |
|---|---|---|---|
| `url` | `string` | *Required* | Full YouTube URL |
| `start_timestamp` | `string` | *Required* | Window start time (e.g. `"14:20"` or `"860"`) |
| `end_timestamp` | `string` | *Required* | Window end time (e.g. `"14:50"` or `"890"`) |
| `interval_seconds` | `integer` | *Required* | Sampling interval in seconds (e.g. `5`) |

> [!IMPORTANT]
> The duration between `start_timestamp` and `end_timestamp` must not exceed **60 seconds** to avoid extraction timeouts.

---

## 📍 Where to Put the Files Later

When integrating this MCP package into other projects or systems, place the files as follows:

### 1. Where to Keep the Server Files
- **Option A (In this repository)**: Keep the server in `mcps/youtube-screenshot/`.
- **Option B (In a dedicated tools folder)**: You can copy this entire `youtube-screenshot` folder into a central tools location, for example:
  - Windows: `C:\Users\<USERNAME>\.gemini\tools\youtube-screenshot-mcp\`
  - macOS / Linux: `~/.config/mcp-tools/youtube-screenshot-mcp/`

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
    "youtube-screenshot": {
      "command": "<ABSOLUTE_PATH_TO>/youtube-screenshot/.venv/Scripts/python.exe",
      "args": [
        "<ABSOLUTE_PATH_TO>/youtube-screenshot/server.py"
      ]
    }
  }
}
```

#### macOS / Linux Configuration Snippet:
```json
{
  "mcpServers": {
    "youtube-screenshot": {
      "command": "<ABSOLUTE_PATH_TO>/youtube-screenshot/.venv/bin/python",
      "args": [
        "<ABSOLUTE_PATH_TO>/youtube-screenshot/server.py"
      ]
    }
  }
}
```

### 3. Where to Put the Companion Skill (`skills/youtube-visual-extraction`)
The bundled folder `skills/youtube-visual-extraction/` instructs your AI agent on how to call `extract_frames` and `extract_frame` to visually select the best diagrams and slides.
- **For Antigravity (Workspace)**: Copy `skills/youtube-visual-extraction/` to `<PROJECT_ROOT>/.agents/skills/youtube-visual-extraction/`
- **For Antigravity (Global)**: Copy `skills/youtube-visual-extraction/` to `~/.gemini/config/skills/youtube-visual-extraction/` (Windows: `C:\Users\<USERNAME>\.gemini\config\skills\youtube-visual-extraction\`)
- **For Obsidian Vaults**: Copy `skills/youtube-visual-extraction/` to `<VAULT_ROOT>/.agents/skills/youtube-visual-extraction/`
- **For Cursor**: Copy the instructions from `SKILL.md` into `.cursor/rules/youtube-visual-extraction.mdc`
- **For GitHub Copilot**: Copy `skills/youtube-visual-extraction/` to `.github/skills/youtube-visual-extraction/`

---

## Troubleshooting

- **`ffmpeg: command not found`**: Verify that `ffmpeg` is installed and accessible from terminal. Restart your IDE after updating system PATH.
- **Process hanging / zombie processes**: Run `mcps/scripts/Clean-Zombie-MCPs.bat` on Windows to terminate orphaned Python processes.
- **`yt-dlp` updates**: If YouTube alters its video formats or stream signatures, update `yt-dlp` (`pip install --upgrade yt-dlp`).
