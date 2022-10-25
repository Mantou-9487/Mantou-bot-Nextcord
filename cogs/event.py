
from imaplib import Commands
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SelectOption
import datetime

# 這邊可以使用Cog功能繼承基本屬性

class Dropdown(nextcord.ui.Select):
    def __init__(self, ctx:commands.Context):
        self.ctx = ctx
        super().__init__(placeholder="設定選單", min_values=1, max_values=1, options=[SelectOption(label="初始化", value="1")])

    async def callback(self, interaction: nextcord.Interaction):
        guild = self.ctx.guild
        category = await guild.create_category("私人語音頻道")
        user = self.ctx.message.author.name
        overwrites = {
            guild.default_role: nextcord.PermissionOverwrite(connect=False)
        }
        await guild.create_voice_channel(f"{user} 的私人頻道", overwrites=overwrites)
        await interaction.response.send_message(f"你初始化成功了!")

class View(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

class enc(commands.Cog): #加密頻道
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        print("Enc Ready!")
    
    @nextcord.slash_command(name='enc',description="創立你專屬的加密頻道", guild_ids=[1003837176464810115])
    async def enc(self, interaction: Interaction):
        embed = nextcord.Embed(title="設置專屬於你的加密頻道", description="加密頻道可以讓你自己一個人享受,且只要有人想加入輸入密碼便可進入", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
        view = View()
        await interaction.response.send_message(view=view, embed=embed)

    async def cog_command_error(interaction:Interaction, error):
        embed = nextcord.Embed(title=":x: 出現錯誤了!!!", description=f"```{error}```")
        await interaction.response.send_message(embed=embed)
def setup(bot):
    bot.add_cog(enc(bot))