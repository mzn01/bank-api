from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    balance: float



app = FastAPI()

DB_CONFIG = {
    "dbname": "bank",
    "user": "postgres",
    "password": "dbpass123",
    "host": "localhost"
}

@app.get("/")
def home():
    return {"message": "Welcome to the Bank of Maazin. Go to /users to see data."}

@app.get("/users")
def get_users():
    try:
        conn = psycopg2.connect(**DB_CONFIG)

        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute("SELECT * FROM accounts;")
        users = cur.fetchall()

        cur.close()
        conn.close()

        return {"user": users}
    
    except Exception as e:
        return {"error": str(e)}



@app.post("/create_user")
def create_user(user_data: UserCreate):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        query = "INSERT INTO accounts (name, balance, interest_rate) VALUES (%s, %s, %s);"
        cur.execute(query, (user_data.name, user_data.balance, 0.05))

        conn.commit()
        
        cur.close()
        conn.close()

        return {"message": f"User {user_data.name} added successfully!"}
    
    except Exception as e:
        return {"error": str(e)}

