from dotenv import load_dotenv
import os
from groq import Groq

# Load .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY not found in .env")

print("✅ API key loaded")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Explain RAG in one simple paragraph."}
    ]
)

print("\n--- MODEL RESPONSE ---\n")
print(response.choices[0].message.content)
