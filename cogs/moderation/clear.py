import asyncio
import discord
from discord.ext import commands
from ..events.utils import Utils


class Clear(commands.Cog):
    """Clear Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Deletes messages from a channel"
        self.usage = "clear [amount]"

    @commands.command(name='clear', aliases=['cl'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        try:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)

            embed = discord.Embed(description=f'Deleted *{amount}* messages', color=ctx.author.color)

            await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=1)
        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Clear(bot))
