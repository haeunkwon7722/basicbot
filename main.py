import discord
import asyncio
from discord.ext import commands

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Game('I am testing'))
    print(str(len(bot.guilds)))
    print('Hello World!')
    
@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)  #The bot won't respond the message that the bot send.
    
@bot.command()
async def dice(ctx):
    import random
    dice = random.randint(1, 6)
    await ctx.channel.send(dice)
    
bot.run('Your Token')
