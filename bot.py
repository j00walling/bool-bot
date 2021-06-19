import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import time
import os

# Bot Link
# https://discord.com/api/oauth2/authorize?client_id=855685328558751744&permissions=8&scope=bot

client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print('We in')

@client.command()
async def jun(ctx):
    await ctx.send('Gay')

@client.command(pass_context = True)
async def bruh(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Bruh Sound Effect #2.mp3')
        voice.play(source)
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Join a voice channel first...nimrod")

@client.command(pass_context = True)
async def twang(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('bool_down_young_loud_1.wav')
        player = voice.play(source)
        time.sleep(5)
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("Join a voice channel first...nimrod")

client.run(os.environ['DISCORD_TOKEN'])

