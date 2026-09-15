import json
import os
import time

from dotenv import load_dotenv
from sarvamai import SarvamAI

from backend.schemas import SchemeAnalysis

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")

if not API_KEY:
    raise ValueError("SARVAM_API_KEY is not set in .env")

client = SarvamAI(api_subscription_key=API_KEY)

MODEL_NAME = "sarvam-105b"

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


def analyze_scheme(scheme_text: str, user_profile: dict) -> SchemeAnalysis:

    prompt = f"""
{SYSTEM_PROMPT}

====================
GOVERNMENT SCHEME DOCUMENT
====================

{scheme_text}

====================
CITIZEN PROFILE
====================

{json.dumps(user_profile, ensure_ascii=False, indent=2)}

====================
TASK
====================

Analyze the scheme for this citizen.

Populate EVERY field in the output schema whenever the
information is available in the scheme document.

Requirements:

- scheme_name:
  Extract the official scheme name.

- summary:
  Give a short, simple citizen-friendly explanation.

- eligibility:
  Determine whether the citizen is likely eligible,
  likely not eligible, or whether eligibility cannot be
  determined.

- benefits:
  MUST contain every benefit explicitly stated in the
  scheme document. Do not leave this empty if benefits
  are present in the document.

- documents:
  MUST contain every required document explicitly stated
  in the scheme document. Do not leave this empty if
  documents are present.

- application_steps:
  MUST contain the application procedure explicitly
  stated in the scheme document. Include all important
  steps available in the document.

- evidence:
  Provide evidence/source references for important claims.
  Use the page number or section name from the supplied
  document whenever available.

IMPORTANT:

Never move information that belongs in benefits,
documents, or application_steps into evidence instead.
Those fields must contain the actual extracted information.

Only leave a field empty when that information is genuinely
not present in the scheme document.

Do not invent information.

Return ONLY the JSON object matching the required schema."""

    schema = SchemeAnalysis.model_json_schema()

    for attempt in range(3):
        try:
            response = client.chat.completions(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.2,
                reasoning_effort=None,
                max_tokens=4096,
                request_options={
                    "additional_body_parameters": {
                        "response_format": {
                            "type": "json_schema",
                            "json_schema": {
                                "name": "scheme_analysis",
                                "description": "Structured SchemeSarthi scheme analysis",
                                "schema": schema,
                                "strict": True,
                            },
                        }
                    }
                },
            )

            raw_content = response.choices[0].message.content

            parsed = json.loads(raw_content)

            return SchemeAnalysis.model_validate(parsed)

        except Exception as error:
            error_message = str(error)

            print("SARVAM ERROR:", repr(error))

            if attempt < 2:
                time.sleep(2 ** attempt)
                continue

            raise RuntimeError(
                "Scheme analysis is temporarily unavailable. "
                "Please try again in a moment."
            ) from error