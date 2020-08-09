from discord.ext import commands
from ..events.utils import Utils


class Say(commands.Cog):
    """Say Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sends a message on behalf of the bot."
        self.usage = "say [text]"

    @commands.command(name='say', aliases=['s'])
    @commands.has_permissions()
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please specify something to say.", description="",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            return await ctx.send(text)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Say(bot))