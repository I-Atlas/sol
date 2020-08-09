from discord.ext import commands
from ..events.utils import Utils


class Tts(commands.Cog):
    """TTS Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sends tts message."
        self.usage = "tts [text]"

    @commands.command(name='tts', aliases=['t'])
    @commands.has_permissions()
    async def tts(self, ctx, *, text):
        await ctx.message.delete()
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please specify something to tts.", description="",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            return await ctx.send(text, tts=True)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Tts(bot))