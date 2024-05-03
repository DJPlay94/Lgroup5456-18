import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

foo = ['уменьшить выброс в атмосферу парниковых газов', 
       'в котельных, на заводах и фабриках установить сооружения для очистки выбрасов в атмосферу', 
       'отказаться от природных видов топлива в пользу более экологически чистых', 
       'уменьшить объём вырубки лесов и обеспечить их воспроизводство', 
       'широкое использование экологических технологий']

@bot.command()
async def ФАКТ(ctx):
    await ctx.send(random.choice(foo))


bot.run("")