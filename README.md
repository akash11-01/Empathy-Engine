# Empathy Engine

Empathy Engine is a Python-based AI voice application that converts plain text into emotionally modulated speech. The system detects sentiment in input text, maps emotion to vocal characteristics, and synthesizes expressive audio using ElevenLabs.

## Features

- Accepts text input from:
  - Web UI
  - REST API
- Detects emotion in text using VADER sentiment analysis
- Supports emotional categories:
  - Positive
  - Negative
  - Neutral
- Dynamically adjusts vocal parameters:
  - Speaking rate
  - Pitch
  - Volume gain
- Generates playable `.mp3` output
- Provides:
  - Browser-based playback
  - Direct audio file URL
- Supports TTS provider:
  - ElevenLabs

## Project Objective

Standard text-to-speech often sounds monotonic and robotic. Empathy Engine bridges the gap between text sentiment and expressive speech output so responses sound enthusiastic, patient, calm, or neutral based on emotional tone.

## Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML + Jinja2 + CSS
- **Emotion Detection:** VADER Sentiment
- **TTS Provider:** ElevenLabs
- **Language:** Python

## Setup Instructions

Follow these steps to run Empathy Engine locally.

### 1) Clone the Repository

```bash
git clone https://github.com/akash11-01/Empathy-Engine.git
cd empathy-engine
```

### 2) Create and Activate a Virtual Environment

This creates an isolated Python environment for dependencies.

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3) Install Dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure Environment Variables

Create a `.env` file in the project root and add:

```env
TTS_PROVIDER=elevenlabs
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_VOICE_ID=EXAVITQu4vr4xnSDxMaL
```

### 5) Run the Application

```bash
uvicorn app.main:app --reload
```

### 6) Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## Design Choices

### 1) Emotion Detection

The project uses **VADER Sentiment Analysis** because it is:

- Lightweight
- Fast
- Easy to integrate
- Suitable for classifying text into positive, negative, and neutral categories

This makes it a strong fit for a fast, practical implementation of emotion-aware speech generation.

### 2) Backend and Interface

The project uses **FastAPI** because it provides:

- Clean and simple backend development
- Built-in request validation
- Easy API creation
- Easy integration with HTML templates

This allows the project to support both a user-facing web interface and a JSON API in the same application.

### 3) TTS Provider

The final working version uses **ElevenLabs** because it produces more natural and expressive voice output than many standard TTS engines. This is especially useful for a project focused on empathy and emotional realism.

## Emotion-to-Voice Mapping Logic

A key design choice in this project is the explicit mapping from detected emotion to vocal behavior.

The system first determines:

- An emotion label
- An emotion intensity score

It then maps those values into voice parameters.

### Positive Emotion

For positive text:

- Speaking rate is increased
- Pitch tendency is increased
- Volume tendency is increased slightly
- Style is interpreted as upbeat, warm, and enthusiastic

This makes the output sound more energetic and expressive.

### Negative Emotion

For negative text:

- Speaking rate is reduced
- Pitch tendency is lowered
- Volume tendency is softened
- Style is interpreted as calm, patient, and reassuring

This makes the output sound more empathetic and composed.

### Neutral Emotion

For neutral text:

- Speaking rate remains near default
- Pitch remains stable
- Volume remains balanced
- Style remains clear and professional

This keeps the output natural without overemphasizing emotion.

## Notes on Mapping with ElevenLabs

The application computes provider-neutral parameters such as:

- Speaking rate
- Pitch tendency
- Volume tendency
- Style note

Since ElevenLabs uses its own internal expressive controls, these are translated into ElevenLabs-compatible settings such as:

- Stability
- Similarity boost
- Style
- Speaker boost

This preserves the emotional logic of the project while taking advantage of ElevenLabs’ natural voice quality.

## Conclusion

Empathy Engine demonstrates how sentiment analysis and voice synthesis can be combined to make AI speech more expressive and emotionally aligned. Instead of simply reading text aloud, the system attempts to reflect the emotional meaning of the message in how it is spoken.

This creates a more engaging and human-centered voice experience, especially in AI-driven communication scenarios where tone and trust matter.
