import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
import torchaudio
import os
import numpy as np
import soundfile as sf
import librosa


# Add all XTTS-related classes to safe_globals
torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    XttsArgs,              # <--- newly required
    BaseDatasetConfig
])

# torchaudio.set_audio_backend("soundfile")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)


def load_audio(path, target_sr=16000):

    audio, sr = sf.read(path)
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1) 
    if sr != target_sr:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
    return audio, target_sr


def generate_voice(text, reference_audio_path, output_path):
    if not os.path.exists(reference_audio_path):
        raise FileNotFoundError(f"Reference audio not found: {reference_audio_path}")
    
    speaker_wav, sr = load_audio(reference_audio_path)
    
    speaker_wav = speaker_wav.flatten()
    if speaker_wav.size == 0:
        speaker_wav = None
    
    # Generate TTS
    tts.tts_to_file(
        text=text,
        speaker_wav=reference_audio_path,
        language="en",   
        file_path=output_path
    )
    print(f"Saved generated audio to {output_path}")
