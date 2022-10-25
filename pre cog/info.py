
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension
import platform

class info(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    

def setup(bot: commands.Bot):
    bot.add_cog(info(bot))