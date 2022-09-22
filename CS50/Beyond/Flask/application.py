from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/<string:name1>")
def name(name1):
    return f"Hello {name1}"