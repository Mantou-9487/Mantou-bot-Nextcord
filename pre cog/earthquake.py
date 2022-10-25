from unittest import result
from discord.ext import commands, tasks
import discord
from core.classes import Cog_Extension
import datetime
import requests
from numpy import random
client = discord.Client()

class earthquake(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True, aliases=['setchannel'])
    async def _setchannel(self, ctx):
        embed = discord.Embed()
        embed = discord.Embed(color=discord.Colour.random(), title="地震通知系統V1.0", description="", timestamp= datetime.datetime.utcnow()) 
        embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
        
    


    @commands.Cog.listener()
    async def on_ready(self):
        self.earthquake.start()

    @tasks.loop(seconds=10)
    async def earthquake(self):
        try:
            channel = self.bot.get_channel(889054851496046635)
            r = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-04DD936F-EBB7-44D1-B647-FDC5A42A73CC')
            results = r.json()
            item = results['records']['earthquake'][0]
            reportContent  = item['reportContent']
            reportImageURI = item['reportImageURI']
            url = item['web']
            originTime = item["earthquakeInfo"]["originTime"]
            location = (item['earthquakeInfo']["epiCenter"]["location"])
            depth = (item['earthquakeInfo']["depth"]["value"])
            magnitude = (item['earthquakeInfo']["magnitude"]["magnitudeValue"])
            embed = discord.Embed()
            embed = discord.Embed(color=discord.Colour.random(), title="地震通知系統V1.0", description="", timestamp= datetime.datetime.utcnow()) 
            embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
            embed.add_field(name="標題", value="{}".format(reportContent), inline=True)
            embed.add_field(name="報告連結", value=str("[點我看連結]({})").format(url), inline=True)
            embed.add_field(name="震央", value="{}".format(location), inline=True)
            embed.add_field(name="發生時間", value="{}".format(originTime), inline=True)
            embed.add_field(name="深度", value="{}".format(depth), inline=True)
            embed.add_field(name="芮氏規模", value="{}".format(magnitude), inline=True)
            embed.set_image(url=reportImageURI)
            embed.set_footer(text="地震報告提供", icon_url='https://media.discordapp.net/attachments/345147297539162115/732527875839885312/ROC_CWB.png')
            await channel.send(embed=embed)
        except Exception as err:
            print(err)
        
def setup(bot):
    bot.add_cog(earthquake(bot))