# Imports
import discord
from discord.ext import commands


# Main Command Class
class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sends a message on behalf of the bot."
        self.usage = "say [text]"

    @commands.command(name='say', aliases=['s'])
    @commands.has_permissions()
    async def say(self, ctx, *, text):
        if not text:
            await ctx.send("Please specify something to say.")
        try:
            await ctx.send(text)
        except:
            await ctx.send("I don't have permission to send messages.")


# Link to bot
def setup(bot):
    bot.add_cog(Say(bot))