import discord
from discord.ext import commands

# Define intents (permissions) for the bot
intents = discord.Intents.default()
intents.members = True  # This enables member-related events, like joining

# Set up the bot with prefix '!' and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    # Find the "general" channel or replace with your welcome channel name
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f'Eda Mownea.....Welcome to Mallu Programmers....., {member.mention}!')

# Run the bot with token
bot.run('MTMwMTQ3MDY0NDcxMzgxNjA4Ng.G0MMy1.J899qpN4LDmneUnV6sUEgYJ-SmWCke5bAqSckc')
