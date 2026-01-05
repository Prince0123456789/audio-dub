from pydub import AudioSegment

def match_duration(audio_path, target_seconds):
    audio = AudioSegment.from_wav(audio_path)
    ratio = len(audio) / (target_seconds * 1000)
    return audio.speedup(playback_speed=ratio)
