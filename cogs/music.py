
from distutils.cmd import Command
from re import T
from urllib import response
import wavelink
import nextcord
from nextcord import Interaction
from nextcord import SlashOption
from nextcord.ext import commands

class CustomPlayer(wavelink.Player):
  def __init__(self):
     self.queue = wavelink.Queue()

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

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
    async def play(self, interaction: Interaction, search:str = SlashOption(description="Song Name")):
        search = await wavelink.YouTubeTrack.search(query=search, return_first=True)
        if not interaction.guild.voice_client:
            vc: wavelink.Player = await interaction.user.voice.channel.connect(cls=wavelink.Player)
        elif not getattr(interaction.user.voice, "channel", None):
          return await interaction.response.send_message("先加入語音啦!")
        else:
            vc: wavelink.Player = interaction.guild.voice_client
        if vc.queue.is_empty and not vc.is_playing():
          await vc.play(search)
          await interaction.response.send_message(f"正在播放 {search.title}")
        else:
          await vc.queue.put_wait(search)
          await interaction.response.send_message(f"加入了 {search.title} 到佇列上!")

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: CustomPlayer, track:wavelink.YouTubeTrack, reason):
        next_song = player.queue.get()
        await player.play(next_song)

    @nextcord.slash_command(name='skip',description="跳過音樂")
    @commands.is_owner()
    async def skip(self, interaction: Interaction):
      vc: wavelink.Player = interaction.guild.voice_client
      if vc:
        if not vc.is_playing():
          return await interaction.response.send_message("沒歌在播放")
        if vc.queue.is_empty:
          return await vc.stop()
        
        await vc.seek(vc.track.length * 1000)
        if vc.is_paused():
          await vc.resume()
      else:
        await interaction.response.send_message("先加入語音啦!")

def setup(bot):
  bot.add_cog(Music(bot))
