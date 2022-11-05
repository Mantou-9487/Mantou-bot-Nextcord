
from nextcord import Interaction, SelectOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import nextcord
import os
import requests
from dotenv import load_dotenv
from flask import Flask
from threading import Thread


intents = nextcord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

testserverid = 889054851496046632

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(activity=nextcord.Game(name="機器人版本:V1.0.2 | 作者by 鰻頭"))


@bot.listen('on_message')
async def my_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("鰻頭"):
        await message.reply("Maaaaaaaaan頭")

for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")

#註冊斜線指令
url = "https://discord.com/api/v10/applications/949535524652216350/commands"

json = {
    "name": "attack",
    "description": "攻擊你的朋友!",
    "type": 1,
    "options": [
            {
            "name": "user",
            "description": "The user to edit",
            "required": True,
            "type": 6
        }
    ]
}

json1 = {
    "name": "eval",
    "description": "噓~",
    "type": 1,
    "options": [
            {
            "name": "option",
            "required": True,
            "type": 1,
            "description": "噓"
        }
    ]
}

def flask_thread(func):
    thread = Thread(target=func)
    print('Start Separate Thread From Bot')
    thread.start()

def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False)

# For authorization, you can use either your bot token
load_dotenv()
headertoken = os.getenv("TOKEN")
headers = {
    "Authorization": f"Bot {headertoken}"
}

if __name__ == "__main__":
    flask_thread(func=run)
    token = os.getenv("TOKEN")
    bot.run(token)
    
    
