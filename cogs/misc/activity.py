import discord
from discord.ext import commands


class Activity(commands.Cog):
    """Game Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Shows user's activity"
        self.usage = "activity [user]"

    @commands.command(name='activity', aliases=['act'])
    @commands.has_permissions()
    async def activity(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        user = ctx.message.author if (member is None) else member
        if user.activity:
            embed = discord.Embed(description=f'User`s {user.mention} activity: **{user.activity}**', color=0xa9ffda)

            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'User {user.mention} has no activity**', color=0xa9ffda)

            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Activity(bot))
