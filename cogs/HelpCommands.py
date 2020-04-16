import platform
import asyncio
import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pages = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('- - - - -\nHelpCommands has been loaded!')

    async def fetchPage(self, selectedPage):
        emb = discord.Embed(title="help", colour=0xff0077)
        for j in self.pages[selectedPage]:
            emb.add_field(name=j['name'], value=j['value'])
        return emb

    async def sysR(self, msg):
        await msg.add_reaction("⬅️")
        await msg.add_reaction("➡️")
        await msg.add_reaction("❌")

    @commands.command()
    @commands.has_permissions()
    async def help(self, ctx):
        """test"""
        page = []
        n = 0
        curPage = 0
        for k, v in self.bot.all_commands.items():
            cmd = {"name": k, "value": v.help}
            page.append(cmd)
            if len(page) > 9:
                self.pages.append(page)
                page = []
        if len(page) > 0:
            self.pages.append(page)
        emb = await self.fetchPage(curPage)
        msg = await ctx.send(embed=emb)
        await self.sysR(msg)
        for i in self.pages[curPage]:
            emb.add_field(name=i['name'], value=i['value'])

        def check(r, u):
            return u.id == ctx.author.id

        leftBlock = True
        rightBlock = False if len(self.pages) != 1 else True
        while True:
            try:
                react, user = await self.bot.wait_for('reaction_add', check=check, timeout=120)
            except asyncio.TimeoutError:
                await msg.delete()
                break
            await react.remove(ctx.author)
            if react.emoji == "⬅️":
                if leftBlock:
                    continue
                rightBlock = False
                curPage -= 1
                emb = await self.fetchPage(curPage)
                await msg.edit(embed=emb)
                if curPage == 0:
                    leftBlock = True
                    continue
            elif react.emoji == "➡️":
                if rightBlock:
                    continue
                leftBlock = False
                curPage += 1
                emb = await self.fetchPage(curPage)
                await msg.edit(embed=emb)
                if curPage + 1 == len(self.pages):
                    rightBlock = True
                    continue
            elif react.emoji == "❌":
                await msg.delete()
                break

    @commands.command(name='stats', aliases=['st'])
    @commands.has_permissions()
    async def stats(self, ctx):
        """
        A command that displays bot stats.
        """
        number_of_servers = len(self.bot.guilds)
        number_of_members = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', color=ctx.author.color,
                              timestamp=ctx.message.created_at)

        embed.add_field(name='Python version', value=platform.python_version())
        embed.add_field(name='discord.py version', value=discord.__version__)
        embed.add_field(name='Total guilds', value=number_of_servers)
        embed.add_field(name='Total users', value=number_of_members)
        embed.add_field(name='Bot developers', value='<@271684584863825920>')

        embed.set_footer(text=f'Hello, world! | {self.bot.user.name}')
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommands(bot))
