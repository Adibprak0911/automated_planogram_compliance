import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect(
        dbname="my_new_database",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    conn.autocommit = True
    cur = conn.cursor()

    # Your database operations here

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)


# Create authors table
create_authors_table_query = sql.SQL("""
    CREATE TABLE authors (
        author_id SERIAL PRIMARY KEY,
        author_name VARCHAR(100) NOT NULL
    )
""")

# Create books table with a foreign key reference to authors table
create_books_table_query = sql.SQL("""
    CREATE TABLE books (
        book_id SERIAL PRIMARY KEY,
        book_title VARCHAR(255) NOT NULL,
        author_id INTEGER REFERENCES authors(author_id)
    )
""")


try:
    # Execute the queries
    cur.execute(create_authors_table_query)
    cur.execute(create_books_table_query)

    print("Tables created successfully.")

except psycopg2.Error as e:
    print("Error executing SQL queries:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
