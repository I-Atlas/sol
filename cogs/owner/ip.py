from discord.ext import commands
from ..events.utils import Utils


class Ip(commands.Cog):
    """Ip Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Creates iptables config."
        self.usage = "iptables [IP#1 IP#2 IP#3 IP#4 IP#5]"

    @commands.command(name='ip', aliases=['iptables'])
    @commands.has_permissions()
    async def ip(self, ctx, *, text):
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please select 5 IPs to generate the configuration.",
                                                description="",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            first = text.split(" ")
            second = [list(i) for i in first]
            third = [[f'3{i}' for i in j] for j in second]

            first_ip = " ".join(third[0])
            second_ip = " ".join(third[1])
            third_ip = " ".join(third[2])
            fourth_ip = " ".join(third[3])
            fifth_ip = " ".join(third[4])

            embed = await Utils(self.bot).embed(ctx, title=f"Generated!",
                                                description="``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            "27000:27200 --match string --algo kmp --hex-string '|73 "
                                                            "74 65 61 6d 69 64 3a 37 36 35 36|' -j DROP``\n "
                                                            f"``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            f"27000:27200 --match string --algo kmp --hex-string '|"
                                                            f"{first_ip}|' -j ACCEPT``\n "
                                                            f"``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            f"27000:27200 --match string --algo kmp --hex-string '|"
                                                            f"{second_ip}|' -j ACCEPT``\n "
                                                            f"``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            f"27000:27200 --match string --algo kmp --hex-string '|"
                                                            f"{third_ip}|' -j ACCEPT``\n "
                                                            f"``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            f"27000:27200 --match string --algo kmp --hex-string '|"
                                                            f"{fourth_ip}|' -j ACCEPT``\n "
                                                            f"``iptables -I FORWARD -s 10.66.66.2 -p udp --dport "
                                                            f"27000:27200 --match string --algo kmp --hex-string '|"
                                                            f"{fifth_ip}|' -j ACCEPT``\n",
                                                color=ctx.author.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Ip(bot))