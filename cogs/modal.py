from http.client import HTTPException
from urllib import response
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
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

        self.pet_type = nextcord.ui.Select(
            options=[
                nextcord.SelectOption(label="Dog", value="4", emoji="🐶"),
            ],
            min_values=1,
            max_values=1,
            placeholder="Type of pet",
        )
        self.add_item(self.pet_type)



    async def callback(self, interaction: Interaction):
        response = f"{interaction.user.mention}'s favourite pet's name is {self.name.value}."
        response += f"\nThe type of pet is {self.pet_type.values[0]}."
        if self.description.value != "":
            response += (
                f"\nTheir pet can be recognized by this information:\n{self.description.value}"
            )
        
        await interaction.response.send_message(response)


class ModalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='modal',description="test", guild_ids=[1003837176464810115])
    async def modal(self, interaction: Interaction):
        modal = Modal()
        await interaction.response.send_modal(modal)

def setup(bot):
    bot.add_cog(ModalCog(bot))