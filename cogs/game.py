import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import datetime
import random
# 這邊可以使用Cog功能繼承基本屬性

class Subscriptions(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.win = 0
        self.choice = None
    
    @nextcord.ui.button(label= "✂️", style=nextcord.ButtonStyle.green)
    async def Scissors(self, button: nextcord.ui.Button, interaction:Interaction):
        if Player != str(interaction.user.id):
            embed = nextcord.Embed(title=":x: | 你幹嘛自己點", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if Player == str(interaction.user.id):
            self.value = False
            self.choice = "剪刀"
            user_result = self.choice
            print(user_result)
            computer_result = random.choice(["剪刀","石頭","布"])
            embed = nextcord.Embed(color=nextcord.Colour.random(), title="🤖 | 剪刀石頭布",description=f"<:trophy:1033707678654005358> 勝利場數: {self.win} 場" ,timestamp= datetime.datetime.utcnow())
            if ((computer_result == "布" and user_result == "剪刀") or (computer_result == "石頭" and user_result == "布") or (computer_result == "剪刀" and user_result == "石頭")): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.win += 1
                await interaction.response.edit_message(embed=embed)
            elif user_result == computer_result:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="平手!", inline=False)
                await interaction.response.edit_message(embed=embed)
            else:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="我贏了!", inline=False)
                await interaction.response.edit_message(embed=embed)

    @nextcord.ui.button(label = "🪨", style=nextcord.ButtonStyle.red)
    async def rock(self, button: nextcord.ui.Button, interaction: Interaction):
        if Player != str(interaction.user.id):
            embed = nextcord.Embed(title=":x: | 你幹嘛自己點", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if Player == str(interaction.user.id):
            self.value = False
            self.choice = "石頭"
            user_result = self.choice
            computer_result = random.choice(["剪刀","石頭","布"])
            embed = nextcord.Embed(color=nextcord.Colour.random(), title="🤖 | 剪刀石頭布",description=f"<:trophy:1033707678654005358> 勝利場數: {self.win} 場" ,timestamp= datetime.datetime.utcnow())
            if ((computer_result == "布" and user_result == "剪刀") or (computer_result == "石頭" and user_result == "布") or (computer_result == "剪刀" and user_result == "石頭")): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.win += 1
                await interaction.response.edit_message(embed=embed)
            elif user_result == computer_result:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="平手!", inline=False)
                await interaction.response.edit_message(embed=embed)
            else:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="我贏了!", inline=False)
                await interaction.response.edit_message(embed=embed)

    @nextcord.ui.button(label = "🖐", style=nextcord.ButtonStyle.blurple)
    async def paper(self, button: nextcord.ui.Button, interaction: Interaction):
        if Player != str(interaction.user.id):
            embed = nextcord.Embed(title=":x: | 你幹嘛自己點", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if Player == str(interaction.user.id):
            self.value = False
            self.choice = "布"
            user_result = self.choice
            print(user_result)
            computer_result = random.choice(["剪刀","石頭","布"])
            embed = nextcord.Embed(color=nextcord.Colour.random(), title="🤖 | 剪刀石頭布",description=f"<:trophy:1033707678654005358> 勝利場數: {self.win} 場" ,timestamp= datetime.datetime.utcnow())
            if ((computer_result == "布" and user_result == "剪刀") or (computer_result == "石頭" and user_result == "布") or (computer_result == "剪刀" and user_result == "石頭")): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.win += 1
                await interaction.response.edit_message(embed=embed)
            elif user_result == computer_result:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="平手!", inline=False)
                await interaction.response.edit_message(embed=embed)
            else:
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="我贏了!", inline=False)
                await interaction.response.edit_message(embed=embed)
class game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='剪刀石頭布',description="就是個剪刀石頭布",guild_ids=[1003837176464810115])
    async def game(self, interaction: Interaction):
        global Player
        Player = str(interaction.user.id)
        view = Subscriptions()
        embed = nextcord.Embed(color=nextcord.Colour.random(), title="🤖 | 剪刀石頭布",description="你要出啥呢?" ,timestamp= datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed, view=view)
        await view.wait()

def setup(bot):
    bot.add_cog(game(bot))