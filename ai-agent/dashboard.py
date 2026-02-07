import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import tools  # Your banking tools

# 1. Setup Page
st.set_page_config(page_title="AI Smart Bank", page_icon="🤖")
st.title("🤖 AI Banker: Talk to your Money")

# 2. Load Keys
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 3. Initialize Chat History (Memory)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "model", "content": "Hello! I am your AI Banker. I can create accounts and check balances. How can I help?"}
    ]

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. The Chat Input
prompt = st.chat_input("Type your request here (e.g., 'Create a user named Batman')")

if prompt:
    # A. Show User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # B. The AI Brain (Thinking...)
    with st.chat_message("model"):
        with st.spinner("Talking to the Bank Vault..."):
            try:
                # Connect to Gemini
                client = genai.Client(api_key=api_key)
                
                # Define Tools
                my_tools = [tools.get_all_users, tools.create_user_tool]
                
                # Create Chat Session
                # (Note: We use a stateless call here for simplicity in Streamlit)
                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        tools=my_tools,
                        automatic_function_calling={"disable": False},
                        system_instruction="You are a helpful Bank Agent. Use the tools to answer. Be concise."
                    )
                )
                
                # Show AI Response
                st.markdown(response.text)
                st.session_state.messages.append({"role": "model", "content": response.text})
                
            except Exception as e:
                st.error(f"Error: {e}")