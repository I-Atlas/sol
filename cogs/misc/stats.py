from discord.ext import commands
from ..events.utils import Utils


class Stats(commands.Cog):
    """Stats Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that displays bot stats"
        self.usage = "stats"

    @commands.command(name='stats', aliases=['st'])
    @commands.has_permissions()
    async def stats(self, ctx):
        try:
            embed = discord.Embed(color=0xFFD700)

            embed.set_image(url=self.bot.user.avatar_url)

            embed.add_field(name='Total guilds', value=str(len(self.bot.guilds)))
            embed.add_field(name='Total users', value=str(len(set(self.bot.get_all_members()))))
            embed.add_field(name='Bot developers', value='<@271684584863825920>')

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Stats", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)
        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Stats(bot))
