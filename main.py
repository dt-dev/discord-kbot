import discord
import os
from discord.ext import commands
from datetime import datetime

#Get Dates
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

now = datetime.now()

currentYear = now.year
currentMonth = now.month
currentDay = now.day
currentHour = now.hour
currentMinute = now.minute

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
    await ctx.send('Comebacks for the month of ' + MONTHS[currentMonth-1] + ': ')

client.run(os.environ['TOKEN_PLACEHOLDER'])