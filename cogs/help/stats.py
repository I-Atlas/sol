# Imports
import os
import platform
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Dotenv
load_dotenv()


# Main Command Class
class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "A command that displays bot stats."
        self.usage = "stats"

    @commands.command(name='stats', aliases=['st'])
    @commands.has_permissions()
    async def stats(self, ctx):
        """
        A command that displays bot stats.
        """
        number_of_servers = len(self.bot.guilds)
        number_of_members = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', color=ctx.author.color,
                              timestamp=ctx.message.created_at)

        embed.add_field(name='Python version', value=platform.python_version())
        embed.add_field(name='discord.py version', value=discord.__version__)
        embed.add_field(name='Total guilds', value=number_of_servers)
        embed.add_field(name='Total users', value=number_of_members)
        embed.add_field(name='Bot developers', value=os.getenv('AUTHOR'))

        embed.set_footer(text=f'Hello, world! | {self.bot.user.name}')
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Stats(bot))
