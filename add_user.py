import psycopg2

name = input('Enter new user name: ')
balance = float(input('Enter current balance: '))


try: 

    conn = psycopg2.connect(
        dbname="bank", user="postgres", password="dbpass123", host="localhost"
    )

    cur = conn.cursor()
     

    query = "INSERT INTO accounts (name, balance, interest_rate) VALUES (%s, %s, %s);"


    cur.execute(query, (name, balance, 0.05))

    conn.commit()
    print(f"Added {name} to the Vault")

    cur.close()
    conn.close()


except Exception as e:
    print(f"Error: {e}")

