# document_processing.py

import re
from PyPDF2 import PdfReader

def read_pdf(file_path):
    """Read text from a PDF file."""
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def remove_special_characters(text):
    """Remove special characters from text."""
    processed_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove non-alphanumeric characters except spaces
    return processed_text

def normalize_text(text):
    """Normalize text by converting to lowercase."""
    return text.lower()

def process_document(file_path):
    """Process an individual document."""
    text = read_pdf(file_path)
    cleaned_text = remove_special_characters(text)
    cleaned_text = normalize_text(cleaned_text)
    return cleaned_text