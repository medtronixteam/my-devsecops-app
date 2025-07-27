from flask import Flask, send_from_directory

# Point Flask to the static folder
app = Flask(__name__, static_folder='vcare')

# Serve index.html from / (root)
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve any other file from vcare/ directory
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
