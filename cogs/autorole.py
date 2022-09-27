import nextcord
import time
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SelectOption
import datetime

class Modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("自訂義身分組")

        self.rolename = nextcord.ui.TextInput(
            label="身分組名稱",
            min_length=1,
            max_length=50,
        )
        self.add_item(self.rolename)

        self.color = nextcord.ui.TextInput(
            label="顏色 (使用顏色代碼,不用加#)",
            min_length=6,
            max_length=6,
        )
        self.add_item(self.color)

    async def callback(self, interaction: Interaction):
        guild = interaction.guild
        colorcode = f"{self.color.value}"
        inte = int(colorcode,16)
        color = hex(inte)
        await guild.create_role(name=f"{self.rolename.value}", colour=int(color,16))
        role = nextcord.utils.get(guild.roles, name=f"{self.rolename.value}")
        await interaction.user.add_roles(role)
        embed = nextcord.Embed(title=":white_check_mark: 執行成功! ", description=f"你已成功取得了 <@&{role.id}> 的身分組!", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed ,ephemeral=True)

class View(nextcord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)

    @nextcord.ui.button(label="設定", emoji="🔧", style=nextcord.ButtonStyle.gray)
    async def set(self, button: nextcord.ui.Button, interaction:Interaction):
        modal = Modal()
        await interaction.response.send_modal(modal=modal)

class autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name='autorole',description="自定義身分組", guild_ids=[1003837176464810115])
    async def autorole(self, interaction: Interaction):
        embed = nextcord.Embed(title="設置你專屬的身分組", description="點選以下的按鈕來設定ㄅ", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
        view = View(interaction.user)
        await interaction.response.send_message(embed=embed, view=view)

def setup(bot):
    bot.add_cog(autorole(bot))
