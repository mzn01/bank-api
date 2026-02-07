import psycopg2

DB_URL = "postgresql://bank_db_7rdt_user:NHdh8ZhbivZ62G771Kf7VtxHzkiTR4Xo@dpg-d62une0gjchc73c1hltg-a.singapore-postgres.render.com/bank_db_7rdt"

try:
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS accounts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        balance FLOAT,
        interest_rate FLOAT

        );
        """
    cur.execute(create_table_query)
    conn.commit()

    print("Sucess")

    cur.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")    