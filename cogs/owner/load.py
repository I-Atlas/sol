import discord
from discord.ext import commands


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
            embed = discord.Embed(title="Please specify a command to load.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Load", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        try:
            self.bot.load_extension(command)

        except Exception as error:
            embed = discord.Embed(title=f"Command {command.split('.')[2]} failed to load. Error: {error}.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Load", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"The ``{command.split('.')[2]}`` command has been loaded.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Load", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Load(bot))
