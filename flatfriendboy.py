import discord
from discord.ext import commands
import datetime
import aiocron
import random
import re
import secret_santa 

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
            # flat friend protest over, uncomment below
            await message.channel.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')
            # flat friend protest not over, uncomment below
            # await message.channel.send('https://twitter.com/gatorsafterdark/status/1423646602691072000?s=20')
        elif today in [0,1,2,3]:
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        elif today in [5,6]:
            await message.channel.send('https://twitter.com/CraigWeekend/status/1393340094602366976?s=20')

    match = whatdays.search(message.content)
    if message.content.startswith('.cornjob'):
        await message.channel.send('https://www.youtube.com/watch?v=ISiGiYfahS0')


    if message.content.startswith('good bot') or message.content.startswith('Good bot'):
        # print(message.author)
        value = random.randrange(1, 100)
        print("the value for good bot is: " + str(value))
        authorObj = message.author
       
        if value%2==0:
            await authorObj.send('011101000110100001100001011011100110101100100000011110010110111101110101, which is my way of saything "thank you"')
        elif value == 69:
            await message.channel.send(authorObj.mention + ' ROLLED A 69!!! NICEEEEEEE.')
        else:
            await message.channel.send("I've seen your Google history," + authorObj.mention + ", you better call me a good bot" )

    if message.content.startswith('hail satan'):
        #1 load excel data in /data folder with pandas? 
        #2 randomly match users (gift_giver, gift_receiver)
           # A) this may be tricky...be deliberate and may make this a function
        #3 
         
        mention_object_list = message.mentions
        user_list = []

        for user_obj in mention_object_list :
            user_list.append(user_obj.name)
        print(user_list)

        results = secret_santa.secret_santa(user_list)
        secret_santa.save_results(results)

        # for user_obj in mention_object_list:
        df =secret_santa.load_excel_pandas()
        for user_obj in mention_object_list:
            gift_giver = user_obj.name
            for pair in results:
                if pair[0] == gift_giver:
                    gift_receiver = pair[1]
                    message = secret_santa.create_gift_receiver_message(gift_receiver, df)
                    print(gift_giver)
                    print(gift_receiver)
                    print(message)

                    if gift_giver == 'EpicureanHeron':
                        await user_obj.send(message)
              #  user_obj will be the gift_giver, so, look up from the results list who is associated with with them probably using a name match in the list 
              # look up info from pandas based on name of gift_receiver
              # format string (do not use the f string formatting) with relevant information
              # message the gift_give with the details (this will be important )
              


        #     await user.send('test')


@aiocron.crontab('0 4 * * FRI')
# @aiocron.crontab('* * * * *')
async def cronjob1():
    CHANNEL_ID = open("channel.txt","r").readline()
    # CHANNEL_ID = open("channel_test.txt","r").readline()
    channel = client.get_channel(int(CHANNEL_ID))
    print('success')
    # after protest
    await channel.send('https://www.youtube.com/watch?v=A5U8ypHq3BU')
    # await channel.send('https://twitter.com/gatorsafterdark/status/1423646602691072000?s=20')
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
    print(value)
    if value%4 == 0:
        print('posting!')
      
        await channel.send('https://tenor.com/view/drugs-dope-high-trippy-gif-4808633')

client.run(TOKEN)