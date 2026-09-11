import os
import re

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")

if not API_KEY:
    raise ValueError("SARVAM_API_KEY is not set in .env")

client = SarvamAI(api_subscription_key=API_KEY)

MODEL_NAME = "sarvam-translate:v1"

LANGUAGE_CODES = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Telugu": "te-IN",
    "Tamil": "ta-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
}


def _split_text(text: str, max_chars: int = 1900) -> list[str]:
    """
    Split long text into chunks below Sarvam's 2000-character limit.
    Prefer splitting at sentence boundaries.
    """
    if len(text) <= max_chars:
        return [text]

    chunks = []
    current = ""

    sentences = re.split(r"(?<=[.!?])\s+", text)

    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= max_chars:
            current = f"{current} {sentence}".strip()
        else:
            if current:
                chunks.append(current)

            if len(sentence) <= max_chars:
                current = sentence
            else:
                for i in range(0, len(sentence), max_chars):
                    chunks.append(sentence[i:i + max_chars])
                current = ""

    if current:
        chunks.append(current)

    return chunks


def translate_text(
    text: str,
    target_language: str,
    source_language: str = "en-IN",
) -> str:

    if not text or not text.strip():
        return text

    if target_language not in LANGUAGE_CODES:
        raise ValueError(
            f"Unsupported language: {target_language}"
        )

    target_code = LANGUAGE_CODES[target_language]

    if source_language == target_code:
        return text

    chunks = _split_text(text)
    translated_chunks = []

    for chunk in chunks:
        response = client.text.translate(
            input=chunk,
            source_language_code=source_language,
            target_language_code=target_code,
            model=MODEL_NAME,
        )

        translated_chunks.append(response.translated_text)

    return "\n".join(translated_chunks)