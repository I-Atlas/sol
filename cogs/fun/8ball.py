import random
import discord
from discord.ext import commands
from ..events.utils import Utils


class Eball(commands.Cog):
    """Eball Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Flips a coin."
        self.usage = "eball [text]"

    @commands.command(name='eball', aliases=['8ball'])
    @commands.has_permissions()
    async def eball(self, ctx, *, text=None):
        if not text:
            embed = discord.Embed(title=f"Please ask a question to the magic ball.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Eball", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        for member in ctx.member.mentions:
            text = text.replace(f"<@!{member.id}>", member.name)
        try:
            embed = discord.Embed(title=text,
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

            embed.set_author(name=f" | 8ball", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Eball(bot))
