import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description=None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name='nothing/prefix .'))






token = os.environ.get('DISCORD_TOKEN')
bot.run(qZh4QwBxtAL_z-nF8LT-RZ7kSKa29gw0)
