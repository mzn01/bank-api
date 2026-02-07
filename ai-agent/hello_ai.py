import os
from dotenv import load_dotenv
from google import genai 

# 1. Load key
load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

print("------------------------------------------------")
print("✅ SUCCESS: Using the NEW 'google-genai' library.")
print("------------------------------------------------")

try:
    # 2. Connect to the Client
    client = genai.Client(api_key=my_api_key)

    # 3. Ask the question
    print("🤖 Asking Gemini 1.5 Flash...")
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents="Explain 'AI Agents' in one sentence."
    )
    
    # 4. Print result
    print(f"✅ Gemini says: {response.text}")

except Exception as e:
    print(f"❌ Error: {e}")