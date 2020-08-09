import discord
from discord.ext import commands
from ..events.utils import Utils


class Avatar(commands.Cog):
    """Avatar Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Opens user avatar"
        self.usage = "avatar [user]"

    @commands.command(name='avatar', aliases=['pp'])
    @commands.has_permissions()
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        try:
            embed = discord.Embed(title=f"{member.name}'s avatar:", color=ctx.author.color)

            embed.set_image(url=member.avatar_url)

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Avatar", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Avatar(bot))
