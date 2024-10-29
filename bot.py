import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

# Import Discord API key from bot_token.py
# USER: Change YOUR_TOKEN_HERE in bot_token.py
from bot_token import bot_token

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

# Initialize the bot with a command prefix.
client = commands.Bot(command_prefix='!', intents=intents)

# Will print in terminal when the bot is ready to use.
# USER: Change '/help' to whatever you want the bot to display. Status and activity can also be changed.
@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.playing, name='/help'))
    print(f'The bot is now ready for use! Logged in as {client.user}')
    print("______________________________________________________")

# Define the help command to provide a list of available commands.
# USER: Add more commands here if you add more yourself.
@client.slash_command(
    name="help", 
    description="Provides information about bot commands",
)
async def help_command(interaction: nextcord.Interaction):
    help_message = (
        "Here are the available commands:\n"
        "/help - Provides information about bot commands.\n"
        "/join - Join the active voice channel.\n"
        "/leave - Leave the active voice channel.\n"
        "/kick - Kick a user from the server.\n"
        "/ban - Ban a user from the server.\n"
        "/giverole - Give a specific role to a specific user.\n"
        "/removerole - Remove a specific role from a specific user.\n"
        "/activedevbadge"
    )
    await interaction.response.send_message(help_message, ephemeral=True)  # Send as an ephemeral message

# List to store the initial extensions (cogs) to be loaded.
initial_extensions = []

# Search through the cogs folder and add each .py file as an extension.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

# Load the extensions.
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'Successfully loaded extension: {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            print(f'{type(e).__name__}: {e}')

# Run the bot with the loaded token.
client.run(bot_token)
