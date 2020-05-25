#Library Import
import discord
import os
from data import *
from discord.ext import commands

#Set Summoning Command
client = commands.Bot(command_prefix = '-k ')

#Set permitted commands
commandDictionary = {
    "k-ping": "Checks bot's latency/message delay",
    "k-month": "Shows Current Month's Comebacks"
}

#Set Bot Commands and Events
@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def khelp(ctx):
    await ctx.send('Options:\n'+dictionaryToString)

@client.command()
async def month(ctx):
    await ctx.send('Comebacks for the month of ' + str(month) + ': ')

client.run(os.environ['TOKEN_PLACEHOLDER'])
