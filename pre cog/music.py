import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from core.classes import Cog_Extension
import yt_dlp as youtube_dl
from nextcord.utils import get
import asyncio
import json
import os


# 這邊可以使用Cog功能繼承基本屬性
class music(commands.Cog):

  def __init__(self, bot, ctx:commands.Context):
    self.bot = bot
    self.ctx = ctx

  @nextcord.slash_command(name='p',description="播個音樂", guild_ids=[1003837176464810115])
  async def _play(self, interaction: Interaction, url: str):
    FFMPEG_OPTIONS = {
      'before_options':
      '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
      'options': '-vn'
    }
    global url1
    global title
    url1 = url
    channel = interaction.user.voice.channel
    voice = get(self.bot.voice_clients, guild=interaction.guild)
    if channel:
      if not voice:
        voice = await channel.connect()
    else:
      return await interaction.response.send_message(f"你沒連進去語音頻道")
    voice = nextcord.utils.get(self.bot.voice_clients, guild=interaction.guild)
    url = (f"{url1}")
    download(url1)
    for file in os.listdir("./"):
      if file.endswith(".json"):
        if not voice.is_playing():
          with open('playlist.json', 'r+') as jf:
            showinfo()
            print("我是一號測試點")
            data = json.load(jf)
            temp = data["Music"]
            nowurl = {"Title": f"{title}" + f" [{id}]"}
            temp.append(nowurl)
            write_json(data)
            voice = nextcord.utils.get(self.bot.voice_clients, guild=interaction.guild)

    if voice.is_playing():
      with open('playlist.json', 'r+') as jf:
        showinfo()
        data = json.load(jf)
        temp = data["Music"]
        queueurl = {"Title": f"{title}" + f" [{id}]"}
        temp.append(queueurl)
        write_json(data)
    else:

      with open('playlist.json', 'r+') as jf:
        showinfo()
        voice.play(nextcord.FFmpegPCMAudio(f"{data['Music'][0]['Title']}.mp3"),
                   after=lambda e: play_next(interaction, self))
        voice.is_playing()

    if voice.disconnect():
      with open('playlist.json', 'r+') as jf:
        showinfo()
        data = json.load(jf)
        del data['Music']

  @nextcord.slash_command(name='resume',
                          description="重播音樂",
                          guild_ids=[1003837176464810115])
  async def _resume(self, ctx):
    channel = ctx.author.voice.channel
    voice = get(self.client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
      voice.resume()
      await ctx.channel.send("開始音樂!")

  @nextcord.slash_command(name='pause',
                          description="暫停音樂",
                          guild_ids=[1003837176464810115])
  async def _pause(self, ctx):
    channel = ctx.author.voice.channel
    voice = get(self.client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
      voice.pause()
      await ctx.channel.send("已暫停音樂!")



  @nextcord.slash_command(name='skip',description="跳過音樂", guild_ids=[1003837176464810115])
  async def _skip(self, ctx):
    channel = ctx.author.voice.channel
    voice = get(self.bot.voice_clients, guild=ctx.guild)
    voice.pause()
    await ctx.invoke(self.play_next)

  async def check_for_play(self, ctx):
    with open('playlist.json', 'r+') as jf:
      queues = json.load(jf)
      if len(queues['Music']) >= 2:
        del queues['Music'][0]
        await self.ctx.invoke(self.play_next)

  async def play_next(self, interaction: Interaction):
    with open('playlist.json', 'r+') as jf:
      queues = json.load(jf)
      global source
      print(queues['Music'][0]['Title'], "new_song")
      showinfo()
      voice = nextcord.utils.get(self.bot.voice_clients, guild=interaction.guild)
      voice.play(nextcord.FFmpegPCMAudio(f"{queues['Music'][0]['Title']}.mp3", after=lambda e: await self.ctx.invoke(self.play_next)))
      voice.is_playing()


def showinfo():
  print("我是二號測試點")
  ydl_opts = {
    'format':
    'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url1, download=False)
    global title
    title = info['title']
    global id
    id = info['id']


def download(url):
  ydl_opts = {
    'format':
    'bestaudio/best',
    "postprocessors": [{
      "key": "FFmpegExtractAudio",
      "preferredcodec": "mp3",
      "preferredquality": "192"
    }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


def write_json(data, filename="playlist.json"):
  with open(filename, "w") as f:
    json.dump(data, f, indent=4)


def setup(bot):
  bot.add_cog(music(bot))
