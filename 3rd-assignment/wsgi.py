from server import create_app
from flask_cors import CORS
import os

app = create_app()
CORS(app)  # Enable CORS for all routes and origins

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return app.send_from_directory(app.static_folder, path)
    else:
        return app.send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()