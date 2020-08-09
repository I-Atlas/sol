import discord
from discord.ext import commands
from ..events.utils import Utils


class Reload(commands.Cog):
    """Reload Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that reloads commands 🧠"
        self.usage = "reload [cogs.category.command]"

    @commands.command(name='reload', aliases=['rl'])
    @commands.is_owner()
    async def reload(self, ctx, command=None):
        if not command:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a command to reload.",
                                                description="", color=ctx.author.color)
            return await ctx.send(embed=embed)
        try:
            self.bot.unload_extension(command)
            self.bot.load_extension(command)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)
        else:
            embed = await Utils(self.bot).embed(ctx, title=f"The ``{command.split('.')[2]}`` command has been reloaded.",
                                                description="", color=ctx.author.color)
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Reload(bot))