import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Empathy Engine"
    TTS_PROVIDER = os.getenv("TTS_PROVIDER", "google").lower()

    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")

    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")

    OUTPUT_DIR = "output"

settings = Settings()