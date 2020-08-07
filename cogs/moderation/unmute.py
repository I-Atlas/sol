# Imports
import discord
from discord.ext import commands


# Main Command Class
class Unmute(commands.Cog):
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
            embed = discord.Embed(title=f"Please specify someone to mute.", color=ctx.author.color)

            embed.set_author(name=f" | Unmute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        if not muted:
            embed = discord.Embed(title=f"No muted role on the server.", color=ctx.author.color)

            embed.set_author(name=f" | Unmute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        if not muted_member:
            embed = discord.Embed(title=None, description=f"User {member.mention} isn't muted.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Unmute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        try:
            await member.remove_roles(muted)

            embed = discord.Embed(title=None, description=f"User {member.mention} has been unmuted  :loud_sound:.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Unmute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            embed = discord.Embed(title=f"Something went wrong: {error}.", color=ctx.author.color)

            embed.set_author(name=f" | Unmute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Unmute(bot))
