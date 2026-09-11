import io

import pdfplumber
from pypdf import PdfReader


def extract_pdf_text(pdf_bytes: bytes) -> str:
    """
    Extract text from a PDF.

    Returns text with page numbers so that important
    information can later be traced back to the source.
    """

    pages = []

    # Primary extraction using pdfplumber
    try:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                text = page.extract_text() or ""

                if text.strip():
                    pages.append(
                        f"\n--- Page {page_number} ---\n{text.strip()}"
                    )

        if pages:
            return "\n".join(pages)

    except Exception:
        pass

    # Fallback extraction using pypdf
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            if text.strip():
                pages.append(
                    f"\n--- Page {page_number} ---\n{text.strip()}"
                )

        return "\n".join(pages)

    except Exception as e:
        raise ValueError(f"Could not extract text from PDF: {e}")