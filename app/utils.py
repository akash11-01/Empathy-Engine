import os
from datetime import datetime

def ensure_output_dir(path: str):
    os.makedirs(path, exist_ok=True)

def build_output_filename(output_dir: str, emotion: str, extension: str = "mp3") -> tuple:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"empathy_{emotion}_{timestamp}.{extension}"
    filepath = os.path.join(output_dir, filename)
    return filename, filepath