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
    if today == 2:
        await ctx.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')
    else:
        await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

# @aiocron.crontab('0 4 * * THU')
@aiocron.crontab('* * * * *')
async def cornjob1():
    CHANNEL_ID = open("channel.txt","r").readline()
    channel = client.get_channel(int(CHANNEL_ID))
    print('success')

    await channel.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')


client.run(TOKEN)