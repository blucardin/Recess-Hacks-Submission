# bot.py
import math, Chemistry, typing
import random

import discord
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print('Dicerning has connected to Discord!')
    

@bot.command(name='test')
async def nine_nine(ctx):

    await ctx.send("testing, testing, testing")

bot.run(input("Token: "))