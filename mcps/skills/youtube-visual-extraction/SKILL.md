---
name: youtube-visual-extraction
description: Extracts and saves the best frame from a YouTube video based on a transcript timestamp. Use this when you need to capture a visual (like a diagram, table, or architecture) discussed in a video to embed it in a note.
---

# YouTube Visual Extraction

This skill allows you to visually inspect candidate frames from a YouTube video and save the best one to the user's workspace.

## Prerequisites
- The `youtube-screenshot` MCP Server must be running and available.

## Workflow

### 1. Candidate Extraction
Given a YouTube URL and an exact timestamp from the transcript (e.g., `18:42`):
1. Use the `call_mcp_tool` tool to invoke `extract_frames` from the `youtube-screenshot` MCP Server. 
2. Pass the arguments: `url`, `start_timestamp`, `end_timestamp` (create a search window around the timestamp, e.g., +/- 10 seconds), and `interval_seconds` (e.g., `5`).
3. The tool will return a list of temporary file paths containing candidate frames.

### 2. Vision Verification
Visually inspect the candidate frames using your vision capabilities.
- Is there actually a relevant visual?
- Is it fully visible and readable?
- Is it not an intermediate transition frame?
- Is the presenter blocking it?
- Is it not purely decorative (e.g., just the presenter's face)?
- **Progressive Build-up Check:** If the frames show a diagram or list being built up over a span of time, select the frame with the **most complete information** (usually near the end of the span), ensuring you do not miss any intermediate information that might have been erased or scrolled off-screen.
Select the *best* frame from the candidates.

### 3. Saving the Frame
Once the best frame is identified and its exact timestamp noted:
1. Use the `call_mcp_tool` tool to invoke `extract_frame` from the `youtube-screenshot` MCP Server. 
2. Pass the arguments: `url`, the exact `timestamp` of the best frame, and an absolute `output_path`.
   **Example Output Path:** `<path-to-attachments-or-notes-folder>/<video-slug>/<note-name>-<timestamp>.png` (e.g. for Obsidian: `<vault-root>/attachments/<video-slug>/<note-name>-<timestamp>.png`)

**Obsidian Auto-Rename Warning:** Obsidian may automatically rename the file immediately after it is saved (e.g., by appending a timestamp). After saving, list the directory contents to confirm the exact final filename.

Return the absolute path of the verified, final saved file to the caller so they can embed it appropriately.
