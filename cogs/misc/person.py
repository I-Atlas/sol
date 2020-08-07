import discord
from discord.ext import commands


class Person(commands.Cog):
    """Person Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "User information"
        self.usage = "person [user]"

    @staticmethod
    def get_status(status):
        status = status.value
        if status == "online":
            return ":green_circle:  Online"
        elif status == "idle":
            return ":crescent_moon:  Idle"
        elif status == "do_not_disturb":
            return ":no_entry:  Do Not Disturb"
        elif status == "offline":
            return ":black_circle:  Offline"
        elif status == "invisible":
            return ":white_circle:  Invisible"

    @commands.command(name='person', aliases=['p'])
    @commands.has_permissions()
    async def person(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        try:
            embed = discord.Embed(color=member.color)

            embed.set_image(url=member.avatar_url)

            embed.add_field(name="Name", value=member)
            embed.add_field(name="Mention", value=member.mention)

            if not member.bot and not ctx.author:
                embed.add_field(name="Your Friend", value=f"{(str(member.is_friend)).capitalize()}")
            if not member.bot and member.activity:
                embed.add_field(name="Activity", value=member.activity)
            if member.bot:
                embed.add_field(name="Bot", value=member.bot)

            embed.add_field(name="Joined Discord", value=member.created_at.strftime('%b %d, %Y'))
            embed.add_field(name="Joined Server", value=member.joined_at.strftime('%b %d, %Y'))
            embed.add_field(name="Main Role", value=f"{member.top_role.mention}\n**Color:** {member.color}")
            embed.add_field(name="Status", value=self.get_status(member.status))
            embed.add_field(name="ID", value=member.id)

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Person", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        except Exception as error:
            embed = discord.Embed(title=f"Something went wrong: {error}.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Person", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Person(bot))
