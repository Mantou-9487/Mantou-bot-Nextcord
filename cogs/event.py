
from imaplib import Commands
import nextcord
import random
from nextcord.ui import Button
from nextcord.ext import commands
from nextcord import Interaction, SelectOption
import datetime

# 這邊可以使用Cog功能繼承基本屬性

class UnlockView(nextcord.ui.View):
    def __init__(self):
        self.choice = None
        super().__init__()
        self.password_payload = {'first': '','second': '','three': '','four': ''}
    @nextcord.ui.button(label="1",style=nextcord.ButtonStyle.green,row=0)
    async def one(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 1
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])       
    @nextcord.ui.button(label="2",style=nextcord.ButtonStyle.green,row=0)
    async def two(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 2
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="3",style=nextcord.ButtonStyle.green,row=0)
    async def three(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 3
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="4",style=nextcord.ButtonStyle.green,row=1)
    async def four(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 4
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="5",style=nextcord.ButtonStyle.green,row=1)
    async def five(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 5
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="6",style=nextcord.ButtonStyle.green,row=1)
    async def six(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 6
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="7",style=nextcord.ButtonStyle.green,row=3)
    async def seven(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 7
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="8",style=nextcord.ButtonStyle.green,row=3)
    async def eight(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 8
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="9",style=nextcord.ButtonStyle.green,row=3)
    async def nine(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 9
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="裝飾",style=nextcord.ButtonStyle.gray,row=4)
    async def none(self, button: nextcord.ui.Button, interaction:Interaction):
        pass
    @nextcord.ui.button(label="0",style=nextcord.ButtonStyle.green,row=4)
    async def zero(self, button: nextcord.ui.Button, interaction:Interaction):
        self.choice = 0
        if self.choice is None:
            if len(self.password_payload) <= 4:
                self.password_payload["first"] = self.choice
                if self.password_payload["first"] != "":
                    self.password_payload["second"] = self.choice
                elif self.password_payload["second"] != "":
                    self.password_payload["three"] = self.choice
                elif self.password_payload["three"] != "":
                    self.password_payload["four"] = self.choice
            else:
                print(self.password_payload["first"]+self.password_payload["second"]+self.password_payload["three"]+self.password_payload["four"])
    @nextcord.ui.button(label="裝飾",style=nextcord.ButtonStyle.gray,row=4)
    async def none2(self, button: nextcord.ui.Button, interaction:Interaction):
        pass


class Modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("請輸入密碼")
    
        self.password = nextcord.ui.TextInput(
                label="請輸入四位數密碼 (可留空)",
                min_length=4,
                max_length=4,
                required=False
            )
        self.add_item(self.password)

    async def callback(self, interaction: Interaction):
        global join_channel
        global message_channel
        global password
        if self.password.value == "":
            number = random.randint(0000,9999)
            password = number
            channel = interaction.user.voice.channel
            embed = nextcord.Embed(title=f":lock: | 已成功鎖定!",description=f"密碼為 `{password}`!",colour=nextcord.Colour.green())
            embed.add_field(name=f"頻道",value=f"{channel.mention}")
            await interaction.response.send_message(embed=embed,ephemeral=True)
            channel = interaction.user.voice.channel
            overwrite = channel.overwrites_for(interaction.guild.default_role)
            overwrite.connect = False
            await channel.set_permissions(interaction.guild.default_role,overwrite=overwrite)
            if channel.category is None:
                pass
            else:
                message_channel = interaction.message.channel
                join_channel = await interaction.guild.create_voice_channel(name=f"進入此頻道以加入 {channel.name}",category=channel.category)
        else:
            channel = interaction.user.voice.channel
            password = self.password.value
            embed = nextcord.Embed(title=f":lock: | 已成功鎖定!",description=f"密碼為 `{self.password.value}`!",colour=nextcord.Colour.green())
            embed.add_field(name=f"頻道",value=f"{channel.mention}")
            await interaction.response.send_message(embed=embed,ephemeral=True)
            channel = interaction.user.voice.channel
            overwrite = channel.overwrites_for(interaction.guild.default_role)
            overwrite.connect = False
            await channel.set_permissions(interaction.guild.default_role,overwrite=overwrite)
            if channel.category is None:
                pass
            else:
                message_channel = interaction.message.channel
                join_channel = await interaction.guild.create_voice_channel(name=f"進入此頻道以加入 {channel.name}",category=channel.category)


class View(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label="初始化", style=nextcord.ButtonStyle.green)
    async def initialization(self, button: nextcord.ui.Button, interaction:Interaction):
        voice_state = interaction.user.voice
        if voice_state is None:
            embed = nextcord.Embed(title="<:x_mark:1033955039615664199> | 請先加入你要鎖定的語音頻道")
            await interaction.response.send_message(embed=embed,ephemeral=True)
        else:
            model = Modal()
            await interaction.response.send_modal(modal=model)
    


class enc(commands.Cog): #加密頻道
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        print("Enc Ready!")
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member:nextcord.Member, before, after):
        try:
            voice_channel = join_channel
        except NameError:
            return
        view = UnlockView()
        if not before.channel and after.channel:
            for channel in member.guild.voice_channels:
                if channel.name == voice_channel.name:
                    embed = nextcord.Embed(title="請輸入密碼",colour=nextcord.Colour.random())
                    await say.followup.send(embed=embed,view=view,ephemeral=True)
                    await view.wait()                            

    @nextcord.slash_command(name='enc',description="創立你專屬的加密頻道", guild_ids=[1003837176464810115])
    async def enc(self, interaction: Interaction):
        global say
        say = interaction
        embed = nextcord.Embed(title="設置專屬於你的加密頻道", description="加密頻道只需密碼便可進入", color=nextcord.Colour.random(), timestamp= datetime.datetime.utcnow())
        view = View()
        await interaction.response.send_message(view=view, embed=embed)
def setup(bot):
    bot.add_cog(enc(bot))