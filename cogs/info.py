import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from typing import Optional
import time
import datetime

class View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.default_avatar = True

    @nextcord.ui.button(label="伺服器頭貼",style=nextcord.ButtonStyle.green,emoji="<:loop:1035850844958105660>")
    async def avatar(self,button: nextcord.ui.Button, interaction:Interaction):
        if self.default_avatar == True:
            if member.guild_avatar != None:
                button.label = "個人頭貼"
                button.style = nextcord.ButtonStyle.green
                self.default_avatar = False
                embed = nextcord.Embed(title=f"{member.name} 的伺服器頭貼",colour=nextcord.Colour.random())
                embed.set_image(url=member.guild_avatar.url)
                await interaction.response.edit_message(embed=embed,view=self)
            else:
                button.label = "沒有伺服器頭貼!"
                button.style = nextcord.ButtonStyle.red
                button.disabled = True
                await interaction.response.edit_message(view=self)
        else:
            button.label = "伺服器頭貼"
            button.style = nextcord.ButtonStyle.blurple
            self.default_avatar = True
            embed = nextcord.Embed(title=f"{member.name} 的個人頭貼",colour=nextcord.Colour.random())
            embed.set_image(url=member.avatar.url)
            await interaction.response.edit_message(embed=embed,view=self)

class BannerView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.default_banner = True

    @nextcord.ui.button(label="伺服器旗幟",style=nextcord.ButtonStyle.green,emoji="<:loop:1035850844958105660>")
    async def banner(self,button: nextcord.ui.Button, interaction:Interaction):
        if self.default_banner == True:
            if guild_target.guild.banner != None:
                button.label = "個人旗幟"
                button.style = nextcord.ButtonStyle.green
                self.default_banner = False
                embed = nextcord.Embed(title=f"{member.name} 的伺服器旗幟",colour=nextcord.Colour.random())
                embed.set_image(url=member.guild.banner.url)
                await interaction.response.edit_message(embed=embed,view=self)
            else:
                button.label = "沒有伺服器旗幟!"
                button.style = nextcord.ButtonStyle.red
                button.disabled = True
                await interaction.response.edit_message(view=self)
        else:
            button.label = "伺服器頭貼"
            button.style = nextcord.ButtonStyle.blurple
            self.default_avatar = True
            embed = nextcord.Embed(title=f"{member.name} 的個人旗幟",colour=nextcord.Colour.random())
            embed.set_image(url=member.banner.url)
            await interaction.response.edit_message(embed=embed,view=self)



class Info(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        super().__init__()

    @nextcord.slash_command(name="查看使用者資訊",description="透過ID查別人")
    async def userinfo(self,interaction:Interaction, target:Optional[Member] = SlashOption(description="放你要查的人ID",required=True)):
        global member
        member = target
        if str(target).isdigit:
            embed = nextcord.Embed(title=target.name,colour=nextcord.Colour.random())
            embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
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

        else:
            embed = nextcord.Embed(title=target.name,colour=nextcord.Colour.random())
            embed.add_field(name="用戶ID",value=f"`{target.id}`",inline=False)
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
        
    @nextcord.slash_command(name="頭貼",description="透過ID查別人",force_global=True)
    async def avatar(self,interaction:Interaction, target:Optional[Member] = SlashOption(description="放你要查的人ID")):
        global member
        member = target
        if str(target).isdigit:
            if target != None:
                embed = nextcord.Embed(title=f"{target.name} 的個人頭貼",colour=nextcord.Colour.random())
                embed.set_image(url=target.avatar.url)
                view = View()
                await interaction.response.send_message(embed=embed, view=view)
            else:
                member = interaction.user
                embed = nextcord.Embed(title=f"{interaction.user.name} 的個人頭貼",colour=nextcord.Colour.random())
                embed.set_image(url=interaction.user.avatar.url)
                view = View()
                await interaction.response.send_message(embed=embed, view=view)
        else:
            embed = nextcord.Embed(title=f"{target.name} 的個人頭貼",colour=nextcord.Colour.random())
            embed.set_image(url=target.avatar.url)
            view = View()
            await interaction.response.send_message(embed=embed, view=view)
    

    @nextcord.slash_command(name="旗幟",description="透過ID查別人",force_global=True)
    async def banner(self,interaction:Interaction, target:Optional[Member] = SlashOption(description="放你要查的人ID")):
        global member
        global guild_target
        guild_target = target
        if str(target).isdigit:
            if target != None:
                try:
                    member = await self.bot.fetch_user(target.id)
                    embed = nextcord.Embed(title=f"{target.name} 的個人旗幟",colour=nextcord.Colour.random())
                    embed.set_image(url=member.banner.url)
                    view = BannerView()
                    await interaction.response.send_message(embed=embed, view=view)
                except AttributeError:
                    embed = nextcord.Embed(title=f"<:x_mark:1033955039615664199> | 指定的使用者沒有旗幟!",colour=nextcord.Colour.red())
                    await interaction.response.send_message(embed=embed)

            else:
                try:
                    member = await self.bot.fetch_user(interaction.user.id)
                    embed = nextcord.Embed(title=f"{interaction.user.name} 的個人旗幟",colour=nextcord.Colour.random())
                    embed.set_image(url=member.banner.url)
                    view = BannerView()
                    await interaction.response.send_message(embed=embed, view=view)
                except AttributeError:
                    embed = nextcord.Embed(title=f"<:x_mark:1033955039615664199> | 指定的使用者沒有旗幟!",colour=nextcord.Colour.red())
                    await interaction.response.send_message(embed=embed)
        else:
            try:
                embed = nextcord.Embed(title=f"{target.name} 的個人旗幟",colour=nextcord.Colour.random())
                embed.set_image(url=member.banner.url)
                view = BannerView()
                await interaction.response.send_message(embed=embed, view=view)
            except AttributeError:
                embed = nextcord.Embed(title=f"<:x_mark:1033955039615664199> | 指定的使用者沒有旗幟!",colour=nextcord.Colour.red())
                await interaction.response.send_message(embed=embed)
                
def setup(bot):
    bot.add_cog(Info(bot))