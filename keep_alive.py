from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
	return 'Bot is aLive!'

def run():
    app.run(port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()