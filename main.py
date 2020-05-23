import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k-')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run('TOKEN PLACEHOLDER')