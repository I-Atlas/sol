import psutil
import platform
import discord
from discord.ext import commands
from ..events.utils import Utils


class System(commands.Cog):
    """System Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that displays system information"
        self.usage = "system"

    @commands.command(name='system', aliases=['sy'])
    @commands.has_permissions()
    async def stats(self, ctx):
        try:
            embed = discord.Embed(color=ctx.author.color)

            embed.set_image(url=self.bot.user.avatar_url)

            embed.add_field(name='Python version', value=platform.python_version())
            embed.add_field(name='discord.py version', value=discord.__version__)
            embed.add_field(name='System', value=f"{platform.uname().system} {platform.uname().release}\n"
                                                 f"{platform.uname().node}")
            embed.add_field(name='RAM', value=f"**Total:** {round(psutil.virtual_memory().total / 1024 ** 3)} GB\n"
                                              f"**Available:** {round(psutil.virtual_memory().available / 1024 ** 3)} GB\n"
                                              f"**Usage:** {psutil.virtual_memory().percent}%")
            embed.add_field(name='CPU', value=f"**Type:** {platform.uname().machine}\n"
                                              f"**Cores:** {psutil.cpu_count(logical=True)}\n"
                                              f"**Frequency:** {psutil.cpu_freq().current:.2f}Mhz\n"
                                              f"**Usage:** {psutil.cpu_percent()}%")

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | System", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)
        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(System(bot))
