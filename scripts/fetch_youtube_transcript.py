from youtube_transcript_api import YouTubeTranscriptApi

video_id = "jQXvbeYF5go"

try:
    transcript = YouTubeTranscriptApi().fetch(video_id)

    output_file = "research/youtube-transcripts/kevin-indig-ai-search.md" 

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Kevin Indig\n\n")
        f.write(f"Video ID: {video_id}\n\n")

        for snippet in transcript:
            f.write(snippet.text + "\n")

    print("Transcript saved successfully!")

except Exception as e:
    print(e) 