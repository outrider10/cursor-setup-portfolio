from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

videos = [
    {
        "author": "Kevin Indig",
        "video_id": "jQXvbeYF5go",
        "filename": "kevin-indig-ai-search.md"
    },
    {
        "author": "Rand Fishkin",
        "video_id": "SUNLVR7-C-w",
        "filename": "rand-fishkin-ai-search.md"
    },
    {
        "author": "Ross Simmonds",
        "video_id": "9AEShQj4OaA",
        "filename": "ross-simmonds-content-distribution.md"
    },
    {
        "author": "Justin Welsh",
        "video_id": "7laZlckl2i4",
        "filename": "justin-welsh-content-systems.md"
    },
    {
        "author": "Dave Gerhardt",
        "video_id": "UB8ZJ01N3bk",
        "filename": "dave-gerhardt-b2b-marketing.md"
    },
    {
        "author": "Amanda Natividad",
        "video_id": "JZ0jue2ef9I",
        "filename": "amanda-natividad-zero-click.md"
    },
    {
        "author": "Anthony Pierri",
        "video_id": "w_rkMuEf6s4",
        "filename": "anthony-pierri-saas-messaging.md"
    },
    {
        "author": "April Dunford",
        "video_id": "PiRPLT4YuHk",
        "filename": "april-dunford-positioning.md"
    },
    {
        "author": "Ashley Faus",
        "video_id": "MpvnzdbQmVs",
        "filename": "ashley-faus-product-marketing.md"
    },
    {
        "author": "Chris Walker",
        "video_id": "IW02GkREyQs",
        "filename": "chris-walker-demand-generation.md"
    }
]

output_dir = Path("research") / "youtube-transcripts"
output_dir.mkdir(parents=True, exist_ok=True)

api = YouTubeTranscriptApi()

for video in videos:
    print(f"Fetching transcript for {video['author']}...")

    try:
        transcript = api.fetch(video["video_id"])

        output_file = output_dir / video["filename"]

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# {video['author']}\n\n")
            f.write(f"Video ID: {video['video_id']}\n\n")
            f.write("## Transcript\n\n")

            for snippet in transcript:
                f.write(snippet.text + "\n")

        print(f"✓ Saved: {output_file}")

    except Exception as e:
        print(f"✗ Failed for {video['author']}: {e}")

print("\nDone!")