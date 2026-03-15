from pydantic import BaseModel

class SynthesizeRequest(BaseModel):
    text: str

class SynthesizeResponse(BaseModel):
    text: str
    emotion: str
    intensity: float
    voice_params: dict
    provider: str
    audio_file: str
    audio_url: str