# Imports
import os
import discord
from discord.ext import commands


# Main Command Class
class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that reloads commands 🧠"
        self.usage = "reload [command]"

    @commands.command(name='reload', aliases=['rl'])
    @commands.is_owner()
    async def reload(self, ctx, command=None):
        if not command:
            return await ctx.send(embed="Please specify a command to reload.")
        try:
            self.bot.unload_extension(command)
            self.bot.load_extension(command)
        except:
            return await ctx.send(embed=f"Command {command.split('.')[2]} failed to reload.")
        else:
            embed = discord.Embed(title=f"The ``{command.split('.')[2]}`` command has been reloaded.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Reload", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Reload(bot))