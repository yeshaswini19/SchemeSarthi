from backend.gemini import ask_gemini


prompt = """
You are SchemeSarthi, an AI assistant that helps Indian citizens
understand government welfare schemes.

Explain in exactly 3 simple bullet points what a government
welfare scheme is.
"""


result = ask_gemini(prompt)

print("\n===== GEMINI RESPONSE =====\n")
print(result)