from threading import Thread
from functools import partial
from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

def stay():
    partial_run = os.system("gunicorn app:app")

    t = Thread(target=partial_run)

    t.start()