import nextcord
import aiohttp
import requests
from nextcord.ext import commands
from nextcord import Interaction

class StateView(nextcord.ui.View):
    def __init__(self, timeout=None):
        self.state = None
        super().__init__(timeout=timeout)

    async def SendToWebhook(self, webhookurl, content):
        async with aiohttp.ClientSession() as session:
            webhook = nextcord.Webhook.from_url(webhookurl, session=session)
            await webhook.send(content)

    @nextcord.ui.button(label="同意聯繫",style=nextcord.ButtonStyle.green)
    async def agree(self, button: nextcord.ui.Button, interaction:Interaction):
        for categorys in guild.categories:
            if categorys == "客服類別":
                break
            else:
                category = await guild.create_category("客服類別", overwrites=interaction.channel.overwrites, reason=None)
            for channels in guild.text_channels:
                name1 = user.replace("(","")
                name2 = name1.replace(")","")
                name = name2.lower()
                print(channels)
                print(name)
                if channels == name:
                    print("hay")
                    channel = nextcord.utils.get(guild.text_channels, name=f"{name}" + f"{tag}")
                    await channel.create_webhook(name=f"{name}" + "#{tag}")
                    webhooks = await channel.webhooks()
                    print(webhooks)
                    break
                else:
                    print("hay2")
                    await guild.create_text_channel(f"{name}" + f"#{tag}",overwrites=interaction.channel.overwrites, category=category, reason=None)
                    print(name2)
                    channel = nextcord.utils.get(guild.text_channels, name=f"{name}" + f"{tag}")
                    await channel.create_webhook(name=f"{name}" + "#{tag}")
                    webhooks = await channel.webhooks()
                    print(webhooks)
                    break


    @nextcord.ui.button(label="拒絕聯繫",style=nextcord.ButtonStyle.red)
    async def deny(self, button: nextcord.ui.Button, interaction:Interaction):
        pass
        print("我拒絕聯繫")

class View(nextcord.ui.View):
    def __init__(self, timeout=None):
        self.state = None
        super().__init__(timeout=timeout)
    @nextcord.ui.button(label="開始聯繫",emoji="<:mail:1044958350925889567>",style=nextcord.ButtonStyle.green)
    async def start(self, button: nextcord.ui.Button, interaction:Interaction):
        global state
        embed = nextcord.Embed(title="請稍後", description="正在嘗試與管理員聯繫",colour=nextcord.Colour.yellow())
        await interaction.response.send_message(embed=embed)
        self.state = "Idle"
        state = self.state
        channel = nextcord.utils.get(guild.text_channels, name="請求聯繫")
        global user #請求人
        global tag
        user = interaction.user.name
        tag = interaction.user.discriminator
        embed = nextcord.Embed(title="聯繫請求!",description=f"{interaction.user.name} 想請求管理員連線!",colour=nextcord.Colour.random())
        view = StateView()
        await channel.send(embed=embed,view=view)
        #await channel.create_webhook(name=interaction.user.name)
        #webhook = await channel.webhooks()
        #print(webhook)

class Report(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        super().__init__()  
    #私訊機器人偵測
    @commands.Cog.listener()
    async def on_message(self, message:nextcord.Message):
        if message.author == self.bot.user: # Don't reply to itself. Could again be client for you
            return
        if isinstance(message.channel, nextcord.DMChannel): #If you want this to work in a group channel, you could also check for discord.GroupChannel
            try:
                if state == "Idle":
                    embed = nextcord.Embed(title="你已經在嘗試連線了", description="請稍後...",colour=nextcord.Colour.red())
                    await message.channel.send(embed=embed)
                else:   
                    embed = nextcord.Embed(title="聯繫管理員", description="如果你是要和管理員反映事項的,請點下方按鈕開始聯繫",colour=nextcord.Colour.random())
                    view = View()
                    await message.channel.send(embed=embed,view=view)
            except NameError:
                embed = nextcord.Embed(title="聯繫管理員", description="如果你是要和管理員反映事項的,請點下方按鈕開始聯繫",colour=nextcord.Colour.random())
                view = View()
                await message.channel.send(embed=embed,view=view)
        global guild
        guild = self.bot.get_guild(1003837176464810115)     
        await self.bot.process_commands(message)
    
    @nextcord.slash_command(name='debug',description="test", guild_ids=[1003837176464810115])
    async def debug(self, interaction: Interaction):
        guild = self.bot.get_guild(1003837176464810115)
        for categorys in guild.categories:
            print(categorys)
            category = nextcord.utils.get(guild.categories, name=f"客服類別")
            await category.delete()
        await interaction.response.send_message("成功!")
def setup(bot):
    bot.add_cog(Report(bot))