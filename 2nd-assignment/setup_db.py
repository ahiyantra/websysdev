import mysql.connector

# Database configuration
DB_HOST = 'localhost'
DB_NAME = 'userbases'
DB_USER = 'student'
DB_PASSWORD = 'student'

def create_database():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        auth_plugin='mysql_native_password'  # Explicitly specify auth plugin      
    )
    cursor = conn.cursor()

    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{DB_NAME}' already exists.")
        else:
            print(f"Error creating database: {err}")

    conn.close()

def create_table():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()

    table_query = """
        CREATE TABLE IF NOT EXISTS usertables (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            phone VARCHAR(8) NOT NULL,
            address VARCHAR(255) NOT NULL,
            age INT NOT NULL
        );
    """

    try:
        cursor.execute(table_query)
        print("Table 'usertables' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

    conn.close()

if __name__ == "__main__":
    create_database()
    create_table()
    