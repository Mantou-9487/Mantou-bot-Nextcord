import nextcord
from nextcord.ext import commands
from nextcord import Interaction
class View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @nextcord.ui.button(label="更新", style=nextcord.ButtonStyle.green, emoji="<:Update:1036992904352243743>")
    async def update(self, button: nextcord.ui.Button, interaction:Interaction):
        print(latency)
        embed = nextcord.Embed(title=":ping_pong: | Pong! {} ms".format(round(latency * 1000)),colour=nextcord.Colour.random())
        await interaction.response.edit_message(embed=embed, view=self)

class Ping(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping Ready!")

    @nextcord.slash_command(name="ping", description="查看機器人的延遲")
    async def ping(self, interaction:Interaction):
        global latency
        global message_id
        latency = self.bot.latency
        print(latency)
        embed = nextcord.Embed(title=":ping_pong: | Pong! {} ms".format(round(latency * 1000)),colour=nextcord.Colour.random())
        view = View() 
        message = await interaction.response.send_message(embed=embed,view=view)
        message_id = await message.fetch()

def setup(bot):
    bot.add_cog(Ping(bot))