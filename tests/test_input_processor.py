from backend.input_processor import process_pdf, process_text
from backend.analyzer import analyze_scheme


PDF_PATH = r"C:\Users\tyesh\Downloads\pmyojna.pdf"


user_profile = {
    "age": 24,
    "state": "Telangana",
    "occupation": "Farmer",
    "annual_income": "Rs. 1.5 lakh",
    "land_size": "1.5 hectares",
    "land_ownership": True,
    "residency": "India"
}


# =========================
# TEST PDF → AI ANALYSIS
# =========================

with open(PDF_PATH, "rb") as file:
    pdf_bytes = file.read()

scheme_text = process_pdf(pdf_bytes)

result = analyze_scheme(
    scheme_text=scheme_text,
    user_profile=user_profile
)

print("\n===== SCHEMESARTHI PDF RESULT =====\n")
print(result.model_dump_json(indent=2))


# =========================
# TEST TEXT → AI ANALYSIS
# =========================

text_scheme = """
Kisan Support Scheme

The scheme provides Rs. 6000 per year to small and marginal farmers.

Eligibility:
1. Applicant must be a farmer.
2. Applicant must own agricultural land up to 2 hectares.
3. Applicant must be a resident of India.

Documents:
- Aadhaar card
- Land ownership document
- Bank account details
"""

processed_text = process_text(text_scheme)

text_result = analyze_scheme(
    scheme_text=processed_text,
    user_profile=user_profile
)

print("\n===== SCHEMESARTHI TEXT RESULT =====\n")
print(text_result.model_dump_json(indent=2))