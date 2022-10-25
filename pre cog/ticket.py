import discord
import datetime
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension

class ticket(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['ticket'], pass_context=True)
    async def _ticket(self, ctx):
        name = ("私人頻道類別")
        guild = ctx.message.guild
        for ticket in guild.channels:
            if ctx.author.name in ticket.name:
                embed = discord.Embed()
                embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
                embed = discord.Embed(color=discord.Colour.random(), title=":tickets: 私人頻道系統", description="你創過了我日!", timestamp= datetime.datetime.utcnow())
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed()
            embed = discord.Embed(color=discord.Colour.random(), title=":tickets: 私人頻道系統", description="自己創私人頻道的東東", timestamp= datetime.datetime.utcnow()) 
            embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
            await ctx.send(embed=embed, components = [Button(label='點我創建', style='3', custom_id='initialization')])
            async def button_callback(interaction):
                category = await guild.create_category(name)
                channel = await guild.create_text_channel('{}'.format(ctx.author.name) + " Channel", category=category)
                embed = discord.Embed(color=discord.Colour.random(), title=":tickets: 私人頻道系統", description="{} 你的頻道在這裡喔!".format(f"{channel.mention}"), timestamp= datetime.datetime.utcnow())
                embed.set_author(name=self.bot.user.name, icon_url=str(self.bot.user.avatar_url))
                await interaction.send(embed=embed, ephemeral=True)
            

def setup(bot):
    bot.add_cog(ticket(bot))