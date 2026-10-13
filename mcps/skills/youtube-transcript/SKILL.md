---
name: youtube-transcript
description: Retrieves transcripts from YouTube videos using the locally configured YouTube transcript MCP server. Use whenever the user provides a YouTube URL and asks for its transcript, captions, subtitles, text, summary, analysis, notes, explanation, or any task that requires understanding the spoken content of a YouTube video.
---

# YouTube Transcript

## Purpose

Use the local YouTube transcript MCP server whenever a task requires obtaining the spoken text or captions from a YouTube video.

The goal is to provide a reliable, local, free transcript workflow without depending on paid transcript APIs.

## When to use

Use this skill when:

- The user provides a YouTube URL.
- The user asks for a YouTube transcript.
- The user asks to summarize a YouTube video.
- The user asks to analyze, explain, extract notes from, or answer questions about a YouTube video.
- The user asks to convert a YouTube video into text.
- The user asks to extract subtitles/captions from a YouTube video.

## Workflow

1. Identify the YouTube URL from the user's request.
2. Use the configured YouTube transcript MCP tool to retrieve the transcript.
3. Prefer the video's manually created transcript/captions when available.
4. If manually created captions are unavailable, use automatically generated captions when available.
5. Preserve timestamps when they are useful for the user's task.
6. If the MCP server supports language selection, prefer the video's original language unless the user requests another language.
7. If the requested language is unavailable, use an available transcript and clearly state which language was retrieved.
8. Do not fabricate missing transcript sections.
9. If no transcript is available, clearly report that the video does not expose usable captions through the configured extraction method.
10. After obtaining the transcript, perform the user's requested operation on it.

## Tool selection

Look for the MCP tool provided by the local YouTube transcript server.

Prefer a dedicated transcript retrieval tool such as:

- `get_youtube_transcript`
- `youtube_transcript`
- `fetch_youtube_transcript`

Use the actual tool name exposed by the MCP server rather than assuming a specific name.

Pass the complete YouTube URL and set `include_timestamps=True` when the tool accepts them.

If the tool accepts a video ID instead, extract the video ID from the URL and pass that.

## Transcript handling

For large transcripts:

- Do not unnecessarily dump the entire transcript into the conversation.
- Retrieve the complete transcript when required for analysis.
- Preserve chronological ordering.
- Keep timestamps if they help identify sections.
- For summaries, notes, or analysis, use the transcript as the source material.

For tasks that require exact quotations:

- Quote only the necessary portions.
- Do not invent wording that is not present in the transcript.

## Reliability

The MCP server is expected to operate locally and should not require a paid API.

Do not claim that every YouTube video is guaranteed to work.

A video may fail if:

- captions are disabled;
- captions are unavailable;
- YouTube restricts access;
- the video is private or inaccessible;
- the transcript extraction library cannot access the captions;
- YouTube changes its underlying interfaces.

When extraction fails:

1. Report the actual failure.
2. Do not invent a transcript.
3. If appropriate, try another transcript language exposed by the tool.
4. Do not switch to a paid API unless the user explicitly asks for an alternative.

## User experience

When the user says something like:

"Summarize this video:
https://www.youtube.com/watch?v=..."

First retrieve the transcript through the MCP server.

Then summarize the transcript directly.

Do not ask the user to manually copy the YouTube transcript unless the local extraction method genuinely fails.

When the user explicitly asks for the raw transcript, return the transcript rather than a summary.

## Important

The MCP server performs transcript retrieval.

This skill provides the decision-making and workflow instructions for when and how the MCP server should be used.