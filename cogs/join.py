import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import datetime
class join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.Cog.listener()
    async def on_member_join(self, member:nextcord.Member):
        channel = nextcord.utils.get(member.guild.channels, id=1024477488405037099)
        embed = nextcord.Embed(title=f"歡迎 {member.name} !", description=f"歡迎來到 {member.guild.name} !\n這裡是松農世界計畫的群組~\n希望你在這裡過得很好!", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow(), url=member.guild.icon.url)
        embed.set_image(url=member.avatar.url)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(join(bot))


