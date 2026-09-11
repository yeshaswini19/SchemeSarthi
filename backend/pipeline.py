from pathlib import Path

from backend.pdf_processor import extract_pdf_text
from backend.analyzer import analyze_scheme


def analyze_pdf(
    pdf_path: str,
    user_profile: dict
):
    """
    Complete PDF → SchemeSarthi analysis pipeline.
    """

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    with open(path, "rb") as file:
        pdf_bytes = file.read()

    # Step 1: Extract text from PDF
    scheme_text = extract_pdf_text(pdf_bytes)

    if not scheme_text.strip():
        raise ValueError("No readable text found in the PDF.")

    # Step 2: Analyze the scheme and citizen profile
    result = analyze_scheme(
        scheme_text=scheme_text,
        user_profile=user_profile
    )

    return result