from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return 'Bot is aLive!'