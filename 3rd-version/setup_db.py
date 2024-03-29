import mysql.connector
from server import create_app
from server.databases.util_db import db_util
from server.models.person_models import Person
from config import config

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'student'
DB_PASSWORD = 'student'
DB_NAME = 'userbases'

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

def init_db():
    create_database()
    # Update the SQLALCHEMY_DATABASE_URI
    config_obj = config['default']
    config_obj.SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

    # Create the Flask app and push the context
    app = create_app()
    with app.app_context():
        db_util.create_all()

        # Clear the Person table
        Person.clear_table()  

        # Add the example entry
        example_person = Person(
            name="Nicholas",
            surname="Szabó",
            phone="01234567",
            address="Washington DC, The USA.",
            age=60
        )
        db_util.session.add(example_person)
        db_util.session.commit()

if __name__ == "__main__":
    init_db()
    print("Database schema initialized successfully!")