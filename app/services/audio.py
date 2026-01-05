import subprocess
import ffmpeg
from pydub import AudioSegment

def extract_audio(video_path: str) -> str:
    audio_path = video_path.replace(".mp4", ".wav")
    print("video_path",video_path)
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar=16000)
        .overwrite_output()
        .run(quiet=True)
    )

    return audio_path


def merge_audio(video_path: str, audio_path: str, output_path: str):
    """
    Replaces original audio with dubbed audio
    """
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-map", "0:v:0",
        "-map", "1:a:0",
        output_path
    ], check=True)



def merge_segments(segments, output_audio):
    final = AudioSegment.silent(duration=0)

    for seg in segments:
        final += AudioSegment.from_wav(seg)

    final.export(output_audio, format="wav")
