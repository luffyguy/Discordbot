import discord 
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

client.run("NzgxMTA5ODU1OTkyODA3NDI0.X743PQ.wVIAAKVgrENu2iHVZV5ITg_-Wtw")