from flask import Flask, render_template, request
import mysql.connector
import webbrowser

app = Flask(__name__, template_folder='templates', static_url_path="/static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Database configuration
DB_HOST = 'localhost'
DB_NAME = 'userbases'
DB_USER = 'student'
DB_PASSWORD = 'student'

def connect_to_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def index():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Clean the database by removing all existing rows
    cursor.execute("DELETE FROM usertables")

    # Add an example entry
    cursor.execute("INSERT INTO usertables (id, name, surname, phone, address, age) VALUES (%s, %s, %s, %s, %s, %s)",
              (1, "Nicholas", "Szabó", "01234567", "Washington DC, The USA.", 60))
    conn.commit()

    cursor.execute('SELECT * FROM usertables')
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('indexes.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Execute a SQL query that counts the number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM usertables")
        
    # Get the result of the query
    id = f'{cursor.fetchone()[0]+1}'

    # Get form data
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    address = request.form['address']
    age = request.form['age']

    # Basic validation (server-side)
    all_filled = all([id, name, surname, phone, address, age])
    phone_numeric = phone.isdigit()
    phone_length = len(phone) == 8
    valid = all_filled and phone_numeric and phone_length

    if valid:
        cursor.execute('INSERT INTO usertables (id, name, surname, phone, address, age) VALUES (%s, %s, %s, %s, %s, %s)', (id, name, surname, phone, address, age))
        conn.commit()
        message = "Data saved successfully!"
    else:
        message = "Please fill in all fields and ensure phone number is 08 digits (numeric)!"

    cursor.execute('SELECT * FROM usertables')
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('indexes.html', message=message, data=data)

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == '__main__':
    print("**Server is running!**")
    print("Access the application at - http://127.0.0.1:5000/")
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
    