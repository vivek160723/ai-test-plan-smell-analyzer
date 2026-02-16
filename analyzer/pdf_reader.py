import PyPDF2

def read_pdf(file_path):
    text_lines = []

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text = page.extract_text()
            if text:
                text_lines.extend(text.split("\n"))

    return text_lines
