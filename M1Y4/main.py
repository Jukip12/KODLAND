import discord
from discord.ext import commands
from random_number import randnum  

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









bot.run("")