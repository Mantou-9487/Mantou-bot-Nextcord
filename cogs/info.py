import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from typing import Optional

class Info(commands.Cog):
    def __init__(self):
        super().__init__()

    @nextcord.slash_command(name="查看使用者資訊",description="透過ID查別人")
    async def userinfo(self,interaction:Interaction, target:Optional[Member] = SlashOption(description="放你要查的人ID")):
        embed = nextcord.Embed(name={target.name},colour=nextcord.Colour.random())
        embed.add_field(name="用戶ID",value=f"{target.id}")
        embed.add_field(name="正在玩",value=f"{target.activity.name} {str(getattr(target.activity, type)).title()}")
        embed.add_field(name="帳號創立時間",value=target.created_at.strftime(f"%d/%m/%Y %H:%M:S"))
        embed.set_thumbnail(url=target.avatar.url)
        await interaction.response.send_message(embed=embed)
def setup(bot):
    bot.add_cog(Info(bot))