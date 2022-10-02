from discord.ext import commands
import discord
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print('Ready !')
@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    message_content = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {message_content} ({channel})')

    if message.author == bot.user:
        return
   
    end_mess = message_content.endswith
    if end_mess('quoi') or end_mess('quoi?')or end_mess('Quoi?')or end_mess('quoi ?')or end_mess('Quoi ?')or end_mess('Quoiii')or end_mess('quoiii'):
        await message.channel.send('feur')
        return

@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    message_content = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {message_content} ({channel})')

    if message.author == bot.user:
        return
   
    end_mess = message_content.endswith
    if end_mess('qui joue') or end_mess('qui joue ?')or end_mess('Qui joue ?'):
        await message.channel.send("t'a pas d'amis connard")
        return
bot.run('MTAyNjExMTgzMjM5NTYxMjIwMA.GB82Ab.UGjSCNdzPQYPGgnoXKRuqmWSi-IWMdN55PWBc4')
