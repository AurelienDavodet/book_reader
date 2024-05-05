import streamlit as st
from pdf_reader.conversion import converter
from pathlib import Path


st.title("PDF Reader")

uploaded_file = st.file_uploader("Choose a pdf", type="pdf")

if uploaded_file is not None:
    audios = converter(uploaded_file)
    for audio in audios:
        st.audio(audio, format="audio/mpeg", loop=True)