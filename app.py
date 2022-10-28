from flask import Flask
from threading import Thread
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

def run():
  os.system("gunicorn app:app")

def stay():
    stay = Thread(target=run)
    stay.start()