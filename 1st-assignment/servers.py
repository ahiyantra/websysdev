import http.server
import json
import sqlite3
import webbrowser
import os
from urllib.parse import urlparse, parse_qs

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    # Create a SQLite database connection
    conn = sqlite3.connect('userbases.db')
    cursor = conn.cursor()

    # Create a table to store personal data
    cursor.execute('''CREATE TABLE IF NOT EXISTS personal_data
                      (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, telephone TEXT, address TEXT, age INTEGER)''')
    conn.commit()

    def do_GET(self):
        if self.path == '/':
            # Serve the client-side HTML file
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('indexes.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/api':
            print('received GET request ...')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            # Retrieve all data from the database
            self.cursor.execute('''SELECT * FROM personal_data''')
            data = self.cursor.fetchall()
            response = json.dumps({'data': data})
            print(data)
            self.wfile.write(response.encode())
        else:
            # Serve static files (CSS, JavaScript, etc.)
            self.path = self.translate_path(self.path)
            if os.path.isfile(self.path):
                self.send_response(200)
                self.send_header('Content-type', self.guess_type(self.path))
                self.end_headers()
                with open(self.path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404)

    def do_POST(self):
        if self.path == '/submit':
            print('received POST request ...')
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))
            print("post data : ", json_data)

            # Extract input values from the JSON payload
            name = json_data.get('name')
            surname = json_data.get('surname')
            telephone = json_data.get('telephone')
            address = json_data.get('address')
            age = json_data.get('age')

            # Insert data into the database
            self.cursor.execute('''INSERT INTO personal_data (name, surname, telephone, address, age)
                          VALUES (?, ?, ?, ?, ?)''', (name, surname, telephone, address, age))
            self.conn.commit()

            # Send JSON response back to client
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            response_data = {'id': None, 'name': name, 'surname': surname, 'telephone': telephone, 'address': address, 'age': age}
            self.wfile.write(json.dumps({'data': [response_data]}).encode())

            print('input data saved successfully ...')
            print("response data : ", response_data)
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        print('received OPTIONS request ...')
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Change the current working directory
    httpd = http.server.HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print('server started on localhost:8000 ...')
    webbrowser.open('http://localhost:8000')  # Open the client in the default browser
    httpd.serve_forever()