import random
from discord.ext import commands
from ..events.utils import Utils


class Eight(commands.Cog):
    """Eight Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Magic 8 ball - fortune telling tool."
        self.usage = "eight [text]"

    @commands.command(name='eight', aliases=['ball'])
    @commands.has_permissions()
    async def eight(self, ctx, *, text=None):
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please ask a question to the magic ball.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        for member in ctx.message.mentions:
            text = text.replace(f"<@!{member.id}>", member.name)
        try:
            embed = await Utils(self.bot).embed(ctx, title=text,
                                                description=random.choice([
                                                    "It is certain.",
                                                    "It is decidedly so.",
                                                    "Without a doubt.",
                                                    "Yes - definitely.",
                                                    "You may rely on it.",
                                                    "As I see it, yes.",
                                                    "Most likely.",
                                                    "Outlook good.",
                                                    "Signs point to yes.",
                                                    "Yes.",
                                                    "Reply hazy, try again.",
                                                    "Ask again later.",
                                                    "Better not tell you now.",
                                                    "Cannot predict now.",
                                                    "Concentrate and ask again.",
                                                    "Don't count on it.",
                                                    "My reply is no.",
                                                    "My sources say no.",
                                                    "Outlook not so good.",
                                                    "Very doubtful."
                                                ]),
                                                color=ctx.author.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Eight(bot))
