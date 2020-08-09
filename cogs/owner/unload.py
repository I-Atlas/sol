import discord
from discord.ext import commands
from ..events.utils import Utils


class Unload(commands.Cog):
    """Unload Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that unloads commands 🧠"
        self.usage = "unload [cogs.category.command]"

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, command=None):
        if not command:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a command to unload.",
                                                description="", color=ctx.author.color)
            return await ctx.send(embed=embed)
        try:
            self.bot.unload_extension(command)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)
        else:
            embed = await Utils(self.bot).embed(ctx, title=f"The ``{command.split('.')[2]}`` command has been unloaded.",
                                                description="", color=ctx.author.color)
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Unload(bot))