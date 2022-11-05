import nextcord
from nextcord.ext import commands
from nextcord import Interaction
class ExceptionHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Error_Handle Ready!")

    @commands.Cog.listener()
    async def on_command_error(self, interaction:Interaction, error) -> None:
        embed = nextcord.Embed(title=":x: 出現錯誤了!!!", description=f"```{error}```")
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(ExceptionHandler(bot))
