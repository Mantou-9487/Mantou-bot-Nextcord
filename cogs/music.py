import wavelink
import nextcord
from nextcord import Interaction
from nextcord import SlashOption
from nextcord.ext import commands

class Playerview(nextcord.ui.View):
    def __init__(self):
      super().__init__()
      self.change = "Play"
      self.player = CustomPlayer()

    @nextcord.ui.button(label="⏸ / ▶️", style=nextcord.ButtonStyle.gray)
    async def pause(self, button: nextcord.ui.Button, interaction:Interaction):
      vc: wavelink.Player = interaction.guild.voice_client
      if vc:
        if self.change != "Play":
          await self.player.pause()
          self.change = "Pause"
          embed = nextcord.Embed(title="⏸ 已暫停!", colour=nextcord.Colour.red())
          await interaction.response.send_message(embed=embed, view=None)
        elif self.change == "Pause":
          self.change = "Play"
          await self.player.play()
          embed = nextcord.Embed(title="▶️ 已繼續撥放!", colour=nextcord.Colour.green())
          await interaction.response.send_message(embed=embed, view=None)
      else:
          embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
          await interaction.response.send_message(embed=embed, ephemeral=True)

    @nextcord.ui.button(label="", style=nextcord.ButtonStyle.red, emoji="<:skip:1036113702115623014>")
    async def skip(self, button: nextcord.ui.Button, interaction:Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if vc:
          await vc.seek(vc.track.length * 1000)
          embed = nextcord.Embed(title="<:skip:1036113702115623014> 已跳過歌曲!", colour=nextcord.Colour.green())
          await interaction.response.send_message(embed=embed, view=None)
        else:
            embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @nextcord.ui.button(label="中斷連線", style=nextcord.ButtonStyle.red, emoji="")
    async def disconnect(self, button: nextcord.ui.Button, interaction:Interaction):
      vc: wavelink.Player = interaction.guild.voice_client
      if vc:
        await self.player.disconnect()
        embed = nextcord.Embed(title=" 我被 {} 中斷連線了!".format(interaction.user.name), colour=nextcord.Colour.red())
        await interaction.response.send_message(embed=embed, view=None)
      else:
          embed = nextcord.Embed(title=":x: 我不在一個語音頻道喔!", colour=nextcord.Colour.red())
          await interaction.response.send_message(embed=embed, ephemeral=True)
          
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
        global say
        global wait_song
        wait_song = search
        say = interaction
        guild = self.bot.get_guild(1003837176464810115)
        playeremoji = nextcord.utils.get(guild.emojis, name="player")
        view = Playerview()
        search = await wavelink.YouTubeTrack.search(query=search, return_first=True)
        if not interaction.guild.voice_client:
            vc: wavelink.Player = await interaction.user.voice.channel.connect(cls=wavelink.Player)
        elif not getattr(interaction.user.voice, "channel", None):
          return await interaction.response.send_message("先加入語音啦!")
        else:
            vc: wavelink.Player = interaction.guild.voice_client
        if vc.queue.is_empty and not vc.is_playing():
          await vc.play(search)
          embed = nextcord.Embed(title="{}".format(search.title), colour=nextcord.Colour.random(),url=wait_song)
          await interaction.response.send_message("{} | 正在播放".format(playeremoji), embed=embed ,view=view)
        else:
          await vc.queue.put_wait(search)
          embed = nextcord.Embed(title="{}".format(wait_song.title),colour=nextcord.Colour.random(),url=wait_song)
        await interaction.response.send_message("{} | 正在播放".format(playeremoji), embed=embed ,view=view)

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: CustomPlayer, track:wavelink.YouTubeTrack, reason):
        guild = self.bot.get_guild(1003837176464810115)
        playeremoji = nextcord.utils.get(guild.emojis, name="player")
        next_song = player.queue.get()
        await player.play(next_song)
        view = Playerview()
        embed = nextcord.Embed(title="[{0}]({1})".format(wait_song.title, wait_song),description="")
        await say.response.send_message("{} | 正在播放".format(playeremoji), embed=embed ,view=view)

def setup(bot):
  bot.add_cog(Music(bot))
