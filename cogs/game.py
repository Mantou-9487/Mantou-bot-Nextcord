import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import datetime
import random
# 這邊可以使用Cog功能繼承基本屬性

class Subscriptions(nextcord.ui.View):
    def __init__(self, ctx:commands.Context):
        super().__init__()
        self.ctx = ctx
        self.value = None
        self.choice = None
    
    @nextcord.ui.button(label = "✂️", style=nextcord.ButtonStyle.green)
    async def scissors(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = True
        self.choice = 2
        self.stop()

    @nextcord.ui.button(label = "🪨", style=nextcord.ButtonStyle.red)
    async def rock(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = True
        self.choice = 1
        self.stop()

    @nextcord.ui.button(label = "🖐", style=nextcord.ButtonStyle.blurple)
    async def paper(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = True
        self.choice = 3
        self.stop()


    async def interaction_check(self, interaction: nextcord.Interaction):
        if interaction.user.id != self.ctx.id:
            await interaction.response.send_message("你點這幹嘛?")
        else:
            user_result = {self.choice}
            computer_result = random.choice([1,2,3])
            embed = nextcord.Embed(color=nextcord.Colour.random(), title="🤖| 剪刀石頭布",description="" ,timestamp= datetime.datetime.utcnow())
            if ((computer_result == 1 and user_result == 3) or (computer_result == 2 and user_result == 1) or (computer_result == 3 and user_result == 2)): #玩家贏了
                embed.add_field(name="你出了", value="{}".format(user_result), inline=False)
                embed.add_field(name="我出了", value="{}".format(computer_result), inline=False)
                embed.add_field(name="結果", value="你贏了!", inline=False)
                self.paper.disabled = True
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
        view = Subscriptions(interaction.user)
        embed = nextcord.Embed(color=nextcord.Colour.random(), title="🤖| 剪刀石頭布",description="你要出啥呢?" ,timestamp= datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed, view=view)
        await view.wait()

def setup(bot):
    bot.add_cog(game(bot))