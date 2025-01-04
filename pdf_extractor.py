import pdfplumber
import re

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    # Clean the extracted text
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text
