from pathlib import Path

from backend.pdf_processor import extract_pdf_text


PDF_PATH = Path(r"C:\Users\tyesh\Downloads\pmyojna.pdf")


with open(PDF_PATH, "rb") as file:
    pdf_bytes = file.read()


text = extract_pdf_text(pdf_bytes)


print("\n===== PDF EXTRACTION TEST =====\n")
print(f"Characters extracted: {len(text)}")
print("\n===== FIRST 5000 CHARACTERS =====\n")
print(text[:5000])