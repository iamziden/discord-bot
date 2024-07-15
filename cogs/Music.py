import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption

class Music(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.voice = None

    # Joins the voice channel that the user is in.
    @nextcord.slash_command(
        name="join",
        description="Join the active voice channel.",
    )
    async def join(self, interaction: Interaction):
        if interaction.guild.voice_client:
            await interaction.response.send_message("I am already in a voice channel.")
        else:
            if interaction.user.voice:
                channel = interaction.user.voice.channel
                self.voice = await channel.connect()
                await interaction.response.send_message(f"Joined {channel.name}.")
            else:
                await interaction.response.send_message("You are not currently in a voice channel!")

    # Leaves the voice channel the bot is in.
    @nextcord.slash_command(
        name="leave", 
        description="Leave the active voice channel.",
    )
    async def leave(self, interaction: Interaction):
        if self.voice and self.voice.is_connected():
            await self.voice.disconnect()
            self.voice = None
            await interaction.response.send_message("I left the voice channel.")
        else:
            await interaction.response.send_message("I am not currently in a voice channel.")
            
    # TO DO: Add YouTube support for video playing.

def setup(client):
    client.add_cog(Music(client))
