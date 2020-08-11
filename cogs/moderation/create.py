import random
import discord
from discord.ext import commands
from ..events.utils import Utils


class Create(commands.Cog):
    """Create Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour(random.randint(0, 0xFFFFFF))
        self.desc = "Creates new role on the server"
        self.usage = "create [role name]"

    @commands.command(name='create', aliases=['newrole', 'new'])
    @commands.has_permissions(manage_roles=True)
    async def create(self, ctx, *, text=None):
        if not text:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a role name.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        elif len(text) > 100:
            embed = await Utils(self.bot).embed(ctx, title="This role name is too long.",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        elif len(ctx.guild.roles) == 250:
            embed = await Utils(self.bot).embed(ctx,
                                                title="The maximum number of roles has been reached on this server",
                                                description="", color=0xDE6246)
            return await ctx.send(embed=embed)

        elif text.startswith("<@!"):
            text = self.bot.get_user(int(text.split("<@!")[1].split(">")[0])).name
        try:
            await ctx.guild.create_role(name=text, colour=self.color)

            embed = await Utils(self.bot).embed(ctx, title=f"Role ``{text}`` created!",
                                                description=f"**Color: ``{self.color}``**",
                                                color=self.color)
            return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Create(bot))
