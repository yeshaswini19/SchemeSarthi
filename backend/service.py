from backend.input_processor import process_pdf, process_text
from backend.analyzer import analyze_scheme
from backend.schemas import SchemeAnalysis


def analyze_pdf_input(file_bytes: bytes, user_profile: dict) -> SchemeAnalysis:
    scheme_text = process_pdf(file_bytes)

    if not scheme_text.strip():
        raise ValueError("No readable text found in the PDF.")

    return analyze_scheme(
        scheme_text=scheme_text,
        user_profile=user_profile,
    )


def analyze_text_input(text: str, user_profile: dict) -> SchemeAnalysis:
    scheme_text = process_text(text)

    return analyze_scheme(
        scheme_text=scheme_text,
        user_profile=user_profile,
    )