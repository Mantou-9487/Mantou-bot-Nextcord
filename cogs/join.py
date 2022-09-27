from imaplib import Commands
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SelectOption
import datetime

# 這邊可以使用Cog功能繼承基本屬性
class Modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("Modal")

        self.name = nextcord.ui.TextInput(
            label="Name",
            min_length=2,
            max_length=50,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Information that can help us recognise your pet",
            required=False,
            max_length=1800,
        )
        self.add_item(self.description)

    async def callback(self, interaction: Interaction):
        response = f"{interaction.user.mention}'s favourite pet's name is {self.name.value}."
        response += f"\nThe type of pet is {self.pet_type.values[0]}."
        if self.description.value != "":
            response += (
                f"\nTheir pet can be recognized by this information:\n{self.description.value}"
            )
        
        await interaction.response.send_message(response)

class Dropdown(nextcord.ui.Select):
    def __init__(self):
        super().__init__(placeholder="Choose a command", min_values=1, max_values=1, options=[SelectOption(label="Hey", value="Hello")])

    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f"You clicked {self.values[0]}")

class View(nextcord.ui.View):
    def __init__(self, ctx:commands.Context):
        super().__init__()
        self.ctx = ctx
        self.value = None
        self.add_item(Dropdown())

    @nextcord.ui.button(label = "啟用", custom_id="1", style=nextcord.ButtonStyle.green)
    async def enable(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = "enable"
        self.stop()

    @nextcord.ui.button(label = "設定加入訊息頻道", custom_id="2", style=nextcord.ButtonStyle.gray)
    async def joinchanel(self, button: nextcord.ui.Button, guild:nextcord.Guild, interaction: Interaction):
        value = []
        channellen = len(nextcord.utils.get(guild.text_channels))
        channel = nextcord.utils.get(guild.text_channels)
        for aaaa in channellen:
            value.append(
                SelectOption(
                    label= channel,
                    value= aaaa + 1
                )
            )
            embed = nextcord.Embed(title="訊息發送頻道", description="請透過底下的選單選擇頻道", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
            chaneeltype = nextcord.ui.select(placeholder="選擇頻道", min_values=1, max_values=1, options=value)
            await interaction.response.edit_message(embed=embed, view=self)
            self.value = "joinchannel"
            self.stop()
    

    async def interaction_check(self, guild:nextcord.Guild, interaction: nextcord.Interaction):
        if interaction.user.id != self.ctx.id:
            await interaction.response.send_message("你點這幹嘛?")
class join(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @nextcord.slash_command(name='joinsettings',description="設置成員加入的選項",guild_ids=[1003837176464810115])
    async def join(self, interaction: Interaction):
        embed = nextcord.Embed(title="設置加入訊息", description="點選以下的按鈕來設定ㄅ", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
        view = View(interaction.user)
        await interaction.response.send_message(view=view, embed=embed)

def setup(bot):
    bot.add_cog(join(bot))