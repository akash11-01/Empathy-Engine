from app.config import settings
from app.services.google_tts import GoogleTTSService
from app.services.elevenlabs_tts import ElevenLabsTTSService

def get_tts_service():
    if settings.TTS_PROVIDER == "elevenlabs":
        return ElevenLabsTTSService()
    return GoogleTTSService()