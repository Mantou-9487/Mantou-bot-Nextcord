from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.classes import Cog_Extension

class event(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        
@commands.Cog.listener()
async def on_member_join(self, member, ctx, MessageChannel, message):
        message.channel = MessageChannel
        await message.channel.send("welcome test")

@commands.command(aliases=['question'])
async def _question(self, ctx, game):
    embed = discord.Embed()
    embed = discord.Embed(color=discord.Colour.random(), title="", description="", timestamp= datetime.datetime.utcnow()) 
    embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
    embed.add_field(name="你的問題為 {}".format(f'{question}'), value="{}".format(f'{l}'), inline=True)
    await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(event(bot))