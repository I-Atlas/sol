import aiohttp
import discord
from discord.ext import commands
from ..events.utils import Utils


class Minecraft(commands.Cog):
    """Minecraft Command Class"""

    def __init__(self, bot):
        self.bot = bot
        self.desc = "Get the status of or query a Minecraft server"
        self.usage = "minecraft [IP address]"

    @commands.command(name='minecraft', aliases=['mc'])
    @commands.has_permissions()
    async def minecraft(self, ctx, *, ip=None):
        if not ip:
            embed = await Utils(self.bot).embed(ctx, title="Please specify a minecraft server IP address.",
                                                description="", color=ctx.author.color)
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
                        embed.add_field(name="Duration", value=f'{(data["duration"])/1e+9} s')

                        embed.set_author(name=f" | Minecraft", icon_url=self.bot.user.avatar_url)
                        embed.set_footer(text=f" | Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

                        return await ctx.send(embed=embed)

                    elif data['status'] == "error":
                        embed = await Utils(self.bot).embed(ctx, title=f'{data["error"]}',
                                                            description="", color=ctx.author.color)
                        return await ctx.send(embed=embed)

        except Exception as error:
            error_handler = await Utils(self.bot).error(ctx, str(error))

            return await ctx.send(embed=error_handler)


def setup(bot):
    bot.add_cog(Minecraft(bot))
