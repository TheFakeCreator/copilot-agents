import os
import json
import subprocess
import tempfile
from typing import Optional
import yt_dlp
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("youtube-screenshot")

def get_stream_url(youtube_url: str) -> Optional[str]:
    ydl_opts = {'format': 'bestvideo[ext=mp4]/best[ext=mp4]/best', 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(youtube_url, download=False)
            return info.get('url')
        except Exception:
            return None

def timestamp_to_seconds(ts: str) -> float:
    parts = str(ts).split(':')
    if len(parts) == 1:
        return float(parts[0])
    elif len(parts) == 2:
        return float(parts[0]) * 60 + float(parts[1])
    elif len(parts) == 3:
        return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
    return 0.0

@mcp.tool()
def get_video_info(url: str) -> str:
    """Get metadata for a YouTube video."""
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            result = {
                "title": info.get("title"),
                "duration": info.get("duration"),
                "channel": info.get("uploader")
            }
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Error: Failed to retrieve video info: {str(e)}"

@mcp.tool()
def extract_frame(url: str, timestamp: str, output_path: str) -> str:
    """Extract a single frame from a YouTube video and save it to output_path.
    
    Args:
        url: The YouTube URL.
        timestamp: The timestamp to extract (e.g., "18:44", "00:18:44", or seconds).
        output_path: Absolute path where the image will be saved.
    """
    stream_url = get_stream_url(url)
    if not stream_url:
        return "Error: Could not retrieve video stream."

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cmd = ['ffmpeg', '-y', '-ss', str(timestamp), '-i', stream_url, '-vframes', '1', '-q:v', '2', '-update', '1', output_path]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(output_path):
            return f"Success: Frame extracted to {output_path}"
        else:
            return "Error: ffmpeg completed but output file not found."
    except subprocess.CalledProcessError as e:
        return f"Error: ffmpeg extraction failed.\n{e.stderr.decode('utf-8', errors='ignore')}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def extract_frames(url: str, start_timestamp: str, end_timestamp: str, interval_seconds: int) -> str:
    """Extract candidate frames over a time window for visual inspection.
    Returns a list of temporary file paths.
    
    Args:
        url: The YouTube URL.
        start_timestamp: The start time.
        end_timestamp: The end time.
        interval_seconds: The interval between frames in seconds.
    """
    start_sec = timestamp_to_seconds(start_timestamp)
    end_sec = timestamp_to_seconds(end_timestamp)
    
    if start_sec >= end_sec:
        return "Error: start_timestamp must be before end_timestamp."
        
    duration = end_sec - start_sec
    if duration > 60:
        return f"Error: The duration of the search window is {duration}s. To prevent timeouts, the duration cannot exceed 60 seconds. Please request a smaller search window."
        
    stream_url = get_stream_url(url)
    if not stream_url:
        return "Error: Could not retrieve video stream."
        
    temp_dir = tempfile.mkdtemp(prefix="youtube_frames_")
    fps = 1.0 / float(interval_seconds)
    output_pattern = os.path.join(temp_dir, "frame_%04d.png")
    
    cmd = ['ffmpeg', '-y', '-ss', str(start_sec), '-t', str(duration), '-i', stream_url, '-vf', f'fps={fps}', '-q:v', '2', output_pattern]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir) if f.endswith('.png')]
        return json.dumps({"candidate_frames": files}, indent=2)
    except subprocess.CalledProcessError as e:
        return f"Error: ffmpeg extraction failed.\n{e.stderr.decode('utf-8', errors='ignore')}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
