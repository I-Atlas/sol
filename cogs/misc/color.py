# Imports
import random
import discord
from discord.ext import commands


# Main Command Class
class Color(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Creates a random rgb color"
        self.usage = "color"

    @commands.command(name='color', aliases=['rc'])
    @commands.has_permissions()
    async def color(self, ctx):
        color = (random.randint(0, 16777215))
        embed = discord.Embed(description=f'Color generated : ``#{hex(color)[2:]}``', color=color)
        return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Color(bot))
