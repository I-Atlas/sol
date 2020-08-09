import random
from discord.ext import commands
from ..events.utils import Utils


class Color(commands.Cog):
    """Color Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Creates a random rgb color"
        self.usage = "color"

    @commands.command(name='color', aliases=['rc'])
    @commands.has_permissions()
    async def color(self, ctx):
        color = (random.randint(0, 16777215))
        embed = await Utils(self.bot).embed(ctx, title="Color generated!", description=f"``#{hex(color)[2:]}``",
                                            color=color)
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Color(bot))
