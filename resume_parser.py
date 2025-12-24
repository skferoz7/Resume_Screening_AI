
import PyPDF2, docx

def extract_text(path):
    if path.endswith(".pdf"):
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for p in reader.pages:
                if p.extract_text():
                    text += p.extract_text()
        return text

    if path.endswith(".docx"):
        doc = docx.Document(path)
        return " ".join([p.text for p in doc.paragraphs])

    return ""
