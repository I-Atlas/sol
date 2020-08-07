import asyncio
import discord
from discord.ext import commands


class Clear(commands.Cog):
    """Clear Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Deletes messages from a channel"
        self.usage = "clear [amount]"

    @commands.command(name='clear', aliases=['cl'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(description=f'Deleted *{amount}* messages', color=0xa9ffda)

        await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Clear(bot))
