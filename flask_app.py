from flask import Flask

app = Flask(__name__, static_folder='static')

# Serves Static HTML
@app.route('/')
def main():
    return app.send_static_file('index.html')

app.run()