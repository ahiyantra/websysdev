
from flask_server import create_app
from flask import send_from_directory
from flask_cors import CORS
import os
import webbrowser

app = create_app()
CORS(app)  # Enable CORS for all routes and origins

# Serve React app from the 'build' directory
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    app.run(debug=True, use_reloader=False)
