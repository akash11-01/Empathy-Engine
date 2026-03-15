# Empathy Engine

Empathy Engine is a Python-based AI voice application that converts plain text into emotionally modulated speech. The system detects the sentiment of the input text, maps that emotion to vocal characteristics, and then synthesizes expressive audio using a cloud TTS provider ElevenLabs.

## Features

- Accepts text input from:
  - Web UI
  - REST API
- Detects emotion in text using VADER sentiment analysis
- Supports at least three emotional categories:
  - Positive
  - Negative
  - Neutral
- Dynamically adjusts vocal parameters:
  - Speaking rate
  - Pitch
  - Volume gain
- Generates playable `.mp3` audio output
- Provides:
  - Browser-based playback
  - Direct audio file URL
- Supports multiple TTS providers:
  - ElevenLabs

---

## Project Objective

Standard text-to-speech often sounds monotonic and robotic. The goal of Empathy Engine is to bridge the gap between text sentiment and expressive speech output by making AI voice responses sound more enthusiastic, patient, calm, or neutral depending on the emotional tone of the text.

---

## Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML + Jinja2 + CSS
- **Emotion Detection:** VADER Sentiment
- **TTS Provider:**
  - ElevenLabs
- **Language:** Python

---

## Project Structure

```bash
empathy-engine/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── emotion.py
│   ├── mapper.py
│   ├── schemas.py
│   ├── utils.py
│   ├── services/
│   │   ├── tts_base.py
│   │   ├── google_tts.py
│   │   ├── elevenlabs_tts.py
│   │   └── tts_factory.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── output/
├── .env
├── requirements.txt
└── README.md
```
