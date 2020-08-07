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
        await ctx.message.delete()
        if not text:
            embed = discord.Embed(title=f"Please specify something to say.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Say", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        try:
            return await ctx.send(text)

        except Exception as error:
            embed = discord.Embed(title=f"Something went wrong: {error}.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Say", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Say(bot))