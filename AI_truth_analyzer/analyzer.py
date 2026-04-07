import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_text(user_input: str) -> str:
    prompt = f"""
You are an AI Truth Analyzer.

Analyze the following statement and provide:

1. Truth Likelihood (Low / Medium / High)
2. Reasoning (why it seems true or not)
3. Tone (e.g., confident, exaggerated, defensive)
4. Confidence Score (0-100%)

Be analytical and concise.

Statement:
{user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    return response.choices[0].message.content