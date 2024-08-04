import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command('info')
async def cmd_info(ctx: commands.Context):
    name = ctx.author.global_name
    text = f'Привет, {name}! Я бот, который помогает в борьбе с экологическими проблемами.😎 Я напомню тебе, что нужно делать для защиты нашей планеты!'
    await ctx.send(text)




@bot.command('helper')
async def cmd_helper(ctx: commands.Context):
    embed = discord.Embed(
        title = 'Какие команды у меня есть?🙃',
        color=discord.Colour.from_rgb(69, 255, 0)
    )

    embed.add_field(
        name = '1 команда',
        value='!info - Бот рассказывает о чём он'
    )

    embed.add_field(
        name = '2 команда',
        value='!memo - Простая и понятная напоминалка о том как нужно заботиться о природе!'
    )

    await ctx.send(embed=embed)


@bot.command('memo')
async def cmd_memo(ctx: commands.Context):
    embed = discord.Embed(
        title = 'Как спасти нашу планету? 🤨 ',
        description='Проблема экологии сейчас очень актуальна, мы должны постараться сохранить нашу планету 🤓',
        color=discord.Colour.from_rgb(244, 11, 33)
    )

    embed.add_field(
        name = '1 правило',
        value='**Сортируйте мусорные отходы.** Это поможет уменьшить загрязнение водоёмов и других природных зон.🏞️'
    )

    embed.add_field(
        name = '2 правило',
        value='**Меньше пользуйтесь машинами.** Ходите пешком или используйте экологичный транспорт. 🚗'
    )

    embed.add_field(
        name = '3 правило',
        value='**Защищайте животных.** Берегите наших маленьких друзей. 🦝'
    )
    await ctx.send(embed=embed)




@bot.command('test')
async def cmd_test(ctx: commands.Context):
    text = "Бла **бла бла** Бла __бла бла__ Бла --бла бла-- бла ~~бла бла~~ "
    await ctx.send(text)



bot.run('')
