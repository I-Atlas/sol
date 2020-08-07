# Imports
import discord
from discord.ext import commands


# Main Command Class
class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Kicks a member from the server"
        self.usage = "kick [user] [reason]"

    @commands.command(name='kick', aliases=['kickuser'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        await ctx.message.delete()
        if member is None:
            embed = discord.Embed(title='⚠', description=f'Please specify someone to kick.', color=0xf75252,
                                  delete_after=10)
            await ctx.send(embed=embed)
        elif member is ctx.message.author:
            embed = discord.Embed(title='⚠', description=f'You cannot kick yourself.', color=0xf75252, delete_after=10)
            await ctx.send(embed=embed)
        else:
            if reason is None:
                embed = discord.Embed(title=None, description=f'{member.mention} kicked by {ctx.author.mention}.',
                                      color=0xa9ffda)
                embed.set_author(name=" | Kick", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Kicked by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Kick',
                                          description=f'You has been kicked from the server {ctx.guild.name}.',
                                          color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception as error:
                    embed = discord.Embed(title=f"Something went wrong: {error}.",
                                          color=ctx.author.color)
                    embed.set_author(name=f" | Kick", icon_url=self.bot.user.avatar_url)
                    embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
                    return await ctx.send(embed=embed)
                finally:
                    await ctx.guild.kick(member)
            elif reason is not None:
                embed = discord.Embed(title=None,
                                      description=f'{member.mention} kicked by {ctx.author.mention} with reason: {reason}.',
                                      color=0xa9ffda)
                embed.set_author(name=" | Kick", icon_url=self.bot.user.avatar_url)
                embed.set_footer(text=f" | Kicked by {ctx.author}.", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
                try:
                    embed = discord.Embed(title='Kick',
                                          description=f'You has been kicked from the server {ctx.guild.name} with reason: {reason}.',
                                          color=0xa9ffda)
                    await member.send(embed=embed)
                except Exception as error:
                    embed = discord.Embed(title=f"Something went wrong: {error}.",
                                          color=ctx.author.color)
                    embed.set_author(name=f" | Kick", icon_url=self.bot.user.avatar_url)
                    embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
                    return await ctx.send(embed=embed)
                finally:
                    await ctx.guild.kick(member)


# Link to bot
def setup(bot):
    bot.add_cog(Kick(bot))
