# Imports
import asyncio
import discord
from discord.ext import commands


# Main Command Class
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Deletes messages from a channel"
        self.usage = "clear [amount]"

    @commands.command(name='clear', aliases=['cl'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        await ctx.message.delete()  # delete your message
        await ctx.channel.purge(limit=amount)  # delete messages
        embed = discord.Embed(description=f'Deleted *{amount}* messages', color=0xa9ffda)
        await ctx.send(embed=embed)  # embed
        await asyncio.sleep(3)  # sleep timer
        await ctx.channel.purge(limit=1)  # delete bot message after 3 seconds


# Link to bot
def setup(bot):
    bot.add_cog(Clear(bot))
