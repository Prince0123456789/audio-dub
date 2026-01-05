import librosa
import soundfile as sf

def stretch_audio(input_audio, target_duration, output_audio):
    y, sr = librosa.load(input_audio, sr=None)
    current_duration = librosa.get_duration(y=y, sr=sr)

    rate = current_duration / target_duration
    y_stretched = librosa.effects.time_stretch(y, rate)

    sf.write(output_audio, y_stretched, sr)
