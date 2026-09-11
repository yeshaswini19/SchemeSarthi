from backend.service import analyze_pdf_input


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


with open(PDF_PATH, "rb") as file:
    pdf_bytes = file.read()


result = analyze_pdf_input(
    file_bytes=pdf_bytes,
    user_profile=user_profile
)


print("\n===== SERVICE LAYER RESULT =====\n")
print(result.model_dump_json(indent=2))