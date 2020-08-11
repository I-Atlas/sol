import random
from discord.ext import commands
from ..events.utils import Utils


class Weird(commands.Cog):
    """Weird Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sends a weird text message."
        self.usage = "weird [text]"

    @commands.command(name='weird', aliases=['w'])
    @commands.has_permissions()
    async def weird(self, ctx, *, text=None):
        message = ""
        await ctx.message.delete()
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please specify something to transform.", description="",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            for char in text:
                if random.randint(1, 2) == 1:
                    message = f"{message}{char.upper()}"
                else:
                    message = f"{message}{char.lower()}"

            return await ctx.send(message)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Weird(bot))
