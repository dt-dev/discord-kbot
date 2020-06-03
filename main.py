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
client.remove_command('help')

#Set Bot Commands and Events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('-k help'))
    print('Bot is ready!')

#Make new help command
@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(
        title="K-Bot Help Menu: ",
        description="""
        -k help                             Shows this help menu
        -k month <month name or number>     Shows comebacks for month specified
        -k subscribe <artist name>          Subscribes you for notifications on a groups comeback
        """,
        colour=discord.Color.purple()
    )
    await ctx.send(embed=helpEmbed)

try:
    ##Test Ping
    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    @client.command()
    async def month(ctx, requestedMonth):
        found = 0

        kdata.getMonth(requestedMonth)
        paragraphEmbed = discord.Embed(
            title=str('Comebacks for the month of ' + kdata.returnedMonth + ': '),
            description=kdata.paragraphString,
            colour=discord.Color.purple()
        )

        # paragraphEmbed.set_footer(text='This is a footer.')
        # paragraphEmbed.set_image(url='')
        # paragraphEmbed.set_thumbnail(url='')
        paragraphEmbed.set_author(name='dbkpop',
                                  icon_url='https://dbkpop.com/wp-content/uploads/2018/04/dbkpopheader.png')
        # paragraphEmbed.add_field()
        if not kdata.found:
            await ctx.send("Could Not Find " + requestedMonth + " showing comebacks for the current month: ")
        await ctx.send(embed=paragraphEmbed)

    ##Subscribe Feature
    @client.command()
    async def subscribe(ctx, *args):
        name = ''
        for word in args:
            name += word
            name += ' '
        if name in kdata.subcriptions.readline():
            await ctx.send('You are already subscribed to ' + name)
        else:
            if name in kdata.stageNameList or kdata.fullNameList:
                kdata.subcriptions.write(name+'\n')
                await ctx.send('You are now subscribed to ' + name)
            else:
                await ctx.send('Could not find '+ name +' please check spelling')
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