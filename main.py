from nextcord import Interaction, SelectOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
import nextcord
import os
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

testserverid = 889054851496046632

@bot.event
async def on_ready():
    print("ready")


@bot.listen('on_message')
async def my_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("鰻頭"):
        await message.reply("Maaaaaaaaan頭")

for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")
        print("Cog已加載")



if __name__ == "__main__":
    bot.run("OTQ5NTM1NTI0NjUyMjE2MzUw.G2Q8tI.PeKrwOzApkOo1kQqLBu3Y2W0N4nSkuCbcnEZpE")







