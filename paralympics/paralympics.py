from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return f"Hello World!"

@app.route("/Trixia")
def hello_greeting(name='Trixia'):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
    app.run(debug=True)