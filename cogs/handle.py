import nextcord
from typing import Optional
from nextcord.ext import commands,application_checks
from nextcord import Interaction, SlashOption
import pymongo
import math

def adv_eval(id, new:dict):
    myclient = pymongo.MongoClient("mongodb://mongo:sHG7YDV0nMasrjtAuQ3m@containers-us-west-188.railway.app:6917")
    mydb = myclient['adventure']
    mycol = mydb["user"]
    eval_data = {"ID": { "$regex": f"^{id}" }}
    eval_new = { "$set": new }
    mycol.update_one(eval_data,eval_new)
    

class ExceptionHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Error_Handle Ready!")

    @commands.Cog.listener()
    async def on_application_command_error(self, interaction:Interaction, error) -> None:
        print(error)
        if isinstance(error, application_checks.ApplicationMissingPermissions):
            embed = nextcord.Embed(title="<:x_mark:1033955039615664199> 無法執行此指令", description=f"請確認您是否有 `{error}` 的權限",colour=nextcord.Colour.red())
            await interaction.response.send_message(embed=embed,ephemeral=True)
        else:
            embed = nextcord.Embed(title=":x: 阿喔，看來你用神奇魔法發現了一個漏洞 <:hahahaha:1038449572915187763>", description=f"```{error}```\n <a:853174934670540811:1038449712359022643> 已自動回報給作者! Bug反饋可以聯繫Man頭(´・ω・)#8870",colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name='eval', description="噓~",guild_ids=[1003837176464810115])
    async def eval(self, interaction: Interaction, option:str = SlashOption(name="option",description="噓")):

        if interaction.user.id == 549056425943629825:
            print(f"邪惡的結果: {eval(option)}")
            embed = nextcord.Embed(title=":white_check_mark: | 神秘的結果", description="```py\n{}```".format(eval(option)),colour=nextcord.Colour.green())
            await interaction.response.send_message(embed=embed)
        else:
            embed = nextcord.Embed(title=":x: | 這個指令太過邪惡了,只有饅頭能夠駕馭他 (?")
            await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(ExceptionHandler(bot))
