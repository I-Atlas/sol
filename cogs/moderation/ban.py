# Imports
import discord
from discord.ext import commands


# Main Command Class
class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Bans a member on the server"
        self.usage = "ban [user] [reason]"

    @commands.command(name='ban', aliases=['bn'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, *, member: discord.Member = None, reason=None):
        await ctx.message.delete()
        if member is None:
            embed = discord.Embed(title='⚠', description=f'Please specify someone to ban.', color=0xf75252,
                                  delete_after=10)
            await ctx.send(embed=embed)
        elif member is ctx.message.author:
            embed = discord.Embed(title='⚠', description=f'You cannot ban yourself.', color=0xf75252, delete_after=10)
            await ctx.send(embed=embed)
        else:
            if reason is None:
                embed = discord.Embed(title=None, description=f'{member.mention} banned by {ctx.author.mention}.',
                                      color=0xa9ffda)
                embed.set_author(name=" | Ban", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Banned by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Ban', description=f'You has been banned on server {ctx.guild.name}.',
                                          color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception as error:
                    embed = discord.Embed(title=f"Something went wrong: {error}.",
                                          color=ctx.author.color)
                    embed.set_author(name=f" | Ban", icon_url=self.bot.user.avatar_url)
                    embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
                    return await ctx.send(embed=embed)
                finally:
                    await ctx.guild.ban(member)
            elif reason is not None:
                embed = discord.Embed(title=None,
                                      description=f'{member.mention} banned by {ctx.author.mention} with reason: {reason}.',
                                      color=0xa9ffda)
                embed.set_author(name=" | Ban", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Banned by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Ban',
                                          description=f'You has been banned on server {ctx.guild.name} with reason: {reason}.',
                                          color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception as error:
                    embed = discord.Embed(title=f"Something went wrong: {error}.",
                                          color=ctx.author.color)
                    embed.set_author(name=f" | Ban", icon_url=self.bot.user.avatar_url)
                    embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
                    return await ctx.send(embed=embed)
                finally:
                    await ctx.guild.ban(member)


# Link to bot
def setup(bot):
    bot.add_cog(Ban(bot))
