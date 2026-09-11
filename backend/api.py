from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from backend.translation import translate_text

from backend.service import analyze_pdf_input, analyze_text_input


app = FastAPI(
    title="SchemeSarthi API",
    description="AI-powered government scheme eligibility assistant",
    version="1.0.0",
)


# Allow the HTML frontend to communicate with this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "SchemeSarthi API",
    }


@app.post("/analyze/pdf")
async def analyze_pdf(
    file: UploadFile = File(...),
    user_profile: str = Form(...)
):
    """
    Analyze a government scheme uploaded as a PDF.

    user_profile is received as a JSON string from the frontend.
    """

    try:
        import json

        profile = json.loads(user_profile)

        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Please upload a PDF file."
            )

        pdf_bytes = await file.read()

        if not pdf_bytes:
            raise HTTPException(
                status_code=400,
                detail="The uploaded PDF is empty."
            )

        result = analyze_pdf_input(
            file_bytes=pdf_bytes,
            user_profile=profile,
        )

        return result.model_dump()

    except HTTPException:
        raise

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid user profile data."
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


@app.post("/analyze/text")
async def analyze_text(
    text: str = Form(...),
    user_profile: str = Form(...)
):
    """
    Analyze a government scheme provided as text.

    user_profile is received as a JSON string from the frontend.
    """

    try:
        import json

        profile = json.loads(user_profile)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="Scheme text cannot be empty."
            )

        result = analyze_text_input(
            text=text,
            user_profile=profile,
        )

        return result.model_dump()

    except HTTPException:
        raise

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Invalid user profile data."
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )
@app.post("/translate")
async def translate(
    text: str = Form(...),
    target_language: str = Form(...),
):
    """
    Translate citizen-facing SchemeSarthi text
    into a supported Indian language.
    """

    try:
        translated = translate_text(
            text=text,
            target_language=target_language,
        )

        return {
            "translated_text": translated,
            "language": target_language,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Translation failed: {error}",
        )