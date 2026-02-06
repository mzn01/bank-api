import psycopg2
try:
    conn = psycopg2.connect(
        dbname="bank",
        user="postgres",
        password="dbpass123",
        host="localhost",
        port="5432"
    )
    print("Successfully connected to the Bank Database!")

    cur = conn.cursor()

    cur.execute("SELECT * FROM accounts;")

    rows = cur.fetchall()

    print("\n--- Data from Postgres ---")
    for row in rows:
        print(f"User: {row[1]} | Balance: {row[2]}")

    cur.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")