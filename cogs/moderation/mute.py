# Imports
import discord
from discord.ext import commands


# Main Command Class
class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Mutes someone on the server"
        self.usage = "mute [user]"

    @commands.command(name='mute', aliases=['m'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, *, member: discord.Member = None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if not member:
            embed = discord.Embed(title=f"Please specify someone to mute.", color=ctx.author.color)

            embed.set_author(name=f" | Mute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        if not muted:
            muted = await ctx.guild.create_role(name="Muted", reason="Sol; Muted role")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted, send_messages=False)
        await member.add_roles(muted)

        try:
            embed = discord.Embed(title=None, description=f"User {member.mention} has been muted  :mute:.",
                                  color=ctx.author.color)

            embed.set_author(name=f" | Mute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            embed = discord.Embed(title=f"Something went wrong: {error}.", color=ctx.author.color)

            embed.set_author(name=f" | Mute", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Mute(bot))
