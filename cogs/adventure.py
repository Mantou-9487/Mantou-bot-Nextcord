import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Member
import datetime
import numpy as np
from numpy import random
import math
from typing import Optional
import pymongo

def upload(name, id, job):
    myclient = pymongo.MongoClient("mongodb://mongo:sHG7YDV0nMasrjtAuQ3m@containers-us-west-188.railway.app:6917")
    mydb = myclient['adventure']
    dblst = myclient.list_database_names()
    if "adventure" in dblst:
        print("冒險資料庫活著！")
    mycol = mydb["user"]
    collst = mydb.list_collection_names()
    if "user" in collst:   # testMongoCol 集合是否存在
        print("玩家清單集合活著！")
        nowtime = datetime.datetime.today()
        datetime_format = nowtime.strftime("%Y/%m/%d %H:%M:%S")
        data = {"Username":name, "ID":id, "Job":job, "Money":0 , "CreateTime":datetime_format}
        query_check = { "ID": { "$regex": f"^5" } }
        mydoc = mycol.find(query_check)
        for b in mydoc:
            print(b) 
        x = mycol.insert_one(data)
        x = mycol.find_one()

def search(id):
    myclient = pymongo.MongoClient("mongodb://mongo:sHG7YDV0nMasrjtAuQ3m@containers-us-west-188.railway.app:6917")
    mydb = myclient['adventure']
    mycol = mydb["user"]
    data = {"ID": id}
    mydoc = mycol.find(data)
    for x in mydoc:
        print(x)
        global money
        money = x['Money']


class jobDropdown(nextcord.ui.Select):
    def __init__(self):
        selectOptions = [
            nextcord.SelectOption(label="魔法師",description="單身好幾年的魔法師,適合單身的人"),
            nextcord.SelectOption(label="戰士",description="於隊伍中衝鋒的前排砲灰 (x")
        ]
        super().__init__(placeholder="選擇一個職業",min_values=1,max_values=1,options=selectOptions)
    
    async def callback(self, interaction: Interaction):
        if self.values[0] == "魔法師":
            upload(name=interaction.user.name, id=interaction.user.id, job=self.values[0])
            embed = nextcord.Embed(title="<:check:1036160202174627840> | 職業設定成功",description="你選擇的是 魔法師!",colour=nextcord.Colour.green())
            await interaction.response.send_message(embed=embed,ephemeral=True)

        elif self.values[0] == "戰士":
            upload(name=interaction.user.name, id=interaction.user.id, job=self.values[0])
            embed = nextcord.Embed(title="<:check:1036160202174627840> | 職業設定成功",description="你選擇的是 戰士!",colour=nextcord.Colour.green())
            await interaction.response.send_message(embed=embed,ephemeral=True)

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(jobDropdown())

class adv(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("冒險準備好了!")
    
    @nextcord.slash_command(name="選擇職業",description="測試",name_localizations={"en-US": "job"},guild_ids=[1003837176464810115])
    async def job(self, interaction:Interaction):
        if interaction.user.id != 549056425943629825:
            embed = nextcord.Embed(title="<:x_mark:1033955039615664199> | 正在開發!",colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)
        else:
            embed = nextcord.Embed(title="<:adv:1055453748396298280> | 冒險者公會",description="你來到了冒險者公會登記職業\n選個你喜歡的職業吧!",colour=nextcord.Colour.random())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            view = DropdownView()
            await interaction.response.send_message(embed=embed,view=view)

    @nextcord.slash_command(name="查看錢錢",description="測試",name_localizations={"en-US": "money"},guild_ids=[1003837176464810115])
    async def money(self, interaction:Interaction):
        search(id=interaction.user.id)
        embed = nextcord.Embed(description=f"你現在有 `{money}` 元",colour=nextcord.Colour.orange())
        embed.set_author(name=interaction.user.name,icon_url=interaction.user.avatar.url)
        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(adv(bot))
