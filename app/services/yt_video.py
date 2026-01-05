import yt_dlp
import os

def download_youtube_video(youtube_url: str, output_dir="input"):
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": f"{output_dir}/%(id)s.%(ext)s",
        "merge_output_format": "mp4",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        video_path = ydl.prepare_filename(info)
        video_path = video_path.rsplit(".", 1)[0] + ".mp4"

    return video_path



# download_youtube_video("https://www.youtube.com/watch?v=nvmc2ECk8Lo")