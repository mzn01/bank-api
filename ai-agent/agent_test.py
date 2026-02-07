import os
from dotenv import load_dotenv
from google import genai

# 1. Load Credentials
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. Connect
client = genai.Client(api_key=api_key)

print("🤖 Connecting to Gemini 2.0 Flash Lite...")

try:
    # 3. Use the EXACT name from your list
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite", 
        contents="Start your sentence with 'Greetings human'. Explain what a Bank is."
    )
    print(f"\n✅ SUCCESS! Gemini says:\n{response.text}")

except Exception as e:
    print("\n❌ FAILED.")
    print(f"Error: {e}")