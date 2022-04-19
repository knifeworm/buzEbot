# Author: buzE
#
# buzEbot

#imports librarys/api-s
from grpc import Channel
import nextcord
from nextcord.ext import commands
import config
import os
import asyncio

#bot definitions (global bot realted variables)
bot = commands.Bot(command_prefix = "!")
    
#onready (when the bot starts up/gets online)
@bot.event
async def on_ready():
    print(f"\n[+] buzzEbot is now online and working! (credits go to {config.AUTHOR} and ILikeFivem)")

#create command load (loads the specific cog)
@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    #loads the cog specified in the message.
    bot.load_extension(f'cogs.{extension}')
    #sends message to channel command was executed in. 'Load cog {cog}'
    await ctx.send(f'[*] Loaded Cog {extension}')

#load all cogs / other files
for filename in os.listdir('./cogs/'):
    #checks to see if the cog's filename ends with .py (if its a python file) and then loads it
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"[*] Loaded Cog: {filename[:-3]}")
    
    #outputs and error if the cog cant be loaded
    else:
        if not filename.endswith('.py'):
            print(f"[*] Invalid cogfile: {filename}. This is likely not an error, just information!")
        else:
            print(f"[*] Failed To Load Cog: {filename[:-3]}, Some Commands/Functions May Not Work Properly")

#auto moderation (deletes blacklisted messages)
@bot.event
async def on_message(message):
    for word in config.filter_words:
        if word in str.lower(message.content):
            await message.delete()
            await message.channel.send(f"mensaje inapropiado {message.author.mention}!")
    await bot.process_commands(message)

#login to buzEbot
bot.run(config.TOKEN)
# drag discord over