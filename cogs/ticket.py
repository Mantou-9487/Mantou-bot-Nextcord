import nextcord
import time
import datetime
import pytz
import os
from nextcord.ext import commands,application_checks
from nextcord import Interaction
from nextcord import SlashOption
from nextcord import Forbidden

class View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label="點我創建",style=nextcord.ButtonStyle.green,custom_id="create_ticket")
    async def create_ticket(self, button: nextcord.ui.Button, interaction:Interaction):
        global channel
        global set_channel
        set_channel = interaction.message.channel
        try:
            ticket_channel = nextcord.utils.get(interaction.guild.text_channels,id=channel.id)
        except NameError:
            pass
        try:
            if ticket_channel is not None:
                failed_embed = nextcord.Embed(title="<:x_mark:1033955039615664199> | 你已經有這個頻道了!",description=f"你的頻道在 {ticket_channel.mention}",colour=nextcord.Colour.red())
                await interaction.response.send_message(embed=failed_embed,ephemeral=True)
            else:
                loading_embed = nextcord.Embed(title="<a:Loading:1059806500241027157> | 正在創建中...",colour=nextcord.Colour.light_grey())
                msg = await interaction.response.send_message(embed=loading_embed,ephemeral=True)
                overwrites = {
                    interaction.guild.default_role: nextcord.PermissionOverwrite(view_channel=False),
                    interaction.guild.me: nextcord.PermissionOverwrite(view_channel=True,send_messages=True,attach_files=True,embed_links=True),
                    interaction.user: nextcord.PermissionOverwrite(view_channel=True, send_messages=True,read_message_history=True)
                }
                channel = await interaction.guild.create_text_channel(f"客服單-{interaction.user.name}",overwrites=overwrites,category=set_channel.category)
                success_embed = nextcord.Embed(title="<:check:1036160202174627840> | 成功創建!",description=f"你的頻道在 {channel.mention}",colour=nextcord.Colour.green())
                await msg.edit(embed=success_embed)
                channel_embed = nextcord.Embed(title=f"{interaction.user.name} 的客服單",description="請等待人員處理您的問題")
                view = TicketView()
                member = interaction.user
                message = await channel.send(content=f"{member.mention}")
                await message.delete()
                await channel.send(embed=channel_embed,view=view)
        except UnboundLocalError: #真正執行的地方
                loading_embed = nextcord.Embed(title="<a:Loading:1059806500241027157> | 正在創建中...",colour=nextcord.Colour.light_grey())
                msg = await interaction.response.send_message(embed=loading_embed,ephemeral=True)
                overwrites = {
                    interaction.guild.default_role: nextcord.PermissionOverwrite(read_messages=False),
                    interaction.guild.me: nextcord.PermissionOverwrite(read_messages=True)
                }
                channel = await interaction.guild.create_text_channel(f"客服單-{interaction.user.name}",overwrites=overwrites,category=set_channel.category)
                success_embed = nextcord.Embed(title="<:check:1036160202174627840> | 成功創建!",description=f"你的頻道在 {channel.mention}",colour=nextcord.Colour.green())
                await msg.edit(embed=success_embed)
                channel_embed = nextcord.Embed(title=f"{interaction.user.name} 的客服單",description="請等待人員處理您的問題")
                view = TicketView()
                member = interaction.user
                message = await channel.send(content=f"{member.mention}")
                await message.delete()
                await channel.send(embed=channel_embed,view=view)
class TicketView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.lock = True
    
    @nextcord.ui.button(label="鎖定客服單",style=nextcord.ButtonStyle.blurple)
    async def lock_ticket(self, button: nextcord.ui.Button, interaction:Interaction):
        if self.lock == True:
            conversation_record = channel.history(limit=None)
            with open(f"chat.txt",'w',encoding='UTF-8') as chat:
                async for message in conversation_record:
                    tzone = datetime.timezone(datetime.timedelta(hours=8))
                    message.created_at.astimezone(tzone)
                    print(message.created_at.hour)
                    msgdate_time = ((str(message.created_at.hour) +":"+ str(message.created_at.minute)+":"+ str(message.created_at.second)))
                    msgdate_date = (str(message.created_at.date()).replace('-','/') + ' '+ msgdate_time)
                    from_zone = pytz.timezone('UTC')
                    tw_zone = pytz.timezone('ROC')
                    created_at =  datetime.datetime.strptime(msgdate_date, "%Y/%m/%d %H:%M:%S").replace(tzinfo=from_zone)
                    central = created_at.astimezone(tw_zone)
                    chat.write(f"{central} - {message.author.display_name}: {message.content}\n")
            ticket_channel = nextcord.utils.get(interaction.guild.text_channels,id=channel.id)
            overwrites = {
                    interaction.guild.default_role: nextcord.PermissionOverwrite(view_channel=False),
                    interaction.guild.me: nextcord.PermissionOverwrite(view_channel=False),
                    interaction.user: nextcord.PermissionOverwrite(view_channel=False)
                }
            await ticket_channel.edit(overwrites=overwrites)
            await interaction.response.send_message(f"客服單已被 {interaction.user.name} 鎖定!")
            await interaction.followup.send(f"本次對話紀錄檔案:",file=nextcord.File(f"chat.txt"))
            os.remove(f"chat.txt")
            self.lock = None
        else:
            await interaction.response.send_message(f"此頻道已經被鎖定了!",ephemeral=True)
        



    @nextcord.ui.button(label="刪除客服單",style=nextcord.ButtonStyle.red)
    async def delete_ticket(self, button: nextcord.ui.Button, interaction:Interaction):
        if self.lock == None:
            ticket_channel = nextcord.utils.get(interaction.guild.text_channels,id=channel.id)
            loading_embed = nextcord.Embed(title="<a:Loading:1059806500241027157> | 正在刪除...",colour=nextcord.Colour.light_grey())
            await interaction.response.send_message(embed=loading_embed)
            await ticket_channel.delete()
        else:
            failed_embed = nextcord.Embed(title="<:x_mark:1033955039615664199> | 請先鎖定客服單後再按按鈕",colour=nextcord.Colour.red())
            await interaction.response.send_message(embed=failed_embed,ephemeral=True)


class ticket(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        super().__init__()
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(View())
        print("Ticket Ready!")
    @nextcord.slash_command(name="ticket",description="創建一個可供你和管理員聯繫的頻道")
    @application_checks.has_permissions(manage_messages=True)
    async def ticket(self, interaction: Interaction, option = SlashOption(name="客服單內文",description="設定您想給大家知道用途的介紹文字 (留空自動生成)",required=False)):
        if option != None:
            embed = nextcord.Embed(title="開啟客服單的系統",description=f"{option}",colour=nextcord.Colour.orange())
        else:
            embed = nextcord.Embed(title="開啟客服單的系統",description="如果你需要和服務人員聯絡\n請點擊下方按鈕開啟客服單",colour=nextcord.Colour.orange())
        view = View()
        await interaction.response.send_message(embed=embed,view=view)

def setup(bot):
    bot.add_cog(ticket(bot))