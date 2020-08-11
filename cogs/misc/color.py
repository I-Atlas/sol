import random
import discord
from discord.ext import commands
from ..events.utils import Utils


class Color(commands.Cog):
    """Color Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour(random.randint(0, 0xFFFFFF))
        self.desc = "Creates a random rgb color"
        self.usage = "color"

    @commands.command(name='color', aliases=['rc'])
    @commands.has_permissions()
    async def color(self, ctx):
        embed = await Utils(self.bot).embed(ctx, title="Generated!", description=f"**Color: ``{self.color}``**",
                                            color=self.color)
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Color(bot))
