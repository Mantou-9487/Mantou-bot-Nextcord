import urllib.request
import json
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.api = "AIzaSyDhxhd0wQL3q2TMBo0QD5WVV_rqpwJwP4A"
    @nextcord.ui.button(label= "更新", style=nextcord.ButtonStyle.green,emoji="<:loop:1035850844958105660>")
    async def update(self, button: nextcord.ui.Button, interaction:Interaction):
        youtubeemoji = nextcord.utils.get(guild.emojis, name="youtube")
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCPcy_WwsHX4K1KR9Ru5091A&key={}".format(self.api)).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        embed = nextcord.Embed(title="{} | 主播的訂閱數".format(youtubeemoji), description="目前主播的訂閱數為 `{}` 個訂閱!".format(subs), colour=nextcord.Colour.random())
        await interaction.response.edit_message(embed=embed)

class sub(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.api = "AIzaSyDhxhd0wQL3q2TMBo0QD5WVV_rqpwJwP4A"
        super().__init__()

    @nextcord.slash_command(name='sub', description="顯示主播的訂閱數")
    async def sub(self, interaction: Interaction):
        global guild
        guild = self.bot.get_guild(1003837176464810115)
        youtubeemoji = nextcord.utils.get(guild.emojis, name="youtube")
        view = View()
        if interaction.user.id != 549056425943629825:
            embed = nextcord.Embed(title=":x: | 錯誤!",description="這個指令太過於恐怖,只有Man頭(´・ω・)才能駕馭它!",colour=nextcord.Colour.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCPcy_WwsHX4K1KR9Ru5091A&key={}".format(self.api)).read()
            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            embed = nextcord.Embed(title="{} | 主播的訂閱數".format(youtubeemoji), description="目前主播的訂閱數為 `{}` 個訂閱!".format(subs), colour=nextcord.Colour.random())
            await interaction.response.send_message(embed=embed, view=view)

def setup(bot):
    bot.add_cog(sub(bot))