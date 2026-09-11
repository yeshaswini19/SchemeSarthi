from backend.input_processor import process_pdf, process_text
from backend.analyzer import analyze_scheme
from backend.schemas import SchemeAnalysis


def analyze_pdf_input(
    file_bytes: bytes,
    user_profile: dict
) -> SchemeAnalysis:
    """Analyze a government scheme provided as a PDF."""

    scheme_text = process_pdf(file_bytes)

    return analyze_scheme(
        scheme_text=scheme_text,
        user_profile=user_profile
    )


def analyze_text_input(
    text: str,
    user_profile: dict
) -> SchemeAnalysis:
    """Analyze a government scheme provided as plain text."""

    scheme_text = process_text(text)

    return analyze_scheme(
        scheme_text=scheme_text,
        user_profile=user_profile
    )