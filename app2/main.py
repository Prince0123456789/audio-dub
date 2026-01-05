
from fastapi import FastAPI
from app2.routes.dub import router as dub_router
import whisper
import ssl
from contextlib import asynccontextmanager

ssl._create_default_https_context = ssl._create_unverified_context

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.whisper_model = whisper.load_model("small")
    yield

app = FastAPI(title="Voice Dubbing API",lifespan=lifespan)

app.include_router(dub_router, prefix="/dub")



