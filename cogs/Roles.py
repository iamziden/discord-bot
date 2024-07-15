import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption

# Provides useful commands for admin use, such as kicking, banning, and more.
class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    def has_manage_roles_permission(self, member: nextcord.Member):
        # Check if the member has the manage_roles permission
        return member.guild_permissions.manage_roles

    # Give a role to a user.
    @nextcord.slash_command(
        name="giverole",
        description="Give a specific role to a specific user.",
    )
    async def give_role(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(description="The user to assign the role to."),
        role: nextcord.Role = SlashOption(description="The role to assign to the user.")
    ):
        if not self.has_manage_roles_permission(interaction.user):
            await interaction.response.send_message("You do not have permission to give roles.", ephemeral=True)
            return

        if role in user.roles:
            await interaction.response.send_message(f"{user.mention} already has the role {role.mention}.", ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"Assigned role {role.mention} to {user.mention}.")

    # Remove a role from a user.
    @nextcord.slash_command(
        name="removerole",
        description="Remove a specific role from a specific user.",
    )
    async def remove_role(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(description="The user to remove the role from."),
        role: nextcord.Role = SlashOption(description="The role to remove from the user.")
    ):
        if not self.has_manage_roles_permission(interaction.user):
            await interaction.response.send_message("You do not have permission to remove roles.", ephemeral=True)
            return

        if role not in user.roles:
            await interaction.response.send_message(f"{user.mention} does not have the role {role.mention}.", ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Removed role {role.mention} from {user.mention}.")

def setup(client):
    client.add_cog(Roles(client))
