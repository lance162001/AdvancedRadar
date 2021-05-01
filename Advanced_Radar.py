import discord
from discord.ext.commands import Bot
from discord import Intents

## for now we default with this
## in the future, put defaults in a config file that can be changed, so it can be configured in discord with commands and remember changes after restarts
categoryCount = 2
categories = [[],[]]
write = 837176317425745950
reads = [837176426435182644,837176452004577281]
inputName = 'Insight'
inputName = 'Ecnal'
admins = ["Ecnal","Ntel"]

intents = Intents.all()
TOKEN = 'ODM3ODY3MjY0MzU0MDI1NDgy.YIyysg.LjwG4jZI5qPAzs_ko0pZ6yvXq4o'
bot = Bot(intents=intents, command_prefix='?')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.playing, name = 'Zkill Stalking Online'))

@bot.listen('on_message')
async def receiver(message):
    if message.channel.id == write:
        return
    print(f"receiving message {message.content}")
    if message.author.display_name == inputName:
        print("and message is from the target\n")
        for i in range(categoryCount):
            if message.content in categories[i]:
                channel = bot.get_channel(write)
                await channel.send(message.content)
                for i in range(categoryCount):
                    if message.content in categories[i]:
                        categories[i].remove(message.content)
                break
            if reads[i] == message.channel.id:
                categories[i].append(message.content)
        
@bot.command(name='setup', help = 'Arguments: bot name, number of categories, write channel, read channels')
async def setup(ctx, name='Insight',categoryCount=2,write=None,*reads):
    if 'Strategic Command' in ctx.author.roles or ctx.author.name in admins:
        await context.send('currently broken, sorry')
        if name == 'Insight' and categoryCount == 2 and write == None:
            await context.send('you gave me all defaults or nothing at all!')
        else:
            if categoryCount <= 1:  
                await context.send('invalid categoryCount')

@bot.command(name='addadmin', help = "Arguments: username (not nickname) of user to add to admin list")
async def addadmin(ctx, name):
    pass
    

bot.run(TOKEN)
