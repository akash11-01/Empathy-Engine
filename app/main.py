import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import settings
from app.schemas import SynthesizeResponse
from app.emotion import detect_emotion
from app.mapper import map_emotion_to_voice
from app.utils import ensure_output_dir, build_output_filename
from app.services.tts_factory import get_tts_service

app = FastAPI(title=settings.APP_NAME)

ensure_output_dir(settings.OUTPUT_DIR)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/output", StaticFiles(directory="output"), name="output")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": None,
        "error": None
    })


@app.post("/", response_class=HTMLResponse)
async def synthesize_from_form(request: Request, text: str = Form(...)):
    text = text.strip()

    if not text:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": None,
            "error": "Please enter some text."
        })

    try:
        emotion_result = detect_emotion(text)
        emotion = emotion_result["emotion"]
        intensity = emotion_result["intensity"]

        voice_params = map_emotion_to_voice(emotion, intensity)

        tts_service = get_tts_service()
        filename, filepath = build_output_filename(
            settings.OUTPUT_DIR,
            emotion,
            extension="mp3"
        )

        tts_service.synthesize(
            text=text,
            voice_params=voice_params,
            output_path=filepath
        )

        result = {
            "text": text,
            "emotion": emotion,
            "intensity": round(intensity, 3),
            "voice_params": voice_params,
            "provider": tts_service.provider_name(),
            "audio_file": filepath,
            "audio_url": f"/output/{filename}"
        }

        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": result,
            "error": None
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": None,
            "error": f"Error generating speech: {str(e)}"
        })


@app.post("/api/synthesize", response_model=SynthesizeResponse)
async def synthesize_api(request_body: dict):
    text = request_body.get("text", "").strip()

    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    emotion_result = detect_emotion(text)
    emotion = emotion_result["emotion"]
    intensity = emotion_result["intensity"]

    voice_params = map_emotion_to_voice(emotion, intensity)

    tts_service = get_tts_service()
    filename, filepath = build_output_filename(
        settings.OUTPUT_DIR,
        emotion,
        extension="mp3"
    )

    tts_service.synthesize(
        text=text,
        voice_params=voice_params,
        output_path=filepath
    )

    return SynthesizeResponse(
        text=text,
        emotion=emotion,
        intensity=round(intensity, 3),
        voice_params=voice_params,
        provider=tts_service.provider_name(),
        audio_file=filepath,
        audio_url=f"/output/{filename}"
    )