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

---

This bot expects to see the following secrets stored in Vault in the path of `secrets/discord/invite-bot`:

|---|---|
|Key|Value|
|---|---|
|DISCORD_GUILD_ID||
|DISCORD_TOKEN||
|INVITE_CODE_01|<Insert unique invite code string>|
|INVITE_CODE_02|<Insert unique invite code string>|
|INVITE_CODE_03|<Insert unique invite code string>|
|INVITE_CODE_04|<Insert unique invite code string>|
|INVITE_CODE_05|<Insert unique invite code string>|
|INVITE_CODE_06|<Insert unique invite code string>|
|ROLE_01|<Insert unique Discord role name>|
|ROLE_02|<Insert unique Discord role name>|
|ROLE_03|<Insert unique Discord role name>|
|ROLE_04|<Insert unique Discord role name>|
|ROLE_05|<Insert unique Discord role name>|
|ROLE_06|<Insert unique Discord role name>|

NOTE: Invite code strings come from Discord invite URLs:

Example Discord Invite URL:

https://discord.gg/q093f5n83de

Invite code from this:

q093f5n83de

You create one hidden channel in your Discord server, per needed code.
You can then right-click on each channel, getting a unique invite code.
You can then map these invite codes to role names. The bot will
see which invite code was used and assign the mapped role to the user
when they join the Discord server using that invite URL.

# Bot Usage

Customize the Vault access details:

```
cp env_sample.txt .env
vi .env # Edit the file, inserting the bot vault username, password, and VAULT_ADDR connection string
```

If Vault has a self-signed SSL certificate, you need to create a `certs` directory and import Vault's SSL public key certificate file there. Maks sure the file is called `vault.crt`:

```
mkdir -p certs
```

Start the bot in a persistent fashion:

```
./setup-persistent-service.sh
```
