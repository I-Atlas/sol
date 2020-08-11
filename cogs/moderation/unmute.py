import discord
from discord.ext import commands
from ..events.utils import Utils


class Unmute(commands.Cog):
    """Unmute Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Unmutes someone on the server"
        self.usage = "unmute [user]"

    @commands.command(name='unmute', aliases=['um'])
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, *, member: discord.Member = None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        muted_member = False

        for role in member.roles:
            if role.name == "Muted":
                muted_member = True

        if not member:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a user to unmute.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        if not muted:
            embed = await Utils(self.bot).embed(ctx, title="No muted role on the server.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        if not muted_member:
            embed = await Utils(self.bot).embed(ctx, title="",
                                                description=f"User {member.mention} isn't muted.",
                                                color=0xDE6246)
            return await ctx.send(embed=embed)
        try:
            await member.remove_roles(muted)

            embed = await Utils(self.bot).embed(ctx, title="",
                                                description=f"User {member.mention} has been unmuted  :loud_sound:.",
                                                color=ctx.author.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Unmute(bot))
