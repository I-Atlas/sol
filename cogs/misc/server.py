import discord
from discord.ext import commands
from ..events.utils import Utils


class Server(commands.Cog):
    """Server Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Server information"
        self.usage = "server"

    @commands.command(name='server', aliases=['guild'])
    @commands.has_permissions()
    async def server(self, ctx):
        try:
            embed = discord.Embed(color=ctx.author.color)

            embed.set_image(url=ctx.guild.icon_url)

            embed.add_field(name="Information about ", value=f"{ctx.guild.name}")
            embed.add_field(name="Region", value=f"{(str(ctx.guild.region)).capitalize()}")
            embed.add_field(name="Server owner", value=f"{ctx.guild.owner.mention}")
            embed.add_field(name="Member quantity", value=f"{ctx.guild.member_count}")
            embed.add_field(name="Role quantity", value=f"{len(ctx.guild.roles)}")
            embed.add_field(name="Emoji quantity", value=f"{len(ctx.guild.emojis)}")
            embed.add_field(name="Verification level", value=f"{(str(ctx.guild.verification_level)).capitalize()}")
            embed.add_field(name="Created", value=f"{ctx.guild.created_at.strftime('%b %#d, %Y')}")
            embed.add_field(name="ID", value=ctx.guild.id)

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Server", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Server(bot))
