import aiohttp
import discord
from discord.ext import commands


class Minecraft(commands.Cog):
    """Minecraft Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Get the status of or query a Minecraft server"
        self.usage = "minecraft [server IP address]"

    @commands.command(name='minecraft', aliases=['mc'])
    @commands.has_permissions()
    async def minecraft(self, ctx, *, ip=None):
        if not ip:
            embed = discord.Embed(title="Please specify a minecraft server IP address.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Minecraft", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://mcapi.us/server/status?ip={}'.format(ip)) as response:
                    data = await response.json()

                    if data['status'] == "success":
                        embed = discord.Embed(title=f'{ip}', color=ctx.author.color)

                        embed.set_image(url=f'https://mcapi.us/server/image?ip={ip}&theme=dark')

                        embed.add_field(name="Name", value=f'{data["server"]["name"]}')
                        embed.add_field(name="Motd", value=f'{data["motd"]}')
                        embed.add_field(name="Duration", value=f'{data["duration"]}')

                        embed.set_author(name=f" | Minecraft", icon_url=self.bot.user.avatar_url)
                        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

                        return await ctx.send(embed=embed)

                    elif data['status'] == "error":
                        embed = discord.Embed(title=f'{data["error"]}', color=ctx.author.color)

                        embed.set_author(name=f" | Minecraft", icon_url=self.bot.user.avatar_url)
                        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

                        return await ctx.send(embed=embed)

        except Exception as error:
            embed = discord.Embed(title=f"Something went wrong: {error}.",
                                  color=ctx.author.color)
            embed.set_author(name=f" | Minecraft", icon_url=self.bot.user.avatar_url)
            embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Minecraft(bot))
