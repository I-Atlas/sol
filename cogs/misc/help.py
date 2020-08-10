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
        self.usage = "help [category or command]"
        self.prefix = ">"

    @staticmethod
    def get_cogs(category):
        cogs = ""
        for cog in os.listdir(f"cogs/{category}"):
            if cog != "__pycache__":
                cogs = f"{cogs}, {cog[:-3]}"
        return f"``{cogs[2:]}``"

    @commands.command(name="help", aliases=["h", "info"])
    @commands.has_permissions()
    async def help(self, ctx, *, category=None):
        if not category:

            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name=":dart:  Fun Commands",
                            value=f"Use ``{self.prefix}help fun``", inline=False)
            embed.add_field(name=":crystal_ball:  Miscellaneous  Commands",
                            value=f"Use ``{self.prefix}help misc``", inline=False)
            embed.add_field(name=":crossed_swords:  Moderation Commands",
                            value=f"Use ``{self.prefix}help moderation``", inline=False)
            embed.add_field(name=":shield:  Owner Commands",
                            value=f"Use ``{self.prefix}help owner``", inline=False)

            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Help", icon_url=self.bot.user.avatar_url)

            await ctx.send(embed=embed)

        elif category == "fun":

            embed = discord.Embed(title=":dart:  Fun Commands", description=None, color=0xf17544)
            embed.add_field(name=f"The most interesting and unique commands out there.",
                            value=f"{self.get_cogs(category)}", inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Fun", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        elif category == "misc":

            embed = discord.Embed(title=":crystal_ball:  Miscellaneous Commands", description=None, color=0xab8cd5)
            embed.add_field(name=f"Commands that fit in no special category.",
                            value=f"{self.get_cogs(category)}", inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Misc", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        elif category == "moderation":

            embed = discord.Embed(title=":crossed_swords:  Moderation Commands", description=None, color=0xccd6dd)
            embed.add_field(name=f"Control the server with these commands.",
                            value=f"{self.get_cogs(category)}", inline=False)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f" | Moderation", icon_url=self.bot.user.avatar_url)

            return await ctx.send(embed=embed)

        elif category == "owner":

            embed = discord.Embed(title=":shield:  Owner Commands", description=None, color=0x50abeb)
            embed.add_field(name=f"Bot owner`s commands.",
                            value=f"{self.get_cogs(category)}", inline=False)
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

                            embed = discord.Embed(title=f"{cog_class.desc}",
                                                  description=f"``{self.prefix}{cog_class.usage}``**",
                                                  color=ctx.author.color)

                            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)
                            embed.set_author(name=f" | Help {category.capitalize()}", icon_url=self.bot.user.avatar_url)

                            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
