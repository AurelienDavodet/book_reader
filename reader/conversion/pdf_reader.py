import PyPDF2


def pdf_extraction(pdf_path: int):
    pdf = PyPDF2.PdfReader(pdf_path)
    texts = []
    for page in pdf.pages:
        texts.append(page.extract_text())

    return " ".join(texts)
