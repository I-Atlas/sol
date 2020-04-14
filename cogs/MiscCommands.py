import random
import discord
from discord.ext import commands


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='color', aliases=['random_color'], pass_context=True)
    @commands.has_permissions()
    async def random_color(self, ctx):
        clr = (random.randint(0, 16777215))
        emb = discord.Embed(description=f'Color generated : ``#{hex(clr)[2:]}``', colour=clr)
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, channel: discord.TextChannel, *, cnt):
        await ctx.message.delete()  # delete your message
        embed = discord.Embed(description=cnt, colour=0x00ff80)  # Generate embed message
        await channel.send(embed=embed)  # Sending a message to the channel you specified

    @commands.command()
    @commands.has_permissions()
    async def game(self, ctx, member: discord.Member = None):
        await ctx.message.delete()  # delete your message
        user = ctx.message.author if (member == None) else member
        if user.activity:
            em = discord.Embed(description=f'User {user.mention} plays **{user.activity}**', color=0xa9ffda)
            await ctx.send(embed=em)
        else:
            em = discord.Embed(description=f'User {user.mention} doesn’t play anything**', color=0xa9ffda)
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(MiscCommands(bot))
