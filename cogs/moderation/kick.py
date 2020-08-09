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

        await ctx.message.delete()

        if member is None:
            embed = await Utils(self.bot).embed(ctx, title="Please specify someone to kick.",
                                                description="", color=0xf75252)
            return await ctx.send(embed=embed)

        elif member is ctx.message.author:
            embed = await Utils(self.bot).embed(ctx, title="You cannot kick yourself.",
                                                description="", color=0xf75252)
            await ctx.send(embed=embed)
        else:
            if reason is None:
                try:
                    await ctx.guild.kick(member)

                    embed = await Utils(self.bot).embed(ctx, title="",
                                                        description=f"{member.mention} kicked by {ctx.author.mention}.",
                                                        color=0xa9ffda)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(title="Kick",
                                          description=f'You has been kicked from the server {ctx.guild.name}.',
                                          color=0xa9ffda)
                    await member.send(embed=embed)

                except Exception as error:
                    error_handler = await Utils(self.bot).error(ctx, str(error))

                    return await ctx.send(embed=error_handler)

            elif reason is not None:
                try:
                    await ctx.guild.kick(member)

                    embed = await Utils(self.bot).embed(ctx, title="",
                                                        description=f"{member.mention} kicked by {ctx.author.mention} "
                                                                    f"with reason: {reason}.",
                                                        color=0xa9ffda)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(title="Kick",
                                          description=f"You has been kicked from the server {ctx.guild.name} "
                                                      f"with reason: {reason}.",
                                          color=0xa9ffda)
                    await member.send(embed=embed)

                except Exception as error:
                    error_handler = await Utils(self.bot).error(ctx, str(error))

                    return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Kick(bot))
