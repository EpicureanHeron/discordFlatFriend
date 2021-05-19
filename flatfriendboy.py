import discord
from discord.ext import commands

# will not play unless it is friday
# instead rickrolls
# auto posts flat friend friday
 
 
TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '.')#answers with the ms latency
@client.command()
async def flatfriend(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=A5U8ypHq3BU')
 
client.run(TOKEN)