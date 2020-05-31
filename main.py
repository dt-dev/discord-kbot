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
try:
    ##Test Ping
    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    ##
    @client.command()
    async def month(*args):
        requestedMonth = ''
        for word in args:
            requestedMonth += word
            requestedMonth += ' '

        if requestedMonth in MONTHS:
            try:
                try:
                    int(requestedMonth)
                except TypeError:
                    requestedMonth = MONTHS.index(requestedMonth)
                except:
                    client.say("ERROR>>> Unknown Error, Please Contact the Developer")
            except:
                paragraphEmbed = discord.Embed(
                    title = str('Comebacks for the month of ' + MONTHS[int(requestedMonth)-1] + ': '),
                    description = kdata.paragraphString,
                    colour = discord.Color.default()
                )

            # paragraphEmbed.set_footer(text='This is a footer.')
            # paragraphEmbed.set_image(url='')
            # paragraphEmbed.set_thumbnail(url='')
            paragraphEmbed.set_author(name='dbkpop',icon_url='https://dbkpop.com/wp-content/uploads/2018/04/dbkpopheader.png')
            #paragraphEmbed.add_field()

            await client.say(embed=paragraphEmbed)

    ##Subscribe Feature
    @client.command()
    async def subscribe(*args):
        name = ''
        for word in args:
            name += word
            name += ' '
        if name in kdata.subcriptions.readline():
            await client.say('You are already subscribed to ' + name)
        else:
            if name in kdata.stageNameList or kdata.fullNameList:
                kdata.subcriptions.write(name+'\n')
                await client.say('You are now subscribed to ' + name)
            else:
                await client.say('Could not find '+ name +' please check spelling')
except:
    @client.event
    async def error():
        await client.say("**ERROR>>>** An error occurred, please contact the developer")

# @client.command()
# async def month(ctx):
#     #await ctx.send('Comebacks for the month of ' + MONTHS[currentMonth-1] + ': ')
#     ##Testing for June
#     await ctx.send('Comebacks for the month of June: ')
#     await ctx.send(kdata.paragraphString)
#     await ctx.send(kdata.table)

client.run(os.environ['TOKEN_PLACEHOLDER'])