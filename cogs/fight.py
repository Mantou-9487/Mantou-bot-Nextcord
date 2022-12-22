import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Member
import datetime
import numpy as np
from numpy import random
from typing import Optional



class View(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        self.choice = None
    
    @nextcord.ui.button(label= "我接受!", style=nextcord.ButtonStyle.green)
    async def agree(self, button: nextcord.ui.Button, interaction:Interaction):
        if victim != str(interaction.user.id):
            embed = nextcord.Embed(title=":x: | 你幹嘛自己點", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if victim == str(interaction.user.id):
            self.value = False
            self.choice = "agree"
            self.stop()

    @nextcord.ui.button(label= "我拒絕!", style=nextcord.ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, interaction:Interaction):
        if victim != str(interaction.user.id):
            embed = nextcord.Embed(title=":x: | 你幹嘛自己點", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if victim == str(interaction.user.id):
            self.value = False
            self.choice = "deny"
            self.stop()
     
class AttackView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=0)
        self.value = None
        self.防禦 = None
        self.action = victim
        self.victim_hp = 20 #被攻擊者
        self.attacker_hp = 20 #攻擊者
        self.round = 1
    @nextcord.ui.button(label= "攻擊他!", style=nextcord.ButtonStyle.green, emoji="<:sword:1033263249988268094>")
    async def attack(self, button: nextcord.ui.Button, interaction:Interaction):
        global victim_hp
        global attacker_hp
        victim_hp = self.victim_hp
        attacker_hp = self.attacker_hp
        global Deduct_attacker_hp
        global Deduct_victim_hp
        battleemoji = nextcord.utils.get(guild.emojis, name="sword2")
        emoji = nextcord.utils.get(guild.emojis, name="sword")
        vsemoji = nextcord.utils.get(guild.emojis, name="vs")
        shieldemoji = nextcord.utils.get(guild.emojis, name="shield1")
        if self.action == victim and victim == str(interaction.user.id):
            if self.防禦 == True:
                print("是我啦哈哈")
                Deducthp = random.randint(1,6) - Deductdef
                if Deducthp < 0:
                    Deducthp = 0
                    print("被攻方的防禦值:" + str(Deductdef))
                    print("被攻方減少的hp:" + str(Deducthp))
                    Deduct_attacker_hp = self.attacker_hp - Deducthp
                    self.attacker_hp = Deduct_attacker_hp
                    print("攻擊方血量 " + str(attacker_hp))
                    embed = nextcord.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=nextcord.Colour.red())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    embed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=nextcord.Colour.random())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                    self.round = self.round + 1
                    self.action = attacker
                    self.value = False
                    self.防禦 = None
                else:
                    print("被攻方的防禦值:" + str(Deductdef))
                    print("被攻方減少的hp:" + str(Deducthp))
                    Deduct_attacker_hp = self.attacker_hp - Deducthp
                    self.attacker_hp = Deduct_attacker_hp
                    print("攻擊方血量 " + str(attacker_hp))
                    embed = nextcord.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=nextcord.Colour.red())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    embed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=nextcord.Colour.random())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                    self.round = self.round + 1
                    self.action = attacker
                    self.value = False
                    self.防禦 = None
            elif self.防禦 == None or False:
                print(self.action)
                Deducthp = random.randint(1,5)
                Deduct_attacker_hp = self.attacker_hp - Deducthp
                self.attacker_hp = Deduct_attacker_hp
                print("攻擊方血量 " + str(attacker_hp))
                embed = nextcord.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(attacker, Deducthp), colour=nextcord.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                embed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(attacker, Deducthp, attacker, Deduct_attacker_hp, victim, victim_hp, interaction.user.mention, vsemoji), colour=nextcord.Colour.random())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
                self.round = self.round + 1
                self.value = False
                self.action = attacker
            elif self.action == victim and victim != str(interaction.user.id):
                print("攻擊時round:" + self.action)
                print("else被攻擊的人:" + str(interaction.user.id))
                embed = nextcord.Embed(title=":x: | 還沒到你的回合", colour=nextcord.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                pass

        if self.action == attacker and attacker == str(interaction.user.id):
            if self.防禦 == True:
                print("是我啦ㄏ哈")
                self.action = victim
                Deducthp = (random.randint(1,6)) - Deductdef
                if Deducthp < 0:
                    Deducthp = 0
                    print("攻方的防禦值:" + str(Deductdef))
                    print("攻方減少的hp:" + str(Deducthp))
                    Deduct_victim_hp = self.victim_hp - Deducthp
                    self.victim_hp = Deduct_victim_hp
                    embed = nextcord.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=nextcord.Colour.red())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    infoembed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=nextcord.Colour.random())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                    self.round = self.round + 1
                    self.防禦 = None
                    self.value = False
                else:
                    print("攻方的防禦值:" + str(Deductdef))
                    print("攻方減少的hp:" + str(Deducthp))
                    Deduct_victim_hp = self.victim_hp - Deducthp
                    self.victim_hp = Deduct_victim_hp
                    embed = nextcord.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=nextcord.Colour.red())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    infoembed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="因對方使用了{8}盾牌防禦部分傷害，因此 {6} 打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji, shieldemoji), colour=nextcord.Colour.random())
                    embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                    await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                    self.round = self.round + 1
                    self.防禦 = None
                    self.value = False

            elif self.防禦 == None or False:
                self.action = victim
                Deducthp = random.randint(1,5)
                Deduct_victim_hp = self.victim_hp - Deducthp
                self.victim_hp = Deduct_victim_hp
                print("被攻擊方血量 " + str(victim_hp))
                embed = nextcord.Embed(title="{0} | {1} 的攻擊!".format(battleemoji, interaction.user.name),description="你打了 <@{0}> `{1}` 滴血!!!".format(victim, Deducthp), colour=nextcord.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                infoembed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{6}打了 <@{0}> `{1}` 滴血!!!\n-------------------------------\n<@{2}> 的血為 `{3}`\n {7} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(victim, Deducthp, attacker, Deduct_attacker_hp, victim, Deduct_victim_hp, interaction.user.mention, vsemoji), colour=nextcord.Colour.random())
                infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
                self.round = self.round + 1
                self.value = False
        elif self.action == attacker and attacker != str(interaction.user.id):
            try:
                print("攻擊時round:" + self.action)
                print("else被攻擊的人:" + str(interaction.user.id))
                embed = nextcord.Embed(title=":x: | 還沒到你的回合", colour=nextcord.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                pass
            except nextcord.errors.InteractionResponded:
                pass
            
        if self.attacker_hp <= 0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = nextcord.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = nextcord.Embed(title="{0} | 遊戲結束!".format(trophyemoji),description="恭喜 {1} 勝利!!!!!!!!!".format(interaction.user.name), colour=int(color, 16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)
        elif self.victim_hp <=0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = nextcord.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = nextcord.Embed(title="{0} | 遊戲結束!".format(trophyemoji),description="恭喜 {1} 勝利!!!!!!!!!".format(interaction.user.name), colour=int(color,16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)

    @nextcord.ui.button(label= "防禦", style=nextcord.ButtonStyle.gray,emoji="<:shield1:1033672396353314856>")
    async def deftense(self, button: nextcord.ui.Button, interaction:Interaction):
        global Deductdef
        Deductdef = random.randint(2,5)
        shieldemoji = nextcord.utils.get(guild.emojis, name="shield1")
        emoji = nextcord.utils.get(guild.emojis, name="sword")
        vsemoji = nextcord.utils.get(guild.emojis, name="vs")
        if self.action == victim and victim == str(interaction.user.id):
            Deduct_victim_hp = self.victim_hp
            embed = nextcord.Embed(title="{0} | 狀態報告".format(shieldemoji),description="你使出了防禦! 對方攻擊你的傷害降低了!", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            embed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{0} 這回合使用了防禦!\n-------------------------------\n<@{1}> 的血為 `{2}`\n {3} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(interaction.user.mention, attacker, self.attacker_hp, vsemoji, victim, Deduct_victim_hp), colour=nextcord.Colour.random())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=self)
            self.round = self.round + 1
            self.value = False
            self.防禦 = True
            self.action = attacker
        elif self.action == victim and victim != str(interaction.user.id):
            print("else被攻擊的人:" + str(interaction.user.id))
            embed = nextcord.Embed(title=":x: | 還沒到你的回合", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            pass
        if self.action == attacker and attacker == str(interaction.user.id):
            print("攻擊時round:" + self.action)
            print("攻擊時:" + str(interaction.user.id))
            Deduct_victim_hp = self.victim_hp
            Deduct_attacker_hp = self.attacker_hp
            print("被攻擊方血量 " + str(victim_hp))
            embed = nextcord.Embed(title="{0} | 狀態報告".format(shieldemoji),description="你使出了防禦! 對方攻擊你的傷害降低了!", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            infoembed = nextcord.Embed(title="{0} | 戰鬥開始 - 第{1}回合!".format(emoji, self.round), description="{0} 這回合使用了防禦!\n-------------------------------\n<@{1}> 的血為 `{2}`\n {3} \n<@{4}> 的血為 `{5}`\n-------------------------------".format(interaction.user.mention, attacker, self.attacker_hp, vsemoji, victim, Deduct_victim_hp), colour=nextcord.Colour.random())
            infoembed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=infoembed, view=self)
            self.round = self.round + 1
            self.value = False
            self.防禦 = True
            self.action = victim
        elif self.action == attacker and attacker != str(interaction.user.id):
            try:
                print("else攻擊時round:" + self.action)
                print("else攻擊時:" + str(interaction.user.id))
                embed = nextcord.Embed(title=":x: | 還沒到你的回合", colour=nextcord.Colour.red())
                embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                pass
            except nextcord.errors.InteractionResponded:
                pass
        if self.attacker_hp <= 0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = nextcord.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = nextcord.Embed(title="{} | 遊戲結束!".format(trophyemoji),description="恭喜 {} 勝利!!!!!!!!!".format(interaction.user.name), colour=int(color, 16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)
        elif self.victim_hp <=0:
            inte = int("FFA500", 16)
            color = hex(inte)
            trophyemoji = nextcord.utils.get(guild.emojis, name="trophy")
            view = OverView()
            print("遊戲結束!")
            embed = nextcord.Embed(title="{} | 遊戲結束!".format(trophyemoji),description="恭喜 {} 勝利!!!!!!!!!".format(interaction.user.name), colour=int(color,16))
            await interaction.followup.edit_message(message_id=message_fetch.id ,embed=embed, view=view)

class OverView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    

class fight(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fight Ready!")
    
    @nextcord.slash_command(name='attack', description="攻擊你的朋友!")
    async def attack(self, interaction: Interaction, user:Optional[Member] = SlashOption(name="user", description="你要攻擊的朋友! 沒有朋友就算了",required=True)):
        global guild
        guild = self.bot.get_guild(1003837176464810115)
        emoji = nextcord.utils.get(guild.emojis, name="sword")
        global victim
        global attacker
        global viewround
        attacker = str(interaction.user.id)
        str1 = str(user.id).strip("<")
        str2 = str1.strip(">")
        victim = str2.strip("@")
        print(victim)
        view = View()
        if victim == str(interaction.user.id):
            print("點的人:" + str(attacker))
            print("被攻擊的人:" + victim)
            embed = nextcord.Embed(title=":x: | 你不能自己找自己當對手", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            embed = nextcord.Embed(title=":warning: 對決!", description="{} 想跟你對戰!".format(interaction.user.mention), colour=nextcord.Colour.random())
            message = await interaction.response.send_message("{}".format(user.mention) ,embed=embed, view=view)
            global message_fetch
            message_fetch = await message.fetch()
            print("元訊息id: "+ str(message_fetch.id))
            await view.wait()

        if view.value is None:
            return

        if view.choice == "agree":
            viewround = victim
            victim_hp = 20 #被攻擊者
            attacker_hp = 20 #攻擊者
            embed = nextcord.Embed(title="{} | 戰鬥開始!".format(emoji), description="{0} 的血為 `{1}`\n vs \n{2} 的血為 `{3}`".format(interaction.user.mention, attacker_hp, user.mention, victim_hp), colour=nextcord.Colour.random())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            attackview = AttackView()
            await interaction.edit_original_message(content=None,embed=embed, view=attackview)
               

        if view.choice == "deny":
            embed = nextcord.Embed(title=":x: 他不跟你打", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.edit_original_message(content=None ,embed=embed, view=None)


    async def cog_command_error(interaction:Interaction, error):
        embed = nextcord.Embed(title=":x: 出現錯誤了!!!", description=f"```{error}```")
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(fight(bot))
