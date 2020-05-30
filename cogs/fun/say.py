# Imports
import discord
from discord.ext import commands


# Main Command Class
class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Makes the bot say something"
        self.usage = "say [text]"

    @commands.command(name='say', aliases=['s'])
    @commands.has_permissions()
    async def say(self, ctx, *, text):
        await ctx.send(text)  # Sending a message to the channel you specified


# Link to bot
def setup(bot):
    bot.add_cog(Say(bot))