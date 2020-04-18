import asyncio
import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('- - - - -\nAdminCommands has been loaded!')

    @commands.command(name='ban', aliases=['banuser'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member):
        await ctx.guild.ban(member)
        await ctx.message.delete()  # delete your message
        embed = discord.Embed(description=f'User *{member.mention}* has been banned.', color=0xa9ffda)
        await ctx.channel.send(embed=embed)  # embed

    @commands.command(name='unban', aliases=['unbanuser'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, member: discord.Member):
        await ctx.guild.unban(member)
        await ctx.message.delete()  # delete your message
        embed = discord.Embed(description=f'User *{member.mention}* has been unbanned.', color=0xa9ffda)
        await ctx.channel.send(embed=embed)  # embed

    @commands.command(name='kick', aliases=['kickuser'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member):
        await ctx.guild.kick(member)
        await ctx.message.delete()  # delete your message
        embed = discord.Embed(description=f'User *{member.mention}* has been kicked.', color=0xa9ffda)
        await ctx.channel.send(embed=embed)  # embed

    @commands.command(name='clear', aliases=['cl'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        """
        A command that clear chat.
        """
        await ctx.message.delete()  # delete your message
        await ctx.channel.purge(limit=amount)  # delete messages
        embed = discord.Embed(description=f'Deleted *{amount}* messages', color=0xa9ffda)
        await ctx.send(embed=embed)  # embed
        await asyncio.sleep(3)  # sleep timer
        await ctx.channel.purge(limit=1)  # delete bot message

    @commands.command(name='move', aliases=['mv'], invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def move(self, ctx, arg=None, member: discord.Member = None):
        """
        A command that move members from one voice chat to another.
        """
        channels = ctx.author.voice.channel.id
        await ctx.message.delete()
        if not channels:
            embed = discord.Embed(description=f'You must be in a voice channel', color=0xf75252)
            await ctx.channel.send(embed=embed, delete_after=10)
            return
        if not arg:
            embed = discord.Embed(description=f'It is necessary to indicate where to move users', color=0xf75252)
            await ctx.channel.send(embed=embed, delete_after=10)
            return
        voice = ctx.guild.voice_channels
        print(voice)
        try:
            vchannel = voice[int(arg) - 1]
        except:
            embed = discord.Embed(description=f'Invalid Argument', color=0xf75252)
            await ctx.channel.send(embed=embed, delete_after=10)
            return
        if member == None:
            x = ctx.author.voice.channel.members
            for mem in x:
                await mem.edit(voice_channel=vchannel)
        else:
            await member.edit(voice_channel=vchannel)


def setup(bot):
    bot.add_cog(AdminCommands(bot))