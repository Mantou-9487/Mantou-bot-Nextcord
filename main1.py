from nextcord.ext import commands
import nextcord
import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template
from threading import Thread


intents = nextcord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="~", intents=intents, help_command=None)

testserverid = 889054851496046632

app = Flask(__name__,template_folder="Templates")


@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/test')
def test():
    return "Helloooo Test!"

@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(activity=nextcord.Game(name="機器人版本:V1.0.6 | 作者by 鰻頭"))


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
    "name": "剪刀石頭布",
    "description": "就是個剪刀石頭布",
    "type": 1
}

json1 = {
    "name": "旗幟",
    "description": "透過ID查別人",
    "type": 1,
    "options": [
            {
            "name": "target",
            "type": 1,
            "description": "放你要查的人ID",
            "required": True,
        }
    ]
}

def flask_thread(func):
    thread = Thread(target=func)
    print('Start Separate Thread From Bot')
    thread.start()

def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False, debug=True)
    requests.post(url, headers=headers, json=json)


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
    
    
