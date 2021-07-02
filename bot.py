from discord.ext import commands
from discord import FFmpegPCMAudio
import time
import os
import random
# import json
import sys

# Bot Link
# https://discord.com/api/oauth2/authorize?client_id=855685328558751744&permissions=8&scope=bot

# f = open('config.json', "r")
# config = json.loads(f.read())
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print('We in')

@client.command()
async def jun(ctx):
    await ctx.send('Beautiful')

@client.command(pass_context = True)
async def bruh(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('bruh.mp3')
        voice.play(source)
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Join a voice channel first")

@client.command(pass_context = True)
async def twang(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('bool_down_young_loud_1.wav')
        voice.play(source)
        time.sleep(5)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Join a voice channel first")

@client.command(pass_context = True)
async def fard(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('fard1.mp3')
        voice.play(source)
        time.sleep(0.5)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Join a voice channel first")

@client.command(pass_context = True)
async def bruno(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('bruno.m4a')
        voice.play(source)
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Join a voice channel first")

client.run(os.environ['DISCORD_TOKEN'])
# client.run(config['token'])

