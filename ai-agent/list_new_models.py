import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("🔍 Asking the NEW SDK for available models...")

try:
    # This command is specific to the new library
    for m in client.models.list():
        print(f"✅ Found: {m.name}")
        
except Exception as e:
    print(f"❌ Error: {e}")