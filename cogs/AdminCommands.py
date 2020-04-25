import asyncio
import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Ban user on server"
        self.usage = "ban/bn [user] [reason]"

    @commands.Cog.listener()
    async def on_ready(self):
        print('- - - - -\nAdminCommands has been loaded!')

    @commands.command(name='ban', aliases=['bn'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member = None, reason=None):
        """
        A command that ban users.
        """
        await ctx.message.delete()
        if member is None:
            embed = discord.Embed(title='⚠', description=f'Please specify someone to ban.', color=0xf75252, delete_after=10)
            await ctx.send(embed=embed)
        elif member is ctx.message.author:
            embed = discord.Embed(title='⚠', description=f'You cannot ban yourself.', color=0xf75252, delete_after=10)
            await ctx.send(embed=embed)
        else:
            if reason is None:
                embed = discord.Embed(title=None, description=f'{member.mention} banned by {ctx.author.mention}.', color=0xa9ffda)
                embed.set_author(name=" | Ban", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Banned by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Ban', description=f'You has been banned on server {ctx.guild.name}.', color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception:
                    print('Ban error')
                finally:
                    await ctx.guild.ban(member)
            elif reason is not None:
                embed = discord.Embed(title=None, description=f'{member.mention} banned by {ctx.author.mention} with reason: {reason}.', color=0xa9ffda)
                embed.set_author(name=" | Ban", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Banned by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Ban', description=f'You has been banned on server {ctx.guild.name} with reason: {reason}.', color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception:
                    print('Ban error')
                finally:
                    await ctx.guild.ban(member)

    @commands.command(name='kick', aliases=['kickuser'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        """
        A command that kick users.
        """
        await ctx.message.delete()
        if member is None:
            embed = discord.Embed(title='⚠', description=f'Please specify someone to kick.', color=0xf75252, delete_after=10)
            await ctx.send(embed=embed)
        elif member is ctx.message.author:
            embed = discord.Embed(title='⚠', description=f'You cannot kick yourself.', color=0xf75252, delete_after=10)
            await ctx.send(embed=embed)
        else:
            if reason is None:
                embed = discord.Embed(title=None, description=f'{member.mention} kicked by {ctx.author.mention}.', color=0xa9ffda)
                embed.set_author(name=" | Kick", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Kicked by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Kick', description=f'You has been kicked from the server {ctx.guild.name}.', color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception:
                    print('Kick error')
                finally:
                    await ctx.guild.kick(member)
            elif reason is not None:
                embed = discord.Embed(title=None, description=f'{member.mention} kicked by {ctx.author.mention} with reason: {reason}.', color=0xa9ffda)
                embed.set_author(name=" | Kick", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Kicked by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Kick', description=f'You has been kicked from the server {ctx.guild.name} with reason: {reason}.', color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception:
                    print('Kick error')
                finally:
                    await ctx.guild.kick(member)

    @commands.command(name='clear', aliases=['cl'])
    @commands.has_permissions(manage_messages=True)
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
    """
    Cog setup.
    """
    bot.add_cog(AdminCommands(bot))
