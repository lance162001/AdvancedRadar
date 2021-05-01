import discord
from discord.ext.commands import Bot
from discord import Intents

configFile = open('config.txt','r')
config = configFile.read().split("\n")
for i in range(len(config)):
    config[i] = config[i].split(":")[1]
categoryCount = 2
categories = [[],[]]
adminRole = config[5]
write = int(config[4])
reads = config[3].split(",")
for i in range(len(reads)):
    reads[i] = int(reads[i])
inputName = config[2]
admins = config[1].split(",")
intents = Intents.all()
TOKEN = config[0]
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
            if message.content in categories[i] and reads[i] != message.channel.id:
                channel = bot.get_channel(write)
                await channel.send(message.content)
                for i in range(categoryCount):
                    if message.content in categories[i]:
                        categories[i].remove(message.content)
                break
            if reads[i] == message.channel.id:
                categories[i].append(message.content)
                
bot.run(TOKEN)
