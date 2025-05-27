import discord
import os
import hvac
import time
import threading
from discord.ext import commands
from dotenv import load_dotenv
import sys
sys.stdout.reconfigure(line_buffering=True)

# Load environment variables
load_dotenv()
VAULT_ADDR = os.getenv("VAULT_ADDR")
VAULT_USERNAME = os.getenv("VAULT_USERNAME")
VAULT_PASSWORD = os.getenv("VAULT_PASSWORD")

# Initialize Vault client (no token yet)
client = hvac.Client(url=VAULT_ADDR, verify="certs/vault.crt")

def login_and_set_token():
    """Login using userpass and set the client token."""
    response = client.auth.userpass.login(
        username=VAULT_USERNAME,
        password=VAULT_PASSWORD
    )
    client.token = response['auth']['client_token']
    return response['auth']['lease_duration']  # Token TTL in seconds

def token_refresher():
    """Background thread to re-login and refresh the Vault token."""
    while True:
        ttl = login_and_set_token()
        print(f"[Vault] Logged in via userpass. Token TTL: {ttl}s")
        # Refresh 30s before expiration
        sleep_time = max(60, ttl - 30)
        time.sleep(sleep_time)

# Start token refresher thread
threading.Thread(target=token_refresher, daemon=True).start()

# Wait until token is acquired
while not client.is_authenticated():
    time.sleep(1)

# Fetch secrets once authenticated
secrets = client.secrets.kv.v2.read_secret_version(
    path='discord/invite-bot',
    mount_point='secrets'
)['data']['data']

# Discord config
TOKEN = secrets['DISCORD_TOKEN']
GUILD_ID = int(secrets['DISCORD_GUILD_ID'])

INVITE_CODE_01 = secrets['INVITE_CODE_01']
ROLE_01 = secrets['ROLE_01']
INVITE_CODE_02 = secrets['INVITE_CODE_02']
ROLE_02 = secrets['ROLE_02']
INVITE_CODE_03 = secrets['INVITE_CODE_03']
ROLE_03 = secrets['ROLE_03']
INVITE_CODE_04 = secrets['INVITE_CODE_04']
ROLE_04 = secrets['ROLE_04']
INVITE_CODE_05 = secrets['INVITE_CODE_05']
ROLE_05 = secrets['ROLE_05']
INVITE_CODE_06 = secrets['INVITE_CODE_06']
ROLE_06 = secrets['ROLE_06']

# Set up Discord bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

invite_cache = {}

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    guild = bot.get_guild(GUILD_ID)
    invites = await guild.invites()
    for invite in invites:
        invite_cache[invite.code] = invite.uses
    print('Invite cache initialized.')

@bot.event
async def on_member_join(member):
    global invite_cache
    guild = member.guild
    invites = await guild.invites()
    used_invite = None

    for invite in invites:
        if invite.code in invite_cache and invite.uses > invite_cache[invite.code]:
            used_invite = invite
            break

    invite_cache = {inv.code: inv.uses for inv in invites}

    if used_invite:
        print(f'{member} joined using invite {used_invite.code}')
        role_map = {
            INVITE_CODE_01: ROLE_01,
            INVITE_CODE_02: ROLE_02,
            INVITE_CODE_03: ROLE_03,
            INVITE_CODE_04: ROLE_04,
            INVITE_CODE_05: ROLE_05,
            INVITE_CODE_06: ROLE_06,
        }
        role_name = role_map.get(used_invite.code)
        if role_name:
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                await member.add_roles(role)
                print(f'Assigned role {role.name} to {member}')
            else:
                print(f'Role "{role_name}" not found')
    else:
        print(f'No matching invite found for {member}')

bot.run(TOKEN)

