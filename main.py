from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
import os

class UserCreate(BaseModel):
    name: str
    balance: float



app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    if DATABASE_URL:
        return psycopg2.connect(DATABASE_URL)
    else:
        return psycopg2.connect(
            dbname="bank",
            user="postgres",
            password="dbpass123",
            host="localhost"
        )



@app.get("/")
def home():
    return {"message": "Welcome to the Bank of Maazin. Go to /users to see data."}

@app.get("/users")
def get_users():
    try:
        conn = get_db_connection()

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
        conn = get_db_connection()
        cur = conn.cursor()

        query = "INSERT INTO accounts (name, balance, interest_rate) VALUES (%s, %s, %s);"
        cur.execute(query, (user_data.name, user_data.balance, 0.05))

        conn.commit()
        
        cur.close()
        conn.close()

        return {"message": f"User {user_data.name} added successfully!"}
    
    except Exception as e:
        return {"error": str(e)}

