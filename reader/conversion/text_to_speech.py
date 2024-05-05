import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


def text_to_speech(segments: List, pdf_name: str):

    client = OpenAI(api_key=SECRET_KEY)

    for i, segment in enumerate(segments):
        speech_file_path = f"../../data/audio/{pdf_name}_{i}.mp3"
        response = client.audio.speech.create(
            model="tts-1", voice="fable", input=segment
        )
        response.stream_to_file(speech_file_path)

    from pathlib import Path

    # Spécifier le chemin du dossier
    chemin_dossier = Path("../../data/audio")

    # Créer une liste des noms de fichiers
    noms_fichiers = [
        "../../data/audio/" + f.name for f in chemin_dossier.iterdir() if f.is_file()
    ]
    
    return noms_fichiers
