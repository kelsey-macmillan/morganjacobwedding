from flask import Flask

app = Flask(__name__, static_folder='static')

# Serves Static HTML
@app.route('/')
def main():
    return app.send_static_file('index.html')

# Debug logger
if __name__ == "__main__":
    app.debug = True
    app.run()

