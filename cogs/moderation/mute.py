import discord
from discord.ext import commands
from ..events.utils import Utils


class Mute(commands.Cog):
    """Mute Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Mutes someone on the server"
        self.usage = "mute [user]"

    @commands.command(name='mute', aliases=['m'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, *, member: discord.Member = None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if not member:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a command to mute.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        if not muted:
            muted = await ctx.guild.create_role(name="Muted", reason="Sol; Muted role", color=0xDE6246)
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted, send_messages=False)
        await member.add_roles(muted)

        try:
            embed = await Utils(self.bot).embed(ctx, title="",
                                                description=f"User {member.mention} has been muted  :mute:.",
                                                color=ctx.author.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Mute(bot))
