import psycopg2

# Function to create the PostgreSQL database and table
def create_database():
    try:
        # Connect to default database or postgres database
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost"
        )
        
        conn.autocommit = True
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Create the database
        cursor.execute("CREATE DATABASE product_flavours")
        print("Database 'product_flavours' created successfully.")
        
        # Close the cursor and connection to default database
        cursor.close()
        conn.close()
        
        # Now connect to the newly created database
        conn = psycopg2.connect(
            dbname="product_flavours",
            user="postgres",
            password="postgres",
            host="localhost"
        )
        
        conn.autocommit = True

        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Create a table to store products and their flavours
        cursor.execute("""
            CREATE TABLE products (
                id SERIAL PRIMARY KEY,
                product_name VARCHAR(100) NOT NULL,
                flavour VARCHAR(100) NOT NULL
            )
        """)
        
        # Commit the table creation
        conn.commit()
        print("Table 'products' created successfully.")
        
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)
        
    finally:
        # Close the cursor and connection
        if conn:
            cursor.close()
            conn.close()

# Function to add product flavours to the database
def add_product_flavour(product_name, flavour):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="product_flavours",
            user="postgres",
            password="postgres",
            host="localhost"
        )
        conn.autocommit = True
        
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # SQL query to insert data into the table
        sql_query = "INSERT INTO products (product_name, flavour) VALUES (%s, %s)"
        
        # Execute the SQL command
        cursor.execute(sql_query, (product_name, flavour))
        
        # Commit your changes to the database
        conn.commit()
        print(f"Successfully added flavour '{flavour}' to '{product_name}'.")
        
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)
        
    finally:
        # Close the cursor and connection
        if conn:
            cursor.close()
            conn.close()

# Function to fetch flavours based on product name
def get_flavours(product_name):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="product_flavours",
            user="postgres",
            password="postgres",
            host="localhost"
        )
        conn.autocommit = True
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # SQL query to select flavours for a specific product
        sql_query = "SELECT flavour FROM products WHERE product_name = %s"
        
        # Execute the SQL command
        cursor.execute(sql_query, (product_name,))
        
        # Fetch all the rows
        flavours = cursor.fetchall()
        
        # Print flavours
        if flavours:
            print(f"Flavours of {product_name}:")
            for flavour in flavours:
                print(flavour[0])
        else:
            print(f"No flavours found for {product_name}.")
        
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)
        
    finally:
        # Close the cursor and connection
        if conn:
            cursor.close()
            conn.close()

# Main function to demonstrate usage
if __name__ == "__main__":
    create_database()
    
    # Adding sample data
    add_product_flavour('lays', 'original')
    add_product_flavour('lays', 'barbecue')
    add_product_flavour('lays', 'sour cream & onion')
    add_product_flavour('doritos', 'nacho cheese')
    add_product_flavour('doritos', 'cool ranch')
    
    # Retrieving flavours
    get_flavours('lays')
