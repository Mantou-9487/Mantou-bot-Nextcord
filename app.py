from threading import Thread
from functools import partial
from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    partial_run = partial(app.run(), host="0.0.0.0", port="10000" ,use_reloader=False)
    t = Thread(target=partial_run)
    t.start()