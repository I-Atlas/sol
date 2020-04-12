import asyncio
import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', aliases=['banuser'], pass_context=True, invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def ban_user_command(self, ctx, member: discord.Member = None, reason=None):
        await ctx.message.delete()  # delete your message
        em = discord.Embed(description=f'User *{member.mention}* has been banned.', color=0xa9ffda)
        await ctx.channel.send(embed=em)  # embed

    @commands.command(name='clear', aliases=['cl'], pass_context=True, invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        await ctx.message.delete()  # delete your message
        await ctx.channel.purge(limit=amount)  # delete messages
        em = discord.Embed(description=f'Deleted *{amount}* messages', color=0xa9ffda)
        await ctx.send(embed=em)  # embed
        await asyncio.sleep(3)  # sleep timer
        await ctx.channel.purge(limit=1)  # delete bot message

    @commands.command(name='move', aliases=['mv'], pass_context=True, invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def move(self, ctx, arg=None, member: discord.Member = None):
        channels = ctx.author.voice.channel.id
        await ctx.message.delete()
        if not channels:
            em = discord.Embed(description=f'You must be in a voice channel', color=0xf75252)
            await ctx.channel.send(embed=em, delete_after=10)
            return
        if not arg:
            em = discord.Embed(description=f'It is necessary to indicate where to move users', color=0xf75252)
            await ctx.channel.send(embed=em, delete_after=10)
            return
        voice = ctx.guild.voice_channels
        print(voice)
        try:
            vchannel = voice[int(arg) - 1]
        except:
            em = discord.Embed(description=f'Invalid Argument', color=0xf75252)
            await ctx.channel.send(embed=em, delete_after=10)
            return
        if member == None:
            x = ctx.author.voice.channel.members
            for mem in x:
                await mem.edit(voice_channel=vchannel)
        else:
            await member.edit(voice_channel=vchannel)


def setup(bot):
    bot.add_cog(AdminCommands(bot))
