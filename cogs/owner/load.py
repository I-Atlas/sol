import discord
from discord.ext import commands
from ..events.utils import Utils


class Load(commands.Cog):
    """Load Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that loads commands 🧠"
        self.usage = "load [cogs.category.command]"

    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, command=None):
        if not command:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a command to load.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            self.bot.load_extension(command)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)
        else:
            embed = await Utils(self.bot).embed(ctx, title=f"The ``{command.split('.')[2]}`` command has been loaded.",
                                                description="", color=ctx.author.color)
            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Load(bot))
