import importlib
import discord
import os
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
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
        found = False

        current = requests.get('https://dbkpop.com/2020/04/20/june-2020-k-pop-comebacks-and-debuts')

        response = ''

        if month == 1 or month == MONTHS[0]:
            response = requests.get('https://dbkpop.com/2019/12/02/january-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[0]
        elif month == 2 or month == MONTHS[1]:
            response = requests.get('https://dbkpop.com/2019/12/26/february-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[1]
        elif month == 3 or month == MONTHS[2]:
            response = requests.get('https://dbkpop.com/2020/01/23/march-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[2]
        elif month == 4 or month == MONTHS[3]:
            response = requests.get('https://dbkpop.com/2020/02/04/april-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[3]
        elif month == 5 or month == MONTHS[4]:
            response = requests.get('https://dbkpop.com/2020/04/03/may-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[4]
        elif month == 6 or month == MONTHS[5]:
            response = requests.get('https://dbkpop.com/2020/04/20/june-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[5]
        elif month == 7 or month == MONTHS[6]:
            response = requests.get('https://dbkpop.com/2020/05/11/july-2020-k-pop-comebacks-and-debuts')
            found = True
            returnedMonth = MONTHS[6]
        elif month == 8 or month == MONTHS[7]:
            response = current
            found = False
            returnedMonth = MONTHS[7]
        elif month == 9 or month == MONTHS[8]:
            response = current
            found = False
            returnedMonth = MONTHS[8]
        elif month == 10 or month == MONTHS[9]:
            response = current
            found = False
            returnedMonth = MONTHS[9]
        elif month == 11 or month == MONTHS[10]:
            response = current
            found = False
            returnedMonth = MONTHS[10]
        elif month == 12 or month == MONTHS[11]:
            response = current
            found = False
            returnedMonth = MONTHS[11]

        soup = BeautifulSoup(response.text, 'html.parser')

        posts = soup.find_all(class_='site-main')

        for post in posts:
            title = post.find(class_='entry-title').get_text()
            body = post.find(class_='entry-content clear')
            table = str(post.find(id='table_1'))
            # print(title)
            # print(body)
            # print(table)
        paragraphs = body.find_all('p')
        # Convert List of Elements to List of Text Only
        n = 0
        paragraphList = []
        paragraphString = ''
        for n in range(len(paragraphs)):
            paragraphList.append(paragraphs[n].get_text() + '\n\n')
            n += 1
        for n in range(len(paragraphList)):
            paragraphString += paragraphList[n]

        paragraphEmbed = discord.Embed(
            title=str('Comebacks for the month of ' + returnedMonth + ': '),
            description=paragraphString,
            colour=discord.Color.purple()
        )

        # paragraphEmbed.set_footer(text='This is a footer.')
        # paragraphEmbed.set_image(url='')
        # paragraphEmbed.set_thumbnail(url='')
        paragraphEmbed.set_author(name='dbkpop',
                                  icon_url='https://dbkpop.com/wp-content/uploads/2018/04/dbkpopheader.png')
        # paragraphEmbed.add_field()
        if not found:
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