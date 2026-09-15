# 🇮🇳 SchemeSarthi

### AI-Powered Government Scheme Eligibility & Assistance Platform

> **Government schemes, explained simply.**

SchemeSarthi helps citizens understand complex government scheme documents and determine their **likely eligibility** based on their personal profile.

Instead of forcing users to read lengthy government documents and interpret eligibility rules themselves, SchemeSarthi converts scheme information into a **simple, personalized and actionable explanation**.

---

## 🎯 Problem

India has numerous government welfare schemes, but many citizens struggle to understand:

- Who is eligible?
- What benefits are available?
- Which documents are required?
- How can I apply?
- Does this scheme apply to me?

Government scheme documents can be lengthy, technical and difficult to interpret.

### The problem is not a lack of information — it is the accessibility of information.

---

## 💡 Our Solution

SchemeSarthi acts as an **AI-powered interpretation layer** between government scheme documents and citizens.

The platform takes:

**Government Scheme Document + Citizen Profile**

and converts them into:

**Personalized Eligibility Assessment + Actionable Guidance**

---

## 🔄 How SchemeSarthi Works

### 1. Provide a Scheme

Users can either:

- 📄 Upload a government scheme PDF
- 📝 Paste government scheme text

### 2. Provide Citizen Details

The user provides relevant profile information such as:

- Age
- Gender
- State
- Annual income
- Citizenship
- Other scheme-specific information

### 3. AI Understands the Scheme

The extracted scheme content is sent to **Sarvam-105B**, which identifies:

- Eligibility criteria
- Benefits
- Required documents
- Application procedure
- Important scheme information

### 4. Personalized Eligibility Assessment

The citizen profile is compared against the eligibility requirements.

The system returns one of three statuses:

- ✅ `likely_eligible`
- ❌ `likely_not_eligible`
- ⚠️ `cannot_determine`

If required information is missing, SchemeSarthi does **not** guess. It returns `cannot_determine` and identifies the missing information.

### 5. Evidence & Explanation

Important claims are accompanied by source references such as:

- Page numbers
- Document sections
- Eligibility sections
- Benefit sections
- Application sections

whenever the supplied document makes those references available.

### 6. Regional-Language Translation

The generated result can be translated using **Sarvam Translate** into supported Indian languages.

---

## ✨ Key Features

### 📄 PDF & Text Input

Upload a government scheme PDF or directly paste scheme text.

### 🤖 AI-Powered Scheme Understanding

Uses **Sarvam-105B** to understand complex government scheme documents.

### 👤 Personalized Eligibility Assessment

The system compares the scheme's requirements against the citizen's profile.

### 🔎 Evidence-Based Results

Important claims include document-based evidence/source references whenever available.

### 📋 Structured Information Extraction

Automatically extracts:

- Scheme name
- Simple summary
- Eligibility criteria
- Benefits
- Required documents
- Application steps
- Evidence/source references

### ⚠️ Missing Information Detection

If a mandatory eligibility requirement cannot be evaluated because the citizen has not provided the required information, the system returns:

> **Cannot Determine**

instead of making an unsupported eligibility claim.

### 🌐 Indian Language Support

Results can currently be translated into:

- 🇬🇧 English
- 🇮🇳 Hindi
- తెలుగు Telugu
- தமிழ் Tamil
- ಕನ್ನಡ Kannada
- മലയാളം Malayalam

using **Sarvam Translate**.

### 🔐 Backend API Key Protection

The Sarvam API key is kept on the backend and is never exposed directly to the frontend.

---

# 🏗️ System Architecture

```text
                        SCHEMESARTHI
                             │
                             ▼
                 ┌─────────────────────┐
                 │      Frontend       │
                 │   HTML / CSS / JS   │
                 └──────────┬──────────┘
                            │
                            │ REST API
                            ▼
                 ┌─────────────────────┐
                 │       FastAPI       │
                 │     REST Backend    │
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
      ┌────────────────┐          ┌────────────────┐
      │ PDF Processing │          │ Citizen Profile│
      │                │          │                │
      │ pdfplumber     │          │ Age            │
      │ pypdf          │          │ Gender         │
      │                │          │ Income         │
      └───────┬────────┘          │ State          │
              │                   │ Citizenship    │
              │                   └───────┬────────┘
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Sarvam-105B     │
                 │   Scheme Analysis   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Structured JSON   │
                 │   JSON Schema       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Pydantic       │
                 │ Response Validation │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Sarvam Translate   │
                 │  Regional Languages │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Personalized Result │
                 │       to User       │
                 └─────────────────────┘
🧠 AI Pipeline

The core AI workflow is:

Government Scheme PDF / Text
            │
            ▼
     Text Extraction
    pdfplumber / pypdf
            │
            ▼
      Scheme Content
            │
            ├───────────────┐
            │               │
            ▼               ▼
     Citizen Profile    Scheme Rules
            │               │
            └───────┬───────┘
                    ▼
             Sarvam-105B
                    │
                    ▼
        Structured JSON Output
                    │
                    ▼
             Pydantic Validation
                    │
                    ▼
       Personalized Eligibility
             Assessment
                    │
                    ▼
           Sarvam Translate
                    │
                    ▼
       Citizen-Friendly Result
🛠️ Complete Tech Stack
Layer	Technology
Frontend	HTML5, CSS3, Vanilla JavaScript
Backend	Python
API Framework	FastAPI
ASGI Server	Uvicorn
AI Model	Sarvam-105B
Translation	Sarvam Translate
PDF Processing	pdfplumber, pypdf
Data Validation	Pydantic
AI Output Format	JSON Schema Structured Outputs
API Communication	REST API, Fetch API
Environment Management	python-dotenv
Secrets	Environment Variables
Version Control	Git
Repository	GitHub
Deployment Target	Render
🤖 AI Model — Sarvam-105B

Sarvam-105B is the core intelligence layer of SchemeSarthi.

It is responsible for understanding the supplied government scheme and producing structured information.

The model performs:
Scheme summarization
Eligibility interpretation
Citizen-profile comparison
Benefit extraction
Document extraction
Application-step extraction
Evidence identification
Missing-information detection

The application does not train or fine-tune the model.

Instead, SchemeSarthi uses:

Prompt Engineering + Structured Outputs + Validation

to make the model output predictable and application-ready.

📦 Structured AI Output

The AI does not return unrestricted free-form text.

The application defines a structured schema containing:

SchemeAnalysis
│
├── scheme_name
├── summary
├── eligibility
│   ├── status
│   ├── reasons
│   └── missing_information
├── benefits
├── documents
├── application_steps
└── evidence
    ├── claim
    └── source

This creates a clear contract between the AI layer and the application layer.

The generated JSON is then validated using Pydantic before being returned to the frontend.

📄 PDF Processing

SchemeSarthi supports text-based government PDFs.

Primary extractor

pdfplumber

Fallback extractor

pypdf

The extracted content preserves page markers where possible:

--- Page 1 ---

Scheme Name:
...

--- Page 2 ---

Eligibility:
...

--- Page 3 ---

Benefits:
...

These markers help the AI provide evidence/source references.

🌐 Multilingual Translation

SchemeSarthi uses Sarvam Translate after the main analysis is generated.

The flow is:

English Structured Result
          │
          ▼
   Sarvam Translate
          │
          ▼
User's Preferred Language

Current UI languages:

English
Hindi
Telugu
Tamil
Kannada
Malayalam

Translation is performed by the backend so that the Sarvam API key remains private.

🔌 API Endpoints
POST /analyze/pdf

Analyzes a government scheme PDF against a citizen profile.

Input
PDF file
+
Citizen profile
Output
Structured SchemeAnalysis
POST /analyze/text

Analyzes pasted scheme text against a citizen profile.

Input
Scheme text
+
Citizen profile
Output
Structured SchemeAnalysis
POST /translate

Translates generated content into a supported language.

Input
Text
+
Target language
Output
Translated text
🧠 Why We Did Not Use RAG

The current MVP does not use Retrieval-Augmented Generation (RAG).

Instead, SchemeSarthi uses direct context injection.

For the current workflow:

One Scheme Document
        │
        ▼
Extract Text
        │
        ▼
Send Document Content
+ Citizen Profile
        │
        ▼
Sarvam-105B
        │
        ▼
Personalized Analysis

There is currently no:

Vector database
Embedding pipeline
Retriever
FAISS
Pinecone
ChromaDB
Why?

The hackathon MVP processes one supplied scheme document at a time.

Introducing a retrieval layer would add unnecessary complexity for this workflow.

RAG would become more appropriate if SchemeSarthi evolves into a large searchable repository containing thousands of government schemes.

🔐 Security

SchemeSarthi keeps external API credentials on the backend.

The frontend never directly accesses the Sarvam API using the secret API key.

Environment variables are used for local development:

SARVAM_API_KEY=your_sarvam_api_key
Important

Never commit:

.env

to GitHub.

The .env file should be included in .gitignore.

For deployment, the API key should be configured using the deployment platform's environment-variable settings.

🚀 Getting Started
Prerequisites

Install:

Python 3.10+
Git
A Sarvam API key
1. Clone the Repository
git clone https://github.com/yeshaswini19/SchemeSarthi.git
cd SchemeSarthi
2. Create a Virtual Environment
Windows PowerShell
python -m venv .venv

Activate it:

.venv\Scripts\Activate.ps1

You should see:

(.venv)

in your terminal.

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the project root:

SARVAM_API_KEY=your_sarvam_api_key

Do not commit this file.

5. Start the FastAPI Backend

From the project root:

uvicorn backend.api:app --reload

The backend will run at:

http://127.0.0.1:8000

FastAPI interactive API documentation is available at:

http://127.0.0.1:8000/docs
6. Open the Frontend

Open:

frontend/index.html

in a browser.

The frontend communicates with the FastAPI backend.

📁 Project Structure
SchemeSarthi/
│
├── backend/
│   ├── __init__.py
│   ├── api.py
│   ├── analyzer.py
│   ├── input_processor.py
│   ├── pdf_processor.py
│   ├── schemas.py
│   ├── service.py
│   └── translation.py
│
├── frontend/
│   └── index.html
│
├── tests/
│   └── ...
│
├── .gitignore
├── README.md
├── requirements.txt
└── .env

.env should exist locally but must not be committed to the repository.

🧪 Testing

The application can be tested using:

Text Input

Paste a scheme document into the text input and provide a citizen profile.

PDF Input

Upload a text-based government scheme PDF.

Language Testing

Run the same analysis in:

English
Hindi
Telugu
Tamil
Kannada
Malayalam
Eligibility Testing

Test all three possible outcomes:

likely_eligible
likely_not_eligible
cannot_determine

The cannot_determine state is particularly important because the system should not infer eligibility when mandatory information is unavailable.

🛡️ Responsible AI Approach

SchemeSarthi is designed to avoid overclaiming.

The AI is instructed to:

Use only the supplied scheme document.
Avoid inventing eligibility criteria.
Avoid inventing benefits.
Avoid inventing required documents.
Avoid inventing application procedures.
Compare the citizen profile against the available requirements.
Identify missing information.
Provide evidence/source references where possible.
Return cannot_determine when required information is unavailable.
Never claim that the government has officially verified the citizen's eligibility.

The application also validates the generated response against a structured Pydantic schema.

⚠️ Limitations

The current hackathon MVP has several limitations.

1. Scanned PDFs

Image-only or scanned PDFs are not currently processed with OCR.

OCR is planned as a future enhancement.

2. AI-Assisted Assessment

The eligibility result is an AI-assisted interpretation.

It is not an official government eligibility decision.

3. Document Quality

The quality of the result depends on:

Accuracy of the supplied document
Completeness of the document
Quality of extracted text
Information provided by the citizen
4. External API Dependency

The application depends on the availability of the Sarvam API.

5. Complex Eligibility Rules

Some schemes contain highly nuanced legal, geographic, financial or administrative conditions that may require verification with the relevant government authority.

6. No Independent Citizen Verification

The system relies on the information provided by the user.

It does not independently verify:

Income
Citizenship
Documents
Government records
Identity
🎯 What Makes SchemeSarthi Different?

SchemeSarthi is not simply a PDF summarizer.

A normal document summarizer answers:

"What does this scheme document say?"

SchemeSarthi aims to answer:

"What does this scheme mean for me?"

The core workflow is:

Government Scheme Document
          +
    Citizen Profile
          │
          ▼
Personalized Eligibility Assessment
          │
          ▼
Reasons
Benefits
Required Documents
Application Steps
Evidence
          │
          ▼
Citizen-Friendly Regional Language

The key differentiation is the document-to-personalized-assistance layer.

🏆 Hackathon Value

SchemeSarthi focuses on a practical citizen-facing problem:

Government information may exist, but understanding and acting on that information can still be difficult.

The project combines:

Generative AI
Document understanding
Personalized reasoning
Structured AI outputs
Evidence-based explanations
Indian-language translation
A lightweight API architecture

into a single workflow.

🔮 Future Enhancements
📄 Document Intelligence
OCR for scanned PDFs
Better page-level citations
Improved document chunking
Support for more document formats
Better handling of tables
🔍 Scheme Discovery
Search across government schemes
Personalized scheme recommendations
Scheme comparison
Automatic scheme matching
🌐 Language Accessibility
More Indian languages
Improved regional-language UI
Regional-language document processing
👤 Citizen Experience
User accounts
Saved schemes
Downloadable eligibility reports
Application tracking
Personalized dashboards
⚙️ Production Infrastructure
Persistent database
Caching
Rate limiting
Authentication
Asynchronous document processing
Monitoring and logging
AI provider fallback
Scalable cloud deployment
☁️ Deployment

The application can be deployed as a FastAPI web service.

Example deployment architecture
                    GitHub
                       │
                       ▼
              Cloud Deployment
                       │
                       ▼
                   FastAPI
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Sarvam-105B        Sarvam Translate
             │                   │
             └─────────┬─────────┘
                       ▼
                  SchemeSarthi

For deployment, configure:

SARVAM_API_KEY

as a secure environment variable on the hosting platform.

Do not upload or commit .env.

👥 Team

Built for DeverT-A-Thon '26.

Team Members
Yeshaswini Thatikunta
Vidhi Gehlot
Swathi Patil
📜 Disclaimer

SchemeSarthi provides an AI-assisted interpretation of information supplied by the user.

It does not constitute an official government eligibility decision.

Users should verify the final eligibility requirements, documents and application procedure with the relevant government authority before applying.