import openai
import os
from dotenv import load_dotenv

# Load your .env file (make sure it exists with the API key inside)
load_dotenv()

# Set the API key securely
openai.api_key = os.getenv(
    "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")


def parse_with_ai(raw_text):
    prompt = (
        "Analyze this reconnaissance data and categorize it into:\n"
        "- Services\n- Vulnerabilities\n- Emails\n- Domains\n- Sensitive Info\n\n"
        f"Recon Data:\n{raw_text}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ OpenAI API Error: {str(e)}"
