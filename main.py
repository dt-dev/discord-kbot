import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k-')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NzAzNDEyNjg1ODA2NTAxOTA4.Xsmpbg.bnq8QCFz6Z0OwsUHUKRizGhoSk8')