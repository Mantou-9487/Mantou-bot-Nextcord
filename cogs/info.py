import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from typing import Optional
import time
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @nextcord.slash_command(name="查看使用者資訊",description="透過ID查別人")
    async def userinfo(self,interaction:Interaction, target:Optional[Member] = SlashOption(description="放你要查的人ID")):
        embed = nextcord.Embed(title=target.name,colour=nextcord.Colour.random())
        embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
        embed.add_field(name="正在玩",value=f"{str(target.activity.name) if target.activity else 'N/A'}" ,inline=False)
        createdate_time = ((str(target.created_at.hour) +":"+ str(target.created_at.minute)))
        createdate_date = (str(target.created_at.date()).replace('-','/') + ' '+ createdate_time)
        joindate_time = ((str(target.joined_at.hour) +":"+ str(target.joined_at.minute)))
        joindate_date = (str(target.joined_at.date()).replace('-','/') + ' '+ joindate_time)
        print(createdate_time)
        create_timestamp = time.mktime(datetime.datetime.strptime(createdate_date, "%Y/%m/%d %H:%M").timetuple())
        join_timestamp = time.mktime(datetime.datetime.strptime(joindate_date, "%Y/%m/%d %H:%M").timetuple())
        embed.add_field(name="帳號創立時間",value=f"<t:{int(create_timestamp)}>" ,inline=True)
        embed.add_field(name="加入群組時間",value=f"<t:{int(join_timestamp)}>",inline=False)
        embed.set_thumbnail(url=target.avatar.url)
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Info(bot))