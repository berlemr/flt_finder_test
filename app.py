import os
from flask import Flask
from werkzeug.utils import import_string


app = Flask(__name__)
cfg = import_string(os.environ['APP_SETTINGS'])()
app.config.from_object(cfg)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()