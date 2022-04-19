#libs
import nextcord
from nextcord.ext import commands
import config

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self, ctx, member : nextcord.Member=None, *, reason=None):
        if config.ban == True:
            if member is None:
                await ctx.send("Please mention a member. usage: !ban <@meber> <reason>")
                if reason is None:
                    await ctx.send("Please specify a reason. usage: !ban <@meber> <reason>")
            elif reason is None:
                await ctx.send("Please specify a reason. usage: !ban <@meber> <reason>")
                if member is None:
                    await ctx.send("Please mention a member. usage: !ban <@meber> <reason>")
            else:
                await ctx.send(f"User {member.mention} has been banned for the reason: {reason}")
                await member.send(f"You Have Been banned From {ctx.guild.name} by the staff member {ctx.author.mention} for the reason: {reason}")
                await member.ban(reason=reason)
        else:
            await ctx.send("banning is turned off, ask the bot owner (buzE) to turn banning on sir!")
            

def setup(bot):
    bot.add_cog(ban(bot))