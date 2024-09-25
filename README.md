# Discord Bot

A Discord bot built using Nextcord with several functionalities including greetings, admin commands, and logging.

## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/iamziden/discord-bot.git
    cd discord-bot
    ```

2. **(Optional but Recommended)** Create and activate a virtual environment:
    - On macOS and Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Edit the `discord_ids.py` file with your server and channel IDs:
    ```python
    welcomeChannelId = 123456789012345678  # Replace with your welcome channel ID
    goodbyeChannelId = 123456789012345678  # Replace with your goodbye channel ID
    logsChannelId = 123456789012345678  # Replace with your logs channel ID
    ```

5. Edit the `bot_token.py` file with your bot token:
    ```python
    bot_token = 'YOUR_TOKEN_HERE'  # Replace with your actual bot token
    ```

6. (Optional) Edit the `bot.py` file to change activity status:
    ```python
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.playing, name='/help'))
    ```

7. Run the bot:
    ```sh
    python bot.py
    ```

## Usage

The bot provides the following commands:
- `/help` - Provides information about bot commands.
- `/join` - Join the active voice channel.
- `/leave` - Leave the active voice channel.
- `/kick` - Kick a user from the server.
- `/ban` - Ban a user from the server.
- `/giverole` - Give a specific role to a specific user.
- `/removerole` - Remove a specific role from a specific user.

## Active Dev Badge

You can also claim your active developer badge by using the command:
- '/activedevbadge' - Provides link to claim Discord active dev badge.

## To Add
YouTube video playing ability.
