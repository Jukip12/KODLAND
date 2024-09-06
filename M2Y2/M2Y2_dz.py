import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

energy_economy = ("Экономия энергии: Выключай свет, когда выходишь из комнаты, используй энергосберегающие лампочки, отключай электроприборы от розетки, когда они не используются.")
water_economy = ("• Экономия воды: Принимай короткие души, не оставляй воду течь во время чистки зубов, используй посудомоечную машину только при полной загрузке.")
utilisation = ("• Правильная утилизация отходов: Разделяй мусор, используй перерабатываемые материалы, компостируй органические отходы.")
potreb = ("• Ограничение потребления: Покупай только то, что тебе действительно нужно, выбирай качественные вещи, чтобы они служили дольше.")
move = ("• Передвижение: Используй общественный транспорт, велосипед или ходьбу вместо машины, особенно на короткие расстояния.")

#блок 2
problem_1 = ('Изменение климата: повышение температуры, экстремальные погодные явления, повышение уровня моря и изменение характера осадков.')

problem_2 = ('Загрязнение воздуха: выбросы промышленных предприятий, автомобильные выхлопы, накопление радиоактивных, бытовых и промышленных отходов.')

problem_3 = ('Утрата биоразнообразия: вырубка лесов, разрушение мест обитания некоторых животных и растений.')

problem_4 = ('Нехватка воды: дефицит пресной воды.')

problem_5 = ('Загрязнение пластиком: чрезмерное использование пластика и неправильное обращение с отходами.')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')



@bot.command()
async def tips(ctx):
    await ctx.send(energy_economy)
    await ctx.send(water_economy)
    await ctx.send(utilisation)
    await ctx.send(potreb)
    await ctx.send(move)

@bot.command()
async def help_me(ctx): 
    await ctx.send("Перечень комманд которые может выполнять бот Vlad17:")
    await ctx.send("Обратите внимание что префикс данного бота $")
    await ctx.send("$hello - Если вы используете эту комманду, бот поприветсвует Вас")
    await ctx.send("$tips - Бот напишет наши базовые экологические советы, простые советы которые сильно помогут природе!")
    await ctx.send("$problem - Бот расскажет Вам о проблемах экологии которые существуют на данный момент")

@bot.command()
async def problem(ctx):
    await ctx.send(problem_1)
    await ctx.send(problem_2)
    await ctx.send(problem_3)
    await ctx.send(problem_4)
    await ctx.send(problem_5)


bot.run("")
