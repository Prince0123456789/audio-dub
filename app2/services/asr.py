

def transcribe(request,audio_path):
    model = request.app.state.whisper_model
    result = model.transcribe(audio_path, word_timestamps=True)
    return result