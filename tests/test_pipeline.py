from backend.pipeline import analyze_pdf


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


result = analyze_pdf(
    pdf_path=PDF_PATH,
    user_profile=user_profile
)


print("\n===== SCHEMESARTHI RESULT =====\n")
print(result.model_dump_json(indent=2))