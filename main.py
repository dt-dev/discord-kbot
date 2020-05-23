#Library Import
import discord
from discord.ext import commands
from datetime import datetime

#Set Summoning Command
client = commands.Bot(command_prefix = 'k-')

#Get Date
now = datetime.now()
month = now.strftime("%m")

#Set permitted commands
commandDictionary = {
    "k-khelp": "Displays this menu",
    "k-ping": "Checks bot's latency/message delay",
    "k-month": "Shows Current Month's Comebacks"
}

#Create User Friendly Command Dictionary
dictionaryToString = ''
for x in commandDictionary:
    dictionaryToString += (("**"+x+"**").ljust(10) + "→" + commandDictionary[x]+"\n")

#Set Bot Commands and Events
@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def khelp(ctx):
    await ctx.send('Options:\n'+dictionaryToString)

@client.command()
async def month(ctx):
    await ctx.send('Comebacks for the month of ' + str(month) + ': ')

client.run('TOKEN PLACE HOLDER')