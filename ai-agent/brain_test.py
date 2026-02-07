import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# The list of keys to try
candidates = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest", 
    "gemini-flash-latest",
    "gemini-1.5-flash-002"
]

print("🧠 Testing Brain Connections...")

for model_name in candidates:
    print(f"\n🔑 Trying key: {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name, 
            contents="Are you online?"
        )
        print(f"✅ SUCCESS! We will use: '{model_name}'")
        print(f"🤖 Response: {response.text}")
        break  # Stop if it works!
    except Exception as e:
        if "429" in str(e):
            print("❌ Quota Exceeded (Too Busy)")
        elif "404" in str(e):
            print("❌ Not Found (Wrong Name)")
        else:
            print(f"❌ Error: {e}")

print("\n--- Test Complete ---")