def map_emotion_to_voice(emotion: str, intensity: float) -> dict:
    """
    Maps detected emotion to vocal characteristics.
    intensity is clamped between 0 and 1.
    """

    intensity = max(0.0, min(1.0, intensity))

    if emotion == "positive":
        return {
            "speaking_rate": round(1.05 + intensity * 0.25, 2),
            "volume_gain_db": round(1.0 + intensity * 3.0, 2),
            "pitch": round(2.0 + intensity * 4.0, 2),
            "style_note": "enthusiastic, upbeat, warm"
        }

    elif emotion == "negative":
        return {
            "speaking_rate": round(0.9 - intensity * 0.15, 2),
            "volume_gain_db": round(-1.0 - intensity * 2.0, 2),
            "pitch": round(-2.0 - intensity * 3.0, 2),
            "style_note": "calm, patient, reassuring"
        }

    return {
        "speaking_rate": 1.0,
        "volume_gain_db": 0.0,
        "pitch": 0.0,
        "style_note": "neutral, clear, professional"
    }