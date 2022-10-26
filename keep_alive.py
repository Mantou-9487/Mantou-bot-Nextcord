from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
	return 'Bot is aLive!'