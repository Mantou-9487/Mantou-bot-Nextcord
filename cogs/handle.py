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
    async def on_application_command_error(self, interaction:Interaction, error) -> None:
        embed = nextcord.Embed(title=":x: 阿喔，看來你用神奇魔法發現了一個漏洞 <:hahahaha:1038449572915187763>", description=f"```{error}```\n <a:853174934670540811:1038449712359022643> 已自動回報給作者! Bug反饋可以聯繫Man頭(´・ω・)#8870",colour=nextcord.Colour.red())
        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(ExceptionHandler(bot))
