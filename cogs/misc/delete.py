from discord.ext import commands
from cogs.events.utils import Utils


class Delete(commands.Cog):
    """Delete Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Removes iptables config."
        self.usage = "delete [number of IP's]"

    @commands.command(name='delete', aliases=['del'])
    @commands.has_permissions()
    async def delete(self, ctx, *, text):
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please specify number of IP's.",
                                                description="",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            first = f"``iptables --delete FORWARD 1``\n"
            second = first * int(text)

            embed = await Utils(self.bot).embed(ctx, title=f"Generated!",
                                                description=f"{second}",
                                                color=ctx.author.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Delete(bot))
