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
        colour=discord.Color.default()
    )
    await ctx.send(embed=helpEmbed)

try:
    ##Test Ping
    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    @client.command()
    async def month(ctx, *, requestedMonth):
        if requestedMonth == 1 or requestedMonth == MONTHS[0]:
            requestedMonth = 1
            kdata.response = kdata.january
        elif requestedMonth == 2 or requestedMonth == MONTHS[1]:
            requestedMonth = 2
            kdata.response = kdata.february
        elif requestedMonth == 3 or requestedMonth == MONTHS[2]:
            requestedMonth = 3
            kdata.response = kdata.march
        elif requestedMonth == 4 or requestedMonth == MONTHS[3]:
            requestedMonth = 4
            kdata.response = kdata.april
        elif requestedMonth == 5 or requestedMonth == MONTHS[4]:
            requestedMonth = 5
            kdata.response = kdata.may
        elif requestedMonth == 6 or requestedMonth == MONTHS[5]:
            requestedMonth = 6
            kdata.response = kdata.june
        elif requestedMonth == 7 or requestedMonth == MONTHS[6]:
            requestedMonth = 7
            kdata.response = kdata.july
        elif requestedMonth == 8 or requestedMonth == MONTHS[7]:
            requestedMonth = 8
            kdata.response = kdata.august
            await ctx.send("No August Comebacks Have Been Posted, Showing This Months Comebacks")
        elif requestedMonth == 9 or requestedMonth == MONTHS[8]:
            requestedMonth = 9
            kdata.response = kdata.september
            await ctx.send("No September Comebacks Have Been Posted, Showing This Months Comebacks")
        elif requestedMonth == 10 or requestedMonth == MONTHS[9]:
            requestedMonth = 10
            kdata.response = kdata.october
            await ctx.send("No October Comebacks Have Been Posted, Showing This Months Comebacks")
        elif requestedMonth == 11 or requestedMonth == MONTHS[10]:
            requestedMonth = 11
            kdata.response = kdata.november
            await ctx.send("No November Comebacks Have Been Posted, Showing This Months Comebacks")
        elif requestedMonth == 12 or requestedMonth == MONTHS[11]:
            requestedMonth = 12
            kdata.response = kdata.december
            await ctx.send("No December Comebacks Have Been Posted, Showing This Months Comebacks")
        paragraphEmbed = discord.Embed(
            title=str('Comebacks for the month of ' + MONTHS[int(requestedMonth) - 1] + ': '),
            description=kdata.paragraphString,
            colour=discord.Color.default()
        )

        # paragraphEmbed.set_footer(text='This is a footer.')
        # paragraphEmbed.set_image(url='')
        # paragraphEmbed.set_thumbnail(url='')
        paragraphEmbed.set_author(name='dbkpop',
                                  icon_url='https://dbkpop.com/wp-content/uploads/2018/04/dbkpopheader.png')
        # paragraphEmbed.add_field()

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