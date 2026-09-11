import time

from backend.gemini import client, MODEL_NAME
from backend.schemas import SchemeAnalysis


SYSTEM_PROMPT = """
You are SchemeSarthi, an AI assistant that helps Indian citizens
understand government welfare schemes.

Your job is to analyze a government scheme document and determine
whether a specific citizen is likely eligible.

IMPORTANT RULES:

1. Use ONLY the information provided in the scheme document.
2. Never invent eligibility criteria, benefits, documents, or
   application procedures.
3. Compare the citizen's information against every relevant
   eligibility requirement.
4. If a mandatory requirement is clearly not satisfied, mark the
   citizen as likely_not_eligible.
5. If all known mandatory requirements are satisfied, mark the
   result as likely_eligible.
6. If a mandatory requirement cannot be evaluated because the
   citizen's information is missing, mark the result as
   cannot_determine.
7. Explain the reasons for the eligibility decision clearly.
8. List missing information separately.
9. For important claims, provide the source location from the
   document, such as "Page 4" or "Section: Eligibility".
10. Do not claim that the government has officially verified the
    citizen's eligibility. This is an AI assessment based on the
    supplied document.
11. Use simple, citizen-friendly language.
"""


def analyze_scheme(
    scheme_text: str,
    user_profile: dict
) -> SchemeAnalysis:

    prompt = f"""
{SYSTEM_PROMPT}

====================
GOVERNMENT SCHEME DOCUMENT
====================

{scheme_text}


====================
CITIZEN PROFILE
====================

{user_profile}


====================
TASK
====================

Analyze the scheme for this citizen.

Return:

- Scheme name
- Simple summary
- Eligibility status
- Clear reasons for the eligibility decision
- Missing information, if any
- Benefits
- Required documents
- Application steps
- Evidence/source references for important claims

Return ONLY the structured response matching the provided schema.
"""

    max_retries = 2

    for attempt in range(max_retries + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": SchemeAnalysis,
                },
            )

            return SchemeAnalysis.model_validate_json(response.text)

        except Exception as error:
            error_message = str(error)

            if (
                ("503" in error_message or "UNAVAILABLE" in error_message)
                and attempt < max_retries
            ):
                time.sleep(2)
                continue

            raise RuntimeError(
                "Scheme analysis is temporarily unavailable. "
                "Please try again in a moment."
            ) from error