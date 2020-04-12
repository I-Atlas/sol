import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()  # load .env file
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
extensions = ['cogs.CommandEvents', 'cogs.AdminCommands', 'cogs.HelpCommands', 'cogs.MiscCommands']  # cogs
list_of_status = ['Hello there!', 'Workspace: Sol', 'Working on 2990WX', 'Events loop']  # list of activities


@tasks.loop(minutes=60)
async def change_status():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=list_of_status[random.randint(0, 3)]))


@bot.event
async def on_ready():
    print(f'{bot.user} is online!', '\nID:', bot.user.id, flush=True)
    change_status.start()


if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)  # load cogs

bot.run(os.getenv('TOKEN'))  # load token from .env file