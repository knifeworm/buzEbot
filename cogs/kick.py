#libs
import nextcord
from nextcord.ext import commands
import config

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : nextcord.Member=None, *, reason=None):
        if config.kick == True:
            if member is None:
                await ctx.send("Please mention a member. usage: !kick <@meber> <reason>")
                if reason is None:
                    await ctx.send("Please specify a reason. usage: !kick <@meber> <reason>")
            elif reason is None:
                await ctx.send("Please specify a reason. usage: !kick <@meber> <reason>")
            else:
                await ctx.send(f"User {member.mention} has been kicked for the reason: {reason}")
                await member.send(f"You Have Been Kicked From {ctx.guild.name} by the staff member {ctx.author.mention} for the reason: {reason}")
                await member.kick(reason=reason)
        else:
            await ctx.send("Kicking is turned off, ask the bot owner (buzE) to turn kicking on sir!")
            

def setup(bot):
    bot.add_cog(kick(bot))