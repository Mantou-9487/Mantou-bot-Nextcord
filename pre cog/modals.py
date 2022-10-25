import discord
import datetime
from discord.ext import commands
from interactions import Modal,TextInput,TextStyleType
from core.classes import Cog_Extension

# 這邊可以使用Cog功能繼承基本屬性
class modal(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['modal'])
    async def _modal(self, ctx):
        modal = Modal(
            custom_id="modal",
            title="Modal Title",
            components=[
                TextInput(
                    style=TextStyleType.SHORT,
                    custom_id="text_input-1",
                    label="Short text input"
                ),
                TextInput(
                    style=TextStyleType.PARAGRAPH,
                    custom_id="text_input-2",
                    label="PARAGRAPH text input"
                ),
            ],
        )
        await ctx.popup(modal)

def setup(bot):
    bot.add_cog(modal(bot))
