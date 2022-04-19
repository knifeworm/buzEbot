#libs
import nextcord
from nextcord.ext import commands
import config
import datetime
import humanfriendly

class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #mute
    @commands.command()
    async def mute(self, ctx, member : nextcord.Member, time, *, reason):
        if config.mute == True:
            if member is None:
                await ctx.send("You Must Specify A member to mute!. usage: !mute <member> <time> <reason>")
                if reason is None:
                    await ctx.send("You Must Specify A reason to mute!. usage: !mute <member> <time> <reason>")
            elif reason is None:
                await ctx.send("You Must Specify A reason to mute!. usage: !mute <member> <time> <reason>")
            else:
                print(f"\n[debug] mute command used [by: {ctx.author.mention}, member: {member}, time: {time}, reason: {reason}]")
                time = humanfriendly.parse_timespan(time)
                await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
                await ctx.send(f"muted {member.mention} for the reason: {reason} with the time of: {time}")
                await member.send(f"You Have been muted by staff member: {ctx.author.mention} for the reason: {reason} with the time of {time}")

    #unmute
    @commands.command()
    async def unmute(self, ctx, member : nextcord.Member, *, reason):
        if config.unmute == True:
            if member is None:
                await ctx.send("You Must Specify A Member to unmute!. usage: !unmute <member> <reason>")
                if reason is None:
                    await ctx.send("You Must Specify A reason to unmute!. usage: !unmute <member> <reason>")
            elif reason is None:
                await ctx.send("You Must Specify A reason to unmute!. usage: !unmute <member> <reason>")
            else:
                await member.edit(timeout=None)
                await ctx.send(f"unmuted {member.mention} for the reason: {reason}")
                print(f"\n[debug] unmute command used [by: {ctx.author.mention}, member: {member}, reason: {reason}]")
            
#setup functions
def setup(bot):
    bot.add_cog(mute(bot))