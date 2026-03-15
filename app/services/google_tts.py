from google.cloud import texttospeech
from app.services.tts_base import BaseTTSService

class GoogleTTSService(BaseTTSService):
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def provider_name(self) -> str:
        return "google"

    def synthesize(self, text: str, voice_params: dict, output_path: str) -> str:
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-F"
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=voice_params.get("speaking_rate", 1.0),
            pitch=voice_params.get("pitch", 0.0),
            volume_gain_db=voice_params.get("volume_gain_db", 0.0)
        )

        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        with open(output_path, "wb") as out:
            out.write(response.audio_content)

        return output_path