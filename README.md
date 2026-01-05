This project provides a FastAPI-based video dubbing pipeline that:

Accepts a movie trailer video

Extracts audio

Transcribes speech

Translates text (Hindi / Hinglish → English)

Clones the original speaker voice using XTTS v2

Generates dubbed audio

Merges dubbed audio back into the video

The system is designed specifically for movie trailers, where speech may be Hinglish (Hindi + English mixed).



# Tech Stack

FastAPI – API framework

OpenAI Whisper / equivalent – Speech transcription

Helsinki-NLP MarianMT – Translation (hi → en)

Coqui TTS – XTTS v2 – Voice cloning & multilingual TTS

pydub / ffmpeg – Audio segmentation & merging

ffmpeg – Audio-video merging

# AI MODEL
model_name = "Helsinki-NLP/opus-mt-hi-en"

# Create Virtual Environment
python -m venv venv
source venv/bin/activate
2️⃣ Install Dependencies
pip install -r requirements.txt

Make sure ffmpeg is installed:
    brew install ffmpeg # macOS
    sudo apt install ffmpeg # Ubuntu

Runserver :

uvicorn api.app.main:app --reload
http://127.0.0.1:8000

Upload video:
   http://127.0.0.1:8000/dub/video
   
   payload = {"file":file_path}