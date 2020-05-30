# Imports
import discord
from discord.ext import commands


# Main Command Class
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "The bot's help command."
        self.usage = "help [category]"


# Link to bot
def setup(bot):
    bot.add_cog(Help(bot))
