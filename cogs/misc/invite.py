# Imports
import discord
from discord.ext import commands


# Main Command Class
class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sol`s invite link"
        self.usage = "stats"

    @commands.command(name='invite', aliases=['inv'])
    @commands.has_permissions()
    async def invite(self, ctx):
        embed = discord.Embed(title="Click here to invite Sol on your server.",
                              url=f"https://discordapp.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot",
                              color=ctx.author.color)
        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
        embed.set_author(name=f" | Invite", icon_url=self.bot.user.avatar_url)

        return await ctx.send(embed=embed)


# Link to bot
def setup(bot):
    bot.add_cog(Invite(bot))