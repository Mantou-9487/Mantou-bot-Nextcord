import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import datetime

# 這邊可以使用Cog功能繼承基本屬性
class Modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("Modal")

        self.pet_type = nextcord.ui.Select(
            options=[
                nextcord.SelectOption(label="跑酷", value="1"),
                nextcord.SelectOption(label="test2", value="2"),
                nextcord.SelectOption(label="test3", value="3"),
                nextcord.SelectOption(label="test4", value="4"),
                nextcord.SelectOption(label="test4", value="5"),
            ],
            min_values=1,
            max_values=5,
            placeholder="影片類型",
        )
        self.add_item(self.pet_type)

        self.idea = nextcord.ui.TextInput(
            label="想合作的題材",
            min_length=10,
            max_length=500,
        )
        self.add_item(self.idea)

        self.script = nextcord.ui.TextInput(
            label="合作腳本提供",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="可以讓我們知道你想合作的內容細節",
            required=False,
            max_length=100,
        )
        self.add_item(self.script)



    async def callback(self, interaction: Interaction):
        response = f"{interaction.user.mention}'s favourite pet's name is {self.name.value}."
        response += f"\nThe type of pet is {self.pet_type.values[0]}."
        if self.description.value != "":
            response += (
                f"\nTheir pet can be recognized by this information:\n{self.description.value}"
            )
        
        await interaction.response.send_message(response)


class Cooperation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='合作申請',description="合作申請", guild_ids=[1003837176464810115])
    async def Cooperation(self, interaction: Interaction):
        modal = Modal()
        await interaction.response.send_modal(modal)

def setup(bot):
    bot.add_cog(Cooperation(bot))