import random
import discord
from discord.ext import commands
from random_number import randnum  
import os
import requests

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 50):
    await ctx.send("he" * count_heh)

@bot.command()
async def random(ctx, max = 10): 
    await ctx.send("Случайное число от 1 до 10:")
    await ctx.send(randnum(max))


@bot.command()
async def help_me(ctx): 
    await ctx.send("Перечень комманд которые может выполнять бот Vlad17:")
    await ctx.send("Обратите внимание что префикс данного бота $")
    await ctx.send("$hello - Если вы используете эту комманду, бот поприветсвует Вас")
    await ctx.send("$heh - Бот скажет Вам 50 раз heh")
    await ctx.send("$random - Бот напишет в чате случайное число от 1 до 10")

@bot.command()
async def sigma(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


@bot.command('duck')
async def duck(ctx):
    #По команде duck вызывает функцию get_duck_image_url
    image_url = get_duck_image_url()
    await ctx.send(image_url)






bot.run("")