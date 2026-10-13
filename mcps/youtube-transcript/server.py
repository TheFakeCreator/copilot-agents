import re
import json
from typing import Optional, List
from mcp.server.mcpserver import MCPServer
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

mcp = MCPServer("youtube-transcript")

def extract_video_id(url: str) -> Optional[str]:
    # Match standard, shortened, shorts URLs and parameters
    patterns = [
        r"(?:v=|/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be/([0-9A-Za-z_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

@mcp.tool()
def get_youtube_transcript(url: str, languages: Optional[List[str]] = None, include_timestamps: Optional[bool] = True) -> str:
    """
    Retrieve the transcript of a YouTube video.
    
    Args:
        url: The full YouTube URL.
        languages: Optional list of language codes to try (e.g. ['en', 'fr']).
        include_timestamps: If True (default), includes inline timestamps in the transcript text and returns a list of segments.
    """
    video_id = extract_video_id(url)
    if not video_id:
        return f"Error: Could not extract a valid YouTube video ID from URL: {url}"
    
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        transcript_obj = None
        if languages:
            try:
                transcript_obj = transcript_list.find_transcript(languages)
            except NoTranscriptFound:
                pass
                
        if not transcript_obj:
            # Prefer manual over generated
            manually_created = transcript_list._manually_created_transcripts
            generated = transcript_list._generated_transcripts
            
            if manually_created:
                # Pick the first manual transcript
                transcript_obj = list(manually_created.values())[0]
            elif generated:
                # Pick the first generated transcript
                transcript_obj = list(generated.values())[0]
            else:
                return f"Error: No transcripts available for video ID {video_id}"
                
        transcript_data = transcript_obj.fetch()
        
        result = {
            "video_id": video_id,
            "language": transcript_obj.language_code,
            "is_generated": transcript_obj.is_generated,
        }
        
        if include_timestamps:
            result["segments"] = [{"text": item.text, "start": item.start, "duration": item.duration} for item in transcript_data]
            
            formatted_transcript = []
            for item in transcript_data:
                m, s = divmod(int(item.start), 60)
                h, m = divmod(m, 60)
                if h > 0:
                    ts = f"[{h:02d}:{m:02d}:{s:02d}]"
                else:
                    ts = f"[{m:02d}:{s:02d}]"
                formatted_transcript.append(f"{ts} {item.text}")
                
            result["transcript"] = "\n".join(formatted_transcript)
        else:
            result["transcript"] = " ".join([item.text for item in transcript_data])
            
        return json.dumps(result, indent=2)

    except TranscriptsDisabled:
        return f"Error: Transcripts are disabled for this video (ID: {video_id})."
    except NoTranscriptFound:
        return f"Error: No transcript found for this video (ID: {video_id})."
    except VideoUnavailable:
        return f"Error: The video is unavailable or private (ID: {video_id})."
    except Exception as e:
        return f"Error: Failed to retrieve transcript: {str(e)}"

if __name__ == "__main__":
    mcp.run()
