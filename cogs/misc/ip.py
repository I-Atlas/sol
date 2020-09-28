from discord.ext import commands
from cogs.events.utils import Utils


class Ip(commands.Cog):
    """Ip Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Creates iptables config."
        self.usage = "ip [IP]"

    @commands.command(name='ip', aliases=['iptables'])
    @commands.has_permissions()
    async def ip(self, ctx, *, text):
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please specify IP's to generate the configuration.",
                                                description="",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            first = text.split(" ")
            second = list(map(lambda x: f"``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                        f"27000:27200 --match string --algo kmp --string "
                                        f"{x} -j ACCEPT``\n ", first))
            third = f"".join(str(x) for x in second)

            embed = await Utils(self.bot).embed(ctx, title=f"Generated!",
                                                description="``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            "27000:27200 --match string --algo kmp --hex-string '|73 "
                                                            "74 65 61 6d 69 64 3a 37 36 35 36|' -j DROP``\n "
                                                            f"{third}",
                                                color=ctx.author.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Ip(bot))
