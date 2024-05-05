import PyPDF2
import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


def pdf_extraction(pdf):
    pdf = PyPDF2.PdfReader(pdf)
    texts = []
    for page in pdf.pages:
        texts.append(page.extract_text())

    return " ".join(texts)


def text_to_speech(segments: List, pdf_name: str, folder: str):

    client = OpenAI(api_key=SECRET_KEY)

    for i, segment in enumerate(segments):
        speech_file_path = f"{folder}/{pdf_name}_{i}.mp3"
        response = client.audio.speech.create(
            model="tts-1", voice="fable", input=segment
        )
        response.stream_to_file(speech_file_path)

    # Spécifier le chemin du dossier
    chemin_dossier = Path(folder)

    # Créer une liste des noms de fichiers
    noms_fichiers = [
        folder + '/' + f.name for f in chemin_dossier.iterdir() if f.is_file()
    ]
    
    return noms_fichiers


def chunck_text(texte):
    taille_segment = 4096
    segments = []
    debut = 0

    while debut < len(texte):
        # Ne coupe pas au milieu des mots si possible
        fin = debut + taille_segment
        if fin < len(texte) and texte[fin] != " " and texte[fin - 1] != " ":
            fin = (
                texte.rfind(" ", debut, fin) + 1
            )  # Trouve l'espace le plus proche pour éviter de couper un mot

        segments.append(texte[debut:fin].strip())  # Ajoute le segment actuel à la liste
        debut = fin  # Déplace le point de départ pour le prochain segment

    return segments


'''

from moviepy.editor import AudioFileClip, concatenate_audioclips

def concatenate_audio_moviepy(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`
    """
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)
'''