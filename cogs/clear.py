#clear command
#
#Author: buzzE

#libs
import nextcord
from nextcord.ext import commands
import config
import time

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, number : int=None):
        if config.clear == True:
            #see if number has been defined
            if number is None and number is not int:
                await ctx.send(f"You Must state the ammount of messages that you want to clear in an integer (single number without a decimal)!")
            else:
                if number > config.clearlimit:
                    await ctx.send(f"The Limit of messages you can clear is is {config.clearlimit}! clear a lower ammount!")
                else:
                    await ctx.send(f"Clearing {number} messages!")
                    time.sleep(0.5)
                    await ctx.channel.purge(limit=number+1)
                    await ctx.send(f"{number} Messages Have Been Cleared!")
                    time.sleep(0.4)
                    await ctx.channel.purge(limit=1)

def setup(bot):
    bot.add_cog(clear(bot))