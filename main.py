import discord
import os
from discord.ext import commands
from datetime import datetime

#Get Dates
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

now = datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

#Set Summoning Command
client = commands.Bot(command_prefix='-k ')

#Set Permitted Commands
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
async def month(ctx):
    await ctx.send('Comebacks for the month of ' + str(MONTHS[month]) + ': ')

client.run(os.environ['TOKEN_PLACEHOLDER'])
