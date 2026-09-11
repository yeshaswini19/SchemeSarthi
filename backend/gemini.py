import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env")


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.6-flash"


def ask_gemini(prompt: str, max_retries: int = 2) -> str:
    """
    Send a text prompt to Gemini.

    Retries temporary server errors before returning
    a clean user-facing error.
    """

    for attempt in range(max_retries + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
            )

            return response.text

        except Exception as error:
            error_message = str(error)

            # Retry temporary Gemini availability/server errors.
            if (
                ("503" in error_message or "UNAVAILABLE" in error_message)
                and attempt < max_retries
            ):
                time.sleep(2)
                continue

            raise RuntimeError(
                "Gemini is temporarily unavailable. "
                "Please try again in a moment."
            ) from error