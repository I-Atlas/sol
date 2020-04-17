import random
import discord
from discord.ext import commands


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- - - - -\nMiscCommands has been loaded!\n- - - - -')

    @commands.command(name='color', aliases=['rc'])
    @commands.has_permissions()
    async def rnd_color(self, ctx):
        clr = (random.randint(0, 16777215))
        embed = discord.Embed(description=f'Color generated : ``#{hex(clr)[2:]}``', colour=clr)
        await ctx.send(embed=embed)

    @commands.command(name='say', aliases=['s'])
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, channel: discord.TextChannel, cnt):
        await ctx.message.delete()  # delete your message
        embed = discord.Embed(description=cnt, colour=0xa9ffda)  # Generate embed message
        await channel.send(embed=embed)  # Sending a message to the channel you specified

    @commands.command(name='game', aliases=['g'])
    @commands.has_permissions()
    async def game(self, ctx, member: discord.Member = None):
        await ctx.message.delete()  # delete your message
        user = ctx.message.author if (member == None) else member
        if user.activity:
            embed = discord.Embed(description=f'User {user.mention} plays **{user.activity}**', color=0xa9ffda)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'User {user.mention} doesn’t play anything**', color=0xa9ffda)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MiscCommands(bot))