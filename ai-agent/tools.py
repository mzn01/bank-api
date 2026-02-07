import requests 
import json

API_BASE_URL = "https://maazin-bank.onrender.com"

def get_all_users():
    try:
        response = requests.get(f"{API_BASE_URL}/users")
        if response.status_code == 200:
            return response.json()

        else:
            return f"Error: Bank API returned status {response.status_code}"
    except Exception as e:
        return f"Connection Failed: {e}"

def create_user_tool(name: str,balance:float):
    payload = {"name": name,"balance": balance}

    try:
        response = requests.post(f"{API_BASE_URL}/create_user", json=payload)
        return response.json()
    except Exception as e:
        return f"Failed to create user: {e}"

if __name__ == "__main__":
    print("Testin tools Manually...")

    print("\n1. Fetching Users...")
    users = get_all_users()
    print(users)

    print("\n2. Creating 'Agent Smith'...")
    result = create_user_tool("Agent Smith",100.0)
    print(result)
