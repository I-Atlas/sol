# Imports
import platform
import discord
from discord.ext import commands


# Main Command Class
class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that displays bot stats"
        self.usage = "stats"

    @commands.command(name='stats', aliases=['st'])
    @commands.has_permissions()
    async def stats(self, ctx):
        number_of_servers = str(len(self.bot.guilds))
        number_of_members = str(len(set(self.bot.get_all_members())))
        author_id = '<@271684584863825920>'

        embed = discord.Embed(color=0xF52100)

        embed.set_image(url=self.bot.user.avatar_url)

        embed.add_field(name='Python version', value=platform.python_version())
        embed.add_field(name='discord.py version', value=discord.__version__)
        embed.add_field(name='Total guilds', value=number_of_servers)
        embed.add_field(name='Total users', value=number_of_members)
        embed.add_field(name='Bot developers', value=author_id)

        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
        embed.set_author(name=f" | Stats", icon_url=self.bot.user.avatar_url)

        return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Stats(bot))
