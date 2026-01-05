from fastapi import APIRouter, UploadFile, File, Request
from app2.services.asr import transcribe

router = APIRouter()

@router.get("/")
def entry_check():
    return {"data":"True"}

@router.post("/transcribe")
async def transcribe_audio(request: Request, file: UploadFile = File(...)):
    
    result = transcribe(request,f"app2/input/{file.filename}")
    return {"text": result['text']}