from dotenv import load_dotenv
from pathlib import Path
import os

# Force-load .env from project root
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

api_key = os.getenv("GROQ_API_KEY")

print("ENV PATH:", ENV_PATH)
print("API KEY LOADED:", api_key is not None)
print("API KEY (first 8 chars):", api_key[:8] if api_key else None)
