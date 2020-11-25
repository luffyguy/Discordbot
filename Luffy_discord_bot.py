import discord 
import random
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


from discord.ext import commands

#used prefix
client = commands.Bot(command_prefix=".")

#tells us when bot is active
@client.event
async def on_ready():
    
    await client.change_presence(status=discord.Status.online,activity=discord.Game(" with Luffyguy"))
    #set status of bot

    print("Bot is ready")

#says hi
@client.command()
async def hello(ctx):
    await ctx.send("Hi")

#just laughs
@client.command()
async def laugh(ctx):
    await ctx.send("Ha Ha Ha.....")    

#responds randomly
@client.command()
async def lol(ctx): 
    responces = [
        "Was it that funny?",
        "Noob Alert!",
        "Watch your tone dude!",
        "You are that dumb Lmao",
        "No comments",
        "You are such a kid dude",
    ]
    await ctx.send(random.choice(responces))

#square of a number
@client.command()
async def square(ctx,number):
    squared_number = int(number) ** 2
    await ctx.send("The square of " + str(number) + " is " + str(squared_number))
 
#cube of a number 
@client.command()
async def cube(ctx,number1):
    cubed_number = int(number1) ** 3
    await ctx.send("The cube of " + str(number1) + " is " + str(cubed_number))

#adds 2 numbers
@client.command()
async def add(ctx,number1,number2):
    summed_number = int(number1) + int(number2)
    await ctx.send("The sum of " + str(number1) + " and " + str(number2) + " is " + str(summed_number))

#subtracts 2 numbers
@client.command()
async def diff(ctx,number1,number2):
    subtracted_number = int(number1) - int(number2)
    await ctx.send("The differnce of " + str(number1) + " and " + str(number2) + " is " + str(subtracted_number))

#to clear chat
@client.command()
async def clear(ctx,amount=1):#algorithm channel id          #project channel id
    if ctx.channel.id != 778499893249310730 and ctx.channel.id !=778225956971347988: 
        await ctx.channel.purge(limit=amount+1)   


#put your token here
client.run(TOKEN)