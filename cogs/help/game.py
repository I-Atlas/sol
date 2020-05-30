# Imports
import discord
from discord.ext import commands


# Main Command Class
class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Shows what the user is playing."
        self.usage = "game [user]"

    @commands.command(name='game', aliases=['g'])
    @commands.has_permissions()
    async def game(self, ctx, member: discord.Member = None):
        await ctx.message.delete()  # delete your message
        user = ctx.message.author if (member is None) else member
        if user.activity:
            embed = discord.Embed(description=f'User {user.mention} plays **{user.activity}**', color=0xa9ffda)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'User {user.mention} doesn’t play anything**', color=0xa9ffda)
            await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Game(bot))
