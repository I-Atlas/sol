import discord
from discord.ext import commands
from datetime import datetime


class Api(commands.Cog):
    def __init__(self, bot):
        """Api Command Class"""

        self.bot = bot
        self.desc = "Opens user avatar"
        self.usage = "avatar [user]"

    @commands.command(name='api')
    @commands.has_permissions()
    async def api(self, ctx):
        api = round(self.bot.latency * 1000)
        time = datetime.now()
        calculation = await ctx.send("Calculation message.")
        bot = str(datetime.now() - time).split(".")[1][:2]

        try:
            await calculation.delete()

            embed = discord.Embed(color=0x362D73)

            embed.set_image(url="https://imgur.com/n4vJk3J.png")

            embed.add_field(name="API Latency", value=f"{api}ms")
            embed.add_field(name=f"{self.bot.user} Latency", value=f"{bot}ms")

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Api", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            embed = discord.Embed(title=f"Something went wrong: {error}.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Api", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Api(bot))