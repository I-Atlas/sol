# Imports
import discord
from discord.ext import commands


# Main Command Class
class Unload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that unloads commands 🧠"
        self.usage = "unload [cogs.category.command]"

    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, command=None):
        if not command:
            embed = discord.Embed(title="Please specify a command to unload.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Unload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        try:
            self.bot.unload_extension(command)

        except Exception as error:
            embed = discord.Embed(title=f"Command {command.split('.')[2]} failed to unload. Error: {error}.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Unload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"The ``{command.split('.')[2]}`` command has been unloaded.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Unload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Unload(bot))