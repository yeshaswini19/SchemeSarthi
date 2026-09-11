from backend.analyzer import analyze_scheme


scheme = """
Kisan Support Scheme

The scheme provides financial assistance of Rs. 6000 per year
to eligible small and marginal farmers.

Eligibility:
1. Applicant must be a farmer.
2. Applicant must own agricultural land.
3. Applicant must be a resident of India.

Benefits:
Eligible farmers receive Rs. 6000 per year.

Documents required:
- Aadhaar card
- Land ownership document
- Bank account details

Application:
Applicants should apply through the designated government
agriculture portal.
"""


user = {
    "age": 24,
    "state": "Telangana",
    "occupation": "Farmer",
    "annual_income": "Rs. 1.5 lakh",
    "land_ownership": True,
    "residency": "India"
}


result = analyze_scheme(scheme, user)

print("\n===== SCHEME ANALYSIS =====\n")
print(result.model_dump_json(indent=2))