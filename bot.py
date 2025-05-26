import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load from .env file if it exists
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))

INVITE_CODE_01 = os.getenv('INVITE_CODE_01')
ROLE_01 = os.getenv('ROLE_01')

INVITE_CODE_02 = os.getenv('INVITE_CODE_02')
ROLE_02 = os.getenv('ROLE_02')

INVITE_CODE_03 = os.getenv('INVITE_CODE_03')
ROLE_03 = os.getenv('ROLE_03')

INVITE_CODE_04 = os.getenv('INVITE_CODE_04')
ROLE_04 = os.getenv('ROLE_04')

INVITE_CODE_05 = os.getenv('INVITE_CODE_05')
ROLE_05 = os.getenv('ROLE_05')

INVITE_CODE_06 = os.getenv('INVITE_CODE_06')
ROLE_06 = os.getenv('ROLE_06')

intents = discord.Intents.default()
intents.members = True
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

intents = discord.Intents.default()
intents.members = True
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

intents = discord.Intents.default()
intents.members = True
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

