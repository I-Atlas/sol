import os
import discord
from discord.ext import commands
import inspect
import importlib


class Help(commands.Cog):
    """Help Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "The Sol's help command"
        self.usage = "help [category]"

    @staticmethod
    def get_cogs(category):
        cogs = ""
        for cog in os.listdir(f"cogs/{category}"):
            if cog != "__pycache__":
                cogs = f"{cogs}, {cog[:-3]}"
        return f"``{cogs[2:]}``"

    @commands.command(name='help', aliases=['h, info'])
    @commands.has_permissions()
    async def help(self, ctx, *, category=None):
        prefix = "~"
        if not category:

            embed = discord.Embed(color=0x6F00CC)
            embed.add_field(name=":dart:  Fun Commands",
                            value=f"See the commands using ``{prefix}help fun``", inline=False)
            embed.add_field(name=":crystal_ball:  Miscellaneous  Commands",
                            value=f"See the commands using ``{prefix}help misc``", inline=False)
            embed.add_field(name=":crossed_swords:  Moderation Commands",
                            value=f"See the commands using ``{prefix}help moderation``", inline=False)
            embed.add_field(name=":shield:  Owner Commands",
                            value=f"See the commands using ``{prefix}help owner``", inline=False)

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Help", icon_url=self.bot.user.avatar_url)

            await ctx.send(embed=embed)

        elif category == "fun":

            embed = discord.Embed(title=":dart:  Fun Commands",
                                  description="The most interesting and unique commands out there.",
                                  color=0x21db56)
            embed.add_field(name="Commands", value=self.get_cogs(category), inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Fun", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        elif category == "misc":

            embed = discord.Embed(title=":crystal_ball:  Miscellaneous Commands",
                                  description="Commands that fit in no special category.",
                                  color=0x05d4e3)
            embed.add_field(name="Commands", value=self.get_cogs(category), inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Misc", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        elif category == "moderation":

            embed = discord.Embed(title=":crossed_swords:  Moderation Commands",
                                  description="Control the server with these commands.",
                                  color=0xe6a081)
            embed.add_field(name="Commands", value=self.get_cogs(category), inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Moderation", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        elif category == "owner":

            embed = discord.Embed(title=":shield:  Owner Commands",
                                  description="Bot owner`s commands.",
                                  color=0x8604f0)
            embed.add_field(name="Commands", value=self.get_cogs(category), inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Owner", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        for cog_folder in os.listdir("cogs"):
            for cog in os.listdir(f"cogs/{cog_folder}"):
                if f"{category}.py" == cog:
                    cog_module = importlib.import_module(f"cogs.{cog_folder}.{cog[:-3]}")
                    for name, obj in inspect.getmembers(cog_module):
                        if inspect.isclass(obj):
                            cog_class = obj(self.bot)

                            embed = discord.Embed(title=f"{category.capitalize()} Command",
                                                  description=f"**{cog_class.desc}**\n**Usage:** ``{cog_class.usage}``",
                                                  color=ctx.author.color)

                            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
                            embed.set_author(name=f" | Help", icon_url=self.bot.user.avatar_url)

                            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
