import discord
from discord.ext import commands
import datetime
import aiocron
import random
import re

# will not play unless it is friday
# instead rickrolls
# auto posts flat friend friday
 
CHANNEL_ID = open("channel.txt","r").readline()
 
TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_message(message):
    whatdays = re.compile(r'(^what*([\w ]+)day$)', re.I)

    match = whatdays.search(message.content)
        # message.channel.send
    # if message.author.bot == False:
    #     print('https://www.youtube.com/watch?v=ISiGiYfahS0')
    if match:
        today = datetime.datetime.today().weekday()
        if today ==4:
            await message.channel.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')
        else:
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    if message.content.startswith('.cornjob'):
        await message.channel.send('https://www.youtube.com/watch?v=ISiGiYfahS0')

# @client.command()   
# async def cornjob(ctx):
    
#     await ctx.send('https://www.youtube.com/watch?v=ISiGiYfahS0')
   

@aiocron.crontab('0 4 * * FRI')
# @aiocron.crontab('* * * * *')
async def cronjob1():
    CHANNEL_ID = open("channel.txt","r").readline()
    # CHANNEL_ID = open("channel_test.txt","r").readline()
    channel = client.get_channel(int(CHANNEL_ID))
    print('success')

    await channel.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')

@aiocron.crontab('30 16 * * FRI')
async def cronjob2():
    CHANNEL_ID = open("channel.txt","r").readline()
    # CHANNEL_ID = open("channel_test.txt","r").readline()
    channel = client.get_channel(int(CHANNEL_ID))
    await channel.send('https://twitter.com/CraigWeekend/status/1393340094602366976?s=20')

@aiocron.crontab('00 8 * * MON')
async def cronjob3():
    CHANNEL_ID = open("channel.txt","r").readline()
    # CHANNEL_ID = open("channel_test.txt","r").readline()
    channel = client.get_channel(int(CHANNEL_ID))

    await channel.send('https://tenor.com/view/impastor-kicked-nuts-kickedinthe-kickedinthenuts-gif-19303039')


@aiocron.crontab('20 16 * * *')
async def cronjob4():
    CHANNEL_ID = open("channel.txt","r").readline()
    # CHANNEL_ID = open("channel_test.txt","r").readline()
    channel = client.get_channel(int(CHANNEL_ID))
    value = random.randrange(1, 100)
    if value%4 == 0:
        print('yup')
        # https://stackoverflow.com/questions/54992629/how-to-save-display-giphy-gif-using-python-api

    await channel.send('https://tenor.com/view/impastor-kicked-nuts-kickedinthe-kickedinthenuts-gif-19303039')

client.run(TOKEN)