import os
from flask import Flask
import discord
from discord.ext import commands

app = Flask(__name__)


TOKEN = os.getenv('MTMwMTQ3MDY0NDcxMzgxNjA4Ng.G0MMy1.J899qpN4LDmneUnV6sUEgYJ-SmWCke5bAqSckc')
bot = commands.Bot(command_prefix='!')

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/ping', methods=['GET'])
def ping():
    return "Pong!"

# Start the bot in a separate thread
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
if __name__ == '__main__':
    bot.loop.create_task(bot.start(TOKEN))
    app.run(host='0.0.0.0', port=5000)
