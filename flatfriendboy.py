import discord
from discord.ext import commands
import datetime
import aiocron

# will not play unless it is friday
# instead rickrolls
# auto posts flat friend friday
 
CHANNEL_ID = open("channel.txt","r").readline()
 
TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '.')#answers with the ms latency
@client.command()
async def whatday(ctx):
    today = datetime.datetime.today().weekday()
    if today ==4:
        await ctx.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')
    else:
        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@aiocron.crontab('0 4 * * FRI')
# @aiocron.crontab('* * * * *')
async def cornjob1():
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


client.run(TOKEN)