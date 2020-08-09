import discord
from discord.ext import commands


class Test(commands.Cog):
    """Test Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Test command"
        self.usage = "test"

    @commands.command(name='test')
    @commands.has_permissions()
    async def test(self, ctx):
        embed = discord.Embed(title=None, description=None, color=ctx.author.color)

        embed.set_author(name=f" | {(str(ctx.command.name)).capitalize()}", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Test(bot))
