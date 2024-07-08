
import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    conn.autocommit = True  # Set autocommit mode to True

    cur = conn.cursor()

    new_db_name = "my_new_database"
    create_database_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name))
    
    cur.execute(create_database_query)

    print(f"Database '{new_db_name}' created successfully.")

except psycopg2.Error as e:
    print("Error creating PostgreSQL database:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()



