import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("=== Resume Review Agent ===")

resume = input("\nPaste your resume:\n\n")

model = genai.GenerativeModel("models/gemini-3.8-flash")

response = model.generate_content(
    f"""
    You are an expert resume reviewer.

    Review this resume and provide:
    1. Strengths
    2. Weaknesses
    3. Missing skills
    4. ATS suggestions
    5. Score out of 10

    Resume:
    {resume}
    """
)

print("\n=== REVIEW ===\n")
print(response.text)