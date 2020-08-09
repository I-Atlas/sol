import random
import asyncio
from discord.ext import commands

commands_tally = {}


class Events(commands.Cog):
    """Events Class"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name + ' was invoked incorrectly.')
        print(error)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:

            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1
            print(commands_tally)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name + ' was invoked sucessfully.')

    '''
    ONLY FOR FUN

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            pass
        elif random.randint(0, 100) > 50:  # probability of a bot
            msgs = []
            channel = ctx.channel
            words_list = ['no you don`t', 'hey girl', 'yell', 'why ya are so sad', 'you leave', ]

            async for msg in channel.history(limit=(random.randint(0, 500))):
                if msg.author == self.bot.user:
                    pass
                else:
                    msgs.append(msg)
            if len(msgs) == 0:

                msgs.append('u girl')  # If the bot does not find messages in the channel
            msg = random.choice(msgs)

            async with channel.typing():  # text input simulation
                author = msg.author.mention
                await asyncio.sleep(random.randint(2, 6))
                await ctx.channel.send(f'{author} {random.choice(words_list)}')'''


def setup(bot):
    bot.add_cog(Events(bot))
