# Imports
import discord
from discord.ext import commands


# Main Command Class
class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that reloads commands 🧠"
        self.usage = "reload [cogs.category.command]"

    @commands.command(name='reload', aliases=['rl'])
    @commands.is_owner()
    async def reload(self, ctx, command=None):
        if not command:
            embed = discord.Embed(title="Please specify a command to reload.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Reload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        try:
            self.bot.unload_extension(command)
            self.bot.load_extension(command)

        except Exception as error:
            embed = discord.Embed(title=f"Command {command.split('.')[2]} failed to reload. Error: {error}.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Reload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"The ``{command.split('.')[2]}`` command has been reloaded.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Reload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Reload(bot))