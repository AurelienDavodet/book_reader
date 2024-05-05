import os

from pdf_reader.utils import chunck_text, pdf_extraction, text_to_speech

def converter(pdf: str):

    # Chemin du dossier que vous souhaitez créer
    audio_folder = '../data/audio'

    # Vérifie si le dossier n'existe pas déjà
    if not os.path.exists(audio_folder):
        # Crée le audio_folder
        os.makedirs(audio_folder)

    pdf_name = os.path.splitext(os.path.basename(pdf.name))[0]
    text = pdf_extraction(pdf)

    segments = chunck_text(text)

    audios = text_to_speech(segments, pdf_name, audio_folder)

    # output_path = f"../data/{pdf_name}_combined.mp3"
    # concatenate_audio_moviepy(audios, output_path)

    return audios