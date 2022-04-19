#libs
import nextcord
from nextcord.ext import commands
import config

class echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, echomessage=None):
        if config.echo == True:
            if echomessage is None:
                await ctx.send(f"You Need To Specify A Message for me to echo!")
            else:
                await ctx.send(f"You Said: {echomessage}")

def setup(bot):
    bot.add_cog(echo(bot))