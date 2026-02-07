import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import tools  # <--- Importing your "Hands"

# 1. Setup
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_ID = "gemini-flash-latest"  # <--- The Winning Key

# 2. Prepare the Tools
# We wrap your Python functions so the AI can understand them
my_tools = [tools.get_all_users, tools.create_user_tool]

# 3. Create the Agent Chat
print(f"🤖 Initializing Agent with Model: {MODEL_ID}...")
chat = client.chats.create(
    model=MODEL_ID,
    config=types.GenerateContentConfig(
        tools=my_tools,  # Give the robot hands
        automatic_function_calling={"disable": False}, # Allow it to use them automatically
        system_instruction="You are a Bank Agent for 'Bank of Maazin'. You can check balances and create users. Be brief and professional."
    )
)

print("✅ Agent is Ready! (Type 'quit' to exit)")
print("-----------------------------------------")

# 4. The Conversation Loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    try:
        # Send the message. The library will:
        # 1. Detect if it needs a tool.
        # 2. Run the Python function (in tools.py).
        # 3. Get the result (from Render).
        # 4. Generate a natural language answer.
        response = chat.send_message(user_input)
        
        print(f"🤖 Agent: {response.text}")
        
    except Exception as e:
        print(f"❌ Error: {e}")