import io
import pdfplumber

MIN_TEXT_LENGTH = 200

def extract_text_from_pdf(file_content: bytes) ->str:
    text_chunks = []
    with pdfplumber.open(io.BytesIO(file_content)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_chunks.append(text)
    return "\n".join(text_chunks)


def is_text_readable(text: str) -> bool:
    return len(text.strip()) >= MIN_TEXT_LENGTH