from elevenlabs.client import ElevenLabs
from app.config import settings
from app.services.tts_base import BaseTTSService

class ElevenLabsTTSService(BaseTTSService):
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
        self.voice_id = settings.ELEVENLABS_VOICE_ID

    def provider_name(self) -> str:
        return "elevenlabs"

    def synthesize(self, text: str, voice_params: dict, output_path: str) -> str:
        # ElevenLabs does not directly map exactly like Google pitch/rate/volume.
        # We approximate with stability / similarity / style controls.
        pitch = voice_params.get("pitch", 0.0)
        speaking_rate = voice_params.get("speaking_rate", 1.0)

        stability = 0.45
        similarity_boost = 0.75
        style = 0.35

        if pitch > 1:
            style = min(1.0, style + 0.2)

        if speaking_rate < 0.95:
            stability = min(1.0, stability + 0.15)

        audio = self.client.text_to_speech.convert(
            voice_id=self.voice_id,
            model_id="eleven_multilingual_v2",
            text=text,
            output_format="mp3_44100_128",
            voice_settings={
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style,
                "use_speaker_boost": True
            }
        )

        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        return output_path