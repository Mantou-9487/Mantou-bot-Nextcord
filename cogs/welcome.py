from re import A, T
import select
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord.abc import GuildChannel
from nextcord import ChannelType
class Modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("自訂義の歡迎訊息")

        self.welcome = nextcord.ui.TextInput(
            label="打上你想要的歡迎訊息在這ㄅ",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="目前可使用的參數: {user}, {guildname}",
            required=False,
            max_length=500,
        )
        self.add_item(self.welcome)

    async def callback(self, interaction: Interaction):
        global welcomemessage
        welcomemessage = str(self.welcome.value)
        customparameter = {"{user}": f"{interaction.user.mention}"}
        custommessage = welcomemessage.replace('{user}', customparameter["{user}"])
        await interaction.response.send_message(f"你的自訂義訊息為:\n{custommessage}")

class View(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=0)
        self.value = None

    @nextcord.ui.button(label= "🔧設定歡迎訊息", style=nextcord.ButtonStyle.green)
    async def setwelcome(self, button: nextcord.ui.Button, interaction:Interaction):
        modal = Modal()
        await interaction.response.send_modal(modal)
        self.value = False
    
    @nextcord.ui.button(label="設置加入訊息的頻道", style=nextcord.ButtonStyle.gray)
    async def setchannel(self, button: nextcord.ui.Button, interaction:Interaction):
        view = DropdownView()
        view.add_item(Dropdown(interaction=interaction))
        embed = nextcord.Embed(title="這是一個測試自訂義歡迎訊息的訊息 (?", description="快ㄊㄇ點選單", colour=nextcord.Colour.random())
        await interaction.response.edit_message(embed=embed, view=view)
        self.value = False

class Dropdown(nextcord.ui.Select):
    def __init__(self, interaction:Interaction):
        options = []
        global text_channel_list
        text_channel_list = []
        text_channel_dict = {}
        for i in interaction.guild.text_channels:
            text_channel_dict['ChannelName'] = f'{i.name}'
            text_channel_dict['ChannelID'] = f'{i.id}'
            text_channel_list.append(text_channel_dict.copy())
        print(text_channel_list)
        for v in text_channel_list:
            if not v["ChannelName"] is None: 
                option = nextcord.SelectOption(label='{}'.format(v["ChannelName"]))
                options.append(option)
                global minvalue
                minvalue = len(text_channel_dict['ChannelName'])
                print(str(minvalue))
        super().__init__(placeholder='選擇一個頻道', min_values=1,max_values=1, options=options)
    
    async def callback(self ,interaction: Interaction):
        await interaction.response.send_message(f"你選了 {self.values[0]}")
        global welcomechannel
        for channel in text_channel_list: 
            if channel["ChannelName"] == self.values[0]:
                welcomechannel = channel["ChannelID"]

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=0)
        self.value = None
    
    @nextcord.ui.button(label= "回到設定選單", style=nextcord.ButtonStyle.green)
    async def back(self, button: nextcord.ui.Button, interaction:Interaction):
        view = View()
        await interaction.response.edit_message(view=view)
        self.value = False
        self.stop()

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @nextcord.slash_command(name='自訂義歡迎訊息',description="test", guild_ids=[1003837176464810115])
    async def welcome(self, interaction: Interaction):
        view = View()
        embed = nextcord.Embed(title="這是一個測試自訂義歡迎訊息的訊息 (?", description="快ㄊㄇ點底下的按鈕", colour=nextcord.Colour.random())
        await interaction.response.send_message(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_member_join(self, member:nextcord.Member):
        customparameter = {"{user}": f"{member.mention}"}
        custommessage = welcomemessage.replace("{user}", customparameter["{user}"])
        channel = nextcord.utils.get(member.guild.channels, id=int(welcomechannel))
        await channel.send(custommessage)

def setup(bot):
    bot.add_cog(Welcome(bot))