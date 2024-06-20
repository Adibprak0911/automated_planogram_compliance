import psycopg2
from psycopg2 import sql

# Database connection parameters
params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Database name
company_db = "company_db"

def database_exists(conn, dbname):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
    exists = cur.fetchone()
    cur.close()
    return exists is not None

def create_database(conn, dbname):
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
    cur.close()

def create_tables(conn):
    cur = conn.cursor()
    
    # Creating table for companies
    cur.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        type VARCHAR(50) NOT NULL CHECK (type IN ('softdrink', 'chips'))
    );
    """)

    # Creating table for flavors
    cur.execute("""
    CREATE TABLE IF NOT EXISTS flavors (
        id SERIAL PRIMARY KEY,
        company_id INTEGER REFERENCES companies(id),
        flavor VARCHAR(100) NOT NULL
    );
    """)

    conn.commit()
    cur.close()

def add_company(conn, name, type):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO companies (name, type) VALUES (%s, %s) RETURNING id",
        (name, type)
    )
    company_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return company_id

def add_flavor(conn, company_id, flavor):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO flavors (company_id, flavor) VALUES (%s, %s)",
        (company_id, flavor)
    )
    conn.commit()
    cur.close()

def get_flavors(conn, company_name):
    cur = conn.cursor()
    cur.execute("""
    SELECT f.flavor
    FROM flavors f
    JOIN companies c ON f.company_id = c.id
    WHERE c.name = %s
    """, (company_name,))
    flavors = cur.fetchall()
    cur.close()
    return [flavor[0] for flavor in flavors]

def main():
    # Connect to the default database to create new database
    conn = psycopg2.connect(**params)

    try:
        # Check if the database exists, if not create it
        if not database_exists(conn, company_db):
            create_database(conn, company_db)
        else:
            print(f"Database {company_db} already exists.")
    except Exception as e:
        print(f"An error occurred while checking/creating database: {e}")
    finally:
        conn.close()

    # Update params to connect to the new company database
    company_params = params.copy()
    company_params['dbname'] = company_db

    # Connect to the new company database and create tables
    conn_company = psycopg2.connect(**company_params)
    try:
        create_tables(conn_company)

        # Add companies and flavors
        lays_id = add_company(conn_company, 'LAYS', 'chips')
        add_flavor(conn_company, lays_id, 'Sour Cream & Onion')
        add_flavor(conn_company, lays_id, 'Barbecue')
        add_flavor(conn_company, lays_id, 'Classic')

        coca_cola_id = add_company(conn_company, 'Coca Cola', 'softdrink')
        add_flavor(conn_company, coca_cola_id, 'Classic')
        add_flavor(conn_company, coca_cola_id, 'Cherry')
        add_flavor(conn_company, coca_cola_id, 'Vanilla')

        # Fetch flavors for LAYS
        lays_flavors = get_flavors(conn_company, 'LAYS')
        print(f'LAYS flavors: {lays_flavors}')

        # Fetch flavors for Coca Cola
        coca_cola_flavors = get_flavors(conn_company, 'Coca Cola')
        print(f'Coca Cola flavors: {coca_cola_flavors}')
        
    except Exception as e:
        print(f"An error occurred while creating tables in the company database: {e}")
    finally:
        conn_company.close()

if __name__ == "__main__":
    main()
