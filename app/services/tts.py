import subprocess
import uuid

def generate_tts(text):
    out = f"output/{uuid.uuid4()}.wav"
    subprocess.run([
        "piper",
        "--model", "models/piper/en_US-amy.onnx",
        "--output_file", out
    ], input=text.encode())
    return out
