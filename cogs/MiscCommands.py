import random
import discord
from discord.ext import commands


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='color', aliases=['random_color'], pass_context=True)
    @commands.has_permissions()
    async def ran_color(self, ctx):
        clr = (random.randint(0, 16777215))
        emb = discord.Embed(description=f'Color generated : ``#{hex(clr)[2:]}``', colour=clr)
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(MiscCommands(bot))
