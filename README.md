# Discord Targeted Invite to Discord Server Role Handler Bot

# Preparation

Step 1: Create a Bot on Discord

    Go to the [Discord Developer Portal](https://discord.com/developers/applications).

    Create a new application.

    Go to the "Bot" tab and click "Add Bot".

    Under Privileged Gateway Intents, enable:

        Server Members Intent

    Copy the bot token and set it in DISCORD_TOKEN.

    Oauth2 permissions:

    Required scopes: bot

    Permission	Needed For

    View Channels	To see the channels where users join
    Manage Roles	To assign roles to new users
    Manage Server (optional)	To fetch all invites (recommended)
    Read Message History	Useful for expansion / debugging

Step 2: Invite Bot to Your Server

Copy the generated URL at the bottom of the Oauth2 page and go there with a web browser. Select the server you want to invite the bot to and authorize it.

Step 3: Create Roles & Invite Links

    Create the roles AlphaRole, BetaRole, etc., in your Discord server.

    Generate invite links via Discord UI and note their invite codes.

    Map invite codes to roles in the role_map dictionary in bot.py.

# Bot Usage

```
cp env_sample.txt .env
vi .env # Edit the file, inserting your Discord bot Token
docker compose up --build -d
```
