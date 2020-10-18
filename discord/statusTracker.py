import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='add', help='Add a new status to be tracked')
async def roll(ctx, status_name, status):
    print(ctx.author.id)
    if status == "t":
        await ctx.send("<@{}>".format(ctx.author.id)+" has taken "+status_name)
    elif status == "f":
        await ctx.send("<@{}>".format(ctx.author.id) + " has stopped using " + status_name)

bot.run(TOKEN)
