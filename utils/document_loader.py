import fitz
from docx import Document

def load_pdf(file):
    doc = fitz.open(stream=file.read(),filetype='pdf')
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_docx(file):
    doc = Document(file)
    text = ""
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def load_text(file):
    return file.read().decode('utf-8')

def chunk_text(text, chunk_size=300, overlaps=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlaps
    return chunks