import urllib.request
import json
import nextcord
import requests
import re
from nextcord.ext import commands, tasks
from nextcord import Interaction, SlashOption


class sub(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.api = "AIzaSyDhxhd0wQL3q2TMBo0QD5WVV_rqpwJwP4A"
        super().__init__()
    #影片通知


    @commands.Cog.listener()
    async def on_ready(self):
        print("檢查影片跟訂閱功能已啟動!")
        

    @nextcord.slash_command(name='sub', description="顯示主播的訂閱數",guild_ids=[1003837176464810115])
    async def sub(self, interaction: Interaction):
        embed = nextcord.Embed(title="施工中", colour=nextcord.Colour.random())
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(sub(bot))