import pdfplumber
from docx import Document

def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text_from_txt(txt_file):
    with open(txt_file, "r", encoding="utf-8") as f:
        return f.read()


def extract_text(file_path, file_type):
    file_type = file_type.lower()

    if file_type == "pdf":
        return extract_text_from_pdf(file_path)

    elif file_type == "docx":
        return extract_text_from_docx(file_path)

    elif file_type == "txt":
        return extract_text_from_txt(file_path)

    else:
        raise ValueError(f"Unsupported file format: {file_type}")
