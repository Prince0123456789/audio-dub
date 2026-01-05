import ffmpeg

def merge_audio_video(video, audio, output):
    ffmpeg.input(video).output(
        audio,
        v=1,
        a=1,
        output=output
    ).overwrite_output().run()
