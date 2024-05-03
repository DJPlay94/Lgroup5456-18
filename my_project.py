import discord, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.command
async def help_info(ctx):
    await ctx.send('комманды для бота: 1)!first_question =  какие климотовые проблемы есть в мире;2)!second_question = из-за чего происходят проблемы с климотом;3)!third_question = что надо сделать что-бы мы смогли побороть эти проблемы; 4)!fourth_question = в каких странах по большей части нарушен климат; 5)!fiveth_question = почему эти проблем влияют на окружающую среду')

@bot.command()
async def first_question(ctx):
    with open('images/1).png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

    await ctx.send('https://dneper.github.io/site_for_final_project_1/')    

@bot.command()
async def second_question(ctx):
    with open('images/2).jpg','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

    await ctx.send('https://dneper.github.io/site_for_final_project_2/')

@bot.command()
async def third_question(ctx):
    with open('images/3).jpg','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

    await ctx.send('https://dneper.github.io/site_for_final_project_3/')

@bot.command()
async def fourth_question(ctx):
    with open('images/4).jpg','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

    await ctx.send('https://dneper.github.io/site_for_final_project_4/')

@bot.command()
async def fiveth_question(ctx):
    with open('images/5).jpg','rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

    await ctx.send('https://dneper.github.io/site_for_final_project_5/')

bot.run('')