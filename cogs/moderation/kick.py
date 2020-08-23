import discord
from discord.ext import commands
from ..events.utils import Utils


class Kick(commands.Cog):
    """Kick Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Kicks a member from the server"
        self.usage = "kick [user] [reason]"

    @commands.command(name='kick', aliases=['kickuser'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None, reason=None):
        if not member:
            embed = await Utils(self.bot).embed(ctx, title="Please specify someone to kick.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        elif member is ctx.message.author:
            embed = await Utils(self.bot).embed(ctx, title="You cannot kick yourself.",
                                                description="", color=0xDE6246)
            await ctx.send(embed=embed)
        else:
            if reason:
                try:
                    await ctx.guild.kick(member)

                    embed = await Utils(self.bot).embed(ctx, title="",
                                                        description=f"{member.mention} kicked by {ctx.author.mention} "
                                                                    f"with reason: {reason}.",
                                                        color=ctx.author.color)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(title="Kick",
                                          description=f"You has been kicked from the server {ctx.guild.name} "
                                                      f"with reason: {reason}.",
                                          color=0xDE6246)
                    await member.send(embed=embed)

                except Exception as error:
                    error_handler = await Utils(self.bot).error(ctx, str(error))

                    return await ctx.send(embed=error_handler)

            elif not reason:
                try:
                    await ctx.guild.kick(member)

                    embed = await Utils(self.bot).embed(ctx, title="",
                                                        description=f"{member.mention} kicked by {ctx.author.mention}.",
                                                        color=ctx.author.color)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(title="Kick",
                                          description=f'You has been kicked from the server {ctx.guild.name}.',
                                          color=0xDE6246)
                    await member.send(embed=embed)

                except Exception as error:
                    error_handler = await Utils(self.bot).error(ctx, str(error))

                    return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Kick(bot))
