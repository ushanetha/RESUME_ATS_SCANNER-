import os
from PyPDF2 import PdfReader
from docx import Document

class ResumeParser:
    def extract_text(self, path):
        ext = os.path.splitext(path)[1].lower()
        if ext == ".pdf":
            return "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
        if ext == ".docx":
            return "\n".join(p.text for p in Document(path).paragraphs)
        raise ValueError("Only PDF and DOCX are supported.")
