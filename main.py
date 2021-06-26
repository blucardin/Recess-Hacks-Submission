# bot.py
import Math, Chemistry, Typing
from discord.ext import commands

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print('Dicerning has connected to Discord!')
    
    

@bot.command(name='test', help = "Meant for testing, should returen \"testing, testing, testing\" ")
async def test(ctx):

    await ctx.send("testing, testing, testing")

Chemistry.run(bot)
Math.run(bot)
Typing.run(bot)

bot.run(input("Token: "))
