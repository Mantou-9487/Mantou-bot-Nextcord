import asyncio
import wavelink
import nextcord
import urllib.request
import json
from nextcord import Interaction
from nextcord import SlashOption
from nextcord.ext import commands
import time



class StopView(nextcord.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.view = Playerview()


class Playerview(nextcord.ui.View):
    def __init__(self):
      super().__init__(timeout=None)
      self.change = "Play"
      self.now_skip = None
    @nextcord.ui.button(label="", style=nextcord.ButtonStyle.gray,emoji="<:pause:1037002511439122523>")
    async def pause(self, button: nextcord.ui.Button, interaction:Interaction):
      vc: wavelink.Player = interaction.guild.voice_client
      if vc:
        if track_end != True:
          if self.change == "Play":
            await vc.pause()
            self.change = "Pause"
            button.emoji = "<:play:1037002859146915941>"
            embed = nextcord.Embed(title="<:pause:1037002511439122523> | 已暫停!", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)
            await interaction.followup.edit_message(message_id=message_fetch.id, content=None, view=self)
          elif self.change == "Pause":
            self.change = "Play"
            button.emoji = "<:pause:1037002511439122523>"
            await vc.resume()
            embed = nextcord.Embed(title="<:play:1037002859146915941> | 已繼續撥放!", colour=nextcord.Colour.green())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)
            await interaction.followup.edit_message(message_id=message_fetch.id, content=None, view=self)
        elif track_end == True:
          if self.change == "Play":
            await vc.pause()
            self.change = "Pause"
            button.label = "▶️"
            embed = nextcord.Embed(title="<:pause:1037002511439122523> | 已暫停!", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)
            await interaction.followup.edit_message(message_id=message_fetch.id, content=None, view=self)
          elif self.change == "Pause":
            self.change = "Play"
            button.label = "⏸"
            await vc.resume()
            embed = nextcord.Embed(title="<:play:1037002859146915941> | 已繼續撥放!", colour=nextcord.Colour.green())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed)
            await interaction.followup.edit_message(message_id=message_fetch.id, content=None, view=self)
      else:
          embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
          embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          await interaction.response.send_message(embed=embed, ephemeral=True)

    @nextcord.ui.button(label="", style=nextcord.ButtonStyle.gray, emoji="<:skip:1036113702115623014>")
    async def skip(self, button: nextcord.ui.Button, interaction:Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        global now_skip
        now_skip = self.now_skip
        if vc:
          self.now_skip = True
          now_skip = self.now_skip
          await vc.seek(vc.track.length * 1000)
          embed = nextcord.Embed(title="<:skip:1036113702115623014> 已跳過歌曲!", colour=nextcord.Colour.green())
          embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          await interaction.response.send_message(embed=embed)
          self.now_skip = False
          now_skip = self.now_skip
        else:
            embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
            embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @nextcord.ui.button(label="中斷連線", style=nextcord.ButtonStyle.red)
    async def disconnect(self, button: nextcord.ui.Button, interaction:Interaction):
      vc: wavelink.Player = interaction.guild.voice_client
      global have_disconnect
      if vc:
        have_disconnect = True
        await vc.disconnect()
        embed = nextcord.Embed(title=" 我被 {} 中斷連線了!".format(interaction.user.name), colour=nextcord.Colour.red())
        vc.queue.clear()
        embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
        await interaction.response.send_message(embed=embed)
      else:
          embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
          embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          await interaction.response.send_message(embed=embed, ephemeral=True)

    @nextcord.ui.button(label="更新", style=nextcord.ButtonStyle.green, emoji="<:Update:1036992904352243743>")
    async def update(self, button: nextcord.ui.Button, interaction:Interaction):
      vc: wavelink.Player = interaction.guild.voice_client
      if vc:
            print(message_fetch.id)
            track = wavelink.Track(id=vc.track.id, info=vc.track.info)
            yttrack = wavelink.YouTubeTrack(id=vc.track.id, info=vc.track.info)
            sec = track.length
            length_time = "%02d:%02d" %divmod(sec, 60)
            now_time = "%02d:%02d" %divmod(track_time, 60)
            url = track.uri
            if wait_song == None or here_song == False:
              print("歌曲時間: " + now_time)
              update_track = wavelink.Track(id=vc.track.id, info=vc.track.info) 
              embed = nextcord.Embed(title="{}".format(update_track.title), description="{1} / {0}".format(length_time, now_time) ,colour=nextcord.Colour.random(),url=url)
              embed.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
              embed.add_field(name="下一首歌",value="沒有下一首歌!", inline=False)
              embed.set_thumbnail(yttrack.thumbnail)
              await interaction.response.send_message("已更新!", ephemeral=True)
              await interaction.followup.edit_message(message_id=message_fetch.id,embed=embed, view=self)
            else:
              print("歌曲時間: " + now_time)
              embed = nextcord.Embed(title="{}".format(track.title), description="{1} / {0}".format(length_time, now_time) ,colour=nextcord.Colour.random(),url=url)
              embed.set_footer(text="機器人作者by 鰻頭!", icon_url= "https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
              embed.add_field(name="下一首歌",value=f"[{title}]({wait_song})", inline=False)
              embed.set_thumbnail(yttrack.thumbnail)
              await interaction.response.send_message("已更新!", ephemeral=True)
              await interaction.followup.edit_message(message_id=message_fetch.id,embed=embed, view=self)
      else:
          embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
          embed.set_footer(text="機器人作者by 鰻頭", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          await interaction.response.send_message(embed=embed, ephemeral=True)


class CustomPlayer(wavelink.Player):
  def __init__(self):
     self.queue = wavelink.Queue()
     self.node = wavelink.NodePool.get_node()

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.track_end = None
        self.here_song = False
        bot.loop.create_task(self.connect_nodes())

    @commands.Cog.listener()
    async def on_ready(self):
      print("Music Ready!")

    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot,
                                            host='lavalink.oops.wtf',
                                            port=443,
                                            password='www.freelavalink.ga',
                                            https=True,
                                            identifier='Main')
    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @nextcord.slash_command(name='play',description="播個音樂")
    async def play(self, interaction: Interaction, song:str = SlashOption(description="Song Name")):
        global here_song
        global say
        global wait_song
        global message_fetch
        global track_end
        track_end = self.track_end
        say = interaction
        here_song = self.here_song
        wait_song = song
        print("hay2")
        view = Playerview()
        print("hay")
        if not getattr(interaction.user.voice, "channel", None):
          return await interaction.response.send_message("先加入語音啦!")
        else:
            vc: wavelink.Player = interaction.guild.voice_client
        if interaction.guild.voice_client == None:
            vc: wavelink.Player = await interaction.user.voice.channel.connect(cls=wavelink.Player)
        if vc.queue.is_empty and not vc.is_playing():
          global search
          search = await wavelink.YouTubeTrack.search(query=song, return_first=True)
          await vc.play(search)
          track = wavelink.Track(id=vc.track.id, info=vc.track.info)
          yttrack = wavelink.YouTubeTrack(id=vc.track.id, info=vc.track.info)
          url = track.uri
          sec = track.length
          length_time = "%02d:%02d" %divmod(sec, 60)
          print(track.info)
          embed = nextcord.Embed(title="{}".format(search.title), description="00:00 / {0}".format(length_time) ,colour=nextcord.Colour.random(),url=url)
          embed.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          embed.add_field(name="下一首歌",value="沒有下一首歌!", inline=False)
          embed.set_thumbnail(yttrack.thumbnail)
          message = await interaction.response.send_message("▶ | 正在播放", embed=embed ,view=view)
          message_fetch = await message.fetch()
          await view.wait()
        else:
          global title
          wait_song = song
          yttrack = wavelink.YouTubeTrack(id=vc.track.id, info=vc.track.info)
          track = wavelink.Track(id=vc.track.id, info=vc.track.info)
          search = await wavelink.YouTubeTrack.search(query=song, return_first=True)
          await vc.queue.put_wait(search)
          api = "AIzaSyDhxhd0wQL3q2TMBo0QD5WVV_rqpwJwP4A"
          id = song.removeprefix("https://www.youtube.com/watch?v=")
          data = urllib.request.urlopen(f"https://www.googleapis.com/youtube/v3/videos?id={id}&key={api}&part=snippet").read()
          title = json.loads(data)['items'][0]['snippet']['title']
          embed = nextcord.Embed(title="<:check:1036160202174627840> 已將 {} 放入佇列上!".format(title), colour=nextcord.Colour.random())
          embed.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          await interaction.response.send_message(embed=embed)
          url = track.uri
          sec = track.length
          length_time = "%02d:%02d" %divmod(sec, 60)
          now_time = "%02d:%02d" %divmod(track_time, 60)
          if self.here_song == False:
            self.here_song = True
            here_song = self.here_song
            print("一號")
            embed1 = nextcord.Embed(title="{}".format(track.title), description="{1} / {0}".format(length_time, now_time) ,colour=nextcord.Colour.random(),url=url)
            embed1.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            embed1.add_field(name="下一首歌",value=f"[{title}]({song})", inline=False)
            embed1.set_thumbnail(yttrack.thumbnail)
            await interaction.followup.edit_message(message_id=message_fetch.id, embed=embed1, view=view)
            await view.wait()
          elif self.here_song == True:
            print(self.here_song)
            print("二號")
            global payload_url
            payload_url = {"title": '','url': ''}
            payload_url["title"] = title
            payload_url["url"] = song
            pass

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track:wavelink.YouTubeTrack, reason):
        vc: wavelink.Player = say.guild.voice_client
        next_song = vc.queue.get()
        await vc.play(next_song)
        view = Playerview()
        global here_song
        here_song = self.here_song
        self.track_end = True
        url = track.uri
        sec = track.length
        now_time = "%02d:%02d" %divmod(track_time, 60)
        length_time = "%02d:%02d" %divmod(sec, 60)
        yttrack = wavelink.YouTubeTrack(id=vc.track.id, info=vc.track.info)
        print(track.info)
        if self.here_song == True:
          try:
            print("三號")
            embed = nextcord.Embed(title="{}".format(track.title), description="{1} / {0}".format(length_time, now_time) ,colour=nextcord.Colour.random(),url=url)
            embed.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            next_title = payload_url["title"][0]
            next_url = payload_url["url"][0]
            embed.add_field(name="下一首歌",value=f"[{next_title}]({next_url})", inline=False)
            embed.set_thumbnail(yttrack.thumbnail)
            await say.followup.edit_message(message_id=message_fetch.id, content="▶ | 正在播放", embed=embed1 ,view=view)
            del payload_url["title"][0]
            del payload_url["url"][0]
            print(self.here_song)
          except NameError:
            self.here_song = False
            here_song = self.here_song
            embed1 = nextcord.Embed(title="{}".format(title), description="{1} / {0}".format(length_time, now_time) ,colour=nextcord.Colour.random(),url=url)
            embed1.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
            embed1.add_field(name="下一首歌",value="沒有下一首歌!", inline=False)
            embed1.set_thumbnail(yttrack.thumbnail)
            await say.followup.edit_message(message_id=message_fetch.id, content="▶ | 正在播放", embed=embed1 ,view=view)
            print("四號")
            pass
        elif self.here_song == False:
          print("五號")
          embed1 = nextcord.Embed(title="{}".format(track.title), description="{1} / {0}".format(length_time, now_time) ,colour=nextcord.Colour.random(),url=url)
          embed1.set_footer(text="機器人作者by 鰻頭!", icon_url="https://cdn.discordapp.com/avatars/949535524652216350/f1e7eb9ffd7d225971468d24748b1ba0.png?size=512")
          embed1.add_field(name="下一首歌",value="沒有下一首歌!", inline=False)
          embed1.set_thumbnail(yttrack.thumbnail)
          await say.followup.edit_message(message_id=message_fetch.id, content="▶ | 正在播放", embed=embed1 ,view=view)
            


    @commands.Cog.listener()
    async def on_wavelink_track_start(self, player: wavelink.Player, track:wavelink.YouTubeTrack):
      vc: wavelink.Player = say.guild.voice_client
      global track_time
      track_time = 0
      sec = int(track.length)
      for i in range(0, sec):
        i1 = i + 1
        track_time = i1 
        await asyncio.sleep(1)
        print(track_time)
        try:
          if track_time == sec or now_skip == True or have_disconnect == True:
            break
        except NameError:
          pass


def setup(bot):
  bot.add_cog(Music(bot))
