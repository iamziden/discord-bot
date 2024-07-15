import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption

# Provides useful commands for admin use, such as kicking, banning, and more.
class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kick a user.
    @nextcord.slash_command(
        name="kick",
        description="Kick a user from the server.",
    )
    async def kick(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = SlashOption(description="The user to kick.")
    ):
        if not self.has_manage_roles_permission(interaction.user):
            await interaction.response.send_message("You do not have permission to kick users.", ephemeral=True)
            return

        await user.kick()
        await interaction.response.send_message(f"Kicked {user.mention} from the server.")

    # Ban a user.
    @nextcord.slash_command(
        name="ban",
        description="Ban a user from the server.",
    )
    async def ban(
        self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = SlashOption(description="The user to ban.")
    ):
        if not self.has_manage_roles_permission(interaction.user):
            await interaction.response.send_message("You do not have permission to ban users.", ephemeral=True)
            return

        await user.ban()
        await interaction.response.send_message(f"Banned {user.mention} from the server.")

def setup(client):
    client.add_cog(Admin(client))