import discord
from discord.ext import commands
from ..events.utils import Utils


class Ban(commands.Cog):
    def __init__(self, bot):
        """Ban Command Class"""

        self.bot = bot
        self.desc = "Bans a member on the server"
        self.usage = "ban [user] [reason]"

    @commands.command(name='ban', aliases=['bn'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, *, member: discord.Member, reason=None):
        if not member:
            embed = await Utils(self.bot).embed(ctx, title="Please specify someone to ban.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        elif member is ctx.message.author:
            embed = await Utils(self.bot).embed(ctx, title="You cannot ban yourself.",
                                                description="", color=0xDE6246)
            await ctx.send(embed=embed)
        else:
            if reason:
                try:
                    await ctx.guild.ban(member)

                    embed = await Utils(self.bot).embed(ctx, title="",
                                                        description=f"{member.mention} banned by {ctx.author.mention} "
                                                                    f"with reason: {reason}.",
                                                        color=ctx.author.color)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(title="Ban",
                                          description=f"You has been banned on the server {ctx.guild.name} "
                                                      f"with reason: {reason}.",
                                          color=0xDE6246)
                    await member.send(embed=embed)

                except Exception as error:
                    error_handler = await Utils(self.bot).error(ctx, str(error))

                    return await ctx.send(embed=error_handler)

            elif not reason:
                try:
                    await ctx.guild.ban(member)

                    embed = await Utils(self.bot).embed(ctx, title="",
                                                        description=f"{member.mention} banned by {ctx.author.mention}.",
                                                        color=0xa9ffda)
                    await ctx.send(embed=embed)

                    embed = discord.Embed(title="Ban",
                                          description=f'You has been banned on the server {ctx.guild.name}.',
                                          color=ctx.author.color)
                    await member.send(embed=embed)

                except Exception as error:
                    error_handler = await Utils(self.bot).error(ctx, str(error))

                    return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Ban(bot))
