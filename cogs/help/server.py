# Imports
import discord
from discord.ext import commands


# Main Command Class
class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Server information"
        self.usage = "server [user]"

    @commands.command(name='server', aliases=['guild'])
    @commands.has_permissions()
    async def server(self, ctx, guild: discord.Guild = None):
        if not guild:
            pass
        try:
            embed = discord.Embed(color=ctx.author.color)

            embed.add_field(name="Information about ", value=f"{ctx.guild.name}", inline=False)

            embed.add_field(name="Region", value=f"{ctx.guild.region}", inline=False)
            embed.add_field(name="Server owner", value=f"{ctx.guild.owner.name}", inline=False)
            embed.add_field(name="Member count", value=f"{ctx.guild.member_count}", inline=False)
            embed.add_field(name="Role count", value=f"{len(ctx.guild.roles)}", inline=False)
            embed.add_field(name="Emoji count", value=f"{len(ctx.guild.emojis)}", inline=False)
            embed.add_field(name="Verification level", value=f"{(str(ctx.guild.verification_level)).capitalize()}",
                            inline=False)
            embed.add_field(name="Created", value=f"{ctx.guild.created_at.strftime('%b %#d, %Y')}",
                            inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Server", icon_url=self.bot.user.avatar_url)
            """
            You can add a field with a full server avatar:

            embed.set_thumbnail(url=guild.avatar_url)
            embed.set_footer(icon_url=guild.avatar_url)
            """
            return await ctx.send(embed=embed)
        except:
            return await ctx.send("I can`t show information about this server.")


# Link to bot
def setup(bot):
    bot.add_cog(Server(bot))
