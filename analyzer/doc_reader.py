from docx import Document

def read_doc(file_path):
    doc = Document(file_path)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():
            content.append(para.text.strip())
    return content
