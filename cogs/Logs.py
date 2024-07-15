import nextcord
from nextcord.ext import commands
from nextcord import Embed, Message, Member

# Import Discord IDs.
from discord_ids import logsChannelId

class Logging(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Will send a embed log of the message that was edited.
    @commands.Cog.listener()
    async def on_message_edit(self, before: Message, after: Message):
        if before.content != after.content:
            embed = Embed(
                title="Message Edited",
                description=f"**Author:** {after.author.mention}\n"
                            f"**Channel:** {after.channel.mention}\n"
                            f"**Before:** {before.content}\n"
                            f"**After:** {after.content}",
                color=nextcord.Color.orange()
            )
            embed.set_footer(text=f"Message ID: {after.id}")
            # Replace with your logging channel ID
            logging_channel = self.client.get_channel(logsChannelId)
            if logging_channel:
                await logging_channel.send(embed=embed)

    # Will send a embed log of the message deleted.
    @commands.Cog.listener()
    async def on_message_delete(self, message: Message):
        embed = Embed(
            title="Message Deleted",
            description=f"**Author:** {message.author.mention}\n"
                        f"**Channel:** {message.channel.mention}\n"
                        f"**Content:** {message.content}",
            color=nextcord.Color.red()
        )
        embed.set_footer(text=f"Message ID: {message.id}")
        logging_channel = self.client.get_channel(logsChannelId)
        if logging_channel:
            await logging_channel.send(embed=embed)
            
    # Will send a embed log when a user joins.
    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        embed = Embed(
            title="Member Joined",
            description=f"**Member:** {member.mention}\n"
                        f"**Joined Server:** {member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"**Created Account:** {member.created_at.strftime('%Y-%m-%d %H:%M:%S')}",
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar)
        # Replace with your logging channel ID
        logging_channel = self.client.get_channel(logsChannelId)
        if logging_channel:
            await logging_channel.send(embed=embed)

    # Will send an embed log when a user leaves.
    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        embed = Embed(
            title="Member Left",
            description=f"**Member:** {member.mention}\n"
                        f"**Left Server:** {nextcord.utils.format_dt(member.joined_at, 'R')}",
            color=nextcord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar)
        # Replace with your logging channel ID
        logging_channel = self.client.get_channel(logsChannelId)
        if logging_channel:
            await logging_channel.send(embed=embed)

def setup(client):
    client.add_cog(Logging(client))
