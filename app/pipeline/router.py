from app.pipeline.text_extractor import extract_text_from_pdf, is_text_readable
from app.pipeline.ocr import run_ocr


def extract_document_text(content: bytes) -> str:
    text = extract_text_from_pdf(content)

    if is_text_readable(text):
        return text

    # Fallback to OCR
    ocr_text = run_ocr(content)
    return ocr_text
