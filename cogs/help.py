import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import datetime

# 這邊可以使用Cog功能繼承基本屬性
class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='help',description="help", guild_ids=[1003837176464810115])
    async def help(self, ctx):
        embed = nextcord.Embed(title="紅翼機器人", description="指令前綴為 +", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
        embed = nextcord.Embed(color=nextcord.Colour.random(), title="指令清單", timestamp= datetime.datetime.utcnow()) 
        embed.add_field(name="邀請", value="invite", inline=False)
        embed.add_field(name="查看延遲", value="Ping", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))