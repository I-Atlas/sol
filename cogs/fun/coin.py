import random
from discord.ext import commands
from ..events.utils import Utils


class Coin(commands.Cog):
    """Coin Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Flips a coin."
        self.usage = "coin"

    @commands.command(name='coin')
    @commands.has_permissions()
    async def coin(self, ctx):
        embed = await Utils(self.bot).embed(ctx, title="Try to toss the coin, heads or tails, you know."
                                            f"\n\nThat leaves you with a ``{random.choice(['heads', 'tails'])}``!",
                                            description="", color=ctx.author.color)
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Coin(bot))