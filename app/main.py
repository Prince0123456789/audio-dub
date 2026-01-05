
from fastapi import FastAPI
from app.routes.dub import router as dub_router

app = FastAPI(title="Video Dubbing API")

app.include_router(dub_router, prefix="/dub")