import importlib
import discord
import os
from discord.ext import commands
from datetime import datetime
import kdata

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

#Set Bot Commands and Events
@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def month(ctx):
    paragraphEmbed = discord.Embed(
        title = str('Comebacks for the month of ' + MONTHS[currentMonth-1] + ': '),
        description = kdata.paragraphString,
        colour = discord.colour.white()
    )

    # paragraphEmbed.set_footer(text='This is a footer.')
    # paragraphEmbed.set_image(url='')
    # paragraphEmbed.set_thumbnail(url='')
    paragraphEmbed.set_author(name='dbkpop',icon_url='https://dbkpop.com/wp-content/uploads/2018/04/dbkpopheader.png')
    #paragraphEmbed.add_field()

    await client.say(embed=paragraphEmbed)

# @client.command()
# async def month(ctx):
#     #await ctx.send('Comebacks for the month of ' + MONTHS[currentMonth-1] + ': ')
#     ##Testing for June
#     await ctx.send('Comebacks for the month of June: ')
#     await ctx.send(kdata.paragraphString)
#     await ctx.send(kdata.table)

client.run(os.environ['TOKEN_PLACEHOLDER'])