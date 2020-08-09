import discord
from discord.ext import commands


class Utils(commands.Cog):
    """Utils Class"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def error(self, ctx, error_message):
        embed = discord.Embed(color=0xDE6246)

        embed.add_field(name=":warning:  Error",
                        value=f"**Something went wrong:** ``{error_message}``", inline=False)

        embed.set_author(name=f" | {(str(ctx.command.name)).capitalize()}", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

        return embed

    @commands.Cog.listener()
    async def embed(self, ctx, title, description, color):
        embed = discord.Embed(title=f"{title}", description=f"{description}", color=color)

        embed.set_author(name=f" | {(str(ctx.command.name)).capitalize()}", icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

        return embed


def setup(bot):
    bot.add_cog(Utils(bot))