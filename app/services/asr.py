import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
model = whisper.load_model("base")

def transcribe(audio_path):
    result = model.transcribe(audio_path, word_timestamps=True)
    print("transcribe done")
    return result["segments"]