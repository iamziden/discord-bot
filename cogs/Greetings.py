import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import Member, Embed

# Import Discord IDs.
from discord_ids import welcomeChannelId, goodbyeChannelId

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Will send a embed welcome message upon a join.
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        role = nextcord.utils.get(guild.roles, name="MEMBER")
        
        if role:
            await member.add_roles(role)
            
        embed = Embed(
            title=f"Welcome {member.display_name} to {guild.name}!",
            description=f"We are excited to have you here, {member.mention}!",
            color=member.accent_color if member.accent_color else nextcord.Color.default()
        )
        
        embed.set_thumbnail(url=member.avatar)
        
        channel = self.client.get_channel(welcomeChannelId)
        await channel.send(embed=embed)

    # Will send a goodbye message when a user leaves.
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(goodbyeChannelId)
        await channel.send(f"Goodbye {member.mention}.")
        
def setup(client):
    client.add_cog(Greetings(client))
