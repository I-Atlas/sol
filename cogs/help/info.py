# Imports
import discord
from discord.ext import commands


# Main Command Class
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "User information."
        self.usage = "info [user]"

    @commands.command(name='info', aliases=['i'])
    @commands.has_permissions()
    async def info(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        try:
            embed = discord.Embed(color=ctx.author.color)

            embed.add_field(name=f"Information about ", value=f"{member.mention}", inline=False)
            embed.add_field(name="Joined the server", value=f"{member.joined_at.strftime('%b %#d, %Y')}", inline=False)
            embed.add_field(name="ID", value=f"{member.id}", inline=False)
            embed.add_field(name="Main nickname", value=f"{member.name}", inline=False)
            embed.add_field(name="Server nickname", value=f"{member.nick}", inline=False)
            embed.add_field(name="Status", value=f"{member.status}", inline=False)
            embed.add_field(name="Created", value=f"{member.created_at.strftime('%b %#d, %Y')}", inline=False)

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Info", icon_url=self.bot.user.avatar_url)
            """
            You can add a field with a full user avatar:
            
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(icon_url=member.avatar_url)
            """
            await ctx.send(embed=embed)
        except:
            await ctx.send("I can`t show information about this user.")


# Link to bot
def setup(bot):
    bot.add_cog(Info(bot))