from backend.pdf_processor import extract_pdf_text


def process_pdf(file_bytes: bytes) -> str:
    """Convert uploaded PDF bytes into text with page references."""

    text = extract_pdf_text(file_bytes)

    if not text.strip():
        raise ValueError("No readable text found in the PDF.")

    return text


def process_text(text: str) -> str:
    """Process directly entered scheme text."""

    if not text or not text.strip():
        raise ValueError("Scheme text cannot be empty.")

    return text.strip()