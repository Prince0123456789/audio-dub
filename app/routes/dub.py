from fastapi import APIRouter, UploadFile, File
from app.services.audio import *
from app.services.asr import transcribe
from app.services.translate import translate_text
from app.services.voice_clone import *
from app.services.tts import *
from app.services.voice_clone import *
from app.services.merge_video import *
from app.services.sync import *
from app.utils.timing import *

router = APIRouter()

@router.get("/")
def entry_check():
    return {"data":"True"}

@router.post("/video")
async def dub_video(file: UploadFile = File(...)):
    # print("file",file)
    video_path = f"/Users/princechuabey/Documents/trailer dub/api/app/input/{file.filename}"
    with open(video_path, "wb") as f:
        f.write(await file.read())

    # audio_path = extract_audio(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    segments = transcribe(audio_path)

    dubbed_audio_segments = []

    print("segments",segments)

    for i, seg in enumerate(segments):
        if not seg["text"]:  # fill text if empty
            seg["text"] = transcribe(seg["file"])  # implement this to get ASR text

        translated = translate_text(seg["text"])
        
        ref_audio = f"temp/segments/ref_{i}.wav"
        out_audio = f"temp/segments/dub_{i}.wav"

        generate_voice(translated, ref_audio, out_audio)
        
        stretch_audio(
            out_audio,
            seg["end"] - seg["start"],
            out_audio
        )

        dubbed_audio_segments.append(out_audio)

    merge_segments(dubbed_audio_segments, "output/final.wav")
    merge_audio_video(
        "/input/nvmc2ECk8Lo.mp4",
        "output/final.wav",
        "output/dubbed_trailer.mp4"
        )

    return {"output": "output_video"}


