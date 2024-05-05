import os

from chunck import chunck_text
from pdf_reader import pdf_extraction
from text_to_speech import text_to_speech
# from audio_concatenation import concatenate_audio_moviepy

def conversion(pdf_path: str):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    text = pdf_extraction(pdf_path)

    segments = chunck_text(text)

    audios = text_to_speech(segments, pdf_name)

    output_path = f"../../data/{pdf_name}_combined.mp3"
    # concatenate_audio_moviepy(audios, output_path)
