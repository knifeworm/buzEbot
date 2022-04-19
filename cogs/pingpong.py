#libs
import nextcord
from nextcord.ext import commands
import config

class pingpong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx, echomessage=None):
        if config.pong == True:
            await ctx.send("pong")
    
    @commands.command()
    async def pong(self, ctx, echomessage=None):
        if config.ping == True:
            await ctx.send("ping")
            

def setup(bot):
    bot.add_cog(pingpong(bot))